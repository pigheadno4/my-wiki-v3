import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.ingest_pilot import (
    campaign_paths,
    init_campaign,
    load_jobs,
    recover_interrupted,
    retry_job,
    run_once,
)


METRONOME_CASES = (
    (
        "security-principles",
        "raw/metronome/guides/platform-configuration/security-principles-2026-07-13.md",
        "wiki/sources/metronome/source-metronome-guides-platform-configuration-security-principles.md",
        "https://docs.metronome.com/guides/platform-configuration/security-principles.md",
    ),
    (
        "design-usage-events",
        "raw/metronome/guides/events/design-usage-events-2026-07-13.md",
        "wiki/sources/metronome/source-metronome-guides-events-design-usage-events.md",
        "https://docs.metronome.com/guides/events/design-usage-events.md",
    ),
    (
        "setup-webhooks",
        "raw/metronome/guides/platform-configuration/setup-webhooks-2026-07-13.md",
        "wiki/sources/metronome/source-metronome-guides-platform-configuration-setup-webhooks.md",
        "https://docs.metronome.com/guides/platform-configuration/setup-webhooks.md",
    ),
    (
        "preview-events",
        "raw/metronome/api-reference/invoices/preview-events-2026-07-13.md",
        "wiki/sources/metronome/source-metronome-api-reference-invoices-preview-events.md",
        "https://docs.metronome.com/api-reference/invoices/preview-events.md",
    ),
    (
        "get-contract-edit-history",
        "raw/metronome/api-reference/contracts/get-contract-edit-history-2026-07-13.md",
        "wiki/sources/metronome/source-metronome-api-reference-contracts-get-contract-edit-history.md",
        "https://docs.metronome.com/api-reference/contracts/get-contract-edit-history.md",
    ),
)

METRONOME_HASHES = (
    "07c9a57f56b4c56ed3c219b5d87aa3994d4f02da10f3ef5109bf94ea3a2eb276",
    "ae48bff62df062d45d423bc66fbeabc2a08951782a435e9fd48047cd82813d3c",
    "be2dac89292c31ac5f489809e5f4b483f2e1633b82799ccff45d6c20e44ad73a",
    "022e7c970bf8eb8dbe80c6f15d6f4be8cbdcaab9733dc51718958edf407d34b6",
    "73072ca968bca78aa30ebcb896a1738061c3a3f90caabfa782af58ef60438c81",
)


class MinimumMetronomeManifestTests(unittest.TestCase):
    def test_manifest_keeps_the_five_immutable_sources_pending(self):
        root = Path(__file__).parents[1]
        manifest_path = root / "tracking/ingest/metronome/metronome-minimum-pilot-01/manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        line_counts = []
        expected_jobs = []

        for (job_id, raw_path, source_target, canonical_url), raw_sha256 in zip(
            METRONOME_CASES, METRONOME_HASHES
        ):
            raw_file = root / raw_path
            self.assertTrue(raw_file.is_file())
            self.assertFalse(raw_file.is_symlink())
            self.assertFalse((root / source_target).exists())
            self.assertEqual(
                raw_file.read_text(encoding="utf-8").splitlines()[0],
                f"<!-- Source URL: {canonical_url} -->",
            )
            self.assertEqual(hashlib.sha256(raw_file.read_bytes()).hexdigest(), raw_sha256)
            line_counts.append(len(raw_file.read_text(encoding="utf-8").splitlines()))
            expected_jobs.append(
                {
                    "job_id": job_id,
                    "raw_path": raw_path,
                    "raw_sha256": raw_sha256,
                    "source_target": source_target,
                    "canonical_url": canonical_url,
                }
            )

        self.assertEqual(line_counts, [29, 88, 870, 1020, 2672])
        self.assertEqual(
            manifest,
            {
                "schema_version": 1,
                "campaign_id": "metronome-minimum-pilot-01",
                "provider": "metronome",
                "mode": "dry_run",
                "worker_concurrency": 5,
                "review_concurrency": 1,
                "max_attempts": 3,
                "jobs": expected_jobs,
            },
        )


