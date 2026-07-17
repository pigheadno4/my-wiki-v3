# Diagnostic Task 2 Report: Cross-worktree Lock and Process-group Cleanup

## Scope

Implemented only Diagnostic Task 2. The change adds common-Git-directory job
locking and process-group TERM/grace/KILL cleanup with diagnostic receipt
metadata. It does not add streaming, input modes, health probes, or changes to
raw evidence or canonical wiki pages.

## RED evidence

After adding the Task 2 tests, this command failed as expected because the new
runtime interfaces were absent:

```text
PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache python3 -m unittest \
  tests.test_run_metronome_model_worker -v
```

The failure was `ImportError: cannot import name 'job_lock' from
'metronome_model_runtime'`. The new tests cover cross-process lock contention
from separate worktree roots, normal-close lock release with the lock file
retained, and TERM followed by KILL for a real parent-and-descendant process
group that ignores TERM.

## Implementation

- Added non-blocking `fcntl.flock` job locks in
  `metronome_model_runtime.py`. Lock filenames are path-safe and include a
  provider/job digest; ownership is kernel-managed and lock files remain after
  close.
- Diagnostic `run_worker` executions resolve `git rev-parse --git-common-dir`
  and acquire the provider/job lock before creating the immutable run
  directory. Legacy no-run-ID worker calls remain unlocked and retain their
  direct artifact layout.
- Default live execution now starts Codex with `start_new_session=True`. A
  timeout sends `SIGTERM` to the process group, waits for the configured grace
  period, escalates to `SIGKILL` if the group remains, and records the signal,
  grace outcome, escalation, and final exit code in diagnostic attempt and
  terminal receipt metadata.
- Injected deterministic `runner=` calls remain compatible; their synthetic
  timeout receipt records `runner_timeout` rather than claiming a real process
  group was terminated.

## GREEN evidence

```text
PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache python3 -m unittest \
  tests.test_run_metronome_model_worker tests.test_metronome_ingest_pilot -v
PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache python3 -m py_compile \
  scripts/metronome_model_runtime.py scripts/run_metronome_model_worker.py
```

Result: 45 focused tests passed; compilation succeeded. The real child-process
test completed with no descendant remaining.

## Concerns

None. The test suite intentionally uses a short grace period only for its
isolated child process; production cleanup keeps the required five-second
default.
