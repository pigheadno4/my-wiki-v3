import hashlib
import json
import os
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
        concepts = root / "wiki" / "concepts" / "metronome"
        concepts.mkdir(parents=True)
        (concepts / "metronome-event-ingestion.md").write_text("---\n", encoding="utf-8")
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

    def materialize_diagnostic_receipt(self, root, job, receipt, run_id="terra-20260717"):
        """Add the immutable artifacts and accounting a diagnostic receipt must prove."""
        run_dir = root / job["artifact_dir"] / run_id
        attempt_dir = run_dir / "attempt-1"
        attempt_dir.mkdir(parents=True)
        events = b'{"type":"thread.started"}\n'
        stderr = b"warning"
        progress = "\n".join(
            json.dumps({"timestamp": "2026-07-14T00:00:00Z", "event": event})
            for event in (
                "lock_acquired",
                "process_started",
                "validation_completed",
                "receipt_published",
            )
        ) + "\n"
        (attempt_dir / "events.jsonl").write_bytes(events)
        (attempt_dir / "stderr.log").write_bytes(stderr)
        (attempt_dir / "progress.jsonl").write_text(progress, encoding="utf-8")
        (attempt_dir / "model-output.raw.json").write_text("{}\n", encoding="utf-8")
        (attempt_dir / "model-output.normalized.json").write_text("{}\n", encoding="utf-8")
        (run_dir / "model-output.normalized.json").write_text("{}\n", encoding="utf-8")
        (run_dir / "model-source-draft.md").write_text("draft\n", encoding="utf-8")

        run_path = f"{job['artifact_dir']}/{run_id}"
        runtime_metadata = {
            "sha256": {
                "raw_text": hashlib.sha256(
                    (root / job["raw_path"]).read_bytes()
                ).hexdigest(),
                "prompt_template": "a" * 64,
                "rendered_prompt": "b" * 64,
                "output_schema": "c" * 64,
                "codex_executable": "d" * 64,
            },
            "codex_executable": "/usr/local/bin/codex",
            "codex_cli_version": "codex 1.0.0",
            "timeout_seconds": 900,
        }
        accounting = {
            "attempt_started_at": "2026-07-14T00:00:00Z",
            "attempt_finished_at": "2026-07-14T00:00:01Z",
            "attempt_elapsed_seconds": 1.0,
            "time_to_first_stdout_event_seconds": 0.0,
            "time_to_first_stderr_byte_seconds": 0.0,
            "streamed_stdout_bytes": len(events),
            "streamed_stderr_bytes": len(stderr),
            "parsed_event_count": 1,
            "truncated_line_count": 0,
        }
        receipt.update(
            {
                "run_id": run_id,
                "input_mode": "staged-file",
                "output_path": f"{run_path}/model-output.normalized.json",
                "normalized_output_path": f"{run_path}/model-output.normalized.json",
                "draft_path": f"{run_path}/model-source-draft.md",
                "events_path": f"{run_path}/attempt-1/events.jsonl",
                "stderr_path": f"{run_path}/attempt-1/stderr.log",
                "progress_path": f"{run_path}/attempt-1/progress.jsonl",
                "runtime_metadata": runtime_metadata,
                "termination": None,
                **accounting,
            }
        )
        receipt["attempts"][0].update(
            {
                "input_mode": "staged-file",
                "output_path": f"{run_path}/attempt-1/model-output.raw.json",
                "normalized_output_path": f"{run_path}/attempt-1/model-output.normalized.json",
                "events_path": f"{run_path}/attempt-1/events.jsonl",
                "stderr_path": f"{run_path}/attempt-1/stderr.log",
                "progress_path": f"{run_path}/attempt-1/progress.jsonl",
                "runtime_metadata": runtime_metadata,
                "termination": None,
                **accounting,
            }
        )
        return run_dir

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

    def test_model_job_rejects_unsafe_job_id_and_raw_path_traversal(self):
        root = self.make_root()
        job = self.valid_model_job()
        job["job_id"] = "../outside"
        job["raw_path"] = "raw/metronome/../outside.md"

        errors = validate_job(root, job)

        self.assertTrue(any("job_id must use lowercase kebab-case" in error for error in errors))
        self.assertTrue(any("raw_path must not contain traversal" in error for error in errors))

    def test_model_job_rejects_nonstring_job_id_and_raw_path(self):
        root = self.make_root()
        job = self.valid_model_job()
        job["job_id"] = 7
        job["raw_path"] = 7

        errors = validate_job(root, job)

        self.assertTrue(any("job_id must use lowercase kebab-case" in error for error in errors))
        self.assertTrue(any("raw_path must be a safe repository-relative path" in error for error in errors))

    def test_model_job_rejects_raw_and_run_root_symlink_escapes(self):
        root = self.make_root()
        job = self.valid_model_job()
        outside = root / "outside"
        outside.mkdir()
        escaped_raw = outside / "escaped.md"
        escaped_raw.write_text("outside\n", encoding="utf-8")
        (root / "raw" / "metronome" / "escape.md").symlink_to(escaped_raw)
        job["raw_path"] = "raw/metronome/escape.md"

        raw_errors = validate_job(root, job)

        self.assertTrue(
            any("raw_path resolves outside raw/metronome" in error for error in raw_errors)
        )

        job = self.valid_model_job()
        run_root = root / "tracking" / "ingest" / "metronome" / "pilot" / "runs"
        run_root.parent.mkdir(parents=True)
        run_root.symlink_to(outside, target_is_directory=True)

        artifact_errors = validate_job(root, job)

        self.assertTrue(
            any("artifact_dir resolves outside the model run root" in error for error in artifact_errors)
        )

    def test_model_output_requires_claim_level_evidence_and_coverage_fields(self):
        root = self.make_root()
        job = self.valid_model_job()
        output = self.valid_model_output(job)

        self.assertEqual([], validate_model_output(root, job, output))

        output["details"][0]["facts"][0]["evidence_quote_ids"] = ["missing"]
        errors = validate_model_output(root, job, output)
        self.assertTrue(any("undefined grounding quote" in error for error in errors))

    def test_model_output_rejects_noncanonical_tags(self):
        root = self.make_root()
        job = self.valid_model_job()
        output = self.valid_model_output(job)
        output["suggested_tags"] = ["metronome", "Usage Events", "usage_events", ""]

        errors = validate_model_output(root, job, output)

        self.assertTrue(any("lowercase kebab-case" in error for error in errors))
        self.assertTrue(any("unique nonempty" in error for error in errors))

    def test_model_output_reports_unknown_metronome_concepts_for_sol(self):
        root = self.make_root()
        job = self.valid_model_job()
        output = self.valid_model_output(job)
        output["suggested_metronome_concepts"] = [
            "metronome-event-ingestion",
            "metronome-unknown-concept",
        ]

        errors = validate_model_output(root, job, output)

        self.assertTrue(
            any(
                "unknown existing Metronome concept for Sol review: metronome-unknown-concept"
                in error
                for error in errors
            )
        )

    def test_diagnostic_worker_receipt_requires_distinct_raw_and_normalized_outputs(self):
        root = self.make_root()
        job = self.valid_model_job()
        receipt = self.valid_model_worker_receipt(job)
        self.materialize_diagnostic_receipt(root, job, receipt)

        self.assertEqual([], validate_worker_receipt(root, job, receipt))

        receipt["attempts"][0]["normalized_output_path"] = receipt["attempts"][0]["output_path"]
        errors = validate_worker_receipt(root, job, receipt)

        self.assertTrue(any("raw and normalized output paths must differ" in error for error in errors))

    def test_diagnostic_receipt_requires_reconciled_runtime_evidence(self):
        root = self.make_root()
        job = self.valid_model_job()
        receipt = self.valid_model_worker_receipt(job)
        self.materialize_diagnostic_receipt(root, job, receipt)

        receipt.pop("input_mode")
        receipt.pop("progress_path")
        receipt.pop("runtime_metadata")
        receipt.pop("termination")
        receipt.pop("attempt_elapsed_seconds")
        receipt["attempts"][0]["streamed_stdout_bytes"] += 1

        errors = validate_worker_receipt(root, job, receipt)

        self.assertTrue(any("diagnostic input_mode is required" in error for error in errors))
        self.assertTrue(any("diagnostic progress_path is required" in error for error in errors))
        self.assertTrue(any("diagnostic runtime_metadata is required" in error for error in errors))
        self.assertTrue(any("diagnostic termination is required" in error for error in errors))
        self.assertTrue(any("attempt_elapsed_seconds is required" in error for error in errors))
        self.assertTrue(any("streamed_stdout_bytes does not match events_path" in error for error in errors))

    def test_diagnostic_receipt_rejects_traversal_and_symlink_path_escapes(self):
        root = self.make_root()
        job = self.valid_model_job()
        receipt = self.valid_model_worker_receipt(job)
        run_dir = self.materialize_diagnostic_receipt(root, job, receipt)
        receipt["events_path"] = (
            f"{job['artifact_dir']}/{receipt['run_id']}/../other/events.jsonl"
        )

        traversal_errors = validate_worker_receipt(root, job, receipt)

        self.assertTrue(
            any("events_path must not contain traversal" in error for error in traversal_errors)
        )

        receipt = self.valid_model_worker_receipt(job)
        run_dir = self.materialize_diagnostic_receipt(root, job, receipt, "terra-symlink")
        outside = root / "outside-events.jsonl"
        outside.write_text("{}\n", encoding="utf-8")
        escaped = run_dir / "events-link.jsonl"
        escaped.symlink_to(outside)
        receipt["events_path"] = (
            f"{job['artifact_dir']}/{receipt['run_id']}/events-link.jsonl"
        )

        symlink_errors = validate_worker_receipt(root, job, receipt)

        self.assertTrue(
            any("events_path resolves outside diagnostic run directory" in error for error in symlink_errors)
        )

    def test_diagnostic_receipt_rejects_missing_artifacts_and_tmp_leftovers(self):
        root = self.make_root()
        job = self.valid_model_job()
        receipt = self.valid_model_worker_receipt(job)
        run_dir = self.materialize_diagnostic_receipt(root, job, receipt)
        (run_dir / "model-output.normalized.json").unlink()
        (run_dir / "model-worker-receipt.json.tmp").write_text("partial", encoding="utf-8")

        errors = validate_worker_receipt(root, job, receipt)

        self.assertTrue(
            any("output_path must reference an existing regular file" in error for error in errors)
        )
        self.assertTrue(any("temporary artifact remains" in error for error in errors))

    def test_diagnostic_receipt_rejects_hardlinked_raw_and_normalized_artifacts(self):
        root = self.make_root()
        job = self.valid_model_job()
        receipt = self.valid_model_worker_receipt(job)
        run_dir = self.materialize_diagnostic_receipt(root, job, receipt)
        attempt_dir = run_dir / "attempt-1"
        normalized = attempt_dir / "model-output.normalized.json"
        normalized.unlink()
        os.link(attempt_dir / "model-output.raw.json", normalized)

        errors = validate_worker_receipt(root, job, receipt)

        self.assertTrue(
            any("raw and normalized output artifacts must be distinct" in error for error in errors)
        )

    def test_legacy_deterministic_receipt_cannot_claim_diagnostic_runtime_without_run_id(self):
        root = self.make_root()
        job = self.valid_model_job()
        receipt = self.valid_model_worker_receipt(job)
        receipt["runtime_metadata"] = {"sha256": {}}

        errors = validate_worker_receipt(root, job, receipt)

        self.assertTrue(
            any("diagnostic runtime fields require run_id" in error for error in errors)
        )

    def test_failed_diagnostic_receipt_requires_raw_output_and_existing_normalized_path(self):
        root = self.make_root()
        job = self.valid_model_job()
        receipt = self.valid_model_worker_receipt(job)
        self.materialize_diagnostic_receipt(root, job, receipt)
        run_dir = f"{job['artifact_dir']}/terra-20260717"
        receipt.update({
            "status": "failed",
            "process_exit_code": 1,
            "output_path": f"{run_dir}/attempt-1/model-output.raw.json",
            "normalized_output_path": f"{run_dir}/attempt-1/model-output.normalized.json",
            "draft_path": None,
            "events_path": f"{run_dir}/attempt-1/events.jsonl",
            "stderr_path": f"{run_dir}/attempt-1/stderr.log",
        })
        receipt["attempts"][0].update({
            "status": "rejected",
            "process_exit_code": 1,
            "validation_errors": ["process failed"],
            "output_path": f"{run_dir}/attempt-1/model-output.raw.json",
            "normalized_output_path": f"{run_dir}/attempt-1/model-output.normalized.json",
            "events_path": f"{run_dir}/attempt-1/events.jsonl",
            "stderr_path": f"{run_dir}/attempt-1/stderr.log",
        })

        self.assertEqual([], validate_worker_receipt(root, job, receipt))

        receipt["output_path"] = f"{run_dir}/attempt-1/output.json"
        errors = validate_worker_receipt(root, job, receipt)

        self.assertTrue(any("failed diagnostic output_path must reference model-output.raw.json" in error for error in errors))

    def test_failed_diagnostic_receipt_accepts_null_paths_when_no_output_exists(self):
        root = self.make_root()
        job = self.valid_model_job()
        receipt = self.valid_model_worker_receipt(job)
        self.materialize_diagnostic_receipt(root, job, receipt)
        run_dir = f"{job['artifact_dir']}/terra-20260717"
        receipt.update({
            "status": "failed",
            "process_exit_code": 1,
            "output_path": None,
            "normalized_output_path": None,
            "draft_path": None,
            "events_path": f"{run_dir}/attempt-1/events.jsonl",
            "stderr_path": f"{run_dir}/attempt-1/stderr.log",
        })
        receipt["attempts"][0].update({
            "status": "rejected",
            "process_exit_code": 1,
            "validation_errors": ["process failed"],
            "output_path": None,
            "normalized_output_path": None,
            "events_path": f"{run_dir}/attempt-1/events.jsonl",
            "stderr_path": f"{run_dir}/attempt-1/stderr.log",
        })

        self.assertEqual([], validate_worker_receipt(root, job, receipt))

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
        self.assertTrue(any("output_path resolves outside artifact_dir" in error for error in errors))

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
