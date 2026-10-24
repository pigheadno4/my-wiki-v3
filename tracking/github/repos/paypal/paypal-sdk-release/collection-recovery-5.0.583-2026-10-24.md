# SDK release 5.0.583 collection recovery

Scope: recover collection only, stop before ingestion. User approved continuation of diagnosis and a bounded fix. Last ingested assembly baseline remains `@paypal/sdk-release@5.0.582`; `5.0.583` is now collected and awaiting approval.

## Root cause and fix

The preliminary `_tagged_changed_paths` check diffed the entire repository with default rename detection, then filtered the output to retained paths. In the partial clone, rename scoring demanded excluded CDN artifact blobs and timed out after 120 seconds. The exact release boundary is `9e81e2b176ff956e378917927459d35069b598a2` to `b544787bd6b5df35e64b98bf91744b24d99cf34d`.

An isolated real partial clone with lazy fetch disabled reproduced the distinction: ordinary name-only diff failed on an unavailable blob; metadata-only no-rename diff succeeded in 0.01 seconds. The fixed helper restricts the diff to the union of prior/current retained paths and uses `--no-renames` only for this preliminary name inventory. On the real boundary it reports only `package.json` in 0.018 seconds without lazy fetching. Final evidence comparisons retain their existing rename-aware behavior and policy limits.

## Verification

- Two new real-Git regression tests failed before the fix and passed after: preserve both sides of a retained rename; avoid reading unavailable excluded artifact blobs.
- Collector and comparison/store suites: 67 tests passed after both fixes.
- Full suite: 815 tests, three unrelated registry-expectation failures, 812 passed. No changes to those registry/tests in this work.
- Existing failures: `test_adyen_postman_has_reviewed_checkout_terminal_policy` (30 versus 40 packet files); `test_braintree_graphql_api_has_reviewed_commit_policy` (15 versus 20 packet files); `test_paypal_messages_ios_uses_the_reviewed_release_capsule` (expected v1-only versus registered v2 track).
- Whitespace check passed after the narrow code/test change.

## Retry boundary

The next collection attempt encountered a separate GitHub release-note HTTP 403. Direct error headers confirmed zero unauthenticated API quota, with reset `2026-10-24T23:38:13+08:00`. No credentials were read or changed, no 403 was converted to missing notes, and no incomplete snapshot was accepted. The failed work item remained recoverable under the existing state machine.

After the API reset, the packet-wide upstream inventory exposed the same rename-scoring problem in `read_upstream_changes`. The blocked Git invocation was stopped and the collector recorded manual review. Accepted immutable snapshot/release/comparison evidence was preserved. Tagged collection and ad-hoc comparison packets now request metadata-only upstream inventories (`--no-renames`), retaining additions/deletions/modifications and policy-exclusion dispositions without downloading excluded blobs. The bounded retained-evidence comparison remains rename-aware; other adapters retain their existing default. A third real-Git regression test verifies the metadata-only inventory with a deliberately unavailable excluded blob.

## Completed collection and findings

Explicit retry succeeded with no collection errors. Work item `github-23561d27ca73a6844368` is `awaiting_approval`, recommended `delta`, with snapshot `raw/github/paypal/paypal-sdk-release/snapshots/2026-10-24-b544787/manifest.json` and its complete review packet. Eleven retained files were collected; only `package.json` changed, ten retained files are unchanged. Release-note evidence explicitly records `notes_available: false`; no release-note narrative was inferred.

Dependency pins advanced: checkout-components `5.0.437 -> 5.0.438`, common-components `1.0.62 -> 1.0.63`, messaging-components `1.99.0 -> 1.99.1`, sdk-client `4.0.204 -> 4.0.205`. Eight other dependency pins are unchanged. These establish assembly composition, not hosted rollout or uncollected component implementation behavior.

Offline GitHub validation reports no SDK Release errors. The global result retains 12 unrelated structural errors across six other repositories (packet budget failures and corresponding invalid-packet references), plus this one pending work item. Whitespace validation passes. No wiki edits, ingest approval, commit or push are included. Next: user approval for delta ingestion preserving all earlier history.
