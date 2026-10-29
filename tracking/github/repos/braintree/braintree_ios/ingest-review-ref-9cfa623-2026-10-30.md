# Braintree iOS exact-ref ingest review

- Work item: `github-5efc2eb4eec2312c8b58`
- Approved mode: full, overriding collector delta; shared GraphQL response-format impact.
- Identity: unreleased `default-branch@9cfa623`, exact SHA `9cfa6232f165285ee7cfbdb644329c7e7a97c180`.
- Prior: released `braintree-ios@7.13.0`, SHA `020dfb7a7803ec3ce8b2df2a0f71e386a4bf84e3`.
- Collection/ingest date: 2026-10-30. Commit date: 2026-10-29.
- Reading exception: user-approved focused reading of changed source/content, affected prior code/dependencies and cumulative wiki source/changelog; mechanical checks for unchanged source, generated inventories and historical raw changelog. Effective full-mode list expands to 303 paths; not a claim to read the entire upstream repository.

## Evidence and grounding

Paths below are relative to `raw/github/braintree/braintree_ios/snapshots/2026-10-30-9cfa623/files/`.

1. `Sources/BraintreeCore/BTCoreConstants.swift:21`: `static let graphQLVersion: String = "2024-08-23"`.
2. `Sources/BraintreeCore/BTGraphQLHTTP.swift:52`: `"Braintree-Version": BTCoreConstants.graphQLVersion,`.
3. `CHANGELOG.md:10`: `` `prepaid`, `healthcare`, `debit`, `durbinRegulated`, `commercial`, and `payroll` now return `YES`, `NO`, or `UNKNOWN` instead of `Yes`, `No`, or `Unknown`. ``
4. `Sources/BraintreeCore/BTBinData.swift:36`: `self.prepaid = json?["prepaid"].asString() ?? "Unknown"`.
5. `Sources/BraintreeCore/BTJSON.swift:275`: `countryCodeAlpha2: self["country"].asString() ?? self["countryCode"].asString(),`.

Both snapshots: 292 files each, all 584 file sizes/SHA-256/Git blob identities verified. Two changed retained paths, 290 unchanged; packet Markdown/snapshot and comparison Markdown/patch hashes verified. Historical raw changelog from `## 7.13.0` onward is byte-identical. The comparison covers selected capsule paths, not every upstream path.

Changed CoreConstants and new changelog content read completely, prior constant compared; unchanged transport, BIN parser, card client/nonce and Venmo nonce dependencies read; address helper/model reviewed. Current cumulative source/changelog read completely. Unchanged dependency identity verified across snapshots. No dependency/deployment or merchant enablement change inferred.

## Wiki disposition

Existing `braintree-ios-sdk` concept updated before cumulative source; additive unreleased section and changelog entry preserve all older body content and raw manifest references. Company source_count remains 797. The released package identity remains 7.13.0. No new source or cross-company comparison created. Reciprocal warnings preserve the upstream uppercase announcement versus unchanged comments/fallback mismatch. No Swift build, upstream SDK tests or gateway/payment execution.

## Workflow repair

Full-mode approval initially raised `KeyError: packages`: release-tracked ref packets intentionally have no package list. Added a regression to the existing tagged-tree ref test, observed the failure, then used repository-root selectors for ref packets as for commit evidence. Packet immutability, original required paths and narrowed selectors remain tested; all 62 packet tests pass. No collection policy or raw evidence changed.

## Final validation

- Work item completed through `complete-ingest`: state `ingested`, approved mode `full`, no package_changes. Collection index retains last accepted package `braintree-ios@7.13.0` and separately records latest discovered ref `default-branch@9cfa623`.
- Targeted wiki validation: five typed pages pass. The provider catalog has no YAML frontmatter by existing design, so its entries, uniqueness and paths were checked mechanically rather than changing its format to satisfy the typed-page validator. Root log checked as an untyped operation log.
- All original source/changelog body lines remain in order; older raw references remain, and every linked raw/tracking path exists. Company count remains 797. Scoped `git diff --check` passes.
- Packet and collection-index unit tests: 71 pass. Full suite: 815 tests, three failures in unchanged registry expectations: `test_adyen_postman_has_reviewed_checkout_terminal_policy` (30 versus 40 packet files), `test_braintree_graphql_api_has_reviewed_commit_policy` (15 versus 20), and `test_paypal_messages_ios_uses_the_reviewed_release_capsule` (old v1-only expectation versus retained v2 track). Registry and registry-test files are unchanged by this work.
- Global collection validation: 13 existing unrelated errors, zero pending items. Six historical packet-budget rebuild failures and their six invalid-packet reports affect Adyen Postman, Adyen SDK automation, Adyen release automation, Braintree restricted-input, Braintree web-sdk-github-actions and PayPal server-side integration. The remaining error is the Adyen PHP 30.1.0 changelog identity. No Braintree iOS error is reported; none of these unrelated issues was modified.
- No commit or push performed. Concurrent Adyen and other unrelated working-tree changes preserved.
