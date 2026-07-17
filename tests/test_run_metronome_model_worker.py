import json
import hashlib
import os
import signal
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from run_metronome_model_worker import (  # noqa: E402
    INLINE_RAW_END_DELIMITER,
    INLINE_RAW_START_DELIMITER,
    build_runtime_metadata,
    build_codex_command,
    build_page_profile,
    common_git_dir,
    recover_attempt,
    render_worker_prompt,
    repair_mandatory_tags,
    repair_raw_link,
    repair_quote_bounds,
    run_process_in_new_group,
    run_worker,
)
from metronome_model_runtime import (  # noqa: E402
    job_lock,
    resolve_run_dir,
    terminate_process_group,
    validate_run_id,
    write_json_atomic,
)


def _pid_is_alive(pid):
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    return True


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

    def test_render_worker_prompt_rejects_unknown_input_mode(self):
        with self.assertRaisesRegex(ValueError, "unsupported input_mode"):
            render_worker_prompt(
                "template", self.valid_job(), {}, "raw evidence", "unknown-mode"
            )

    def test_input_modes_preserve_substantive_worker_requirements(self):
        job = self.valid_job()
        profile = build_page_profile("# Alpha\nPOST /v1/events\nrequired when enabled\n")
        profile["existing_metronome_concept_slugs"] = ["metronome-events"]
        template = (ROOT / "tracking/ingest/metronome/pilot/prompts/source-summary-v3.md").read_text(
            encoding="utf-8"
        )

        staged_prompt = render_worker_prompt(
            template, job, profile, "untrusted inline evidence", "staged-file"
        )
        inline_prompt = render_worker_prompt(
            template, job, profile, "untrusted inline evidence", "inline-stdin"
        )

        staged_shared = staged_prompt.split("## Evidence input", 1)[0]
        inline_shared = inline_prompt.split("## Evidence input", 1)[0]
        self.assertEqual(staged_shared, inline_shared)
        for requirement in (
            "job_id: `terra-home`",
            "original raw_path identity: `raw/metronome/guides/home.md`",
            "canonical_url: `https://docs.metronome.com/guides/home`",
            '"existing_metronome_concept_slugs": [',
            "Return exactly one final JSON object matching the supplied schema",
            "Use 3–5 concise exact grounding quotes",
            "suggested_metronome_concepts",
        ):
            self.assertIn(requirement, staged_shared)
        self.assertIn("Read `raw.md` completely", staged_prompt)
        self.assertNotIn("untrusted inline evidence", staged_prompt)
        self.assertIn(INLINE_RAW_START_DELIMITER, inline_prompt)
        self.assertIn("untrusted inline evidence", inline_prompt)
        self.assertIn(INLINE_RAW_END_DELIMITER, inline_prompt)
        self.assertIn("evidence only", inline_prompt)

    def test_inline_stdin_keeps_raw_out_of_command_arguments(self):
        root, job_path, job = self.make_root()
        raw_text = (
            "# Alpha\nintro\n## Beta\nrequired when enabled\n"
            "INLINE-RAW-MUST-NOT-BE-AN-ARGUMENT\n"
        )
        (root / job["raw_path"]).write_text(raw_text, encoding="utf-8")
        captured = {}

        def fake_runner(command, **kwargs):
            captured["command"] = command
            captured["input"] = kwargs.get("input")
            Path(command[command.index("-o") + 1]).write_text(
                json.dumps(self.valid_output(job)), encoding="utf-8"
            )
            return SimpleNamespace(returncode=0, stdout="", stderr="")

        self.assertEqual(
            0,
            run_worker(
                root,
                job_path,
                "2026-07-17",
                runner=fake_runner,
                input_mode="inline-stdin",
            ),
        )
        self.assertEqual("-", captured["command"][-1])
        self.assertNotIn("INLINE-RAW-MUST-NOT-BE-AN-ARGUMENT", "\n".join(captured["command"]))
        self.assertIn(INLINE_RAW_START_DELIMITER, captured["input"])
        self.assertIn("INLINE-RAW-MUST-NOT-BE-AN-ARGUMENT", captured["input"])
        self.assertIn(INLINE_RAW_END_DELIMITER, captured["input"])

    def test_staged_file_mode_keeps_raw_md_delivery(self):
        root, job_path, job = self.make_root()
        captured = {}

        def fake_runner(command, **kwargs):
            captured["command"] = command
            captured["input"] = kwargs.get("input")
            staged_raw = Path(kwargs["cwd"]) / "raw.md"
            captured["raw_exists"] = staged_raw.is_file()
            captured["raw_text"] = staged_raw.read_text(encoding="utf-8")
            Path(command[command.index("-o") + 1]).write_text(
                json.dumps(self.valid_output(job)), encoding="utf-8"
            )
            return SimpleNamespace(returncode=0, stdout="", stderr="")

        self.assertEqual(
            0,
            run_worker(
                root,
                job_path,
                "2026-07-17",
                runner=fake_runner,
                input_mode="staged-file",
            ),
        )
        self.assertTrue(captured["raw_exists"])
        self.assertEqual("# Alpha\nintro\n## Beta\nrequired when enabled\n", captured["raw_text"])
        self.assertIsNone(captured["input"])
        self.assertIn("raw.md", captured["command"][-1])

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

    def test_streaming_attempt_files_are_visible_before_process_exit(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        attempt_dir = root / "attempt-1"
        release_path = root / "release"
        command = [
            sys.executable,
            "-c",
            (
                "import os, pathlib, sys, time\n"
                "os.write(sys.stdout.fileno(), b'{\"type\":\"thread.started\"}\\n')\n"
                "os.write(sys.stderr.fileno(), b'booting\\n')\n"
                "release = pathlib.Path(sys.argv[1])\n"
                "deadline = time.monotonic() + 5\n"
                "while not release.exists() and time.monotonic() < deadline:\n"
                "    time.sleep(0.01)\n"
            ),
            str(release_path),
        ]
        result_box = []

        thread = threading.Thread(
            target=lambda: result_box.append(
                run_process_in_new_group(
                    command,
                    cwd=root,
                    timeout=5,
                    env=os.environ.copy(),
                    attempt_dir=attempt_dir,
                )
            )
        )
        thread.start()
        self.addCleanup(lambda: release_path.touch(exist_ok=True))
        deadline = time.monotonic() + 2
        while time.monotonic() < deadline:
            if (
                (attempt_dir / "events.jsonl").read_bytes()
                if (attempt_dir / "events.jsonl").is_file()
                else b""
            ) and (
                (attempt_dir / "stderr.log").read_bytes()
                if (attempt_dir / "stderr.log").is_file()
                else b""
            ) and (attempt_dir / "progress.jsonl").is_file():
                break
            time.sleep(0.01)

        self.assertTrue(thread.is_alive(), "fake process exited before live files were observed")
        self.assertEqual(
            b'{"type":"thread.started"}\n',
            (attempt_dir / "events.jsonl").read_bytes(),
        )
        self.assertEqual(b"booting\n", (attempt_dir / "stderr.log").read_bytes())
        progress = [
            json.loads(line)
            for line in (attempt_dir / "progress.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertIn("process_started", [item["event"] for item in progress])
        self.assertIn("first_stdout_event", [item["event"] for item in progress])
        self.assertIn("first_stderr_byte", [item["event"] for item in progress])

        release_path.touch()
        thread.join(timeout=2)
        self.assertFalse(thread.is_alive())
        self.assertEqual(0, result_box[0].returncode)

    def test_streaming_attempt_accounts_for_events_bytes_usage_and_truncated_final_line(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        attempt_dir = root / "attempt-1"
        complete = b'{"type":"thread.started"}\n{"usage":{"input_tokens":3,"output_tokens":2}}\n'
        truncated = b'{"type":"turn.completed"'
        stderr = b"warning: \xff\n"
        command = [
            sys.executable,
            "-c",
            (
                "import os, sys, time; time.sleep(0.02); "
                f"os.write(sys.stdout.fileno(), {complete + truncated!r}); "
                f"os.write(sys.stderr.fileno(), {stderr!r})"
            ),
        ]

        result = run_process_in_new_group(
            command,
            cwd=root,
            timeout=2,
            env=os.environ.copy(),
            attempt_dir=attempt_dir,
        )

        self.assertEqual(0, result.returncode)
        self.assertEqual(len(complete + truncated), result.streamed_stdout_bytes)
        self.assertEqual(len(stderr), result.streamed_stderr_bytes)
        self.assertEqual(2, result.parsed_event_count)
        self.assertEqual(1, result.truncated_line_count)
        self.assertGreaterEqual(result.time_to_first_stdout_event_seconds, 0)
        self.assertLessEqual(result.time_to_first_stdout_event_seconds, result.elapsed_seconds)
        self.assertGreaterEqual(result.time_to_first_stderr_byte_seconds, 0)
        self.assertLessEqual(result.time_to_first_stderr_byte_seconds, result.elapsed_seconds)
        self.assertEqual({"input_tokens": 3, "output_tokens": 2}, result.token_usage)
        self.assertEqual(complete + truncated, (attempt_dir / "events.jsonl").read_bytes())
        self.assertEqual(stderr, (attempt_dir / "stderr.log").read_bytes())

    def test_timeout_survives_leader_exit_and_kills_child_holding_inherited_pipes(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        child_pid_path = root / "child.pid"
        parent_code = (
            "import pathlib, subprocess, sys; "
            "child = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(2)']); "
            "pathlib.Path(sys.argv[1]).write_text(str(child.pid), encoding='utf-8')"
        )
        started = time.monotonic()

        result = run_process_in_new_group(
            [sys.executable, "-c", parent_code, str(child_pid_path)],
            cwd=root,
            timeout=0.1,
            env=os.environ.copy(),
            attempt_dir=root / "attempt-1",
        )
        elapsed = time.monotonic() - started
        child_pid = int(child_pid_path.read_text(encoding="utf-8"))
        self.addCleanup(
            lambda: os.kill(child_pid, signal.SIGKILL)
            if _pid_is_alive(child_pid)
            else None
        )

        self.assertEqual(124, result.returncode)
        self.assertLess(elapsed, 1.0)
        deadline = time.monotonic() + 1
        while _pid_is_alive(child_pid) and time.monotonic() < deadline:
            time.sleep(0.01)
        self.assertFalse(_pid_is_alive(child_pid), "timeout left inherited-pipe child alive")
        self.assertIsNotNone(result.termination)

    def test_term_handler_output_larger_than_pipe_capacity_is_drained_without_kill(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        payload_size = 256 * 1024
        child_code = (
            "import os, signal, sys, time\n"
            f"payload = b'x' * {payload_size}\n"
            "def handle_term(_signal, _frame):\n"
            "    offset = 0\n"
            "    while offset < len(payload):\n"
            "        offset += os.write(sys.stdout.fileno(), payload[offset:])\n"
            "    raise SystemExit(0)\n"
            "signal.signal(signal.SIGTERM, handle_term)\n"
            "while True:\n"
            "    time.sleep(1)\n"
        )

        from unittest.mock import patch
        with patch(
            "run_metronome_model_worker.terminate_process_group",
            side_effect=lambda process: terminate_process_group(process, grace_seconds=0.2),
        ):
            result = run_process_in_new_group(
                [sys.executable, "-c", child_code],
                cwd=root,
                timeout=0.1,
                env=os.environ.copy(),
                attempt_dir=root / "attempt-1",
            )

        self.assertEqual(124, result.returncode)
        self.assertEqual(payload_size, result.streamed_stdout_bytes)
        self.assertEqual(b"x" * payload_size, (root / "attempt-1/events.jsonl").read_bytes())
        self.assertEqual("terminated", result.termination["grace_outcome"])
        self.assertIsNone(result.termination["escalation_signal"])

    def test_runtime_metadata_hashes_all_inputs_and_records_version_and_timeout(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        executable = root / "fake-codex"
        executable_bytes = b"#!/bin/sh\nprintf 'codex-cli test-version\\n'\n"
        executable.write_bytes(executable_bytes)
        executable.chmod(0o755)
        schema_path = root / "schema.json"
        schema_bytes = b'{"type":"object"}\n'
        schema_path.write_bytes(schema_bytes)
        raw_bytes = b"raw evidence\n"
        template_bytes = b"template {{ job }}\n"
        rendered_prompt = "rendered prompt\n"

        metadata = build_runtime_metadata(
            raw_bytes=raw_bytes,
            prompt_template_bytes=template_bytes,
            rendered_prompt=rendered_prompt,
            schema_path=schema_path,
            codex_executable=str(executable),
            timeout_seconds=37,
            env=os.environ.copy(),
        )

        self.assertEqual(
            {
                "raw_text": hashlib.sha256(raw_bytes).hexdigest(),
                "prompt_template": hashlib.sha256(template_bytes).hexdigest(),
                "rendered_prompt": hashlib.sha256(rendered_prompt.encode("utf-8")).hexdigest(),
                "output_schema": hashlib.sha256(schema_bytes).hexdigest(),
                "codex_executable": hashlib.sha256(executable_bytes).hexdigest(),
            },
            metadata["sha256"],
        )
        self.assertEqual(str(executable.resolve()), metadata["codex_executable"])
        self.assertEqual("codex-cli test-version", metadata["codex_cli_version"])
        self.assertEqual(37, metadata["timeout_seconds"])

    def test_diagnostic_receipt_includes_streaming_lifecycle_and_runtime_metadata(self):
        root, job_path, job = self.make_root()
        stdout_text = '{"usage":{"input_tokens":3}}\n{"partial":'
        metadata = {
            "sha256": {
                "raw_text": "a",
                "prompt_template": "b",
                "rendered_prompt": "c",
                "output_schema": "d",
                "codex_executable": "e",
            },
            "codex_executable": "/fake/codex",
            "codex_cli_version": "codex-cli test",
            "timeout_seconds": 900,
        }

        def fake_runner(command, **kwargs):
            Path(command[command.index("-o") + 1]).write_text(
                json.dumps(self.valid_output(job)), encoding="utf-8"
            )
            return SimpleNamespace(
                returncode=0,
                stdout=stdout_text,
                stderr="warning",
            )

        self.assertEqual(
            0,
            run_worker(
                root,
                job_path,
                "2026-07-17",
                runner=fake_runner,
                run_id="terra-streaming",
                runtime_metadata_provider=lambda **_kwargs: metadata,
            ),
        )

        run_dir = resolve_run_dir(root, job, "terra-streaming")
        receipt = json.loads((run_dir / "model-worker-receipt.json").read_text(encoding="utf-8"))
        attempt = receipt["attempts"][0]
        self.assertEqual(metadata, attempt["runtime_metadata"])
        self.assertEqual(metadata, receipt["runtime_metadata"])
        self.assertEqual(1, attempt["parsed_event_count"])
        self.assertEqual(1, attempt["truncated_line_count"])
        self.assertEqual(len(stdout_text.encode("utf-8")), attempt["streamed_stdout_bytes"])
        progress = [
            json.loads(line)
            for line in (run_dir / "attempt-1/progress.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertIn("lock_acquired", [item["event"] for item in progress])
        self.assertIn("validation_completed", [item["event"] for item in progress])
        self.assertIn("receipt_published", [item["event"] for item in progress])

    def test_injected_runner_uses_metadata_provider_without_real_codex_or_path(self):
        root, job_path, job = self.make_root()
        metadata = {
            "sha256": {
                "raw_text": "a",
                "prompt_template": "b",
                "rendered_prompt": "c",
                "output_schema": "d",
                "codex_executable": "e",
            },
            "codex_executable": "/deterministic/fake-codex",
            "codex_cli_version": "codex-cli deterministic",
            "timeout_seconds": 900,
        }
        provider_calls = []

        def metadata_provider(**kwargs):
            provider_calls.append(kwargs)
            return metadata

        def fake_runner(command, **_kwargs):
            Path(command[command.index("-o") + 1]).write_text(
                json.dumps(self.valid_output(job)), encoding="utf-8"
            )
            return SimpleNamespace(returncode=0, stdout="", stderr="")

        from unittest.mock import patch
        with patch.dict(os.environ, {"PATH": ""}), patch(
            "run_metronome_model_worker.build_runtime_metadata",
            side_effect=AssertionError("injected runner must not probe real Codex"),
        ):
            self.assertEqual(
                0,
                run_worker(
                    root,
                    job_path,
                    "2026-07-17",
                    runner=fake_runner,
                    run_id="terra-injected",
                    runtime_metadata_provider=metadata_provider,
                ),
            )

        self.assertEqual(1, len(provider_calls))
        receipt = json.loads(
            (
                resolve_run_dir(root, job, "terra-injected")
                / "model-worker-receipt.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(metadata, receipt["runtime_metadata"])

    def test_job_lock_is_shared_across_worktrees_but_not_jobs(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        shared_git_dir = Path(tmp.name) / "repository.git"
        worktree_a = Path(tmp.name) / "worktree-a"
        worktree_b = Path(tmp.name) / "worktree-b"
        worktree_a.mkdir()
        worktree_b.mkdir()

        from unittest.mock import patch
        with patch(
            "run_metronome_model_worker.subprocess.check_output",
            side_effect=[f"{shared_git_dir}\n", f"{shared_git_dir}\n"],
        ):
            resolved_a = common_git_dir(worktree_a)
            resolved_b = common_git_dir(worktree_b)

        self.assertEqual(shared_git_dir, resolved_a)
        self.assertEqual(resolved_a, resolved_b)
        with job_lock(resolved_a, "metronome", "terra-home"):
            script = (
                "import sys\n"
                "from pathlib import Path\n"
                f"sys.path.insert(0, {str(SCRIPTS)!r})\n"
                "from metronome_model_runtime import job_lock\n"
                "with job_lock(Path(sys.argv[1]), 'metronome', sys.argv[2]):\n"
                "    pass\n"
            )
            duplicate = subprocess.run(
                [sys.executable, "-c", script, str(resolved_b), "terra-home"],
                cwd=worktree_b,
                capture_output=True,
                text=True,
            )
            unrelated = subprocess.run(
                [sys.executable, "-c", script, str(resolved_b), "terra-other"],
                cwd=worktree_b,
                capture_output=True,
                text=True,
            )

        self.assertNotEqual(worktree_a, worktree_b)
        self.assertNotEqual(0, duplicate.returncode)
        self.assertIn("already locked", duplicate.stderr)
        self.assertEqual(0, unrelated.returncode)

        self.assertTrue((shared_git_dir / "metronome-model-locks").is_dir())

    def test_job_lock_is_kernel_released_without_deleting_its_lock_file(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        common_git_dir = Path(tmp.name) / "repository.git"

        with job_lock(common_git_dir, "metronome", "terra-home") as lock_path:
            self.assertTrue(lock_path.is_file())
        self.assertTrue(lock_path.is_file())
        with job_lock(common_git_dir, "metronome", "terra-home"):
            pass
        self.assertTrue(lock_path.is_file())

    def test_timeout_cleanup_terms_then_kills_the_whole_process_group(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        child_pid_path = Path(tmp.name) / "child.pid"
        child_code = (
            "import signal, time; "
            "signal.signal(signal.SIGTERM, signal.SIG_IGN); "
            "time.sleep(30)"
        )
        parent_code = (
            "import pathlib, signal, subprocess, sys, time; "
            "signal.signal(signal.SIGTERM, signal.SIG_IGN); "
            "child = subprocess.Popen([sys.executable, '-c', sys.argv[2]]); "
            "pathlib.Path(sys.argv[1]).write_text(str(child.pid), encoding='utf-8'); "
            "time.sleep(30)"
        )
        process = subprocess.Popen(
            [sys.executable, "-c", parent_code, str(child_pid_path), child_code],
            start_new_session=True,
        )
        self.addCleanup(
            lambda: terminate_process_group(process, grace_seconds=0.01)
            if process.poll() is None
            else None
        )
        deadline = time.monotonic() + 2
        while not child_pid_path.is_file() and time.monotonic() < deadline:
            time.sleep(0.01)
        self.assertTrue(child_pid_path.is_file())
        child_pid = int(child_pid_path.read_text(encoding="utf-8"))

        def force_group_cleanup():
            try:
                os.killpg(os.getpgid(child_pid), signal.SIGKILL)
            except ProcessLookupError:
                pass

        self.addCleanup(force_group_cleanup)

        termination = terminate_process_group(process, grace_seconds=0.05)

        self.assertEqual("SIGTERM", termination["signal"])
        self.assertEqual("killed", termination["grace_outcome"])
        self.assertEqual("SIGKILL", termination["escalation_signal"])
        self.assertIsNotNone(termination["final_return_code"])
        deadline = time.monotonic() + 2
        while time.monotonic() < deadline:
            try:
                os.kill(child_pid, 0)
            except ProcessLookupError:
                break
            time.sleep(0.02)
        else:
            self.fail("process-group cleanup left a descendant alive")

    def test_term_honoring_process_group_finishes_during_grace(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        child_pid_path = Path(tmp.name) / "child.pid"
        parent_code = (
            "import pathlib, subprocess, sys, time; "
            "child = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(30)']); "
            "pathlib.Path(sys.argv[1]).write_text(str(child.pid), encoding='utf-8'); "
            "time.sleep(30)"
        )
        process = subprocess.Popen(
            [sys.executable, "-c", parent_code, str(child_pid_path)],
            start_new_session=True,
        )
        self.addCleanup(
            lambda: terminate_process_group(process, grace_seconds=0.01)
            if process.poll() is None
            else None
        )
        deadline = time.monotonic() + 2
        while not child_pid_path.is_file() and time.monotonic() < deadline:
            time.sleep(0.01)
        self.assertTrue(child_pid_path.is_file())
        child_pid = int(child_pid_path.read_text(encoding="utf-8"))

        self.addCleanup(
            lambda: os.kill(child_pid, signal.SIGKILL)
            if _pid_is_alive(child_pid)
            else None
        )

        termination = terminate_process_group(process, grace_seconds=0.05)

        self.assertEqual("terminated", termination["grace_outcome"])
        self.assertIsNone(termination["escalation_signal"])
        self.assertIsNotNone(termination["final_return_code"])
        deadline = time.monotonic() + 2
        while time.monotonic() < deadline:
            try:
                os.kill(child_pid, 0)
            except ProcessLookupError:
                break
            time.sleep(0.02)
        else:
            self.fail("TERM-honoring cleanup left a descendant alive")

    def test_live_timeout_is_logical_124_and_does_not_retry(self):
        root, job_path, job = self.make_root()
        job["timeout_seconds"] = 1
        job_path.write_text(json.dumps(job), encoding="utf-8")
        command = [
            sys.executable,
            "-c",
            "import signal, time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(30)",
        ]

        from unittest.mock import patch
        with patch("run_metronome_model_worker.build_codex_command", return_value=command), patch(
            "run_metronome_model_worker.terminate_process_group",
            side_effect=lambda process: terminate_process_group(process, grace_seconds=0.05),
        ):
            self.assertEqual(
                1,
                run_worker(root, job_path, "2026-07-17", run_id="terra-timeout"),
            )

        receipt_path = resolve_run_dir(root, job, "terra-timeout") / "model-worker-receipt.json"
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        self.assertEqual("failed", receipt["status"])
        self.assertEqual(1, receipt["attempt_count"])
        self.assertEqual(124, receipt["process_exit_code"])
        self.assertEqual(124, receipt["attempts"][0]["process_exit_code"])
        self.assertEqual("killed", receipt["termination"]["grace_outcome"])
        self.assertLess(receipt["termination"]["final_return_code"], 0)

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
