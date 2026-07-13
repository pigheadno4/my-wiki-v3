import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import fetch_psp  # noqa: E402


class FetchPspTests(unittest.TestCase):
    def test_metronome_relative_page_path(self):
        self.assertEqual(
            fetch_psp.relative_page_path(
                "https://docs.metronome.com/guides/get-started/home.md"
            ),
            Path("guides/get-started/home.md"),
        )

    def test_retryable_status_policy(self):
        self.assertTrue(fetch_psp.is_retryable_status(429, 1))
        self.assertTrue(fetch_psp.is_retryable_status(503, 2))
        self.assertTrue(fetch_psp.is_retryable_status(403, 1))
        self.assertFalse(fetch_psp.is_retryable_status(403, 2))
        self.assertFalse(fetch_psp.is_retryable_status(404, 1))

    def test_dry_run_does_not_write(self):
        llms = "- [Home](https://docs.metronome.com/guides/get-started/home.md)"
        sitemap = (
            "<urlset><url><loc>https://docs.metronome.com/guides/get-started/home"
            "</loc></url></urlset>"
        )
        with tempfile.TemporaryDirectory() as tmp, patch.object(fetch_psp, "ROOT", Path(tmp)):
            result = fetch_psp.build_metronome_inventory(llms, sitemap)
            self.assertEqual(len([item for item in result if item.selected]), 1)
            self.assertFalse((Path(tmp) / "raw").exists())

    def test_manifest_summarizes_states(self):
        text = fetch_psp.render_metronome_manifest(
            [
                {"state": "collected-new", "url": "https://example.test/new"},
                {"state": "unchanged", "url": "https://example.test/same"},
                {"state": "failed", "url": "https://example.test/fail"},
            ],
            "2026-07-13T090000",
        )
        self.assertIn("# Metronome collection manifest", text)
        self.assertIn("- collected-new: 1", text)
        self.assertIn("- failed: 1", text)
        self.assertIn("https://example.test/fail", text)


if __name__ == "__main__":
    unittest.main()
