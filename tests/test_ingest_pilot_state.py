import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path

from scripts.ingest_pilot.state import (
    PilotError,
    append_event,
    campaign_paths,
    create_attempt,
    initialize_state,
    load_campaign,
    load_jobs,
    recover_interrupted,
    render_monitor,
    save_jobs,
    write_attempt_file,
)


class PilotStateTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)
        self.campaign_id = "metronome-minimum-pilot-01"
        self.manifest = {
            "campaign_id": self.campaign_id,
            "provider": "metronome",
            "jobs": [
                {
                    "job_id": "security-principles",
                    "raw_path": "raw/metronome/guides/platform-configuration/security-principles-2026-07-13.md",
                    "raw_sha256": "0" * 64,
                    "source_target": "wiki/sources/metronome/source-metronome-guides-platform-configuration-security-principles.md",
                    "canonical_url": "https://docs.metronome.com/guides/platform-configuration/security-principles.md",
                },
                {
                    "job_id": "audit-logs",
                    "raw_path": "raw/metronome/guides/platform-configuration/audit-logs-2026-07-13.md",
                    "raw_sha256": "1" * 64,
                    "source_target": "wiki/sources/metronome/source-metronome-guides-platform-configuration-audit-logs.md",
                    "canonical_url": "https://docs.metronome.com/guides/platform-configuration/audit-logs.md",
                },
                {
                    "job_id": "setup-webhooks",
                    "raw_path": "raw/metronome/guides/platform-configuration/setup-webhooks-2026-07-13.md",
                    "raw_sha256": "2" * 64,
                    "source_target": "wiki/sources/metronome/source-metronome-guides-platform-configuration-setup-webhooks.md",
                    "canonical_url": "https://docs.metronome.com/guides/platform-configuration/setup-webhooks.md",
                },
                {
                    "job_id": "role-based-access-rbac",
                    "raw_path": "raw/metronome/guides/platform-configuration/role-based-access-rbac-2026-07-13.md",
                    "raw_sha256": "3" * 64,
                    "source_target": "wiki/sources/metronome/source-metronome-guides-platform-configuration-role-based-access-rbac.md",
                    "canonical_url": "https://docs.metronome.com/guides/platform-configuration/role-based-access-rbac.md",
                },
                {
                    "job_id": "single-sign-on-sso",
                    "raw_path": "raw/metronome/guides/platform-configuration/single-sign-on-sso-2026-07-13.md",
                    "raw_sha256": "4" * 64,
                    "source_target": "wiki/sources/metronome/source-metronome-guides-platform-configuration-single-sign-on-sso.md",
                    "canonical_url": "https://docs.metronome.com/guides/platform-configuration/single-sign-on-sso.md",
                },
            ],
        }

    def initialize_jobs(self):
        initialize_state(self.root, self.manifest)
        return load_jobs(self.root, self.campaign_id)

    def test_initialize_fails_without_truncating_existing_events(self):
        paths = campaign_paths(self.root, self.campaign_id)
        paths["campaign_dir"].mkdir(parents=True)
        expected_events = b'{"event":"existing"}\n'
        paths["events"].write_bytes(expected_events)

        with self.assertRaisesRegex(PilotError, "events.jsonl already exists"):
            initialize_state(self.root, self.manifest)

        self.assertEqual(paths["events"].read_bytes(), expected_events)
        self.assertFalse(paths["jobs"].exists())

    def test_initialize_rejects_a_destination_manifest_that_differs_from_input(self):
        paths = campaign_paths(self.root, self.campaign_id)
        paths["campaign_dir"].mkdir(parents=True)
        destination_manifest = dict(self.manifest)
        destination_manifest["jobs"] = list(self.manifest["jobs"])
        destination_manifest["jobs"][0] = dict(destination_manifest["jobs"][0])
        destination_manifest["jobs"][0]["job_id"] = "different-security-principles"
        expected_manifest = (json.dumps(destination_manifest, indent=2) + "\n").encode("utf-8")
        paths["manifest"].write_bytes(expected_manifest)

        with self.assertRaisesRegex(PilotError, "destination manifest does not match input"):
            initialize_state(self.root, self.manifest)

        self.assertEqual(paths["manifest"].read_bytes(), expected_manifest)
        self.assertFalse(paths["jobs"].exists())

    def test_initialize_creates_only_minimum_campaign_files(self):
        initialize_state(self.root, self.manifest)

        campaign_dir = self.root / "tracking/ingest/metronome/metronome-minimum-pilot-01"
        self.assertEqual(
            sorted(path.name for path in campaign_dir.iterdir()),
            ["campaign.json", "events.jsonl", "jobs.json", "manifest.json", "monitor.md"],
        )
        jobs = load_jobs(self.root, self.campaign_id)
        self.assertEqual([job["state"] for job in jobs], ["queued"] * 5)
        self.assertEqual([job["queue_position"] for job in jobs], [1, 2, 3, 4, 5])
        self.assertEqual(
            load_campaign(self.root, self.campaign_id),
            {
                "schema_version": 1,
                "campaign_id": self.campaign_id,
                "provider": "metronome",
                "state": "active",
                "worker_concurrency": 5,
                "max_attempts": 3,
                "review_concurrency": 1,
                "mode": "dry_run",
            },
        )

    def test_initialize_preserves_portable_worker_routing_metadata(self):
        manifest = deepcopy(self.manifest)
        manifest["jobs"][0]["recommended_worker_tier"] = "standard"
        manifest["jobs"][0]["routing_reason"] = "short operational guide"
        manifest["jobs"][1]["recommended_worker_tier"] = "strong"
        manifest["jobs"][1]["routing_reason"] = "cross-provider billing boundary"

        initialize_state(self.root, manifest)

        jobs = load_jobs(self.root, self.campaign_id)
        self.assertEqual(jobs[0]["recommended_worker_tier"], "standard")
        self.assertEqual(jobs[0]["routing_reason"], "short operational guide")
        self.assertEqual(jobs[1]["recommended_worker_tier"], "strong")
        self.assertEqual(jobs[1]["routing_reason"], "cross-provider billing boundary")
        self.assertNotIn("recommended_worker_tier", jobs[2])
        self.assertNotIn("routing_reason", jobs[2])

    def test_initialize_rejects_incomplete_worker_routing_metadata(self):
        incomplete = deepcopy(self.manifest)
        incomplete["jobs"][0]["recommended_worker_tier"] = "standard"

        with self.assertRaisesRegex(
            PilotError, "worker routing requires both recommended_worker_tier and routing_reason"
        ):
            initialize_state(self.root, incomplete)

        paths = campaign_paths(self.root, self.campaign_id)
        self.assertFalse(paths["manifest"].exists())
        self.assertFalse(paths["campaign"].exists())
        self.assertFalse(paths["jobs"].exists())

    def test_initialize_rejects_unknown_worker_tier(self):
        unknown = deepcopy(self.manifest)
        unknown["jobs"][0]["recommended_worker_tier"] = "premium"
        unknown["jobs"][0]["routing_reason"] = "unsupported tier"

        with self.assertRaisesRegex(PilotError, "recommended_worker_tier must be standard or strong"):
            initialize_state(self.root, unknown)

        paths = campaign_paths(self.root, self.campaign_id)
        self.assertFalse(paths["manifest"].exists())
        self.assertFalse(paths["campaign"].exists())
        self.assertFalse(paths["jobs"].exists())

    def test_initialize_rejects_blank_routing_reason(self):
        blank = deepcopy(self.manifest)
        blank["jobs"][0]["recommended_worker_tier"] = "standard"
        blank["jobs"][0]["routing_reason"] = "   "

        with self.assertRaisesRegex(PilotError, "routing_reason must be non-empty text"):
            initialize_state(self.root, blank)

    def test_initialize_rejects_non_text_worker_tier(self):
        malformed = deepcopy(self.manifest)
        malformed["jobs"][0]["recommended_worker_tier"] = []
        malformed["jobs"][0]["routing_reason"] = "invalid type"

        with self.assertRaisesRegex(PilotError, "recommended_worker_tier must be standard or strong"):
            initialize_state(self.root, malformed)

    def test_initialize_copies_review_concurrency_and_validates_audit_jobs(self):
        parallel = deepcopy(self.manifest)
        parallel["review_concurrency"] = 2
        parallel["audit_job_ids"] = ["security-principles", "audit-logs", "setup-webhooks"]

        initialize_state(self.root, parallel)

        campaign = load_campaign(self.root, self.campaign_id)
        self.assertEqual(campaign["review_concurrency"], 2)
        self.assertEqual(campaign["audit_job_ids"], parallel["audit_job_ids"])

    def test_initialize_defaults_legacy_review_concurrency_and_rejects_invalid_parallel_audit_shape(self):
        initialize_state(self.root, self.manifest)
        self.assertEqual(load_campaign(self.root, self.campaign_id)["review_concurrency"], 1)

        invalid = deepcopy(self.manifest)
        invalid["campaign_id"] = "invalid-parallel-audit"
        invalid["review_concurrency"] = 2
        invalid["audit_job_ids"] = ["security-principles", "security-principles", "not-in-manifest"]
        with self.assertRaisesRegex(PilotError, "audit_job_ids"):
            initialize_state(self.root, invalid)
        paths = campaign_paths(self.root, invalid["campaign_id"])
        self.assertFalse(paths["campaign"].exists())

        zero = deepcopy(self.manifest)
        zero["campaign_id"] = "zero-review-concurrency"
        zero["review_concurrency"] = 0
        with self.assertRaisesRegex(PilotError, "review_concurrency must be a positive integer"):
            initialize_state(self.root, zero)

        explicit_null = deepcopy(self.manifest)
        explicit_null["campaign_id"] = "null-audit-job-ids"
        explicit_null["audit_job_ids"] = None
        with self.assertRaisesRegex(PilotError, "audit_job_ids"):
            initialize_state(self.root, explicit_null)
        self.assertFalse(campaign_paths(self.root, explicit_null["campaign_id"])["campaign"].exists())

    def test_save_jobs_replaces_projection_without_rewriting_events(self):
        self.initialize_jobs()
        jobs = load_jobs(self.root, self.campaign_id)
        jobs[0]["state"] = "running"
        events = campaign_paths(self.root, self.campaign_id)["events"]
        before_events = events.read_bytes()

        save_jobs(self.root, self.campaign_id, jobs)

        self.assertEqual(load_jobs(self.root, self.campaign_id)[0]["state"], "running")
        self.assertEqual(events.read_bytes(), before_events)

    def test_save_jobs_rejects_a_preexisting_sibling_tmp_file(self):
        jobs = self.initialize_jobs()
        paths = campaign_paths(self.root, self.campaign_id)
        paths["jobs_tmp"].write_text("stale", encoding="utf-8")

        with self.assertRaisesRegex(PilotError, "temporary jobs file already exists"):
            save_jobs(self.root, self.campaign_id, jobs)

        self.assertEqual(paths["jobs_tmp"].read_text(encoding="utf-8"), "stale")

    def test_attempt_files_are_additive_and_never_overwritten(self):
        jobs = self.initialize_jobs()
        attempt = create_attempt(self.root, self.campaign_id, jobs[0], 1)
        write_attempt_file(attempt, "input.json", b"{}\n")

        with self.assertRaisesRegex(PilotError, "already exists"):
            write_attempt_file(attempt, "input.json", b'{"changed":true}\n')

        self.assertEqual((attempt / "input.json").read_bytes(), b"{}\n")

    def test_restart_fails_running_and_reviewing_jobs(self):
        jobs = self.initialize_jobs()
        jobs[0]["state"] = "running"
        jobs[1]["state"] = "reviewing"
        jobs[2]["state"] = "candidate_ready"
        save_jobs(self.root, self.campaign_id, jobs)

        recovered = recover_interrupted(self.root, self.campaign_id)

        self.assertEqual([recovered[0]["state"], recovered[1]["state"]], ["failed", "failed"])
        self.assertEqual(recovered[2]["state"], "candidate_ready")
        self.assertEqual(recovered[0]["failure_reason"], "interrupted")
        events = campaign_paths(self.root, self.campaign_id)["events"].read_text(encoding="utf-8")
        self.assertIn('"event":"interrupted"', events)

    def test_append_event_is_compact_and_does_not_change_jobs(self):
        jobs = self.initialize_jobs()

        append_event(self.root, self.campaign_id, {"event": "worker_started", "job_id": "security-principles"})

        event_line = campaign_paths(self.root, self.campaign_id)["events"].read_text(
            encoding="utf-8"
        ).splitlines()[-1]
        self.assertEqual(
            json.loads(event_line),
            {"event": "worker_started", "job_id": "security-principles"},
        )
        self.assertNotIn(" ", event_line)
        self.assertEqual(load_jobs(self.root, self.campaign_id), jobs)

    def test_append_event_failure_preserves_jobs(self):
        jobs = self.initialize_jobs()
        events = campaign_paths(self.root, self.campaign_id)["events"]
        events.unlink()
        events.mkdir()

        with self.assertRaises(PilotError):
            append_event(self.root, self.campaign_id, {"event": "cannot_append"})

        self.assertEqual(load_jobs(self.root, self.campaign_id), jobs)

    def test_render_monitor_uses_current_job_counts_and_table(self):
        jobs = self.initialize_jobs()
        jobs[0]["state"] = "running"
        jobs[1]["state"] = "candidate_ready"
        jobs[2]["state"] = "reviewing"
        jobs[3]["state"] = "approved"
        jobs[4]["state"] = "failed"
        jobs[4]["failure_reason"] = "worker_timeout"
        save_jobs(self.root, self.campaign_id, jobs)

        monitor = render_monitor(self.root, self.campaign_id)

        self.assertIn("# Metronome Minimum Pilot 01", monitor)
        self.assertIn("- Campaign state: `active`", monitor)
        self.assertIn("- Worker concurrency: `5`", monitor)
        self.assertIn("- Queued: 0", monitor)
        self.assertIn("- Running: 1", monitor)
        self.assertIn("- Candidate ready: 1", monitor)
        self.assertIn("- Reviewing: 1", monitor)
        self.assertIn("- Approved: 1", monitor)
        self.assertIn("- Failed: 1", monitor)
        self.assertIn("| Job | Attempt | State | Raw | Source target | Last event | Failure |", monitor)
        self.assertIn("worker_timeout", monitor)
        self.assertEqual(
            campaign_paths(self.root, self.campaign_id)["monitor"].read_text(encoding="utf-8"),
            monitor,
        )


if __name__ == "__main__":
    unittest.main()
