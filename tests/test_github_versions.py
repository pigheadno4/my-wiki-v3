import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_versions import (  # noqa: E402
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


if __name__ == "__main__":
    unittest.main()
