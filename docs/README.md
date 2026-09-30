# SCAP Research — GitHub Pages via GitHub Actions

**Repository:** [Gajarthan/SCAP-N0000-Research](https://github.com/Gajarthan/SCAP-N0000-Research)  
**Expected Pages URL, subject to live verification:** https://gajarthan.github.io/SCAP-N0000-Research/

## Current configuration

As of 30 September 2026 the public repository has a GitHub Pages site enabled (`has_pages = true`), and all static site files are committed in `main/docs`. A dedicated workflow is now stored at [`.github/workflows/deploy-pages.yml`](../.github/workflows/deploy-pages.yml). A successful publishing run and the actual public URL must still be confirmed before declaring the site live.

## Run it with GitHub Actions

1. Open [Settings → Pages](https://github.com/Gajarthan/SCAP-N0000-Research/settings/pages) and make sure **Build and deployment → Source = GitHub Actions**, not **Deploy from a branch**.
2. Open [Actions → Publish SCAP Research website](https://github.com/Gajarthan/SCAP-N0000-Research/actions/workflows/deploy-pages.yml). Select **Run workflow → main → Run workflow** if an automatic run has not started.
3. Ensure an **online self-hosted Linux Actions runner** is assigned to this repository with labels `self-hosted` and `linux`. Check [Settings → Actions → Runners](https://github.com/Gajarthan/SCAP-N0000-Research/settings/actions/runners). If no matching runner is available, the job remains queued; it does not switch to a GitHub-hosted runner.
4. Verify the run: **Check out → Check website files → Configure Pages → Upload artifact → Deploy**. Then open the reported deployment URL in Settings → Pages.

The workflow triggers automatically on pushes to `main` that change `docs/**` or the workflow file itself, and supports manual `workflow_dispatch`. Research-only Markdown commits outside `docs/` do not trigger a deployment: the website fetches those reports directly from the public GitHub `main` branch when opened.

GitHub's official recommended Pages actions are `actions/checkout`, `actions/configure-pages@v5`, `actions/upload-pages-artifact@v4` and `actions/deploy-pages@v4`, with permissions `contents: read`, `pages: write`, and `id-token: write`. The workflow uploads only `docs/` as the site artifact; it does not publish private or unrelated repository files.

## Ready website files

- [index.html](index.html) — responsive multilingual research homepage.
- [assets/site.css](assets/site.css) — accessible dark/light website layout.
- [assets/config.js](assets/config.js) — 20 topics, English / தமிழ் / සිංහල labels.
- [assets/app.js](assets/app.js) — topic search, financial comparisons, Markdown reader and Mermaid diagrams.
- [assets/favicon.svg](assets/favicon.svg) — project icon.
- `.nojekyll` — disables unnecessary Jekyll processing.

## Data and security

The original research is maintained in the three-language Markdown folders and `sources/` in the same repository. The site reads those public files from GitHub raw URLs and includes links to original publishers. Source records should not be mistaken for stored original PDF binaries.

**Financial caveat:** FY2025 audited and FY2026 year-end **interim (subject to audit)** are different evidence classes. Financial figures are historical, not live prices or buy/sell instructions. Do not disclose personal trading credentials or customer data in the repository.

## Verify publishing

- [x] Static website files committed in `main/docs`.
- [x] Pages site is enabled at the repository level.
- [x] GitHub Pages Actions workflow authored for self-hosted Linux runner.
- [ ] Pages publishing source is **GitHub Actions** (requires confirmation in Settings).
- [ ] Matching self-hosted Linux runner is available and online.
- [ ] At least one deployment run succeeds.
- [ ] The published URL is checked in English, Tamil and Sinhala with Markdown and Mermaid reports.

**If the setup workflow fails at Configure GitHub Pages:** ensure the Pages source is **GitHub Actions**. `GITHUB_TOKEN` alone cannot be used by `configure-pages` to enable a previously disabled Pages site using its optional `enablement` input; a separately privileged token is required. The repository-level Pages flag was already enabled during this setup.
