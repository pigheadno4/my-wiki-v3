import sys
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from metronome_ingest_pilot import (  # noqa: E402
    render_luna_draft,
    render_model_draft,
    validate_final_receipt,
    validate_job,
    validate_luna_output,
    validate_model_output,
    validate_receipt,
    validate_worker_receipt,
)


class MetronomeIngestPilotTests(unittest.TestCase):
    def make_root(self) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        raw = root / "raw" / "metronome" / "guides" / "home.md"
        raw.parent.mkdir(parents=True)
        raw.write_text("alpha\nbeta\ngamma\ndelta\n", encoding="utf-8")
        return root

    def valid_job(self):
        source = "wiki/sources/metronome/source-home.md"
        concept = "wiki/concepts/metronome/metronome-usage-based-billing.md"
        return {
            "schema_version": 1,
            "job_id": "pilot-home-baseline",
            "provider": "metronome",
            "canonical_url": "https://docs.metronome.com/guides/home",
            "raw_path": "raw/metronome/guides/home.md",
            "source_page": source,
            "concept_leases": [concept],
            "role": "strong_baseline",
            "allowed_write_paths": [source, concept],
            "forbidden_write_paths": [
                "wiki/companies/metronome.md",
                "wiki/metronome-index.md",
                "wiki/metronome-log.md",
                "wiki/index.md",
                "wiki/log.md",
            ],
            "forbidden_write_prefixes": [
                "raw/",
                "wiki/comparisons/",
            ],
        }

    def valid_receipt(self, job):
        return {
            "schema_version": 1,
            "job_id": job["job_id"],
            "provider": job["provider"],
            "canonical_url": job["canonical_url"],
            "raw_path": job["raw_path"],
            "source_page": job["source_page"],
            "status": "success",
            "grounding_quotes": [
                {"line_start": 1, "line_end": 1, "text": "alpha"},
                {"line_start": 2, "line_end": 2, "text": "beta"},
                {"line_start": 3, "line_end": 4, "text": "gamma\ndelta"},
            ],
            "files_changed": list(job["allowed_write_paths"]),
            "worker_commit": "1234567abcdef",
            "validation": [
                {"command": "python3 scripts/validate_wiki.py source.md", "passed": True}
            ],
            "worker": {
                "role": job["role"],
                "model_provider": "openai",
                "model": "gpt-5",
                "token_usage": None,
                "token_usage_unavailable_reason": "runtime does not expose per-job usage",
            },
            "review": {
                "status": "approved",
                "reviewer": "coordinator",
                "notes": "Claims and quotes checked against raw lines.",
            },
        }

    def valid_luna_job(self):
        run_dir = "tracking/ingest/metronome/pilot/runs/pilot-invoices-overview-luna"
        return {
            "schema_version": 2,
            "job_id": "pilot-invoices-overview-luna",
            "provider": "metronome",
            "mode": "real_ingest",
            "canonical_url": "https://docs.metronome.com/guides/invoices/overview",
            "raw_path": "raw/metronome/guides/home.md",
            "source_page": "wiki/sources/metronome/source-metronome-guides-invoices-overview.md",
            "artifact_dir": run_dir,
            "role": "cheap_ingester",
            "model_provider": "openai",
            "model": "gpt-5.6-luna",
            "reasoning_effort": "high",
            "allowed_write_paths": [run_dir],
            "forbidden_write_paths": [
                "wiki/companies/metronome.md",
                "wiki/metronome-index.md",
                "wiki/metronome-log.md",
                "wiki/index.md",
                "wiki/log.md",
            ],
            "forbidden_write_prefixes": ["raw/", "wiki/"],
        }

    def valid_luna_output(self, job):
        return {
            "job_id": job["job_id"],
            "raw_path": job["raw_path"],
            "canonical_url": job["canonical_url"],
            "title": "Metronome Invoicing Overview",
            "grounding_quotes": [
                {
                    "line_start": 1,
                    "line_end": 1,
                    "text": "alpha",
                    "supports": "first claim",
                },
                {
                    "line_start": 2,
                    "line_end": 2,
                    "text": "beta",
                    "supports": "second claim",
                },
                {
                    "line_start": 3,
                    "line_end": 4,
                    "text": "gamma\ndelta",
                    "supports": "third claim",
                },
            ],
            "overview": "A grounded overview.",
            "key_takeaways": ["A grounded takeaway."],
            "details": [{"heading": "Scope", "facts": ["A grounded fact."]}],
            "suggested_tags": ["metronome", "invoicing"],
            "suggested_metronome_concepts": ["metronome-invoicing"],
            "proposed_raw_link": "[[raw/metronome/guides/home|collection snapshot]]",
            "unsupported_claim_self_check": [],
        }

    def valid_model_job(self, model="gpt-5.6-terra", reasoning="medium"):
        job_id = "terra-design-usage-events"
        run_dir = f"tracking/ingest/metronome/pilot/runs/{job_id}"
        return {
            "schema_version": 3,
            "job_id": job_id,
            "provider": "metronome",
            "mode": "real_ingest",
            "canonical_url": "https://docs.metronome.com/guides/events/design-usage-events",
            "raw_path": "raw/metronome/guides/home.md",
            "source_page": "wiki/sources/metronome/source-design-usage-events.md",
            "artifact_dir": run_dir,
            "role": "cheap_ingester",
            "model_provider": "openai",
            "model": model,
            "reasoning_effort": reasoning,
            "allowed_write_paths": [run_dir],
            "forbidden_write_paths": ["wiki/metronome-index.md"],
            "forbidden_write_prefixes": ["raw/", "wiki/"],
        }

    def valid_model_output(self, job):
        return {
            "job_id": job["job_id"],
            "raw_path": job["raw_path"],
            "canonical_url": job["canonical_url"],
            "title": "Design usage events",
            "grounding_quotes": [
                {"id": "q1", "line_start": 1, "line_end": 1, "text": "alpha", "supports": "overview"},
                {"id": "q2", "line_start": 2, "line_end": 2, "text": "beta", "supports": "takeaway"},
                {"id": "q3", "line_start": 3, "line_end": 4, "text": "gamma\ndelta", "supports": "detail"},
            ],
            "overview": "A grounded overview.",
            "overview_evidence_quote_ids": ["q1"],
            "key_takeaways": [{"text": "A grounded takeaway.", "evidence_quote_ids": ["q2"]}],
            "details": [{"heading": "Scope", "facts": [{"text": "A grounded fact.", "evidence_quote_ids": ["q3"]}]}],
            "sections_covered": ["alpha", "beta", "gamma"],
            "scope_boundaries": [{"text": "Only the assigned page is covered.", "evidence_quote_ids": ["q1"]}],
            "conditional_requirements": [],
            "feature_gates": [],
            "internal_inconsistencies": [],
            "material_omissions": [],
            "suggested_tags": ["metronome", "events"],
            "suggested_metronome_concepts": ["metronome-event-ingestion"],
            "proposed_raw_link": "[[raw/metronome/guides/home|collection snapshot]]",
            "unsupported_claim_self_check": [],
        }

    def valid_worker_receipt(self, job):
        artifact_dir = job["artifact_dir"]
        return {
            "schema_version": 2,
            "job_id": job["job_id"],
            "provider": "metronome",
            "canonical_url": job["canonical_url"],
            "raw_path": job["raw_path"],
            "source_page": job["source_page"],
            "status": "success",
            "model_provider": "openai",
            "model": "gpt-5.6-luna",
            "reasoning_effort": "high",
            "attempt_count": 1,
            "started_at": "2026-07-14T00:00:00Z",
            "finished_at": "2026-07-14T00:00:02Z",
            "elapsed_seconds": 2.0,
            "process_exit_code": 0,
            "output_path": f"{artifact_dir}/luna-output.json",
            "draft_path": f"{artifact_dir}/luna-source-draft.md",
            "events_path": f"{artifact_dir}/attempt-1/events.jsonl",
            "stderr_path": f"{artifact_dir}/attempt-1/stderr.log",
            "grounding_quotes": self.valid_luna_output(job)["grounding_quotes"],
            "validation": [{"command": "validate_luna_output", "passed": True}],
            "token_usage": None,
            "token_usage_unavailable_reason": "Codex event stream omitted usage.",
        }

    def valid_model_worker_receipt(self, job):
        artifact_dir = job["artifact_dir"]
        quotes = self.valid_model_output(job)["grounding_quotes"]
        usage = {"input_tokens": 100, "output_tokens": 20}
        return {
            "schema_version": 3,
            "job_id": job["job_id"],
            "provider": "metronome",
            "canonical_url": job["canonical_url"],
            "raw_path": job["raw_path"],
            "source_page": job["source_page"],
            "status": "success",
            "model_provider": "openai",
            "model": job["model"],
            "reasoning_effort": job["reasoning_effort"],
            "attempt_count": 1,
            "attempts": [{
                "attempt": 1,
                "status": "accepted",
                "process_exit_code": 0,
                "validation_errors": [],
                "retry_reason": None,
                "output_path": f"{artifact_dir}/attempt-1/output.json",
                "events_path": f"{artifact_dir}/attempt-1/events.jsonl",
                "stderr_path": f"{artifact_dir}/attempt-1/stderr.log",
                "token_usage": usage,
            }],
            "started_at": "2026-07-14T00:00:00Z",
            "finished_at": "2026-07-14T00:00:02Z",
            "elapsed_seconds": 2.0,
            "process_exit_code": 0,
            "output_path": f"{artifact_dir}/model-output.json",
            "draft_path": f"{artifact_dir}/model-source-draft.md",
            "events_path": f"{artifact_dir}/attempt-1/events.jsonl",
            "stderr_path": f"{artifact_dir}/attempt-1/stderr.log",
            "grounding_quotes": quotes,
            "validation": [{"command": "validate_model_output", "passed": True}],
            "token_usage": usage,
            "cumulative_token_usage": usage,
            "token_usage_unavailable_reason": None,
        }

    def valid_final_receipt(self, job):
        artifact_dir = job["artifact_dir"]
        return {
            "schema_version": 2,
            "job_id": job["job_id"],
            "provider": "metronome",
            "canonical_url": job["canonical_url"],
            "raw_path": job["raw_path"],
            "source_page": job["source_page"],
            "mode": job["mode"],
            "worker_receipt": f"{artifact_dir}/luna-worker-receipt.json",
            "luna_draft": f"{artifact_dir}/luna-source-draft.md",
            "final_status": "approved",
            "repairs": [],
            "coordinator_repair_minutes": 0,
            "concepts_updated": ["wiki/concepts/metronome/metronome-invoicing.md"],
            "contradictions": [],
            "shared_files_updated": ["wiki/metronome-index.md"],
            "validation": [{"command": "python3 scripts/validate_wiki.py", "passed": True}],
            "review": {
                "reviewer": "sol-coordinator",
                "model": "gpt-5.6-sol",
                "status": "approved",
                "notes": "Compared every claim with the complete raw page.",
            },
        }

    def test_valid_job_has_existing_raw_and_disjoint_write_sets(self):
        root = self.make_root()

        self.assertEqual([], validate_job(root, self.valid_job()))

    def test_job_rejects_missing_raw_and_overlapping_forbidden_path(self):
        root = self.make_root()
        job = self.valid_job()
        job["raw_path"] = "raw/metronome/guides/missing.md"
        job["forbidden_write_paths"].append(job["source_page"])

        errors = validate_job(root, job)

        self.assertTrue(any("raw_path does not exist" in error for error in errors))
        self.assertTrue(any("allowed and forbidden write paths overlap" in error for error in errors))

    def test_receipt_identity_must_match_job(self):
        root = self.make_root()
        job = self.valid_job()
        receipt = self.valid_receipt(job)
        receipt["canonical_url"] = "https://docs.metronome.com/wrong"

        errors = validate_receipt(root, job, receipt)

        self.assertTrue(any("canonical_url does not match job" in error for error in errors))

    def test_receipt_rejects_files_outside_allowed_write_set(self):
        root = self.make_root()
        job = self.valid_job()
        receipt = self.valid_receipt(job)
        receipt["files_changed"].append("wiki/metronome-index.md")

        errors = validate_receipt(root, job, receipt)

        self.assertTrue(any("outside allowed_write_paths" in error for error in errors))

    def test_grounding_quote_must_match_exact_raw_lines(self):
        root = self.make_root()
        job = self.valid_job()
        receipt = self.valid_receipt(job)
        receipt["grounding_quotes"][0]["text"] = "not alpha"

        errors = validate_receipt(root, job, receipt)

        self.assertTrue(any("does not match raw lines 1-1" in error for error in errors))

    def test_success_receipt_requires_commit_validation_model_and_review(self):
        root = self.make_root()
        job = self.valid_job()
        receipt = self.valid_receipt(job)
        receipt["worker_commit"] = ""
        receipt["validation"][0]["passed"] = False
        receipt["worker"]["model"] = ""
        receipt["review"]["status"] = "pending"

        errors = validate_receipt(root, job, receipt)

        self.assertTrue(any("worker_commit" in error for error in errors))
        self.assertTrue(any("validation command did not pass" in error for error in errors))
        self.assertTrue(any("model is required" in error for error in errors))
        self.assertTrue(any("review status must be approved" in error for error in errors))

    def test_null_token_usage_requires_reason(self):
        root = self.make_root()
        job = self.valid_job()
        receipt = deepcopy(self.valid_receipt(job))
        receipt["worker"].pop("token_usage_unavailable_reason")

        errors = validate_receipt(root, job, receipt)

        self.assertTrue(any("token_usage_unavailable_reason" in error for error in errors))

    def test_valid_luna_job_limits_worker_to_its_artifact_directory(self):
        root = self.make_root()

        self.assertEqual([], validate_job(root, self.valid_luna_job()))

    def test_model_job_accepts_only_terra_medium_or_luna_high(self):
        root = self.make_root()

        self.assertEqual([], validate_job(root, self.valid_model_job()))
        self.assertEqual([], validate_job(root, self.valid_model_job("gpt-5.6-luna", "high")))

        wrong = self.valid_model_job("gpt-5.6-terra", "high")
        self.assertTrue(any("model/reasoning pair" in error for error in validate_job(root, wrong)))

    def test_model_output_requires_claim_level_evidence_and_coverage_fields(self):
        root = self.make_root()
        job = self.valid_model_job()
        output = self.valid_model_output(job)

        self.assertEqual([], validate_model_output(root, job, output))

        output["details"][0]["facts"][0]["evidence_quote_ids"] = ["missing"]
        errors = validate_model_output(root, job, output)
        self.assertTrue(any("undefined grounding quote" in error for error in errors))

    def test_render_model_draft_preserves_evidence_and_raw_link(self):
        job = self.valid_model_job()
        rendered = render_model_draft(job, self.valid_model_output(job), "2026-07-14")

        self.assertIn("A grounded takeaway. [q2]", rendered)
        self.assertIn("A grounded fact. [q3]", rendered)
        self.assertIn("[[raw/metronome/guides/home|collection snapshot]]", rendered)

    def test_luna_job_rejects_wiki_write_access_and_wrong_model(self):
        root = self.make_root()
        job = self.valid_luna_job()
        job["allowed_write_paths"].append(job["source_page"])
        job["model"] = "gpt-5.6-sol"

        errors = validate_job(root, job)

        self.assertTrue(any("allowed_write_paths" in error for error in errors))
        self.assertTrue(any("model must be gpt-5.6-luna" in error for error in errors))

    def test_valid_luna_output_checks_identity_quotes_tags_concepts_and_raw_link(self):
        root = self.make_root()
        job = self.valid_luna_job()

        self.assertEqual([], validate_luna_output(root, job, self.valid_luna_output(job)))

    def test_luna_output_rejects_unsupported_claims_and_wrong_raw_link(self):
        root = self.make_root()
        job = self.valid_luna_job()
        output = self.valid_luna_output(job)
        output["unsupported_claim_self_check"] = ["outside claim"]
        output["proposed_raw_link"] = "[[raw/metronome/other|snapshot]]"

        errors = validate_luna_output(root, job, output)

        self.assertTrue(any("unsupported_claim_self_check" in error for error in errors))
        self.assertTrue(any("proposed_raw_link" in error for error in errors))

    def test_render_luna_draft_uses_stable_template_and_relative_raw_file(self):
        job = self.valid_luna_job()
        rendered = render_luna_draft(job, self.valid_luna_output(job), "2026-07-14")

        self.assertIn('title: "Metronome Invoicing Overview"', rendered)
        self.assertIn('  - "metronome/guides/home.md"', rendered)
        self.assertIn("## Key takeaways", rendered)
        self.assertIn("### Scope", rendered)
        self.assertIn("[[raw/metronome/guides/home|collection snapshot]]", rendered)

    def test_worker_receipt_requires_luna_runtime_and_artifact_paths(self):
        root = self.make_root()
        job = self.valid_luna_job()
        receipt = self.valid_worker_receipt(job)

        self.assertEqual([], validate_worker_receipt(root, job, receipt))

        receipt["model"] = "gpt-5.6-sol"
        receipt["output_path"] = "wiki/source.md"
        errors = validate_worker_receipt(root, job, receipt)
        self.assertTrue(any("model must be gpt-5.6-luna" in error for error in errors))
        self.assertTrue(any("output_path must stay inside artifact_dir" in error for error in errors))

    def test_model_worker_receipt_matches_job_and_accounts_for_attempts(self):
        root = self.make_root()
        job = self.valid_model_job()
        receipt = self.valid_model_worker_receipt(job)

        self.assertEqual([], validate_worker_receipt(root, job, receipt))

        receipt["model"] = "gpt-5.6-luna"
        receipt["attempts"] = []
        errors = validate_worker_receipt(root, job, receipt)
        self.assertTrue(any("model does not match job" in error for error in errors))
        self.assertTrue(any("attempts must match attempt_count" in error for error in errors))

    def test_failed_worker_receipt_may_preserve_no_valid_quotes(self):
        root = self.make_root()
        job = self.valid_luna_job()
        receipt = self.valid_worker_receipt(job)
        receipt["status"] = "failed"
        receipt["attempt_count"] = 2
        receipt["grounding_quotes"] = []
        receipt["draft_path"] = None
        receipt["validation"] = [
            {"command": "validate_luna_output", "passed": False, "errors": ["invalid JSON"]}
        ]

        self.assertEqual([], validate_worker_receipt(root, job, receipt))

    def test_final_receipt_requires_sol_review_and_passing_validation(self):
        root = self.make_root()
        job = self.valid_luna_job()
        receipt = self.valid_final_receipt(job)

        self.assertEqual([], validate_final_receipt(root, job, receipt))

        receipt["review"]["model"] = "gpt-5.6-luna"
        receipt["validation"][0]["passed"] = False
        errors = validate_final_receipt(root, job, receipt)
        self.assertTrue(any("review model must be gpt-5.6-sol" in error for error in errors))
        self.assertTrue(any("validation command did not pass" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
