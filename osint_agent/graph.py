"""LangGraph agent graph for OSINTAgent."""

from __future__ import annotations

import json
import os
from datetime import datetime

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph
from langgraph.prebuilt import ToolNode

from osint_agent.state import AgentState, ToolResult
from osint_agent.tools import ALL_TOOLS

_PLAN_SYSTEM = """You are an OSINT research planner. Given a seed entity (an organization,
domain, or technical target), produce a JSON search plan listing the tools to invoke and the
exact query to pass to each one.

Available tools: tavily_search, github_lookup, news_search, whois_lookup

Respond ONLY with a JSON array. Each element must have:
  - "tool": one of the available tool names
  - "query": the exact string argument to pass
  - "rationale": one sentence explaining why this query is useful

Example for seed entity "Palantir Technologies":
[
  {"tool": "tavily_search", "query": "Palantir Technologies overview founding history", "rationale": "General background and founding context."},
  {"tool": "github_lookup", "query": "palantir", "rationale": "Check public GitHub org for open-source activity."},
  {"tool": "news_search", "query": "Palantir Technologies 2024", "rationale": "Recent news and controversies."},
  {"tool": "whois_lookup", "query": "palantir.com", "rationale": "Domain registration data and registrar."}
]"""

_SYNTH_SYSTEM = """You are an OSINT analyst. Synthesize the following raw tool results into a
structured Markdown intelligence report. Include:

1. **Executive Summary** (2-3 sentences)
2. **Key Findings** (categorized bullet points with source attribution)
3. **Confidence Notes** (high/medium/low confidence per major claim)
4. **Potential Conflicts or Gaps** (any contradictions or missing data)
5. **Sources** (list of all tools queried)

Be factual and concise. Do not hallucinate. If a source returned no data, note it."""


def _log(state: AgentState, node: str, detail: dict) -> list[dict]:
    entry = {"node": node, "timestamp": datetime.utcnow().isoformat(), **detail}
    return state.execution_log + [entry]


def plan_node(state: AgentState) -> dict:
    """Query-planning step: LLM decomposes seed entity into tool invocation plan."""
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content=_PLAN_SYSTEM),
        HumanMessage(content=f"Seed entity: {state.seed_entity}"),
    ]
    response = llm.invoke(messages)
    raw = response.content.strip()

    try:
        plan = json.loads(raw)
    except json.JSONDecodeError:
        # Strip markdown code fences if present
        import re
        match = re.search(r"```(?:json)?\s*([\s\S]+?)```", raw)
        plan = json.loads(match.group(1)) if match else []

    log = _log(state, "plan", {"plan_length": len(plan)})
    return {"search_plan": plan, "execution_log": log}


def collect_node(state: AgentState) -> dict:
    """Execute each planned tool call and collect raw results."""
    tool_map = {t.name: t for t in ALL_TOOLS}
    results = list(state.tool_results)

    for step in state.search_plan:
        tool_name = step.get("tool", "")
        query = step.get("query", "")
        tool = tool_map.get(tool_name)

        if tool is None:
            results.append(ToolResult(tool_name=tool_name, query=query, raw_output="", error=f"Unknown tool: {tool_name}"))
            continue

        try:
            output = tool.invoke(query)
            results.append(ToolResult(tool_name=tool_name, query=query, raw_output=str(output)))
        except Exception as e:
            results.append(ToolResult(tool_name=tool_name, query=query, raw_output="", error=str(e)))

    log = _log(state, "collect", {"tools_run": len(results)})
    return {"tool_results": results, "execution_log": log}


def synthesize_node(state: AgentState) -> dict:
    """LLM synthesizes raw tool results into a structured Markdown report."""
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    results_text = "\n\n".join(
        f"=== {r.tool_name} (query: {r.query}) ===\n"
        + (r.raw_output if not r.error else f"ERROR: {r.error}")
        for r in state.tool_results
    )

    messages = [
        SystemMessage(content=_SYNTH_SYSTEM),
        HumanMessage(content=f"Seed entity: {state.seed_entity}\n\nRaw results:\n{results_text}"),
    ]
    response = llm.invoke(messages)
    log = _log(state, "synthesize", {"report_chars": len(response.content)})
    return {"report": response.content, "execution_log": log}


def build_graph() -> StateGraph:
    graph = StateGraph(AgentState)

    graph.add_node("plan", plan_node)
    graph.add_node("collect", collect_node)
    graph.add_node("synthesize", synthesize_node)

    graph.set_entry_point("plan")
    graph.add_edge("plan", "collect")
    graph.add_edge("collect", "synthesize")
    graph.add_edge("synthesize", END)

    return graph.compile()
