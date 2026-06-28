# OSINT Intelligence Report: Hugging Face

## 1. Executive Summary

Hugging Face is an open-source AI company founded in 2016 (originally as a consumer chatbot, later pivoted to ML developer infrastructure) that operates a widely-used "GitHub for machine learning" platform hosting models, datasets, and tools. As of its August 2023 Series D round, the company raised $235M at a $4.5 billion valuation, backed by major technology firms including Nvidia, Salesforce, Google, Intel, AMD, and IBM. The company maintains a US/Brooklyn operational presence alongside French corporate registration.

---

## 2. Key Findings

### Corporate Identity & History
- Founded in **2016** by **Clément Delangue, Julien Chaumond**, and others; pivoted from a teen-focused emotional chatbot to a developer-first AI infrastructure company. *(Source: tavily_search – businessmodelcanvastemplate.com, Instagram, kitrum.com)*
- Mission framed as advancing and **democratizing Natural Language Processing / open-source AI**. *(Source: tavily_search – Lux Capital)*
- Key product milestone: **2019 release of the Transformers library**, unifying access to BERT, GPT-2, and other models, driving major adoption. *(Source: tavily_search – businessmodelcanvastemplate.com)*
- French corporate registration: **CIN 822168043, France, Active, registered Aug 24, 2016**. *(Source: tavily_search – Tracxn)*

### Funding & Valuation
- **Series D: $235M on Aug 22–24, 2023**, at a **$4.5 billion** post-money valuation — roughly double its May 2022 valuation. *(Source: tavily_search – Reuters, TechCrunch, Tracxn)*
- Reported **22 institutional + 12 angel investors**. *(Source: tavily_search – Tracxn)*
- Series D investors include **Salesforce, Google, Nvidia, Intel, AMD, IBM, Sound Ventures, Amazon**. *(Source: tavily_search – Tracxn, TechCrunch)*
- Pre-round reporting (mid-2023) indicated a target valuation of ~$4 billion before the final $4.5B figure. *(Source: tavily_search – Reddit/MachineLearning)*

### Customers & Traction
- **2,000+ paying enterprise customers** as of June 2025, including **Intel, Pfizer, Bloomberg, eBay**. *(Source: tavily_search – Contrary Research)*
- Platform used by **50,000+ organizations** (including free-tier users). *(Source: tavily_search – Contrary Research/huggingface.co)*
- Reported scale: **1.5M+ models and 300,000+ datasets** by early 2026. *(Source: tavily_search – businessmodelcanvastemplate.com)*

### Digital Infrastructure
- Primary domain **huggingface.co** created **2016-07-18**, registrar **OVH SAS**, expires 2026-07-17; uses AWS name servers. *(Source: whois_lookup)*
- Secondary domain **huggingface.com** created **2015-03-14** (predates company founding), registrar OVH, country FR, expires 2029. *(Source: whois_lookup)*
- Both domains use AWS DNS and have transfer/delete locks enabled (standard protective configuration). *(Source: whois_lookup)*

### Competitive Landscape
- Positioned among/against **OpenAI (2015), Anthropic (2021), and Cohere (2019)** as comparable AI model providers. *(Source: tavily_search – Contrary Research)*

---

## 3. Confidence Notes

| Claim | Confidence | Rationale |
|-------|-----------|-----------|
| Series D $235M / $4.5B valuation (Aug 2023) | **High** | Corroborated by Reuters, TechCrunch, and Tracxn independently |
| Founded 2016, chatbot-to-platform pivot | **High** | Multiple sources agree; consistent with domain WHOIS (.co created 2016) |
| Founders (Delangue, Chaumond) | **High** | Named across multiple sources |
| Transformers library released 2019 | **Medium-High** | Single primary source but widely consistent with known history |
| Enterprise customer/model/dataset counts | **Medium** | Sourced largely from marketing-oriented/self-reported pages; some (1.5M models, "early 2026") appear projected/promotional |
| French corporate registration details | **Medium** | Single source (Tracxn); note inconsistency in stated HQ (Paris vs. Brooklyn) |

---

## 4. Potential Conflicts or Gaps

**Conflicts / Inconsistencies:**
- **Founding year discrepancy:** Most sources cite 2016, but one (businessmodelcanvastemplate.com) states "What started in 2017... Founded in 2016," creating internal ambiguity. WHOIS supports a 2015–2016 timeframe.
- **Headquarters ambiguity:** Sources variously describe the company as a "Brooklyn startup," "Paris (France)," and French-registered. Likely a US-operating company with French corporate/founder origins, but not definitively resolved.
- **Founder tenure claim:** kitrum.com states "as much as 15 years," which conflicts with a 2016 founding — likely promotional exaggeration.
- **Valuation pre-round reporting:** Reddit source cited ~$4B target vs. the finalized $4.5B.
- **CEO name spelling:** Appears as both "Delangue" and "Delaunge"/"Delaunge" (typo in source).

**Data Gaps:**
- **GitHub data unavailable** — both `github_lookup` calls failed (unauthenticated rate limit; no GITHUB_TOKEN). No repository, contributor, or open-source activity metrics obtained.
- **News data unavailable** — both `news_search` calls failed (NEWS_API_KEY not set). No coverage of 2024 developments or the queried **security vulnerability/incident** — this remains an open intelligence gap.
- No revenue figures confirmed (only a "100x annualized revenue" multiple reference).
- No post-2023 funding rounds identified; current 2025–2026 valuation/funding status unverified.
- Board of directors details referenced by Tracxn but not captured in results.

---

## 5. Sources Queried

| Tool | Status |
|------|--------|
| `tavily_search` (company overview) | ✅ Returned data |
| `tavily_search` (funding/valuation) | ✅ Returned data |
| `github_lookup` (huggingface) | ❌ Failed — rate limit, no GITHUB_TOKEN |
| `github_lookup` (transformers huggingface) | ❌ Failed — rate limit, no GITHUB_TOKEN |
| `news_search` (Hugging Face 2024) | ❌ Failed — NEWS_API_KEY not set |
| `news_search` (security vulnerability incident) | ❌ Failed — NEWS_API_KEY not set |
| `whois_lookup` (huggingface.co) | ✅ Returned data |
| `whois_lookup` (huggingface.com) | ✅ Returned data |

*Note: 4 of 8 tool queries failed due to missing API credentials/rate limits. Findings rely primarily on web search and WHOIS data; technical (GitHub) and current-events (news) verification could not be performed.*