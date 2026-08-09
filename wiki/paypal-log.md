---
title: "PayPal Collection and Ingest Log"
type: log
tags: [paypal, github-repository, operations]
---

> PayPal-specific collection and ingest history. The root [[log]] keeps a concise cross-provider chronology.

## [2026-08-08] ingest | paypal/paypal-js React `10.3.0`

- Approved and processed work item `github-9ce02cb999656064a1a6` in delta mode after serial full-read review of all 13 required paths.
- Ingested `@paypal/react-paypal-js@10.3.0` at exact SHA `1ce6b30db4b7bcec8177a0c25aaf6408c6d523f2`; no `@paypal/paypal-js` release or dependency update is attached.
- Added typed `merchant_info.merchant_origin` support for server eligibility requests, the release-noted Google Pay payments-flow impact, and response-body eligibility diagnostics.
- Updated [[source-github-paypal-js]], [[changelog-github-paypal-js]], and [[paypal-google-pay]] without adding a concept, contradiction, or PayPal source count.

## [2026-08-05] ingest | paypal-examples/paypal-sdk-server-side-integration `default-branch@5409a3b`

- Approved and processed work item `github-849ba0a66c8ae04ad9da` in full mode after serial review of all 41 required paths.
- Hash-verified the 36-file, 101,281-byte immutable snapshot at `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/manifest.json`; two tests totaling 4,537 bytes were excluded by policy.
- Established a cumulative historical source and separate commit-qualified changelog for the September 2023 JS SDK 5.1.x server-side sample.
- Added server-owned amount construction, partner headers, Hosted Fields, one-key capture retry, shipping patches, and subscription create, activate, and revise orchestration.
- Preserved API-base precedence, order-retrieval, duplicate response parsing, shipping validation/arithmetic, subscription validation, revise-response, idempotency, and TypeScript defects as explicit warnings.
- Updated [[paypal-checkout]], [[paypal-expanded-checkout]], and [[paypal-subscriptions]] while keeping current documentation and the newer v6 sample authoritative.

## [2026-08-04] ingest | paypal-examples/v6-web-sdk-sample-integration `default-branch@b5f2df2`

- Approved and processed work item `github-6403ae7181617adc4020` in full mode after serial review of all 262 required paths totaling 1,585,894 bytes.
- Hash-verified the 257-file, 854,493-byte immutable snapshot at `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/manifest.json`; three tests, seven images, and one lockfile were excluded by policy.
- Preserved the April 2026 `dd9ef8a` review, moved the cumulative source into the canonical PayPal/GitHub hierarchy, and added a separate `dd9ef8a` to `b5f2df2` changelog.
- Added React v10.1.0 multi-flow, Fastlane, Google Pay 3DS, Apple Pay vaulting, expanded server routes, and 46 local-method implementations.
- Recorded that six local-method implementations explicitly capture despite the shared README's universal auto-completion claim, and kept merchant eligibility outside the sample's evidence boundary.
- Updated [[paypal-checkout]], [[paypal-apm]], [[paypal-fastlane]], [[paypal-google-pay]], [[paypal-apple-pay]], [[paypal-vault]], and [[paypal-subscriptions]].

## [2026-07-31] ingest | paypal/paypal-android `2.3.0`

- Approved and processed work item `github-c2ebe224d536e16acded` in full mode.
- Read the complete 245-path assignment, including the 242-file, 567,836-byte exact-SHA capsule at `raw/github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/manifest.json`; tests, fixtures, CI, binaries, and tooling were excluded by policy.
- Preserved the listener-era review and added the v2 callback/result model, explicit browser challenge completion, process-restorable state, card and PayPal vault flows, PaymentButtons, fraud data, and demo server contract.
- Isolated the exact `2.3.0` asynchronous `PayPalWebCheckoutClient.start(activity, request, callback)` addition from the broader `2.0.0` migration and intermediate finish/cancellation changes.
- Confirmed that the PayPal web funding enum, buttons, demo, and retained `Venmo` public surface expose no native Venmo integration.
- Updated [[paypal-android-sdk]] and [[paypal-vault]], migrated the cumulative source into the canonical PayPal/GitHub hierarchy, and added a separate changelog without changing PayPal's source count.

## [2026-07-31] ingest | paypal/paypal-ios `2.0.1`

- Approved and processed work item `github-5c8c7287ce91fe6f34c2` in full mode.
- Read the complete 148-path ingest assignment, including the 145-file, 281,036-byte exact-SHA capsule at `raw/github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/manifest.json`; tests and fixtures were excluded by policy.
- Preserved the older delegate-era review and added the v2 `Result`/async migration, public domain errors, error-based cancellation handling, card and PayPal vault flows, PaymentButtons, fraud data, and privacy evidence.
- Isolated the exact `2.0.1` deep-link cancellation fixes from the broader `2.0.0` migration.
- Confirmed the native PayPal checkout and button funding-source enums do not expose Venmo; a stale comment is not capability evidence.
- Recorded the PayPal vault `usage_type` discrepancy and repository license metadata mismatch without changing PayPal's source count.

