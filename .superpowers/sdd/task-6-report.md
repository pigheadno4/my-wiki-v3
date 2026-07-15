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
