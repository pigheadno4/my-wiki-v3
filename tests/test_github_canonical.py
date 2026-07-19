import hashlib
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_canonical import (  # noqa: E402
    canonical_json_bytes,
    canonical_sha256,
    readable_label,
    safe_policy_path,
    validate_npm_package_name,
)


class CanonicalJsonTests(unittest.TestCase):
    def test_sorts_object_keys_but_preserves_semantic_array_order(self):
        value = {"z": ["last", {"b": 2, "a": 1}], "a": "first"}

        self.assertEqual(
            b'{"a":"first","z":["last",{"a":1,"b":2}]}',
            canonical_json_bytes(value),
        )

    def test_uses_utf8_without_insignificant_whitespace_or_trailing_newline(self):
        encoded = canonical_json_bytes({"message": "支付", "items": ["一", "二"]})

        self.assertEqual('{"items":["一","二"],"message":"支付"}'.encode("utf-8"), encoded)
        self.assertEqual("支付".encode("utf-8") in encoded, True)
        self.assertNotIn(b"\n", encoded)
        self.assertEqual(hashlib.sha256(encoded).hexdigest(), canonical_sha256({"message": "支付", "items": ["一", "二"]}))


class NpmPackageNameTests(unittest.TestCase):
    def test_accepts_scoped_names_whose_package_component_starts_with_dot_or_underscore(self):
        self.assertTrue(validate_npm_package_name("@scope/.pkg"))
        self.assertTrue(validate_npm_package_name("@scope/_pkg"))
        self.assertTrue(validate_npm_package_name("plain.pkg~1"))

    def test_rejects_invalid_scopes_and_unscoped_leading_dot_or_underscore(self):
        invalid = (
            "@.scope/pkg",
            "@_scope/pkg",
            ".pkg",
            "_pkg",
            "@scope/",
            "@scope/pkg/extra",
            "@scope/pkg@1.2.3",
            "@Scope/pkg",
            "plain/pkg",
            "plain%pkg",
            "plain pkg",
        )

        for name in invalid:
            with self.subTest(name=name):
                self.assertFalse(validate_npm_package_name(name))

    def test_rejects_names_over_the_214_byte_limit(self):
        self.assertFalse(validate_npm_package_name("a" * 215))
        self.assertTrue(validate_npm_package_name("a" * 214))


class PolicyPathTests(unittest.TestCase):
    def test_accepts_safe_relative_posix_paths(self):
        for path in ("src/index.ts", "packages/example/package.json", "types"):
            with self.subTest(path=path):
                self.assertTrue(safe_policy_path(path))

    def test_rejects_absolute_navigation_empty_and_non_posix_paths(self):
        invalid = (
            "",
            "/src/index.ts",
            "./src/index.ts",
            "src/../package.json",
            "src/./index.ts",
            "src//index.ts",
            "src/index.ts/",
            "src\\index.ts",
            ".",
            "..",
        )

        for path in invalid:
            with self.subTest(path=path):
                self.assertFalse(safe_policy_path(path))


class ReadableLabelTests(unittest.TestCase):
    def test_normalizes_to_a_bounded_ascii_label_with_fallback(self):
        self.assertEqual("paypal-react-sdk", readable_label("PayPal / React SDK"))
        self.assertEqual("capsule", readable_label("!!!"))
        self.assertLessEqual(len(readable_label("A" * 100).encode("ascii")), 40)

    def test_truncation_does_not_leave_a_separator_at_the_boundary(self):
        self.assertEqual("a" * 39, readable_label("a" * 39 + "-tail"))


if __name__ == "__main__":
    unittest.main()