## [2026-07-30] ingest | paypal/paypal-js React `10.2.1`

- Approved and processed work item `github-ca78b4ec339be0d6bdb8` in delta mode.
- Read the 20-path ingest packet and the 147-file, 1,098,433-byte exact-SHA capsule at `raw/github/paypal/paypal-js/snapshots/2026-07-30-7ff3eee/manifest.json`; 97 test/fixture files were excluded by policy.
- Ingested `@paypal/react-paypal-js@10.2.1` at SHA `7ff3eeec13e734f24f6e8fbf9aded68437c1398e`; no core package release is attached to this change set.
- Added the server-hydration/client-fetch race fix and resolved-response SSR guidance to [[source-github-paypal-js]], [[changelog-github-paypal-js]], and [[paypal-checkout]].
- No new concept, contradiction, payment behavior, Braintree behavior, or PayPal source count was introduced.

## [2026-07-30] ingest | paypal/paypal-js core `10.1.0` and React `10.2.0`

- Approved and processed work item `github-c2f5968bcd8357fc29d5` in delta mode.
- Read the 38-path ingest packet and the 150-file, 1,138,032-byte exact-SHA capsule at `raw/github/paypal/paypal-js/snapshots/2026-07-30-b496f3a/manifest.json`; 97 test/fixture files were excluded by policy.
- Ingested `@paypal/paypal-js@10.1.0` and `@paypal/react-paypal-js@10.2.0` as separate package releases sharing SHA `b496f3a7ea2a547b99ea5fb9895dfaf8cd01f6a3`.
- Added loader prototype-pollution protection, non-null Messages failure content, Braintree PayPal Messages, the `fetchEligibleMethods()` migration, and corrected server-hydration reuse.
- Updated [[paypal-checkout]], [[paypal-pay-later]], and [[paypal-braintree-integration]] without adding a new concept, contradiction, or PayPal source count.

## [2026-07-23] ingest | paypal/paypal-checkout-components `5.0.425`

- Approved and processed work item `github-f8c98215ba0bd54e6149` in full mode.
- Read the 325-file, 1,985,255-byte exact-SHA capsule at `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/manifest.json`; tests and fixtures were excluded by policy.
- Preserved the `4.1.47` baseline and added the accumulated v5 component architecture, exact bfcache patch, Venmo desktop/QR history, and experiment-gated vault-without-purchase behavior.
- Updated [[paypal-checkout]], [[paypal-vault]], and [[paypal-expanded-checkout]] without changing PayPal's source count.

## [2026-07-23] ingest | paypal/paypal-js core `10.0.3` and React `10.1.2`

- Approved and processed work item `github-92e87b7fea5fb1703585` in full mode.
- Read and hash-verified the 146-file, 997,074-byte exact-SHA capsule at `raw/github/paypal/paypal-js/snapshots/2026-07-22-3caece5/manifest.json`; 95 test/fixture files were excluded by policy.
- Ingested `@paypal/paypal-js@10.0.3` and `@paypal/react-paypal-js@10.1.2` as separate package releases sharing SHA `3caece5256428b6b5c713decbaec10ff7d785e9f`.
- Added v6 Venmo save-payment types, React Apple Pay disabled-prop removal, and PayPal Messages `TEXT` logo typing.
- Updated [[paypal-vault]], [[paypal-apple-pay]], and [[paypal-pay-later]].
- Preserved and flagged the conflict between older no-Venmo-purchase-later product guidance and the new package type; runtime availability remains unconfirmed.

## [2026-07-23] ingest | paypal/paypal-js core `10.0.2` and React `10.1.1`

- Approved and processed work item `github-986685252a62505561c4` in full mode.
- Read and hash-verified the 146-file, 994,570-byte exact-SHA capsule at `raw/github/paypal/paypal-js/snapshots/2026-07-22-3d72ac9/manifest.json`; 95 test/fixture files were excluded and historical stories remained available in prior capsules.
- Ingested `@paypal/paypal-js@10.0.2` and `@paypal/react-paypal-js@10.1.1` as separate package releases sharing SHA `3d72ac928b059cffab3c004d83656bd964ff4a1b`.
- Recorded the core `/sdk-v6` default export condition that prevents condition-sensitive tooling from falling back to v5.
- Recorded the React v5 Storybook 6-to-10 migration and separate-workspace extraction without treating removed in-package stories as removed payment support.
- No concept or contradiction update was required because the release changes package resolution and development tooling, not payment behavior.

