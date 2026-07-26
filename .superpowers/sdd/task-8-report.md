# Task 8: Collection CLI and Monitoring Evidence

## Scope

Implemented the public GitHub collection coordinator and generated reporting:

- `scripts/github_reporting.py`
- `scripts/collect_github_repos.py`
- `tests/test_github_reporting.py`
- `tests/test_collect_github_repos.py`

The implementation composes the approved registry, release, Git, snapshot, and
packet modules. It does not ingest wiki content.

Feature commit: `dd07bfe` (`feat: add github collection cli and monitoring`)

## TDD Evidence

### RED

The focused command was run before the two production modules existed:

```text
python3 -m unittest tests.test_github_reporting tests.test_collect_github_repos -v
```

The expected import failures established the missing reporting and CLI
interfaces before implementation:

```text
Ran 2 tests
FAILED (errors=2)
ModuleNotFoundError: No module named 'github_reporting'
ModuleNotFoundError: No module named 'collect_github_repos'
```

Later RED cycles exposed three failures and one error around release-track
filtering, index-load terminal reporting, generated-state exit handling, and
corrupted packet history. A final RED regression test showed that packet
failure left a newly-created empty version index. Each failure was reproduced
before its implementation fix.

### GREEN

```text
python3 -m unittest tests.test_github_reporting tests.test_collect_github_repos -v
Ran 27 tests in 0.069s
OK

python3 -m unittest discover -s tests -v
Ran 210 tests in 6.662s
OK

git diff --check
exit 0
```

## Design Evidence

- The public coordinator exposes `CollectionResult`, `collect_one`,
  `compare_one`, `prepare_one`, `regenerate_status`, and `main`, with the
  required collection, comparison, packet preparation, status, and packet-state
  CLI forms.
- Collection events are append-only sorted JSON lines; reconciliation requires
  exactly one terminal event for every selected repository/ref.
- Packet transitions use the exact approved state machine and reject corrupted
  or invalid histories without appending.
- Dry-run collection resolves and reports selections without creating `raw/`
  or generated tracking state.
- Batch selection excludes disabled repositories unless explicitly requested;
  a direct one-repository request may select a disabled row.
- Backfill and future modes enumerate each retained release independently and
  create at most one packet and one terminal event per release.
- Collection failures clean temporary snapshot state and still emit a terminal
  event. Packet failure rolls back a newly promoted snapshot and absent version
  index rather than leaving an unreconciled partial run.
- Status regeneration derives JSON and Markdown dashboards from registry,
  collection events, packet contracts, and valid packet state history.
- Successful reconciled work exits 0, operational/validation/reconciliation
  failures exit 1, and CLI or registry misuse exits 2.
- Default tests mock Git/GitHub operations and do not contact the network.

## Integration Remediation

Integration fix commit: `b6d3b6b` (`fix: reconcile github collection state and evidence`)

### RED

The owned reporting, collector, and packet tests were extended before the
implementation changes. The first focused run reproduced every integration
finding:

```text
python3 -m unittest tests.test_github_reporting tests.test_collect_github_repos tests.test_github_packets -v
Ran 41 tests in 1.513s
FAILED (failures=6, errors=27)
```

The failures showed that both concurrent transitions succeeded, a symlinked
packet directory was followed, foreign history was projected, same-SHA release
aliases returned `unchanged`, future discovery missed alias representations,
and owner/company evidence paths were rejected. A second focused RED test
proved that supplemental changelog evidence could not round-trip through the
version index.

### GREEN

```text
python3 -m unittest tests.test_github_reporting tests.test_collect_github_repos tests.test_github_packets -v
Ran 52 tests in 1.500s
OK

python3 -m unittest discover -s tests -v
Ran 219 tests in 6.926s
OK

git diff --check
exit 0
```

### Corrected Contracts

- Packet transitions open the exact
  `tracking/github/repos/<config.id>/packets` namespace without following
  symlinks and hold the stable packet lock across strict history read, current
  state validation, and append. Concurrent identical transitions serialize, so
  only one succeeds.
- `validate_packet_history` is the single strict history validator used by both
  transitions and status reconstruction. It requires an exact
  `awaiting-review` initial event, matching packet identity and `from_state`,
  exact event shapes, and legal transitions; invalid history aborts status
  generation rather than being skipped.
- A newly observed release alias on an indexed SHA creates an immutable
  supplement when exact GitHub notes are available, retains one canonical
  version entry for the SHA, merges aliases and supplemental evidence, and
  creates one independent awaiting-review packet without changing canonical raw
  bytes.
- Future discovery recognizes matching versions represented by canonical refs,
  aliases, or the entry package identity for package and plain tracks. It still
  enforces package namespace, selected major, and prerelease policy, so unrelated
  packages are excluded and indexed releases are not repeatedly selected.
- Tracking identity remains GitHub owner/repository from `config.id`. Raw
  evidence validation now receives `RepoConfig` and derives
  `raw/github/<config.company>/<repo-name>/`. The enabled PayPal examples-style
  regression proves collection and packet generation across the split
  namespaces without network access.
- Existing dry-run zero-mutation, terminal-event reconciliation, snapshot/index
  rollback, Python 3.9 compatibility, and Task 7 packet publication hardening
  remain covered by the focused and full suites.

## Remaining Boundary

Task 9 remains responsible for repository-wide validation, and Task 11 remains
the hard user-gated live PayPal pilot. The Task 8 owner/company namespace
boundary is resolved.

## Final Transaction and Reporting Remediation

Code and tests commit: `4426f56` (`fix: make github collection rollback ownership safe`)

### RED

The snapshot ownership API was specified before implementation. The focused
snapshot run failed at import because `promote_snapshot_with_result` and
`rollback_promoted_snapshot` did not exist.

The collector/reporting regressions were then added before their production
changes:

```text
python3 -m unittest tests.test_github_reporting tests.test_collect_github_repos -v
Ran 26 tests
FAILED (errors=6)
```

The failures covered the missing promotion result and rollback interfaces, the
missing repository collection lock, and global rejection of equal packet IDs
from different repositories. A subsequent 38-test run retained two expected
rollback fixture failures until macOS `/var` aliases were canonicalized to
their `/private/var` filesystem identities.

### GREEN

```text
python3 -m unittest tests.test_github_snapshot tests.test_github_reporting tests.test_collect_github_repos -v
Ran 81 tests in 0.305s
OK

python3 -m unittest discover -s tests -v
Ran 225 tests in 6.978s
OK

git diff --check
exit 0
```

### Corrected Contracts

- `promote_snapshot(record) -> Path` remains compatible. The collector uses a
  promotion result whose created/reused decision is made while the stable
  promotion lock is held; only created results carry rollback tokens.
- A rollback token binds the exact target path, device, and inode. Rollback
  reacquires the stable repository promotion lock, verifies that identity, and
  removes content descriptor-relatively. Reused, replaced, missing, or foreign
  targets are never deleted as owned snapshots.
- One stable no-follow `.collection.lock` serializes non-dry-run collection for
  each `config.id`. The focused regression observes it held during version-index
  load, packet publication, and rollback. Dry-run remains zero-mutation.
- Failure recovery restores or removes the prior version index before snapshot
  cleanup. Index rollback failure is surfaced, skips snapshot deletion, and
  leaves the updated index and referenced snapshot together. Snapshot rollback
  failures are also surfaced rather than swallowed.
- Packet lifecycle mappings now use deterministic repository-plus-packet keys.
  Equal packet IDs in PayPal and Stripe repositories retain independent states
  in both `status.json` and ingest Markdown; duplicate IDs within one repository
  remain invalid.
