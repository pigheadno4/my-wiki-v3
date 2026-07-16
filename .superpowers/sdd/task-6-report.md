# Task 6 Snapshot Evidence

## RED

- Focused run before production edits: 20 tests ran; 5 failures and 5 errors.
- The failures demonstrated the missing changed-path and release-note parameters, JSON manifest authority, containment checks, post-copy byte limits, no-clobber lock, supplement revision allocation, and promotion cleanup.

## GREEN

- `python3 -m unittest tests.test_github_snapshot -v`: 21 tests passed.
- `python3 -m unittest discover -s tests -v`: 148 tests passed.
- `git diff --check`: passed.

## Design Evidence

- `snapshot.md` carries one versioned JSON metadata block as the integrity authority; Markdown tables are escaped display only.
- The manifest records repository/ref identity, saved hashes and sizes, exclusions, explicit release-note absence or source metadata, and prior snapshot. Exact `release-notes.md` bytes are hashed in that metadata.
- Selection rejects absolute/traversal paths and symlinks. Staging enforces destination containment, validates copied-byte limits after copying, and rejects symlinks, unlisted files, unexpected top-level entries, and patch or diff files.
- Promotion uses an exclusive per-repository `.promotion.lock`; canonical SHA lookup and supplement `-rN` allocation occur while locked. Current-operation staging is cleaned on validation, target, filesystem, and replacement failures; the stable lock pathname is retained and never deleted.

## Integrity Fix Evidence

- RED: focused Task 6 run executed 27 tests with 8 failures and 1 error for selected-file and staged-root swaps, provenance tampering, lock-write cleanup, and replaced-lock preservation.
- GREEN: `python3 -m unittest tests.test_github_snapshot -v` passed 27 tests; `python3 -m unittest discover -s tests -v` passed 154 tests; `git diff --check` passed.
- Checkout copies now use component-by-component descriptor traversal with `O_NOFOLLOW`, regular-file verification, copied-byte limits, and exact streamed hashes.
- `SnapshotRecord` carries trusted repository and release-note provenance plus staged-directory device/inode identity; validation rejects tampered provenance and swapped staged roots.
- This evidence described a temporary-lock deletion strategy that was superseded by the final promotion amendment. The final contract retains one stable regular `.promotion.lock` per repository and releases its advisory flock only by closing its descriptor; write, validation, target, and replacement failures clean only the original staging directory.

## Promotion Safety Amendment Evidence

- RED: `python3 -m unittest tests.test_github_snapshot -v` ran 31 tests with 8 expected failures before the production change: stable lock retention, advisory-lock contention, lock symlink rejection, collector-private parent checks, descriptor-relative replacement, and release-note byte plus manifest tampering.
- GREEN: `python3 -m unittest tests.test_github_snapshot -v` passed 31 tests; `python3 -m unittest discover -s tests -v` passed 158 tests; `git diff --check` passed.
- Promotion requires collector-owned, non-group/world-writable staging and snapshot parents, opens every parent path component without following symlinks, and keeps a stable regular `.promotion.lock` protected by `fcntl.flock` for canonical lookup, supplement allocation, validation, target checks, and descriptor-relative `os.replace`.
- `SnapshotRecord` now binds the exact release-note SHA-256 and byte size; validation reads staged content through no-follow descriptors and rejects altered note bytes even if the staged JSON manifest is altered to match.
- Lock contention, lock-file symlinks, unsafe parents, target collisions, staged identity mismatches, validation failures, and replacement failures preserve existing evidence and clean only the current operation's original staging directory. The lock pathname is never deleted.

## Final Review Fix Evidence

- RED: `python3 -m unittest tests.test_github_snapshot -v` ran 37 tests with 6 expected failures before the final implementation change. The failures covered missing or boolean `format_version`, malformed or duplicate excluded entries, boolean file and release sizes, and leaf and parent checkout swaps after containment.
- GREEN: `python3 -m unittest tests.test_github_snapshot -v` passed 37 tests; `python3 -m unittest discover -s tests -v` passed 164 tests; `git diff --check` passed before this documentation-only evidence update.
- JSON validation now requires the complete authoritative schema with exact built-in types, rejects unknown keys and duplicate JSON keys, and validates saved and excluded entry shapes before trusting identity, release, or copied-file evidence.
- Checkout enumeration, candidate size inspection, binary detection, and copying use no-follow descriptor traversal. Deterministic leaf and parent-component swap tests prove outside bytes are neither selected nor copied.
- The stable `.promotion.lock` is released only when its descriptor closes; there is no explicit `LOCK_UN` or lock-path deletion. A failed promotion leaves the stable lock reusable by the next promotion.

## Empty Snapshot Fix Evidence

- RED: focused Task 6 run executed 39 tests with 2 expected failures for empty-selection and release-notes-only snapshots because `files/` was missing.
- GREEN: `build_snapshot` now creates the required empty `files/` directory before copying; focused tests passed 39/39, the full suite passed 166/166, and `git diff --check` passed.
- Regression coverage validates and promotes an empty selection, and validates and promotes a release-notes-only capture while preserving the exact release-note bytes.

## Final Task 6 Cleanup Edge Evidence

- RED: the deterministic mkdir-failure regression test ran alone and failed because one newly created `snapshot-*` staging directory remained after required `files/` creation raised `OSError`.
- GREEN: `files/` creation now runs inside the existing `build_snapshot` cleanup boundary; focused snapshot tests passed 40/40, the full suite passed 167/167, and `git diff --check` passed.
- Empty-selection behavior is unchanged: the required `files/` directory is still created unconditionally inside the protected block and is validated and promoted by the existing regression coverage.
