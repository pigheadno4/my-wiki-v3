import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_versions import (  # noqa: E402
    SemanticVersion,
    compare_semver,
    matches_semver,
    parse_package_tag,
    parse_semver,
)


class GitHubVersionTests(unittest.TestCase):
    def test_major_selector_excludes_newer_prerelease_by_default(self):
        target = parse_semver("10")
        stable = parse_semver("10.1.5")
        prerelease = parse_semver("10.2.0-beta.1")
        self.assertTrue(matches_semver(stable, target))
        self.assertFalse(matches_semver(prerelease, target))

    def test_major_selector_can_include_prereleases_when_requested(self):
        target = parse_semver("10")
        prerelease = parse_semver("10.2.0-beta.1")

        self.assertFalse(matches_semver(prerelease, target))
        self.assertTrue(matches_semver(prerelease, target, include_prerelease=True))

    def test_exact_prerelease_matches_only_itself(self):
        target = parse_semver("10.2.0-beta.1")
        self.assertTrue(matches_semver(parse_semver("10.2.0-beta.1"), target))
        self.assertFalse(matches_semver(parse_semver("10.2.0"), target))

    def test_semver_precedence_handles_numeric_prerelease_identifiers(self):
        self.assertLess(
            compare_semver(parse_semver("10.0.0-rc.2"), parse_semver("10.0.0-rc.10")),
            0,
        )

    def test_parser_accepts_optional_leading_v(self):
        version = parse_semver("v10.2.0")

        self.assertEqual(10, version.major)
        self.assertEqual(2, version.minor)
        self.assertEqual(0, version.patch)
        self.assertTrue(version.is_exact)

    def test_parser_accepts_scoped_package_tags(self):
        self.assertEqual(
            ("@scope/name", "v10.2.0"),
            parse_package_tag("@scope/name@v10.2.0"),
        )

    def test_parser_accepts_unscoped_package_tags(self):
        self.assertEqual(
            ("braintree-web", "3.112.1"),
            parse_package_tag("braintree-web@3.112.1"),
        )

    def test_parser_accepts_composer_package_tags(self):
        self.assertEqual(
            ("paypal/paypal-server-sdk", "2.4.0"),
            parse_package_tag("paypal/paypal-server-sdk@2.4.0"),
        )

    def test_parser_accepts_case_sensitive_non_npm_release_identity(self):
        self.assertEqual(
            ("BraintreeDropIn", "9.14.0"),
            parse_package_tag("BraintreeDropIn@9.14.0"),
        )

    def test_parser_accepts_build_metadata_without_affecting_precedence(self):
        with_build = parse_semver("1.2.3+build.7")
        other_build = parse_semver("1.2.3+build.8")

        self.assertIsNotNone(with_build)
        self.assertEqual(0, compare_semver(with_build, other_build))
        self.assertEqual(
            ("@scope/name", "1.2.3+build.7"),
            parse_package_tag("@scope/name@1.2.3+build.7"),
        )

    def test_parser_rejects_malformed_semver(self):
        malformed = (
            "01",
            "1.02",
            "1.2.03",
            "1.2.3-01",
            "1.2.3-rc.01",
            "1.2.3-",
            "1.2.3-rc..1",
            "1.2.3+",
            "1.2.3+build..7",
            "1.2.3+build$",
            "1-beta",
            "1.2-beta",
            "1+build",
            "1.2+build",
        )

        for value in malformed:
            with self.subTest(value=value):
                self.assertIsNone(parse_semver(value))

    def test_exact_targets_require_exact_candidates(self):
        self.assertFalse(matches_semver(parse_semver("1.2"), parse_semver("1.2.0")))
        self.assertFalse(
            matches_semver(
                SemanticVersion(1, 2, None, ("rc", "1"), False),
                parse_semver("1.2.0-rc.1"),
            )
        )


if __name__ == "__main__":
    unittest.main()
