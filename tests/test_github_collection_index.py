import json
import sys
import tempfile
import unittest
from dataclasses import replace
from datetime import date
from itertools import permutations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_collection_index import (  # noqa: E402
    build_collection_index,
    load_collection_index,
    render_collection_index,
    validate_collection_index,
    write_collection_index,
)
from github_canonical import canonical_json_bytes  # noqa: E402
from github_registry import RepoConfig, load_registry  # noqa: E402
from github_work_items import (  # noqa: E402
    PackageChange,
    RefChange,
    WorkItem,
)


SHA = "a" * 40


def _repo(repo_id, *, enabled=True, frequency="monthly", priority="tier1"):
    company = repo_id.split("/", 1)[0]
    return RepoConfig(
        id=repo_id,
        company=company,
        url="https://github.com/" + repo_id,
        enabled=enabled,
        repo_type="sdk",
        priority=priority,
        track="releases-and-default-branch",
        version_strategy="semver-tags",
        collection_frequency=frequency,
    )


def _item(repo_id, state, mode="delta", *, day="2026-08-01"):
    change = PackageChange(
        "example-sdk",
        "1.0.0",
        "1.1.0",
        "example-sdk@1.1.0",
        "raw/release.json",
        "tracking/comparison.json",
        mode,
        ("contained-minor-release",),
    )
    return WorkItem(
        "github-" + repo_id.replace("/", "")[:8].ljust(20, "0"),
        repo_id,
        SHA,
        day,
        (change,),
        "raw/snapshot.json",
        mode,
        state=state,
        approved_mode=mode if state in ("approved", "ingesting", "ingested") else None,
        last_error="network timeout" if state == "collection_failed" else "",
    )


