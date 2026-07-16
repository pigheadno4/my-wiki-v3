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

## Remaining Boundary

Task 8 provides orchestration and monitoring. Task 9 remains responsible for
repository-wide validation, and Task 11 remains the hard user-gated live PayPal
pilot.

The existing Task 7 packet/evidence path validation derives its namespace from
the owner portion of `config.id`, while snapshot routing derives it from
`config.company`. The enabled registry row
`paypal-examples/v6-web-sdk-sample-integration` uses company `paypal`, so its
snapshot path and Task 7 packet expectation differ. Task 8 detects the packet
failure and rolls back its new snapshot/index, but collection of that row cannot
complete until the pre-existing namespace contract is aligned outside Task 8's
owned files.
