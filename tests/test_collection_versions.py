import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from collection_versions import (  # noqa: E402
    body_sha256,
    classify_candidate,
    latest_prior,
    next_target,
)


class VersionTests(unittest.TestCase):
    def test_hash_ignores_only_repository_headers(self):
        left = "<!-- Source URL: a -->\n<!-- Fetched: 2026-07-12 -->\n\n# Body\n"
        right = "<!-- Source URL: b -->\n<!-- Fetched: 2026-08-05 -->\n\n# Body\n"
        self.assertEqual(body_sha256(left), body_sha256(right))
        self.assertNotEqual(body_sha256(left), body_sha256(right + "Changed\n"))

    def test_latest_prior_and_same_day_revision(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp)
            page = raw / "guides" / "home-2026-07-12.md"
            page.parent.mkdir(parents=True)
            page.write_text("old", encoding="utf-8")
            self.assertEqual(
                latest_prior(raw, Path("guides/home.md")),
                page,
            )
            first = next_target(raw, Path("guides/home.md"), "2026-08-05")
            first.parent.mkdir(parents=True, exist_ok=True)
            first.write_text("new", encoding="utf-8")
            self.assertEqual(
                next_target(raw, Path("guides/home.md"), "2026-08-05").name,
                "home-2026-08-05-r2.md",
            )

    def test_classification(self):
        self.assertEqual(classify_candidate(None, "body"), "new")
        self.assertEqual(classify_candidate("body", "body"), "unchanged")
        self.assertEqual(classify_candidate("body", "changed"), "changed")


if __name__ == "__main__":
    unittest.main()
