import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from collection_reporting import (  # noqa: E402
    render_status,
    validate_terminal_counts,
    write_jsonl,
)


class ReportingTests(unittest.TestCase):
    def test_terminal_counts_reconcile(self):
        events = [
            {"selected": True, "state": "collected-new"},
            {"selected": True, "state": "unchanged"},
            {"selected": True, "state": "failed"},
        ]
        self.assertEqual(validate_terminal_counts(events), 3)

    def test_pending_state_rejects_completed_run(self):
        with self.assertRaisesRegex(ValueError, "non-terminal"):
            validate_terminal_counts([{"selected": True, "state": "pending"}])

    def test_jsonl_and_markdown(self):
        events = [{"url": "https://example.test/a", "selected": True, "state": "failed"}]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "run.jsonl"
            write_jsonl(path, events)
            self.assertEqual(json.loads(path.read_text().strip())["state"], "failed")
        status = render_status("metronome", [], events)
        self.assertIn("# Metronome Collection Status", status)
        self.assertIn("| failed | 1 |", status)


if __name__ == "__main__":
    unittest.main()
