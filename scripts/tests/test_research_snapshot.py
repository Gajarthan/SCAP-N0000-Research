import datetime as dt
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import research_snapshot as snap


class SnapshotTests(unittest.TestCase):
    def test_current_queue_has_20_topics(self):
        body=(snap.ROOT/"RESEARCH-QUEUE.md").read_text(encoding="utf-8")
        self.assertEqual(len(snap.status(body)),20)

    def test_missing_queue_topics_is_error(self):
        with self.assertRaises(ValueError):
            snap.status("| [only one](test.md) | **PARTIAL** |")

    def test_snapshot_artifacts_and_assurance(self):
        with tempfile.TemporaryDirectory() as directory:
            created=snap.write_snapshot(
                Path(directory),
                current=dt.datetime(2026,9,30,19,0,tzinfo=dt.timezone.utc))
            self.assertEqual(created["date_sri_lanka"],"2026-10-01")
            self.assertEqual(created["periods"]["FY2026_INTERIM"]["assurance"],
                             "interim_subject_to_audit")
            files=list(Path(directory).glob("SCAP-research-2026-10-01*"))
            self.assertEqual(len(files),3)
            m=next(x for x in files if x.suffix==".md").read_text()
            self.assertIn("SUBJECT TO AUDIT",m.upper())

    def test_snapshot_ledger_is_traceable(self):
        with tempfile.TemporaryDirectory() as directory:
            snap.write_snapshot(Path(directory))
            data=json.loads(next(Path(directory).glob("*.json")).read_text())
            self.assertGreaterEqual(data["source_cards"],18)
            self.assertEqual(data["source_pdf_binaries_archived"],0)


if __name__ == "__main__":
    unittest.main()
