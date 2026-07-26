import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import validate_wiki  # noqa: E402


class NestedRawLinkTests(unittest.TestCase):
    def test_link_index_includes_nested_raw_basename_and_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "raw"
            wiki = root / "wiki"
            nested = raw / "metronome" / "guides" / "home-2026-07-13.md"
            nested.parent.mkdir(parents=True)
            wiki.mkdir()
            nested.write_text("raw", encoding="utf-8")

            with patch.multiple(validate_wiki, ROOT=root, RAW=raw, WIKI=wiki):
                links = validate_wiki.build_link_index()

            self.assertIn("home-2026-07-13", links)
            self.assertIn("raw/metronome/guides/home-2026-07-13", links)

    def test_path_qualified_nested_raw_wikilink_resolves(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "raw"
            wiki = root / "wiki"
            nested = raw / "metronome" / "guides" / "home-2026-07-13.md"
            source = wiki / "sources" / "source-home.md"
            nested.parent.mkdir(parents=True)
            source.parent.mkdir(parents=True)
            nested.write_text("raw", encoding="utf-8")
            source.write_text(
                "---\n"
                'title: "Home"\n'
                "type: source\n"
                "date_ingested: 2026-07-13\n"
                "original_format: webpage\n"
                "raw_files:\n"
                '  - "metronome/guides/home-2026-07-13.md"\n'
                "tags: [metronome]\n"
                "---\n\n"
                "## Raw Sources\n\n"
                "- [[raw/metronome/guides/home-2026-07-13|snapshot]]\n",
                encoding="utf-8",
            )

            with patch.multiple(validate_wiki, ROOT=root, RAW=raw, WIKI=wiki):
                links = validate_wiki.build_link_index()
                errors = []
                validate_wiki.check_file(source, links, errors)

            self.assertEqual([], errors)

    def test_path_qualified_github_snapshot_and_release_ledger_links_resolve(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "raw"
            wiki = root / "wiki"
            source = wiki / "sources" / "paypal" / "github" / "source-github-paypal-js.md"
            snapshots = [
                raw / "github/paypal/paypal-js/snapshots/2026-07-15-v10-aaaaaaa",
                raw / "github/paypal/paypal-js/snapshots/2026-07-01-v9-bbbbbbb",
            ]
            for snapshot in snapshots:
                (snapshot / "files").mkdir(parents=True)
                (snapshot / "snapshot.md").write_text("snapshot\n", encoding="utf-8")
                (snapshot / "files/CHANGELOG.md").write_text(
                    "changelog\n", encoding="utf-8"
                )
                (snapshot / "release-notes.md").write_text(
                    "release notes\n", encoding="utf-8"
                )
            source.parent.mkdir(parents=True)
            source.write_text(
                "---\n"
                'title: "PayPal JS"\n'
                "type: source\n"
                "date_ingested: 2026-07-15\n"
                "original_format: github-repo\n"
                "raw_files:\n"
                '  - "github/paypal/paypal-js/snapshots/2026-07-15-v10-aaaaaaa/snapshot.md"\n'
                '  - "github/paypal/paypal-js/snapshots/2026-07-01-v9-bbbbbbb/snapshot.md"\n'
                "tags: [paypal, github]\n"
                "---\n\n"
                "## Release History\n\n"
                "| Version | Snapshot | Changelog | Release notes |\n"
                "| --- | --- | --- | --- |\n"
                "| v10 | [[raw/github/paypal/paypal-js/snapshots/2026-07-15-v10-aaaaaaa/snapshot|snapshot]] "
                "| [[raw/github/paypal/paypal-js/snapshots/2026-07-15-v10-aaaaaaa/files/CHANGELOG|changelog]] "
                "| [[raw/github/paypal/paypal-js/snapshots/2026-07-15-v10-aaaaaaa/release-notes|release notes]] |\n"
                "| v9 | [[raw/github/paypal/paypal-js/snapshots/2026-07-01-v9-bbbbbbb/snapshot|snapshot]] "
                "| [[raw/github/paypal/paypal-js/snapshots/2026-07-01-v9-bbbbbbb/files/CHANGELOG|changelog]] "
                "| [[raw/github/paypal/paypal-js/snapshots/2026-07-01-v9-bbbbbbb/release-notes|release notes]] |\n",
                encoding="utf-8",
            )

            with patch.multiple(validate_wiki, ROOT=root, RAW=raw, WIKI=wiki):
                links = validate_wiki.build_link_index()
                errors = []
                validate_wiki.check_file(source, links, errors)

            self.assertEqual([], errors)

    def test_provider_log_is_a_valid_page_type(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "raw"
            wiki = root / "wiki"
            log = wiki / "metronome-log.md"
            raw.mkdir()
            wiki.mkdir()
            log.write_text(
                "---\n"
                'title: "Metronome Log"\n'
                "type: log\n"
                "tags: [metronome, operations]\n"
                "---\n\n"
                "## 2026-07-13\n\nCollection completed.\n",
                encoding="utf-8",
            )

            with patch.multiple(validate_wiki, ROOT=root, RAW=raw, WIKI=wiki):
                errors = []
                validate_wiki.check_file(log, validate_wiki.build_link_index(), errors)

            self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
