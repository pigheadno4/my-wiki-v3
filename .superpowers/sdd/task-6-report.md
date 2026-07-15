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
- Promotion uses an exclusive per-repository `.promotion.lock`; canonical SHA lookup and supplement `-rN` allocation occur while locked. Current-operation staging and locks are cleaned on validation, target, filesystem, and replacement failures without removing foreign locks or targets.

## Integrity Fix Evidence

- RED: focused Task 6 run executed 27 tests with 8 failures and 1 error for selected-file and staged-root swaps, provenance tampering, lock-write cleanup, and replaced-lock preservation.
- GREEN: `python3 -m unittest tests.test_github_snapshot -v` passed 27 tests; `python3 -m unittest discover -s tests -v` passed 154 tests; `git diff --check` passed.
- Checkout copies now use component-by-component descriptor traversal with `O_NOFOLLOW`, regular-file verification, copied-byte limits, and exact streamed hashes.
- `SnapshotRecord` carries trusted repository and release-note provenance plus staged-directory device/inode identity; validation rejects tampered provenance and swapped staged roots.
- Promotion records the lock descriptor identity before writing and removes a lock only when its pathname still resolves to that same inode; write, validation, target, and replacement failures clean only the original staging directory.

## Promotion Safety Amendment Evidence

- RED: `python3 -m unittest tests.test_github_snapshot -v` ran 31 tests with 8 expected failures before the production change: stable lock retention, advisory-lock contention, lock symlink rejection, collector-private parent checks, descriptor-relative replacement, and release-note byte plus manifest tampering.
- GREEN: `python3 -m unittest tests.test_github_snapshot -v` passed 31 tests; `python3 -m unittest discover -s tests -v` passed 158 tests; `git diff --check` passed.
- Promotion requires collector-owned, non-group/world-writable staging and snapshot parents, opens every parent path component without following symlinks, and keeps a stable regular `.promotion.lock` protected by `fcntl.flock` for canonical lookup, supplement allocation, validation, target checks, and descriptor-relative `os.replace`.
- `SnapshotRecord` now binds the exact release-note SHA-256 and byte size; validation reads staged content through no-follow descriptors and rejects altered note bytes even if the staged JSON manifest is altered to match.
- Lock contention, lock-file symlinks, unsafe parents, target collisions, staged identity mismatches, validation failures, and replacement failures preserve existing evidence and clean only the current operation's original staging directory. The lock pathname is never deleted.
