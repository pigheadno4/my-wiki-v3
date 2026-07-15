# Task 5 Report: Discover Retained Releases and Preserve Release Notes

## Status

Completed. Task 5 adds deterministic remote tag discovery, pure retained-release selection, and exact available GitHub release-note evidence retrieval. It does not create snapshots or write any raw artifacts.

## TDD Evidence

### RED

After adding the release-selection, local-remote discovery, and mocked HTTP tests, the required focused command failed as expected because the module did not exist:

```text
python3 -m unittest tests.test_github_releases -v
ModuleNotFoundError: No module named 'github_releases'
```

### GREEN

Added `scripts/github_releases.py` using `github_git.run_git` for `ls-remote --tags` and shared `github_versions` parsing/comparison. The initial focused GREEN run passed 10 tests. A self-review regression then demonstrated that incomplete tags such as `v9` and `v9.0` were being retained; release candidates now require exact `major.minor.patch` versions.

```text
python3 -m unittest tests.test_github_releases -v
Ran 11 tests in 1.038s
OK
```

## Behavior and Error-Boundary Review

- Pairs annotated tag objects with peeled commit rows; lightweight tags use their commit SHA for both fields.
- Package tracks accept only their exact namespace. Plain tracks accept only plain semantic tags and reject multiple matching package namespaces.
- `all-stable`, `minor-baselines`, and future selection are deduplicated, semantically ordered, stable-only by default, and reject missing pins or invalid policies/modes.
- Release notes use only the standard library, URL-quote every endpoint segment, preserve the release body as UTF-8 bytes, send required headers plus optional bearer auth, return `None` only for 404, and attach repository/tag context to all other failures.
- No default test contacts the network; local bare remotes and mocked openers cover discovery and HTTP behavior.

## Final Verification

```text
python3 -m unittest discover -s tests -v
Ran 114 tests in 5.250s
OK

git diff --check
exit 0
```

## Commit

```text
6cafe86 feat: select github release history
```

## Concerns

None. Snapshot storage, generated version-index integration, and concrete PayPal registry tracks remain intentionally deferred to later tasks.

---

## Review Fix Evidence (2026-07-15)

### RED

Added focused regressions before implementation. The first focused run failed in the intended areas: build-metadata identity for retention, pins, and existing versions; duplicate, conflicting, and orphan `ls-remote` rows; matching incomplete plain/package tags; successful response context entry/exit; and `HTTPError` response cleanup.

```text
python3 -m unittest tests.test_github_releases -v
Ran 18 tests in 0.988s
FAILED (failures=12)
```

### Final Verification

```text
python3 -m unittest tests.test_github_releases -v
Ran 18 tests in 0.988s
OK

python3 -m unittest discover -s tests -v
Ran 121 tests in 4.452s
OK

git diff --check
exit 0
```

### Files and Self-Review

- `scripts/github_releases.py`: preserves validated build metadata in release identity while retaining SemVer precedence; rejects deterministic malformed tag metadata and matching incomplete tags; context-manages successful responses and closes caught `HTTPError` bodies.
- `tests/test_github_releases.py`: covers exact build identities, malformed rows and order independence, incomplete tag boundaries, context entry/exit, and HTTP error body cleanup.
- Preserved existing all-stable, minor-baseline, future, annotated/lightweight identity, exact body bytes, headers/token, Python 3.9, and no-network/no-raw-write behavior.

### Commit

```text
2ae0e0346f8ad050b4496eed73934d8ba06e005e fix: preserve github release identity
```

### Concerns

None.

## Scope Fix Evidence (2026-07-15)

### Root Cause

Incomplete-tag discovery previously rejected every incomplete tag with the
same major number as the selector. That made `v9.0` fail a `v9.1` plain track
and `@scope/widget@9.0` fail a `package:@scope/widget@9.1` track. The fix now
requires each available component to satisfy the configured selector while
preserving major-only matching for `v9` and `v9.0`.

### RED

Added focused plain and package regressions for unrelated incomplete tags,
matching incomplete tags, and input-order independence. Before the production
change, the focused suite failed with 2 failures and 2 errors across 22 tests:

```text
python3 -m unittest tests.test_github_releases -v
Ran 22 tests in 1.111s
FAILED (failures=2, errors=2)
```

### GREEN

```text
python3 -m unittest tests.test_github_releases -v
Ran 22 tests in 1.108s
OK

python3 -m unittest discover -s tests -v
Ran 125 tests in 4.653s
OK

git diff --check
exit 0
```

### Files and Scope

- `scripts/github_releases.py`: scopes incomplete-tag errors by the semantic
  components required by the configured track.
- `tests/test_github_releases.py`: covers plain and package minor selectors,
  unrelated tags, input-order independence, and major-only `v9`/`v9.0` behavior.
- No other files were modified.

### Commit

Commit message: `fix: scope incomplete github release tags`.
