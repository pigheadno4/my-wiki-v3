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
                "original_format: webpage\n"
                "raw_files:\n"
                f'  - "{job["raw_path"].removeprefix("raw/")}"\n'
                "tags: [metronome]\n"
                "---\n\n"
                "## Raw Sources\n"
                f"- [[{raw_stem}]] — verbatim documentation\n"
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
