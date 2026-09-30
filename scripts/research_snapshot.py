#!/usr/bin/env python3
"""Create dated, traceable SCAP research snapshots as downloadable workflow artifacts."""
import argparse
import csv
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
QUEUE = re.compile(r"^\|\s*\[([^\]]+)\]\(([^)]+\.md)\)\s*\|\s*\*\*(PARTIAL|TEMPLATE|FILLED)", re.M)


def status(queued):
    values = [{"topic": name, "document": path, "status": stat}
              for name, path, stat in QUEUE.findall(queued)]
    if len(values) != 20:
        raise ValueError(f"Expected 20 topic statuses, parsed {len(values)}. The queue format changed.")
    return values


def compose(data, topics, sources, timestamp, sha):
    periods = data["periods"]
    amounts = {m["id"]:m for m in data["amounts"]}
    def amount(name, period):
        return amounts[name]["values"][period]
    digest = {
        "generated_at":timestamp.isoformat(),
        "date_sri_lanka":timestamp.astimezone(ZoneInfo("Asia/Colombo")).date().isoformat(),
        "research_as_of":data["as_of"],
        "commit":sha,
        "ticker":"SCAP.N0000",
        "note":"Historical research snapshot; not live pricing, and not an investment recommendation.",
        "disclosure":"FY2026 is YEAR-END INTERIM SUBJECT TO AUDIT; final FY2026 SCAP audit and June 2026 SCAP original quarter remain OPEN.",
        "source_cards":sources,
        "source_pdf_binaries_archived":0,
        "periods":periods,
        "chapters":topics,
        "amounts":data["amounts"],
        "arithmetic_equations":data["equations"],
        "ratios":data["ratios"],
        "original_source_register":"sources/SOURCE-REGISTER.md",
    }
    return digest


def summary(snapshot):
    t = snapshot["chapters"]
    counts = {k:sum(x["status"] == k for x in t) for k in ("PARTIAL","TEMPLATE","FILLED")}
    amount_map = {m["id"]:m["values"] for m in snapshot["amounts"]}
    def fmt(n):
        return f"{n:,.2f}"
    def row(label, key, *periods):
        m=amount_map[key]
        vals=[fmt(m[p]) if p in m else "—" for p in periods]
        return "| " + label + " | " + " | ".join(vals) + " |"
    lines = [
        "# SCAP.N0000 public research snapshot — " + snapshot["date_sri_lanka"],
        "",
        "**Generated:** " + snapshot["generated_at"] + " · **Git commit:** " + snapshot["commit"],
        "**Evidence cutoff:** " + snapshot["research_as_of"] + " · **Source cards:** " + str(snapshot["source_cards"]),
        "",
        "> **ASSURANCE:** FY2025 figures were recorded from the audited issuer report. FY2026 figures were",
        "> recorded from the **27 May 2026 year-end INTERIM, subject to audit**. This snapshot does",
        "> NOT verify the final FY2025/26 signed SCAP audit, restatements, nor the original June",
        "> 2026 SCAP interim. It does not download/copy original PDF binaries.",
        "",
        "## Historical financial comparison",
        "",
        "**Amounts in LKR million.** GROUP figures and PARENT figures are separate legal/accounting scopes.",
        "",
        "| Metric | FY2025 audited | FY2026 year-end interim |",
        "|---|---:|---:|",
        row("GROUP operating income","group_income","FY2025","FY2026_INTERIM"),
        row("GROUP profit after tax","group_PAT","FY2025","FY2026_INTERIM"),
        row("GROUP PAT attributable to SCAP owners","owners_PAT","FY2025","FY2026_INTERIM"),
        row("GROUP PAT attributable to non-controlling interests","NCI_PAT","FY2025","FY2026_INTERIM"),
        row("GROUP cash from operations","group_operating_cash_flow","FY2025","FY2026_INTERIM"),
        row("PARENT standalone borrowings","parent_borrowings","FY2025","FY2026_INTERIM"),
        row("PARENT standalone cash/bank","parent_cash","FY2025","FY2026_INTERIM"),
        "",
        "## Research coverage",
        "",
        f"**20 subjects · 3 languages:** {counts['PARTIAL']} partially researched, "
        f"{counts['TEMPLATE']} research templates, {counts['FILLED']} fully sourced.",
        "",
        "| Topic | Status | Original report |",
        "|---|---|---|",
    ]
    for ch in t:
        lines.append(f"| {ch['topic'].replace('|', '/')} | {ch['status']} | [{ch['document']}]"
                     f"(https://github.com/Gajarthan/SCAP-N0000-Research/blob/main/{ch['document']}) |")
    lines += [
        "",
        "## Evidence and open verification",
        "",
        "- [Source register](https://github.com/Gajarthan/SCAP-N0000-Research/blob/main/sources/SOURCE-REGISTER.md)",
        "- [Research queue](https://github.com/Gajarthan/SCAP-N0000-Research/blob/main/RESEARCH-QUEUE.md)",
        "- [FY2025 audited source record](https://github.com/Gajarthan/SCAP-N0000-Research/blob/main/sources/records/SCAP-AR-2025.md)",
        "- [FY2026 subject-to-audit interim source record](https://github.com/Gajarthan/SCAP-N0000-Research/blob/main/sources/records/SCAP-FY2026-YE-INTERIM.md)",
        "- Original SCAP FY2025/26 final signed audit, 30 June 2026 SCAP quarter,"
          " current pledge/loan-covenant status and the provider revenue-definition bridge remain OPEN.",
        "- Separate actual subsidiary dividend receipts from dividend announcements and SCAP shareholder distributions.",
        "",
        "**Scope:** Evidence-index snapshot, not advice or a signed accounting opinion.",
        "",
    ]
    return "\n".join(lines)


