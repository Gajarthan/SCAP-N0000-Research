import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import financial_check as check


class FinancialTest(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((check.ROOT / "data/financial-facts.json").read_text())
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def run_with(self, value):
        path = Path(self.tmp.name) / "facts.json"
        path.write_text(json.dumps(value), encoding="utf-8")
        return check.run(path)

    def test_original_passes(self):
        self.run_with(self.data)

    def test_group_pat_allocation(self):
        data = copy.deepcopy(self.data)
        next(x for x in data["amounts"] if x["id"] == "NCI_PAT")["values"]["FY2026_INTERIM"] += 100
        with self.assertRaises(check.CheckError):
            self.run_with(data)

    def test_parent_debt_total(self):
        data = copy.deepcopy(self.data)
        next(x for x in data["amounts"] if x["id"] == "parent_commercial_paper")["values"]["FY2025"] -= 50
        with self.assertRaises(check.CheckError):
            self.run_with(data)

    def test_bad_owner_ratio(self):
        data = copy.deepcopy(self.data)
        data["ratios"][0]["as_percent"] = 42.00
        with self.assertRaises(check.CheckError):
            self.run_with(data)

    def test_scope_mismatch(self):
        data = copy.deepcopy(self.data)
        next(x for x in data["amounts"] if x["id"] == "NCI_PAT")["scope"] = "parent"
        with self.assertRaises(check.CheckError):
            self.run_with(data)

    def test_no_fabricated_fy26_audit(self):
        data = copy.deepcopy(self.data)
        data["periods"]["FY2026_INTERIM"]["assurance"] = "audited"
        with self.assertRaises(check.CheckError):
            self.run_with(data)

    def test_bad_period_date(self):
        data = copy.deepcopy(self.data)
        data["periods"]["FY2025"]["end"] = "2026-03-31"
        with self.assertRaises(check.CheckError):
            self.run_with(data)

    def test_missing_original_source(self):
        data = copy.deepcopy(self.data)
        data["periods"]["FY2025"]["source_id"] = "DOES-NOT-EXIST"
        with self.assertRaises(check.CheckError):
            self.run_with(data)


if __name__ == "__main__":
    unittest.main()
