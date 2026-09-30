import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import source_monitor as mon


class SourceMonitoringTests(unittest.TestCase):
    def test_only_issuer_1100(self):
        original = "https://cdn.cse.lk/cmt/upload_report_file/1100_1780000000.pdf"
        wrong = "https://cdn.cse.lk/cmt/upload_report_file/1075_1780000000.pdf"
        self.assertTrue(mon.candidate(original, "SCAP Annual 2026"))
        self.assertFalse(mon.candidate(wrong, "SCAP Annual 2026"))

    def test_reject_2018(self):
        self.assertFalse(mon.candidate("https://softlogiccapital.lk/reports/report-2018.pdf", "FY 2018"))

    def test_reject_third_party(self):
        self.assertFalse(mon.candidate("https://other.example/reports/report-2026.pdf", "FY 2026"))

    def test_heading_context_is_preserved(self):
        html = "<h2>SCAP Annual Report 2025-2026</h2><a href='/pdf/report.pdf'>Download</a>"
        results = mon.discover(html, "https://softlogiccapital.lk/financials/")
        self.assertEqual(len(results), 1)

    def test_tracking_parameters_ignored(self):
        self.assertEqual(mon.canonical("https://cdn.cse.lk/a.pdf?ref=x"), "https://cdn.cse.lk/a.pdf")


if __name__ == "__main__":
    unittest.main()