def write_snapshot(destination, current=None, root=ROOT):
    now = current or dt.datetime.now(dt.timezone.utc)
    if now.tzinfo is None:
        raise ValueError("Timestamp must be timezone-aware")
    data = json.loads((root / "data/financial-facts.json").read_text(encoding="utf-8"))
    topics = status((root / "RESEARCH-QUEUE.md").read_text(encoding="utf-8"))
    sources = len(list((root / "sources/records").glob("*.md")))
    if not sources:
        raise ValueError("Cannot produce source-free financial snapshot")
    try:
        sha = subprocess.check_output(["git","rev-parse","HEAD"],cwd=root,text=True).strip()
    except (FileNotFoundError,subprocess.CalledProcessError):
        sha = "unknown-not-verified"
    payload = compose(data,topics,sources,now,sha)
    path = Path(destination)
    path.mkdir(parents=True,exist_ok=True)
    date = payload["date_sri_lanka"]
    base = "SCAP-research-" + date
    (path / (base + ".json")).write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (path / (base + ".md")).write_text(summary(payload),encoding="utf-8")
    with (path / (base + "-financials.csv")).open("w",encoding="utf-8",newline="") as out:
        writer = csv.writer(out)
        writer.writerow(["metric","scope","unit","period","period_end","assurance","value","original_source_record_id"])
        for item in data["amounts"]:
            for period,value in item["values"].items():
                period_data=data["periods"][period]
                writer.writerow([item["id"],item["scope"],data["currency"]+" "+data["unit"],
                                 period,period_data["end"],period_data["assurance"],value,period_data["source_id"]])
    msg=f"Saved dated research snapshot for {date}: {sources} source cards and {len(topics)} chapters."
    print(msg)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"],"a",encoding="utf-8") as handle:
            handle.write(summary(payload))
    return payload


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output",type=Path,default=ROOT/"out/research-snapshot")
    args=p.parse_args()
    try:
        write_snapshot(args.output)
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print("::error title=Research snapshot::"+str(exc))
        return 1


if __name__ == "__main__":
    sys.exit(main())
