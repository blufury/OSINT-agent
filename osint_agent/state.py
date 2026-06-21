"""LangGraph state schema for OSINTAgent."""

from __future__ import annotations

from typing import Annotated, Any
from pydantic import BaseModel, Field
from langgraph.graph.message import add_messages


class ToolResult(BaseModel):
    tool_name: str
    query: str
    raw_output: str
    error: str | None = None


class AgentState(BaseModel):
    """Central state passed between all nodes in the LangGraph agent loop."""

    # The seed entity being researched (org name, domain, GitHub handle, etc.)
    seed_entity: str

    # Structured plan produced by the query-planning node
    search_plan: list[dict[str, Any]] = Field(default_factory=list)

    # Raw results from each tool invocation
    tool_results: list[ToolResult] = Field(default_factory=list)

    # Structured facts extracted by spaCy (added in Week 4)
    extracted_facts: list[dict[str, Any]] = Field(default_factory=list)

    # Conflicts flagged between sources (added in Week 4)
    conflicts: list[dict[str, Any]] = Field(default_factory=list)

    # Final synthesized report in Markdown
    report: str = ""

    # LangChain messages for LLM calls (append-only via add_messages reducer)
    messages: Annotated[list, add_messages] = Field(default_factory=list)

    # Structured JSON log of every node execution for observability
    execution_log: list[dict[str, Any]] = Field(default_factory=list)
