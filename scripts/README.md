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
