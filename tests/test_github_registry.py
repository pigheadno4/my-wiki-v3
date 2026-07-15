import dataclasses
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_registry import RepoConfig, load_registry, select_repos, validate_registry  # noqa: E402
from toml_compat import load_toml  # noqa: E402


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
        repo = self.repo()

        self.assertEqual("on-demand", repo.collection_frequency)
        self.assertEqual((), repo.requested_refs)
        self.assertEqual((), repo.key_paths)
        self.assertEqual((), repo.exclude_paths)
        self.assertEqual(1048576, repo.max_file_bytes)
        self.assertEqual(10485760, repo.max_snapshot_bytes)
        with self.assertRaises(dataclasses.FrozenInstanceError):
            repo.enabled = False

    def test_registry_rejects_duplicate_ids_and_mutable_state(self):
        repos = (self.repo(), self.repo())
        self.assertTrue(any("duplicate id" in error for error in validate_registry(repos)))

        repo = self.repo()
        object.__setattr__(repo, "latest_version", "10.0.0")
        self.assertTrue(any("latest_version" in error for error in validate_registry((repo,))))

    def test_load_registry_rejects_mutable_state(self):
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
            'latest_version = "10.0.0"\n'
        )

        with self.assertRaisesRegex(ValueError, "latest_version"):
            load_registry(path)

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

    def test_full_inventory_has_71_rows_and_five_enabled_pilots(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")

        self.assertEqual(71, len(repos))
        self.assertEqual(5, len(select_repos(repos, enabled_only=True)))
        self.assertEqual(
            {
                "paypal/paypal-js",
                "paypal-examples/v6-web-sdk-sample-integration",
                "braintree/braintree_ios",
                "stripe/stripe-ios",
                "adyen/adyen-web",
            },
            {repo.id for repo in select_repos(repos)},
        )


if __name__ == "__main__":
    unittest.main()
