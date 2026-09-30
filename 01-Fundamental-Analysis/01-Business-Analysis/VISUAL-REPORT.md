# 📊 SCAP.N0000 — Business Analysis: 15 data-backed visuals

[← Business Analysis](README.md) · [தமிழ்](../../../ta/01-Fundamental-Analysis/01-Business-Analysis/VISUAL-REPORT.md) · [සිංහල](../../../si/01-Fundamental-Analysis/01-Business-Analysis/VISUAL-REPORT.md)

> **Scope:** 15 editable GitHub Markdown visualizations built from SCAP's March 2026 CSE **year-end interim**, Softlogic Life's **calendar-year 2025** disclosures, issuer web pages and clearly identified secondary observations. **Reviewed 30 Sep 2026.** Numbers have different reporting periods and legal-entity scopes; figures are **not** a live quote or an investment recommendation.

## 🧭 Visual index

| # | Visualization | Data basis |
|---|---|---|
| 01 | [Ownership tree — dated](#01-ownership-tree-dated) | FY2026 ownership |
| 02 | [Business ecosystem](#02-business-ecosystem) | Issuer business map |
| 03 | [Business-model canvas](#03-businessmodel-canvas) | Business mechanisms |
| 04 | [Segment revenue](#04-segment-revenue) | FY2026 interim + reconciled estimate |
| 05 | [Segment profit and loss](#05-segment-profit-and-loss) | FY2026 interim |
| 06 | [Who receives group profit?](#06-who-receives-group-profit) | FY2026 interim |
| 07 | [Profit-to-cash pathway](#07-profittocash-pathway) | FY2026 parent-only |
| 08 | [Company milestones](#08-company-milestones) | 2005–2026 events |
| 09 | [Insurance customers and reach](#09-insurance-customers-and-reach) | Insurer 2023–2025 |
| 10 | [Distribution-channel map](#10-distributionchannel-map) | Insurer FY25 / undated finance |
| 11 | [Industry market position](#11-industry-market-position) | Insurer calendar 2025 |
| 12 | [Competitive-advantage evidence](#12-competitiveadvantage-evidence) | Insurer 2025 / hypotheses |
| 13 | [Related-party flow of funds](#13-relatedparty-flow-of-funds) | FY2026 parent-only |
| 14 | [Regulatory dependency map](#14-regulatory-dependency-map) | Insurer 2025 / sector regulation |
| 15 | [Opportunities and constraints](#15-opportunities-and-constraints) | Mixed historical periods |

> **Source label key:** *CSE interim* = SCAP's 27 May 2026 company disclosure, FY2026 **subject to audit**; *Insurer 2025* = Softlogic Life, a different reporting entity with a **December** year-end; *issuer site, undated* = operating description, not a 2026 audited count; *secondary* = unverified news/data vendor. "Other segment" is a **derived rounded reconciliation**—see chart 04.

## 01 · Ownership tree — dated

```mermaid
flowchart TB
  H["Softlogic Holdings PLC"] --> P["Listed SCAP\n31 Mar 2026"]
  P --> L["Life 50.16%"]
  P --> F["Finance 81.71%"]
  P --> O["SCAP One 100%"]
  P --> R["SR One 100%"]
  P -.-> B["Broker stake OPEN"]
  P -.-> A["Asset manager stake OPEN"]
```

Softlogic Holdings' **69.35%** of SCAP and SCAP's **50.16%** of Softlogic Life, **81.71%** of Softlogic Finance, and **100%** each of SCAP One and SR One are reported **as at 31 Mar 2026**. **Stockbrokers and Asset Management exact current stakes are unverified**. The acquired life insurer is an *indirect* holding, not an extra 100%-owned SCAP asset.

**Provenance:** [Source 1](https://cdn.cse.lk/cmt/upload_report_file/1100_1779968696398.pdf) · [Source 2](https://softlogiccapital.lk/about-us-overview/).

## 02 · Business ecosystem

```mermaid
flowchart TB
  P["SCAP holding company"] --> I["Life insurance"]
  P --> F["Lending and deposits"]
  P --> B["Stockbroking"]
  P --> A["Asset management"]
  I --> IC["Policies and claims"]
  F --> FC["Interest and credit"]
  B --> BC["Commissions"]
  A --> AC["Fund management fees"]
```

SCAP's operating exposures include insurance, lending and deposits, equity intermediation, and asset/unit-trust management. These are **categories of activity**, not revenue weights. The insurer reported **LKR 40.1bn GWP in calendar 2025**, which is **not** SCAP group revenue.

**Provenance:** [Source 1](https://softlogiccapital.lk/about-us-overview/) · [Source 2](https://softlogiccapital.lk/subsidiaries/) · [Source 3](https://softlogiclife.lk/news/softlogic-life-surpasses-rs-40-bn-gwp-in-fy25-doubles-key-financial-metrics-over-four-years/).

## 03 · Business-model canvas

```mermaid
flowchart LR
  C["Customers"] --> C1["Insurance policyholders"]
  C --> C2["Borrowers / savers"]
  C --> C3["Investors / traders"]
  C --> C4["Fund investors"]
  E["Money engines"] --> E1["Premium contracts"]
  E --> E2["Loan interest and fees"]
  E --> E3["Trading commissions"]
  E --> E4["Fund management fees"]
  R["Risk and costs"] --> R1["Claims / solvency"]
  R --> R2["Credit loss / funding"]
  R --> R3["Market turnover"]
  R --> R4["Redemptions / expense"]
```

Customers, fee and interest receipts, costs and regulatory restrictions differ across the four activities. **Deposits are funding liabilities, not revenue; managed client assets are not SCAP's own assets.** The canvas documents economic mechanics, not actual segment margins.

**Provenance:** [Source 1](https://softlogiccapital.lk/about-us-overview/) · [Source 2](https://softlogiccapital.lk/subsidiaries/).

## 04 · Segment revenue

```mermaid
xychart-beta
  title "SCAP segment revenue FY2026 (before adjustments)"
  x-axis ["Insurance", "Finance", "Other*"]
  y-axis "LKR million" 0 --> 55000
  bar [48425.96, 1384.78, 2759.84]
```

Segment gross revenues for the year ended **31 Mar 2026** in **LKR million**: Insurance **48,425.96**, Finance **1,384.78**, Other **approximately 2,759.84**, then adjustments/eliminations **−1,260.09**, giving group total **51,310.49**. **The Other value is derived algebraically** from previously reviewed CSE-line totals and aligns with a third-party segment figure rounded to 2,760; it has **not** been separately rechecked against the original segment PDF line in this pass. Never add a segment GWP series to this chart.

**Provenance:** [Source 1](https://cdn.cse.lk/cmt/upload_report_file/1100_1779968696398.pdf) · [Source 2](https://stockanalysis.com/quote/cose/SCAP.N0000/financials/) · Other segment is a **derived reconciliation**, not an independently reverified exact PDF line..

## 05 · Segment profit and loss

```mermaid
xychart-beta
  title "SCAP segment after-tax result FY2026"
  x-axis ["Insurance", "Finance", "Other"]
  y-axis "LKR million" -1000 --> 5500
  bar [4870.86, -136.24, -515.4]
```

Segment **profit/(loss) after tax**, LKR million, from the previously reviewed FY2026 year-end interim: insurance **+4,870.86**, NBFI **−136.24**, Other **−515.40**; consolidation adjustments **−847.95**; group total **+3,371.26** (rounding may create 0.01 difference). Segment PAT cannot be valued without minority interests and parent debt.

**Provenance:** [Source 1](https://cdn.cse.lk/cmt/upload_report_file/1100_1779968696398.pdf).

## 06 · Who receives group profit?

```mermaid
pie showData
  title SCAP FY2026 group PAT allocation LKR mn
  "SCAP owners" : 973.77
  "Non-controlling interests" : 2397.49
```

Of FY2026 interim **group PAT LKR 3,371.26mn**, **LKR 973.77mn (28.88%)** belongs to SCAP owners and **LKR 2,397.49mn (71.12%)** is attributable to non-controlling shareholders. This is **allocation of accounting profit, not cash distributed**.

**Provenance:** [Source 1](https://cdn.cse.lk/cmt/upload_report_file/1100_1779968696398.pdf).

## 07 · Profit-to-cash pathway

```mermaid
flowchart TB
  B["Operating subsidiaries"] --> G["Group PAT 3,371.26"]
  G --> P["SCAP owners 973.77"]
  G --> N["Minorities 2,397.49"]
  B --> C["Subsidiary cash"]
  C --> R["Legal / capital restrictions"]
  R --> D["Dividends received by parent"]
  D --> I["Parent interest / repayments"]
  I --> E["Potential shareholder distribution"]
  P -.-> D
```

The **SCAP standalone** company reported **FY2026 dividend income LKR 635.18mn**, **interest expense LKR 1,810.84mn**, and **loss LKR 722.49mn**. At **31 Mar 2026**, parent interest-bearing borrowings were **LKR 17,324.26mn**, overdraft **323.13mn**, cash/bank **32.07mn**. The flowchart shows the *required logic*, not a numerical waterfall: dividend cash paid by subsidiaries, recorded accounting profit and available cash are not interchangeable.

**Provenance:** [Source 1](https://cdn.cse.lk/cmt/upload_report_file/1100_1779968696398.pdf).

## 08 · Company milestones

```mermaid
flowchart TB
  Y1["2005 Incorporated"] --> Y2["2010 Softlogic Holdings purchase"]
  Y2 --> Y3["2012 Life enters group"]
  Y3 --> Y4["2025 Jul Life acquisition"]
  Y4 --> Y5["2026 Mar FY end"]
  Y5 --> Y6["2026 May interim filed"]
```

Dated events: **2005** incorporation, **2010** Softlogic Holdings acquisition, **2012** life insurance added to the group portfolio, **11 Jul 2025** acquisition of Softlogic Life Insurance Lanka by Softlogic Life (reported consideration **LKR 1,426mn**), and **31 Mar / 27 May 2026** financial year-end and interim disclosure. The 2025 acquisition is not a direct SCAP transaction.

**Provenance:** [Source 1](https://softlogiccapital.lk/about-us-overview/) · [Source 2](https://cdn.cse.lk/cmt/upload_report_file/1100_1779968696398.pdf).

## 09 · Insurance customers and reach

```mermaid
xychart-beta
  title "Life policies in force | year-end counts"
  x-axis ["2023", "2024", "2025"]
  y-axis "Policies" 0 --> 1000000
  bar [733002, 748101, 880706]
```

Softlogic Life's **2025 annual report** records **880,706 policies in force** (2024: **748,101**, 2023: **733,002**) and **88.7% customer retention** (2024: **85.4%**). Its separate 2025 company release describes **1.3 million lives covered** and **LKR 19.4bn claims and benefits paid**. The chart measures **policies**, not unique people or SCAP group customers.

**Provenance:** [Source 1](https://softlogiclife.lk/wp-content/uploads/sites/3/2026/04/Softlogic-Life-Integrated-Annual-Report-2025-3.pdf) · [Source 2](https://softlogiclife.lk/news/softlogic-life-surpasses-rs-40-bn-gwp-in-fy25-doubles-key-financial-metrics-over-four-years/).

## 10 · Distribution-channel map

```mermaid
flowchart TB
  I["Insurance distribution"] --> IL["159 operating locations"]
  F["Finance distribution"] --> FL["36 locations on undated site"]
  FL --> FB["30 branches"]
  FL --> FP["6 pawning centres"]
  B["Stockbroker channels"] --> BR["Retail and institutional"]
  A["Asset-management channels"] --> U["2 unit trusts on undated site"]
```

The insurer's **2025 integrated-report portal** lists **159 operating locations**; SCAP's **undated website** describes Softlogic Finance as **36 locations (30 branches + 6 dedicated pawning centres)**. These are **different entities and non-matched as-of dates**, not a comparable branch-efficiency ranking. Brokerage targets retail/institutional/high-net-worth clients; asset-management site mentions **two unit trusts**, but today's number is unverified.

**Provenance:** [Source 1](https://annualreport.softlogiclife.lk/) · [Source 2](https://softlogiccapital.lk/subsidiaries/).

## 11 · Industry market position

```mermaid
pie showData
  title Softlogic Life 2025 share of life GWP (%)
  "Softlogic Life" : 18.4
  "All other insurers together" : 81.6
```

Softlogic Life reported **18.4% Sri Lanka life-insurance GWP market share for calendar 2025**; the remaining **81.6%** is a mathematical complement, **not one competitor**. A news report places insurer share at **20.3% at Q2 2026**, but this later **secondary** claim uses a different period and still needs direct insurer/regulator confirmation. SCAP itself does **not** have an equivalent market share across all financial services.

**Provenance:** [Source 1](https://softlogiclife.lk/news/softlogic-life-surpasses-rs-40-bn-gwp-in-fy25-doubles-key-financial-metrics-over-four-years/) · [Source 2](https://www.dailymirror.lk/business-news/Softlogic-Life-delivers-Rs-7-2bn-GWP/273-348142).

## 12 · Competitive-advantage evidence

```mermaid
flowchart TB
  Q["Testable hypotheses"] --> I["Insurance scale"]
  I --> G["FY25 GWP 40.1bn"]
  I --> R["Retention 88.7%"]
  I --> P["880,706 policies"]
  G --> T1["Compare acquisition cost"]
  R --> T2["Compare claim margins"]
  P --> T3["Compare peer ROE and capital"]
  T1 --> N["No proven moat"]
  T2 --> N
  T3 --> N
```

Potential advantages must be tested: 2025 Life **GWP LKR 40.1bn (+27%)**, **customer retention 88.7%**, **880,706 active policies**; all support questions about distribution and servicing but do **not** prove a moat. Compare profitable customer acquisition, renewal economics, claims and insurer solvency against true peers over matching periods.

**Provenance:** [Source 1](https://softlogiclife.lk/wp-content/uploads/sites/3/2026/04/Softlogic-Life-Integrated-Annual-Report-2025-3.pdf) · [Source 2](https://softlogiclife.lk/news/softlogic-life-surpasses-rs-40-bn-gwp-in-fy25-doubles-key-financial-metrics-over-four-years/).

## 13 · Related-party flow of funds

```mermaid
flowchart LR
  H["Softlogic Holdings"] -->|"Interest 427.04"| P["SCAP parent company"]
  S["SR One"] -->|"Interest 160.39"| P
  L["Softlogic Life"] -->|"Fees 120.00"| P
  B["Stockbrokers"] -->|"Fees 64.11"| P
  A["Asset Management"] -->|"Fees 76.00"| P
```

In the SCAP **company-only related-party FY2026 note**, reported amounts in **LKR million** include interest income from Softlogic Holdings **427.04** and SR One **160.39**, plus consultancy/professional fees from Life **120.00**, Stockbrokers **64.11**, and Asset Management **76.00**. These are **parent-account transactions; they must not be double-counted as external consolidated revenue or assumed to be cash collected**.

**Provenance:** [Source 1](https://cdn.cse.lk/cmt/upload_report_file/1100_1779968696398.pdf).

## 14 · Regulatory dependency map

```mermaid
flowchart TB
  IR["IRCSL"] --> L["Softlogic Life"]
  L --> LC["2025 CAR 245%; stated minimum 120%"]
  CB["CBSL"] --> F["Softlogic Finance"]
  SE["SEC / CSE"] --> BA["Brokerage and manager"]
  L --> D["SCAP dividend capacity NOT proven"]
  F --> D
  BA --> D
```

The insurance entity is supervised by **IRCSL**; the finance entity by **CBSL**; stockbroking/investment-management by **SEC/CSE** as applicable. Life reports **2025 capital adequacy ratio (CAR) 245%** against its stated **120% requirement**. Those figures are insurer-only and **do not establish parent dividend availability**. A reported **LKR 1,515.80mn restricted insurance reserve at Mar 2026** requires attention to conditions on release.

**Provenance:** [Source 1](https://cdn.cse.lk/cmt/upload_report_file/1100_1779968696398.pdf) · [Source 2](https://softlogiclife.lk/news/softlogic-life-surpasses-rs-40-bn-gwp-in-fy25-doubles-key-financial-metrics-over-four-years/) · [Source 3](https://ircsl.gov.lk/) · [Source 4](https://www.cbsl.gov.lk/) · [Source 5](https://www.sec.gov.lk/).

## 15 · Opportunities and constraints

```mermaid
flowchart TB
  Q["Evidence to weigh"] --> I["Potential: insurance distribution"]
  I --> G["FY25 GWP 40.1bn; +27%"]
  Q --> A["Potential: acquisition integration"]
  A --> AL["Life purchase 11 Jul 2025"]
  Q --> F["Constraint: finance result"]
  F --> FL["FY26 segment loss 136.24mn"]
  Q --> P["Constraint: parent finance"]
  P --> PL["FY26 interest 1,810.84mn"]
  Q --> C["Constraint: dividend access"]
  C --> CL["Insurance capital restrictions"]
```

The documented **potential drivers** are FY2025 insurer GWP **LKR 40.1bn (+27%)**, its service footprint, and insurer acquisition integration. The documented **constraints** include FY2026 non-bank-finance segment loss **LKR 136.24mn**, parent interest expense **LKR 1,810.84mn**, parent borrowing **LKR 17,324.26mn**, and regulatory cash-upstream limits. These are different-period observations and **not a forecast or a ranking**.

**Provenance:** [Source 1](https://cdn.cse.lk/cmt/upload_report_file/1100_1779968696398.pdf) · [Source 2](https://softlogiclife.lk/news/softlogic-life-surpasses-rs-40-bn-gwp-in-fy25-doubles-key-financial-metrics-over-four-years/).

## 📚 Sources and limitations

[S1] [SCAP year-ended 31 Mar 2026, interim approved 27 May 2026](https://cdn.cse.lk/cmt/upload_report_file/1100_1779968696398.pdf) — PDF pp. 2–3, 6, 10–11, 13, 15–17, 19. FY2026 subject to audit.

[S2] [SCAP company overview](https://softlogiccapital.lk/about-us-overview/) and [business descriptions](https://softlogiccapital.lk/subsidiaries/) — undated issuer pages.

[S3] [Softlogic Life calendar-2025 issuer results release](https://softlogiclife.lk/news/softlogic-life-surpasses-rs-40-bn-gwp-in-fy25-doubles-key-financial-metrics-over-four-years/) — GWP, market share, lives, claims, CAR.

[S4] [Softlogic Life 2025 integrated annual report](https://softlogiclife.lk/wp-content/uploads/sites/3/2026/04/Softlogic-Life-Integrated-Annual-Report-2025-3.pdf) — policies in force and retention; 2025/2024/2023 values in report's sustainability metrics table.

[S5] [Life annual-report portal](https://annualreport.softlogiclife.lk/) — 159 locations; issuer portal snapshot (report-year context).

[S6] [SCAP financial aggregator segment table](https://stockanalysis.com/quote/cose/SCAP.N0000/financials/) — only a *secondary rounded cross-check* for Other segment approximately 2,760; verify the exact official row.

[S7] [August 2026 news on insurer market share](https://www.dailymirror.lk/business-news/Softlogic-Life-delivers-Rs-7-2bn-GWP/273-348142) — **secondary** Q2 2026 share 20.3%; not used as a FY2025 number.

[S8] Sector supervisors: [IRCSL](https://ircsl.gov.lk/), [CBSL](https://www.cbsl.gov.lk/), [SEC](https://www.sec.gov.lk/), [CSE](https://www.cse.lk/).

All LKR figures and stakes are historical. Compare with a later audited annual report and original subsequent interim before using them in any decision.
