import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from run_metronome_luna_worker import (  # noqa: E402
    build_codex_command,
    build_prompt,
    run_worker,
)


class LunaWorkerRunnerTests(unittest.TestCase):
    def make_root(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        raw = root / "raw/metronome/guides/home.md"
        raw.parent.mkdir(parents=True)
        raw.write_text("alpha\nbeta\ngamma\n", encoding="utf-8")
        schema = root / "tracking/ingest/metronome/pilot/schemas/luna-output.schema.json"
        schema.parent.mkdir(parents=True)
        schema.write_text('{"type":"object"}', encoding="utf-8")
        prompt = root / "tracking/ingest/metronome/pilot/prompts/source-summary-benchmark.md"
        prompt.parent.mkdir(parents=True)
        prompt.write_text("Read one complete file and return JSON.", encoding="utf-8")
        job = self.valid_job()
        job_path = root / "tracking/ingest/metronome/pilot/jobs/pilot-home-luna.json"
        job_path.parent.mkdir(parents=True)
        job_path.write_text(json.dumps(job), encoding="utf-8")
        return root, job_path, job

    def valid_job(self):
        run_dir = "tracking/ingest/metronome/pilot/runs/pilot-home-luna"
        return {
            "schema_version": 2,
            "job_id": "pilot-home-luna",
            "provider": "metronome",
            "mode": "shadow",
            "canonical_url": "https://docs.metronome.com/guides/home",
            "raw_path": "raw/metronome/guides/home.md",
            "source_page": "wiki/sources/metronome/source-home.md",
            "artifact_dir": run_dir,
            "role": "cheap_ingester",
            "model_provider": "openai",
            "model": "gpt-5.6-luna",
            "reasoning_effort": "high",
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
                {"line_start": 1, "line_end": 1, "text": "alpha", "supports": "a"},
                {"line_start": 2, "line_end": 2, "text": "beta", "supports": "b"},
                {"line_start": 3, "line_end": 3, "text": "gamma", "supports": "c"},
            ],
            "overview": "Overview.",
            "key_takeaways": ["Takeaway."],
            "details": [{"heading": "Scope", "facts": ["Fact."]}],
            "suggested_tags": ["metronome"],
            "suggested_metronome_concepts": [],
            "proposed_raw_link": "[[raw/metronome/guides/home|snapshot]]",
            "unsupported_claim_self_check": [],
        }

    def test_build_codex_command_pins_model_reasoning_and_read_only_sandbox(self):
        root = Path("/repo")
        schema = root / "schema.json"
        output = root / "output.json"

        command = build_codex_command(root, schema, output, "prompt")

        self.assertEqual(
            [
                "codex",
                "exec",
                "-m",
                "gpt-5.6-luna",
                "-c",
                'model_reasoning_effort="high"',
                "-s",
                "read-only",
                "-a",
                "never",
                "--ephemeral",
                "--output-schema",
                str(schema),
                "--json",
                "-o",
                str(output),
                "-C",
                str(root),
                "prompt",
            ],
            command,
        )

    def test_build_prompt_includes_job_identity_and_retry_errors(self):
        job = self.valid_job()

        prompt = build_prompt("template", job, ["quote 1 does not match"])

        self.assertIn(job["job_id"], prompt)
        self.assertIn(job["raw_path"], prompt)
        self.assertIn(job["canonical_url"], prompt)
        self.assertIn("quote 1 does not match", prompt)

    def test_success_writes_accepted_output_draft_receipt_and_attempt_log(self):
        root, job_path, job = self.make_root()

        def fake_runner(command, **kwargs):
            output_path = Path(command[command.index("-o") + 1])
            output_path.write_text(json.dumps(self.valid_output(job)), encoding="utf-8")
            return SimpleNamespace(
                returncode=0,
                stdout='{"type":"turn.completed","usage":{"input_tokens":100,"output_tokens":20}}\n',
                stderr="",
            )

        result = run_worker(root, job_path, "2026-07-14", runner=fake_runner)

        run_dir = root / job["artifact_dir"]
        self.assertEqual(0, result)
        self.assertTrue((run_dir / "luna-output.json").is_file())
        self.assertTrue((run_dir / "luna-source-draft.md").is_file())
        self.assertTrue((run_dir / "luna-worker-receipt.json").is_file())
        self.assertTrue((run_dir / "attempt-1/events.jsonl").is_file())
        receipt = json.loads((run_dir / "luna-worker-receipt.json").read_text())
        self.assertEqual("success", receipt["status"])
        self.assertEqual({"input_tokens": 100, "output_tokens": 20}, receipt["token_usage"])

    def test_invalid_first_output_retries_once_with_validation_errors(self):
        root, job_path, job = self.make_root()
        calls = []

        def fake_runner(command, **kwargs):
            calls.append(command)
            output = self.valid_output(job)
            if len(calls) == 1:
                output["grounding_quotes"][0]["text"] = "wrong"
            output_path = Path(command[command.index("-o") + 1])
            output_path.write_text(json.dumps(output), encoding="utf-8")
            return SimpleNamespace(returncode=0, stdout="", stderr="")

        result = run_worker(root, job_path, "2026-07-14", runner=fake_runner)

        self.assertEqual(0, result)
        self.assertEqual(2, len(calls))
        self.assertIn("does not match raw lines", calls[1][-1])
        receipt = json.loads(
            (root / job["artifact_dir"] / "luna-worker-receipt.json").read_text()
        )
        self.assertEqual(2, receipt["attempt_count"])

    def test_second_invalid_output_records_failure_without_draft(self):
        root, job_path, job = self.make_root()

        def fake_runner(command, **kwargs):
            output_path = Path(command[command.index("-o") + 1])
            output_path.write_text("not json", encoding="utf-8")
            return SimpleNamespace(returncode=0, stdout="", stderr="")

        result = run_worker(root, job_path, "2026-07-14", runner=fake_runner)

        run_dir = root / job["artifact_dir"]
        self.assertEqual(1, result)
        self.assertTrue((run_dir / "attempt-1/output.json").is_file())
        self.assertTrue((run_dir / "attempt-2/output.json").is_file())
        self.assertFalse((run_dir / "luna-source-draft.md").exists())
        receipt = json.loads((run_dir / "luna-worker-receipt.json").read_text())
        self.assertEqual("failed", receipt["status"])
        self.assertEqual(2, receipt["attempt_count"])


if __name__ == "__main__":
    unittest.main()
