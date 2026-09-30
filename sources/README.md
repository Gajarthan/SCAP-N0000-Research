# SCAP Research Source Archive

**[Browse the stable-ID source register](SOURCE-REGISTER.md)** · [Research completion queue](../RESEARCH-QUEUE.md) · [English references](../SOURCES.md) · [தமிழ் ஆதாரங்கள்](../ta/SOURCES.md) · [සිංහල මූලාශ්‍ර](../si/SOURCES.md)

This `sources/` directory is the source-of-record **provenance archive** for the public [SCAP.N0000 research repository](../README.md).

### What's stored here now

- **20 source/evidence records**, each saved as a Markdown file in `sources/records/`, with original URLs, publisher, period, entity, assurance status, page/section references, key facts and outstanding checks.
- One central **[SOURCE-REGISTER.md](SOURCE-REGISTER.md)** with stable IDs for use in English, Tamil and Sinhala.
- **No raw PDFs or full web articles stored yet.** Original document links are retained; a source's being publicly accessible is not itself proof that reposting a full copy in a public GitHub repository is permitted. This directory does not assert that its source documents have been newly downloaded or independently reaudited.


### 30 September 2026 follow-up

Seven further provenance cards have been saved covering SCAP FY2026 annual and June interim *catalogue-only* leads; the Life 30 June 2026 shareholder register and Life Rs 5.30 dividend announcement; Union Assurance 2025 insurer CAR; CBSL March 2026 finance-company sector CAR; and a Softlogic Finance issuer capital statement. **20 Markdown source/evidence cards are in the repo, but raw PDF copies remain zero.** A listed-but-unretrieved audited document remains OPEN.

### Required process for every hourly research task

1. **Find** the authoritative original document and check the publisher, legal entity, report period and whether figures are audited or interim.
2. **Save** one provenance record, or update an existing stable-ID record. Include issuer URL, original PDF page/section, quoted claim in your *own words*, units, date and confidence/limitations.
3. **Archive a copy only if legally permitted and technically feasible** under `sources/documents/<source-id>.<ext>`. If archived, compute and record the real SHA-256 hash and source file size; verify the committed GitHub file. Otherwise mark **external original only**.
4. **Cross-link** the report from the source record, and the source record from the English/Tamil/Sinhala report pages and `SOURCES.md` indexes.
5. **Record conflicting figures** explicitly in `RESEARCH-LOG.md`; never silently overwrite reported audited figures with a data-provider normalized number.
6. **Validate Markdown links, source labels, GitHub commit and privacy**. Do not create GitHub Actions or workflows.

### Citation convention

Use a stable record identifier next to a factual claim, for example **[`SCAP-AR-2025`](records/SCAP-AR-2025.md), original PDF p. 63, Group, LKR million, FY ended 31 March 2025 (audited)**. For financial data, distinguish **SCAP Group**, **SCAP standalone Company**, **Softlogic Life** and **Softlogic Finance**, as well as minority-owner allocations.

### Not included

No personal portfolio positions, brokerage credentials, copied private datasets, or automated bulk rehosting of third-party copyrighted material.

**Initialized 30 September 2026; updated incrementally by scheduled research tasks.**

### Newly discovered reports / CI requirements

Every file in `sources/records/`, **including DISCOVERY / index-only notes**, must list a matching stable source ID, source publisher, period, legal entity/scope, assurance status (including **NOT VERIFIED**), page/section (**N/A** when original not retrieved), external original or **explicitly labelled secondary lead URL**, redistribution permission and SHA-256/archival status (**N/A** when no binary). Every source/evidence file is indexed in `SOURCE-REGISTER.md`. This is verified by [Research Validation Actions](../.github/workflows/research-validation.yml).
