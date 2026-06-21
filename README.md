# OSINT-agent
OSINTAgent is an agentic system that takes a seed entity (an organization, domain, or technical target), autonomously queries multiple public data sources, resolves conflicts between them, and produces a structured intelligence report with per-fact confidence ratings.

# PROBLEM & MOTIVATION
Open-source intelligence gathering is a time-intensive process that requires a researcher to manually
query multiple sources, reconcile conflicting information, and synthesize findings into a coherent
picture. This problem is directly relevant in defense contractor, cybersecurity, and compliance contexts
where rapid, sourced research on organizations or technical entities is routinely needed. The agentic
framing is well-suited here because the search strategy itself must adapt based on what is found —
discovering a GitHub organization, for example, should trigger a follow-on contributor and repository
analysis that was not planned in advance.
