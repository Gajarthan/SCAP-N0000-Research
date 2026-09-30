# SCAP.N0000 — Investment Research

**🌐 GitHub Pages with Actions:** [Deployment workflow](.github/workflows/deploy-pages.yml) · [View Actions runs](https://github.com/Gajarthan/SCAP-N0000-Research/actions/workflows/deploy-pages.yml) · [Choose publishing source](https://github.com/Gajarthan/SCAP-N0000-Research/settings/pages). The GitHub Pages deployment workflow has completed successfully; public URL should be checked independently. [Website setup](docs/README.md).

**[🔎 Homepage source-trust disclosure](https://gajarthan.github.io/SCAP-N0000-Research/?view=overview)** — transparent evidence status in English, Tamil and Sinhala; **no unsupported numerical trust rating** until a published methodology and original-source verification exist.\n\n**[📚 Stored source records](sources/SOURCE-REGISTER.md)** — 23 Markdown source/evidence cards (including 2 discovery-only records); full original PDFs remain externally linked, not mirrored.

**[📋 Research coverage & scheduled fill queue — 20 topics / 3 languages](RESEARCH-QUEUE.md)**

**[📈 Financial Statement Analysis — 12 sourced charts, audited FY2025 vs interim FY2026](01-Fundamental-Analysis/02-Financial-Statements/VISUAL-REPORT.md)** ([தமிழ்](ta/01-Fundamental-Analysis/02-Financial-Statements/VISUAL-REPORT.md) · [සිංහල](si/01-Fundamental-Analysis/02-Financial-Statements/VISUAL-REPORT.md)).

**[🧭 Business SWOT: 4 quadrants + 12 evidence-led tests](01-Fundamental-Analysis/01-Business-Analysis/SWOT-ANALYSIS.md)**

**New: [SCAP Business Analysis — 16 evidence-backed editable Markdown visuals](01-Fundamental-Analysis/01-Business-Analysis/VISUAL-REPORT.md)** (also available in [Tamil](ta/01-Fundamental-Analysis/01-Business-Analysis/VISUAL-REPORT.md) and [Sinhala](si/01-Fundamental-Analysis/01-Business-Analysis/VISUAL-REPORT.md)).

**Softlogic Capital PLC** · Colombo Stock Exchange (CSE) · `SCAP.N0000`

A public, multilingual research notebook covering **company fundamentals** and **market technicals**. Documents are editable Markdown; visual reports use Mermaid.

**Languages:** [English](en/README.md) · [தமிழ்](ta/README.md) · [සිංහල](si/README.md)

> **Research status — 30 September 2026:** Educational research in progress, **not** investment advice. FY2025 audited issuer figures and FY2026 year-end interim figures have been added to the research, but the final FY2026 audited statements and later quarter still require source reconciliation; disputed third-party historical figures are marked. No verified current price, trading signal or SCAP valuation is presented.


## GitHub Actions research automation

These workflows run on **GitHub-hosted `ubuntu-latest`**; no self-hosted runner is required:

| Action | When | Result |
|---|---|---|
| [Research validation](.github/workflows/research-validation.yml) | Relevant Markdown commits/PRs | Checks links, citations, provenance and Mermaid syntax. |
| [Translation consistency](.github/workflows/translation-consistency.yml) | Research commits/PRs | Enforces 20 English/Tamil/Sinhala topic triplets, companion diagrams and designated shared financial figures. |
| [Source monitoring](.github/workflows/source-monitoring.yml) | Daily **09:13 Sri Lanka**; on demand | Best-effort watches issuer/CSE/public catalogs; opens **deduplicated review Issues** only for newly found, signature-verified SCAP PDFs. A catalogue listing alone never becomes audited evidence. |
| [Financial reconciliation](.github/workflows/financial-reconciliation.yml) | Financial data or applicable research changes | Checks group PAT attribution, parent debt sums, ratio, group/parent scope and audit/interim periods against [versioned figures](data/financial-facts.json). |
| [Research snapshots](.github/workflows/research-snapshots.yml) | Daily **00:17 Sri Lanka**, and on demand | Generates Markdown, JSON and CSV in a **90-day downloadable Actions artifact**; does not silently rewrite repository research. |
| [GitHub Pages](.github/workflows/deploy-pages.yml) | Website files in `docs/` change | Deploys the light-first public research website. |

[Workflow setup, check limitations and manual instructions](scripts/README.md). Scheduled runs are best-effort and may be delayed. **No script can independently certify an audit opinion, financial data accuracy or translation meaning.** Missing original FY2026 SCAP audited/June filings remain OPEN until actual verification.


## Start with one of two analysis branches

|  | Fundamental analysis · 15 subjects | Technical analysis · 5 subjects |
|---|---|---|
| **Question** | What does the business own, earn, risk and potentially justify in value? | What do dated market prices, volume and market conditions show? |
| **English** | **[Open fundamental analysis](01-Fundamental-Analysis/README.md)** | **[Open technical analysis](02-Technical-Analysis/README.md)** |
| **தமிழ்** | [அடிப்படைப் பகுப்பாய்வு](ta/01-Fundamental-Analysis/README.md) | [தொழில்நுட்பப் பகுப்பாய்வு](ta/02-Technical-Analysis/README.md) |
| **සිංහල** | [මූලික විශ්ලේෂණය](si/01-Fundamental-Analysis/README.md) | [තාක්ෂණික විශ්ලේෂණය](si/02-Technical-Analysis/README.md) |

**Every subject** has a guide in all three languages, including a research checklist, Mermaid workflow, SCAP-specific investigation and evidence table. The separate **portfolio** decision (position sizing, concentration, suitability) is a cross-cutting concern, not a claim about SCAP itself.

## Visual reports

| | English | தமிழ் | සිංහල |
|---|---|---|---|
| **Research dashboard** | [Open](reports/README.md) | [திறக்கவும்](ta/reports/README.md) | [විවෘත කරන්න](si/reports/README.md) |
| **Business map** | [Open](reports/business-model.md) | [திறக்கவும்](ta/reports/business-model.md) | [විවෘත කරන්න](si/reports/business-model.md) |
| **Financial charts¹** | [Open](reports/financial-pulse.md) | [திறக்கவும்](ta/reports/financial-pulse.md) | [විවෘත කරන්න](si/reports/financial-pulse.md) |
| **Risk map** | [Open](reports/risk-map.md) | [திறக்கவும்](ta/reports/risk-map.md) | [විවෘත කරන්න](si/reports/risk-map.md) |
| **Research roadmap** | [Open](reports/research-roadmap.md) | [திறக்கவும்](ta/reports/research-roadmap.md) | [විවෘත කරන්න](si/reports/research-roadmap.md) |

¹ **Provisional data only:** the financial charts visualize a prior third-party snapshot, not independently verified financial results.

## Supporting evidence and earlier research

These original notes are **preserved at their existing paths** to avoid breaking references. The two analysis branches above are the **primary navigation**.

<details>
<summary>Open earlier company notes, research methodology and sources</summary>

| Earlier document | Link |
|---|---|
| Company and ownership | [01 · Business and ownership](01-business-and-ownership.md) |
| How SCAP earns money | [02 · Revenue model](02-how-it-makes-money.md) |
| Competition | [03 · Competitors](03-competition.md) |
| Advantage hypotheses | [04 · Competitive advantage](04-competitive-advantage.md) |
| Risk questions | [05 · Risk register](05-risks-and-questions.md) |
| Preliminary financial figures | [06 · Financial snapshot](06-financial-snapshot.md) |
| Pre-purchase diligence | [07 · Reading checklist](07-reading-checklist.md) |
| Business-analysis method | [Guide](guides/01-business-analysis-method.md) |
| Reading group and parent financials | [Guide](guides/02-how-to-read-the-financials.md) |
| Evidence quality rules | [Research standards](guides/03-research-standards.md) |
| Reusable company checklist | [Template](templates/company-business-analysis.md) |

</details>

**Source material:** [Sources and provenance](SOURCES.md) · [Dated research log](RESEARCH-LOG.md) · [CSE](https://www.cse.lk/)

## How to maintain the project

1. Update the relevant English topic first; keep its Tamil and Sinhala equivalents aligned.
2. Attach a source URL, reporting period, original document page, units and **group vs. parent vs. subsidiary** scope to every material claim.
3. Record revisions in the relevant language's research log: [English](RESEARCH-LOG.md) · [தமிழ்](ta/RESEARCH-LOG.md) · [සිංහල](si/RESEARCH-LOG.md).
4. Mark missing or conflicting information **OPEN**. Do not present secondary data as audited, an old shareholding as current, or historical technical patterns as predictions.
5. Keep private brokerage accounts, personal positions and trade receipts **out of this public repository**.

GitHub Actions are used for website deployment, research validation, trilingual consistency, source monitoring, financial reconciliation and downloadable daily snapshots.
