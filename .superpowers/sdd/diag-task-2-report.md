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

## Fix Review

### Findings addressed

1. `terminate_process_group` now polls and reaps a TERM-honoring leader during
   the grace window while independently checking the process group. A missing
   or sandbox-inaccessible group after the leader is reaped is recorded as
   `terminated`, without a spurious KILL or escaping `PermissionError`.
2. Real Popen timeouts now preserve the actual terminated-process return code
   in `termination.final_return_code` while returning a logical worker exit
   code of `124`. The attempt loop branches on termination metadata, so timeout
   handling stops after one attempt and cannot be overwritten by a later
   success.
3. The lock test now exercises `common_git_dir()` for two distinct worktree
   roots through controlled `git rev-parse --git-common-dir` responses before
   proving both resolved paths contend on the same provider/job lock.

### RED evidence

The new focused review tests failed against the prior Task 2 commit:

- A TERM-honoring process group reached the unconditional KILL path and raised
  `PermissionError` instead of returning `terminated`.
- A real default-Popen timeout retried a second time because the actual signal
  return code was not `124`.

### GREEN evidence

```text
PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache python3 -m unittest \
  tests.test_run_metronome_model_worker tests.test_metronome_ingest_pilot -v
PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache python3 -m py_compile \
  scripts/metronome_model_runtime.py scripts/run_metronome_model_worker.py
```

Result: 47 focused tests passed. The focused real child tests cover both
TERM-honoring cleanup and TERM-ignoring escalation, with no surviving child.
