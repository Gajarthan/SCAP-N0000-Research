# SCAP Research Coverage & Fill Queue

[← Repository](README.md) · **English** · [தமிழ்](ta/RESEARCH-QUEUE.md) · [සිංහල](si/RESEARCH-QUEUE.md)

> **Audit date: 30 September 2026.** This is the maintenance tracker for all **20 research topics × 3 languages = 60 core guides**. It records *document completion*, not investment merit. Existing business and financial research is substantial but still requires a final-audit refresh; the other 18 topics are mainly generic templates. The repository is public.

**Current coverage:** 2 partially researched topics, 18 template-only topics, 0 fully source-reconciled topics. Six subject-level English/Tamil/Sinhala visual report files are present (three visual types in three languages: Business, Financial Statements, and Business SWOT; Business visuals contain 16 diagrams; Financial visuals contain 12 diagrams).

## Topic-by-topic status

| Topic | Status | Missing evidence / next step |
|---|---|---|
| [Business Analysis](01-Fundamental-Analysis/01-Business-Analysis/README.md) | **PARTIAL — source refresh** | 16 business visuals and SWOT exist; source refresh remains |
| [Financial Statements](01-Fundamental-Analysis/02-Financial-Statements/README.md) | **PARTIAL — source refresh** | 12 charts; final audited FY2026 and June quarter need tie-out |
| [Valuation](01-Fundamental-Analysis/03-Valuation/README.md) | **TEMPLATE — not filled** | Parent NAV / minorities / debt / audited inputs |
| [Industry](01-Fundamental-Analysis/04-Industry/README.md) | **TEMPLATE — not filled** | Insurance, NBFI, brokerage market structure |
| [Competitors](01-Fundamental-Analysis/05-Competitors/README.md) | **TEMPLATE — not filled** | Like-for-like peer metric comparisons |
| [Macroeconomics](01-Fundamental-Analysis/06-Macroeconomics/README.md) | **TEMPLATE — not filled** | Sri Lanka rates, FX, inflation and segment transmission |
| [Management & Governance](01-Fundamental-Analysis/07-Management-Governance/README.md) | **TEMPLATE — not filled** | Board changes, audit committees, related parties |
| [Risk](01-Fundamental-Analysis/08-Risk/README.md) | **TEMPLATE — not filled** | Parent refinancing, credit losses, insurer solvency |
| [Dividends](01-Fundamental-Analysis/09-Dividends/README.md) | **TEMPLATE — not filled** | Paid vs proposed; subsidiary cash vs parent payouts |
| [Shareholding](01-Fundamental-Analysis/10-Shareholding/README.md) | **TEMPLATE — not filled** | Current dated ownership, direct vs indirect stakes |
| [Corporate Actions](01-Fundamental-Analysis/11-Corporate-Actions/README.md) | **TEMPLATE — not filled** | CSE notices, rights, acquisitions and effective dates |
| [Forensic Accounting](01-Fundamental-Analysis/12-Forensic-Accounting/README.md) | **TEMPLATE — not filled** | Original-versus-vendor discrepancies; restatements |
| [Regulatory](01-Fundamental-Analysis/13-Regulatory/README.md) | **TEMPLATE — not filled** | Latest CBSL/IRCSL/SEC/CSE entity-specific notices |
| [Scenarios & Sensitivities](01-Fundamental-Analysis/14-Scenario-Analysis/README.md) | **TEMPLATE — not filled** | Conditional verified inputs, no unsupported probabilities |
| [Fundamental Quantitative](01-Fundamental-Analysis/15-Quantitative/README.md) | **TEMPLATE — not filled** | Period-consistent time series and robustness checks |
| [Price Action](02-Technical-Analysis/01-Price-Action/README.md) | **TEMPLATE — not filled** | CSE sourced timestamped OHLCV and corporate adjustments |
| [Trend & Momentum](02-Technical-Analysis/02-Trend-Momentum/README.md) | **TEMPLATE — not filled** | Indicators after verifiable OHLCV; avoid false signals |
| [Volume & Liquidity](02-Technical-Analysis/03-Volume-Liquidity/README.md) | **TEMPLATE — not filled** | No-trade days, turnover, bid/ask depth and slippage |
| [Patterns & Indicators](02-Technical-Analysis/04-Patterns-Indicators/README.md) | **TEMPLATE — not filled** | Reproducible rules, costs and out-of-sample checks |
| [Quantitative & Sentiment](02-Technical-Analysis/05-Quantitative-Sentiment/README.md) | **TEMPLATE — not filled** | Dated events, objective tests, no future leaks |

## Planned execution order

**Prerequisite (first run):** retrieve SCAP's *final FY2025/26 audited annual report* and *original quarter ended 30 June 2026*, read auditor opinion and reporting dates, reconcile older FY2026 interim values; update already populated Business/Financial reports and the source logs. If the originals cannot be accessed, mark **OPEN**; do not replace them with an aggregator.

