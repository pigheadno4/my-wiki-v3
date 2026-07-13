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


if __name__ == "__main__":
    unittest.main()
