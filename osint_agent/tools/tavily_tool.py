"""Tavily web search tool — primary search for LLM agents."""

import os
from langchain_core.tools import tool


@tool
def tavily_search(query: str) -> str:
    """Search the web for information about an entity using Tavily.

    Args:
        query: The search query string.

    Returns:
        A formatted string of search results with titles, URLs, and snippets.
    """
    try:
        from tavily import TavilyClient

        client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
        response = client.search(query=query, max_results=5, search_depth="basic")

        results = []
        for r in response.get("results", []):
            results.append(
                f"Title: {r.get('title', 'N/A')}\n"
                f"URL: {r.get('url', 'N/A')}\n"
                f"Content: {r.get('content', 'N/A')}\n"
            )
        return "\n---\n".join(results) if results else "No results found."

    except KeyError:
        return "Error: TAVILY_API_KEY not set in environment."
    except Exception as e:
        return f"Tavily search error: {e}"