1. [Shareholding](01-Fundamental-Analysis/10-Shareholding/README.md) — Current dated ownership, direct vs indirect stakes.
2. [Dividends](01-Fundamental-Analysis/09-Dividends/README.md) — Paid vs proposed; subsidiary cash vs parent payouts.
3. [Regulatory](01-Fundamental-Analysis/13-Regulatory/README.md) — Latest CBSL/IRCSL/SEC/CSE entity-specific notices.
4. [Risk](01-Fundamental-Analysis/08-Risk/README.md) — Parent refinancing, credit losses, insurer solvency.
5. [Corporate Actions](01-Fundamental-Analysis/11-Corporate-Actions/README.md) — CSE notices, rights, acquisitions and effective dates.
6. [Management & Governance](01-Fundamental-Analysis/07-Management-Governance/README.md) — Board changes, audit committees, related parties.
7. [Forensic Accounting](01-Fundamental-Analysis/12-Forensic-Accounting/README.md) — Original-versus-vendor discrepancies; restatements.
8. [Industry](01-Fundamental-Analysis/04-Industry/README.md) — Insurance, NBFI, brokerage market structure.
9. [Competitors](01-Fundamental-Analysis/05-Competitors/README.md) — Like-for-like peer metric comparisons.
10. [Macroeconomics](01-Fundamental-Analysis/06-Macroeconomics/README.md) — Sri Lanka rates, FX, inflation and segment transmission.
11. [Valuation](01-Fundamental-Analysis/03-Valuation/README.md) — Parent NAV / minorities / debt / audited inputs.
12. [Scenarios & Sensitivities](01-Fundamental-Analysis/14-Scenario-Analysis/README.md) — Conditional verified inputs, no unsupported probabilities.
13. [Fundamental Quantitative](01-Fundamental-Analysis/15-Quantitative/README.md) — Period-consistent time series and robustness checks.
14. [Price Action](02-Technical-Analysis/01-Price-Action/README.md) — CSE sourced timestamped OHLCV and corporate adjustments.
15. [Volume & Liquidity](02-Technical-Analysis/03-Volume-Liquidity/README.md) — No-trade days, turnover, bid/ask depth and slippage.
16. [Trend & Momentum](02-Technical-Analysis/02-Trend-Momentum/README.md) — Indicators after verifiable OHLCV; avoid false signals.
17. [Patterns & Indicators](02-Technical-Analysis/04-Patterns-Indicators/README.md) — Reproducible rules, costs and out-of-sample checks.
18. [Quantitative & Sentiment](02-Technical-Analysis/05-Quantitative-Sentiment/README.md) — Dated events, objective tests, no future leaks.

## What counts as a filled topic

- [ ] Each topic must include **dated, SCAP-specific evidence** from primary issuer/CSE/CBSL/IRCSL/SEC material (or explicitly labelled secondary corroboration), with **original URLs, dates, units and PDF pages** for key claims.
- [ ] Distinguish **SCAP Group, SCAP standalone parent, subsidiary and non-controlling interests**; never treat insurer gross written premiums, fund AUM or subsidiary cash as freely distributable parent income.
- [ ] Include **readable Markdown tables and real-data Mermaid diagrams/charts**; avoid invented price histories, ratios, annual values, profitability forecasts or unsupported trading indicators.
- [ ] Update **English, Tamil and Sinhala** within the same work session; use identical dates, figures and evidence statuses. Maintain working cross-links, language navigation, and matching visual report where data supports it.
- [ ] Update the **SOURCES.md** and **RESEARCH-LOG.md** for all three languages, mark disputed or missing figures OPEN, document any corrections, and verify the GitHub commit and local links.
- [ ] Only advance a row from TEMPLATE → PARTIAL → FILLED after checking source availability, provenance and reporting scope. **FILLED means researched to available evidence, not that every unknown has been resolved.**
- [ ] Do not commit personal portfolio/account information, publish GitHub Actions/workflows or use GitHub-hosted runners.

## Scheduled completion workflow

A ChatGPT task will check this tracker and GitHub's latest content on each run, research **one unfinished topic** (or a necessary source-reconciliation step), update the three language versions, verify its changes, and report the result. **No GitHub Actions or hidden workflows are created.** When all topics are filled to the above standard, it should report completion and stop making recurring edits.

## Sources and baseline

Primary starting points: [SCAP CSE annual FY2025](https://cdn.cse.lk/cmt/upload_report_file/1100_1764673838964.03.2025%20-%20Annual%20Report.pdf) · [SCAP 27 May 2026 year-end interim (subject to audit)](https://cdn.cse.lk/cmt/upload_report_file/1100_1779968696398.pdf) · [CSE](https://www.cse.lk/) · [CBSL](https://www.cbsl.gov.lk/) · [IRCSL](https://ircsl.gov.lk/) · [SEC](https://www.sec.gov.lk/). For technical analysis, fetch lawful, timestamped SCAP.N0000 market data; the repository currently contains **no verified historical OHLCV dataset**.

> **Reminder:** the SCAP March 2026 interim numbers are subject to audit; some older third-party FY2025 revenue and segment values were disputed or algebraically reconstructed. Source accuracy takes priority over making a dashboard appear complete.

**Next step status:** `SOURCE-CHECK — QUEUED` · **Last source-audit date:** `2026-09-30`.
