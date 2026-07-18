import json
import os
import signal
import subprocess
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

import metronome_model_runtime as runtime  # noqa: E402


def _pid_is_alive(pid):
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    return True


class ProcessGroupInterruptionTests(unittest.TestCase):
    def _spawn_leader_that_exits_with_term_ignoring_descendant(self, root):
        child_pid_path = root / "descendant.pid"
        child_ready_path = root / "descendant-ready"
        child_code = (
            "import pathlib, signal, sys, time; "
            "signal.signal(signal.SIGTERM, signal.SIG_IGN); "
            "pathlib.Path(sys.argv[1]).write_text('ready', encoding='utf-8'); "
            "time.sleep(30)"
        )
        leader_code = (
            "import pathlib, subprocess, sys; "
            "child = subprocess.Popen([sys.executable, '-c', sys.argv[2], sys.argv[3]]); "
            "pathlib.Path(sys.argv[1]).write_text(str(child.pid), encoding='utf-8')"
        )
        process = subprocess.Popen(
            [
                sys.executable,
                "-c",
                leader_code,
                str(child_pid_path),
                child_code,
                str(child_ready_path),
            ],
            start_new_session=True,
        )
        deadline = time.monotonic() + 2
        while (
            not (child_pid_path.is_file() and child_ready_path.is_file())
            and time.monotonic() < deadline
        ):
            time.sleep(0.01)
        self.assertTrue(child_pid_path.is_file())
        self.assertTrue(child_ready_path.is_file())
        child_pid = int(child_pid_path.read_text(encoding="utf-8"))
        process.wait(timeout=2)
        self.assertIsNotNone(process.poll(), "leader must have exited before cleanup")
        self.assertTrue(_pid_is_alive(child_pid), "descendant must still be running")
        return process, child_pid

    def _assert_descendant_exited(self, child_pid):
        deadline = time.monotonic() + 2
        while _pid_is_alive(child_pid) and time.monotonic() < deadline:
            time.sleep(0.01)
        self.assertFalse(_pid_is_alive(child_pid), "process-group cleanup left a descendant alive")

    @staticmethod
    def _force_group_cleanup(child_pid):
        try:
            os.killpg(os.getpgid(child_pid), signal.SIGKILL)
        except ProcessLookupError:
            pass

    @staticmethod
    def _force_process_group_cleanup(process_group):
        try:
            os.killpg(process_group, signal.SIGKILL)
        except ProcessLookupError:
            pass

    def test_terminate_process_group_cleans_descendant_after_leader_exits(self):
        with tempfile.TemporaryDirectory() as directory:
            process, child_pid = self._spawn_leader_that_exits_with_term_ignoring_descendant(
                Path(directory)
            )
            self.addCleanup(self._force_group_cleanup, child_pid)

            termination = runtime.terminate_process_group(process, grace_seconds=0.05)

            self.assertEqual("SIGTERM", termination["signal"])
            self.assertEqual("killed", termination["grace_outcome"])
            self.assertEqual("SIGKILL", termination["escalation_signal"])
            self.assertEqual(process.returncode, termination["final_return_code"])
            self._assert_descendant_exited(child_pid)

    def test_coordinator_interrupt_cleans_group_after_leader_exits(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            child_pid_path = root / "descendant.pid"
            child_ready_path = root / "descendant-ready"
            child_code = (
                "import pathlib, signal, sys, time; "
                "signal.signal(signal.SIGTERM, signal.SIG_IGN); "
                "pathlib.Path(sys.argv[1]).write_text('ready', encoding='utf-8'); "
                "time.sleep(30)"
            )
            leader_code = (
                "import pathlib, subprocess, sys; "
                "child = subprocess.Popen([sys.executable, '-c', sys.argv[2], sys.argv[3]]); "
                "pathlib.Path(sys.argv[1]).write_text(str(child.pid), encoding='utf-8')"
            )
            command = [
                sys.executable,
                "-c",
                leader_code,
                str(child_pid_path),
                child_code,
                str(child_ready_path),
            ]
            created_processes = []
            real_popen = subprocess.Popen
            real_group_exists = runtime._process_group_exists

            def capture_process(*args, **kwargs):
                process = real_popen(*args, **kwargs)
                created_processes.append(process)
                return process

            def interrupt_after_leader_exit(process_group):
                if (
                    created_processes
                    and created_processes[0].poll() is not None
                    and child_ready_path.is_file()
                ):
                    raise KeyboardInterrupt("deterministic coordinator interruption")
                return real_group_exists(process_group)

            with patch(
                "metronome_model_runtime.subprocess.Popen", side_effect=capture_process
            ), patch(
                "metronome_model_runtime._process_group_exists",
                side_effect=interrupt_after_leader_exit,
            ):
                with self.assertRaisesRegex(
                    KeyboardInterrupt, "deterministic coordinator interruption"
                ) as caught:
                    runtime.run_streaming_process(
                        command,
                        cwd=root,
                        timeout=10,
                        env=os.environ.copy(),
                        attempt_dir=root / "attempt-1",
                        termination_grace_seconds=0.05,
                        pipe_cleanup_seconds=0.05,
                    )

            termination = caught.exception.termination
            self.assertIsInstance(termination, dict)
            self.assertEqual(
                termination["final_return_code"], caught.exception.process_exit_code
            )
            self.assertEqual(termination["final_return_code"], caught.exception.returncode)
            progress = [
                json.loads(line)
                for line in (root / "attempt-1/progress.jsonl").read_text().splitlines()
            ]
            cleanup_events = [
                item for item in progress if item["event"] == "interruption_cleanup_completed"
            ]
            self.assertEqual(1, len(cleanup_events))
            self.assertEqual(termination, cleanup_events[0]["termination"])

            self.assertEqual(1, len(created_processes))
            self.assertIsNotNone(created_processes[0].poll())
            self.assertTrue(child_pid_path.is_file())
            self.assertTrue(child_ready_path.is_file())
            child_pid = int(child_pid_path.read_text(encoding="utf-8"))
            self.addCleanup(self._force_group_cleanup, child_pid)
            self._assert_descendant_exited(child_pid)

    def test_interrupt_cleanup_survives_progress_logging_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            child_pid_path = root / "descendant.pid"
            child_ready_path = root / "descendant-ready"
            child_code = (
                "import pathlib, signal, sys, time; "
                "signal.signal(signal.SIGTERM, signal.SIG_IGN); "
                "pathlib.Path(sys.argv[1]).write_text('ready', encoding='utf-8'); "
                "time.sleep(30)"
            )
            leader_code = (
                "import pathlib, subprocess, sys; "
                "child = subprocess.Popen([sys.executable, '-c', sys.argv[2], sys.argv[3]]); "
                "pathlib.Path(sys.argv[1]).write_text(str(child.pid), encoding='utf-8')"
            )
            command = [
                sys.executable,
                "-c",
                leader_code,
                str(child_pid_path),
                child_code,
                str(child_ready_path),
            ]
            created_processes = []
            real_popen = subprocess.Popen
            real_group_exists = runtime._process_group_exists
            real_append_progress_event = runtime.append_progress_event

            def capture_process(*args, **kwargs):
                process = real_popen(*args, **kwargs)
                created_processes.append(process)
                self.addCleanup(self._force_process_group_cleanup, process.pid)
                return process

            def interrupt_after_leader_exit(process_group):
                if (
                    created_processes
                    and created_processes[0].poll() is not None
                    and child_ready_path.is_file()
                ):
                    child_pid = int(child_pid_path.read_text(encoding="utf-8"))
                    self.assertTrue(
                        _pid_is_alive(child_pid), "descendant must be live at interruption"
                    )
                    raise KeyboardInterrupt("deterministic coordinator interruption")
                return real_group_exists(process_group)

            def fail_interruption_progress(path, event, **details):
                if event == "interruption_initiated":
                    raise OSError("progress storage unavailable")
                return real_append_progress_event(path, event, **details)

            with patch(
                "metronome_model_runtime.subprocess.Popen", side_effect=capture_process
            ), patch(
                "metronome_model_runtime._process_group_exists",
                side_effect=interrupt_after_leader_exit,
            ), patch(
                "metronome_model_runtime.append_progress_event",
                side_effect=fail_interruption_progress,
            ):
                with self.assertRaisesRegex(
                    KeyboardInterrupt, "deterministic coordinator interruption"
                ):
                    runtime.run_streaming_process(
                        command,
                        cwd=root,
                        timeout=10,
                        env=os.environ.copy(),
                        attempt_dir=root / "attempt-1",
                        termination_grace_seconds=0.05,
                        pipe_cleanup_seconds=0.05,
                    )

            self.assertEqual(1, len(created_processes))
            self.assertIsNotNone(created_processes[0].poll())
            self.assertTrue(child_pid_path.is_file())
            self.assertTrue(child_ready_path.is_file())
            child_pid = int(child_pid_path.read_text(encoding="utf-8"))
            self.addCleanup(self._force_group_cleanup, child_pid)
            self._assert_descendant_exited(child_pid)

    def test_initial_progress_logging_failure_cleans_process_group(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            child_pid_path = root / "descendant.pid"
            child_ready_path = root / "descendant-ready"
            child_code = (
                "import pathlib, signal, sys, time; "
                "signal.signal(signal.SIGTERM, signal.SIG_IGN); "
                "pathlib.Path(sys.argv[1]).write_text('ready', encoding='utf-8'); "
                "time.sleep(30)"
            )
            leader_code = (
                "import pathlib, subprocess, sys; "
                "child = subprocess.Popen([sys.executable, '-c', sys.argv[2], sys.argv[3]]); "
                "pathlib.Path(sys.argv[1]).write_text(str(child.pid), encoding='utf-8')"
            )
            command = [
                sys.executable,
                "-c",
                leader_code,
                str(child_pid_path),
                child_code,
                str(child_ready_path),
            ]
            created_processes = []
            real_popen = subprocess.Popen

            def capture_process(*args, **kwargs):
                process = real_popen(*args, **kwargs)
                created_processes.append(process)
                self.addCleanup(self._force_process_group_cleanup, process.pid)
                return process

            def fail_initial_progress_after_descendant_starts(path, event, **details):
                self.assertEqual("process_started", event)
                deadline = time.monotonic() + 2
                while (
                    not (child_pid_path.is_file() and child_ready_path.is_file())
                    and time.monotonic() < deadline
                ):
                    time.sleep(0.01)
                self.assertTrue(child_pid_path.is_file())
                self.assertTrue(child_ready_path.is_file())
                child_pid = int(child_pid_path.read_text(encoding="utf-8"))
                self.assertTrue(
                    _pid_is_alive(child_pid), "descendant must be live at logging failure"
                )
                raise OSError("initial progress storage unavailable")

            with patch(
                "metronome_model_runtime.subprocess.Popen", side_effect=capture_process
            ), patch(
                "metronome_model_runtime.append_progress_event",
                side_effect=fail_initial_progress_after_descendant_starts,
            ):
                with self.assertRaisesRegex(OSError, "initial progress storage unavailable"):
                    runtime.run_streaming_process(
                        command,
                        cwd=root,
                        timeout=10,
                        env=os.environ.copy(),
                        attempt_dir=root / "attempt-1",
                        termination_grace_seconds=0.05,
                        pipe_cleanup_seconds=0.05,
                    )

            self.assertEqual(1, len(created_processes))
            self.assertIsNotNone(created_processes[0].poll())
            child_pid = int(child_pid_path.read_text(encoding="utf-8"))
            self.addCleanup(self._force_group_cleanup, child_pid)
            self._assert_descendant_exited(child_pid)


if __name__ == "__main__":
    unittest.main()