class TenJobRollingCampaignTests(unittest.TestCase):
    def setUp(self):
        temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(temporary_directory.cleanup)
        self.root = Path(temporary_directory.name)
        self.campaign_id = "ten-job-rolling-campaign"
        self.raw_files = {}
        self.manifest = {
            "schema_version": 1,
            "campaign_id": self.campaign_id,
            "provider": "metronome",
            "mode": "dry_run",
            "worker_concurrency": 5,
            "review_concurrency": 1,
            "max_attempts": 3,
            "jobs": [],
        }
        for number in range(1, 11):
            job_id = f"job-{number}"
            raw_path = f"raw/metronome/fake/{job_id}.md"
            raw_file = self.root / raw_path
            raw_file.parent.mkdir(parents=True, exist_ok=True)
            raw_file.write_text(
                f"# Fake {job_id}\n\n"
                "Quote one: immutable raw input.\n"
                "Quote two: serial review only.\n"
                "Quote three: candidates stay in tracking.\n",
                encoding="utf-8",
            )
            self.raw_files[job_id] = raw_file
            self.manifest["jobs"].append(
                {
                    "job_id": job_id,
                    "raw_path": raw_path,
                    "raw_sha256": hashlib.sha256(raw_file.read_bytes()).hexdigest(),
                    "source_target": f"wiki/sources/metronome/source-{job_id}.md",
                    "canonical_url": f"https://example.test/metronome/{job_id}",
                }
            )
        self.raw_before = {job_id: raw_file.read_bytes() for job_id, raw_file in self.raw_files.items()}

    def job(self, job_id):
        return next(job for job in load_jobs(self.root, self.campaign_id) if job["job_id"] == job_id)

    def write_worker_result(self, job_id, *, invalid=False):
        job = self.job(job_id)
        raw_stem = Path(job["raw_path"]).stem
        result = {
            "job_id": job_id,
            "attempt": job["attempt"],
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
                f"- [[{raw_stem}]] — fake immutable raw input\n"
            ),
            "quotes": [
                {"text": "Quote one: immutable raw input.", "location": "body"},
                {"text": "Quote two: serial review only.", "location": "body"},
                {"text": "Quote three: candidates stay in tracking.", "location": "body"},
            ],
            "suggestions": {"company": [], "concepts": [], "index": [], "log": []},
            "raw_path": job["raw_path"],
            "raw_sha256": "0" * 64 if invalid else job["raw_sha256"],
            "status": "candidate_ready",
        }
        result_path = self.root / f"{job_id}-attempt-{job['attempt']}-worker-result.json"
        result_path.write_text(json.dumps(result), encoding="utf-8")
        return result_path

    def write_review_result(self, job_id, verdict):
        job = self.job(job_id)
        result_path = self.root / f"{job_id}-attempt-{job['attempt']}-review-result.json"
        result_path.write_text(
            json.dumps(
                {
                    "job_id": job_id,
                    "attempt": job["attempt"],
                    "verdict": verdict,
                    "reason": "fake review result",
                    "required_changes": [],
                }
            ),
            encoding="utf-8",
        )
        return result_path

    def running_count(self):
        return sum(job["state"] == "running" for job in load_jobs(self.root, self.campaign_id))

    def test_ten_jobs_refill_review_retry_restart_and_preserve_dry_run_boundaries(self):
        initialized = init_campaign(self.root, self.manifest)
        self.assertEqual(len(initialized["jobs"]), 10)
        self.assertEqual([job["state"] for job in initialized["jobs"]], ["queued"] * 10)

        first = run_once(self.root, self.campaign_id, available_worker_slots=5)
        self.assertEqual([order["job_id"] for order in first["worker_orders"]], [f"job-{n}" for n in range(1, 6)])
        self.assertEqual(self.running_count(), 5)

        invalid = run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-1", invalid=True),
            available_worker_slots=5,
        )
        self.assertEqual([order["job_id"] for order in invalid["worker_orders"]], ["job-6"])
        self.assertEqual(self.job("job-1")["state"], "failed")
        self.assertEqual(self.running_count(), 5)

        for number, expected_refill in zip(range(2, 6), range(7, 11)):
            output = run_once(
                self.root,
                self.campaign_id,
                worker_result_path=self.write_worker_result(f"job-{number}"),
                available_worker_slots=5,
            )
            self.assertEqual([order["job_id"] for order in output["worker_orders"]], [f"job-{expected_refill}"])
            self.assertLessEqual(self.running_count(), 5)
            if number == 2:
                self.assertEqual(output["review_order"]["job_id"], "job-2")
            else:
                self.assertIsNone(output["review_order"])

        retry_job(self.root, self.campaign_id, "job-1")
        self.assertEqual(self.job("job-1")["state"], "queued")
        self.assertGreater(
            self.job("job-1")["queue_position"],
            max(self.job(f"job-{number}")["queue_position"] for number in range(7, 11)),
        )

        changes = run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review_result("job-2", "changes_requested"),
            available_worker_slots=5,
        )
        self.assertEqual(changes["worker_orders"], [])
        self.assertEqual(changes["review_order"]["job_id"], "job-3")
        self.assertEqual(self.job("job-2")["state"], "queued")
        self.assertGreater(
            self.job("job-2")["queue_position"],
            max(
                job["queue_position"]
                for job in load_jobs(self.root, self.campaign_id)
                if job["job_id"] != "job-2"
            ),
        )

        attempts = campaign_paths(self.root, self.campaign_id)["attempts"]
        candidate = attempts / "job-3/attempt-1/candidate.md"
        interrupted_inputs = {
            job_id: (attempts / f"{job_id}/attempt-1/input.json").read_bytes()
            for job_id in ("job-3", "job-6", "job-7", "job-8", "job-9", "job-10")
        }
        self.assertTrue(candidate.is_file())
        recover_interrupted(self.root, self.campaign_id)
        self.assertEqual(
            [self.job(job_id)["state"] for job_id in interrupted_inputs],
            ["failed"] * len(interrupted_inputs),
        )
        self.assertTrue(candidate.is_file())
        self.assertEqual(
            {
                job_id: (attempts / f"{job_id}/attempt-1/input.json").read_bytes()
                for job_id in interrupted_inputs
            },
            interrupted_inputs,
        )

        resumed = run_once(self.root, self.campaign_id, available_worker_slots=5)
        self.assertEqual([order["job_id"] for order in resumed["worker_orders"]], ["job-1", "job-2"])
        self.assertEqual(resumed["review_order"]["job_id"], "job-4")
        next_review = run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review_result("job-4", "approved"),
            available_worker_slots=5,
        )
        self.assertEqual(next_review["review_order"]["job_id"], "job-5")
        no_review = run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review_result("job-5", "approved"),
            available_worker_slots=5,
        )
        self.assertIsNone(no_review["review_order"])

        second_attempt = run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-2"),
            available_worker_slots=5,
        )
        self.assertEqual(self.job("job-2")["attempt"], 2)
        self.assertEqual(second_attempt["review_order"]["job_id"], "job-2")
        run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review_result("job-2", "changes_requested"),
            available_worker_slots=5,
        )

        third_attempt = run_once(self.root, self.campaign_id, available_worker_slots=5)
        self.assertEqual([order["job_id"] for order in third_attempt["worker_orders"]], ["job-2"])
        third_review = run_once(
            self.root,
            self.campaign_id,
            worker_result_path=self.write_worker_result("job-2"),
            available_worker_slots=5,
        )
        self.assertEqual(third_review["review_order"]["job_id"], "job-2")
        run_once(
            self.root,
            self.campaign_id,
            review_result_path=self.write_review_result("job-2", "changes_requested"),
            available_worker_slots=5,
        )
        self.assertEqual(self.job("job-2")["state"], "rejected")
        self.assertEqual(self.job("job-2")["attempt"], 3)

        for job_id, raw_file in self.raw_files.items():
            self.assertEqual(raw_file.read_bytes(), self.raw_before[job_id])
        self.assertFalse((self.root / "wiki").exists())
        self.assertTrue((campaign_paths(self.root, self.campaign_id)["attempts"] / "job-2/attempt-2/candidate.md").is_file())
        self.assertTrue((campaign_paths(self.root, self.campaign_id)["attempts"] / "job-2/attempt-3/candidate.md").is_file())


if __name__ == "__main__":
    unittest.main()
