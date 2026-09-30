"""No-network regression tests for SCAP research checks."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import research_validate as v


class ResearchValidationTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.doc = self.root / "01-Fundamental-Analysis/12-Forensic-Accounting/README.md"
        self.doc.parent.mkdir(parents=True)
        self.source = self.root / "sources/records/EXAMPLE-1.md"
        self.source.parent.mkdir(parents=True)
        self.source.write_text("Placeholder", encoding="utf-8")
        self.patch = patch.object(v, "ROOT", self.root)
        self.patch.start()
        self.addCleanup(self.patch.stop)

    def check(self, text):
        self.doc.write_text(text, encoding="utf-8")
        result = v.Results()
        clean = v.clean_code_and_export(self.doc, text, None, result)
        v.validate_links(self.doc, clean, result)
        v.validate_citations(self.doc, clean, result)
        return result

    def test_link_good(self):
        self.assertEqual(self.check("[S](../../sources/records/EXAMPLE-1.md)").errors, 0)

    def test_link_broken(self):
        self.assertGreater(self.check("[S](../../sources/records/MISSING.md)").errors, 0)

    def test_fence_unclosed(self):
        self.assertGreater(self.check("# Title\n" + "\x60" * 3 + "mermaid\nflowchart LR\n A-->B").errors, 0)

    def test_chart_export(self):
        result = v.Results()
        with tempfile.TemporaryDirectory() as directory:
            text = "# Title\n" + "\x60" * 3 + "mermaid\nflowchart LR\n A --> B\n" + "\x60" * 3 + "\n"
            v.clean_code_and_export(self.doc, text, Path(directory), result)
            self.assertEqual(result.diagrams, 1)
            self.assertEqual(len(list(Path(directory).glob("*.mmd"))), 1)
            self.assertEqual(result.errors, 0)

    def test_uncited_claim_fails(self):
        self.assertGreater(self.check("# Finance\nThe group earned LKR 120 million.\n").errors, 0)

    def test_cited_claim_passes(self):
        self.assertEqual(self.check("# Finance\nThe group earned LKR 120 million. [Report](https://issuer.example/annual.pdf)\n").errors, 0)

    def test_bad_source_fields(self):
        result = v.Results()
        v.validate_record(self.source, result)
        self.assertGreater(result.errors, 4)

    def test_good_source_fields(self):
        self.source.write_text(
            "# EXAMPLE-1\n| Field | Value |\n|---|---|\n"
            "| Stable source ID | \x60EXAMPLE-1\x60 |\n| Publisher | Issuer |\n"
            "| Reporting/announcement period | FY2025 |\n| Legal entity and scope | SCAP Group |\n"
            "| Verification status | Historical |\n| Original page/section | p.2 |\n"
            "| Redistribution permission | Not verified |\n| Original SHA-256 / size | N/A |\n"
            "| Original URL | [Original](https://issuer.example/report.pdf) |\n", encoding="utf-8")
        result = v.Results()
        v.validate_record(self.source, result)
        self.assertEqual(result.errors, 0)

    def test_unindexed_record(self):
        reg = self.root / "sources/SOURCE-REGISTER.md"
        reg.write_text("# Empty register", encoding="utf-8")
        result = v.Results()
        v.check_register(result)
        self.assertGreater(result.errors, 0)


if __name__ == "__main__":
    unittest.main()
