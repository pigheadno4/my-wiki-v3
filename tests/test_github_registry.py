import dataclasses
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_registry import (  # noqa: E402
    RepoConfig,
    VersionTrack,
    load_registry,
    select_repos,
    validate_enabled_policy,
    validate_registry,
)
from github_capsule_policy import CapsuleConfig, PackageOverride, SecretAllowlist  # noqa: E402
from toml_compat import load_toml  # noqa: E402


APPENDIX_A_INVENTORY = (
    ('paypal/paypal-messaging-components', 'https://github.com/paypal/paypal-messaging-components', 'web-component', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('paypal/paypal-checkout-components', 'https://github.com/paypal/paypal-checkout-components', 'web-component', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('paypal/paypal-android', 'https://github.com/paypal/paypal-android', 'mobile-sdk', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('paypal/paypal-sdk-release', 'https://github.com/paypal/paypal-sdk-release', 'release-index', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('paypal/paypal-js', 'https://github.com/paypal/paypal-js', 'web-sdk', 'tier1', 'monorepo-packages', True, 'releases-and-default-branch', 'weekly'),
    ('paypal/paypal-ios', 'https://github.com/paypal/paypal-ios', 'mobile-sdk', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('paypal/postman-collections', 'https://github.com/paypal/postman-collections', 'api-collection', 'tier2', 'commit', True, 'default-branch', 'monthly'),
    ('paypal/paypal-typescript-server-sdk', 'https://github.com/paypal/PayPal-TypeScript-Server-SDK', 'server-sdk', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('paypal/paypal-php-server-sdk', 'https://github.com/paypal/PayPal-PHP-Server-SDK', 'server-sdk', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('paypal/paypal-messages-ios', 'https://github.com/paypal/paypal-messages-ios', 'messaging-sdk', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('paypal/paypal-messages-android', 'https://github.com/paypal/paypal-messages-android', 'messaging-sdk', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('paypal/paypal-sdk-logos', 'https://github.com/paypal/paypal-sdk-logos', 'assets', 'tier2', 'commit', True, 'default-branch', 'monthly'),
    ('paypal/paypal-rest-api-specifications', 'https://github.com/paypal/paypal-rest-api-specifications', 'api-specification', 'tier1', 'commit', True, 'default-branch', 'monthly'),
    ('paypal-examples/v6-web-sdk-sample-integration', 'https://github.com/paypal-examples/v6-web-sdk-sample-integration', 'sample-app', 'tier1', 'commit', True, 'default-branch', 'monthly'),
    ('paypal-examples/v6-web-sdk-with-braintree-sdk-sample-integration', 'https://github.com/paypal-examples/v6-web-sdk-with-braintree-sdk-sample-integration', 'sample-app', 'tier1', 'commit', True, 'default-branch', 'monthly'),
    ('paypal-examples/paypal-android-sdk-demo-app', 'https://github.com/paypal-examples/paypal-android-sdk-demo-app', 'sample-app', 'tier1', 'commit', True, 'default-branch', 'monthly'),
    ('paypal-examples/paypal-sdk-server-side-integration', 'https://github.com/paypal-examples/paypal-sdk-server-side-integration', 'sample-app', 'tier1', 'commit', True, 'default-branch', 'monthly'),
    ('paypal-examples/paypal-ios-sdk-demo-app', 'https://github.com/paypal-examples/paypal-ios-sdk-demo-app', 'sample-app', 'tier1', 'commit', True, 'default-branch', 'monthly'),
    ('braintree/braintree_android', 'https://github.com/braintree/braintree_android', 'mobile-sdk', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('braintree/braintree_ios', 'https://github.com/braintree/braintree_ios', 'mobile-sdk', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('braintree/web-sdk-github-actions', 'https://github.com/braintree/web-sdk-github-actions', 'automation', 'tier3', 'commit', False, 'default-branch', 'on-demand'),
    ('braintree/mobile-sdk-tooling', 'https://github.com/braintree/mobile-sdk-tooling', 'tooling', 'tier3', 'commit', True, 'default-branch', 'on-demand'),
    ('braintree/graphql-api', 'https://github.com/braintree/graphql-api', 'api-specification', 'tier1', 'commit', True, 'default-branch', 'monthly'),
    ('braintree/credit-card-type', 'https://github.com/braintree/credit-card-type', 'utility', 'tier3', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('braintree/braintree-web', 'https://github.com/braintree/braintree-web', 'web-sdk', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('braintree/uuid', 'https://github.com/braintree/uuid', 'utility', 'tier3', 'semver-tags', False, 'releases-and-default-branch', 'monthly'),
    ('braintree/popup-bridge-ios', 'https://github.com/braintree/popup-bridge-ios', 'mobile-utility', 'tier3', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('braintree/restricted-input', 'https://github.com/braintree/restricted-input', 'web-utility', 'tier3', 'commit', True, 'default-branch', 'monthly'),
    ('braintree/braintree-web-drop-in', 'https://github.com/braintree/braintree-web-drop-in', 'drop-in', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('braintree/popup-bridge-android', 'https://github.com/braintree/popup-bridge-android', 'mobile-utility', 'tier3', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('braintree/braintree_php', 'https://github.com/braintree/braintree_php', 'server-sdk', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('braintree/braintree_ruby', 'https://github.com/braintree/braintree_ruby', 'server-sdk', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('braintree/braintree_node', 'https://github.com/braintree/braintree_node', 'server-sdk', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('braintree/braintree-ios-drop-in', 'https://github.com/braintree/braintree-ios-drop-in', 'drop-in', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('braintree/braintree-android-drop-in', 'https://github.com/braintree/braintree-android-drop-in', 'drop-in', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('stripe/stripe-ios', 'https://github.com/stripe/stripe-ios', 'mobile-sdk', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('stripe/stripe-apps', 'https://github.com/stripe/stripe-apps', 'developer-platform', 'tier2', 'commit', True, 'default-branch', 'monthly'),
    ('stripe/stripe-cli', 'https://github.com/stripe/stripe-cli', 'cli', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('stripe/stripe-android', 'https://github.com/stripe/stripe-android', 'mobile-sdk', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('stripe/link-cli', 'https://github.com/stripe/link-cli', 'cli', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('stripe/stripe-react-native', 'https://github.com/stripe/stripe-react-native', 'mobile-sdk', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('stripe/stripe-ios-spm', 'https://github.com/stripe/stripe-ios-spm', 'release-mirror', 'tier3', 'commit', False, 'default-branch', 'on-demand'),
    ('stripe/stripe-php', 'https://github.com/stripe/stripe-php', 'server-sdk', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('stripe/stripe-node', 'https://github.com/stripe/stripe-node', 'server-sdk', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('stripe/stripe-js', 'https://github.com/stripe/stripe-js', 'web-sdk', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('stripe/sync-engine', 'https://github.com/stripe/sync-engine', 'tooling', 'tier2', 'commit', True, 'default-branch', 'monthly'),
    ('stripe/react-stripe-js', 'https://github.com/stripe/react-stripe-js', 'web-sdk', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('stripe/stripe-terminal-ios', 'https://github.com/stripe/stripe-terminal-ios', 'terminal-sdk', 'tier1', 'semver-tags', False, 'releases-and-default-branch', 'weekly'),
    ('stripe/stripe-terminal-android', 'https://github.com/stripe/stripe-terminal-android', 'terminal-sdk', 'tier1', 'semver-tags', False, 'releases-and-default-branch', 'weekly'),
    ('stripe/ai', 'https://github.com/stripe/ai', 'developer-tooling', 'tier2', 'commit', True, 'default-branch', 'monthly'),
    ('metronome-industries/metronome-node', 'https://github.com/Metronome-Industries/metronome-node', 'server-sdk', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('metronome-industries/ai', 'https://github.com/Metronome-Industries/ai', 'developer-tooling', 'tier2', 'commit', True, 'default-branch', 'monthly'),
    ('metronome-industries/ai-eval', 'https://github.com/Metronome-Industries/ai-eval', 'evaluation-tooling', 'tier3', 'commit', False, 'default-branch', 'on-demand'),
    ('metronome-industries/mintlify-docs', 'https://github.com/Metronome-Industries/mintlify-docs', 'docs-source', 'tier2', 'commit', False, 'default-branch', 'monthly'),
    ('metronome-industries/terraform-provider-metronome', 'https://github.com/Metronome-Industries/terraform-provider-metronome', 'terraform-provider', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('adyen/adyen-node-api-library', 'https://github.com/Adyen/adyen-node-api-library', 'server-sdk', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('adyen/adyen-react-native', 'https://github.com/Adyen/adyen-react-native', 'mobile-sdk', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('adyen/adyen-web', 'https://github.com/Adyen/adyen-web', 'web-sdk', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('adyen/adyen-android', 'https://github.com/Adyen/adyen-android', 'mobile-sdk', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('adyen/adyen-ios', 'https://github.com/Adyen/adyen-ios', 'mobile-sdk', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
    ('adyen/adyen-magento2', 'https://github.com/Adyen/adyen-magento2', 'commerce-plugin', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('adyen/adyen-pos-mobile-ios', 'https://github.com/Adyen/adyen-pos-mobile-ios', 'terminal-sdk', 'tier1', 'semver-tags', False, 'releases-and-default-branch', 'weekly'),
    ('adyen/adyen-pos-mobile-ios-test', 'https://github.com/Adyen/adyen-pos-mobile-ios-test', 'test-tooling', 'tier3', 'commit', False, 'default-branch', 'on-demand'),
    ('adyen/adyen-postman', 'https://github.com/Adyen/adyen-postman', 'api-collection', 'tier2', 'commit', True, 'default-branch', 'monthly'),
    ('adyen/adyen-php-api-library', 'https://github.com/Adyen/adyen-php-api-library', 'server-sdk', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('adyen/adyen-sdk-automation', 'https://github.com/Adyen/adyen-sdk-automation', 'automation', 'tier3', 'commit', True, 'default-branch', 'on-demand'),
    ('adyen/release-automation-action', 'https://github.com/Adyen/release-automation-action', 'automation', 'tier3', 'commit', True, 'default-branch', 'on-demand'),
    ('adyen/adyen-3ds2-ios-swift', 'https://github.com/Adyen/adyen-3ds2-ios-swift', 'authentication-sdk', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('adyen/adyen-wechatpay-ios', 'https://github.com/Adyen/adyen-wechatpay-ios', 'payment-method-sdk', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('adyen/adyen-3ds2-android', 'https://github.com/Adyen/adyen-3ds2-android', 'authentication-sdk', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
    ('adyen/adyen-3ds2-ios', 'https://github.com/Adyen/adyen-3ds2-ios', 'authentication-sdk', 'tier2', 'semver-tags', True, 'releases-and-default-branch', 'monthly'),
)


class RegistryTests(unittest.TestCase):
    def write_registry(self, text):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "repo-registry.toml"
        path.write_text(text, encoding="utf-8")
        return path

    def repo(self, **overrides):
        values = {
            "id": "paypal/paypal-js",
            "company": "paypal",
            "url": "https://github.com/paypal/paypal-js",
            "enabled": True,
            "repo_type": "web-sdk",
            "priority": "tier1",
            "track": "releases-and-default-branch",
            "version_strategy": "monorepo-packages",
        }
        values.update(overrides)
        return RepoConfig(**values)

    def test_loads_multiline_arrays_and_repo_tables(self):
        data = load_toml(self.write_registry(
            '[[repos]]\n'
            'id = "paypal/paypal-js"\n'
            'company = "paypal"\n'
            'url = "https://github.com/paypal/paypal-js"\n'
            'enabled = true\n'
            'repo_type = "web-sdk"\n'
            'priority = "tier1"\n'
            'track = "releases-and-default-branch"\n'
            'version_strategy = "monorepo-packages"\n'
            'requested_refs = [\n'
            '  "default-branch",\n'
            '  "package:@paypal/react-paypal-js@9",\n'
            ']\n'
        ))

        self.assertEqual(2, len(data["repos"][0]["requested_refs"]))

    def test_registry_applies_optional_field_defaults_and_is_immutable(self):
        repo = self.repo(enabled=False)

        self.assertEqual("on-demand", repo.collection_frequency)
        self.assertEqual((), repo.requested_refs)
        self.assertEqual((), repo.key_paths)
        self.assertEqual((), repo.exclude_paths)
        self.assertEqual(1048576, repo.max_file_bytes)
        self.assertEqual(10485760, repo.max_snapshot_bytes)
        self.assertEqual((), repo.version_tracks)
        self.assertEqual((), repo.capsules)
        self.assertEqual((), repo.secret_allowlist)
        self.assertEqual((), repo.ingest_required_paths)
        with self.assertRaises(dataclasses.FrozenInstanceError):
            repo.enabled = False

    def test_registry_rejects_unsafe_filesystem_components(self):
        unsafe = (
            self.repo(company="../outside"),
            self.repo(
                id="../paypal-js",
                url="https://github.com/../paypal-js",
            ),
            self.repo(
                id="paypal/..",
                url="https://github.com/paypal/..",
            ),
        )

        for repo in unsafe:
            with self.subTest(repo=repo):
                self.assertTrue(
                    any("safe lowercase path component" in error for error in validate_registry((repo,)))
                )

    def test_enabled_release_repository_requires_runnable_package_policy(self):
        no_policy = self.repo(enabled=True)
        no_capsule = self.repo(
            enabled=True,
            version_tracks=(
                VersionTrack("package:@paypal/paypal-js@10", "all-stable", "all-stable"),
            ),
        )

        self.assertIn("enabled repository requires version tracks", validate_enabled_policy(no_policy))
        self.assertIn(
            "enabled repository requires exactly one capsule",
            validate_enabled_policy(no_capsule),
        )

    def test_enabled_commit_repository_requires_default_branch_commit_policy(self):
        commit_capsule = CapsuleConfig(
            id="sample-source",
            adapter="commit-tree-v1",
            source_id="sample",
            dependency_scope="configured-repository-paths",
            changed_path_policy="policy-bounded",
        )
        valid = self.repo(
            id="paypal-examples/sample",
            url="https://github.com/paypal-examples/sample",
            track="default-branch",
            version_strategy="commit",
            capsules=(commit_capsule,),
        )

        self.assertEqual([], validate_enabled_policy(valid))

        invalid_rows = (
            (
                self.repo(
                    id="paypal-examples/sample",
                    url="https://github.com/paypal-examples/sample",
                    version_strategy="commit",
                    capsules=(commit_capsule,),
                ),
                "default-branch tracking",
            ),
            (
                self.repo(
                    id="paypal-examples/sample",
                    url="https://github.com/paypal-examples/sample",
                    track="default-branch",
                    version_strategy="commit",
                    version_tracks=(VersionTrack("package:sample@1", "none", "none"),),
                    capsules=(commit_capsule,),
                ),
                "must not define version tracks",
            ),
            (
                self.repo(
                    id="paypal-examples/sample",
                    url="https://github.com/paypal-examples/sample",
                    track="default-branch",
                    version_strategy="commit",
                ),
                "exactly one commit capsule",
            ),
            (
                self.repo(
                    id="paypal-examples/sample",
                    url="https://github.com/paypal-examples/sample",
                    track="default-branch",
                    version_strategy="commit",
                    capsules=(CapsuleConfig(
                        id="release-source",
                        adapter="npm-tracked-source-v1",
                        focus_packages=("sample",),
                    ),),
                ),
                "commit-tree-v1 capsule",
            ),
            (
                self.repo(
                    id="paypal-examples/sample",
                    url="https://github.com/paypal-examples/sample",
                    track="default-branch",
                    version_strategy="commit",
                    capsules=(CapsuleConfig(
                        id="commit-source",
                        adapter="commit-tree-v1",
                        dependency_scope="configured-repository-paths",
                    ),),
                ),
                "safe source_id",
            ),
        )

        for repo, message in invalid_rows:
            with self.subTest(message=message):
                self.assertTrue(
                    any(message in error for error in validate_enabled_policy(repo)),
                    validate_enabled_policy(repo),
                )

    def test_registry_loads_immutable_nested_version_tracks_in_order(self):
        path = self.write_registry(
            '[[repos]]\n'
            'id = "paypal/paypal-js"\n'
            'company = "paypal"\n'
            'url = "https://github.com/paypal/paypal-js"\n'
            'enabled = true\n'
            'repo_type = "web-sdk"\n'
            'priority = "tier1"\n'
            'track = "releases-and-default-branch"\n'
            'version_strategy = "monorepo-packages"\n'
            '[[repos.version_tracks]]\n'
            'selector = "package:@scope/name@10"\n'
            'backfill = "all-stable"\n'
            'future = "all-stable"\n'
            '[[repos.version_tracks]]\n'
            'selector = "package:@scope/name@9"\n'
            'backfill = "minor-baselines"\n'
            'future = "none"\n'
            'include_prerelease = true\n'
            'pinned_versions = ["9.0.1", "9.2.0-rc.1"]\n'
        )

        repo = load_registry(path)[0]

        self.assertEqual(
            (
                VersionTrack("package:@scope/name@10", "all-stable", "all-stable"),
                VersionTrack("package:@scope/name@9", "minor-baselines", "none", True, ("9.0.1", "9.2.0-rc.1")),
            ),
            repo.version_tracks,
        )
        with self.assertRaises(dataclasses.FrozenInstanceError):
            repo.version_tracks[0].future = "all-stable"

    def test_registry_accepts_latest_stable_and_rejects_unknown_latest_policy(self):
        template = (
            '[[repos]]\n'
            'id = "paypal/paypal-js"\n'
            'company = "paypal"\n'
            'url = "https://github.com/paypal/paypal-js"\n'
            'enabled = true\n'
            'repo_type = "web-sdk"\n'
            'priority = "tier1"\n'
            'track = "releases-and-default-branch"\n'
            'version_strategy = "monorepo-packages"\n'
            '[[repos.version_tracks]]\n'
            'selector = "package:@paypal/paypal-js@9"\n'
            'backfill = "{backfill}"\n'
            'future = "none"\n'
        )

        repo = load_registry(
            self.write_registry(template.format(backfill="latest-stable"))
        )[0]

        self.assertEqual("latest-stable", repo.version_tracks[0].backfill)
        with self.assertRaisesRegex(ValueError, "unknown backfill policy latest-major"):
            load_registry(self.write_registry(template.format(backfill="latest-major")))

    def test_registry_loads_exact_capsule_policy_and_repository_allowlist(self):
        path = self.write_registry(
            '[[repos]]\n'
            'id = "paypal/paypal-js"\n'
            'company = "paypal"\n'
            'url = "https://github.com/paypal/paypal-js"\n'
            'enabled = true\n'
            'repo_type = "web-sdk"\n'
            'priority = "tier1"\n'
            'track = "releases-and-default-branch"\n'
            'version_strategy = "monorepo-packages"\n'
            '[[repos.capsules]]\n'
            'id = "react-runtime"\n'
            'adapter = "npm-tracked-source-v1"\n'
            'focus_packages = ["@scope/z", "@scope/a"]\n'
            'changed_path_policy = "policy-bounded"\n'
            'default_required_roots = ["types", "src"]\n'
            'default_generated_target_paths = ["index.js", "dist/"]\n'
            'include_paths = ["extra", "config"]\n'
            'excluded_categories = ["stories", "tests"]\n'
            '[[repos.capsules.package_overrides]]\n'
            'name = "@scope/internal"\n'
            'required_roots = ["src", "types"]\n'
            'generated_target_paths = ["dist/"]\n'
            'include_paths = ["config"]\n'
            '[[repos.secret_allowlist]]\n'
            'path = "packages/runtime/src/token.ts"\n'
            'blob_oid = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"\n'
            'detector_code = "github-token-v1"\n'
        )

        repo = load_registry(path)[0]

        self.assertEqual(
            CapsuleConfig(
                "react-runtime",
                "npm-tracked-source-v1",
                ("@scope/a", "@scope/z"),
                changed_path_policy="policy-bounded",
                default_required_roots=("src", "types"),
                default_generated_target_paths=("dist/", "index.js"),
                include_paths=("config", "extra"),
                excluded_categories=("stories", "tests"),
                package_overrides=(
                    PackageOverride("@scope/internal", ("src", "types"), ("dist/",), ("config",)),
                ),
            ),
            repo.capsules[0],
        )
        self.assertEqual(
            (SecretAllowlist("packages/runtime/src/token.ts", "a" * 40, "github-token-v1"),),
            repo.secret_allowlist,
        )

    def test_registry_rejects_invalid_capsule_and_allowlist_policy(self):
        base = (
            '[[repos]]\n'
            'id = "paypal/paypal-js"\n'
            'company = "paypal"\n'
            'url = "https://github.com/paypal/paypal-js"\n'
            'enabled = true\n'
            'repo_type = "web-sdk"\n'
            'priority = "tier1"\n'
            'track = "releases-and-default-branch"\n'
            'version_strategy = "monorepo-packages"\n'
        )
        invalid = (
            '[[repos.capsules]]\nid = "bad_slug"\nadapter = "npm-tracked-source-v1"\nfocus_packages = ["@scope/runtime"]\n',
            '[[repos.capsules]]\nid = "runtime"\nadapter = "unknown"\nfocus_packages = ["@scope/runtime"]\n',
            '[[repos.capsules]]\nid = "runtime"\nadapter = "npm-tracked-source-v1"\nfocus_packages = ["@scope/runtime", "@scope/runtime"]\n',
            '[[repos.capsules]]\nid = "runtime"\nadapter = "npm-tracked-source-v1"\nfocus_packages = ["@scope/runtime"]\ndefault_required_roots = ["../outside"]\n',
            '[[repos.capsules]]\nid = "runtime"\nadapter = "npm-tracked-source-v1"\nfocus_packages = ["@scope/runtime"]\ndefault_generated_target_paths = ["dist//"]\n',
            '[[repos.capsules]]\nid = "runtime"\nadapter = "npm-tracked-source-v1"\nfocus_packages = ["@scope/runtime"]\ndefault_required_roots = ["src"]\ndefault_generated_target_paths = ["src/index.js"]\n',
            '[[repos.capsules]]\nid = "runtime"\nadapter = "npm-tracked-source-v1"\nfocus_packages = ["@scope/runtime"]\nchanged_path_policy = "unbounded"\n',
            '[[repos.capsules]]\nid = "runtime"\nadapter = "npm-tracked-source-v1"\nfocus_packages = ["@scope/runtime"]\nunknown = "value"\n',
            '[[repos.capsules]]\nid = "runtime"\nadapter = "npm-tracked-source-v1"\nfocus_packages = ["@scope/runtime"]\n[[repos.capsules.package_overrides]]\nname = "@scope/runtime"\nrequired_roots = ["src"]\ngenerated_target_paths = []\n',
            '[[repos.secret_allowlist]]\npath = "src\\\\token.ts"\nblob_oid = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"\ndetector_code = "github-token-v1"\n',
            '[[repos.secret_allowlist]]\npath = "src/token.ts"\nblob_oid = "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"\ndetector_code = "github-token-v1"\n',
        )

        for suffix in invalid:
            with self.subTest(suffix=suffix):
                with self.assertRaises(ValueError):
                    load_registry(self.write_registry(base + suffix))

    def test_registry_rejects_duplicate_capsule_and_allowlist_rows(self):
        base_capsule = (
            '[[repos.capsules]]\n'
            'id = "runtime"\n'
            'adapter = "npm-tracked-source-v1"\n'
            'focus_packages = ["@scope/runtime"]\n'
        )
        duplicate_allowlist = (
            '[[repos.secret_allowlist]]\n'
            'path = "src/token.ts"\n'
            'blob_oid = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"\n'
            'detector_code = "github-token-v1"\n'
        )
        base = (
            '[[repos]]\nid = "paypal/paypal-js"\ncompany = "paypal"\n'
            'url = "https://github.com/paypal/paypal-js"\nenabled = true\nrepo_type = "web-sdk"\n'
            'priority = "tier1"\ntrack = "releases-and-default-branch"\nversion_strategy = "monorepo-packages"\n'
        )

        with self.assertRaisesRegex(ValueError, "duplicate capsule"):
            load_registry(self.write_registry(base + base_capsule + base_capsule))
        duplicate_override = (
            '[[repos.capsules.package_overrides]]\nname = "@scope/internal"\nrequired_roots = ["src"]\n'
            'generated_target_paths = []\ninclude_paths = []\n'
        )
        with self.assertRaisesRegex(ValueError, "duplicate package override"):
            load_registry(self.write_registry(base + base_capsule + duplicate_override + duplicate_override))
        with self.assertRaisesRegex(ValueError, "duplicate secret allowlist"):
            load_registry(self.write_registry(base + duplicate_allowlist + duplicate_allowlist))

    def test_registry_rejects_invalid_nested_version_track_values(self):
        base = (
            '[[repos]]\n'
            'id = "paypal/paypal-js"\n'
            'company = "paypal"\n'
            'url = "https://github.com/paypal/paypal-js"\n'
            'enabled = true\n'
            'repo_type = "web-sdk"\n'
            'priority = "tier1"\n'
            'track = "releases-and-default-branch"\n'
            'version_strategy = "monorepo-packages"\n'
            '[[repos.version_tracks]]\n'
        )
        invalid_tracks = (
            'selector = "v10"\nbackfill = "unknown"\nfuture = "none"\n',
            'selector = "v10"\nbackfill = "none"\nfuture = "unknown"\n',
            'selector = ""\nbackfill = "none"\nfuture = "none"\n',
            'selector = "tag:v10"\nbackfill = "none"\nfuture = "none"\n',
            'selector = "v1.2-beta"\nbackfill = "none"\nfuture = "none"\n',
            'selector = "v10"\nbackfill = "none"\nfuture = "none"\ninclude_prerelease = "false"\n',
            'selector = "v10"\nbackfill = "none"\nfuture = "none"\npinned_versions = ["10"]\n',
            'selector = "v10"\nbackfill = "none"\nfuture = "none"\nunknown = "value"\n',
        )

        for invalid_track in invalid_tracks:
            with self.subTest(invalid_track=invalid_track):
                with self.assertRaises(ValueError):
                    load_registry(self.write_registry(base + invalid_track))

    def test_registry_rejects_plain_version_track_selectors(self):
        text = (
            '[[repos]]\n'
            'id = "paypal/paypal-js"\n'
            'company = "paypal"\n'
            'url = "https://github.com/paypal/paypal-js"\n'
            'enabled = false\n'
            'repo_type = "web-sdk"\n'
            'priority = "tier1"\n'
            'track = "releases-and-default-branch"\n'
            'version_strategy = "semver-tags"\n'
            '[[repos.version_tracks]]\n'
            'selector = "v10"\n'
            'backfill = "latest-stable"\n'
            'future = "all-stable"\n'
        )

        with self.assertRaisesRegex(ValueError, "package-qualified"):
            load_registry(self.write_registry(text))

    def test_registry_rejects_duplicate_version_track_selectors(self):
        path = self.write_registry(
            '[[repos]]\n'
            'id = "paypal/paypal-js"\n'
            'company = "paypal"\n'
            'url = "https://github.com/paypal/paypal-js"\n'
            'enabled = true\n'
            'repo_type = "web-sdk"\n'
            'priority = "tier1"\n'
            'track = "releases-and-default-branch"\n'
            'version_strategy = "monorepo-packages"\n'
            '[[repos.version_tracks]]\n'
            'selector = "package:@scope/name@10"\n'
            'backfill = "none"\n'
            'future = "none"\n'
            '[[repos.version_tracks]]\n'
            'selector = "package:@scope/name@10"\n'
            'backfill = "none"\n'
            'future = "none"\n'
        )

        with self.assertRaisesRegex(ValueError, "duplicate selector"):
            load_registry(path)

    def test_registry_rejects_duplicate_ids_and_mutable_state(self):
        repos = (self.repo(), self.repo())
        self.assertTrue(any("duplicate id" in error for error in validate_registry(repos)))

        repo = self.repo()
        object.__setattr__(repo, "latest_version", "10.0.0")
        self.assertTrue(any("latest_version" in error for error in validate_registry((repo,))))

    def test_load_registry_rejects_mutable_state(self):
        base = (
            '[[repos]]\n'
            'id = "paypal/paypal-js"\n'
            'company = "paypal"\n'
            'url = "https://github.com/paypal/paypal-js"\n'
            'enabled = true\n'
            'repo_type = "web-sdk"\n'
            'priority = "tier1"\n'
            'track = "releases-and-default-branch"\n'
            'version_strategy = "monorepo-packages"\n'
        )

        for key, value in (
            ("latest_version", '"10.0.0"'),
            ("policy_hash", '"a"'),
            ("ingest_progress", '"reviewed"'),
        ):
            with self.subTest(key=key):
                with self.assertRaisesRegex(ValueError, key):
                    load_registry(self.write_registry(base + key + " = " + value + "\n"))

    def test_registry_rejects_invalid_values_and_repository_identity(self):
        invalid = (
            dataclasses.replace(self.repo(), priority="important"),
            dataclasses.replace(self.repo(), track="tags"),
            dataclasses.replace(self.repo(), version_strategy="rolling"),
            dataclasses.replace(self.repo(), id="paypal/not-paypal-js"),
            dataclasses.replace(self.repo(), url="http://github.com/paypal/paypal-js"),
        )

        errors = validate_registry(invalid)

        self.assertTrue(any("priority" in error for error in errors))
        self.assertTrue(any("track" in error for error in errors))
        self.assertTrue(any("version_strategy" in error for error in errors))
        self.assertTrue(any("id" in error for error in errors))
        self.assertTrue(any("HTTPS GitHub URL" in error for error in errors))

    def test_selection_filters_by_enabled_company_and_id(self):
        disabled = dataclasses.replace(
            self.repo(id="stripe/stripe-ios", company="stripe", url="https://github.com/stripe/stripe-ios", enabled=False)
        )
        repos = (self.repo(), disabled)

        self.assertEqual((self.repo(),), select_repos(repos))
        self.assertEqual((disabled,), select_repos(repos, company="stripe", enabled_only=False))
        self.assertEqual((disabled,), select_repos(repos, repo_id="stripe/stripe-ios", enabled_only=False))

    def test_paypal_messages_ios_uses_the_reviewed_release_capsule(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        repo = next(item for item in repos if item.id == "paypal/paypal-messages-ios")

        self.assertTrue(repo.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:paypal-messages-ios@1",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("1.2.0",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("paypal-messages-ios-public-source", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("paypal-messages-ios",), capsule.focus_packages)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertIn("Sources/PayPalMessages/Config", capsule.default_required_roots)
        self.assertIn("Sources/PayPalMessages/IO", capsule.default_required_roots)
        self.assertIn("Demo/Demo/Components", capsule.default_required_roots)
        self.assertIn("Sources/PayPalMessages/PayPalMessageView.swift", capsule.include_paths)
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)

    def test_paypal_messages_android_uses_the_reviewed_release_capsule(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        repo = next(item for item in repos if item.id == "paypal/paypal-messages-android")

        self.assertTrue(repo.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:paypal-messages-android@1",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("1.3.0",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("paypal-messages-android-public-source", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("paypal-messages-android",), capsule.focus_packages)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertIn("library/src/main/java", capsule.default_required_roots)
        self.assertIn("library/src/main/res", capsule.default_required_roots)
        self.assertIn("demo/src/main/java", capsule.default_required_roots)
        self.assertIn("library/src/main/AndroidManifest.xml", capsule.include_paths)
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)

    def test_adyen_web_uses_the_reviewed_bounded_public_source_capsule(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        adyen = next(repo for repo in repos if repo.id == "adyen/adyen-web")
        capsule = adyen.capsules[0]

        self.assertEqual(
            (
                "src/components/Card",
                "src/components/Dropin",
                "src/components/ThreeDS2",
                "src/core",
                "src/types",
            ),
            capsule.default_required_roots,
        )
        self.assertEqual(
            (
                "src/components/index.ts",
                "src/components/types.ts",
                "src/index.ts",
                "src/index.umd.ts",
                "src/types.ts",
            ),
            capsule.include_paths,
        )
        self.assertEqual(("dist/",), capsule.default_generated_target_paths)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual(340, capsule.max_capsule_files)
        self.assertEqual(3000000, capsule.max_capsule_utf8_bytes)

    def test_adyen_ios_uses_the_reviewed_complete_swift_source_capsule(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        repo = next(item for item in repos if item.id == "adyen/adyen-ios")

        self.assertTrue(repo.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:adyen-ios@5",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("5.25.1",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("adyen-ios-public-source", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("adyen-ios",), capsule.focus_packages)
        self.assertEqual("configured-repository-paths", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(56, len(capsule.default_required_roots))
        self.assertEqual(38, len(capsule.include_paths))
        self.assertEqual((), capsule.default_generated_target_paths)
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(750, capsule.max_capsule_files)
        self.assertEqual(4000000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(800, capsule.max_packet_files)
        self.assertEqual(5000000, capsule.max_packet_utf8_bytes)

        required = set(capsule.default_required_roots)
        includes = set(capsule.include_paths)
        self.assertTrue({
            "Adyen/Core",
            "AdyenActions/Components",
            "AdyenCard/Components",
            "AdyenComponents/Apple Pay",
            "AdyenDropIn/Components",
            "AdyenSession/API",
            "Demo/Common/IntegrationExamples",
        }.issubset(required))
        self.assertTrue({
            "Adyen/Assets/Generated/LocalizationKey.swift",
            "Demo/Configuration+secrets.swift",
            "Demo/Configuration.swift",
            "Package.swift",
            "MIGRATION.md",
        }.issubset(includes))

    def test_adyen_android_uses_the_reviewed_complete_kotlin_source_capsule(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        repo = next(item for item in repos if item.id == "adyen/adyen-android")

        self.assertTrue(repo.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:adyen-android@5",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("5.20.0",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("adyen-android-public-source", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("adyen-android",), capsule.focus_packages)
        self.assertEqual("configured-repository-paths", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(53, len(capsule.default_required_roots))
        self.assertEqual(133, len(capsule.include_paths))
        self.assertEqual((), capsule.default_generated_target_paths)
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(1250, capsule.max_capsule_files)
        self.assertEqual(5000000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(1300, capsule.max_packet_files)
        self.assertEqual(6000000, capsule.max_packet_utf8_bytes)

        required = set(capsule.default_required_roots)
        includes = set(capsule.include_paths)
        self.assertTrue({
            "components-core/src/main/java",
            "drop-in/src/main/java",
            "sessions-core/src/main/java",
            "card/src/main/java",
            "googlepay/src/main/java",
            "example-app/src/main/java",
        }.issubset(required))
        self.assertTrue({
            "README.md",
            "settings.gradle",
            "gradle/libs.versions.toml",
            "drop-in/build.gradle",
            "example-app/src/main/AndroidManifest.xml",
            "card/src/main/res/values/strings.xml",
        }.issubset(includes))

    def test_adyen_3ds2_android_uses_public_api_distribution_capsule(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        repo = next(item for item in repos if item.id == "adyen/adyen-3ds2-android")

        self.assertTrue(repo.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:adyen-3ds2-android@2",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("2.2.27",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("adyen-3ds2-android-public-api", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("adyen-3ds2-android",), capsule.focus_packages)
        self.assertEqual(("docs/com",), capsule.default_required_roots)
        self.assertIn("RELEASE_NOTES", capsule.include_paths)
        self.assertIn("TROUBLESHOOTING.md", capsule.include_paths)
        self.assertNotIn("adyen-3ds2-2.2.27-sources.jar", capsule.include_paths)
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)

    def test_adyen_3ds2_ios_uses_canonical_public_header_capsule(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        repo = next(item for item in repos if item.id == "adyen/adyen-3ds2-ios")

        self.assertTrue(repo.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:adyen-3ds2-ios@2",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("2.4.4",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("adyen-3ds2-ios-public-api", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("adyen-3ds2-ios",), capsule.focus_packages)
        self.assertEqual(
            (
                "XCFramework/Dynamic/Adyen3DS2.xcframework/ios-arm64/Adyen3DS2.framework/Headers",
            ),
            capsule.default_required_roots,
        )
        self.assertIn("Adyen3DS2.podspec", capsule.include_paths)
        self.assertIn("Package.swift", capsule.include_paths)
        self.assertIn(
            "XCFramework/Dynamic/Adyen3DS2.xcframework/ios-arm64/Adyen3DS2.framework/Modules/module.modulemap",
            capsule.include_paths,
        )
        self.assertIn(
            "XCFramework/Dynamic/Adyen3DS2.xcframework/ios-arm64/Adyen3DS2.framework/PrivacyInfo.xcprivacy",
            capsule.include_paths,
        )
        self.assertFalse(any(path.endswith("Info.plist") for path in capsule.include_paths))
        self.assertNotIn("XCFramework/Static", capsule.default_required_roots)
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)

    def test_adyen_3ds2_ios_swift_uses_canonical_public_api_capsule(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        repo = next(
            item for item in repos if item.id == "adyen/adyen-3ds2-ios-swift"
        )

        self.assertTrue(repo.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:adyen-3ds2-ios-swift@3",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("3.0.1",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("adyen-3ds2-ios-swift-public-api", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("adyen-3ds2-ios-swift",), capsule.focus_packages)
        self.assertEqual(
            (
                "XCFramework/Dynamic/Adyen3DS2_Swift.xcframework/ios-arm64/Adyen3DS2_Swift.framework/Headers",
            ),
            capsule.default_required_roots,
        )
        public_interface = (
            "XCFramework/Dynamic/Adyen3DS2_Swift.xcframework/ios-arm64/"
            "Adyen3DS2_Swift.framework/Modules/Adyen3DS2_Swift.swiftmodule/"
            "arm64-apple-ios.swiftinterface"
        )
        self.assertIn(public_interface, capsule.include_paths)
        self.assertIn("Adyen3DS2_Swift.podspec", capsule.include_paths)
        self.assertIn("Package.swift", capsule.include_paths)
        self.assertTrue(
            all("private.swiftinterface" not in path for path in capsule.include_paths)
        )
        self.assertFalse(
            any(path.endswith(".abi.json") for path in capsule.include_paths)
        )
        self.assertNotIn("XCFramework/Static", capsule.default_required_roots)
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)

    def test_adyen_wechatpay_ios_uses_public_wrapper_capsule(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        repo = next(item for item in repos if item.id == "adyen/adyen-wechatpay-ios")

        self.assertTrue(repo.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:AdyenWeChatPayInternal@2",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("2.2.0",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("adyen-wechatpay-ios-public-wrapper", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("AdyenWeChatPayInternal",), capsule.focus_packages)
        self.assertEqual(
            (
                "AdyenWeChatPayInternal.xcframework/ios-arm64/AdyenWeChatPayInternal.framework/Headers",
            ),
            capsule.default_required_roots,
        )
        self.assertIn("AdyenWeChatPayInternal.podspec", capsule.include_paths)
        self.assertIn("AdyenWeChatPayInternal.xcframework/Info.plist", capsule.include_paths)
        self.assertNotIn(
            "AdyenWeChatPayInternal.xcframework/ios-arm64/AdyenWeChatPayInternal.framework/Info.plist",
            capsule.include_paths,
        )
        self.assertFalse(any(path.endswith(".abi.json") for path in capsule.include_paths))
        self.assertFalse(any(path.endswith("/AdyenWeChatPayInternal") for path in capsule.include_paths))
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)

    def test_stripe_sync_engine_uses_operational_commit_capsule(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        repo = next(item for item in repos if item.id == "stripe/sync-engine")

        self.assertTrue(repo.enabled)
        self.assertEqual("commit", repo.version_strategy)
        self.assertEqual("default-branch", repo.track)
        self.assertEqual((), repo.version_tracks)
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("stripe-sync-engine-operational", capsule.id)
        self.assertEqual("commit-tree-v1", capsule.adapter)
        self.assertEqual("stripe-sync-engine", capsule.source_id)
        self.assertEqual("configured-repository-paths", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual((), capsule.default_generated_target_paths)
        self.assertTrue({
            "docs/architecture",
            "docs/engine",
            "docs/service",
            "apps/engine/src/api",
            "apps/engine/src/bin",
            "apps/engine/src/cli",
            "apps/engine/src/lib/progress",
            "apps/service/src/api",
            "apps/service/src/bin",
            "apps/service/src/cli",
            "apps/service/src/lib",
            "apps/service/src/temporal",
            "packages/protocol/src",
            "packages/source-stripe/src/transforms",
            "packages/source-stripe/src/utils",
            "packages/destination-postgres/src",
            "packages/state-postgres/src",
            "packages/util-postgres/src",
        }.issubset(set(capsule.default_required_roots)))
        self.assertNotIn("apps/engine/src/lib", capsule.default_required_roots)
        self.assertTrue({
            "README.md",
            "CHANGELOG.md",
            "package.json",
            "pnpm-workspace.yaml",
            "apps/engine/package.json",
            "apps/engine/src/index.ts",
            "apps/service/package.json",
            "apps/service/src/index.ts",
            "packages/protocol/package.json",
            "packages/source-stripe/package.json",
            "packages/source-stripe/src/catalog.ts",
            "packages/source-stripe/src/client.ts",
            "packages/source-stripe/src/src-list-api.ts",
            "packages/source-stripe/src/src-webhook.ts",
            "packages/destination-postgres/package.json",
            "packages/state-postgres/package.json",
            "packages/util-postgres/package.json",
        }.issubset(set(capsule.include_paths)))
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertTrue({
            "README.md",
            "CHANGELOG.md",
            "docs/architecture/packages.md",
            "docs/engine/ARCHITECTURE.md",
            "docs/service/ARCHITECTURE.md",
            "apps/engine/src/lib/engine.ts",
            "apps/service/src/temporal/workflows/pipeline-lifecycle.ts",
            "packages/protocol/src/protocol.ts",
            "packages/source-stripe/src/catalog.ts",
            "packages/source-stripe/src/src-list-api.ts",
            "packages/source-stripe/src/src-webhook.ts",
            "packages/destination-postgres/src/index.ts",
            "packages/state-postgres/src/state-store.ts",
            "packages/util-postgres/src/upsert.ts",
        }.issubset(set(repo.ingest_required_paths)))
        self.assertFalse(any("__generated__" in path for path in capsule.default_required_roots))
        self.assertFalse(any("__snapshots__" in path for path in capsule.default_required_roots))

    def test_stripe_apps_uses_manifest_and_full_page_commit_capsule(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        repo = next(item for item in repos if item.id == "stripe/stripe-apps")

        self.assertTrue(repo.enabled)
        self.assertEqual("commit", repo.version_strategy)
        self.assertEqual("default-branch", repo.track)
        self.assertEqual((), repo.version_tracks)
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("stripe-apps-platform", capsule.id)
        self.assertEqual("commit-tree-v1", capsule.adapter)
        self.assertEqual("stripe-apps", capsule.source_id)
        self.assertEqual(
            ("examples/full-page/src",),
            capsule.default_required_roots,
        )
        self.assertTrue({
            "README.md",
            "CHANGELOG.md",
            "SECURITY.md",
            "LICENSE",
            "schema/README.md",
            "schema/package.json",
            "schema/stripe-app-local.schema.json",
            "schema/stripe-app.schema.json",
            "schema/stripe-app.schema.yaml",
            "examples/full-page/README.md",
            "examples/full-page/package.json",
            "examples/full-page/stripe-app.json",
            "examples/full-page/tsconfig.json",
            "examples/full-page/ui-extensions.d.ts",
        }.issubset(set(capsule.include_paths)))
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertFalse(any("lock" in path for path in capsule.include_paths))
        self.assertFalse(any(path.startswith(".github/") for path in capsule.include_paths))

    def test_braintree_web_uses_the_reviewed_public_source_capsule(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        braintree = next(repo for repo in repos if repo.id == "braintree/braintree-web")

        self.assertTrue(braintree.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:braintree-web@3",
                    "latest-stable",
                    "all-stable",
                ),
            ),
            braintree.version_tracks,
        )
        self.assertEqual(1, len(braintree.capsules))
        capsule = braintree.capsules[0]
        self.assertEqual("braintree-web-public-source", capsule.id)
        self.assertEqual("npm-tracked-source-v1", capsule.adapter)
        self.assertEqual(("braintree-web",), capsule.focus_packages)
        self.assertEqual("internal-runtime-closure", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(
            (".storybook/stories", "src"),
            capsule.default_required_roots,
        )
        self.assertEqual(("dist/",), capsule.default_generated_target_paths)
        self.assertEqual(("CHANGELOG.md", "components.json"), capsule.include_paths)
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(380, capsule.max_capsule_files)
        self.assertEqual(3000000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(420, capsule.max_packet_files)
        self.assertEqual(3500000, capsule.max_packet_utf8_bytes)

    def test_braintree_android_uses_the_reviewed_tagged_tree_profile(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        repo = next(
            item for item in repos if item.id == "braintree/braintree_android"
        )

        self.assertTrue(repo.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:braintree-android@5",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("5.30.0",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("braintree-android-public-source", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("braintree-android",), capsule.focus_packages)
        self.assertEqual(
            "configured-repository-paths",
            capsule.dependency_scope,
        )
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(
            {
                "AmericanExpress/src/main",
                "BraintreeCore/src/main",
                "Card/src/main",
                "DataCollector/src/main",
                "GooglePay/src/main",
                "LocalPayment/src/main",
                "PayPal/src/main",
                "PayPalMessaging/src/main",
                "SEPADirectDebit/src/main",
                "ShopperInsights/src/main",
                "SharedUtils/src/main",
                "ThreeDSecure/src/main",
                "UIComponents/src/main/java",
                "UIComponents/src/main/res/drawable",
                "UIComponents/src/main/res/layout",
                "UIComponents/src/main/res/values",
                "Venmo/src/main",
            },
            set(capsule.default_required_roots),
        )
        self.assertEqual(
            {
                "README.md",
                "CHANGELOG.md",
                "v5_MIGRATION_GUIDE.md",
                "v4_MIGRATION_GUIDE.md",
                "v4.9.0+_MIGRATION_GUIDE.md",
                "APP_LINK_SETUP.md",
                "DEPENDENCIES.md",
                "LICENSE",
                "settings.gradle",
                "build.gradle",
                "gradle.properties",
                "UIComponents/src/main/AndroidManifest.xml",
                "AmericanExpress/build.gradle",
                "BraintreeCore/build.gradle",
                "Card/build.gradle",
                "DataCollector/build.gradle",
                "GooglePay/build.gradle",
                "LocalPayment/build.gradle",
                "PayPal/build.gradle",
                "PayPalMessaging/build.gradle",
                "SEPADirectDebit/build.gradle",
                "ShopperInsights/build.gradle",
                "SharedUtils/build.gradle",
                "ThreeDSecure/build.gradle",
                "UIComponents/build.gradle",
                "Venmo/build.gradle",
                "BraintreeCore/proguard.pro",
                "GooglePay/proguard.pro",
                "ThreeDSecure/proguard.pro",
            },
            set(capsule.include_paths),
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(500, capsule.max_capsule_files)
        self.assertEqual(5000000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(550, capsule.max_packet_files)
        self.assertEqual(6000000, capsule.max_packet_utf8_bytes)
        self.assertNotIn(
            "UIComponents/src/main/res/drawable-xxhdpi",
            capsule.default_required_roots,
        )

    def test_braintree_popup_bridges_use_reviewed_platform_capsules(self):
        repos = {
            repo.id: repo
            for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
        }

        ios = repos["braintree/popup-bridge-ios"]
        self.assertTrue(ios.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:PopupBridge@3",
                    "latest-stable",
                    "all-stable",
                    pinned_versions=("3.1.0",),
                ),
            ),
            ios.version_tracks,
        )
        self.assertEqual(1, len(ios.capsules))
        ios_capsule = ios.capsules[0]
        self.assertEqual("popup-bridge-ios-public-source", ios_capsule.id)
        self.assertEqual("tagged-tree-v1", ios_capsule.adapter)
        self.assertEqual(("PopupBridge",), ios_capsule.focus_packages)
        self.assertEqual(
            ("Demo/Demo", "Sources/PopupBridge"),
            ios_capsule.default_required_roots,
        )
        self.assertEqual(("fixtures", "tests"), ios_capsule.excluded_categories)

        android = repos["braintree/popup-bridge-android"]
        self.assertTrue(android.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:popup-bridge@5",
                    "latest-stable",
                    "all-stable",
                    pinned_versions=("5.3.0",),
                ),
            ),
            android.version_tracks,
        )
        self.assertEqual(1, len(android.capsules))
        android_capsule = android.capsules[0]
        self.assertEqual("popup-bridge-android-public-source", android_capsule.id)
        self.assertEqual("tagged-tree-v1", android_capsule.adapter)
        self.assertEqual(("popup-bridge",), android_capsule.focus_packages)
        self.assertEqual(
            (
                "Demo/src/main/java",
                "Demo/src/main/res/layout",
                "Demo/src/main/res/values",
                "Demo/src/main/res/xml",
                "PopupBridge/src/main",
            ),
            android_capsule.default_required_roots,
        )
        self.assertEqual(("fixtures", "tests"), android_capsule.excluded_categories)

    def test_braintree_credit_card_type_uses_reviewed_source_capsule(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        repo = next(
            item for item in repos if item.id == "braintree/credit-card-type"
        )

        self.assertTrue(repo.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:credit-card-type@10",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("10.3.0",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("credit-card-type-public-source", capsule.id)
        self.assertEqual("npm-tracked-source-v1", capsule.adapter)
        self.assertEqual(("credit-card-type",), capsule.focus_packages)
        self.assertEqual(("src",), capsule.default_required_roots)
        self.assertEqual(("dist/",), capsule.default_generated_target_paths)
        self.assertTrue(
            {
                "CHANGELOG.md",
                "LICENSE",
                "README.md",
                "SECURITY.md",
                "package.json",
                "tsconfig.json",
            }.issubset(capsule.include_paths)
        )
        self.assertNotIn("package-lock.json", capsule.include_paths)
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)

    def test_braintree_restricted_input_uses_commit_tracked_source_capsule(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        repo = next(
            item for item in repos if item.id == "braintree/restricted-input"
        )

        self.assertTrue(repo.enabled)
        self.assertEqual("commit", repo.version_strategy)
        self.assertEqual("default-branch", repo.track)
        self.assertEqual((), repo.version_tracks)
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("restricted-input-public-source", capsule.id)
        self.assertEqual("commit-tree-v1", capsule.adapter)
        self.assertEqual("restricted-input", capsule.source_id)
        self.assertEqual(("src",), capsule.default_required_roots)
        self.assertEqual(
            (
                "CHANGELOG.md",
                "LICENSE",
                "README.md",
                "package.json",
                "supports-input-formatting.js",
                "tsconfig.json",
            ),
            capsule.include_paths,
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertNotIn("package-lock.json", capsule.include_paths)
        self.assertEqual(40, capsule.max_capsule_files)
        self.assertEqual(250000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(1000000, capsule.max_packet_utf8_bytes)

    def test_braintree_web_drop_in_uses_the_reviewed_public_source_capsule(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        drop_in = next(
            repo for repo in repos if repo.id == "braintree/braintree-web-drop-in"
        )

        self.assertTrue(drop_in.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:braintree-web-drop-in@1",
                    "latest-stable",
                    "all-stable",
                ),
            ),
            drop_in.version_tracks,
        )
        self.assertEqual(1, len(drop_in.capsules))
        capsule = drop_in.capsules[0]
        self.assertEqual("braintree-web-drop-in-public-source", capsule.id)
        self.assertEqual("npm-tracked-source-v1", capsule.adapter)
        self.assertEqual(("braintree-web-drop-in",), capsule.focus_packages)
        self.assertEqual(("src",), capsule.default_required_roots)
        self.assertEqual(("CHANGELOG.md",), capsule.include_paths)
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual(200, capsule.max_capsule_files)
        self.assertEqual(1500000, capsule.max_capsule_utf8_bytes)

    def test_braintree_ios_drop_in_uses_reviewed_public_source_capsule(self):
        repos = {
            repo.id: repo
            for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
        }
        repo = repos["braintree/braintree-ios-drop-in"]

        self.assertTrue(repo.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:BraintreeDropIn@9",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("9.14.0",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("braintree-ios-drop-in-public-source", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("BraintreeDropIn",), capsule.focus_packages)
        self.assertEqual("configured-repository-paths", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(
            {
                "Demo/Application/Settings",
                "Demo/Application/SwiftUI",
                "Sources/BraintreeDropIn",
            },
            set(capsule.default_required_roots),
        )
        self.assertEqual((), capsule.default_generated_target_paths)
        self.assertEqual(
            {
                "BraintreeDropIn.podspec",
                "BraintreeDropIn.xcodeproj/project.pbxproj",
                "CHANGELOG.md",
                "DEVELOPMENT.md",
                "Demo/Application/DemoAppDelegate.swift",
                "Demo/Application/DemoBaseViewController.swift",
                "Demo/Application/DemoContainerViewController.swift",
                "Demo/Application/DemoDropInView.swift",
                "Demo/Application/DemoDropInViewController.swift",
                "Demo/Application/DemoMerchantAPIClient.swift",
                "Demo/Application/DemoPurchaseButton.swift",
                "Demo/Application/ViewHelpers.swift",
                "LICENSE",
                "Package.swift",
                "README.md",
            },
            set(capsule.include_paths),
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(500, capsule.max_capsule_files)
        self.assertEqual(5000000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(550, capsule.max_packet_files)
        self.assertEqual(6000000, capsule.max_packet_utf8_bytes)

    def test_braintree_android_drop_in_uses_reviewed_public_source_capsule(self):
        repos = {
            repo.id: repo
            for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
        }
        repo = repos["braintree/braintree-android-drop-in"]

        self.assertTrue(repo.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:drop-in@6",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("6.17.0",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("braintree-android-drop-in-public-source", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("drop-in",), capsule.focus_packages)
        self.assertEqual("configured-repository-paths", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(
            {
                "Demo/src/main/java",
                "Demo/src/main/res/layout",
                "Demo/src/main/res/menu",
                "Demo/src/main/res/values",
                "Demo/src/main/res/xml",
                "Drop-In/src/main/java",
                "Drop-In/src/main/res/anim",
                "Drop-In/src/main/res/drawable",
                "Drop-In/src/main/res/drawable-v21",
                "Drop-In/src/main/res/layout",
                "Drop-In/src/main/res/values",
                "Drop-In/src/main/res/values-ar",
                "Drop-In/src/main/res/values-cs",
                "Drop-In/src/main/res/values-da",
                "Drop-In/src/main/res/values-de",
                "Drop-In/src/main/res/values-el",
                "Drop-In/src/main/res/values-es",
                "Drop-In/src/main/res/values-es-rXC",
                "Drop-In/src/main/res/values-fi",
                "Drop-In/src/main/res/values-fr",
                "Drop-In/src/main/res/values-fr-rCA",
                "Drop-In/src/main/res/values-fr-rXC",
                "Drop-In/src/main/res/values-he",
                "Drop-In/src/main/res/values-hu",
                "Drop-In/src/main/res/values-id",
                "Drop-In/src/main/res/values-it",
                "Drop-In/src/main/res/values-iw",
                "Drop-In/src/main/res/values-ja",
                "Drop-In/src/main/res/values-ko",
                "Drop-In/src/main/res/values-land",
                "Drop-In/src/main/res/values-nb",
                "Drop-In/src/main/res/values-nl",
                "Drop-In/src/main/res/values-pl",
                "Drop-In/src/main/res/values-pt",
                "Drop-In/src/main/res/values-ru",
                "Drop-In/src/main/res/values-sk",
                "Drop-In/src/main/res/values-sv",
                "Drop-In/src/main/res/values-th",
                "Drop-In/src/main/res/values-v16",
                "Drop-In/src/main/res/values-v21",
                "Drop-In/src/main/res/values-w700dp",
                "Drop-In/src/main/res/values-zh-rCN",
                "Drop-In/src/main/res/values-zh-rHK",
                "Drop-In/src/main/res/values-zh-rTW",
                "Drop-In/src/main/res/values-zh-rXC",
            },
            set(capsule.default_required_roots),
        )
        self.assertEqual((), capsule.default_generated_target_paths)
        self.assertEqual(
            {
                "ACKNOWLEDGEMENTS.md",
                "CHANGELOG.md",
                "CONTRIBUTING.md",
                "DEVELOPMENT.md",
                "Demo/build.gradle",
                "Demo/src/main/AndroidManifest.xml",
                "Drop-In/build.gradle",
                "Drop-In/src/main/AndroidManifest.xml",
                "LICENSE",
                "README.md",
                "build.gradle",
                "gradle.properties",
                "settings.gradle",
                "v6_MIGRATION_GUIDE.md",
            },
            set(capsule.include_paths),
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(500, capsule.max_capsule_files)
        self.assertEqual(5000000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(550, capsule.max_packet_files)
        self.assertEqual(6000000, capsule.max_packet_utf8_bytes)

    def test_braintree_node_uses_complete_runtime_checkout_profile(self):
        repos = {
            repo.id: repo
            for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
        }
        repo = repos["braintree/braintree_node"]

        self.assertTrue(repo.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:braintree@3",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("3.39.0",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("braintree-node-checkout-source", capsule.id)
        self.assertEqual("npm-tracked-source-v1", capsule.adapter)
        self.assertEqual(("braintree",), capsule.focus_packages)
        self.assertEqual("internal-runtime-closure", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(("lib",), capsule.default_required_roots)
        self.assertEqual((), capsule.default_generated_target_paths)
        self.assertEqual(
            ("CHANGELOG.md", "LICENSE", "README.md", "SECURITY.md", "index.js"),
            capsule.include_paths,
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(220, capsule.max_capsule_files)
        self.assertEqual(1500000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(260, capsule.max_packet_files)
        self.assertEqual(2000000, capsule.max_packet_utf8_bytes)

    def test_braintree_graphql_api_has_reviewed_commit_policy(self):
        repos = {
            repo.id: repo
            for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
        }
        repo = repos["braintree/graphql-api"]

        self.assertTrue(repo.enabled)
        self.assertEqual("api-specification", repo.repo_type)
        self.assertEqual("tier1", repo.priority)
        self.assertEqual("monthly", repo.collection_frequency)
        self.assertEqual("default-branch", repo.track)
        self.assertEqual("commit", repo.version_strategy)
        self.assertEqual((), repo.version_tracks)
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("braintree-graphql-api-schema", capsule.id)
        self.assertEqual("commit-tree-v1", capsule.adapter)
        self.assertEqual("braintree-graphql-api", capsule.source_id)
        self.assertEqual("configured-repository-paths", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(("schema.graphql",), capsule.default_required_roots)
        self.assertEqual(("CHANGELOG.md", "README.md"), capsule.include_paths)
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual(650000, capsule.max_file_bytes)
        self.assertEqual(3, capsule.max_capsule_files)
        self.assertEqual(800000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(15, capsule.max_packet_files)
        self.assertEqual(1500000, capsule.max_packet_utf8_bytes)

    def test_braintree_mobile_sdk_tooling_has_reviewed_commit_policy(self):
        repos = {
            repo.id: repo
            for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
        }
        repo = repos["braintree/mobile-sdk-tooling"]

        self.assertTrue(repo.enabled)
        self.assertEqual("tooling", repo.repo_type)
        self.assertEqual("tier3", repo.priority)
        self.assertEqual("on-demand", repo.collection_frequency)
        self.assertEqual("default-branch", repo.track)
        self.assertEqual("commit", repo.version_strategy)
        self.assertEqual((), repo.version_tracks)
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("braintree-mobile-sdk-tooling", capsule.id)
        self.assertEqual("commit-tree-v1", capsule.adapter)
        self.assertEqual("mobile-sdk-tooling", capsule.source_id)
        self.assertEqual("configured-repository-paths", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(
            ("README.md",),
            capsule.default_required_roots,
        )
        self.assertEqual(
            (".github/workflows/pr-review-digest.yml",),
            capsule.include_paths,
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(2, capsule.max_capsule_files)
        self.assertEqual(200000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(15, capsule.max_packet_files)
        self.assertEqual(1500000, capsule.max_packet_utf8_bytes)

    def test_stripe_cli_uses_checkout_focused_tagged_profile(self):
        repos = {
            repo.id: repo
            for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
        }
        repo = repos["stripe/stripe-cli"]

        self.assertTrue(repo.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:stripe-cli@1",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("1.50.0",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("stripe-cli-checkout-source", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("stripe-cli",), capsule.focus_packages)
        self.assertEqual(
            "configured-repository-paths",
            capsule.dependency_scope,
        )
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(
            (
                "pkg/config",
                "pkg/login",
                "pkg/proxy",
                "pkg/requests",
                "pkg/stripe",
                "pkg/websocket",
            ),
            capsule.default_required_roots,
        )
        self.assertEqual((), capsule.default_generated_target_paths)
        self.assertEqual(75, len(capsule.include_paths))
        self.assertIn("pkg/cmd/listen.go", capsule.include_paths)
        self.assertIn("pkg/cmd/trigger.go", capsule.include_paths)
        self.assertIn(
            "pkg/fixtures/triggers/checkout.session.completed.json",
            capsule.include_paths,
        )
        self.assertIn(
            "pkg/fixtures/triggers/payment_intent.succeeded.json",
            capsule.include_paths,
        )
        self.assertIn(
            "pkg/fixtures/triggers/customer.subscription.updated.json",
            capsule.include_paths,
        )
        self.assertIn(
            "pkg/fixtures/triggers/subscription_schedule.updated.json",
            capsule.include_paths,
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(1000000, capsule.max_file_bytes)
        self.assertEqual(180, capsule.max_capsule_files)
        self.assertEqual(2500000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(220, capsule.max_packet_files)
        self.assertEqual(3200000, capsule.max_packet_utf8_bytes)

    def test_stripe_php_uses_broad_public_runtime_tagged_profile(self):
        repos = {
            repo.id: repo
            for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
        }
        repo = repos["stripe/stripe-php"]

        self.assertTrue(repo.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:stripe-php@21",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("21.2.0",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("stripe-php-public-runtime", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("stripe-php",), capsule.focus_packages)
        self.assertEqual("configured-repository-paths", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(("lib",), capsule.default_required_roots)
        self.assertEqual((), capsule.default_generated_target_paths)
        self.assertEqual(
            ("CHANGELOG.md", "LICENSE", "README.md", "composer.json", "init.php"),
            capsule.include_paths,
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(1000000, capsule.max_file_bytes)
        self.assertEqual(492, capsule.max_capsule_files)
        self.assertEqual(3100000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(512, capsule.max_packet_files)
        self.assertEqual(3600000, capsule.max_packet_utf8_bytes)

    def test_stripe_js_uses_the_root_npm_public_source_profile(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        stripe_js = next(repo for repo in repos if repo.id == "stripe/stripe-js")

        self.assertTrue(stripe_js.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:@stripe/stripe-js@8",
                    "latest-stable",
                    "none",
                ),
                VersionTrack(
                    "package:@stripe/stripe-js@9",
                    "latest-stable",
                    "all-stable",
                ),
            ),
            stripe_js.version_tracks,
        )
        self.assertEqual(1, len(stripe_js.capsules))
        capsule = stripe_js.capsules[0]
        self.assertEqual("stripe-js-public-source", capsule.id)
        self.assertEqual("npm-tracked-source-v1", capsule.adapter)
        self.assertEqual(("@stripe/stripe-js",), capsule.focus_packages)
        self.assertEqual("internal-runtime-closure", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(
            (
                "examples/parcel/src",
                "examples/rollup/src",
                "pure",
                "src",
                "types",
            ),
            capsule.default_required_roots,
        )
        self.assertEqual((), capsule.default_generated_target_paths)
        self.assertEqual((), capsule.include_paths)
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(160, capsule.max_capsule_files)
        self.assertEqual(2000000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(200, capsule.max_packet_files)
        self.assertEqual(2500000, capsule.max_packet_utf8_bytes)

    def test_react_stripe_js_uses_the_root_npm_public_source_profile(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        react_stripe_js = next(
            repo for repo in repos if repo.id == "stripe/react-stripe-js"
        )

        self.assertTrue(react_stripe_js.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:@stripe/react-stripe-js@6",
                    "latest-stable",
                    "all-stable",
                ),
            ),
            react_stripe_js.version_tracks,
        )
        self.assertEqual(1, len(react_stripe_js.capsules))
        capsule = react_stripe_js.capsules[0]
        self.assertEqual("react-stripe-js-public-source", capsule.id)
        self.assertEqual("npm-tracked-source-v1", capsule.adapter)
        self.assertEqual(("@stripe/react-stripe-js",), capsule.focus_packages)
        self.assertEqual("internal-runtime-closure", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(("examples", "src"), capsule.default_required_roots)
        self.assertEqual(("dist/",), capsule.default_generated_target_paths)
        self.assertEqual((), capsule.include_paths)
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(240, capsule.max_capsule_files)
        self.assertEqual(2500000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(280, capsule.max_packet_files)
        self.assertEqual(3000000, capsule.max_packet_utf8_bytes)

    def test_stripe_react_native_uses_the_cross_platform_public_source_profile(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        react_native = next(
            repo for repo in repos if repo.id == "stripe/stripe-react-native"
        )

        self.assertTrue(react_native.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:@stripe/stripe-react-native@0",
                    "latest-stable",
                    "all-stable",
                ),
            ),
            react_native.version_tracks,
        )
        self.assertEqual(1, len(react_native.capsules))
        capsule = react_native.capsules[0]
        self.assertEqual("stripe-react-native-public-source", capsule.id)
        self.assertEqual("npm-tracked-source-v1", capsule.adapter)
        self.assertEqual(("@stripe/stripe-react-native",), capsule.focus_packages)
        self.assertEqual("internal-runtime-closure", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(
            ("android/src/main", "ios", "src"),
            capsule.default_required_roots,
        )
        self.assertEqual(("lib/",), capsule.default_generated_target_paths)
        self.assertEqual(
            (
                "CHANGELOG.md",
                "MIGRATING.md",
                "android/build.gradle",
                "android/gradle.properties",
                "example/src/screens/ApplePayScreen.tsx",
                "example/src/screens/ConnectAccountOnboardingScreen.tsx",
                "example/src/screens/CustomerSheetScreen.tsx",
                "example/src/screens/EmbeddedPaymentElementScreen.tsx",
                "example/src/screens/GooglePayScreen.tsx",
                "example/src/screens/Onramp/CryptoOnrampFlow.tsx",
                "example/src/screens/PaymentSheetDeferredIntentScreen.tsx",
                "example/src/screens/PaymentSheetWithSetupIntent.tsx",
                "stripe-react-native.podspec",
            ),
            capsule.include_paths,
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(340, capsule.max_capsule_files)
        self.assertEqual(3000000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(380, capsule.max_packet_files)
        self.assertEqual(3500000, capsule.max_packet_utf8_bytes)

    def test_adyen_react_native_uses_the_cross_platform_public_source_profile(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        react_native = next(
            repo for repo in repos if repo.id == "adyen/adyen-react-native"
        )

        self.assertTrue(react_native.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:@adyen/react-native@2",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("2.12.0",),
                ),
            ),
            react_native.version_tracks,
        )
        self.assertEqual(1, len(react_native.capsules))
        capsule = react_native.capsules[0]
        self.assertEqual("adyen-react-native-public-source", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("@adyen/react-native",), capsule.focus_packages)
        self.assertEqual("configured-repository-paths", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(
            ("android/src/main", "example/src", "ios", "src"),
            capsule.default_required_roots,
        )
        self.assertEqual((), capsule.default_generated_target_paths)
        self.assertEqual(16, len(capsule.include_paths))
        self.assertTrue(
            {
                "adyen-react-native.podspec",
                "android/build.gradle",
                "android/dependencies.gradle",
                "app.plugin.js",
                "docs/Architecture.md",
                "docs/Compatibility.md",
                "docs/Configuration.md",
                "docs/v2-MigrationGuide.md",
                "example/README.md",
                "example/package.json",
                "package.json",
            }.issubset(set(capsule.include_paths))
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(420, capsule.max_capsule_files)
        self.assertEqual(4000000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(470, capsule.max_packet_files)
        self.assertEqual(5000000, capsule.max_packet_utf8_bytes)

    def test_adyen_node_uses_checkout_deep_and_domain_inventory_profile(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        adyen_node = next(
            repo for repo in repos if repo.id == "adyen/adyen-node-api-library"
        )

        self.assertTrue(adyen_node.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:@adyen/api-library@32",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("32.0.0",),
                ),
            ),
            adyen_node.version_tracks,
        )
        self.assertEqual(1, len(adyen_node.capsules))
        capsule = adyen_node.capsules[0]
        self.assertEqual("adyen-node-checkout-source", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("@adyen/api-library",), capsule.focus_packages)
        self.assertEqual("configured-repository-paths", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(
            (
                "doc",
                "src/constants",
                "src/helpers",
                "src/httpClient",
                "src/security",
                "src/services",
                "src/typings/checkout",
                "src/typings/payment",
                "src/typings/recurring",
                "src/utils",
            ),
            capsule.default_required_roots,
        )
        self.assertEqual(
            (
                "LICENSE",
                "README.md",
                "VERSION",
                "package.json",
                "src/client.ts",
                "src/config.ts",
                "src/index.ts",
                "src/notification/notificationRequest.ts",
                "src/service.ts",
                "src/typings/index.ts",
                "src/typings/notification/amount.ts",
                "src/typings/notification/models.ts",
                "src/typings/notification/notification.ts",
                "src/typings/notification/notificationItem.ts",
                "src/typings/notification/notificationRequestItem.ts",
                "src/webhooks.ts",
                "tsconfig.json",
            ),
            capsule.include_paths,
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual(
            ("35829dc91506c9d75f2227a2d1fee3e2ede206ea84184245748a9d179bd2e197",),
            capsule.historical_policy_hashes,
        )
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(620, capsule.max_capsule_files)
        self.assertEqual(3500000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(700, capsule.max_packet_files)
        self.assertEqual(5000000, capsule.max_packet_utf8_bytes)

    def test_adyen_php_uses_checkout_focused_tagged_profile(self):
        repos = {
            repo.id: repo
            for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
        }
        repo = repos["adyen/adyen-php-api-library"]

        self.assertTrue(repo.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:adyen-php-api-library@30",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("30.0.2",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("adyen-php-checkout-source", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("adyen-php-api-library",), capsule.focus_packages)
        self.assertEqual("configured-repository-paths", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(
            (
                "src/Adyen/HttpClient",
                "src/Adyen/Model/Checkout",
                "src/Adyen/Model/Payments",
                "src/Adyen/Model/Recurring",
                "src/Adyen/Model/TokenizationWebhooks",
                "src/Adyen/Service/Checkout",
                "src/Adyen/Service/Payments",
                "src/Adyen/Service/ResourceModel/Checkout",
                "src/Adyen/Service/ResourceModel/CheckoutUtility",
                "src/Adyen/Service/ResourceModel/Payment",
                "src/Adyen/Service/ResourceModel/Recurring",
                "src/Adyen/Service/Validator",
                "src/Adyen/Util",
            ),
            capsule.default_required_roots,
        )
        self.assertEqual((), capsule.default_generated_target_paths)
        self.assertEqual(24, len(capsule.include_paths))
        self.assertTrue(
            {
                "LICENSE",
                "README.md",
                "SECURITY.md",
                "VERSION",
                "composer.json",
                "src/Adyen/Client.php",
                "src/Adyen/Config.php",
                "src/Adyen/Service/Checkout.php",
                "src/Adyen/Service/Notification.php",
                "src/Adyen/Service/Payment.php",
                "src/Adyen/Service/Recurring.php",
                "src/Adyen/Service/TokenizationWebhookParser.php",
                "src/Adyen/Service/WebhookReceiver.php",
            }.issubset(set(capsule.include_paths))
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(1000000, capsule.max_file_bytes)
        self.assertEqual(500, capsule.max_capsule_files)
        self.assertEqual(9000000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(550, capsule.max_packet_files)
        self.assertEqual(10000000, capsule.max_packet_utf8_bytes)

    def test_adyen_postman_has_reviewed_checkout_terminal_policy(self):
        repos = {
            repo.id: repo
            for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
        }
        repo = repos["adyen/adyen-postman"]

        self.assertTrue(repo.enabled)
        self.assertEqual("api-collection", repo.repo_type)
        self.assertEqual("tier2", repo.priority)
        self.assertEqual("monthly", repo.collection_frequency)
        self.assertEqual("default-branch", repo.track)
        self.assertEqual("commit", repo.version_strategy)
        self.assertEqual((), repo.version_tracks)
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("adyen-postman-checkout-terminal", capsule.id)
        self.assertEqual("commit-tree-v1", capsule.adapter)
        self.assertEqual("adyen-postman", capsule.source_id)
        self.assertEqual("configured-repository-paths", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(
            (
                "in-person-payments/ipp.json",
                "postman/BinLookupService-v54.json",
                "postman/CheckoutService-v72.json",
                "postman/RecurringService-v68.json",
                "postman/TestCardService-v1.json",
            ),
            capsule.default_required_roots,
        )
        self.assertEqual(
            (
                ".github/workflows/sync-collections.yml",
                "README.md",
                "adyendev-postman-release-notes.md",
                "generateAll.sh",
                "in-person-payments/readme.md",
            ),
            capsule.include_paths,
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual(600000, capsule.max_file_bytes)
        self.assertEqual(11, capsule.max_capsule_files)
        self.assertEqual(1100000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(30, capsule.max_packet_files)
        self.assertEqual(3000000, capsule.max_packet_utf8_bytes)

    def test_native_sdks_use_tagged_tree_profiles(self):
        repos = {
            repo.id: repo
            for repo in load_registry(
                ROOT / "tracking/github/repo-registry.toml"
            )
        }

        for repo_id, package, major, pinned, root_count, include_count in (
            (
                "paypal/paypal-android",
                "paypal-android",
                "2",
                "2.3.0",
                6,
                47,
            ),
            (
                "braintree/braintree_android",
                "braintree-android",
                "5",
                "5.30.0",
                17,
                29,
            ),
            (
                "braintree/braintree_ios",
                "braintree-ios",
                "7",
                "7.9.0",
                16,
                19,
            ),
            (
                "stripe/stripe-ios",
                "stripe-ios",
                "26",
                "26.4.1",
                6,
                41,
            ),
            (
                "stripe/stripe-android",
                "stripe-android",
                "23",
                "23.13.1",
                3,
                41,
            ),
        ):
            with self.subTest(repo_id=repo_id):
                repo = repos[repo_id]
                self.assertTrue(repo.enabled)
                self.assertEqual(
                    (
                        VersionTrack(
                            "package:" + package + "@" + major,
                            "latest-stable",
                            "all-stable",
                            False,
                            (pinned,),
                        ),
                    ),
                    repo.version_tracks,
                )
                self.assertEqual(1, len(repo.capsules))
                capsule = repo.capsules[0]
                self.assertEqual("tagged-tree-v1", capsule.adapter)
                self.assertEqual((package,), capsule.focus_packages)
                self.assertEqual(
                    "configured-repository-paths",
                    capsule.dependency_scope,
                )
                self.assertEqual(
                    "policy-bounded",
                    capsule.changed_path_policy,
                )
                self.assertEqual((), capsule.default_generated_target_paths)
                self.assertEqual(
                    root_count,
                    len(capsule.default_required_roots),
                )
                self.assertEqual(
                    include_count,
                    len(capsule.include_paths),
                )
                self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
                self.assertEqual(512000, capsule.max_file_bytes)
                self.assertEqual(500, capsule.max_capsule_files)
                self.assertEqual(5000000, capsule.max_capsule_utf8_bytes)
                self.assertEqual(550, capsule.max_packet_files)
                self.assertEqual(6000000, capsule.max_packet_utf8_bytes)

    def test_registry_matches_appendix_a_inventory_and_collection_cadence(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")

        actual = tuple(
            (
                repo.id,
                repo.url,
                repo.repo_type,
                repo.priority,
                repo.version_strategy,
                repo.enabled,
                repo.track,
                repo.collection_frequency,
            )
            for repo in repos
        )
        self.assertEqual(APPENDIX_A_INVENTORY, actual)

    def test_paypal_v6_sample_has_reviewed_enabled_commit_policy(self):
        repos = {
            repo.id: repo
            for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
        }
        repo = repos["paypal-examples/v6-web-sdk-sample-integration"]

        self.assertTrue(repo.enabled)
        self.assertEqual("sample-app", repo.repo_type)
        self.assertEqual("tier1", repo.priority)
        self.assertEqual("monthly", repo.collection_frequency)
        self.assertEqual("default-branch", repo.track)
        self.assertEqual("commit", repo.version_strategy)
        self.assertEqual((), repo.version_tracks)
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("commit-tree-v1", capsule.adapter)
        self.assertEqual("v6-web-sdk-sample-integration", capsule.source_id)
        self.assertEqual((), capsule.focus_packages)
        self.assertEqual("configured-repository-paths", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual((), capsule.default_generated_target_paths)
        self.assertEqual(
            (
                "client/components",
                "client/prebuiltPages/react/src",
                "client/shared",
                "server/node/src",
            ),
            capsule.default_required_roots,
        )
        self.assertEqual(
            (
                ".env.sample",
                "LICENSE",
                "README.md",
                "client/index.html",
                "client/package.json",
                "client/prebuiltPages/react/README.md",
                "client/prebuiltPages/react/package.json",
                "client/prebuiltPages/react/tsconfig.json",
                "client/prebuiltPages/react/vite.config.ts",
                "server/node/README.md",
                "server/node/package.json",
                "server/node/tsconfig.json",
            ),
            capsule.include_paths,
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(300, capsule.max_capsule_files)
        self.assertEqual(1000000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(550, capsule.max_packet_files)
        self.assertEqual(3000000, capsule.max_packet_utf8_bytes)
        self.assertEqual(
            ("24146810ee2bfac4384859a127e11a7631160f0a8ca5079ea47fb2658d865416",),
            capsule.historical_policy_hashes,
        )

    def test_paypal_mobile_demo_apps_have_reviewed_enabled_commit_policies(self):
        repos = {
            repo.id: repo
            for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
        }
        android = repos["paypal-examples/paypal-android-sdk-demo-app"]
        ios = repos["paypal-examples/paypal-ios-sdk-demo-app"]

        for repo in (android, ios):
            self.assertTrue(repo.enabled)
            self.assertEqual("sample-app", repo.repo_type)
            self.assertEqual("tier1", repo.priority)
            self.assertEqual("monthly", repo.collection_frequency)
            self.assertEqual("default-branch", repo.track)
            self.assertEqual("commit", repo.version_strategy)
            self.assertEqual((), repo.version_tracks)
            self.assertEqual(1, len(repo.capsules))
            capsule = repo.capsules[0]
            self.assertEqual("commit-tree-v1", capsule.adapter)
            self.assertEqual((), capsule.focus_packages)
            self.assertEqual(
                "configured-repository-paths", capsule.dependency_scope
            )
            self.assertEqual("policy-bounded", capsule.changed_path_policy)
            self.assertEqual((), capsule.default_generated_target_paths)
            self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
            self.assertEqual("text-secrets-v1", capsule.secret_detector)
            self.assertEqual(512000, capsule.max_file_bytes)
            self.assertEqual(180, capsule.max_capsule_files)
            self.assertEqual(1200000, capsule.max_capsule_utf8_bytes)
            self.assertEqual(220, capsule.max_packet_files)
            self.assertEqual(2000000, capsule.max_packet_utf8_bytes)

        android_capsule = android.capsules[0]
        self.assertEqual("paypal-android-sdk-demo-source", android_capsule.id)
        self.assertEqual(
            "paypal-android-sdk-demo-app", android_capsule.source_id
        )
        self.assertEqual(
            (
                "app/src/main/java",
                "app/src/main/res/values",
                "app/src/main/res/xml",
            ),
            android_capsule.default_required_roots,
        )
        self.assertEqual(
            (
                "README.md",
                "app/build.gradle",
                "app/src/main/AndroidManifest.xml",
                "build.gradle",
                "gradle.properties",
                "gradle/libs.versions.toml",
                "settings.gradle",
            ),
            android_capsule.include_paths,
        )

        ios_capsule = ios.capsules[0]
        self.assertEqual("paypal-ios-sdk-demo-source", ios_capsule.id)
        self.assertEqual("paypal-ios-sdk-demo-app", ios_capsule.source_id)
        self.assertEqual(
            (
                "PayPalDemo/CardCheckoutViews",
                "PayPalDemo/ConfigSettings",
                "PayPalDemo/Helpers",
                "PayPalDemo/Models",
                "PayPalDemo/Networking",
                "PayPalDemo/ViewModels",
            ),
            ios_capsule.default_required_roots,
        )
        self.assertEqual(
            (
                "PayPalDemo/CheckoutCoordinator.swift",
                "PayPalDemo/CheckoutFlow.swift",
                "PayPalDemo/PayPalDemoApp.swift",
                "PayPalDemo/PaymentLinkCompleteView.swift",
                "README.md",
                "paypal-ios-sdk-demo-app-Info.plist",
                "paypal-ios-sdk-demo-app.entitlements",
                "paypal-ios-sdk-demo-app.xcodeproj/project.pbxproj",
            ),
            ios_capsule.include_paths,
        )

    def test_paypal_typescript_server_sdk_uses_complete_source_profile(self):
        repos = {
            repo.id: repo
            for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
        }
        repo = repos["paypal/paypal-typescript-server-sdk"]

        self.assertTrue(repo.enabled)
        self.assertEqual("server-sdk", repo.repo_type)
        self.assertEqual("tier2", repo.priority)
        self.assertEqual("monthly", repo.collection_frequency)
        self.assertEqual("releases-and-default-branch", repo.track)
        self.assertEqual("semver-tags", repo.version_strategy)
        self.assertEqual(
            (
                VersionTrack(
                    "package:@paypal/paypal-server-sdk@2",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("2.3.0", "2.4.0"),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("paypal-typescript-server-sdk-source", capsule.id)
        self.assertEqual("npm-tracked-source-v1", capsule.adapter)
        self.assertEqual(("@paypal/paypal-server-sdk",), capsule.focus_packages)
        self.assertEqual("internal-runtime-closure", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(("doc/controllers", "src"), capsule.default_required_roots)
        self.assertEqual(("dist/",), capsule.default_generated_target_paths)
        self.assertEqual(
            ("CHANGELOG.md", "LICENSE", "README.md"),
            capsule.include_paths,
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(430, capsule.max_capsule_files)
        self.assertEqual(3000000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(500, capsule.max_packet_files)
        self.assertEqual(4000000, capsule.max_packet_utf8_bytes)

    def test_paypal_php_server_sdk_uses_complete_runtime_source_profile(self):
        repos = {
            repo.id: repo
            for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
        }
        repo = repos["paypal/paypal-php-server-sdk"]

        self.assertTrue(repo.enabled)
        self.assertEqual("server-sdk", repo.repo_type)
        self.assertEqual("tier2", repo.priority)
        self.assertEqual("monthly", repo.collection_frequency)
        self.assertEqual("releases-and-default-branch", repo.track)
        self.assertEqual("semver-tags", repo.version_strategy)
        self.assertEqual(
            (
                VersionTrack(
                    "package:paypal/paypal-server-sdk@2",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("2.4.0",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("paypal-php-server-sdk-source", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("paypal/paypal-server-sdk",), capsule.focus_packages)
        self.assertEqual("configured-repository-paths", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(("doc/controllers", "src"), capsule.default_required_roots)
        self.assertEqual((), capsule.default_generated_target_paths)
        self.assertEqual(
            ("CHANGELOG.md", "LICENSE", "README.md", "composer.json"),
            capsule.include_paths,
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(750, capsule.max_capsule_files)
        self.assertEqual(6000000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(780, capsule.max_packet_files)
        self.assertEqual(7000000, capsule.max_packet_utf8_bytes)
        self.assertEqual(
            (
                "CHANGELOG.md",
                "LICENSE",
                "README.md",
                "composer.json",
                "doc/controllers",
                "src/ApiHelper.php",
                "src/Authentication",
                "src/ClientCredentialsAuth.php",
                "src/ConfigurationDefaults.php",
                "src/ConfigurationInterface.php",
                "src/Controllers",
                "src/Environment.php",
                "src/Exceptions",
                "src/Http",
                "src/Logging",
                "src/PaypalServerSdkClient.php",
                "src/PaypalServerSdkClientBuilder.php",
                "src/Proxy",
                "src/Server.php",
                "src/Utils",
                "src/Models/BalancesResponse.php",
                "src/Models/BillingPlan.php",
                "src/Models/CapturedPayment.php",
                "src/Models/CustomerVaultPaymentTokensResponse.php",
                "src/Models/ModifySubscriptionResponse.php",
                "src/Models/OAuthToken.php",
                "src/Models/Order.php",
                "src/Models/OrderAuthorizeResponse.php",
                "src/Models/PaymentAuthorization.php",
                "src/Models/PaymentTokenResponse.php",
                "src/Models/PlanCollection.php",
                "src/Models/Refund.php",
                "src/Models/SearchResponse.php",
                "src/Models/SetupTokenResponse.php",
                "src/Models/Subscription.php",
                "src/Models/SubscriptionCollection.php",
                "src/Models/SubscriptionTransactionDetails.php",
                "src/Models/TransactionsList.php",
            ),
            repo.ingest_required_paths,
        )

    def test_paypal_server_side_sample_has_reviewed_enabled_commit_policy(self):
        repos = {
            repo.id: repo
            for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
        }
        repo = repos["paypal-examples/paypal-sdk-server-side-integration"]

        self.assertTrue(repo.enabled)
        self.assertEqual("sample-app", repo.repo_type)
        self.assertEqual("tier1", repo.priority)
        self.assertEqual("monthly", repo.collection_frequency)
        self.assertEqual("default-branch", repo.track)
        self.assertEqual("commit", repo.version_strategy)
        self.assertEqual((), repo.version_tracks)
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("commit-tree-v1", capsule.adapter)
        self.assertEqual("paypal-sdk-server-side-integration", capsule.source_id)
        self.assertEqual((), capsule.focus_packages)
        self.assertEqual("configured-repository-paths", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual((), capsule.default_generated_target_paths)
        self.assertEqual(
            ("docs", "public", "src"),
            capsule.default_required_roots,
        )
        self.assertEqual(
            ("README.md", "example.env", "package.json", "tsconfig.json"),
            capsule.include_paths,
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(50, capsule.max_capsule_files)
        self.assertEqual(250000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(60, capsule.max_packet_files)
        self.assertEqual(900000, capsule.max_packet_utf8_bytes)

    def test_metronome_ai_uses_complete_skills_and_scenarios_profile(self):
        repos = {
            repo.id: repo
            for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
        }
        repo = repos["metronome-industries/ai"]

        self.assertTrue(repo.enabled)
        self.assertEqual("default-branch", repo.track)
        self.assertEqual("commit", repo.version_strategy)
        self.assertEqual((), repo.version_tracks)
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("metronome-ai-skills", capsule.id)
        self.assertEqual("commit-tree-v1", capsule.adapter)
        self.assertEqual("metronome-ai", capsule.source_id)
        self.assertEqual("configured-repository-paths", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertEqual(("skills",), capsule.default_required_roots)
        self.assertEqual((), capsule.default_generated_target_paths)
        self.assertEqual(
            {
                "README.md",
                "CONTRIBUTING.md",
                "LICENSE",
                "tests/dogfood/scenarios/add-new-product-to-existing.md",
                "tests/dogfood/scenarios/change-pricing-raise-rate.md",
                "tests/dogfood/scenarios/start-billing-saas-with-credits.md",
            },
            set(capsule.include_paths),
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(80, capsule.max_capsule_files)
        self.assertEqual(1000000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(100, capsule.max_packet_files)
        self.assertEqual(1500000, capsule.max_packet_utf8_bytes)

    def test_adyen_magento2_uses_checkout_plugin_profile(self):
        repos = {
            repo.id: repo
            for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
        }
        repo = repos["adyen/adyen-magento2"]

        self.assertTrue(repo.enabled)
        self.assertEqual(
            (
                VersionTrack(
                    "package:adyen/module-payment@11",
                    "latest-stable",
                    "all-stable",
                    False,
                    ("11.0.0",),
                ),
            ),
            repo.version_tracks,
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        self.assertEqual("adyen-magento2-checkout-source", capsule.id)
        self.assertEqual("tagged-tree-v1", capsule.adapter)
        self.assertEqual(("adyen/module-payment",), capsule.focus_packages)
        self.assertEqual("configured-repository-paths", capsule.dependency_scope)
        self.assertEqual("policy-bounded", capsule.changed_path_policy)
        self.assertTrue(
            {
                "Api",
                "Controller",
                "Gateway",
                "Helper",
                "Model",
                "etc",
                "view/frontend",
            }.issubset(set(capsule.default_required_roots))
        )
        self.assertEqual((), capsule.default_generated_target_paths)
        self.assertEqual(
            {
                "LICENSE.txt",
                "README.md",
                "SECURITY.md",
                "VERSION",
                "composer.json",
                "registration.php",
            },
            set(capsule.include_paths),
        )
        self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
        self.assertEqual("text-secrets-v1", capsule.secret_detector)
        self.assertEqual(512000, capsule.max_file_bytes)
        self.assertEqual(600, capsule.max_capsule_files)
        self.assertEqual(4000000, capsule.max_capsule_utf8_bytes)
        self.assertEqual(650, capsule.max_packet_files)
        self.assertEqual(5000000, capsule.max_packet_utf8_bytes)
        self.assertEqual(
            (
                "README.md",
                "VERSION",
                "composer.json",
                "Api/AdyenGiftcardInterface.php",
                "Api/AdyenOrderPaymentStatusInterface.php",
                "Api/AdyenPaymentMethodManagementInterface.php",
                "Api/AdyenPaymentsDetailsInterface.php",
                "Api/AdyenPosCloudInterface.php",
                "Api/AdyenStateDataInterface.php",
                "Api/TokenDeactivateInterface.php",
                "Api/Webhook/WebhookAcceptorInterface.php",
                "Cron/PaymentResponseCleanUp.php",
                "Cron/StateDataCleanUp.php",
                "Cron/WebhookProcessor.php",
                "Gateway/Http/Client/TransactionCancel.php",
                "Gateway/Http/Client/TransactionCapture.php",
                "Gateway/Http/Client/TransactionPayment.php",
                "Gateway/Http/Client/TransactionRefund.php",
                "Gateway/Request/BrowserInfoDataBuilder.php",
                "Gateway/Request/CaptureDataBuilder.php",
                "Gateway/Request/CheckoutDataBuilder.php",
                "Gateway/Request/GiftcardDataBuilder.php",
                "Gateway/Request/LineItemsDataBuilder.php",
                "Gateway/Request/MerchantAccountDataBuilder.php",
                "Gateway/Request/MerchantRiskIndicatorDataBuilder.php",
                "Gateway/Request/OneclickAuthorizationDataBuilder.php",
                "Gateway/Request/OriginDataBuilder.php",
                "Gateway/Request/PaymentDataBuilder.php",
                "Gateway/Request/PosCloudBuilder.php",
                "Gateway/Request/RecurringDataBuilder.php",
                "Gateway/Request/RecurringVaultDataBuilder.php",
                "Gateway/Request/RefundDataBuilder.php",
                "Gateway/Request/ReturnUrlDataBuilder.php",
                "Gateway/Request/ShopperInteractionDataBuilder.php",
                "Gateway/Response/CheckoutPaymentsResponseHandler.php",
                "Gateway/Response/CheckoutStateDataCleanupHandler.php",
                "Gateway/Response/ModificationsCapturesResponseHandler.php",
                "Gateway/Response/ModificationsRefundsResponseHandler.php",
                "Gateway/Response/PaymentPosCloudHandler.php",
                "Gateway/Validator/CheckoutResponseValidator.php",
                "Helper/Config.php",
                "Helper/Creditmemo.php",
                "Helper/GiftcardPayment.php",
                "Helper/Idempotency.php",
                "Helper/Invoice.php",
                "Helper/Order.php",
                "Helper/PaymentMethods.php",
                "Helper/PaymentMethodsFilter.php",
                "Helper/PaymentResponseHandler.php",
                "Helper/PaymentsDetails.php",
                "Helper/PointOfSale.php",
                "Helper/Quote.php",
                "Helper/StateData.php",
                "Helper/Vault.php",
                "Helper/Webhook.php",
                "Helper/Webhook/AuthorisationWebhookHandler.php",
                "Helper/Webhook/CaptureWebhookHandler.php",
                "Helper/Webhook/RecurringContractWebhookHandler.php",
                "Helper/Webhook/RecurringTokenCreatedWebhookHandler.php",
                "Helper/Webhook/RefundWebhookHandler.php",
                "Helper/Webhook/WebhookHandlerFactory.php",
                "Model/Api",
                "Model/Method",
                "Model/PaymentResponse.php",
                "Model/Resolver",
                "Model/StateData.php",
                "Model/Ui",
                "Model/Webhook",
                "Observer/AdyenCcDataAssignObserver.php",
                "Observer/AdyenPaymentMethodDataAssignObserver.php",
                "Observer/SetOrderStateAfterPaymentObserver.php",
                "Plugin/CustomerFilterVaultTokens.php",
                "Plugin/GraphQlPlaceOrderAddCartId.php",
                "Plugin/PaymentInformationManagement.php",
                "Plugin/PaymentVaultDeleteToken.php",
                "Plugin/SortAndFilterAdyenPaymentMethods.php",
                "etc/config.xml",
                "etc/crontab.xml",
                "etc/csp_whitelist.xml",
                "etc/db_schema.xml",
                "etc/events.xml",
                "etc/payment.xml",
                "etc/queue_consumer.xml",
                "etc/queue_publisher.xml",
                "etc/queue_topology.xml",
                "etc/schema.graphqls",
                "etc/webapi.xml",
                "view/frontend",
            ),
            repo.ingest_required_paths,
        )


if __name__ == "__main__":
    unittest.main()
