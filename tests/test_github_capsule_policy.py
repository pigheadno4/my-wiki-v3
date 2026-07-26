import dataclasses
import hashlib
import json
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
        allowlist = SecretAllowlist("src/token.ts", "a" * 40, "github-token-v1")

        self.assertEqual("internal-runtime-closure", capsule.dependency_scope)
        self.assertEqual("package-owned", capsule.changed_path_policy)
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
            changed_path_policy="policy-bounded",
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
            SecretAllowlist("src/z.ts", "b" * 40, "github-token-v1"),
            SecretAllowlist("src/a.ts", "a" * 40, "github-token-v1"),
            SecretAllowlist("src/ignored.ts", "c" * 40, "github-token-v1"),
            SecretAllowlist("src/not-selected-detector.ts", "d" * 40, "other-detector"),
        )

        policy = build_effective_policy(
            capsule,
            allowlists,
            (("src/z.ts", "b" * 40), ("src/a.ts", "a" * 40), ("src/not-selected-detector.ts", "d" * 40)),
            ("github-token-v1",),
        )
        reordered = build_effective_policy(
            capsule,
            tuple(reversed(allowlists)),
            (("src/a.ts", "a" * 40), ("src/z.ts", "b" * 40), ("src/not-selected-detector.ts", "d" * 40)),
            ("github-token-v1",),
        )

        self.assertEqual(("@scope/a", "@scope/z"), policy.capsule.focus_packages)
        self.assertEqual("policy-bounded", policy.capsule.changed_path_policy)
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

    def test_effective_policy_uses_the_exact_npm_schema_and_canonical_bytes(self):
        policy = build_effective_policy(
            self.capsule(),
            (SecretAllowlist("src/token.ts", "a" * 40, "github-token-v1"),),
            (("src/token.ts", "a" * 40),),
            ("github-token-v1",),
        )
        expected_payload = {
            "adapter": "npm-tracked-source-v1",
            "category_classifier": "excluded-categories-v1",
            "changed_path_policy": "package-owned",
            "default_generated_target_paths": [],
            "default_required_roots": ["src"],
            "dependency_scope": "internal-runtime-closure",
            "excluded_categories": ["fixtures", "stories", "tests"],
            "focus_packages": ["@scope/runtime"],
            "id": "runtime",
            "include_paths": [],
            "max_capsule_files": 120,
            "max_capsule_utf8_bytes": 750000,
            "max_file_bytes": 512000,
            "max_packet_files": 160,
            "max_packet_utf8_bytes": 1000000,
            "package_overrides": [],
            "secret_allowlist": [
                {"path": "src/token.ts", "blob_oid": "a" * 40, "detector_code": "github-token-v1"}
            ],
            "secret_detector": "text-secrets-v1",
            "workspace_resolver": "npm-workspaces-v1",
        }
        expected_bytes = json.dumps(
            expected_payload,
            ensure_ascii=False,
            allow_nan=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")

        self.assertEqual(set(expected_payload), set(json.loads(policy.canonical_bytes)))
        self.assertEqual("excluded-categories-v1", json.loads(policy.canonical_bytes)["category_classifier"])
        self.assertEqual("npm-workspaces-v1", json.loads(policy.canonical_bytes)["workspace_resolver"])
        self.assertEqual(expected_bytes, policy.canonical_bytes)
        self.assertEqual(hashlib.sha256(expected_bytes).hexdigest(), policy.policy_hash)

    def test_changed_path_policy_is_validated_and_hash_bound(self):
        package_owned = build_effective_policy(self.capsule(), (), (), ())
        policy_bounded = build_effective_policy(
            self.capsule(changed_path_policy="policy-bounded"),
            (),
            (),
            (),
        )

        self.assertEqual("package-owned", package_owned.capsule.changed_path_policy)
        self.assertEqual("policy-bounded", policy_bounded.capsule.changed_path_policy)
        self.assertNotEqual(package_owned.policy_hash, policy_bounded.policy_hash)
        with self.assertRaisesRegex(ValueError, "changed_path_policy"):
            build_effective_policy(
                self.capsule(changed_path_policy="unbounded"),
                (),
                (),
                (),
            )

    def test_effective_policy_rejects_duplicate_applicable_allowlist_rows(self):
        allowlist = SecretAllowlist("src/token.ts", "a" * 40, "github-token-v1")

        with self.assertRaisesRegex(ValueError, "duplicate applicable secret allowlist"):
            build_effective_policy(
                self.capsule(),
                (allowlist, allowlist),
                (("src/token.ts", "a" * 40),),
                ("github-token-v1",),
            )


if __name__ == "__main__":
    unittest.main()
