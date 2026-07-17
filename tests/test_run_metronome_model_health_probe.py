import hashlib
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
    class FakeClock:
        def __init__(self):
            self.value = 0.0

        def __call__(self):
            return self.value

        def advance(self, seconds):
            self.value += seconds

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
        execution = AttemptExecution(
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
        execution.time_to_first_model_event_seconds = latency
        return execution

    def fake_executor(self, output, execution=None, captured=None, events=None):
        execution = execution or self.execution()
        events = events or [
            {"type": "thread.started"},
            {"type": "turn.started"},
            {
                "type": "item.completed",
                "item": {"type": "agent_message", "text": output},
                "usage": execution.token_usage,
            },
        ]

        def run(command, **kwargs):
            if captured is not None:
                captured.update(kwargs)
                captured["command"] = command
            attempt_dir = kwargs["attempt_dir"]
            attempt_dir.mkdir(parents=True, exist_ok=True)
            for name in ("events.jsonl", "stderr.log", "progress.jsonl"):
                (attempt_dir / name).touch()
            events_bytes = "".join(
                json.dumps(event) + "\n" for event in events
            ).encode("utf-8")
            (attempt_dir / "events.jsonl").write_bytes(events_bytes)
            progress_records = [
                {"event": "process_started", "pid": 12345},
                {
                    "event": "first_model_event",
                    "elapsed_seconds": execution.time_to_first_model_event_seconds,
                    "event_type": "item.completed",
                    "item_type": "agent_message",
                },
                {
                    "event": "process_exited",
                    "process_return_code": execution.returncode,
                    "logical_return_code": execution.returncode,
                    "elapsed_seconds": execution.elapsed_seconds,
                },
            ]
            (attempt_dir / "progress.jsonl").write_text(
                "".join(json.dumps(record) + "\n" for record in progress_records),
                encoding="utf-8",
            )
            execution.streamed_stdout_bytes = len(events_bytes)
            execution.parsed_event_count = len(events)
            execution.truncated_line_count = 0
            execution.token_usage = next(
                (
                    event["usage"]
                    for event in reversed(events)
                    if isinstance(event.get("usage"), dict)
                ),
                None,
            )
            Path(command[command.index("-o") + 1]).write_text(output, encoding="utf-8")
            return execution

        return run

    def receipt(self, root, run_id):
        return json.loads(self.receipt_path(root, run_id).read_text(encoding="utf-8"))

    @staticmethod
    def receipt_path(root, run_id):
        return (
            root
            / "tracking/ingest/metronome/pilot/diagnostics/health-probes"
            / run_id
            / "model-health-probe-receipt.json"
        )

    def real_metadata_provider(self, root, timeout=60):
        executable = root / "fake-codex"
        executable.write_bytes(b"deterministic fake codex")

        def provider(**kwargs):
            self.assertEqual(timeout, kwargs["timeout_seconds"])
            return {
                "sha256": {
                    "raw_text": hashlib.sha256(kwargs["raw_bytes"]).hexdigest(),
                    "prompt_template": hashlib.sha256(
                        kwargs["prompt_template_bytes"]
                    ).hexdigest(),
                    "rendered_prompt": hashlib.sha256(
                        kwargs["rendered_prompt"].encode("utf-8")
                    ).hexdigest(),
                    "output_schema": hashlib.sha256(
                        kwargs["schema_path"].read_bytes()
                    ).hexdigest(),
                    "codex_executable": hashlib.sha256(executable.read_bytes()).hexdigest(),
                },
                "codex_executable": str(executable),
                "codex_cli_version": "codex-cli deterministic",
                "timeout_seconds": timeout,
            }

        return provider

    def make_passing_probe(self, root, run_id="luna-gate"):
        result = run_health_probe(
            root,
            run_id,
            executor=self.fake_executor('{"status":"ok"}'),
            runtime_metadata_provider=self.real_metadata_provider(root),
        )
        self.assertEqual(0, result)
        return self.receipt_path(root, run_id)

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

    def test_lifecycle_events_do_not_satisfy_the_model_activity_gate(self):
        root = self.make_root()
        result = run_health_probe(
            root,
            "luna-lifecycle-only",
            executor=self.fake_executor(
                '{"status":"ok"}',
                execution=self.execution(latency=0.01),
                events=[{"type": "thread.started"}, {"type": "turn.started"}],
            ),
            runtime_metadata_provider=lambda **_kwargs: self.complete_metadata(),
        )

        receipt = self.receipt(root, "luna-lifecycle-only")
        self.assertEqual(1, result)
        self.assertIsNone(receipt["first_model_event_latency_seconds"])
        self.assertFalse(receipt["first_model_event_within_limit"])

    def test_actual_model_item_uses_its_own_latency_not_first_stdout_latency(self):
        root = self.make_root()
        execution = self.execution(latency=0.01)
        execution.time_to_first_model_event_seconds = 0.75

        result = run_health_probe(
            root,
            "luna-model-latency",
            executor=self.fake_executor('{"status":"ok"}', execution=execution),
            runtime_metadata_provider=lambda **_kwargs: self.complete_metadata(),
        )

        receipt = self.receipt(root, "luna-model-latency")
        self.assertEqual(0, result)
        self.assertEqual(0.01, receipt["time_to_first_stdout_event_seconds"])
        self.assertEqual(0.75, receipt["first_model_event_latency_seconds"])

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
        receipt_path = self.receipt_path(root, "failed-probe")
        receipt_path.parent.mkdir(parents=True)
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
            launch_enterprise_ab_if_probe_passes(
                root, "failed-probe", lambda: launches.append(True)
            )

        self.assertEqual([], launches)

    def test_gate_ignores_caller_selected_receipt_outside_diagnostics_tree(self):
        root = self.make_root()
        rogue = root / "rogue-receipt.json"
        rogue.write_text(
            json.dumps(
                {
                    "diagnostic_type": "model_health_probe",
                    "status": "passed",
                    "within_total_timeout": True,
                    "terminal_json_valid": True,
                    "first_model_event_within_limit": True,
                    "runtime_metadata_complete": True,
                    "process_cleanup_passed": True,
                }
            ),
            encoding="utf-8",
        )
        launches = []

        with self.assertRaises(HealthProbeGateError):
            launch_enterprise_ab_if_probe_passes(
                root, "missing-expected-run", lambda: launches.append(True)
            )

        self.assertEqual([], launches)

    def test_gate_recomputes_facts_instead_of_trusting_pass_booleans(self):
        root = self.make_root()
        receipt_path = self.make_passing_probe(root, "luna-forged-summary")
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        receipt.update(
            {
                "status": "passed",
                "within_total_timeout": True,
                "terminal_json_valid": True,
                "first_model_event_within_limit": True,
                "runtime_metadata_complete": True,
                "process_cleanup_passed": True,
                "model": "gpt-5.6-terra",
                "process_exit_code": 1,
                "failures": ["forged receipt ignored this failure"],
                "canonical_coverage_eligible": True,
            }
        )
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        launches = []

        with self.assertRaises(HealthProbeGateError):
            launch_enterprise_ab_if_probe_passes(
                root, "luna-forged-summary", lambda: launches.append(True)
            )

        self.assertEqual([], launches)

    def test_gate_rejects_receipt_published_after_deadline(self):
        root = self.make_root()
        receipt_path = self.make_passing_probe(root, "luna-late-receipt-gate")
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        receipt["receipt_published_within_deadline"] = False
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")

        with self.assertRaises(HealthProbeGateError):
            launch_enterprise_ab_if_probe_passes(
                root, "luna-late-receipt-gate", lambda: self.fail("must not launch")
            )

    def test_gate_rejects_forged_model_and_process_timing_progress(self):
        root = self.make_root()
        self.make_passing_probe(root, "luna-forged-runtime-timing")
        progress_path = (
            root
            / "tracking/ingest/metronome/pilot/diagnostics/health-probes"
            / "luna-forged-runtime-timing/attempt-1/progress.jsonl"
        )
        records = [json.loads(line) for line in progress_path.read_text().splitlines()]
        for record in records:
            if record.get("event") == "first_model_event":
                record["elapsed_seconds"] = 45.0
        progress_path.write_text(
            "".join(json.dumps(record) + "\n" for record in records), encoding="utf-8"
        )

        with self.assertRaises(HealthProbeGateError):
            launch_enterprise_ab_if_probe_passes(
                root, "luna-forged-runtime-timing", lambda: self.fail("must not launch")
            )

    def test_gate_rejects_artifact_and_provenance_tampering(self):
        root = self.make_root()
        receipt_path = self.make_passing_probe(root, "luna-tampered-artifact")
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        raw_output = root / receipt["output_path"]
        raw_output.write_text('{"status":"tampered"}', encoding="utf-8")

        with self.assertRaises(HealthProbeGateError):
            launch_enterprise_ab_if_probe_passes(
                root, "luna-tampered-artifact", lambda: None
            )

    def test_gate_rejects_run_id_mismatch_and_leftover_tmp_receipt(self):
        root = self.make_root()
        receipt_path = self.make_passing_probe(root, "luna-atomic-gate")
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        receipt["run_id"] = "different-run"
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        receipt_path.with_name(f"{receipt_path.name}.tmp").write_text(
            "incomplete", encoding="utf-8"
        )

        with self.assertRaises(HealthProbeGateError):
            launch_enterprise_ab_if_probe_passes(root, "luna-atomic-gate", lambda: None)

    def test_gate_launches_only_after_recomputing_a_valid_expected_run(self):
        root = self.make_root()
        self.make_passing_probe(root, "luna-valid-gate")
        launches = []

        result = launch_enterprise_ab_if_probe_passes(
            root, "luna-valid-gate", lambda: launches.append("launched") or 17
        )

        self.assertEqual(17, result)
        self.assertEqual(["launched"], launches)

    def test_missing_prompt_after_run_claim_publishes_terminal_failure_receipt(self):
        root = self.make_root()
        (
            root / "tracking/ingest/metronome/pilot/prompts/model-health-probe.md"
        ).unlink()

        result = run_health_probe(
            root,
            "luna-missing-prompt",
            executor=lambda *_args, **_kwargs: self.fail("executor must not launch"),
            runtime_metadata_provider=lambda **_kwargs: self.fail(
                "metadata preflight must not run"
            ),
        )

        receipt_path = self.receipt_path(root, "luna-missing-prompt")
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        self.assertEqual(1, result)
        self.assertEqual("failed", receipt["status"])
        self.assertTrue(any("setup failed" in item for item in receipt["failures"]))
        self.assertFalse(receipt_path.with_name(f"{receipt_path.name}.tmp").exists())

    def test_attempt_directory_creation_race_publishes_terminal_failure_receipt(self):
        root = self.make_root()
        run_id = "luna-attempt-race"
        probe_dir = (
            root
            / "tracking/ingest/metronome/pilot/diagnostics/health-probes"
            / run_id
        )
        real_mkdir = Path.mkdir

        def racing_mkdir(path, *args, **kwargs):
            if Path(path).name == "attempt-1":
                raise FileExistsError("simulated attempt-1 creation race")
            return real_mkdir(path, *args, **kwargs)

        with patch.object(
            type(probe_dir), "mkdir", autospec=True, side_effect=racing_mkdir
        ):
            result = run_health_probe(
                root,
                run_id,
                executor=lambda *_args, **_kwargs: self.fail("executor must not launch"),
                runtime_metadata_provider=lambda **_kwargs: self.fail(
                    "metadata preflight must not run"
                ),
            )

        receipt = self.receipt(root, run_id)
        self.assertEqual(1, result)
        self.assertEqual("failed", receipt["status"])
        self.assertTrue(
            any("bootstrap failed" in item for item in receipt["failures"]),
            receipt["failures"],
        )
        self.assertFalse(
            self.receipt_path(root, run_id)
            .with_name("model-health-probe-receipt.json.tmp")
            .exists()
        )

    def test_late_progress_failure_uses_outer_terminal_receipt_boundary(self):
        root = self.make_root()
        run_id = "luna-progress-failure"
        real_append = __import__(
            "run_metronome_model_health_probe"
        ).append_progress_event

        def fail_classification(path, event, **details):
            if event == "model_activity_classified":
                raise OSError("progress storage interrupted")
            return real_append(path, event, **details)

        with patch(
            "run_metronome_model_health_probe.append_progress_event",
            side_effect=fail_classification,
        ):
            result = run_health_probe(
                root,
                run_id,
                executor=self.fake_executor('{"status":"ok"}'),
                runtime_metadata_provider=lambda **_kwargs: self.complete_metadata(),
            )

        receipt = self.receipt(root, run_id)
        self.assertEqual(1, result)
        self.assertEqual("failed", receipt["status"])
        self.assertTrue(
            any("progress storage interrupted" in item for item in receipt["failures"])
        )
        self.assertFalse(receipt["canonical_coverage_eligible"])

    def test_codex_home_setup_failure_after_claim_publishes_terminal_receipt(self):
        root = self.make_root()

        with patch(
            "run_metronome_model_health_probe.prepare_minimal_codex_home",
            side_effect=OSError("home unavailable"),
        ):
            result = run_health_probe(
                root,
                "luna-home-failure",
                executor=lambda *_args, **_kwargs: self.fail("executor must not launch"),
                runtime_metadata_provider=lambda **_kwargs: self.fail(
                    "metadata preflight must not run"
                ),
            )

        receipt = self.receipt(root, "luna-home-failure")
        self.assertEqual(1, result)
        self.assertEqual("failed", receipt["status"])
        self.assertIsNone(receipt["process_exit_code"])
        self.assertTrue(any("home unavailable" in item for item in receipt["failures"]))

    def test_metadata_and_process_share_one_absolute_monotonic_deadline(self):
        root = self.make_root()
        clock = self.FakeClock()
        observed = {}

        def metadata_provider(**kwargs):
            observed["metadata_deadline"] = kwargs.get("deadline_monotonic")
            clock.advance(2)
            return self.complete_metadata()

        def executor(command, **kwargs):
            observed["process_deadline"] = kwargs.get("absolute_deadline")
            clock.advance(3)
            return self.fake_executor('{"status":"ok"}')(command, **kwargs)

        with patch("run_metronome_model_health_probe.time.monotonic", side_effect=clock):
            result = run_health_probe(
                root,
                "luna-one-deadline",
                executor=executor,
                runtime_metadata_provider=metadata_provider,
            )

        receipt = self.receipt(root, "luna-one-deadline")
        self.assertEqual(0, result)
        self.assertEqual(60.0, observed["metadata_deadline"])
        self.assertEqual(observed["metadata_deadline"], observed["process_deadline"])
        self.assertEqual(60.0, receipt["deadline_monotonic"])
        self.assertTrue(receipt["receipt_published_within_deadline"])

    def test_receipt_publication_crossing_deadline_is_truthful_terminal_failure(self):
        root = self.make_root()
        clock = self.FakeClock()
        real_atomic_write = __import__(
            "run_metronome_model_health_probe"
        ).write_json_atomic

        def slow_receipt_write(path, payload):
            real_atomic_write(path, payload)
            if Path(path).name == "model-health-probe-receipt.json":
                clock.advance(0.3)

        with patch("run_metronome_model_health_probe.time.monotonic", side_effect=clock), patch(
            "run_metronome_model_health_probe.write_json_atomic",
            side_effect=slow_receipt_write,
        ):
            result = run_health_probe(
                root,
                "luna-late-publication",
                executor=self.fake_executor('{"status":"ok"}'),
                runtime_metadata_provider=lambda **_kwargs: self.complete_metadata(0.2),
                total_timeout_seconds=0.2,
            )

        receipt = self.receipt(root, "luna-late-publication")
        self.assertEqual(1, result)
        self.assertEqual("failed", receipt["status"])
        self.assertFalse(receipt["receipt_published_within_deadline"])
        self.assertTrue(any("deadline" in item for item in receipt["failures"]))

    def test_normalization_failure_after_claim_still_publishes_failed_receipt(self):
        root = self.make_root()
        real_atomic_write = __import__(
            "run_metronome_model_health_probe"
        ).write_json_atomic

        def fail_normalization(path, payload):
            if Path(path).name == "model-output.normalized.json":
                raise OSError("normalization storage failed")
            real_atomic_write(path, payload)

        with patch(
            "run_metronome_model_health_probe.write_json_atomic",
            side_effect=fail_normalization,
        ):
            result = run_health_probe(
                root,
                "luna-normalization-failure",
                executor=self.fake_executor('{"status":"ok"}'),
                runtime_metadata_provider=lambda **_kwargs: self.complete_metadata(),
            )

        receipt = self.receipt(root, "luna-normalization-failure")
        self.assertEqual(1, result)
        self.assertEqual("failed", receipt["status"])
        self.assertTrue(
            any("normalization storage failed" in item for item in receipt["failures"])
        )

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
        self.assertEqual("string", schema["properties"]["status"]["type"])
        self.assertIn("enterprise A/B remains suspended", manifest)
        self.assertIn("never participates in canonical coverage", manifest)


if __name__ == "__main__":
    unittest.main()
