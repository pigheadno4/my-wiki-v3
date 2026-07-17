# Task 10 Local Git Pipeline Evidence

## Interrupted-Draft Recovery

- Recovery started after Sol reached model capacity and left a large uncommitted draft on `codex/github-repository-collection`; no reset or wholesale discard was used.
- The audit covered snapshot build/promotion/manifest validation, version-index load/save/mutation, packet identity and endpoints, collection rollback, GitHub validation, reporting projections, source-ledger contracts, and their tests.
- The recovered implementation keeps one canonical raw snapshot per SHA while retaining every distinct semantic release identity and package scope. Syntactic aliases of one semantic release remain one identity.

## RED

- `python3 -m unittest tests.test_github_snapshot tests.test_github_packets tests.test_collect_github_repos -v`
  - Result: `Ran 102 tests in 5.318s` and `FAILED (failures=8, errors=2)`.
  - The draft referenced missing grouped-release orchestration helpers, could not validate the new snapshot schema, selected the wrong same-SHA release endpoint, and had stale rollback/index expectations.
- The focused failures established that the draft was not publication-safe: same-SHA release groups could not complete, validator/schema consumers were unreconciled, and transactional behavior was not yet proved.
- Recovery added two focused validator regressions. They initially failed because packets were reconciled against a mutable latest-only evidence projection and source-ledger rows could not distinguish package scopes sharing one version. Both now pass while preserving valid historical packets.

## Recovered Design

### Snapshot evidence

- Snapshot manifest schema v2 stores an ordered `release_evidence` list. Each `SnapshotReleaseEvidence` entry owns one semantic release identity, package scope, aliases, exact release-note metadata, and an immutable evidence-file path.
- A newly accepted SHA is promoted once, only after the complete release-evidence set discovered in that collection group has been built and validated.
- If a later run discovers another release identity for an already accepted SHA, it writes through the existing explicit supplement mechanism. Canonical raw files and their manifest are never rewritten.

### Version index and branches

- Distinct `(package, normalized version)` release identities may have separate `VersionEntry` rows that share the same SHA and canonical snapshot path. Alias tags for one semantic release merge into one row.
- Immutable tag and package-version identities are checked against the existing index before snapshot, packet, or index publication. A moved identity raises a conflict and the collection transaction restores validator-clean state.
- Branch observations are append history independent of unique SHA capture order. This represents `A -> B -> A -> C`, unchanged re-observations, and multiple branch names without duplicating canonical snapshots.
- Legacy indexes infer branch order only when timestamps make it unambiguous. Same-day repeated branch history without explicit observations is rejected instead of guessed.

### Packets and transactions

- Every newly retained release identity receives one packet, including identities sharing a SHA. Packet IDs include a readable bounded label plus a digest of the full identity, preventing collisions between sanitized labels, package scopes, and alias forms.
- Group collection validates all index mutations before canonical promotion. Packet ownership tokens allow a later packet failure to remove only packets created by the transaction, then restore the prior index and any newly promoted snapshot.
- An unchanged branch re-observation still saves its observation and branch-head state transactionally even when no snapshot or packet is created.

### Validator reconciliation

- `github_validation` understands manifest v1 and v2, per-release evidence files, supplements, multiple index/source-ledger rows per snapshot, identity-specific packet endpoints, and collection lock files.
- Validation reconciles canonical and supplemented evidence by exact release identity. It does not treat every supplement on a shared SHA as evidence for every release row.
- Deterministic ordering, Python 3.9 compatibility, and no-network default behavior remain unchanged.

## GREEN

- `PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache python3 -m unittest tests.test_github_releases tests.test_github_snapshot tests.test_github_packets tests.test_collect_github_repos tests.test_github_validation -v`
  - Result: `Ran 190 tests in 9.490s` and `OK`.
  - Includes the two original Task 10 local E2E tests plus same-SHA distinct versions, package scopes, annotated/lightweight aliases, force-move rollback, branch reversion, multiple branches, unchanged re-observation, packet-ID collision, grouped packet rollback, and legacy-history coverage.
- `PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache python3 -m unittest discover -s tests -v`
  - Result: `Ran 298 tests in 13.305s` and `OK`.
- `PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache python3 scripts/validate_github_collection.py`
  - Result: `validate_github_collection: OK (0 snapshots, 0 pending packets, no structural errors)`.
- `git diff --check`
  - Result: passed with no output.

## Final Recovery GREEN

- `python3 -m py_compile scripts/collect_github_repos.py scripts/github_packets.py scripts/github_snapshot.py scripts/github_validation.py`
  - Result: passed.
- `python3 -m unittest tests.test_github_snapshot tests.test_github_packets tests.test_collect_github_repos tests.test_github_validation -v`
  - Result: `Ran 158 tests in 8.380s` and `OK`.
- The two original Task 10 local E2E tests plus five new edge E2E cases for branch reversion, same-SHA release identities, package scopes, force-moved tags, and grouped rollback
  - Result: `Ran 7 tests in 5.341s` and `OK`.
- `python3 -m unittest discover -s tests -v`
  - Result: `Ran 299 tests in 13.508s` and `OK`.
- `python3 scripts/validate_github_collection.py`
  - Result: `validate_github_collection: OK (0 snapshots, 0 pending packets, no structural errors)`.
- `git diff --check`
  - Result: passed with no output.

## Boundaries

- No public GitHub endpoint was contacted. E2E tests use temporary local Git repositories and mocked release-note responses whose stored bytes are asserted.
- Production dashboards remain unchanged because the production collection is empty and their deterministic projection did not change.
- Live collection and Task 11 were not started.
