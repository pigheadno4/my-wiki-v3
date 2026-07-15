import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from toml_compat import _load_toml_subset  # noqa: E402


class TomlCompatTests(unittest.TestCase):
    def write_toml(self, text):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "config.toml"
        path.write_text(text, encoding="utf-8")
        return path

    def test_fallback_loads_multiline_arrays_and_array_tables(self):
        path = self.write_toml(
            '[[repos]]\n'
            'id = "paypal/paypal-js"\n'
            'requested_refs = [\n'
            '  "default-branch",\n'
            '  "package:@paypal/react-paypal-js@9",\n'
            ']\n'
            '\n'
            '[metadata]\n'
            'enabled = true\n'
        )

        data = _load_toml_subset(path)

        self.assertEqual(
            ["default-branch", "package:@paypal/react-paypal-js@9"],
            data["repos"][0]["requested_refs"],
        )
        self.assertTrue(data["metadata"]["enabled"])

    def test_fallback_preserves_hashes_and_escaped_quotes_inside_strings(self):
        path = self.write_toml(
            'title = "value # retained" # comment\n'
            'escaped = "quote: \\" # retained" # comment\n'
            'values = ["# retained", "value#retained", 2] # comment\n'
        )

        data = _load_toml_subset(path)

        self.assertEqual("value # retained", data["title"])
        self.assertEqual('quote: " # retained', data["escaped"])
        self.assertEqual(["# retained", "value#retained", 2], data["values"])

    def test_fallback_reports_unterminated_array_source_line(self):
        path = self.write_toml('title = "valid"\nvalues = ["missing"\n')

        with self.assertRaisesRegex(ValueError, r"line 2"):
            _load_toml_subset(path)

    def test_fallback_reports_malformed_multiline_json_source_line(self):
        path = self.write_toml(
            'values = [\n'
            '  "valid",\n'
            '  broken\n'
            ']\n'
        )

        with self.assertRaisesRegex(ValueError, r"line 3"):
            _load_toml_subset(path)

    def test_fallback_rejects_unmatched_closing_brackets(self):
        path = self.write_toml('[[parent]]]\n')

        with self.assertRaisesRegex(ValueError, r"line 1: malformed table header"):
            _load_toml_subset(path)

    def test_fallback_rejects_duplicate_scalar_key_at_later_line(self):
        path = self.write_toml('title = "first"\ntitle = "second"\n')

        with self.assertRaisesRegex(ValueError, r"line 2: duplicate key title"):
            _load_toml_subset(path)

    def test_fallback_rejects_duplicate_normal_table_at_later_line(self):
        path = self.write_toml('[metadata]\nenabled = true\n[metadata]\n')

        with self.assertRaisesRegex(ValueError, r"line 3: duplicate table metadata"):
            _load_toml_subset(path)

    def test_fallback_supports_nested_array_tables(self):
        path = self.write_toml(
            '[[parent]]\n'
            'name = "first"\n'
            '[[parent.child]]\n'
            'name = "first-child"\n'
            '[[parent.child]]\n'
            'name = "second-child"\n'
            '[[parent]]\n'
            'name = "second"\n'
            '[[parent.child]]\n'
            'name = "third-child"\n'
        )

        data = _load_toml_subset(path)

        self.assertEqual(
            ["first-child", "second-child"],
            [child["name"] for child in data["parent"][0]["child"]],
        )
        self.assertEqual(
            ["third-child"],
            [child["name"] for child in data["parent"][1]["child"]],
        )

    def test_fallback_reads_existing_psp_config(self):
        data = _load_toml_subset(ROOT / "scripts" / "psp_config.toml")

        self.assertEqual("docs.stripe.com", data["stripe"]["host"])
        self.assertEqual(2, len(data["adyen"]["discovery"]))


if __name__ == "__main__":
    unittest.main()
