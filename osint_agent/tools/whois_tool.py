"""WHOIS tool — domain registration and ownership data."""

from langchain_core.tools import tool


@tool
def whois_lookup(domain: str) -> str:
    """Look up WHOIS registration data for a domain.

    Args:
        domain: The domain name to look up (e.g., 'microsoft.com').

    Returns:
        Formatted string with registrar, creation date, expiry, and name servers.
    """
    try:
        import whois

        w = whois.whois(domain)

        lines = [
            f"Domain: {w.domain_name}",
            f"Registrar: {w.registrar}",
            f"Created: {w.creation_date}",
            f"Expires: {w.expiration_date}",
            f"Updated: {w.updated_date}",
            f"Name servers: {w.name_servers}",
            f"Status: {w.status}",
            f"Emails: {w.emails}",
            f"Org: {w.org}",
            f"Country: {w.country}",
        ]
        return "\n".join(str(l) for l in lines)

    except Exception as e:
        return f"WHOIS lookup error: {e}"