## [2026-07-23] ingest | paypal/paypal-js core `10.0.1` and React `10.1.0`

- Approved and processed work item `github-ee6197518787f8152774` in full mode.
- Read and hash-verified the 176-file, 1,246,268-byte exact-SHA capsule at `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/manifest.json`; 95 test/fixture files were excluded by policy.
- Ingested `@paypal/paypal-js@10.0.1` and `@paypal/react-paypal-js@10.1.0` as separate package releases sharing SHA `59cb2ce64d158ac4f4cabecdd82f7b4191a8dff3`.
- Added typed v6 DOM elements, legacy Buttons Venmo setup-token approval data, Braintree Pay Later and eligibility, server environment validation, Google Pay setup errors, and eligibility lifecycle fixes.
- Recorded the release-note contradiction for checkout-with-vault shipping options in [[paypal-braintree-integration]], [[source-github-paypal-js]], and [[changelog-github-paypal-js]].
- Updated [[paypal-checkout]], [[paypal-vault]], and [[paypal-google-pay]] while preserving all earlier package sections.

## [2026-07-23] ingest | paypal/paypal-js coordinated `10.0.0` transition

- Approved and processed work item `github-bd7fe849961b5c6b9964` in full mode.
- Read and hash-verified the 171-file, 1,206,475-byte exact-SHA capsule at `raw/github/paypal/paypal-js/snapshots/2026-07-22-4bd05ab/manifest.json`; 89 tests were excluded and stories remained eligible.
- Ingested `@paypal/paypal-js@10.0.0` and `@paypal/react-paypal-js@10.0.0` as separate package releases sharing SHA `4bd05aba2f3263f0ea4694140dc71dfe1dd5b429`.
- Added the required v6 `environment` migration to [[paypal-checkout]], [[source-github-paypal-js]], and [[changelog-github-paypal-js]] while preserving all v8 and v9 knowledge.
- Kept the evidence boundary explicit: the release changes environment selection, not payment functionality, and does not establish a change to the separate Braintree provider.

## [2026-07-23] ingest | paypal/paypal-js v9 major transition

- Approved and processed work item `github-aa80084a50abf57e06d7` in full mode.
- Read and hash-verified the 198-file, 1,250,862-byte exact-SHA capsule at `raw/github/paypal/paypal-js/snapshots/2026-07-22-31eb658/manifest.json`; 96 tests were excluded and stories remained eligible.
- Ingested `@paypal/paypal-js@9.8.0` and `@paypal/react-paypal-js@9.3.0` as separate package releases sharing SHA `31eb658ac885a490d38ef34e471c069b0c6e49cb`.
- Added v9 component, provider, eligibility, Card Fields, Google Pay, and Braintree knowledge to [[source-github-paypal-js]] and [[changelog-github-paypal-js]] without removing either v8 baseline.
- Created [[paypal-braintree-integration]] and updated [[paypal-checkout]], [[paypal-expanded-checkout]], [[paypal-google-pay]], and [[paypal-vault]].
- Corrected [[source-github-paypal-js-v6]]: v9 `PayPalProvider` does not automatically call `findEligibleMethods()`.

## [2026-07-23] ingest | paypal/paypal-js `@paypal/react-paypal-js@8.9.2`

- Approved and processed work item `github-b11f1f62c66a78b84806` in full mode.
- Read and hash-verified the 101-file exact-SHA capsule at `raw/github/paypal/paypal-js/snapshots/2026-07-22-77487d6/manifest.json`; 36 tests were excluded and integration stories were retained.
- Updated [[paypal-expanded-checkout]] with React Card Fields callback-freshness behavior.
- Added the React v8 baseline to [[source-github-paypal-js]] and [[changelog-github-paypal-js]].
- Recorded the dependency move to `@paypal/paypal-js ^9.0.0` without marking that core package release as ingested.

## [2026-07-23] ingest | paypal/paypal-js `@paypal/paypal-js@8.4.2`

- Approved and processed work item `github-8416828e1141b2d896ea` in full mode.
- Read the exact-SHA capsule at `raw/github/paypal/paypal-js/snapshots/2026-07-22-702863f/manifest.json`, its 100 assigned files, and the package release notes.
- Updated [[paypal-checkout]] with package-qualified historical v6 evidence.
- Moved the cumulative source authority to `wiki/sources/paypal/github/source-github-paypal-js.md`.
- Created [[changelog-github-paypal-js]] as the separate release ledger.
- Recorded `@paypal/react-paypal-js@8.9.1` only as collateral repository context; no React release was ingested.
- Preserved the legacy v8 and later v6/v9 source pages as historical supporting evidence.
