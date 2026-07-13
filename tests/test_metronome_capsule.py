import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from metronome_capsule import inspect_capsule, validate_capsule  # noqa: E402


class MetronomeCapsuleTests(unittest.TestCase):
    def make_capsule(self, root: Path, source_count: int = 0, index_links=()):
        (root / "raw" / "metronome").mkdir(parents=True)
        (root / "wiki" / "sources" / "metronome").mkdir(parents=True)
        (root / "wiki" / "companies").mkdir(parents=True)
        links = "\n".join(f"- [[{link}]]" for link in index_links)
        (root / "wiki" / "metronome-index.md").write_text(
            "# Metronome Index\n\n## Sources\n\n" + links + "\n",
            encoding="utf-8",
        )
        (root / "wiki" / "companies" / "metronome.md").write_text(
            "---\n"
            'title: "Metronome"\n'
            "type: company\n"
            "tags: [metronome]\n"
            f"source_count: {source_count}\n"
            "---\n",
            encoding="utf-8",
        )

    def write_raw(self, root: Path, relative="guides/home-2026-07-13.md") -> str:
        path = root / "raw" / "metronome" / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("raw", encoding="utf-8")
        return "metronome/" + relative

    def write_source(
        self,
        root: Path,
        name="source-metronome-guides-home.md",
        canonical_url="https://docs.metronome.com/guides/home",
        raw_files=("metronome/guides/home-2026-07-13.md",),
        raw_links=("metronome/guides/home-2026-07-13.md",),
    ):
        raw_list = "\n".join(f'  - "{path}"' for path in raw_files)
        links = "\n".join(
            f"- [[raw/{Path(path).with_suffix('').as_posix()}|snapshot]]"
            for path in raw_links
        )
        path = root / "wiki" / "sources" / "metronome" / name
        path.write_text(
            "---\n"
            'title: "Metronome source"\n'
            "type: source\n"
            "date_ingested: 2026-07-13\n"
            f'canonical_url: "{canonical_url}"\n'
            "original_format: webpage\n"
            "raw_files:\n"
            f"{raw_list}\n"
            "tags: [metronome]\n"
            "---\n\n"
            "## Overview\n\nSummary.\n\n"
            "## Raw Sources\n\n"
            f"{links}\n",
            encoding="utf-8",
        )

    def test_uningested_raw_page_is_reported_as_pending_not_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_capsule(root)
            raw_file = self.write_raw(root)

            report = inspect_capsule(root)

            self.assertEqual((raw_file,), report.orphan_raw_files)
            self.assertEqual([], validate_capsule(report))

    def test_valid_source_reconciles_raw_links_index_and_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = "source-metronome-guides-home"
            self.make_capsule(root, source_count=1, index_links=(source,))
            self.write_raw(root)
            self.write_source(root)

            report = inspect_capsule(root)

            self.assertEqual((), report.orphan_raw_files)
            self.assertEqual([], validate_capsule(report))

    def test_duplicate_canonical_url_is_an_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_capsule(
                root,
                source_count=2,
                index_links=("source-metronome-guides-home", "source-metronome-guides-home-copy"),
            )
            self.write_raw(root)
            self.write_source(root)
            self.write_source(root, name="source-metronome-guides-home-copy.md")

            errors = validate_capsule(inspect_capsule(root))

            self.assertTrue(any("duplicate canonical_url" in error for error in errors))

    def test_raw_files_and_raw_sources_must_match_in_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = "source-metronome-guides-home"
            self.make_capsule(root, source_count=1, index_links=(source,))
            first = self.write_raw(root)
            second = self.write_raw(root, "guides/home-2026-07-14.md")
            self.write_source(root, raw_files=(second, first), raw_links=(first, second))

            errors = validate_capsule(inspect_capsule(root))

            self.assertTrue(any("raw_files and Raw Sources differ" in error for error in errors))

    def test_source_missing_from_index_is_an_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_capsule(root, source_count=1)
            self.write_raw(root)
            self.write_source(root)

            errors = validate_capsule(inspect_capsule(root))

            self.assertTrue(any("missing from metronome-index" in error for error in errors))

    def test_company_source_count_must_be_derived_from_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = "source-metronome-guides-home"
            self.make_capsule(root, source_count=0, index_links=(source,))
            self.write_raw(root)
            self.write_source(root)

            errors = validate_capsule(inspect_capsule(root))

            self.assertTrue(any("source_count is 0 but found 1" in error for error in errors))

    def test_nonexistent_indexed_source_is_an_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_capsule(root, index_links=("source-metronome-missing",))

            errors = validate_capsule(inspect_capsule(root))

            self.assertTrue(any("indexed source does not exist" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
