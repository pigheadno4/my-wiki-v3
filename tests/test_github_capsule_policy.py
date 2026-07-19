import dataclasses
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_capsule_policy import (  # noqa: E402
    CapsuleConfig,
    PackageOverride,
    SecretAllowlist,
    build_effective_policy,
)


class EffectivePolicyTests(unittest.TestCase):
    def capsule(self, **overrides):
        values = {
            "id": "runtime",
            "adapter": "npm-tracked-source-v1",
            "focus_packages": ("@scope/runtime",),
        }
        values.update(overrides)
        return CapsuleConfig(**values)

    def test_frozen_policy_records_apply_exact_defaults(self):
        capsule = self.capsule()
        override = PackageOverride("@scope/internal", ("src",), (), ())
        allowlist = SecretAllowlist("src/token.ts", "a" * 40, "text-secrets-v1:generic-token")

        self.assertEqual("internal-runtime-closure", capsule.dependency_scope)
        self.assertEqual(("src",), capsule.default_required_roots)
        self.assertEqual((), capsule.default_generated_target_paths)
        self.assertEqual((), capsule.include_paths)
        self.assertEqual(("fixtures", "stories", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(120, capsule.max_capsule_files)
        self.assertEqual(750000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(160, capsule.max_packet_files)
        self.assertEqual(1000000, capsule.max_packet_utf8_bytes)
        with self.assertRaises(dataclasses.FrozenInstanceError):
            capsule.id = "changed"
        with self.assertRaises(dataclasses.FrozenInstanceError):
            override.name = "changed"
        with self.assertRaises(dataclasses.FrozenInstanceError):
            allowlist.path = "changed"

    def test_effective_policy_canonicalizes_nested_values_and_applicable_allowlist(self):
        capsule = self.capsule(
            focus_packages=("@scope/z", "@scope/a"),
            default_required_roots=("types", "src"),
            default_generated_target_paths=("index.js", "dist/"),
            include_paths=("extra", "config"),
            excluded_categories=("stories", "tests", "fixtures"),
            package_overrides=(
                PackageOverride("@scope/z", ("types", "src"), ("dist/", "index.js"), ("extra",)),
                PackageOverride("@scope/a", ("src",), (), ("config",)),
            ),
        )
        allowlists = (
            SecretAllowlist("src/z.ts", "b" * 40, "text-secrets-v1:generic-token"),
            SecretAllowlist("src/a.ts", "a" * 40, "text-secrets-v1:generic-token"),
            SecretAllowlist("src/ignored.ts", "c" * 40, "text-secrets-v1:generic-token"),
            SecretAllowlist("src/not-selected-detector.ts", "d" * 40, "other-detector"),
        )

        policy = build_effective_policy(
            capsule,
            allowlists,
            (("src/z.ts", "b" * 40), ("src/a.ts", "a" * 40), ("src/not-selected-detector.ts", "d" * 40)),
            ("text-secrets-v1:generic-token",),
        )
        reordered = build_effective_policy(
            capsule,
            tuple(reversed(allowlists)),
            (("src/a.ts", "a" * 40), ("src/z.ts", "b" * 40), ("src/not-selected-detector.ts", "d" * 40)),
            ("text-secrets-v1:generic-token",),
        )

        self.assertEqual(("@scope/a", "@scope/z"), policy.capsule.focus_packages)
        self.assertEqual(("src", "types"), policy.capsule.default_required_roots)
        self.assertEqual(("dist/", "index.js"), policy.capsule.default_generated_target_paths)
        self.assertEqual(("config", "extra"), policy.capsule.include_paths)
        self.assertEqual(("fixtures", "stories", "tests"), policy.capsule.excluded_categories)
        self.assertEqual(("@scope/a", "@scope/z"), tuple(item.name for item in policy.capsule.package_overrides))
        self.assertEqual(
            ("src/a.ts", "src/z.ts"),
            tuple(item.path for item in policy.applicable_secret_allowlist),
        )
        self.assertEqual(policy.policy_hash, reordered.policy_hash)
        self.assertRegex(policy.policy_hash, r"^[0-9a-f]{64}$")
        with self.assertRaises(dataclasses.FrozenInstanceError):
            policy.policy_hash = "0" * 64


if __name__ == "__main__":
    unittest.main()
