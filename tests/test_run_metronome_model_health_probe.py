import json
import os
import signal
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from metronome_model_runtime import AttemptExecution, run_streaming_process  # noqa: E402
from run_metronome_model_health_probe import (  # noqa: E402
    FIRST_MODEL_EVENT_LIMIT_SECONDS,
    TOTAL_TIMEOUT_SECONDS,
    HealthProbeGateError,
    launch_enterprise_ab_if_probe_passes,
    run_health_probe,
)


class ModelHealthProbeTests(unittest.TestCase):
    def make_root(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        schema = root / "tracking/ingest/metronome/pilot/schemas/model-health-probe.schema.json"
        schema.parent.mkdir(parents=True)
        schema.write_text(
            json.dumps(
                {
                    "type": "object",
                    "required": ["status"],
                    "properties": {"status": {"const": "ok"}},
                    "additionalProperties": False,
                }
            ),
            encoding="utf-8",
        )
        prompt = root / "tracking/ingest/metronome/pilot/prompts/model-health-probe.md"
        prompt.parent.mkdir(parents=True)
        prompt.write_text('Return exactly {"status":"ok"}.\n', encoding="utf-8")
        return root

    @staticmethod
    def complete_metadata(timeout=60):
        return {
            "sha256": {
                "raw_text": "a" * 64,
                "prompt_template": "b" * 64,
                "rendered_prompt": "c" * 64,
                "output_schema": "d" * 64,
                "codex_executable": "e" * 64,
            },
            "codex_executable": "/fake/codex",
            "codex_cli_version": "codex-cli test",
            "timeout_seconds": timeout,
        }

    @staticmethod
    def execution(*, latency=0.2, elapsed=0.3, returncode=0, termination=None):
        return AttemptExecution(
            returncode=returncode,
            started_at="2026-07-17T00:00:00Z",
            finished_at="2026-07-17T00:00:01Z",
            elapsed_seconds=elapsed,
            time_to_first_stdout_event_seconds=latency,
            time_to_first_stderr_byte_seconds=None,
            streamed_stdout_bytes=24,
            streamed_stderr_bytes=0,
            parsed_event_count=1,
            truncated_line_count=0,
            token_usage={"input_tokens": 1, "output_tokens": 1},
            termination=termination,
        )

    def fake_executor(self, output, execution=None, captured=None):
        execution = execution or self.execution()

        def run(command, **kwargs):
            if captured is not None:
                captured.update(kwargs)
                captured["command"] = command
            attempt_dir = kwargs["attempt_dir"]
            attempt_dir.mkdir(parents=True, exist_ok=True)
            for name in ("events.jsonl", "stderr.log", "progress.jsonl"):
                (attempt_dir / name).touch()
            Path(command[command.index("-o") + 1]).write_text(output, encoding="utf-8")
            return execution

        return run

    def receipt(self, root, run_id):
        path = (
            root
            / "tracking/ingest/metronome/pilot/diagnostics/health-probes"
            / run_id
            / "model-health-probe-receipt.json"
        )
        return json.loads(path.read_text(encoding="utf-8"))

    def test_probe_enforces_60_second_total_cap(self):
        root = self.make_root()
        captured = {}

        result = run_health_probe(
            root,
            "luna-cap",
            executor=self.fake_executor('{"status":"ok"}', captured=captured),
            runtime_metadata_provider=lambda **_kwargs: self.complete_metadata(),
        )

        self.assertEqual(0, result)
        self.assertEqual(60, TOTAL_TIMEOUT_SECONDS)
        self.assertLessEqual(captured["timeout"], 60)
        self.assertEqual(60, self.receipt(root, "luna-cap")["total_timeout_seconds"])

    def test_probe_fails_when_first_model_event_exceeds_30_seconds(self):
        root = self.make_root()
        result = run_health_probe(
            root,
            "luna-late-event",
            executor=self.fake_executor(
                '{"status":"ok"}', execution=self.execution(latency=30.001)
            ),
            runtime_metadata_provider=lambda **_kwargs: self.complete_metadata(),
        )

        receipt = self.receipt(root, "luna-late-event")
        self.assertEqual(1, result)
        self.assertEqual(30, FIRST_MODEL_EVENT_LIMIT_SECONDS)
        self.assertEqual("failed", receipt["status"])
        self.assertFalse(receipt["first_model_event_within_limit"])

    def test_probe_accepts_only_the_valid_tiny_terminal_json(self):
        root = self.make_root()
        result = run_health_probe(
            root,
            "luna-valid-json",
            executor=self.fake_executor('{"status":"ok"}'),
            runtime_metadata_provider=lambda **_kwargs: self.complete_metadata(),
        )

        receipt = self.receipt(root, "luna-valid-json")
        self.assertEqual(0, result)
        self.assertEqual("passed", receipt["status"])
        self.assertTrue(receipt["terminal_json_valid"])

        second_root = self.make_root()
        invalid_result = run_health_probe(
            second_root,
            "luna-invalid-json",
            executor=self.fake_executor('{"status":"unexpected"}'),
            runtime_metadata_provider=lambda **_kwargs: self.complete_metadata(),
        )
        invalid_receipt = self.receipt(second_root, "luna-invalid-json")
        self.assertEqual(1, invalid_result)
        self.assertFalse(invalid_receipt["terminal_json_valid"])

    def test_probe_requires_complete_runtime_metadata(self):
        root = self.make_root()
        incomplete = self.complete_metadata()
        del incomplete["sha256"]["codex_executable"]

        result = run_health_probe(
            root,
            "luna-incomplete-metadata",
            executor=self.fake_executor('{"status":"ok"}'),
            runtime_metadata_provider=lambda **_kwargs: incomplete,
        )

        receipt = self.receipt(root, "luna-incomplete-metadata")
        self.assertEqual(1, result)
        self.assertFalse(receipt["runtime_metadata_complete"])

    def test_receipt_contains_complete_runtime_and_cleanup_accounting(self):
        root = self.make_root()
        execution = self.execution(latency=0.25, elapsed=0.5)

        result = run_health_probe(
            root,
            "luna-runtime-accounting",
            executor=self.fake_executor('{"status":"ok"}', execution=execution),
            runtime_metadata_provider=lambda **_kwargs: self.complete_metadata(),
        )

        receipt = self.receipt(root, "luna-runtime-accounting")
        self.assertEqual(0, result)
        self.assertEqual("fixed-prompt", receipt["input_mode"])
        self.assertEqual(execution.started_at, receipt["attempt_started_at"])
        self.assertEqual(execution.finished_at, receipt["attempt_finished_at"])
        self.assertEqual(execution.elapsed_seconds, receipt["attempt_elapsed_seconds"])
        self.assertEqual(
            execution.time_to_first_stdout_event_seconds,
            receipt["time_to_first_stdout_event_seconds"],
        )
        self.assertEqual(
            execution.time_to_first_stderr_byte_seconds,
            receipt["time_to_first_stderr_byte_seconds"],
        )
        self.assertEqual(
            {"passed": True, "termination": None}, receipt["process_cleanup"]
        )
        self.assertFalse(receipt["canonical_coverage_eligible"])

    def test_probe_receipt_is_published_atomically(self):
        root = self.make_root()
        observed = {}
        real_replace = os.replace

        def observe_replace(source, destination):
            source_path = Path(source)
            destination_path = Path(destination)
            if destination_path.name == "model-health-probe-receipt.json":
                observed["tmp_exists"] = source_path.is_file()
                observed["final_absent"] = not destination_path.exists()
            real_replace(source, destination)

        with patch("metronome_model_runtime.os.replace", side_effect=observe_replace):
            result = run_health_probe(
                root,
                "luna-atomic",
                executor=self.fake_executor('{"status":"ok"}'),
                runtime_metadata_provider=lambda **_kwargs: self.complete_metadata(),
            )

        self.assertEqual(0, result)
        self.assertEqual({"tmp_exists": True, "final_absent": True}, observed)

    def test_timeout_cleans_up_the_probe_process_group(self):
        root = self.make_root()
        child_pid_path = root / "child.pid"

        def live_timeout_executor(_command, **kwargs):
            child_code = (
                "import signal,time;"
                "signal.signal(signal.SIGTERM,signal.SIG_IGN);"
                "time.sleep(30)"
            )
            parent_code = (
                "import json,pathlib,signal,subprocess,sys,time;"
                "signal.signal(signal.SIGTERM,signal.SIG_IGN);"
                "child=subprocess.Popen([sys.executable,'-c',sys.argv[2]]);"
                "pathlib.Path(sys.argv[1]).write_text(str(child.pid),encoding='utf-8');"
                "print(json.dumps({'type':'thread.started'}),flush=True);"
                "time.sleep(30)"
            )
            return run_streaming_process(
                [sys.executable, "-c", parent_code, str(child_pid_path), child_code],
                cwd=kwargs["cwd"],
                timeout=kwargs["timeout"],
                env=kwargs["env"],
                attempt_dir=kwargs["attempt_dir"],
                termination_grace_seconds=0.05,
                pipe_cleanup_seconds=0.05,
            )

        result = run_health_probe(
            root,
            "luna-cleanup",
            executor=live_timeout_executor,
            runtime_metadata_provider=lambda **_kwargs: self.complete_metadata(0.2),
            total_timeout_seconds=0.2,
        )

        receipt = self.receipt(root, "luna-cleanup")
        self.assertEqual(1, result)
        self.assertTrue(receipt["process_cleanup_passed"])
        self.assertTrue(child_pid_path.is_file())
        child_pid = int(child_pid_path.read_text(encoding="utf-8"))
        deadline = time.monotonic() + 2
        while time.monotonic() < deadline:
            try:
                os.kill(child_pid, 0)
            except ProcessLookupError:
                break
            time.sleep(0.02)
        else:
            try:
                os.kill(child_pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            self.fail("probe child process survived timeout cleanup")

    def test_failed_probe_prevents_enterprise_ab_launch(self):
        root = self.make_root()
        receipt_path = root / "failed-probe.json"
        receipt_path.write_text(
            json.dumps(
                {
                    "diagnostic_type": "model_health_probe",
                    "status": "failed",
                    "terminal_json_valid": False,
                    "first_model_event_within_limit": True,
                    "runtime_metadata_complete": True,
                    "process_cleanup_passed": True,
                }
            ),
            encoding="utf-8",
        )
        launches = []

        with self.assertRaisesRegex(HealthProbeGateError, "enterprise A/B remains suspended"):
            launch_enterprise_ab_if_probe_passes(receipt_path, lambda: launches.append(True))

        self.assertEqual([], launches)

    def test_repository_prompt_schema_and_manifest_keep_probe_diagnostic_only(self):
        prompt = (
            ROOT / "tracking/ingest/metronome/pilot/prompts/model-health-probe.md"
        ).read_text(encoding="utf-8")
        schema = json.loads(
            (
                ROOT
                / "tracking/ingest/metronome/pilot/schemas/model-health-probe.schema.json"
            ).read_text(encoding="utf-8")
        )
        manifest = (
            ROOT / "tracking/ingest/metronome/pilot/luna-expansion-manifest.md"
        ).read_text(encoding="utf-8")

        self.assertIn('{"status":"ok"}', prompt)
        self.assertEqual("ok", schema["properties"]["status"]["const"])
        self.assertIn("enterprise A/B remains suspended", manifest)
        self.assertIn("never participates in canonical coverage", manifest)


if __name__ == "__main__":
    unittest.main()
