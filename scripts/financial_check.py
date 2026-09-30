#!/usr/bin/env python3
"""SCAP financial reconciliation: arithmetic plus scope, period and evidence invariants."""
import argparse
import datetime as dt
import json
import math
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CheckError(ValueError):
    pass


def compare_close(actual, expected, tolerance, label):
    if not math.isclose(actual, expected, rel_tol=0, abs_tol=tolerance):
        raise CheckError(f"{label}: reported {actual:g} vs computed {expected:g} (tolerance {tolerance:g})")


def run(path=ROOT / "data/financial-facts.json", root=ROOT):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        raise CheckError("Unrecognized financial facts schema")
    as_of = dt.date.fromisoformat(data["as_of"])
    if as_of > dt.date.today():
        raise CheckError("Data evidence cutoff date is in the future")
    if data.get("currency") != "LKR" or data.get("unit") != "million":
        raise CheckError("Amounts must clearly identify LKR millions")
    periods = data["periods"]
    if len(periods) < 2:
        raise CheckError("Both audited and interim periods must be recorded")
    starts = []
    for name, period in periods.items():
        date = dt.date.fromisoformat(period["end"])
        starts.append(date)
        if date > as_of:
            raise CheckError(f"{name}: period ends after evidence cutoff")
        if date.month != 3 or date.day != 31:
            raise CheckError(f"{name}: SCAP fiscal year-end must be 31 March")
        if "2026" in name and period["assurance"] == "audited":
            raise CheckError(f"{name}: FY2026 is NOT established as audited in this ledger")
        if name == "FY2025" and period["assurance"] != "audited":
            raise CheckError("FY2025 must retain original audited status")
        if name == "FY2026_INTERIM" and period["assurance"] != "interim_subject_to_audit":
            raise CheckError("FY2026 original data is interim, subject to audit")
        if name == "FY2025" and date.year != 2025:
            raise CheckError("FY2025 period end mislabelled")
        if name == "FY2026_INTERIM" and date.year != 2026:
            raise CheckError("FY2026 period end mislabelled")
        source = root / "sources/records" / (period["source_id"] + ".md")
        if not source.is_file():
            raise CheckError(f"{name}: original evidence record does not exist: {source.name}")
        if not period.get("original_page"):
            raise CheckError(f"{name}: missing source page/section")
    if len(set(starts)) != len(starts):
        raise CheckError("Duplicate fiscal reporting dates")
    metrics = {}
    for item in data["amounts"]:
        key = item["id"]
        if key in metrics:
            raise CheckError(f"Duplicate financial metric ID: {key}")
        if item["scope"] not in ("group", "parent"):
            raise CheckError(f"{key}: scope must distinguish group and parent")
        values = item["values"]
        if not values:
            raise CheckError(f"{key}: no numeric values")
        for period, amount in values.items():
            if period not in periods:
                raise CheckError(f"{key}: unknown period {period}")
            if type(amount) not in (float, int) or not math.isfinite(amount):
                raise CheckError(f"{key}/{period}: amount must be a finite number")
        metrics[key] = item
    if len(metrics) < 5:
        raise CheckError("Financial dataset is unexpectedly incomplete")

    def get(key, period, scope):
        if key not in metrics:
            raise CheckError(f"Missing metric: {key}")
        obj = metrics[key]
        if obj["scope"] != scope:
            raise CheckError(f"{key}: expected {scope} not {obj['scope']} (group/parent mixing)")
        if period not in obj["values"]:
            raise CheckError(f"{key}: missing period {period}")
        return obj["values"][period]

    for eq in data["equations"]:
        scope, period = eq["scope"], eq["period"]
        result = get(eq["result"], period, scope)
        actual = sum(get(x, period, scope) for x in eq["components"])
        if len(set(eq["components"])) != len(eq["components"]):
            raise CheckError(f"{eq['id']}: repeated component counted twice")
        compare_close(result, actual, float(eq["tolerance"]), eq["id"])
    for ratio in data["ratios"]:
        a = get(ratio["numerator"], ratio["period"], ratio["scope"])
        b = get(ratio["denominator"], ratio["period"], ratio["scope"])
        if not b:
            raise CheckError(f"{ratio['id']}: zero denominator")
        compare_close(float(ratio["as_percent"]), 100.0 * a / b,
                      float(ratio["tolerance_percentage_points"]), ratio["id"])

    for article, literals in data["translation_required"].items():
        if not article.startswith(("01-Fundamental-Analysis/", "02-Technical-Analysis/")):
            raise CheckError(f"Nonresearch article key: {article}")
        if not isinstance(literals, list) or not literals:
            raise CheckError(f"Missing figures used for translation checks: {article}")
        if len(set(literals)) != len(literals):
            raise CheckError(f"Duplicate required literal in {article}")

    print(f"Financial checks passed: {len(metrics)} scoped metrics, {len(periods)} periods, "
          f"{len(data['equations'])} arithmetic equations, {len(data['ratios'])} ratios; "
          f"as-of {as_of}.")
    return data


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", type=Path, default=ROOT / "data/financial-facts.json")
    args = p.parse_args()
    try:
        run(args.input)
        return 0
    except (CheckError, ValueError, KeyError, TypeError, OSError) as exc:
        print(f"::error title=Financial reconciliation::{exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
