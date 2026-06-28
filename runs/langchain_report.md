# OSINT Intelligence Report: LangChain

## 1. Executive Summary

LangChain is a U.S.-based (San Francisco) software company founded circa 2022–2023 that develops an open-source orchestration framework for building, testing, and deploying LLM-powered applications and AI agents. As of October 20, 2025, the company reached unicorn status with a $125M Series B round at a $1.25B valuation, and its tools are reportedly in use by major enterprises including Cisco, Cloudflare, Workday, and ServiceNow. The company maintains a prominent open-source presence, with its flagship repository exceeding 140,000 GitHub stars.

---

## 2. Key Findings

### Corporate & Funding
- **Series B round:** $125M raised on Oct 20, 2025, at a $1.25B post-money valuation, achieving unicorn status. *(Fortune; Tracxn)*
- **Total funding:** Reported at ~$260M across rounds. *(Tracxn)*
- **Investors:** 11 participated in the latest round; named backers include Sapphire Ventures and IVP (plus 13+ others). *(Tracxn)*
- **Founded:** 2022 per Tracxn; GitHub organization created March 2, 2023. *(Tracxn; GitHub)*
- **Headquarters:** San Francisco, United States. *(Tracxn; GitHub)*
- **Investor thesis:** Positioned as potential foundational AI infrastructure, compared to CrowdStrike and Datadog. *(Fortune)*

### Product & Technology
- **Core framework:** Open-source orchestration framework for LLM application development, available in Python and JavaScript. *(IBM; LangChain docs)*
- **Capabilities:** Supports chatbots, intelligent search, Q&A, summarization, RAG (Retrieval-Augmented Generation), and AI agents. *(IBM; lakeFS)*
- **Product ecosystem:**
  - **LangChain** – core agent/application framework. *(LangChain docs)*
  - **LangGraph** – framework for durable execution and multi-agent systems (35,954 stars). *(LangChain docs; GitHub)*
  - **LangSmith** – unified developer platform for building, testing, and monitoring LLM apps. *(LangChain docs)*
- **Model integrations:** Connects to OpenAI, Anthropic, Google, Hugging Face, and others. *(LangChain docs; IBM)*

### Customers
- Named enterprise users: Cisco, Replit, Clay, Cloudflare, Workday, ServiceNow. *(Fortune)*

### Digital Footprint
- **Primary domain:** langchain.com, registered Dec 3, 2019 via GoDaddy; expires Dec 2029; uses Google Cloud name servers. *(WHOIS)*
- **GitHub org (langchain-ai):** 248 public repos, 20,226 followers, created March 2, 2023. *(GitHub)*
- **Flagship repo (langchain):** 140,400 stars, described as "The agent engineering platform." *(GitHub)*
- **Other notable repos:** deepagents (25,226 stars), langchainjs (17,863 stars), open_deep_research (11,836 stars). *(GitHub)*
- **Contact:** support@langchain.dev; blog at langchain.com. *(GitHub)*

---

## 3. Confidence Notes

| Claim | Confidence | Rationale |
|-------|-----------|-----------|
| $125M Series B at $1.25B valuation (Oct 2025) | **High** | Corroborated by Fortune and Tracxn |
| Open-source LLM/agent framework with Python & JS libraries | **High** | Multiple independent sources (IBM, official docs, lakeFS) |
| Enterprise customer list | **Medium** | Single source (Fortune); not independently verified |
| Total funding ~$260M | **Medium** | Single source (Tracxn); not cross-confirmed |
| Founding year (2022 vs. 2023) | **Medium** | Tracxn states 2022; GitHub org created 2023 — see conflicts |
| GitHub metrics | **High** | Direct API lookup |
| Domain registration details | **High** | Direct WHOIS lookup |

---

## 4. Potential Conflicts or Gaps

- **Founding date discrepancy:** Tracxn lists the company founding year as **2022**, while the GitHub organization was created **March 2, 2023**. The langchain.com domain predates both (registered **2019**), possibly by a prior owner or earlier registration. This warrants clarification.
- **Total funding ambiguity:** Tracxn cites $260M total funding, but only the $125M Series B is detailed. The composition of earlier rounds (Seed/Series A) is not captured in the available data.
- **Missing news coverage:** Both `news_search` queries failed (NEWS_API_KEY not set), leaving a gap in recent partnership/product-launch reporting.
- **langchain.dev WHOIS:** Returned no data despite being used as the support email domain — registration details unverified.
- **Unverified customer claims:** Enterprise adoption (Cisco, Cloudflare, etc.) stems solely from a company-sourced Fortune article and may reflect promotional framing.
- **Founder/leadership data:** No founder names, team size, or executive details were returned by any source.
- **GitHub "langchain" user:** A separate user account (created 2018, 0 repos, 48 followers) is unrelated to the company org and should not be conflated.

---

## 5. Sources Queried

| Tool | Query | Status |
|------|-------|--------|
| tavily_search | LangChain company overview, founding, funding | ✅ Returned data |
| tavily_search | LangChain framework architecture, features, LLM integration | ✅ Returned data |
| github_lookup | langchain-ai (organization) | ✅ Returned data |
| github_lookup | langchain (user) | ✅ Returned data (unrelated account) |
| news_search | LangChain 2024 funding partnerships | ❌ Failed — NEWS_API_KEY not set |
| news_search | LangChain LangSmith LangGraph product launch | ❌ Failed — NEWS_API_KEY not set |
| whois_lookup | langchain.com | ✅ Returned data |
| whois_lookup | langchain.dev | ❌ No data returned |

*Referenced publications within search results: Fortune, Tracxn, PitchBook, Crunchbase, IBM, Contrary Research, lakeFS, Medium, DataCamp/YouTube.*