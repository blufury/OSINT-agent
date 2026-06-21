"""Basic tests for state schema and tool interface contracts."""

from osint_agent.state import AgentState, ToolResult


def test_agent_state_defaults():
    state = AgentState(seed_entity="Acme Corp")
    assert state.seed_entity == "Acme Corp"
    assert state.search_plan == []
    assert state.tool_results == []
    assert state.report == ""
    assert state.execution_log == []


def test_tool_result_model():
    r = ToolResult(tool_name="tavily_search", query="Acme Corp", raw_output="some result")
    assert r.error is None
    assert r.raw_output == "some result"


def test_tool_result_with_error():
    r = ToolResult(tool_name="whois_lookup", query="acme.com", raw_output="", error="timeout")
    assert r.error == "timeout"
