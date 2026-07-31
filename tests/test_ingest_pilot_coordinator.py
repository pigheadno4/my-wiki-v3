import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.ingest_pilot.coordinator import (
    PilotError,
    complete_campaign,
    init_campaign,
    reject_job,
    retry_job,
    run_once,
    status,
)
from scripts.ingest_pilot.state import load_jobs, save_jobs


class CoordinatorTests(unittest.TestCase):
    def setUp(self):
        temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(temporary_directory.cleanup)
        self.root = Path(temporary_directory.name)
        self.campaign_id = "metronome-minimum-pilot-01"
        self.manifest = {
            "campaign_id": self.campaign_id,
            "provider": "metronome",
            "jobs": [self.make_manifest_job(number) for number in range(1, 6)],
        }

    def make_manifest_job(self, number):
        raw_path = f"raw/metronome/job-{number}.md"
        raw = self.root / raw_path
        raw.parent.mkdir(parents=True, exist_ok=True)
        raw.write_text(
            f"# Metronome job {number}\n\n"
            "Least privilege\n"
            "Separation of duties\n"
            "Secure by default\n",
            encoding="utf-8",
        )
        return {
            "job_id": f"job-{number}",
            "raw_path": raw_path,
            "raw_sha256": hashlib.sha256(raw.read_bytes()).hexdigest(),
            "source_target": f"wiki/sources/metronome/source-job-{number}.md",
            "canonical_url": f"https://docs.metronome.com/job-{number}",
        }

    def test_run_emits_five_orders_and_persists_running_attempts(self):
        init_campaign(self.root, self.manifest)

        output = run_once(self.root, self.campaign_id)

        self.assertEqual(len(output["worker_orders"]), 5)
        jobs = load_jobs(self.root, self.campaign_id)
        self.assertEqual([job["state"] for job in jobs], ["running"] * 5)
        self.assertEqual([job["attempt"] for job in jobs], [1] * 5)
        campaign_dir = self.root / "tracking/ingest/metronome" / self.campaign_id
        for job in jobs:
            attempt = campaign_dir / "attempts" / job["job_id"] / "attempt-1"
            self.assertTrue(attempt.joinpath("input.json").is_file())

    def start_five(self):
        init_campaign(self.root, self.manifest)
        run_once(self.root, self.campaign_id)

    def attempt(self, job_id, number):
        return (
            self.root
            / "tracking"
            / "ingest"
            / "metronome"
            / self.campaign_id
            / "attempts"
            / job_id
            / f"attempt-{number}"
        )

    def write_worker_result(self, job_id, attempt=1, **overrides):
        job = next(job for job in load_jobs(self.root, self.campaign_id) if job["job_id"] == job_id)
        raw_stem = Path(job["raw_path"]).stem
        result = {
            "job_id": job_id,
            "attempt": attempt,
            "source_page": (
                "---\n"
                f'title: "{job_id}"\n'
                "type: source\n"
                "date_ingested: 2026-07-27\n"
                f'canonical_url: "{job["canonical_url"]}"\n'
                "original_format: webpage\n"
                "raw_files:\n"
                f'  - "{job["raw_path"].removeprefix("raw/")}"\n'
                "tags: [metronome]\n"
                "---\n\n"
                "## Raw Sources\n"
                f"- [[{job['raw_path'].removesuffix('.md')}|{raw_stem}]] — verbatim documentation\n"
            ),
            "quotes": [
                {"text": "Least privilege", "location": "body"},
                {"text": "Separation of duties", "location": "body"},
                {"text": "Secure by default", "location": "body"},
            ],
            "suggestions": {"company": [], "concepts": [], "index": [], "log": []},
            "raw_path": job["raw_path"],
            "raw_sha256": job["raw_sha256"],
            "status": "candidate_ready",
        }
        result.update(overrides)
        path = self.root / f"{job_id}-worker-result.json"
        path.write_text(json.dumps(result), encoding="utf-8")
        return path

    def write_review(self, job_id, attempt, verdict, **overrides):
        result = {
            "job_id": job_id,
            "attempt": attempt,
            "verdict": verdict,
            "reason": "Grounded and complete",
            "required_changes": [],
            "review_scope": "full",
            "retry_review_scope": None,
            "shared_update_decisions": [],
        }
        result.update(overrides)
        path = self.root / f"{job_id}-review-result.json"
        path.write_text(json.dumps(result), encoding="utf-8")
        return path

    def make_reviewing(self, job_id, attempt, suggestions=None):
        init_campaign(self.root, self.manifest)
        jobs = load_jobs(self.root, self.campaign_id)
        job = next(job for job in jobs if job["job_id"] == job_id)
        job["attempt"] = attempt
        job["state"] = "reviewing"
        job["last_event"] = "review_started"
        job["reviewer_identity"] = "reviewer-a"
        job["reviewer_model"] = "Sol"
        save_jobs(self.root, self.campaign_id, jobs)
        attempt_dir = self.attempt(job_id, attempt)
        attempt_dir.mkdir(parents=True)
        suggestions = suggestions or {"company": [], "concepts": [], "index": [], "log": []}
        attempt_dir.joinpath("suggestions.json").write_text(
            json.dumps(suggestions),
            encoding="utf-8",
        )
        self.write_receipt(job, attempt_dir, suggestions)

    def write_receipt(self, job, attempt_dir, suggestions):
        attempt_dir.joinpath("receipt.json").write_text(json.dumps({
            "job_id": job["job_id"],
            "attempt": job["attempt"],
            "source_page": "validated source page",
            "quotes": [
                {"text": "Least privilege", "location": "body"},
                {"text": "Separation of duties", "location": "body"},
                {"text": "Secure by default", "location": "body"},
            ],
            "suggestions": suggestions,
            "raw_path": job["raw_path"],
            "raw_sha256": job["raw_sha256"],
            "status": "candidate_ready",
        }), encoding="utf-8")

    def test_valid_worker_result_persists_candidate_and_emits_review_order(self):
        self.start_five()

        output = run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-1"),
            reviewer_assignments=[{"identity": "reviewer-a", "model": "Sol"}],
        )

        job = load_jobs(self.root, self.campaign_id)[0]
        self.assertEqual(job["state"], "reviewing")
        attempt = self.attempt("job-1", 1)
        self.assertTrue(attempt.joinpath("candidate.md").is_file())
        self.assertTrue(attempt.joinpath("receipt.json").is_file())
        self.assertTrue(attempt.joinpath("suggestions.json").is_file())
        self.assertEqual(output["review_order"]["job_id"], "job-1")

    def test_serial_v2_review_requires_provenance_and_persists_review_evidence(self):
        self.start_five()

        candidate = run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-1"),
            reviewer_assignments=[{"identity": "reviewer-a", "model": "Sol"}],
        )
        approved = run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review("job-1", 1, "approved"),
        )

        review_path = self.attempt("job-1", 1).joinpath("review.json")
        self.assertEqual(candidate["review_order"]["reviewer_identity"], "reviewer-a")
        self.assertEqual(approved["jobs"][0]["state"], "approved")
        self.assertTrue(review_path.is_file())
        review = json.loads(review_path.read_text(encoding="utf-8"))
        self.assertEqual(review["reviewer_identity"], "reviewer-a")
        self.assertEqual(review["reviewer_model"], "Sol")

    def test_serial_v2_candidate_requires_a_reviewer_assignment(self):
        self.start_five()

        with self.assertRaisesRegex(PilotError, "reviewer assignments"):
            run_once(
                self.root,
                self.campaign_id,
                worker_result_path=self.write_worker_result("job-1"),
            )

        self.assertEqual(load_jobs(self.root, self.campaign_id)[0]["state"], "running")

    def test_invalid_worker_result_fails_only_that_job(self):
        self.start_five()

        output = run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-1", raw_sha256="0" * 64),
        )

        self.assertEqual(load_jobs(self.root, self.campaign_id)[0]["state"], "failed")
        self.assertTrue(self.attempt("job-1", 1).joinpath("failure.json").is_file())
        self.assertEqual(output["campaign_state"], "active")

    def test_unhashable_worker_update_kind_becomes_failure_evidence(self):
        self.start_five()
        suggestion = {
            "update_id": "concept-billing-link",
            "target_path": "wiki/concepts/metronome/metronome-billing.md",
            "update_kind": ["durable_fact"],
            "anchor": "## Sources",
            "proposed_markdown": "- [[source-job-1]] — documented billing behavior",
            "quote_indexes": [0],
            "warnings": [],
        }

        output = run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-1", suggestions={
                "company": [], "concepts": [suggestion], "index": [], "log": [],
            }),
        )

        failure = json.loads(self.attempt("job-1", 1).joinpath("failure.json").read_text(encoding="utf-8"))
        self.assertEqual(output["jobs"][0]["state"], "failed")
        self.assertIn("update_kind", failure["reason"])

    def test_third_invalid_worker_result_is_terminal_and_retains_failure_evidence(self):
        self.start_five()

        for attempt in (1, 2):
            run_once(
                self.root,
                self.campaign_id,
                worker_result_path=self.write_worker_result(
                    "job-1", attempt=attempt, raw_sha256="0" * 64
                ),
            )
            self.assertEqual(load_jobs(self.root, self.campaign_id)[0]["state"], "failed")
            retry_job(self.root, self.campaign_id, "job-1")
            run_once(self.root, self.campaign_id)

        output = run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-1", attempt=3, raw_sha256="0" * 64),
        )

        job = load_jobs(self.root, self.campaign_id)[0]
        self.assertEqual(job["state"], "rejected")
        self.assertEqual(job["last_event"], "worker_result_rejected")
        self.assertTrue(self.attempt("job-1", 3).joinpath("failure.json").is_file())
        self.assertEqual(output["jobs"][0]["state"], "rejected")

    def test_terminal_rejections_clear_retry_and_active_review_context(self):
        init_campaign(self.root, self.manifest)
        jobs = load_jobs(self.root, self.campaign_id)
        jobs[0].update({
            "attempt": 3,
            "state": "running",
            "retry_context": {
                "prior_attempt": 2,
                "review_scope": "targeted",
                "required_changes": ["Fix the concept backlink and no other prose."],
                "prior_reviewer_identity": "reviewer-a",
            },
            "active_review_scope": "targeted",
        })
        save_jobs(self.root, self.campaign_id, jobs)

        run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-1", attempt=3, raw_sha256="0" * 64),
        )

        terminal_worker = load_jobs(self.root, self.campaign_id)[0]
        self.assertEqual(terminal_worker["state"], "rejected")
        self.assertNotIn("retry_context", terminal_worker)
        self.assertNotIn("active_review_scope", terminal_worker)

        terminal_worker.update({
            "state": "failed",
            "retry_context": {
                "prior_attempt": 2,
                "review_scope": "full",
                "required_changes": ["Fix the concept backlink and no other prose."],
                "prior_reviewer_identity": "reviewer-a",
            },
            "active_review_scope": "full",
        })
        save_jobs(self.root, self.campaign_id, [terminal_worker, *load_jobs(self.root, self.campaign_id)[1:]])

        reject_job(self.root, self.campaign_id, "job-1", "operator decision")

        terminal_operator = load_jobs(self.root, self.campaign_id)[0]
        self.assertEqual(terminal_operator["state"], "rejected")
        self.assertNotIn("retry_context", terminal_operator)
        self.assertNotIn("active_review_scope", terminal_operator)

    def test_non_utf8_worker_result_fails_only_that_job(self):
        self.start_five()
        result_path = self.write_worker_result("job-1")
        result = json.loads(result_path.read_text(encoding="utf-8"))
        result["source_page"] += "\ud800"
        result_path.write_text(json.dumps(result), encoding="utf-8")

        output = run_once(self.root, self.campaign_id, worker_result_path=result_path)

        self.assertEqual(load_jobs(self.root, self.campaign_id)[0]["state"], "failed")
        self.assertTrue(self.attempt("job-1", 1).joinpath("failure.json").is_file())
        self.assertEqual(output["campaign_state"], "active")

    def test_approved_review_stays_dry_run_approved(self):
        self.make_reviewing("job-1", attempt=1)

        output = run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review("job-1", 1, "approved"),
        )

        self.assertEqual(load_jobs(self.root, self.campaign_id)[0]["state"], "approved")
        self.assertNotIn("promotion_order", output)

    def test_complete_requires_terminal_jobs_and_records_explicit_campaign_close(self):
        with patch(
            "scripts.ingest_pilot.state._utc_now", return_value="2026-07-31T01:02:03Z"
        ):
            self.start_five()
        run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-1"),
            reviewer_assignments=[{"identity": "reviewer-a", "model": "Sol"}],
        )
        run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review("job-1", 1, "approved"),
        )
        jobs = load_jobs(self.root, self.campaign_id)
        for job in jobs[1:]:
            job["state"] = "rejected"
        save_jobs(self.root, self.campaign_id, jobs)
        review_path = self.attempt("job-1", 1) / "review.json"
        review_before = review_path.read_bytes()

        with patch(
            "scripts.ingest_pilot.coordinator._utc_now", return_value="2026-07-31T04:05:06Z"
        ):
            output = complete_campaign(self.root, self.campaign_id, 2)

        campaign = json.loads((self.root / "tracking/ingest/metronome" / self.campaign_id / "campaign.json").read_text(encoding="utf-8"))
        self.assertEqual(campaign["state"], "complete")
        self.assertEqual(campaign["completed_at"], "2026-07-31T04:05:06Z")
        self.assertEqual(campaign["coordinator_repairs"], 2)
        self.assertEqual(output["campaign_state"], "complete")
        self.assertIn("- Completed at: `2026-07-31T04:05:06Z`", output["monitor"])
        self.assertIn("- Elapsed: `10983 seconds`", output["monitor"])
        self.assertEqual(review_path.read_bytes(), review_before)
        with self.assertRaisesRegex(PilotError, "already complete"):
            complete_campaign(self.root, self.campaign_id, 0)

    def test_complete_rejects_invalid_repair_counts_and_nonterminal_jobs(self):
        init_campaign(self.root, self.manifest)
        for repairs in (-1, True):
            with self.subTest(repairs=repairs):
                with self.assertRaisesRegex(PilotError, "non-negative integer"):
                    complete_campaign(self.root, self.campaign_id, repairs)

        for state in ("queued", "running", "candidate_ready", "reviewing", "failed"):
            with self.subTest(state=state):
                jobs = load_jobs(self.root, self.campaign_id)
                for job in jobs:
                    job["state"] = "approved"
                jobs[0]["state"] = state
                save_jobs(self.root, self.campaign_id, jobs)
                with self.assertRaisesRegex(PilotError, "terminal"):
                    complete_campaign(self.root, self.campaign_id, 0)

    def test_complete_validates_approved_evidence_before_persisting_completion_and_can_retry(self):
        self.make_reviewing("job-1", attempt=1)
        run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review("job-1", 1, "approved"),
        )
        jobs = load_jobs(self.root, self.campaign_id)
        for job in jobs[1:]:
            job["state"] = "rejected"
        save_jobs(self.root, self.campaign_id, jobs)
        review_path = self.attempt("job-1", 1) / "review.json"
        evidence = review_path.read_bytes()
        review_path.unlink()

        with self.assertRaisesRegex(PilotError, "cannot read result"):
            complete_campaign(self.root, self.campaign_id, 0)

        campaign_path = self.root / "tracking/ingest/metronome" / self.campaign_id / "campaign.json"
        self.assertEqual(json.loads(campaign_path.read_text(encoding="utf-8"))["state"], "active")

        review_path.write_bytes(evidence)
        output = complete_campaign(self.root, self.campaign_id, 0)
        self.assertEqual(output["campaign_state"], "complete")

    def test_changes_requested_queues_fresh_attempt_at_tail(self):
        self.make_reviewing("job-1", attempt=1)
        initial_tail = max(job["queue_position"] for job in load_jobs(self.root, self.campaign_id))

        run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review(
                "job-1", 1, "changes_requested",
                required_changes=["Revise the source page"], retry_review_scope="full",
            ),
        )

        job = load_jobs(self.root, self.campaign_id)[0]
        self.assertEqual(job["state"], "queued")
        self.assertGreater(job["queue_position"], initial_tail)
        self.assertEqual(job["attempt"], 1)
        self.assertFalse(self.attempt("job-1", 2).exists())

    def test_targeted_changes_request_carries_bounded_context_to_retry_orders(self):
        self.make_reviewing("job-1", attempt=1)

        run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review(
                "job-1", 1, "changes_requested",
                required_changes=["Fix the concept backlink and no other prose."],
                retry_review_scope="targeted",
            ),
        )

        queued = load_jobs(self.root, self.campaign_id)[0]
        self.assertEqual(
            queued["retry_context"],
            {
                "prior_attempt": 1,
                "review_scope": "targeted",
                "required_changes": ["Fix the concept backlink and no other prose."],
                "prior_reviewer_identity": "reviewer-a",
            },
        )
        self.assertNotIn("reviewer_identity", queued)
        self.assertNotIn("reviewer_model", queued)

        retry = run_once(self.root, self.campaign_id)
        worker_order = next(order for order in retry["worker_orders"] if order["job_id"] == "job-1")
        self.assertEqual(worker_order["retry_context"], queued["retry_context"])

        corrected = run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-1", attempt=2),
            reviewer_assignments=[{"identity": "reviewer-a", "model": "Sol"}],
        )

        self.assertEqual(corrected["review_order"]["review_scope"], "targeted")
        self.assertEqual(corrected["review_order"]["prior_attempt"], 1)
        self.assertEqual(corrected["review_order"]["preferred_reviewer_identity"], "reviewer-a")

    def test_full_retry_does_not_prefer_the_prior_reviewer(self):
        self.make_reviewing("job-1", attempt=1)

        run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review(
                "job-1", 1, "changes_requested",
                required_changes=["Fix the concept backlink and no other prose."],
                retry_review_scope="full",
            ),
        )
        run_once(self.root, self.campaign_id)
        corrected = run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-1", attempt=2),
            reviewer_assignments=[{"identity": "reviewer-b", "model": "Sol"}],
        )

        self.assertEqual(corrected["review_order"]["review_scope"], "full")
        self.assertEqual(corrected["review_order"]["prior_attempt"], 1)
        self.assertIsNone(corrected["review_order"]["preferred_reviewer_identity"])

    def test_third_changes_request_rejects_job(self):
        self.make_reviewing("job-1", attempt=3)

        run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review(
                "job-1", 3, "changes_requested",
                required_changes=["Revise the source page"], retry_review_scope="full",
            ),
        )

        self.assertEqual(load_jobs(self.root, self.campaign_id)[0]["state"], "rejected")

    def test_rejected_review_is_immediately_terminal(self):
        self.make_reviewing("job-1", attempt=1)

        run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review("job-1", 1, "rejected", reason="Not grounded"),
        )

        job = load_jobs(self.root, self.campaign_id)[0]
        self.assertEqual(job["state"], "rejected")
        self.assertEqual(job["failure_reason"], "Not grounded")

    def test_approved_review_requires_no_changes_and_no_retry_scope(self):
        self.make_reviewing("job-1", attempt=1)
        for overrides in (
            {"required_changes": ["Revise the source page"]},
            {"retry_review_scope": "targeted"},
        ):
            with self.subTest(overrides=overrides):
                with self.assertRaisesRegex(PilotError, "review result is invalid"):
                    run_once(
                        self.root,
                        self.campaign_id,
                        review_result_path=self.write_review("job-1", 1, "approved", **overrides),
                    )

    def test_changes_requested_requires_changes_and_a_retry_scope(self):
        self.make_reviewing("job-1", attempt=1)
        for overrides in (
            {},
            {"required_changes": ["Revise the source page"], "retry_review_scope": None},
            {"required_changes": ["Revise the source page"], "retry_review_scope": "partial"},
        ):
            with self.subTest(overrides=overrides):
                with self.assertRaisesRegex(PilotError, "review result is invalid"):
                    run_once(
                        self.root,
                        self.campaign_id,
                        review_result_path=self.write_review("job-1", 1, "changes_requested", **overrides),
                    )

    def test_review_scope_must_be_full_or_targeted(self):
        self.make_reviewing("job-1", attempt=1)

        with self.assertRaisesRegex(PilotError, "review result is invalid"):
            run_once(
                self.root,
                self.campaign_id,
                review_result_path=self.write_review("job-1", 1, "approved", review_scope="partial"),
            )

    def test_review_result_must_match_the_active_review_scope(self):
        self.make_reviewing("job-1", attempt=1)
        jobs = load_jobs(self.root, self.campaign_id)
        jobs[0]["active_review_scope"] = "targeted"
        save_jobs(self.root, self.campaign_id, jobs)

        with self.assertRaisesRegex(PilotError, "review result is invalid"):
            run_once(
                self.root,
                self.campaign_id,
                review_result_path=self.write_review("job-1", 1, "approved", review_scope="full"),
            )

        self.assertEqual(load_jobs(self.root, self.campaign_id)[0]["state"], "reviewing")

    def test_review_result_boolean_attempt_is_rejected_without_transitioning_job(self):
        self.make_reviewing("job-1", attempt=1)

        with self.assertRaisesRegex(PilotError, "review result does not match a reviewing job"):
            run_once(
                self.root,
                self.campaign_id,
                review_result_path=self.write_review("job-1", True, "approved"),
            )

        self.assertEqual(load_jobs(self.root, self.campaign_id)[0]["state"], "reviewing")

    def test_review_enum_lists_are_rejected_without_type_errors(self):
        self.make_reviewing("job-1", attempt=1)
        malformed_results = (
            {"verdict": ["approved"]},
            {"review_scope": ["full"]},
            {
                "verdict": "changes_requested",
                "required_changes": ["Revise the source page"],
                "retry_review_scope": ["targeted"],
            },
            {"shared_update_decisions": [{
                "update_id": "unexpected", "verdict": ["approved"], "reason": "Grounded",
            }]},
        )
        for overrides in malformed_results:
            with self.subTest(overrides=overrides):
                verdict = overrides.get("verdict", "approved")
                payload = {key: value for key, value in overrides.items() if key != "verdict"}
                with self.assertRaisesRegex(PilotError, "review result is invalid"):
                    run_once(
                        self.root,
                        self.campaign_id,
                        review_result_path=self.write_review("job-1", 1, verdict, **payload),
                    )

    def test_legacy_review_verdict_list_is_rejected_without_a_type_error(self):
        self.make_reviewing("job-1", attempt=1)
        campaign_path = self.root / "tracking/ingest/metronome" / self.campaign_id / "campaign.json"
        campaign = json.loads(campaign_path.read_text(encoding="utf-8"))
        campaign["schema_version"] = 1
        campaign_path.write_text(json.dumps(campaign), encoding="utf-8")
        legacy_review = self.root / "legacy-review.json"
        legacy_review.write_text(json.dumps({
            "job_id": "job-1",
            "attempt": 1,
            "verdict": ["approved"],
            "reason": "Grounded and complete",
            "required_changes": [],
        }), encoding="utf-8")

        with self.assertRaisesRegex(PilotError, "review result is invalid"):
            run_once(self.root, self.campaign_id, review_result_path=legacy_review)

    def test_review_decisions_match_current_attempt_suggestions(self):
        suggestion = {
            "update_id": "concept-billing-link",
            "target_path": "wiki/concepts/metronome/metronome-billing.md",
            "update_kind": "durable_fact",
            "anchor": "## Sources",
            "proposed_markdown": "- [[source-job-1]] — documented billing behavior",
            "quote_indexes": [0],
            "warnings": [],
        }
        self.make_reviewing("job-1", attempt=1, suggestions={
            "company": [], "concepts": [suggestion], "index": [], "log": [],
        })
        invalid_decision_sets = (
            [],
            [{"update_id": "concept-billing-link", "verdict": "approved"}],
            [{"update_id": "concept-billing-link", "verdict": "deferred", "reason": "Later"}],
            [{"update_id": "other-update", "verdict": "approved", "reason": "Grounded"}],
            [
                {"update_id": "concept-billing-link", "verdict": "approved", "reason": "Grounded"},
                {"update_id": "concept-billing-link", "verdict": "rejected", "reason": "Duplicate"},
            ],
        )
        for decisions in invalid_decision_sets:
            with self.subTest(decisions=decisions):
                with self.assertRaisesRegex(PilotError, "review result is invalid"):
                    run_once(
                        self.root,
                        self.campaign_id,
                        review_result_path=self.write_review(
                            "job-1", 1, "approved", shared_update_decisions=decisions,
                        ),
                    )

        output = run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review("job-1", 1, "approved", shared_update_decisions=[{
                "update_id": "concept-billing-link", "verdict": "approved", "reason": "Grounded",
            }]),
        )
        review = json.loads(self.attempt("job-1", 1).joinpath("review.json").read_text(encoding="utf-8"))
        self.assertEqual(output["jobs"][0]["state"], "approved")
        self.assertEqual(review["shared_update_decisions"][0]["update_id"], "concept-billing-link")

    def test_status_groups_only_reviewer_approved_shared_updates(self):
        approved_billing_updates = (
            ("job-1", "billing-a", "- [[source-job-1]] — billing fact A"),
            ("job-2", "billing-b", "- [[source-job-2]] — billing fact B"),
        )
        self.make_reviewing("job-1", attempt=1)
        jobs = load_jobs(self.root, self.campaign_id)
        for job_id, update_id, proposed_markdown in approved_billing_updates:
            job = next(job for job in jobs if job["job_id"] == job_id)
            job["attempt"] = 1
            job["state"] = "approved"
            job["last_event"] = "review_approved"
            job["reviewer_identity"] = "reviewer-a"
            job["reviewer_model"] = "Sol"
            attempt = self.attempt(job_id, 1)
            attempt.mkdir(parents=True, exist_ok=True)
            suggestions = {
                "company": [{
                    "update_id": f"{update_id}-company",
                    "target_path": "wiki/companies/metronome.md",
                    "update_kind": "durable_fact",
                    "anchor": "## Overview",
                    "proposed_markdown": "- unnecessary company update",
                    "quote_indexes": [0],
                    "warnings": [],
                }],
                "concepts": [{
                    "update_id": update_id,
                    "target_path": "wiki/concepts/metronome/metronome-billing.md",
                    "update_kind": "durable_fact",
                    "anchor": "## Sources",
                    "proposed_markdown": proposed_markdown,
                    "quote_indexes": [0],
                    "warnings": [],
                }],
                "index": [],
                "log": [],
            }
            attempt.joinpath("suggestions.json").write_text(json.dumps(suggestions), encoding="utf-8")
            attempt.joinpath("receipt.json").write_text(json.dumps({
                "job_id": job_id,
                "attempt": 1,
                "source_page": "valid receipt source page",
                "quotes": [
                    {"text": "Least privilege", "location": "body"},
                    {"text": "Separation of duties", "location": "body"},
                    {"text": "Secure by default", "location": "body"},
                ],
                "suggestions": suggestions,
                "raw_path": job["raw_path"],
                "raw_sha256": job["raw_sha256"],
                "status": "candidate_ready",
            }), encoding="utf-8")
            review = {
                "job_id": job_id,
                "attempt": 1,
                "verdict": "approved",
                "reason": "Grounded and complete",
                "required_changes": [],
                "review_scope": "full",
                "retry_review_scope": None,
                "shared_update_decisions": [
                    {"update_id": f"{update_id}-company", "verdict": "rejected", "reason": "Unnecessary"},
                    {"update_id": update_id, "verdict": "approved", "reason": "Grounded"},
                ],
                "reviewer_identity": "reviewer-a",
                "reviewer_model": "Sol",
            }
            attempt.joinpath("review.json").write_text(json.dumps(review), encoding="utf-8")
        save_jobs(self.root, self.campaign_id, jobs)

        output = status(self.root, self.campaign_id)

        self.assertEqual(output["shared_update_plan"], {
            "wiki/concepts/metronome/metronome-billing.md": [
                {
                    "job_id": "job-1", "attempt": 1, "update_id": "billing-a",
                    "update_kind": "durable_fact", "anchor": "## Sources",
                    "proposed_markdown": "- [[source-job-1]] — billing fact A",
                    "quote_indexes": [0], "warnings": [],
                },
                {
                    "job_id": "job-2", "attempt": 1, "update_id": "billing-b",
                    "update_kind": "durable_fact", "anchor": "## Sources",
                    "proposed_markdown": "- [[source-job-2]] — billing fact B",
                    "quote_indexes": [0], "warnings": [],
                },
            ],
        })
        self.assertFalse((self.root / "wiki").exists())

        review_path = self.attempt("job-1", 1).joinpath("review.json")
        review = json.loads(review_path.read_text(encoding="utf-8"))
        for field, tampered_value in (("reviewer_identity", "reviewer-b"), ("reviewer_model", "Terra")):
            review[field] = tampered_value
            review_path.write_text(json.dumps(review), encoding="utf-8")
            with self.subTest(field=field):
                with self.assertRaisesRegex(PilotError, "approved shared update evidence is invalid"):
                    status(self.root, self.campaign_id)
            review[field] = "reviewer-a" if field == "reviewer_identity" else "Sol"
        review_path.write_text(json.dumps(review), encoding="utf-8")

        suggestions_path = self.attempt("job-1", 1).joinpath("suggestions.json")
        suggestions = json.loads(suggestions_path.read_text(encoding="utf-8"))
        suggestions["concepts"][0]["quote_indexes"] = [99]
        suggestions_path.write_text(json.dumps(suggestions), encoding="utf-8")
        with self.assertRaisesRegex(PilotError, "approved shared update evidence is invalid"):
            status(self.root, self.campaign_id)
        self.assertFalse((self.root / "wiki").exists())
        suggestions["concepts"][0]["quote_indexes"] = [0]
        suggestions_path.write_text(json.dumps(suggestions), encoding="utf-8")

        jobs[0]["queue_position"] = 2
        jobs[1]["queue_position"] = 1
        save_jobs(self.root, self.campaign_id, jobs)
        self.assertEqual(
            [update["job_id"] for update in status(self.root, self.campaign_id)["shared_update_plan"]
             ["wiki/concepts/metronome/metronome-billing.md"]],
            ["job-2", "job-1"],
        )

        campaign_path = self.root / "tracking/ingest/metronome" / self.campaign_id / "campaign.json"
        campaign = json.loads(campaign_path.read_text(encoding="utf-8"))
        campaign["schema_version"] = 1
        campaign_path.write_text(json.dumps(campaign), encoding="utf-8")
        self.attempt("job-1", 1).joinpath("suggestions.json").write_text(
            json.dumps({"company": ["historical string suggestion"]}), encoding="utf-8",
        )

        self.assertEqual(status(self.root, self.campaign_id)["shared_update_plan"], {})

    def test_parallel_assignments_are_required_before_state_mutation_and_distinct(self):
        parallel = dict(self.manifest)
        parallel["review_concurrency"] = 2
        parallel["audit_job_ids"] = ["job-1", "job-2", "job-3"]
        init_campaign(self.root, parallel)
        before = load_jobs(self.root, self.campaign_id)

        with self.assertRaisesRegex(PilotError, "worker assignments"):
            run_once(self.root, self.campaign_id, total_subagent_slots=3)
        self.assertEqual(load_jobs(self.root, self.campaign_id), before)

        first = run_once(
            self.root,
            self.campaign_id,
            total_subagent_slots=3,
            worker_assignments={"job-1": {"identity": "worker-a", "model": "Terra"}, "job-2": {"identity": "worker-b", "model": "Terra"}, "job-3": {"identity": "worker-c", "model": "Terra"}},
            reviewer_assignments={},
        )
        self.assertEqual([order["job_id"] for order in first["worker_orders"]], ["job-1", "job-2", "job-3"])
        self.assertEqual(load_jobs(self.root, self.campaign_id)[0]["worker_identity"], "worker-a")

        ready = load_jobs(self.root, self.campaign_id)
        ready[0]["state"] = "candidate_ready"
        ready[1]["state"] = "candidate_ready"
        save_jobs(self.root, self.campaign_id, ready)
        before_reviews = load_jobs(self.root, self.campaign_id)
        with self.assertRaisesRegex(PilotError, "reviewer identity"):
            run_once(
                self.root,
                self.campaign_id,
                total_subagent_slots=3,
                reviewer_assignments={
                    "job-1": {"identity": "worker-a", "model": "Sol"},
                    "job-2": {"identity": "reviewer-b", "model": "Sol"},
                },
                worker_assignments={},
            )
        self.assertEqual(load_jobs(self.root, self.campaign_id), before_reviews)

    def test_serial_ready_candidate_requires_reviewer_assignment_before_worker_attempt_mutation(self):
        serial = dict(self.manifest)
        serial["worker_concurrency"] = 1
        init_campaign(self.root, serial)
        jobs = load_jobs(self.root, self.campaign_id)
        jobs[0].update({"attempt": 1, "state": "candidate_ready", "last_event": "candidate_ready"})
        save_jobs(self.root, self.campaign_id, jobs)
        attempts = self.root / "tracking/ingest/metronome" / self.campaign_id / "attempts"
        before_jobs = load_jobs(self.root, self.campaign_id)
        before_attempt_paths = sorted(path.relative_to(attempts) for path in attempts.rglob("*"))

        with self.assertRaisesRegex(PilotError, "reviewer assignments"):
            run_once(self.root, self.campaign_id)

        self.assertEqual(load_jobs(self.root, self.campaign_id), before_jobs)
        self.assertEqual(sorted(path.relative_to(attempts) for path in attempts.rglob("*")), before_attempt_paths)

        output = run_once(
            self.root,
            self.campaign_id,
            reviewer_assignments=[{"identity": "reviewer-a", "model": "Sol"}],
        )
        self.assertEqual(output["review_order"]["job_id"], "job-1")
        self.assertEqual(load_jobs(self.root, self.campaign_id)[1]["state"], "running")

    def test_parallel_review_result_without_assignment_fails_closed(self):
        parallel = dict(self.manifest)
        parallel["review_concurrency"] = 2
        parallel["audit_job_ids"] = ["job-1", "job-2", "job-3"]
        init_campaign(self.root, parallel)
        jobs = load_jobs(self.root, self.campaign_id)
        jobs[0]["attempt"] = 1
        jobs[0]["state"] = "reviewing"
        jobs[0]["last_event"] = "review_started"
        save_jobs(self.root, self.campaign_id, jobs)
        before = load_jobs(self.root, self.campaign_id)

        with self.assertRaisesRegex(PilotError, "reviewer assignment"):
            run_once(
                self.root,
                self.campaign_id,
                review_result_path=self.write_review("job-1", 1, "approved"),
                total_subagent_slots=3,
                worker_assignments={},
                reviewer_assignments={},
            )
        self.assertEqual(load_jobs(self.root, self.campaign_id), before)

    def test_parallel_worker_result_missing_reviewer_assignment_leaves_state_and_attempt_unchanged_then_retries(self):
        parallel = dict(self.manifest)
        parallel["review_concurrency"] = 2
        parallel["audit_job_ids"] = ["job-1", "job-2", "job-3"]
        init_campaign(self.root, parallel)
        run_once(
            self.root,
            self.campaign_id,
            total_subagent_slots=3,
            worker_assignments={
                "job-1": {"identity": "worker-a", "model": "Terra"},
                "job-2": {"identity": "worker-b", "model": "Terra"},
                "job-3": {"identity": "worker-c", "model": "Terra"},
            },
            reviewer_assignments={},
        )
        before_jobs = load_jobs(self.root, self.campaign_id)
        before_attempt = {
            path.name: path.read_bytes() for path in self.attempt("job-1", 1).iterdir()
        }

        with self.assertRaisesRegex(PilotError, "reviewer assignments"):
            run_once(
                self.root,
                self.campaign_id,
                worker_result_path=self.write_worker_result("job-1"),
                total_subagent_slots=3,
                worker_assignments={},
                reviewer_assignments={},
            )

        self.assertEqual(load_jobs(self.root, self.campaign_id), before_jobs)
        self.assertEqual(
            {path.name: path.read_bytes() for path in self.attempt("job-1", 1).iterdir()},
            before_attempt,
        )

        retried = run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-1"),
            total_subagent_slots=3,
            worker_assignments={},
            reviewer_assignments={"job-1": {"identity": "reviewer-a", "model": "Sol"}},
        )
        self.assertEqual(retried["review_order"]["job_id"], "job-1")
        self.assertEqual(next(job for job in load_jobs(self.root, self.campaign_id) if job["job_id"] == "job-1")["state"], "reviewing")
        self.assertTrue(self.attempt("job-1", 1).joinpath("candidate.md").is_file())

    def test_parallel_review_result_missing_worker_assignment_leaves_state_and_attempt_unchanged_then_retries(self):
        parallel = dict(self.manifest)
        parallel["review_concurrency"] = 2
        parallel["audit_job_ids"] = ["job-1", "job-2", "job-3"]
        init_campaign(self.root, parallel)
        run_once(
            self.root,
            self.campaign_id,
            total_subagent_slots=3,
            worker_assignments={
                "job-1": {"identity": "worker-a", "model": "Terra"},
                "job-2": {"identity": "worker-b", "model": "Terra"},
                "job-3": {"identity": "worker-c", "model": "Terra"},
            },
            reviewer_assignments={},
        )
        run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-1"),
            total_subagent_slots=3,
            worker_assignments={},
            reviewer_assignments={"job-1": {"identity": "reviewer-a", "model": "Sol"}},
        )
        before_jobs = load_jobs(self.root, self.campaign_id)
        before_attempt = {
            path.name: path.read_bytes() for path in self.attempt("job-1", 1).iterdir()
        }

        with self.assertRaisesRegex(PilotError, "worker assignments"):
            run_once(
                self.root,
                self.campaign_id,
                review_result_path=self.write_review("job-1", 1, "approved"),
                total_subagent_slots=3,
                worker_assignments={},
                reviewer_assignments={},
            )

        self.assertEqual(load_jobs(self.root, self.campaign_id), before_jobs)
        self.assertEqual(
            {path.name: path.read_bytes() for path in self.attempt("job-1", 1).iterdir()},
            before_attempt,
        )

        retried = run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review("job-1", 1, "approved"),
            total_subagent_slots=3,
            worker_assignments={"job-4": {"identity": "worker-d", "model": "Terra"}},
            reviewer_assignments={},
        )
        self.assertEqual(next(job for job in load_jobs(self.root, self.campaign_id) if job["job_id"] == "job-1")["state"], "approved")
        self.assertEqual([order["job_id"] for order in retried["worker_orders"]], ["job-4"])
        self.assertTrue(self.attempt("job-1", 1).joinpath("review.json").is_file())

    def test_parallel_reviews_write_immutable_provenance_for_each_verdict(self):
        self.start_five()
        for job_id, verdict, expected_state in (
            ("job-1", "approved", "approved"),
            ("job-2", "changes_requested", "queued"),
            ("job-3", "rejected", "rejected"),
        ):
            with self.subTest(verdict=verdict):
                jobs = load_jobs(self.root, self.campaign_id)
                job = next(item for item in jobs if item["job_id"] == job_id)
                job["state"] = "reviewing"
                job["last_event"] = "review_started"
                job["worker_identity"] = "worker-a"
                job["worker_model"] = "Terra"
                job["reviewer_identity"] = "reviewer-a"
                job["reviewer_model"] = "Sol"
                save_jobs(self.root, self.campaign_id, jobs)
                attempt = self.attempt(job_id, 1)
                attempt.joinpath("suggestions.json").write_text(
                    json.dumps({"company": [], "concepts": [], "index": [], "log": []}),
                    encoding="utf-8",
                )
                self.write_receipt(job, attempt, {"company": [], "concepts": [], "index": [], "log": []})

                review_kwargs = (
                    {"required_changes": ["Revise the source page"], "retry_review_scope": "full"}
                    if verdict == "changes_requested" else {}
                )
                run_once(
                    self.root, self.campaign_id,
                    review_result_path=self.write_review(job_id, 1, verdict, **review_kwargs),
                )

                review = json.loads(self.attempt(job_id, 1).joinpath("review.json").read_text(encoding="utf-8"))
                self.assertEqual(review["verdict"], verdict)
                self.assertEqual(review["reviewer_identity"], "reviewer-a")
                self.assertEqual(review["reviewer_model"], "Sol")
                self.assertEqual(next(job for job in load_jobs(self.root, self.campaign_id) if job["job_id"] == job_id)["state"], expected_state)

    def test_cli_runs_a_shared_slot_worker_review_cycle(self):
        manifest = dict(self.manifest)
        manifest["review_concurrency"] = 2
        manifest["audit_job_ids"] = ["job-1", "job-2", "job-3"]
        manifest_path = self.root / "parallel-manifest.json"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        script = Path(__file__).parents[1] / "scripts" / "manage_ingest_pilot.py"

        def invoke(*arguments):
            completed = subprocess.run(
                [sys.executable, str(script), *arguments], cwd=self.root, text=True, capture_output=True, check=True
            )
            self.assertEqual(completed.stderr, "")
            return json.loads(completed.stdout)

        invoke("init", "--manifest", str(manifest_path))
        started = invoke(
            "run", "--campaign", self.campaign_id, "--total-subagent-slots", "3",
            "--worker-assignment", "worker-a=Terra", "--worker-assignment", "worker-b=Terra",
            "--worker-assignment", "worker-c=Terra",
        )
        self.assertEqual([order["job_id"] for order in started["worker_orders"]], ["job-1", "job-2", "job-3"])
        candidate = invoke(
            "run", "--campaign", self.campaign_id, "--total-subagent-slots", "3",
            "--worker-result", str(self.write_worker_result("job-1")),
            "--reviewer-assignment", "reviewer-a=Sol",
        )
        self.assertEqual([order["job_id"] for order in candidate["review_orders"]], ["job-1"])
        reviewed = invoke(
            "run", "--campaign", self.campaign_id, "--total-subagent-slots", "3",
            "--review-result", str(self.write_review("job-1", 1, "approved")),
            "--worker-assignment", "worker-d=Terra",
        )
        self.assertEqual(reviewed["jobs"][0]["state"], "approved")
        self.assertEqual([order["job_id"] for order in reviewed["worker_orders"]], ["job-4"])

    def test_retry_and_reject_require_failed_jobs_and_retain_attempts(self):
        self.start_five()
        run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-1", raw_sha256="0" * 64),
        )
        failure = self.attempt("job-1", 1) / "failure.json"
        before_tail = max(job["queue_position"] for job in load_jobs(self.root, self.campaign_id))

        retry_job(self.root, self.campaign_id, "job-1")

        retried = load_jobs(self.root, self.campaign_id)[0]
        self.assertEqual(retried["state"], "queued")
        self.assertGreater(retried["queue_position"], before_tail)
        self.assertIsNone(retried["failure_reason"])
        self.assertTrue(failure.is_file())
        with self.assertRaises(PilotError):
            reject_job(self.root, self.campaign_id, "job-1", "operator decision")

    def test_reject_records_nonempty_reason_and_status_regenerates_monitor(self):
        self.start_five()
        run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-1", raw_sha256="0" * 64),
        )

        output = reject_job(self.root, self.campaign_id, "job-1", "operator decision")

        job = load_jobs(self.root, self.campaign_id)[0]
        self.assertEqual(job["state"], "rejected")
        self.assertEqual(job["failure_reason"], "operator decision")
        self.assertIn("- Rejected: 1", status(self.root, self.campaign_id)["monitor"])
        self.assertEqual(output["campaign_state"], "active")
        with self.assertRaises(PilotError):
            reject_job(self.root, self.campaign_id, "job-2", "")

    def test_retry_returns_warning_after_audit_append_failure(self):
        self.start_five()
        run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-1", raw_sha256="0" * 64),
        )
        events = self.root / "tracking/ingest/metronome" / self.campaign_id / "events.jsonl"
        events.unlink()
        events.mkdir()

        output = retry_job(self.root, self.campaign_id, "job-1")

        self.assertEqual(load_jobs(self.root, self.campaign_id)[0]["state"], "queued")
        self.assertIn("warnings", output)
        self.assertTrue(output["warnings"])

    def test_reject_returns_warning_after_audit_append_failure(self):
        self.start_five()
        run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-1", raw_sha256="0" * 64),
        )
        events = self.root / "tracking/ingest/metronome" / self.campaign_id / "events.jsonl"
        events.unlink()
        events.mkdir()

        output = reject_job(self.root, self.campaign_id, "job-1", "operator decision")

        self.assertEqual(load_jobs(self.root, self.campaign_id)[0]["state"], "rejected")
        self.assertIn("warnings", output)
        self.assertTrue(output["warnings"])

    def test_run_rejects_worker_and_review_results_together_without_mutation(self):
        self.start_five()
        before = load_jobs(self.root, self.campaign_id)

        with self.assertRaisesRegex(PilotError, "either a worker result or a review result"):
            run_once(
                self.root,
                self.campaign_id,
                worker_result_path=self.write_worker_result("job-1"),
                review_result_path=self.write_review("job-1", 1, "approved"),
            )

        self.assertEqual(load_jobs(self.root, self.campaign_id), before)

    def test_cli_prints_one_json_object_for_each_dry_run_command(self):
        manifest_path = self.root / "manifest.json"
        manifest_path.write_text(json.dumps(self.manifest), encoding="utf-8")
        script = Path(__file__).parents[1] / "scripts" / "manage_ingest_pilot.py"

        def invoke(*arguments):
            completed = subprocess.run(
                [sys.executable, str(script), *arguments],
                cwd=self.root,
                text=True,
                capture_output=True,
                check=True,
            )
            self.assertEqual(len(completed.stdout.splitlines()), 1)
            self.assertEqual(completed.stderr, "")
            return json.loads(completed.stdout)

        initialized = invoke("init", "--manifest", str(manifest_path))
        started = invoke("run", "--campaign", self.campaign_id, "--available-worker-slots", "3")
        worker_result = self.write_worker_result("job-1")
        reviewed = invoke(
            "run",
            "--campaign",
            self.campaign_id,
            "--worker-result",
            str(worker_result),
            "--reviewer-assignment",
            "reviewer-a=Sol",
        )
        review_result = self.write_review("job-1", 1, "approved")
        approved = invoke(
            "run",
            "--campaign",
            self.campaign_id,
            "--review-result",
            str(review_result),
        )
        monitored = invoke("status", "--campaign", self.campaign_id)
        jobs = load_jobs(self.root, self.campaign_id)
        jobs[0]["state"] = "failed"
        jobs[0]["failure_reason"] = "test failure"
        save_jobs(self.root, self.campaign_id, jobs)
        retried = invoke("retry", "--campaign", self.campaign_id, "--job", "job-1")
        jobs = load_jobs(self.root, self.campaign_id)
        jobs[0]["state"] = "failed"
        jobs[0]["failure_reason"] = "test failure"
        save_jobs(self.root, self.campaign_id, jobs)
        rejected = invoke(
            "reject",
            "--campaign",
            self.campaign_id,
            "--job",
            "job-1",
            "--reason",
            "three attempts exhausted",
        )

        self.assertEqual(initialized["campaign_id"], self.campaign_id)
        self.assertEqual(len(started["worker_orders"]), 3)
        self.assertEqual(reviewed["review_order"]["job_id"], "job-1")
        self.assertEqual(approved["jobs"][0]["state"], "approved")
        self.assertEqual(monitored["campaign_state"], "active")
        self.assertEqual(retried["jobs"][0]["state"], "queued")
        self.assertEqual(rejected["jobs"][0]["state"], "rejected")

    def test_cli_completes_terminal_campaign_with_repair_count(self):
        init_campaign(self.root, self.manifest)
        jobs = load_jobs(self.root, self.campaign_id)
        for job in jobs:
            job["state"] = "rejected"
        save_jobs(self.root, self.campaign_id, jobs)
        script = Path(__file__).parents[1] / "scripts" / "manage_ingest_pilot.py"

        completed = subprocess.run(
            [
                sys.executable,
                str(script),
                "complete",
                "--campaign",
                self.campaign_id,
                "--coordinator-repairs",
                "3",
            ],
            cwd=self.root,
            text=True,
            capture_output=True,
        )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        output = json.loads(completed.stdout)
        self.assertEqual(output["campaign_state"], "complete")
        self.assertEqual(
            json.loads(
                (self.root / "tracking/ingest/metronome" / self.campaign_id / "campaign.json").read_text(
                    encoding="utf-8"
                )
            )["coordinator_repairs"],
            3,
        )

    def test_cli_reports_handled_errors_only_to_stderr(self):
        script = Path(__file__).parents[1] / "scripts" / "manage_ingest_pilot.py"

        completed = subprocess.run(
            [sys.executable, str(script), "status", "--campaign", self.campaign_id],
            cwd=self.root,
            text=True,
            capture_output=True,
        )

        self.assertNotEqual(completed.returncode, 0)
        self.assertEqual(completed.stdout, "")
        self.assertIn("cannot read campaign.json", completed.stderr)


if __name__ == "__main__":
    unittest.main()
