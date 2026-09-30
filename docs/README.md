# SCAP Research — GitHub Pages

**Publishing target:** GitHub Pages for [Gajarthan/SCAP-N0000-Research](https://github.com/Gajarthan/SCAP-N0000-Research).

**Status checked on 30 September 2026:** the repository is public and the website files are already committed under main → /docs. The GitHub repository currently has **has_pages = false**. Publishing is **not enabled or live yet**.

## Enable GitHub Pages

1. Open [Settings → Pages](https://github.com/Gajarthan/SCAP-N0000-Research/settings/pages) while signed in with repository administrator permissions.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Choose branch **main** and folder **/docs**.
4. Click **Save**.
5. Once GitHub confirms publication, open its website URL and check the homepage, all three languages, charts and original-source links.

**Expected URL after enabling, not yet confirmed live:** https://gajarthan.github.io/SCAP-N0000-Research/

GitHub Pages runs a **GitHub-managed internal Actions deployment** even for branch-based publishing. There are **no custom GitHub Actions workflow YAML files** in this repository, and you do not need to create any.

## Files ready to publish

- [index.html](index.html) — accessible, responsive public dashboard.
- [assets/site.css](assets/site.css) — dark/light layout and mobile navigation.
- [assets/config.js](assets/config.js) — all 20 subjects, English / தமிழ் / සිංහල labels.
- [assets/app.js](assets/app.js) — report library, financial comparisons, Markdown reader and Mermaid rendering.
- [assets/favicon.svg](assets/favicon.svg) — project icon.
- .nojekyll — skip Jekyll processing.

The website uses the existing Markdown reports and source records from this same public repository as the authoritative research. It fetches readable Markdown on main from raw.githubusercontent.com and reads the current research-queue and source-register files on site load. A GitHub fallback opens the original report when CDN dependencies are unavailable.

## Evidence limits

The homepage FY2025 figures come from audited issuer statements; FY2026 figures are from the 27 May 2026 year-end **interim, subject to audit**, not verified final audited statements. This is not live pricing or investment advice. The public source register holds Markdown provenance records, not mirrored complete original PDFs.

## Publication checklist

- [x] Site source code committed to main/docs.
- [x] Relative site asset links suitable for GitHub Pages subdirectory.
- [x] Canonical URL now points to the proposed GitHub Pages URL.
- [ ] Enable Pages using **main → /docs** in GitHub Settings.
- [ ] Confirm GitHub displays the published URL.
- [ ] Check Tamil, Sinhala and English reports plus Mermaid diagrams.
- [ ] Confirm the GitHub repository's has_pages property is true.

The connected GitHub tools used in this chat can commit website files, but currently do **not** provide a GitHub Pages settings/write action.