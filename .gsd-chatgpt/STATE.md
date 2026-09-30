# SCAP research — GSD-inspired state

- **As of:** 2026-09-30
- **Repository and active baseline:** `Gajarthan/SCAP-N0000-Research`, **`main`**.
- **GSD planning PR:** [#1](https://github.com/Gajarthan/SCAP-N0000-Research/pull/1) **MERGED** on 2026-09-30 at 08:22:02 UTC; merge commit `d9ee582d7c373a45e43d4575155706229d0f7bb0`. The old `docs/gsd-chatgpt-research-plan` branch is **not** the active baseline.
- **Validation at inspected baseline:** the GitHub Actions run for `d9ee582d7c373a45e43d4575155706229d0f7bb0` reported **completed / success**. This verifies that merge commit's existing checks, **not** this subsequent state update until its own CI finishes.
- **Current task:** synchronize the GSD plan and progress tracker with merged `main`; no new SCAP original financial evidence obtained by this metadata change.
- **Source register:** [23 source/evidence Markdown records](../sources/SOURCE-REGISTER.md); **0** verified original PDF binaries stored in this public repository.
- **20-topic baseline:** 7 historically PARTIAL and 13 historically TEMPLATE. Since that snapshot, the 13 template-era topics received short addendums, and **Valuation** and **Industry** received more substantive evidence updates. These are **PARTIAL**, not **FILLED**. The other 11 addendum-only topics have not been independently accepted as PARTIAL or FILLED under the queue's evidence checklist.
- **Outstanding originals:** SCAP FY2025/26 signed audited annual report and original quarter ended 30 June 2026 **OPEN**; parent maturities, current legal stakes/pledge releases and lawful timestamped SCAP.N0000 OHLCV also **OPEN**.
- **Current milestone:** M01 original-source reconciliation **BLOCKED / OPEN**; M02 financial reconciliation **OPEN**; M03 fundamental chapters **PARTIAL**; M04 technical chapters **BLOCKED on OHLCV**; M05 multilingual/source validation **IN PROGRESS**.
- **Next bounded research slice:** seek **SCAP-specific** FY2025/26 signed audit and 30 June 2026 original; if unavailable, record attempted issuer/CSE URLs, dates and retrieval limitations without claiming audited figures. Then reconcile Valuation and Industry original-vs-interim claims.
- **Task automation:** the prior hourly ChatGPT SCAP research task was previously disabled. A GSD skill or repository merge **does not restart it**; schedule only upon explicit request.
- **Execution policy:** the user explicitly requested **this GSD tracking update on main**. This is not a blanket authorization to push all future research to main, auto-merge, create GitHub workflows, or deploy. Future research slices follow [PLAN](PLAN.md) and [DECISIONS](DECISIONS.md).
- **Completion status:** GSD planning is merged; the 20-topic research program is **NOT COMPLETE**.

## GSD execution slice — 2026-09-30: SCAP issuer original retrieval

- **Inspected main:** `4f1ff99395e0e825e4fef8465ef1814972eafde9`; existing research validation run `36689412256` **completed/success**. **Open PRs at start: zero**.
- **Branch:** `research/scap-fy2026-original-discovery-20260930` (branched from inspected main). This is a **discovery-only** change, not a new audited financial reconciliation.
- **Source checks:** SCAP official annual and quarterly indexes, secondary Nanayojana catalogue, SCAP 1100 FY2026 interim, and separate issuer IDs Holdings 1075 and Life 364. Details in [SCAP issuer-index discovery record](../sources/records/SCAP-OFFICIAL-FINANCIALS-INDEX-2026.md).
- **Outcome:** SCAP original signed FY2026 audit and June 2026 original **NOT RETRIEVED**. Third-party catalogue listing alone is not an audited primary PDF. **23 source records, 0 PDFs archived; 9 PARTIAL, 11 addendum-only, 0 FILLED**.
- **Next:** obtain direct issuer-1100 CSE original PDF URLs; inspect auditor opinion and original June filing before reconciling numbers. If retrieval still fails, move to a separate, sourced topic in a future run rather than repeat unsupported figures.
- **Checks:** this branch's commit/PR and existing CI must be verified separately; the green baseline CI is **not** a branch test.
- **Automation:** hourly ChatGPT task is now enabled by explicit user request; no GitHub workflow created or changed.

## GSD execution slice — 2026-09-30: source-index count integrity

- **Inspected main:** `fc8fa67864db025326fd7fdb1a53943b5fe60581`; existing validation **completed/success**. Open PRs: **zero**.
- **Original-source check:** new public CSE issuer-1100 PDF-domain searches for signed SCAP FY2026 audit and June 2026 interim returned no matching originals. A Softlogic Holdings `1075` report and Softlogic Life `364` interim are **not** SCAP `1100` original financial statements; both SCAP originals remain **OPEN**. No new financial data introduced.
- **One bounded maintenance slice:** reconcile source-index references to **23 current Markdown source records / 0 original PDF binaries** in English, Tamil and Sinhala; preserve 20-record counts only as explicitly labelled historical snapshots. Record the user's later **direct-to-main authorization** in [DECISIONS](DECISIONS.md), superseding prior PR-only language for this repository.
- **Research statuses unchanged:** 9 PARTIAL, 11 addendum-only awaiting evidence, 0 FILLED. No audit opinion or interim figures upgraded.
- **Next task:** verify official SCAP issuer-1100 original filings if found; otherwise work on a distinct source-backed topic. Check the new commit's own CI before reporting it as passed.

## GSD substantive slice — 2026-09-30: Life share collateral and dividend bridge

- **Inspected main:** `2678da8f63c319753db9ed2366512dfcfebfad16`; existing CI success; open PRs zero. Direct-to-main permission D008 applies.
- **One topic:** Shareholding. Three language chapters now calculate historical NDB + DFCC Life-share pledges **81,049,704**, June 2026 Life holdings **158,714,972**, cross-date illustrative **51.07%**, residual **77,665,268** and conditional gross July dividend **LKR 841,189,351.60**. These do NOT establish 2026 security, actual parent cash, withholding or lender sweep.
- **Sources:** reused and extended three registered issuer records (FY2025 audited SCAP p.149, Life June interim note 19 p.19, Life June dividend notice). No new original PDFs, no new source IDs; corrected invalid Life PDF links in all three chapters.
- **Status:** Shareholding PARTIAL, overall 9 PARTIAL / 11 addendum-only / 0 FILLED; 23 evidence cards / 0 PDF binaries.
- **Next:** locate SCAP FY2026 signed audit and June original; obtain parent cash receipt and lender charge-release records for substantive cash-access tie-out. This slice is not a verified current pledge or dividend receipt.
