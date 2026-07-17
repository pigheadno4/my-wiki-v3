# Task 10 Local Git Pipeline Evidence

## RED

- `python3 -m unittest tests.test_collect_github_repos.CollectGitHubReposTests.test_local_end_to_end_baseline_unchanged_change_and_compare tests.test_collect_github_repos.CollectGitHubReposTests.test_local_release_backfill_and_future_patch -v` initially failed before execution because the local Git helper was imported outside the `tests` package. The test now imports `tests.github_test_support`.
- The first behavioral run then exposed `version index contains conflicting reference entries` when a changed default branch created a second capture for the same branch name. This prevented the required comparison flow. `github_packets.load_version_index` now preserves branch capture history while retaining duplicate-reference rejection for immutable ref kinds.
- The release fixture was updated to provide mocked release-note evidence for both tags on the same SHA. The proof asserts canonical snapshot count, so semantic aliases create one canonical capture rather than requiring unfetched aliases to appear in an index record.

## GREEN

- `python3 -m unittest tests.test_collect_github_repos.CollectGitHubReposTests.test_local_end_to_end_baseline_unchanged_change_and_compare tests.test_collect_github_repos.CollectGitHubReposTests.test_local_release_backfill_and_future_patch -v`: passed, 2 tests.
- `python3 scripts/collect_github_repos.py status`: generated the empty production status projections.
- `python3 scripts/validate_github_collection.py`: `OK (0 snapshots, 0 pending packets, no structural errors)`.
- `python3 -m unittest discover -s tests -v`: passed, 283 tests.
- `git diff --check`: passed.

## Files Changed

- `tests/test_collect_github_repos.py`: adds local default-branch and monorepo release end-to-end pipeline coverage using direct local-path `RepoConfig` values and mocked release-note responses.
- `scripts/github_packets.py`: permits multiple historical captures of the same default branch while preserving immutable-reference identity checks.
- `tracking/github/status.json`, `tracking/github/collection-status.md`, and `tracking/github/ingest-status.md`: generated empty production dashboards.

## Production Dashboard Counts

- Registered repositories: 71.
- Enabled pilots: 5.
- Collected versions: 0.
- Ingest packets: 0.

## Boundaries

- No public GitHub endpoint was contacted. The end-to-end tests use temporary local Git repositories; release-note responses are mocked while their stored bytes are asserted exactly.
- Live collection remains the explicitly deferred Task 11 boundary.
