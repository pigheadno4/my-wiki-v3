"""Tests for GitHub collection and ingest state reporting."""

import json
from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_packets import PacketRecord  # noqa: E402
from github_registry import RepoConfig  # noqa: E402
from github_reporting import (  # noqa: E402
    COLLECTION_TERMINAL,
    PACKET_TRANSITIONS,
    CollectionReconciliationError,
    StateTransitionError,
    append_event,
    render_collection_status,
    render_ingest_status,
    transition_packet,
    validate_collection_run,
)


class GitHubReportingTests(unittest.TestCase):
    def config(self, repo_id="paypal/paypal-js", enabled=True):
        company = repo_id.split("/", 1)[0]
        return RepoConfig(
            id=repo_id,
            company=company,
            url="https://github.com/" + repo_id,
            enabled=enabled,
            repo_type="sdk",
            priority="tier1",
            track="releases-and-default-branch",
            version_strategy="semver-tags",
        )

    def packet(self, packet_id="baseline-1.0.0-aaaaaaa"):
        return PacketRecord(
            packet_id=packet_id,
            repo_id="paypal/paypal-js",
            packet_type="baseline",
            from_snapshot="",
            to_snapshot="raw/github/paypal/paypal-js/snapshots/v1",
            required_reading=("raw/github/paypal/paypal-js/snapshots/v1/snapshot.md",),
            changed_files=(),
            initial_state="awaiting-review",
            directory=Path("tracking/github/repos/paypal/paypal-js/packets") / packet_id,
        )

    def test_exact_collection_terminal_and_packet_transition_sets(self):
        self.assertEqual(
            {"unchanged", "collected-baseline", "collected-change", "retry-pending", "failed"},
            COLLECTION_TERMINAL,
        )
        self.assertEqual(
            {
                "awaiting-review": {"approved", "rejected"},
                "approved": {"ingesting", "rejected"},
                "ingesting": {"ingested", "validation-failed"},
                "validation-failed": {"approved", "rejected"},
                "ingested": set(),
                "rejected": set(),
            },
            PACKET_TRANSITIONS,
        )

    def test_append_event_appends_one_sorted_json_object_per_line(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nested" / "events.jsonl"

            append_event(path, {"z": 2, "a": 1})
            append_event(path, {"state": "approved", "packet_id": "p1"})

            self.assertEqual(
                '{"a": 1, "z": 2}\n'
                '{"packet_id": "p1", "state": "approved"}\n',
                path.read_text(encoding="utf-8"),
            )

    def test_every_allowed_packet_transition_returns_requested_state(self):
        for current, requested_states in PACKET_TRANSITIONS.items():
            for requested in requested_states:
                with self.subTest(current=current, requested=requested):
                    self.assertEqual(requested, transition_packet(current, requested))

    def test_invalid_or_unknown_packet_transition_raises(self):
        for current, requested in (
            ("awaiting-review", "ingesting"),
            ("ingested", "approved"),
            ("unknown", "approved"),
            ("approved", "unknown"),
        ):
            with self.subTest(current=current, requested=requested):
                with self.assertRaises(StateTransitionError):
                    transition_packet(current, requested)

    def test_collection_reconciliation_requires_one_terminal_per_selected_repo_ref(self):
        events = (
            {"repo_id": "paypal/paypal-js", "selector": "default-branch", "selected": True, "state": "selected"},
            {"repo_id": "paypal/paypal-js", "selector": "default-branch", "state": "unchanged"},
            {"repo_id": "stripe/stripe-ios", "selector": "v1", "selected": True, "state": "selected"},
        )

        with self.assertRaisesRegex(CollectionReconciliationError, "stripe/stripe-ios.*v1"):
            validate_collection_run(events)

    def test_collection_reconciliation_rejects_duplicate_terminal_events(self):
        events = (
            {"repo_id": "paypal/paypal-js", "selector": "default-branch", "selected": True, "state": "selected"},
            {"repo_id": "paypal/paypal-js", "selector": "default-branch", "state": "unchanged"},
            {"repo_id": "paypal/paypal-js", "selector": "default-branch", "state": "failed"},
        )

        with self.assertRaisesRegex(CollectionReconciliationError, "exactly one terminal"):
            validate_collection_run(events)

    def test_collection_reconciliation_counts_selected_targets(self):
        events = (
            {"repo_id": "paypal/paypal-js", "selector": "v1", "selected": True, "state": "selected"},
            {"repo_id": "paypal/paypal-js", "selector": "v1", "state": "collected-baseline"},
            {"repo_id": "paypal/paypal-js", "selector": "v2", "selected": True, "state": "selected"},
            {"repo_id": "paypal/paypal-js", "selector": "v2", "state": "collected-change"},
        )

        self.assertEqual(2, validate_collection_run(events))

    def test_collection_status_uses_latest_terminal_event_and_lists_unattempted_repos(self):
        repos = (self.config(), self.config("stripe/stripe-ios", enabled=False))
        events = (
            {"repo_id": "paypal/paypal-js", "selector": "v1", "state": "failed", "error": "old"},
            {"repo_id": "paypal/paypal-js", "selector": "v1", "state": "collected-change", "version": "1.1.0"},
        )

        status = render_collection_status(repos, events)

        self.assertIn("# GitHub Collection Status", status)
        self.assertIn("paypal/paypal-js", status)
        self.assertIn("collected-change", status)
        self.assertIn("1.1.0", status)
        self.assertIn("stripe/stripe-ios", status)
        self.assertIn("not-collected", status)
        self.assertTrue(status.endswith("\n"))
        self.assertFalse(status.endswith("\n\n"))

    def test_ingest_status_renders_packet_state_without_mutating_packet_contract(self):
        packet = self.packet()
        original = dict(vars(packet))

        status = render_ingest_status((packet,), {packet.packet_id: "approved"})

        self.assertIn("# GitHub Ingest Status", status)
        self.assertIn(packet.packet_id, status)
        self.assertIn("baseline", status)
        self.assertIn("approved", status)
        self.assertEqual(original, vars(packet))

    def test_reporting_events_remain_json_serializable(self):
        event = {"repo_id": "paypal/paypal-js", "selector": "v1", "state": "unchanged"}
        self.assertEqual(event, json.loads(json.dumps(event, sort_keys=True)))


if __name__ == "__main__":
    unittest.main()
