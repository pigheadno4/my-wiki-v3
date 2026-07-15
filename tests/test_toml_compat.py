import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from toml_compat import _load_toml_subset, load_toml  # noqa: E402


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

    def test_fallback_ignores_comments_only_outside_strings(self):
        path = self.write_toml(
            'title = "value # retained" # comment\n'
            'values = ["# retained", 2] # comment\n'
        )

        data = _load_toml_subset(path)

        self.assertEqual("value # retained", data["title"])
        self.assertEqual(["# retained", 2], data["values"])

    def test_fallback_reports_malformed_source_line(self):
        path = self.write_toml('title = "valid"\nvalues = ["missing"\n')

        with self.assertRaisesRegex(ValueError, r"line 2"):
            _load_toml_subset(path)

    def test_public_loader_reads_existing_psp_config(self):
        data = load_toml(ROOT / "scripts" / "psp_config.toml")

        self.assertEqual("docs.stripe.com", data["stripe"]["host"])
        self.assertEqual(2, len(data["adyen"]["discovery"]))


if __name__ == "__main__":
    unittest.main()
