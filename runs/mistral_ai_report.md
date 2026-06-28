# OSINT Intelligence Report: Mistral AI

## 1. Executive Summary

Mistral AI is a Paris-based artificial intelligence company founded in 2023 by three former researchers from Google DeepMind and Meta (Facebook AI), specializing in open-source large language models and enterprise AI solutions with a strong emphasis on European technological sovereignty. The company has rapidly become one of Europe's most prominent AI startups, raising billions across multiple funding rounds and reaching multi-billion-dollar valuations. Reporting across sources is broadly consistent on its founders and mission, though specific funding totals, valuations, and exact founding month vary by source and date.

---

## 2. Key Findings

### Corporate Profile
- **France-based AI startup** developing open-source LLMs, AI assistants, agents, and enterprise platforms; emphasizes European sovereignty, open-source accessibility, and multilingual/multimodal capabilities. *(startupintros.com, Tracxn, Clay)*
- Headquartered in **Paris, Île-de-France, France**. *(Tracxn, Clay)*
- Serves enterprises, developers, governments, and public institutions; deployment on-premises, cloud, or edge. *(startupintros.com)*
- Listed enterprise/partner logos include Stellantis, HSBC, SAP, CMA CGM, AXA, ESA, France Travail, Cisco, TotalEnergies, and the Austrian Academy of Sciences. *(mistral.ai/about)*

### Founders & Leadership
- **Arthur Mensch** (CEO) — former research scientist at Google DeepMind. *(Substack, polytechnique.edu)*
- **Guillaume Lample** (Scientific/Chief Scientist) — former Meta/Facebook AI research scientist; credited as a creator of Meta's LLaMA model. *(Substack, polytechnique.edu)*
- **Timothée Lacroix** — former Meta/Facebook AI research engineer; graduate of École Normale Supérieure. *(Substack, polytechnique.edu)*
- Mensch and Lample are both **École Polytechnique (X2011) alumni**. *(polytechnique.edu)*

### Founding Date
- **2023** founding year consistently reported; specific month varies: **February 2023** (polytechnique.edu) vs. **May 2023** (Substack). GitHub org created **2 May 2023**. *(multiple)*

### Funding & Valuation
- **Seed round:** €105M (~$113M), reported mid-2023; Index Ventures first invested in Seed round on 13 Jun 2023. *(Substack, Tracxn)*
- **Series A:** December 2023 — raised ~$385M, valuing company near $2B; BNP Paribas first invested 11 Dec 2023. *(polytechnique.edu, Tracxn)*
- **Series B:** 14 Mar 2024 — investors included Databricks, Salesforce, and Headline. *(Tracxn)*
- **Series C:** ~€1.7B led by **ASML**, valuing company at ~€11.7B; ASML became largest shareholder. *(LinkedIn/AIM)*
- **Conventional Debt round:** 30 Mar 2026 — ~$830M with HSBC participation. *(Tracxn)*
- **Rumored raise:** ~€3B at ~€20B valuation (reported June 2026, unconfirmed). *(TechCrunch)*
- **Strategic partnership** with Microsoft (Azure model integration). *(startupintros.com, Clay)*

### Technical/Open-Source Footprint
- GitHub organization **`mistralai`**: 24 public repos, 8,692 followers, created 2 May 2023. *(github_lookup)*
- Notable repositories: `mistral-inference` (10,824★), `mistral-vibe` (4,588★), `mistral-finetune` (3,094★), `cookbook` (2,279★), `mistral-common` (917★). *(github_lookup)*
- Named products/models: Mistral Medium 3, Codestral (code generation), Voxtral (referenced in site graphics). *(startupintros.com, Clay, mistral.ai)*

### Domain/Infrastructure
- **mistral.ai** registered **15 May 2019** (predates company founding), via Cloudflare; expires 2029; updated Oct 2025; Cloudflare name servers. *(whois_lookup)*

---

## 3. Confidence Notes

| Claim | Confidence | Rationale |
|-------|-----------|-----------|
| Founded 2023 in Paris, France | **High** | Corroborated by multiple independent sources |
| Three named founders & their prior employers | **High** | Consistent across Substack, polytechnique.edu, mistral.ai |
| Open-source LLM focus / European sovereignty mission | **High** | Multiple sources + GitHub evidence |
| Microsoft/Azure partnership | **Medium-High** | Reported by two aggregator sources, not primary-confirmed here |
| Exact founding month (Feb vs May) | **Low** | Direct source conflict |
| Specific valuation figures ($11.7B / €11.7B / €5.8B / $13.7B) | **Low-Medium** | Figures vary widely by source and date |
| Total funding raised ($3.05B vs $3.7B) | **Low-Medium** | Sources disagree |
| ASML-led Series C and top-shareholder status | **Medium** | Single source cluster (LinkedIn aggregation) |
| €3B/€20B raise | **Low** | Explicitly "rumored" per TechCrunch |

---

## 4. Potential Conflicts or Gaps

- **Founding month conflict:** February 2023 (École Polytechnique) vs. May 2023 (Substack). GitHub org creation (2 May 2023) supports the later date for online presence but does not settle legal incorporation date.
- **Valuation discrepancies:** Reported values include $11.7B / €11.7B (premieralts, LinkedIn), €5.8B (Clay), and $13.7B as of Sep 2025 (Tracxn). These likely reflect different points in time and currency conventions but are not reconcilable from the data provided.
- **Total funding discrepancy:** $3.05B across 8 rounds (Tracxn) vs. $3.7B across 6 rounds (premieralts).
- **Domain registration anomaly:** mistral.ai was registered in **2019**, four years before the company's 2023 founding — possibly acquired secondhand or pre-registered; origin unexplained.
- **Polytechnique source error:** States company raised funds "just eight years after its creation," which is internally inconsistent (likely "eight months") — reduces reliability of that source's numeric precision.
- **News data gap:** Both `news_search` queries failed (API key not set); no contemporaneous news coverage on 2024–2025 developments, regulation, or EU partnerships could be retrieved.
- **Missing data:** No location/registrant org in WHOIS (privacy-masked via Cloudflare); no official confirmation of current employee count beyond Tracxn's 1,143 (May 2026).
- **Forward-dated sources:** Several entries carry 2026 dates (TechCrunch, Tracxn, premieralts), which should be treated as projections or future-dated records relative to verification.

---

## 5. Sources Queried

| Tool | Status |
|------|--------|
| `tavily_search` (company overview/founders) | ✅ Returned data |
| `tavily_search` (funding/investors/valuation) | ✅ Returned data |
| `github_lookup` (mistralai) | ✅ Returned data |
| `news_search` (Mistral AI 2024 2025) | ❌ Failed — NEWS_API_KEY not set |
| `news_search` (regulation/EU partnership) | ❌ Failed — NEWS_API_KEY not set |
| `whois_lookup` (mistral.ai) | ✅ Returned data |

**Referenced web sources within tool results:** mistral.ai/about, startupintros.com, tracxn.com, offthegridxp.substack.com, polytechnique.edu, premieralts.com, clay.com, techcrunch.com, linkedin.com (Analytics India Magazine).

---
*Report compiled from raw tool output only. No external knowledge added. Unverified or single-source claims flagged accordingly.*