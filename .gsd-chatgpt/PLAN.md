# SCAP research — GSD-inspired execution plan

**Repository:** `Gajarthan/SCAP-N0000-Research` · **Plan created:** 2026-09-30 · **Status:** IN PROGRESS

## Goal and boundaries

Bring the existing **20 research topics × English/Tamil/Sinhala** to evidence-backed, internally consistent coverage. The existing [research queue](../RESEARCH-QUEUE.md) is authoritative for topic inventory, while the [source register](../sources/SOURCE-REGISTER.md) owns provenance. This plan coordinates incremental research; it does **not** certify financial results, automate ChatGPT, or install an external GSD runtime.

**Constraints:** Preserve existing research and source IDs. No invented figures, target prices, current trading signals, or inferred audit opinions. Distinguish SCAP Group, SCAP standalone Company, subsidiaries and non-controlling interests. Label FY2026 year-end interim **subject to audit** until the signed audited SCAP original is inspected. Never publish personal portfolio data, credentials or unlicensed full PDFs. No new GitHub Actions or hosted runners; the existing validator may continue running unchanged.

## Milestones and acceptance checks

| Milestone | State | Reviewable output | Acceptance criteria |
|---|---|---|---|
| M01 — Baseline and source truth | **OPEN** | Original SCAP FY2025/26 signed audit and June 2026 original; stable source records | Canonical issuer/CSE URLs, reporting date, scope, audit opinion, page numbers, exceptions and exact provenance recorded; archive only if redistribution permitted |
| M02 — Financial reconciliation | **OPEN** | Audited vs year-end-interim and June-quarter tie-out | Group/Company statements, owners vs NCI, parent debt/cash and prior revenue discrepancy reconciled with explicit units and page citations |
| M03 — Fundamental chapters | **IN PROGRESS / PARTIAL** | Evidence-backed updates to all 15 fundamental topics | Each language's canonical README has factual evidence, source links, status and diagram/table only when supported; no placeholder promoted to FILLED without checklist |
| M04 — Technical chapters | **BLOCKED ON MARKET DATA** | Five technical chapters with reproducible inputs | Lawful dated SCAP.N0000 OHLCV, adjustments, no-trade dates, indicator parameters and costs; otherwise explicitly OPEN, no fabricated signals |
| M05 — Multilingual and source-index QA | **IN PROGRESS** | English, Tamil, Sinhala reports + source indexes/log/queue | Matching numeric figures and periods, correct relative links, complete source metadata, no false audit status, existing validation green |

## One-topic-at-a-time sequence

The existing 13 template-era topics have research addendums, **not** 13 verified completions. Work in this order, skipping only a topic already fully reconciled on the latest branch:

1. Valuation — prior evidence bridge added, **PARTIAL**; integrate audit and complete owner/NCI/debt inputs.
2. Industry — regulator sector evidence added, **PARTIAL**; obtain company-period matched market comparisons.
3. Macroeconomics — obtain dated CBSL rates, inflation, FX and distinguish segment effects.
4. Management and governance — signed board/committee/related-party evidence and subsequent changes.
5. Corporate actions — date-scoped CSE announcement and legal-effective-event ledger.
6. Regulatory — entity-specific IRCSL/CBSL/SEC notices and compliance facts.
7. Scenarios and sensitivities — conditional verified inputs only.
8. Fundamental quantitative — reconciled consistent time series and metric definitions.
9. Price action — verified OHLCV prerequisite.
10. Trend and momentum — adjusted series and explicit indicator warm-up.
11. Volume and liquidity — dated volume/spread/no-trade evidence.
12. Patterns and indicators — reproducible rules and out-of-sample checks.
13. Quantitative and sentiment — event timestamps and look-ahead controls.

The other seven fundamental topics remain in the [queue](../RESEARCH-QUEUE.md) for later audit refresh; a topic is **FILLED** only when the queue's full checklist is satisfied.

## Standard slice: research → edit → verify

For **each** topic:

1. Read this plan, [STATE](STATE.md), [DECISIONS](DECISIONS.md), the current [queue](../RESEARCH-QUEUE.md), source register, relevant existing reports, and previous commit/PR status.
2. Write a compact research specification: question, legal entity, time period, source IDs, what is unknown, acceptance checks and rollback plan.
3. Obtain primary originals where accessible; compare with existing source cards. Mark unretrieved or inconsistent claims **OPEN**, not verified.
4. Edit **one focused topic** in English/Tamil/Sinhala, its relevant source record(s), three language source indexes, central research log and queue. Preserve stable IDs and numeric parity.
5. Run existing validation if an actual test runner is available; otherwise use existing CI run results and state precisely what was not executed. Verify source registration, links, Mermaid fences and commit.
6. Update STATE with verified SHA/PR, actual checks, blockers and the next bounded task. Open a draft PR; do not merge automatically.

**Definition of done:** Reviewable diff; all changed factual claims cited to original pages/sections; matching translations and figures; no unresolved validation errors; honest PARTIAL/FILLED status; existing CI success or explicit pending/failure record. A committed plan alone does not advance a research topic.

## Rollback

Use the topic's focused PR/commit to revert incorrect data; never rewrite audited figures without retaining the discrepancy and correction in the log. Stop the slice when primary sources cannot support it. Do not silently edit protected main or deploy anything.
