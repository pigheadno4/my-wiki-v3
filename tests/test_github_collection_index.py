import json
import sys
import tempfile
import unittest
from dataclasses import replace
from datetime import date
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
