import json
import os
import subprocess
import sys
import tempfile
import threading
import unittest
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from run_metronome_model_worker import (  # noqa: E402
    build_codex_command,
    build_page_profile,
    recover_attempt,
    repair_mandatory_tags,
    repair_raw_link,
    repair_quote_bounds,
    run_worker,
)
from metronome_model_runtime import (  # noqa: E402
    resolve_run_dir,
    validate_run_id,
    write_json_atomic,
)


class ModelWorkerRunnerTests(unittest.TestCase):
    def make_root(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        raw = root / "raw/metronome/guides/home.md"
        raw.parent.mkdir(parents=True)
        raw.write_text("# Alpha\nintro\n## Beta\nrequired when enabled\n", encoding="utf-8")
        schema = root / "tracking/ingest/metronome/pilot/schemas/model-output-v3.schema.json"
        schema.parent.mkdir(parents=True)
        schema.write_text('{"type":"object"}', encoding="utf-8")
        prompt = root / "tracking/ingest/metronome/pilot/prompts/source-summary-v3.md"
        prompt.parent.mkdir(parents=True)
        prompt.write_text("Read raw.md completely and return JSON.", encoding="utf-8")
        job = self.valid_job()
        job_path = root / "tracking/ingest/metronome/pilot/jobs/terra-home.json"
        job_path.parent.mkdir(parents=True)
        job_path.write_text(json.dumps(job), encoding="utf-8")
        return root, job_path, job

    def valid_job(self):
        run_dir = "tracking/ingest/metronome/pilot/runs/terra-home"
        return {
            "schema_version": 3,
            "job_id": "terra-home",
            "provider": "metronome",
            "mode": "real_ingest",
            "canonical_url": "https://docs.metronome.com/guides/home",
            "raw_path": "raw/metronome/guides/home.md",
            "source_page": "wiki/sources/metronome/source-home.md",
            "artifact_dir": run_dir,
            "role": "cheap_ingester",
            "model_provider": "openai",
            "model": "gpt-5.6-terra",
            "reasoning_effort": "medium",
            "allowed_write_paths": [run_dir],
            "forbidden_write_paths": ["wiki/metronome-index.md"],
            "forbidden_write_prefixes": ["raw/", "wiki/"],
        }

    def valid_output(self, job):
        return {
            "job_id": job["job_id"],
            "raw_path": job["raw_path"],
            "canonical_url": job["canonical_url"],
            "title": "Home",
            "grounding_quotes": [
                {"id": "q1", "line_start": 1, "line_end": 1, "text": "# Alpha", "supports": "title"},
                {"id": "q2", "line_start": 2, "line_end": 2, "text": "intro", "supports": "overview"},
                {"id": "q3", "line_start": 3, "line_end": 4, "text": "## Beta\nrequired when enabled", "supports": "condition"},
            ],
            "overview": "Overview.",
            "overview_evidence_quote_ids": ["q2"],
            "key_takeaways": [{"text": "Takeaway.", "evidence_quote_ids": ["q1"]}],
            "details": [{"heading": "Beta", "facts": [{"text": "Fact.", "evidence_quote_ids": ["q3"]}]}],
            "sections_covered": ["Alpha", "Beta"],
            "scope_boundaries": [],
            "conditional_requirements": [{"text": "Conditional.", "evidence_quote_ids": ["q3"]}],
            "feature_gates": [],
            "internal_inconsistencies": [],
            "material_omissions": [],
            "suggested_tags": ["metronome"],
            "suggested_metronome_concepts": [],
            "proposed_raw_link": "[[raw/metronome/guides/home|snapshot]]",
            "unsupported_claim_self_check": [],
        }

    def test_command_uses_job_model_reasoning_read_only_and_minimal_cwd(self):
        command = build_codex_command(
            Path("/tmp/minimal"), Path("/repo/schema.json"), Path("/repo/output.json"),
            "prompt", "gpt-5.6-terra", "medium"
        )

        self.assertIn("gpt-5.6-terra", command)
        self.assertIn('model_reasoning_effort="medium"', command)
        self.assertEqual("read-only", command[command.index("-s") + 1])
        self.assertEqual("/tmp/minimal", command[command.index("-C") + 1])
        self.assertIn("--skip-git-repo-check", command)
        self.assertNotIn("--ignore-user-config", command)
        for feature in ("plugins", "remote_plugin", "apps", "hooks", "memories"):
            positions = [index for index, value in enumerate(command) if value == "--disable"]
            self.assertTrue(any(command[index + 1] == feature for index in positions))

    def test_page_profile_covers_headings_and_conditional_hints(self):
        profile = build_page_profile("# Alpha\n## Beta\nrequired when enabled\n")

        self.assertEqual(["Alpha", "Beta"], profile["headings"])
        self.assertEqual([3], profile["conditional_hint_lines"])

    def test_unique_exact_quote_gets_local_line_repair(self):
        output = {"grounding_quotes": [{"line_start": 9, "line_end": 9, "text": "beta"}]}

        repaired = repair_quote_bounds("alpha\nbeta\ngamma\n", output)

        self.assertEqual(1, repaired)
        self.assertEqual((2, 2), (output["grounding_quotes"][0]["line_start"], output["grounding_quotes"][0]["line_end"]))

    def test_ambiguous_quote_is_not_repaired(self):
        output = {"grounding_quotes": [{"line_start": 9, "line_end": 9, "text": "same"}]}

        self.assertEqual(0, repair_quote_bounds("same\nother\nsame\n", output))

    def test_raw_link_target_is_repaired_without_changing_label(self):
        job = self.valid_job()
        output = {"proposed_raw_link": "[[raw/metronome/wrong|dated snapshot]]"}

        self.assertTrue(repair_raw_link(job, output))
        self.assertEqual(
            "[[raw/metronome/guides/home|dated snapshot]]",
            output["proposed_raw_link"],
        )

    def test_tags_are_repaired_to_unique_lowercase_kebab_case(self):
        output = {
            "suggested_tags": [
                "Usage Events",
                "usage_events",
                "USAGE-EVENTS",
                "",
                "Invoices & Credits!",
            ]
        }

        self.assertEqual(1, repair_mandatory_tags(output))
        self.assertEqual(
            ["metronome", "usage-events", "invoices-credits"],
            output["suggested_tags"],
        )
        self.assertEqual(0, repair_mandatory_tags(output))

    def test_diagnostic_run_ids_require_lowercase_kebab_case(self):
        self.assertEqual("terra-20260717", validate_run_id("terra-20260717"))
        for invalid in ("", "Terra-20260717", "terra_20260717", "terra--20260717"):
            with self.assertRaises(ValueError):
                validate_run_id(invalid)

    def test_existing_diagnostic_run_is_rejected_before_runner_invocation(self):
        root, job_path, job = self.make_root()
        run_dir = resolve_run_dir(root, job, "terra-20260717")
        run_dir.mkdir(parents=True)
        calls = []

        def fake_runner(*args, **kwargs):
            calls.append((args, kwargs))
            raise AssertionError("runner must not be invoked")

        self.assertEqual(
            1,
            run_worker(root, job_path, "2026-07-17", runner=fake_runner, run_id="terra-20260717"),
        )
        self.assertEqual([], calls)

    def test_concurrent_diagnostic_claims_start_exactly_one_runner(self):
        root, job_path, job = self.make_root()
        run_id = "terra-20260717"
        target = resolve_run_dir(root, job, run_id)
        original_exists = Path.exists
        barrier = threading.Barrier(2)
        runner_calls = []
        results = []

        def race_boundary_exists(path):
            if path == target:
                barrier.wait(timeout=2)
                return False
            return original_exists(path)

        def fake_runner(*args, **kwargs):
            runner_calls.append(args)
            raise subprocess.TimeoutExpired(args[0], kwargs["timeout"])

        def invoke():
            results.append(
                run_worker(root, job_path, "2026-07-17", runner=fake_runner, run_id=run_id)
            )

        from unittest.mock import patch
        with patch("run_metronome_model_worker.Path.exists", new=race_boundary_exists):
            threads = [threading.Thread(target=invoke) for _ in range(2)]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join(timeout=5)

        self.assertEqual([False, False], [thread.is_alive() for thread in threads])
        self.assertEqual(2, len(results))
        self.assertEqual(1, len(runner_calls))
        self.assertTrue(target.is_dir())

    def test_legacy_worker_keeps_direct_job_artifact_layout(self):
        root, job_path, job = self.make_root()

        def fake_runner(command, **kwargs):
            Path(command[command.index("-o") + 1]).write_text(
                json.dumps(self.valid_output(job)), encoding="utf-8"
            )
            return SimpleNamespace(returncode=0, stdout="", stderr="")

        self.assertEqual(0, run_worker(root, job_path, "2026-07-17", runner=fake_runner))
        artifact_dir = root / job["artifact_dir"]
        self.assertTrue((artifact_dir / "model-output.json").is_file())
        self.assertTrue((artifact_dir / "model-worker-receipt.json").is_file())
        self.assertFalse(any(artifact_dir.glob("terra-20260717")))

    def test_diagnostic_repair_preserves_raw_output_and_writes_normalized_output(self):
        root, job_path, job = self.make_root()
        raw_payload = self.valid_output(job)
        raw_payload["proposed_raw_link"] = "[[raw/metronome/wrong|snapshot]]"

        def fake_runner(command, **kwargs):
            Path(command[command.index("-o") + 1]).write_text(
                json.dumps(raw_payload), encoding="utf-8"
            )
            return SimpleNamespace(returncode=0, stdout="", stderr="")

        run_id = "terra-20260717"
        self.assertEqual(
            0,
            run_worker(root, job_path, "2026-07-17", runner=fake_runner, run_id=run_id),
        )
        attempt_dir = resolve_run_dir(root, job, run_id) / "attempt-1"
        raw_path = attempt_dir / "model-output.raw.json"
        normalized_path = attempt_dir / "model-output.normalized.json"
        self.assertEqual(raw_payload, json.loads(raw_path.read_text(encoding="utf-8")))
        normalized = json.loads(normalized_path.read_text(encoding="utf-8"))
        self.assertEqual("[[raw/metronome/guides/home|snapshot]]", normalized["proposed_raw_link"])
        self.assertNotEqual(raw_path.read_bytes(), normalized_path.read_bytes())

    def test_failed_diagnostic_receipt_references_existing_raw_and_normalized_outputs(self):
        root, job_path, job = self.make_root()

        def fake_runner(command, **kwargs):
            Path(command[command.index("-o") + 1]).write_text(
                json.dumps(self.valid_output(job)), encoding="utf-8"
            )
            return SimpleNamespace(returncode=1, stdout="", stderr="failed")

        run_id = "terra-20260717"
        self.assertEqual(
            1,
            run_worker(root, job_path, "2026-07-17", runner=fake_runner, run_id=run_id),
        )
        run_dir = resolve_run_dir(root, job, run_id)
        receipt = json.loads((run_dir / "model-worker-receipt.json").read_text(encoding="utf-8"))

        self.assertEqual("failed", receipt["status"])
        self.assertTrue(receipt["output_path"].endswith("attempt-2/model-output.raw.json"))
        self.assertTrue(receipt["normalized_output_path"].endswith("attempt-2/model-output.normalized.json"))
        self.assertTrue((root / receipt["output_path"]).is_file())
        self.assertTrue((root / receipt["normalized_output_path"]).is_file())

    def test_failed_diagnostic_receipt_uses_null_paths_when_no_output_exists(self):
        root, job_path, _job = self.make_root()

        def fake_runner(command, **kwargs):
            return SimpleNamespace(returncode=1, stdout="", stderr="failed")

        self.assertEqual(
            1,
            run_worker(root, job_path, "2026-07-17", runner=fake_runner, run_id="terra-20260717"),
        )
        receipt_path = (
            resolve_run_dir(root, _job, "terra-20260717") / "model-worker-receipt.json"
        )
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))

        self.assertIsNone(receipt["output_path"])
        self.assertIsNone(receipt["normalized_output_path"])
        self.assertIsNone(receipt["attempts"][-1]["output_path"])
        self.assertIsNone(receipt["attempts"][-1]["normalized_output_path"])

    def test_atomic_receipt_is_tmp_until_replace_publishes_final_file(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        receipt_path = Path(tmp.name) / "model-worker-receipt.json"
        observed = []
        original_replace = os.replace

        def observing_replace(source, destination):
            observed.append((Path(source).read_text(encoding="utf-8"), Path(destination).exists()))
            self.assertTrue(Path(source).name.endswith(".tmp"))
            self.assertFalse(Path(destination).exists())
            original_replace(source, destination)

        from unittest.mock import patch
        with patch("metronome_model_runtime.os.replace", side_effect=observing_replace):
            write_json_atomic(receipt_path, {"status": "success"})

        self.assertEqual(1, len(observed))
        self.assertFalse((Path(tmp.name) / "model-worker-receipt.json.tmp").exists())
        self.assertEqual({"status": "success"}, json.loads(receipt_path.read_text(encoding="utf-8")))

    def test_retry_receipt_sums_usage_and_keeps_rejected_reason(self):
        root, job_path, job = self.make_root()
        calls = []
        staged_files = []

        def fake_runner(command, **kwargs):
            calls.append((command, kwargs))
            staged_files.append((Path(kwargs["cwd"]) / "raw.md").is_file())
            output = self.valid_output(job)
            if len(calls) == 1:
                output["key_takeaways"][0]["evidence_quote_ids"] = ["missing"]
            output_path = Path(command[command.index("-o") + 1])
            output_path.write_text(json.dumps(output), encoding="utf-8")
            usage = {"input_tokens": 100 * len(calls), "output_tokens": 10 * len(calls)}
            return SimpleNamespace(returncode=0, stdout=json.dumps({"usage": usage}) + "\n", stderr="")

        result = run_worker(root, job_path, "2026-07-14", runner=fake_runner)

        self.assertEqual(0, result)
        self.assertEqual(2, len(calls))
        self.assertEqual(900, calls[0][1]["timeout"])
        self.assertNotEqual(root, calls[0][1]["cwd"])
        self.assertEqual([True, True], staged_files)
        self.assertNotEqual(str(Path.home() / ".codex"), calls[0][1]["env"]["CODEX_HOME"])
        self.assertFalse((Path(calls[0][1]["env"]["CODEX_HOME"]) / "skills").exists())
        receipt = json.loads((root / job["artifact_dir"] / "model-worker-receipt.json").read_text())
        self.assertEqual({"input_tokens": 300, "output_tokens": 30}, receipt["cumulative_token_usage"])
        self.assertIn("undefined grounding quote", receipt["attempts"][0]["retry_reason"])
        self.assertEqual("rejected", receipt["attempts"][0]["status"])
        self.assertEqual("accepted", receipt["attempts"][1]["status"])

    def test_quote_only_failure_is_repaired_without_retry(self):
        root, job_path, job = self.make_root()
        calls = []

        def fake_runner(command, **kwargs):
            calls.append(command)
            output = self.valid_output(job)
            output["grounding_quotes"][0]["line_start"] = 99
            output["grounding_quotes"][0]["line_end"] = 99
            output_path = Path(command[command.index("-o") + 1])
            output_path.write_text(json.dumps(output), encoding="utf-8")
            return SimpleNamespace(returncode=0, stdout="", stderr="")

        result = run_worker(root, job_path, "2026-07-14", runner=fake_runner)

        self.assertEqual(0, result)
        self.assertEqual(1, len(calls))
        receipt = json.loads((root / job["artifact_dir"] / "model-worker-receipt.json").read_text())
        self.assertEqual(1, receipt["quote_line_repairs"])

    def test_process_timeout_fails_fast_without_second_attempt(self):
        root, job_path, job = self.make_root()
        calls = []

        def fake_runner(command, **kwargs):
            calls.append(command)
            raise subprocess.TimeoutExpired(command, kwargs["timeout"])

        result = run_worker(root, job_path, "2026-07-15", runner=fake_runner)

        self.assertEqual(1, result)
        self.assertEqual(1, len(calls))
        receipt = json.loads((root / job["artifact_dir"] / "model-worker-receipt.json").read_text())
        self.assertEqual(1, receipt["attempt_count"])
        self.assertEqual(124, receipt["process_exit_code"])

    def test_recover_attempt_accepts_prior_output_after_deterministic_tag_repair(self):
        root, job_path, job = self.make_root()
        artifact_dir = root / job["artifact_dir"]
        attempt_dir = artifact_dir / "attempt-1"
        attempt_dir.mkdir(parents=True)
        output = self.valid_output(job)
        output["suggested_tags"] = ["events"]
        (attempt_dir / "output.json").write_text(json.dumps(output), encoding="utf-8")
        (attempt_dir / "events.jsonl").write_text("", encoding="utf-8")
        (attempt_dir / "stderr.log").write_text("", encoding="utf-8")
        receipt = {
            "schema_version": 3,
            "job_id": job["job_id"],
            "provider": job["provider"],
            "canonical_url": job["canonical_url"],
            "raw_path": job["raw_path"],
            "source_page": job["source_page"],
            "status": "failed",
            "model_provider": job["model_provider"],
            "model": job["model"],
            "reasoning_effort": job["reasoning_effort"],
            "attempt_count": 1,
            "attempts": [{
                "attempt": 1, "status": "rejected", "process_exit_code": 0,
                "validation_errors": ["model output: suggested_tags must include metronome"],
                "retry_reason": "model output: suggested_tags must include metronome",
                "output_path": f"{job['artifact_dir']}/attempt-1/output.json",
                "events_path": f"{job['artifact_dir']}/attempt-1/events.jsonl",
                "stderr_path": f"{job['artifact_dir']}/attempt-1/stderr.log",
                "token_usage": {"input_tokens": 10, "output_tokens": 2},
            }],
            "started_at": "2026-07-16T00:00:00Z", "finished_at": "2026-07-16T00:01:00Z",
            "elapsed_seconds": 60, "process_exit_code": 1,
            "output_path": f"{job['artifact_dir']}/attempt-1/output.json", "draft_path": None,
            "events_path": f"{job['artifact_dir']}/attempt-1/events.jsonl",
            "stderr_path": f"{job['artifact_dir']}/attempt-1/stderr.log",
            "grounding_quotes": [], "validation": [], "token_usage": None,
            "cumulative_token_usage": {"input_tokens": 10, "output_tokens": 2},
            "token_usage_unavailable_reason": None, "quote_line_repairs": 0,
            "raw_link_repairs": 0,
        }
        (artifact_dir / "model-worker-receipt.json").write_text(json.dumps(receipt), encoding="utf-8")

        result = recover_attempt(root, job_path, "2026-07-16", 1)

        self.assertEqual(0, result)
        recovered = json.loads((artifact_dir / "model-worker-receipt.json").read_text())
        self.assertEqual("success", recovered["status"])
        self.assertEqual(1, recovered["recovered_from_attempt"])
        self.assertEqual(1, recovered["mandatory_tag_repairs"])
        self.assertTrue((artifact_dir / "model-source-draft.md").is_file())


if __name__ == "__main__":
    unittest.main()
