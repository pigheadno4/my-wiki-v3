import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.ingest_pilot.coordinator import (
    PilotError,
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
        }
        result.update(overrides)
        path = self.root / f"{job_id}-review-result.json"
        path.write_text(json.dumps(result), encoding="utf-8")
        return path

    def make_reviewing(self, job_id, attempt):
        init_campaign(self.root, self.manifest)
        jobs = load_jobs(self.root, self.campaign_id)
        job = next(job for job in jobs if job["job_id"] == job_id)
        job["attempt"] = attempt
        job["state"] = "reviewing"
        job["last_event"] = "review_started"
        save_jobs(self.root, self.campaign_id, jobs)

    def test_valid_worker_result_persists_candidate_and_emits_review_order(self):
        self.start_five()

        output = run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-1"),
        )

        job = load_jobs(self.root, self.campaign_id)[0]
        self.assertEqual(job["state"], "reviewing")
        attempt = self.attempt("job-1", 1)
        self.assertTrue(attempt.joinpath("candidate.md").is_file())
        self.assertTrue(attempt.joinpath("receipt.json").is_file())
        self.assertTrue(attempt.joinpath("suggestions.json").is_file())
        self.assertEqual(output["review_order"]["job_id"], "job-1")

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

    def test_changes_requested_queues_fresh_attempt_at_tail(self):
        self.make_reviewing("job-1", attempt=1)
        initial_tail = max(job["queue_position"] for job in load_jobs(self.root, self.campaign_id))

        run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review("job-1", 1, "changes_requested"),
        )

        job = load_jobs(self.root, self.campaign_id)[0]
        self.assertEqual(job["state"], "queued")
        self.assertGreater(job["queue_position"], initial_tail)
        self.assertEqual(job["attempt"], 1)
        self.assertFalse(self.attempt("job-1", 2).exists())

    def test_third_changes_request_rejects_job(self):
        self.make_reviewing("job-1", attempt=3)

        run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review("job-1", 3, "changes_requested"),
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

                run_once(self.root, self.campaign_id, review_result_path=self.write_review(job_id, 1, verdict))

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
