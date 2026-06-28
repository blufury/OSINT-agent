"""GitHub REST API tool — public org/user/repo metadata."""

import os
from langchain_core.tools import tool


@tool
def github_lookup(entity: str) -> str:
    """Look up a GitHub organization or user and return public metadata.

    Args:
        entity: GitHub organization or username (e.g., 'microsoft' or 'torvalds').

    Returns:
        Formatted string with org/user metadata, top repos, and recent activity.
    """
    try:
        from github import Github, UnknownObjectException, RateLimitExceededException

        token = os.environ.get("GITHUB_TOKEN")
        g = Github(token, retry=0) if token else Github(retry=0)

        lines = []

        try:
            org = g.get_organization(entity)
            lines.append(f"Type: Organization")
            lines.append(f"Name: {org.name}")
            lines.append(f"Description: {org.description}")
            lines.append(f"Location: {org.location}")
            lines.append(f"Public repos: {org.public_repos}")
            lines.append(f"Followers: {org.followers}")
            lines.append(f"Created: {org.created_at}")
            lines.append(f"Blog: {org.blog}")
            lines.append(f"Email: {org.email}")

            repos = sorted(org.get_repos(), key=lambda r: r.stargazers_count, reverse=True)[:5]
            if repos:
                lines.append("\nTop repositories:")
                for repo in repos:
                    lines.append(f"  - {repo.name} ({repo.stargazers_count} stars): {repo.description}")

        except UnknownObjectException:
            user = g.get_user(entity)
            lines.append(f"Type: User")
            lines.append(f"Name: {user.name}")
            lines.append(f"Bio: {user.bio}")
            lines.append(f"Location: {user.location}")
            lines.append(f"Public repos: {user.public_repos}")
            lines.append(f"Followers: {user.followers}")
            lines.append(f"Created: {user.created_at}")

        return "\n".join(lines)

    except RateLimitExceededException:
        return "GitHub lookup skipped: unauthenticated rate limit exceeded. Set GITHUB_TOKEN to increase limits."
    except Exception as e:
        return f"GitHub lookup error: {e}"
