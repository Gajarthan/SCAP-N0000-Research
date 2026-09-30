# SCAP Research — public website

**Live site:** https://scap-public-research.thisanthan02.workers.dev/

**Source of truth:** This public repository, `main` branch. The site uses the Markdown reports and source cards under the existing folders; it does not maintain another copy of those detailed analyses.

## Features

- Responsive editorial dashboard, historical FY2025/FY2026 comparison and owner-versus-minority profit chart.
- Searchable 15-subject fundamental and 5-subject technical research library.
- English / தமிழ் / සිංහල language navigation.
- In-browser Markdown reader with sanitized HTML and Mermaid visualization support, loading the latest public research directly from GitHub when opened.
- Live topic statuses from `RESEARCH-QUEUE.md` and evidence cards from `sources/SOURCE-REGISTER.md`.
- Dark and light themes. No visitor login or brokerage integration.

## Deployment (verified 30 September 2026)

The live site is **served through a Cloudflare Worker** named `scap-public-research` on the connected account's `thisanthan02.workers.dev` subdomain. The script is preserved at [site-hosting/cloudflare-worker.js](../site-hosting/cloudflare-worker.js).

This Worker proxies **only** the five static site assets from the public GitHub `docs/` directory, with a short cache. Detailed reports are fetched by the client's browser from GitHub's public raw Markdown endpoints and rendered with the pinned marked, DOMPurify and Mermaid libraries from jsDelivr. A Cloudflare Browser Rendering check verified the live homepage and the Tamil 20-topic library on 30 September 2026. Other individual article views were not browser-verified during that check because the Browser Rendering service returned a rate-limit error.

**No custom GitHub Actions, workflow YAML, GitHub-hosted runner or build service was created.** Cloudflare Worker request usage may be subject to the connected account's plan and limits.

## Optional GitHub Pages deployment

The same static files are ready for GitHub Pages if wanted:

1. Open [repository Settings → Pages](https://github.com/Gajarthan/SCAP-N0000-Research/settings/pages).
2. Select **Deploy from a branch** → **main** → **/docs** → **Save**.
3. GitHub's expected project URL is `https://gajarthan.github.io/SCAP-N0000-Research/`, **but Pages is not currently verified as enabled**.

GitHub Pages internally runs a GitHub-managed Actions deployment, even with branch-based publishing. This is different from the deployed Cloudflare Worker, which requires no GitHub Actions.

## Evidence and limits

- Figures on the homepage are historical, sourced to the repository's earlier SCAP financial analysis. FY2025 is from audited comparative statements. FY2026 figures come from the **27 May 2026 interim**, and are **subject to audit**. The final FY2026 audited report and later quarter may revise them.
- The source archive holds Markdown provenance records and publisher URLs; the original PDF documents have **not** been mirrored as files.
- Site visitors do not log in; only a local theme preference may be stored.
- Hosting and third-party CDN availability can affect report rendering; every report has a link back to the canonical GitHub file.