class CollectionIndexTests(unittest.TestCase):
    def test_untracked_major_check_overrides_wait_without_changing_accepted_release(self):
        repo = _repo("alpha/sdk", frequency="weekly")
        item = _item(repo.id, "ingested")
        rows = build_collection_index(
            (repo,), (item,),
            checked_state={repo.id: {
                "last_checked_date": "2026-08-02",
                "latest_discovered_ref": "example-sdk@2.0.0",
                "last_error": "untracked stable major: example-sdk@2.0.0",
            }},
            today=date(2026, 8, 2),
        )
        row = rows["repositories"][0]
        self.assertEqual("manual-review", row["next_action"])
        self.assertEqual("example-sdk@1.1.0", row["last_accepted_ref"])

    def test_same_day_core_patch_follows_shared_monorepo_release(self):
        core = replace(
            _item("alpha/sdk", "ingested").package_changes[0],
            package="@example/core",
            from_version="11.2.0",
            to_version="11.2.1",
            release_id="@example/core@11.2.1",
        )
        react = replace(
            core,
            package="@example/react",
            from_version="10.5.2",
            to_version="10.6.0",
            release_id="@example/react@10.6.0",
        )
        shared = replace(
            _item("alpha/sdk", "ingested"),
            work_item_id="github-ffffffffffffffffffff",
            package_changes=(core, react),
        )
        patch = replace(
            shared,
            work_item_id="github-00000000000000000000",
            package_changes=(replace(
                core,
                from_version="11.2.1",
                to_version="11.2.2",
                release_id="@example/core@11.2.2",
            ),),
        )
        older_react = replace(
            shared,
            work_item_id="github-88888888888888888888",
            package_changes=(replace(
                react,
                from_version="10.5.1",
                to_version="10.5.2",
                release_id="@example/react@10.5.2",
            ),),
        )
        for items in permutations((shared, patch, older_react)):
            with self.subTest(order=[item.work_item_id for item in items]):
                row = build_collection_index(
                    (_repo("alpha/sdk"),), items, {}, date(2026, 8, 3)
                )["repositories"][0]
                self.assertEqual("@example/core@11.2.2", row["last_accepted_ref"])
                self.assertEqual("@example/core@11.2.2", row["latest_discovered_ref"])
                self.assertEqual("@example/core@11.2.1", row["comparison_base"])

        pending = tuple(
            replace(
                item,
                state="collection_failed" if item is older_react else "awaiting_approval",
                approved_mode=None,
            )
            for item in (shared, patch, older_react)
        )
        for items in permutations(pending):
            with self.subTest(pending_order=[item.work_item_id for item in items]):
                row = build_collection_index(
                    (_repo("alpha/sdk"),), items, {}, date(2026, 8, 3)
                )["repositories"][0]
                self.assertEqual("@example/core@11.2.2", row["latest_discovered_ref"])
                self.assertEqual("@example/core@11.2.1", row["comparison_base"])
                self.assertEqual("collection_failed", row["queue_state"])
                self.assertEqual("retry", row["next_action"])

    def test_conflicting_same_day_package_histories_have_stable_fallback(self):
        template = _item("alpha/sdk", "ingested")

        def item(item_id, versions):
            return replace(
                template,
                work_item_id=item_id,
                package_changes=tuple(
                    replace(template.package_changes[0], package=package,
                            to_version=version, release_id=package + "@" + version)
                    for package, version in versions
                ),
            )

        # Overlapping partial histories imply a cycle rather than a release order.
        first = item("github-00000000000000000000", (("core", "1.0.0"), ("react", "3.0.0")))
        second = item("github-88888888888888888888", (("core", "2.0.0"), ("lpm", "1.0.0")))
        third = item("github-ffffffffffffffffffff", (("react", "2.0.0"), ("lpm", "2.0.0")))
        for items in permutations((first, second, third)):
            row = build_collection_index(
                (_repo("alpha/sdk"),), items, {}, date(2026, 8, 3)
            )["repositories"][0]
            self.assertEqual("react@2.0.0, lpm@2.0.0", row["last_accepted_ref"])

    def test_ingested_ref_boundary_does_not_replace_last_package_release(self):
        release = replace(
            _item("alpha/sdk", "ingested", "full", day="2026-08-01"),
            work_item_id="github-release0000000000000",
        )
        ref_change = RefChange(
            "default-branch",
            "main",
            "b" * 40,
            "c" * 40,
            "default-branch@ccccccc",
            "tracking/ref-comparison.json",
            "delta",
            ("contained-default-branch-change",),
        )
        boundary = WorkItem(
            "github-boundary0000000000",
            "alpha/sdk",
            "c" * 40,
            "2026-08-02",
            (),
            "raw/ref-snapshot.json",
            "delta",
            approved_mode="delta",
            state="ingested",
            ref_changes=(ref_change,),
        )

        document = build_collection_index(
            (_repo("alpha/sdk"),),
            (release, boundary),
            {},
            date(2026, 8, 3),
        )
        row = document["repositories"][0]

        self.assertEqual("example-sdk@1.1.0", row["last_accepted_ref"])
        self.assertEqual("default-branch@ccccccc", row["latest_discovered_ref"])

    def test_same_day_ingested_baseline_does_not_hide_pending_delta(self):
        baseline = replace(
            _item("alpha/sdk", "ingested", "full"),
            work_item_id="github-ffffffffffffffffffff",
        )
        delta_change = PackageChange(
            "example-sdk",
            "1.1.0",
            "1.2.0",
            "example-sdk@1.2.0",
            "raw/release-1.2.0.json",
            "tracking/comparison-1.1.0--1.2.0.json",
            "delta",
            ("contained-minor-release",),
        )
        delta = replace(
            _item("alpha/sdk", "awaiting_approval", "delta"),
            work_item_id="github-00000000000000000000",
            package_changes=(delta_change,),
        )

        document = build_collection_index(
            (_repo("alpha/sdk"),),
            (baseline, delta),
            {},
            date(2026, 8, 3),
        )
        row = document["repositories"][0]

        self.assertEqual("example-sdk@1.2.0", row["latest_discovered_ref"])
        self.assertEqual("example-sdk@1.1.0", row["comparison_base"])
        self.assertEqual("awaiting_approval", row["queue_state"])
        self.assertEqual("review-delta", row["next_action"])

    def test_actions_scheduling_and_sorting(self):
        repos = (
            _repo("zeta/disabled", enabled=False, priority="tier3"),
            _repo("beta/baseline", frequency="weekly", priority="tier2"),
            _repo("alpha/wait", frequency="monthly"),
            _repo("alpha/review-delta"),
            _repo("alpha/review-full"),
            _repo("alpha/ingest"),
            _repo("alpha/retry"),
            _repo("alpha/manual"),
        )
        items = (
            _item("alpha/wait", "ingested"),
            _item("alpha/review-delta", "awaiting_approval", "delta"),
            _item("alpha/review-full", "awaiting_approval", "full"),
            _item("alpha/ingest", "approved"),
            _item("alpha/retry", "collection_failed"),
            replace(_item("alpha/manual", "collection_failed"), state="needs_manual_review"),
        )
        checked = {
            "alpha/wait": {
                "last_checked_date": "2026-08-01",
                "latest_discovered_ref": "example-sdk@1.1.0",
            }
        }

        document = build_collection_index(repos, items, checked, date(2026, 8, 3))
        rows = document["repositories"]

        self.assertEqual(
            sorted(
                rows,
                key=lambda row: (
                    row["company"],
                    {"tier1": 1, "tier2": 2, "tier3": 3}[row["priority"]],
                    row["repo_id"],
                ),
            ),
            rows,
        )
        actions = {row["repo_id"]: row["next_action"] for row in rows}
        self.assertEqual("disabled", actions["zeta/disabled"])
        self.assertEqual("collect-baseline", actions["beta/baseline"])
        self.assertEqual("wait", actions["alpha/wait"])
        self.assertEqual("review-delta", actions["alpha/review-delta"])
        self.assertEqual("review-full", actions["alpha/review-full"])
        self.assertEqual("ingest", actions["alpha/ingest"])
        self.assertEqual("retry", actions["alpha/retry"])
        self.assertEqual("manual-review", actions["alpha/manual"])
        wait = next(row for row in rows if row["repo_id"] == "alpha/wait")
        self.assertEqual("2026-09-01", wait["next_due_date"])

    def test_real_registry_coverage_and_deterministic_views(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        document = build_collection_index(repos, (), {}, date(2026, 8, 3))
        self.assertEqual(71, len(document["repositories"]))
        self.assertEqual(
            render_collection_index(document), render_collection_index(document)
        )

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write_collection_index(root, repos, (), {}, date(2026, 8, 3))
            loaded = load_collection_index(root)
            self.assertEqual(document, loaded)
            self.assertEqual(
                render_collection_index(document),
                (root / "tracking/github/collection-index.md").read_text(),
            )

    def test_validation_rejects_malformed_or_mismatched_views(self):
        repos = (_repo("alpha/sdk"),)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write_collection_index(root, repos, (), {}, date(2026, 8, 3))
            self.assertEqual([], validate_collection_index(root, repos, ()))

            markdown = root / "tracking/github/collection-index.md"
            markdown.write_text("stale\n", encoding="utf-8")
            self.assertIn(
                "tracking/github/collection-index.md is stale",
                validate_collection_index(root, repos, ()),
            )

            json_path = root / "tracking/github/collection-index.json"
            json_path.write_text(json.dumps({"format_version": 1}), encoding="utf-8")
            self.assertTrue(validate_collection_index(root, repos, ()))

    def test_validation_rejects_queue_identity_tampering(self):
        repos = (_repo("alpha/sdk"),)
        item = _item("alpha/sdk", "awaiting_approval")
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            document = write_collection_index(
                root, repos, (item,), {}, date(2026, 8, 3)
            )
            document["repositories"][0]["latest_discovered_ref"] = "fake@9.9.9"
            path = root / "tracking/github/collection-index.json"
            path.write_bytes(canonical_json_bytes(document) + b"\n")
            self.assertIn(
                "tracking/github/collection-index.json does not match registry and queue",
                validate_collection_index(root, repos, (item,)),
            )


if __name__ == "__main__":
    unittest.main()
