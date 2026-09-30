# Research validation automation

**[View GitHub Actions runs](https://github.com/Gajarthan/SCAP-N0000-Research/actions/workflows/research-validation.yml)** · [Workflow source](../.github/workflows/research-validation.yml).

The workflow runs on every push to `main` involving research Markdown or the validator, on relevant pull requests, and manually. It runs on the GitHub-hosted `ubuntu-latest` runner, with read-only repository permissions.

### Rules

- **Broken relative links:** FAIL when the linked file or directory does not exist. External source URLs are not spidered, and fragment-anchor spelling is not validated.
- **Source provenance:** FAIL when any source card under `sources/records/` lacks a matching stable ID, publisher, reporting period, legal entity/scope, assurance status, original page/section, redistribution rights, external original/discovery URL, or SHA-256/archival status. Every source record must be registered in `sources/SOURCE-REGISTER.md`. For a discovery-only record, explicitly say the original is not located and label the link as secondary.
- **Quantitative citations:** FAIL when a research report has materially numeric financial claims without any source-record or external citation. Emit GitHub editorial WARNINGS for quantitative prose without a nearby link; these are not independent truth checks. Table rows and remote links still need expert review.
- **Mermaid diagrams:** FAIL on unclosed fences, missing chart headers, or Mermaid CLI syntax errors. Changed Mermaid blocks are rendered using official `@mermaid-js/mermaid-cli@11.4.1`. The smoke fixture ensures this stage is exercised in CI. GitHub-hosted Ubuntu currently disallows Chromium user namespaces; Mermaid CLI uses a dedicated Puppeteer config with --no-sandbox on disposable read-only GitHub-hosted runners. Do not use the config for a privileged server runner.

On regular pushes/PRs the checker scans changed Markdown files **plus the entire source register**. Manual `workflow_dispatch` has a `full_scan` checkbox to audit all existing Markdown, including older research. To run locally:

```bash
python3 -m unittest discover -s scripts/tests -p 'test_*.py' -v
python3 scripts/research_validate.py --base HEAD^ --mermaid-dir .scap-validation/mermaid
```

Check results in Actions → Research quality gates; errors fail the workflow and appear as annotations. **This does not itself block direct pushes or guarantee audited accounting correctness.** If you want rejected pull-request merges until validation passes, separately enable a protected-branch ruleset requiring the Research quality gates status.

Maintaining source declarations, periods, group-versus-parent distinctions, and actual original PDF access remains the responsibility of the research process. The validator never fabricates citations or replaces source verification.

## Additional automation (installed and verified 30 September 2026)

| Workflow | Scope | Example successful run |
|---|---|---|
| [Check English Tamil Sinhala parity](../.github/workflows/translation-consistency.yml) | All 20 topic triplets + companion chart counts + selected financial literals; other differences produce warnings | [Translation run](https://github.com/Gajarthan/SCAP-N0000-Research/actions/runs/36678792792) |
| [Monitor SCAP original filings](../.github/workflows/source-monitoring.yml) | Daily 09:13 Asia/Colombo; scans issuer annual/quarterly, CSE company profile and a third-party *discovery* catalog. Only issuer-specific, signature-verified new PDF URLs create deduplicated review Issues | [Source monitor](https://github.com/Gajarthan/SCAP-N0000-Research/actions/runs/36678508842) |
| [Reconcile SCAP financials](../.github/workflows/financial-reconciliation.yml) | On financial data/relevant report changes, verifies group PAT=NCI+owners, parent debt decomposition, owner-profit share, entity scope, fiscal dates and signed-audit distinction | [Reconciliation](https://github.com/Gajarthan/SCAP-N0000-Research/actions/runs/36678792793) |
| [Daily SCAP research snapshot](../.github/workflows/research-snapshots.yml) | Daily 00:17 Asia/Colombo; saves date-stamped Markdown/JSON/CSV as downloadable Action artifacts (90-day retention) | [Download from Artifacts](https://github.com/Gajarthan/SCAP-N0000-Research/actions/runs/36678792857) |

**Operational caveats:** The first monitor run fetched **3 of 4** configured indexes; the CSE profile URL returned **404**, and the accessible indexes exposed **zero new eligible original PDF links**. This is best-effort monitoring, **not exhaustive CSE filing surveillance**. Its output is an Issue for review, not a claim of audited evidence. Scheduled Actions can be delayed or dropped by GitHub. The financial ledger retains FY2026 as *subject to audit*; a verified final audited report should be added as a **separate period**, not silently overwrite the interim. See [machine-readable financial evidence](../data/financial-facts.json) and [monitored URL list](../sources/watchlist.json).

**Protection and publication:** These Actions report checks but cannot prohibit direct commits. To require successful checks before PR merge, separately configure a GitHub branch ruleset. Dated artifacts are not automatically published on the website.
