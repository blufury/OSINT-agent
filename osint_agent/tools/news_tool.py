"""NewsAPI tool — recent news articles about an entity."""

import os
from langchain_core.tools import tool


@tool
def news_search(query: str) -> str:
    """Search recent news articles about an entity using NewsAPI.

    Args:
        query: The entity or topic to search news for.

    Returns:
        Formatted string with article titles, sources, dates, and descriptions.
    """
    try:
        from newsapi import NewsApiClient

        client = NewsApiClient(api_key=os.environ["NEWS_API_KEY"])
        response = client.get_everything(
            q=query,
            language="en",
            sort_by="relevancy",
            page_size=5,
        )

        articles = response.get("articles", [])
        if not articles:
            return "No news articles found."

        results = []
        for a in articles:
            results.append(
                f"Title: {a.get('title', 'N/A')}\n"
                f"Source: {a.get('source', {}).get('name', 'N/A')}\n"
                f"Published: {a.get('publishedAt', 'N/A')}\n"
                f"Description: {a.get('description', 'N/A')}\n"
                f"URL: {a.get('url', 'N/A')}"
            )
        return "\n---\n".join(results)

    except KeyError:
        return "Error: NEWS_API_KEY not set in environment."
    except Exception as e:
        return f"NewsAPI error: {e}"
