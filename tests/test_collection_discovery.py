import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from collection_discovery import canonicalize_url, reconcile_metronome  # noqa: E402


class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        fixture = ROOT / "tests" / "fixtures" / "metronome"
        self.llms = (fixture / "llms.txt").read_text(encoding="utf-8")
        self.sitemap = (fixture / "sitemap.xml").read_text(encoding="utf-8")

    def test_canonicalize_markdown_and_trailing_slash(self):
        self.assertEqual(
            canonicalize_url("https://docs.metronome.com/guides/home.md#start"),
            "https://docs.metronome.com/guides/home",
        )

    def test_reconcile_selects_english_union(self):
        records = reconcile_metronome(self.llms, self.sitemap)
        selected = [record for record in records if record.selected and record.kind == "page"]
        self.assertEqual(len(selected), 3)
        by_url = {record.canonical_url: record for record in records}
        home = by_url["https://docs.metronome.com/guides/get-started/home"]
        self.assertTrue(home.in_llms)
        self.assertTrue(home.in_sitemap)
        gap = by_url[
            "https://docs.metronome.com/api-reference/credit-grants/create-a-credit-grant"
        ]
        self.assertFalse(gap.in_llms)
        self.assertTrue(gap.in_sitemap)
        self.assertEqual(
            gap.fetch_url,
            "https://docs.metronome.com/api-reference/credit-grants/create-a-credit-grant.md",
        )

    def test_reconcile_records_artifact_and_exclusions(self):
        records = reconcile_metronome(self.llms, self.sitemap)
        payload = json.dumps([record.to_dict() for record in records])
        self.assertIn('"kind": "artifact"', payload)
        self.assertIn('"exclusion_reason": "localized-fr"', payload)
        self.assertIn('"exclusion_reason": "external-host"', payload)


if __name__ == "__main__":
    unittest.main()
