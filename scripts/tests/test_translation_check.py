import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import translation_check as check


class TranslationTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.ledger = self.root / "data/financial-facts.json"
        self.ledger.parent.mkdir(parents=True)
        self.ledger.write_text(json.dumps({"translation_required": {}}))
        for n in range(20):
            name = f"01-Fundamental-Analysis/{n+1:02d}-Example/README.md"
            for lang in ("en", "ta", "si"):
                path = check.langfile(lang, name, self.root)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("# Example\nAmount 42,383.72.\n")

    def test_complete_translations(self):
        self.assertEqual(check.check(self.root, self.ledger)[1], [])

    def test_missing_tamil_detected(self):
        check.langfile("ta", "01-Fundamental-Analysis/01-Example/README.md", self.root).unlink()
        self.assertTrue(any("missing ta" in e for e in check.check(self.root, self.ledger)[1]))

    def test_changed_financial_figure_detected(self):
        financial = {"translation_required": {
            "01-Fundamental-Analysis/01-Example/README.md": ["42,383.72"]}}
        self.ledger.write_text(json.dumps(financial))
        check.langfile("si", "01-Fundamental-Analysis/01-Example/README.md", self.root).write_text(
            "# Example\nAmount 39,794.\n")
        self.assertTrue(any("42,383.72" in e for e in check.check(self.root, self.ledger)[1]))

    def test_mermaid_count_detected(self):
        path = check.langfile("en", "01-Fundamental-Analysis/02-Example/README.md", self.root)
        path.write_text(path.read_text() + "\n" + "\x60" * 3 + "mermaid\nflowchart LR\n A --> B\n" + "\x60" * 3)
        self.assertTrue(any("Mermaid chart count" in e for e in check.check(self.root, self.ledger)[1]))

    def test_unlisted_number_is_warning(self):
        p = check.langfile("en", "01-Fundamental-Analysis/03-Example/README.md", self.root)
        p.write_text("# Example\nAmount 42,383.72 and 51,310.49\n")
        _, errors, warnings = check.check(self.root, self.ledger)
        self.assertFalse(errors)
        self.assertTrue(warnings)


if __name__ == "__main__":
    unittest.main()
