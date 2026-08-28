import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import fetch_psp  # noqa: E402


class FetchPspTests(unittest.TestCase):
    def test_load_config_uses_shared_toml_loader(self):
        expected = {"stripe": {"host": "docs.stripe.com"}}

        with patch("fetch_psp.load_toml", return_value=expected) as load_toml:
            self.assertIs(expected, fetch_psp.load_config())

        load_toml.assert_called_once_with(fetch_psp.CONFIG)

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

    def test_artifact_lookup_does_not_cross_matching_stems(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            expected = root / "openapi-2026-07-13.json"
            expected.write_text("main", encoding="utf-8")
            (root / "openapi-plans-2026-07-13.json").write_text("plans", encoding="utf-8")
            self.assertEqual(
                fetch_psp.latest_artifact_prior(root, "openapi"),
                expected,
            )

    def test_artifact_target_returns_next_available_same_day_revision(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "openapi-2026-08-28.json").write_text("first", encoding="utf-8")

            self.assertEqual(
                fetch_psp._next_artifact_target(root, "openapi", "2026-08-28"),
                root / "openapi-2026-08-28-r2.json",
            )

    def test_metronome_collection_persists_empty_inventory_and_manifest(self):
        config = {
            "raw_root": "raw/metronome",
            "discovery": [
                {"name": "llms", "url": "https://example.test/llms.txt"},
                {"name": "sitemap", "url": "https://example.test/sitemap.xml"},
            ],
        }
        with (
            tempfile.TemporaryDirectory() as tmp,
            patch.object(fetch_psp, "ROOT", Path(tmp)),
            patch("fetch_psp.http_get", return_value=""),
            patch("fetch_psp.build_metronome_inventory", return_value=[]),
        ):
            fetch_psp.collect_metronome(
                config,
                limit=None,
                dry_run=False,
                collection_date="2026-08-28",
                run_id="test-run",
            )

            self.assertTrue(
                (Path(tmp) / "tracking/collections/metronome/inventory-current.json").exists()
            )
            self.assertTrue(
                (Path(tmp) / "tracking/collections/metronome/runs/test-run-manifest.md").exists()
            )


if __name__ == "__main__":
    unittest.main()
