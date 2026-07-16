# Task 9: GitHub Collection Validation Evidence

## Scope

Implemented repository-wide validation for immutable GitHub snapshots, version
indexes, packet histories, generated status, source ledgers, and nested wiki
links:

- `scripts/github_validation.py`
- `scripts/validate_github_collection.py`
- `tests/test_github_validation.py`
- `tests/test_validate_wiki.py`

`scripts/validate_wiki.py` required no production change because its existing
path-qualified link resolution passed the new snapshot, changelog, and
release-note regression.

## TDD Evidence

### RED

Before `github_validation.py` existed, the focused validation test command
failed with the expected import error. Structural regressions were then added
for malformed snapshots, release retention, packet state, generated artifacts,
source ordering, dashboards, and nested links before their validation logic.

### GREEN

```text
python3 -m unittest tests.test_github_validation tests.test_validate_wiki -v
Ran 23 tests
OK

python3 scripts/validate_github_collection.py
OK (0 snapshots, 0 pending packets, no structural errors)

python3 -m unittest discover -s tests -v
Ran 245 tests
OK

git diff --check
exit 0
```

## Validation Boundary

- Snapshot validation checks manifest/file agreement, exact hashes and sizes,
  canonical SHA uniqueness, valid supplements, explicit release evidence, and
  rejects generated patch/diff files under raw.
- Version-index and retention checks detect missing retained versions,
  prereleases in stable-only tracks, duplicate canonical snapshots, unsafe
  evidence paths, and release/index disagreement.
- Packet validation checks required-reading existence, strict transition
  history, exactly one packet per newly collected release, and generated status
  agreement.
- Awaiting-review packets are reported through `pending_packets` and remain
  informational rather than structural errors.
- Source validation checks company-first records, ordered `raw_files`, and
  path-qualified snapshot, changelog, and release-note links using the existing
  wiki parser and link index.
- Inspection records malformed or unsafe artifacts as errors and does not
  follow symlink or traversal escapes.

## Local Baseline

No live GitHub pilot has run in this worktree, so the validator correctly
reports zero snapshots and zero pending packets. Task 10 provides deterministic
local end-to-end proof before the Task 11 live user gate.
