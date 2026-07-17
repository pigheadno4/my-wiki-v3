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

## Review Fix Cycle

### RED evidence

- The first alias test invocation used the singular class name `GitHubReleaseTests` and failed test loading. After correcting it to `GitHubReleasesTests`, `python3 -m unittest tests.test_github_releases.GitHubReleasesTests.test_semantic_aliases_on_the_same_commit_deduplicate -v` failed with `AttributeError: 'ReleaseCandidate' object has no attribute 'aliases'`. This proved release deduplication discarded the discovered same-SHA alias set.
- `python3 -m unittest tests.test_github_packets.GitHubPacketTests.test_branch_prior_selection_uses_immediately_preceding_same_day_capture -v` failed because the expected immediately preceding `aaaaaaaa...` capture was replaced by the older lexical-path winner `ffffffff...`. This reproduced the same-day branch predecessor defect.

### Design rationale

- Release selection now carries a sorted alias tuple on the one deterministically retained `ReleaseCandidate`. Deduplication first preserves the existing semantic-version and package-scoped matching rules and rejects aliases that resolve to different commits; only then does it attach every same-version, same-SHA tag. Collection merges that tuple into the resolved ref before snapshot creation. The retained candidate's `tag` still exclusively owns the fetched release-note URL, published date, and exact bytes.
- The version index now persists a top-level `capture_order` SHA ledger. Version entries remain independently sorted by the existing deterministic key, while branch predecessor selection uses the append ledger. Legacy indexes containing only `repo_id` and `versions` remain readable and acquire a deterministic order on load/save. The loader requires `capture_order` to contain every indexed SHA exactly once, preserving duplicate-SHA safety.
- Branch names remain repeatable history identities, but immutable tag, package-version, and commit identities remain unique. Packet endpoint entry schemas are unchanged, so packet/source validation continues to compare the complete canonical entry contract.
- The multi-release E2E proof now inspects every final index entry, immutable snapshot, and packet. It verifies the `10.0.0`/`v10.0.0` manifest and index aliases, deterministic release-note ownership, exact release-note/changelog/package bytes, future `10.1.6`, the independent default-branch evidence, and one `awaiting-review` packet per retained snapshot.
- The default-branch E2E proof now verifies delta and comparison SHAs/snapshot paths plus exact add, rename, and delete records. Both local E2E paths patch the release HTTP opener with a failure tripwire; their Git remotes remain temporary local repositories.
- Production dashboards were not regenerated because the changes did not alter their deterministic empty projection.

### GREEN evidence

- `python3 -m unittest tests.test_github_releases.GitHubReleasesTests.test_semantic_aliases_on_the_same_commit_deduplicate -v`: passed, 1 test.
- `python3 -m unittest tests.test_github_packets.GitHubPacketTests.test_branch_prior_selection_uses_immediately_preceding_same_day_capture -v`: passed, 1 test, including the generated delta packet's exact predecessor endpoint.
- `python3 -m unittest tests.test_collect_github_repos.CollectGitHubReposTests.test_local_end_to_end_baseline_unchanged_change_and_compare tests.test_collect_github_repos.CollectGitHubReposTests.test_local_release_backfill_and_future_patch -v`: passed, 2 tests.
- `python3 -m unittest tests.test_github_releases tests.test_github_packets tests.test_collect_github_repos -v`: passed, 82 tests.
- `python3 -m unittest discover -s tests -v`: passed, 286 tests.
- `python3 scripts/validate_github_collection.py`: `OK (0 snapshots, 0 pending packets, no structural errors)`.
- `git diff --check`: passed.
