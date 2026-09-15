---
title: "Adyen Collection and Ingest Log"
type: log
tags: [adyen, github-repository, operations]
---

> Adyen-specific collection and ingest history. The root [[log]] keeps a concise cross-provider chronology.

## [2026-09-15] ingest | adyen/adyen-web `@adyen/adyen-web@6.45.0`

- Full-ingested `github-b1ef47fd1c229bf1ffb7` at exact SHA `b29934f6cf5de6e1912039f669b48ae45b75d3fd`, after user approval and serial reading of the assigned packet, comparison and 26-file supplement. Standard snapshot: 221 files, 13 modified, 208 unchanged.
- Added review-page lifecycle, payment-method exceptions, action and donation ownership, Google Pay nonce, address/rendering changes, and dependency updates. Recorded three ADR/code discrepancies without modifying raw evidence.
- Created the review-page concept first, then additively updated cumulative source/changelog, company and index. All older releases remain; source count unchanged. Full mode reflects the new checkout lifecycle, not a vulnerability claim from the CSP keyword.
- No runtime tests or live merchant eligibility verification. Stories are retained examples with explicit production-safety limitations. Details: [[source-github-adyen-web]], [[changelog-github-adyen-web]], [[adyen-review-page-checkout]].

## [2026-09-14] ingest | adyen/adyen-web `@adyen/adyen-web@6.44.0`

- Delta-ingested `github-92b6b54198b4cd5b55a6`, 6.43.0 to exact SHA `f10995d33491d8107c01a27dec2bc1fc4d6e28b0`, after serial review of the assigned current evidence and approved 40-file supplement.
- Preserved older knowledge; added keyboard dispatch, Amex CVC mapping, null defaults, country normalization, screen-reader lifecycle, Preact and Secured Fields version changes. PayPal JS remains 10.0.3; 3DS2 changes are formatting-only.
- User-approved delta overrides the recorded full recommendation after review: the security keyword matched CVC "security code", not vulnerability evidence. No classifier change.
- Updated source, changelog, co-badged-cards concept, company, index, and logs. No new source or comparison. No runtime tests; translation and external Secured Fields runtime limits remain explicit. 6.45.0 stays awaiting approval.

## [2026-09-14] ingest | adyen/adyen-web `@adyen/adyen-web@6.43.0`

- Delta-ingested `github-9ddbf78a69c5ce3ccc94`, 6.42.0 to exact SHA `b98917359c0b5b701ef99b583aef44f447e73bf6`, with its linked 14-file Select/Tag supplement including three stories.
- Preserved older knowledge; recorded tags, supporting-text visibility, filterable click handling, source/CSS accessibility boundaries, and PayPal JS 10.0.2 to 10.0.3 dependency.
- Updated source, changelog, company, and index. No new source count, concept, or comparison page; no contradiction found. No runtime tests. 6.44.0 and 6.45.0 remain awaiting approval.

## [2026-08-29] ingest | adyen/adyen-3ds2-ios-swift `adyen-3ds2-ios-swift@3.0.1`

- Approved and full-ingested work item `github-a200548203865cde87a4` at exact SHA `1596f558f39d9e706030ab77ebcf8c01492d1ecd` after serial full reading of all 12 required evidence paths.
- Established [[source-github-adyen-3ds2-ios-swift]] and its package-qualified changelog, and extended [[adyen-3ds2-ios-sdk]] without merging the independent `adyen/adyen-3ds2-ios` history.
- Recorded Swift-native transaction initialization, authentication parameters, callback and async challenge execution, lifecycle controls, security warnings, appearance, privacy declarations, and deprecated `LegacyInterface` compatibility.
- Preserved the binary implementation boundary and recorded the Apache-versus-MIT license conflict, incorrect Carthage repository reference, classic API-version caveat, and exact Swift 6 warning/iOS 26 logo release claims.

## [2026-08-28] ingest | adyen/release-automation-action `default-branch@9675ced`

- Approved and full-ingested work item `github-631f3be17d0207a5120c` at exact SHA `9675cedc9efe9d0b5563bd7dd0f8ef88f26ad03b` from the complete seven-file retained capsule plus required context.
- Established [[source-github-release-automation-action]] and its commit-qualified changelog for merged-PR discovery, label-based semantic version selection, prerelease transitions, version-file updates, release pull requests, optional auto-merge, and GitHub releases.
- Extended [[adyen-sdk-automation]] while preserving repository ownership: generic release orchestration remains independent from OpenAPI generation and every downstream SDK release history.
- Preserved the engineering-tooling boundary and recorded the bounded GraphQL query, label-normalization limitation, unvalidated version input, token and branch-setting prerequisites, and stale README example version.

## [2026-08-26] ingest | adyen/adyen-wechatpay-ios `AdyenWeChatPayInternal@2.2.0`

- Approved and full-ingested work item `github-3da269c833aa3c1fde17` at exact SHA `1127f793854d8624dbe6741d5c42be39dadd4f93` after serial full reading of all 14 required evidence paths.
- Established [[source-github-adyen-wechatpay-ios]], its package-qualified changelog, and [[adyen-wechatpay-ios-wrapper]] for Tencent SDK packaging, iOS requirements, public native handoff, and the payment request/response surface.
- Preserved the independently versioned `adyen-ios` Component boundary, binary implementation limit, and the distinction between native callbacks and authoritative merchant-server payment status.
- Recorded the simulator contradiction between the XCFramework inventory, README warning, and umbrella-header imports; physical-device testing remains the dependable boundary.

## [2026-08-25] ingest | adyen/adyen-magento2 `adyen/module-payment@11.0.0`

- Approved and full-ingested work item `github-f9bb5a2b85a6fd26d4e8` at exact SHA `4206983499d829ef695185ac78af06b9bdfe96c6` after serial full reading of all 206 required evidence and context paths.
- Established [[source-github-adyen-magento2]], its package-qualified changelog, and [[adyen-magento2]] for storefront and headless checkout, modifications, vault, asynchronous webhooks, gift-card partial payments, POS Cloud, and Giving.
- Preserved Magento 2.4.8 and PHP 8.2-8.5 compatibility, Checkout API v71 and Components 6.35.0 boundaries, independently versioned dependencies, and merchant eligibility limits.
- Recorded the callback-argument mismatch and residual `supports_auto_capture` setting as source-code caveats requiring focused verification rather than confirmed runtime failures.

## [2026-08-25] ingest | adyen/adyen-sdk-automation `default-branch@2f180b9`

- Approved and full-ingested work item `github-8048e778dfc5ff78b746` at exact SHA `2f180b958babc6bbd6f0b6b73d7e4c6feefe256e` after serial full reading of all 49 required evidence and context paths.
- Established [[source-github-adyen-sdk-automation]], its commit-qualified changelog, and [[adyen-sdk-automation]] for seven-language OpenAPI generation, service inventory, CI execution, provenance logs, and release-note validation.
- Attached an exact-SHA four-file supplement for production generation scripts and workflows that the baseline's generic CI exclusion omitted; test scripts remain excluded.
- Preserved downstream SDK version ownership, generated-code-versus-runtime boundaries, and merchant-eligibility limits while updating the Adyen company page and provider index.

## [2026-08-20] ingest | Adyen/adyen-php-api-library `30.0.2`

- Approved and full-ingested work item `github-1ef004e332164a8359d6` at exact SHA `6ef96571834bc460201df8aea8c89882b2043cd8` after serial full reading of all 450 required evidence paths.
- Established [[source-github-adyen-php-api-library]], its package-qualified changelog, and [[adyen-php-api-library]] for Checkout API v71, Payments and Recurring APIs v68, tokenization webhooks, transport, and HMAC helpers.
- Preserved the checkout-focused boundary, merchant-specific live Checkout prefix requirement, generated-model-versus-eligibility distinction, and the stale `SECURITY.md` support-table contradiction.
- Updated [[recurring-payments]], the Adyen company page, provider index, and calculated cumulative source and release counts.

## [2026-08-19] ingest | Adyen/adyen-3ds2-ios `2.4.4`

- Approved and full-ingested work item `github-b8f0d09e7fd89635c59f` at exact SHA `00862adbc079d0be943666a4ad2523deb31f9546` after serial full reading of all 32 required evidence paths.
- Established [[source-github-adyen-3ds2-ios]], its package-qualified changelog, and [[adyen-3ds2-ios-sdk]] for service setup, server handoff, universal-link challenges, lifecycle, errors, security warnings, privacy, and UI customization.
- Preserved the binary/public-header evidence boundary, classic Payment API v64 references, selected-framework-slice limitation, and erroneous warning-class specification link.
- Updated the parent iOS evidence, cross-platform 3DS2 concepts, Adyen company page, provider index, and calculated cumulative source count.

## [2026-08-19] ingest | Adyen/adyen-3ds2-android `2.2.27`

- Approved and full-ingested work item `github-ddb53c093685674310ef` at exact SHA `de845e67488b6aecb1ff57ea7908b662f5ee2d40` after serial full reading of all 69 required evidence paths.
- Established [[source-github-adyen-3ds2-android]], its package-qualified changelog, and [[adyen-3ds2-android-sdk]] for transaction setup, `/authorise3ds2` handoffs, challenge outcomes, lifecycle, security warnings, and UI customization.
- Preserved the public-documentation-only boundary and recorded the missing `DATA_SAFETY_GUIDE.md`, absent `2.2.27` compatibility row, and contradictory generated cleanup wording as explicit evidence gaps.
- Updated the parent Android concept, Adyen company page, provider index, and calculated cumulative source count.

## [2026-08-12] ingest | adyen/adyen-postman `default-branch@ecb2907`

- Approved and processed work item `github-ab2d0a488d97d9590b4c` in full mode at exact SHA `ecb2907c79a0aef2208aa2796a2bd0fc8ffd0cd7`.
- Read the complete 11-file, 851,723-byte snapshot plus packet, manifest, provider context, and collection scripts; parsed all 60 Checkout and 82 Terminal request examples.
- Established [[source-github-adyen-postman]] and its commit-qualified changelog for Checkout v72, Recurring v68, BIN Lookup v54, Test Card v1, and Terminal API.
- Created [[adyen-terminal-api]], corrected [[recurring-payments]] to distinguish preferred Checkout recurring endpoints from the legacy Recurring API, and updated the Adyen company and provider index.
- Preserved API-example evidence as exact-commit request guidance rather than merchant eligibility, enablement, or current-production proof.

## [2026-08-09] ingest | Adyen/adyen-web `6.42.0`

- Approved and processed work item `github-b307f27febbff4df8e80` in delta mode at exact SHA `1e157f8bc62b9519d68becedd9c1267180810e77`.
- Compared `@adyen/adyen-web@6.41.1` with `6.42.0` and retained an approved five-file supplement for changed Address and shared IFrame implementation.
- Added Drop-in payment-list analytics, country-aware partial US postal validation, and internal 3DS2 iframe permissions for WebAuthn and SPC while preserving both 6.41.x history layers.
- Updated [[source-github-adyen-web]], its package-qualified changelog, the Adyen company page, and provider index; no concept or cross-provider comparison page required a semantic update.

## [2026-08-09] ingest | Adyen/adyen-web `6.41.1`

- Approved and processed work item `github-60b7545cc0ad3999d886` in delta mode at exact SHA `c98ea8a7fe3c504075509755a0eda2264042d076`.
- Compared `@adyen/adyen-web@6.41.0` with `6.41.1` and retained an approved nine-file source supplement for changed implementation outside the standard checkout capsule.
- Preserved the cumulative `6.41.0` knowledge and added version-qualified OpenInvoice focus isolation, Enter-key submission protection, IME address-input handling, internal BIN lookup typing, and dependency updates.
- Updated [[source-github-adyen-web]], its package-qualified changelog, the Adyen company page, and provider index; no concept or comparison page required a semantic update.

## [2026-08-02] ingest | Adyen/adyen-node-api-library `32.0.0`

- Approved and processed work item `github-2957d7d341f9f6cb5ecc` in full mode.
- Read and hash-verified all 548 packet paths plus the approved six-path notification supplement at exact SHA `99d1a0cf69c8660952baffd1437b00aae2fa4f23`.
- Established the cumulative Node.js server-library source and package-qualified release ledger for `@adyen/api-library@32.0.0`.
- Recorded Checkout API v72, request transport and idempotency, notifications and HMAC, recurring operations, Cloud Device API v1, encrypted Nexo handling, and explicit inventory-only boundaries for other API domains.
- Isolated exact `32.0.0` Checkout breaking changes, Cloud Device introduction, and security fixes from broader cumulative library behavior; created [[adyen-node-api-library]] and updated the Adyen company and provider index.

## [2026-08-02] ingest | Adyen/adyen-react-native `2.12.0`

- Approved and processed work item `github-43baf5daaf3a92e79a79` in full mode.
- Read and hash-verified all 304 required evidence files, including the complete 301-file, 651,593-byte exact-SHA capsule at `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/manifest.json`.
- Established the cumulative React Native source and package-qualified release ledger at exact SHA `2912c913266b2d1df73882980303b563ea04ab63`.
- Recorded Drop-in, Components, Session and advanced flows, embedded Fabric CardView, actions, cards, wallets, platform setup, and merchant-server boundaries.
- Isolated exact `2.12.0` features, fixes, and native dependency updates from broader cumulative wrapper behavior; created [[adyen-react-native-sdk]] and linked the independently versioned iOS and Android evidence.

## [2026-08-01] ingest | Adyen/adyen-android `5.20.0`

- Approved and processed work item `github-b241eb5a8bcbadf2be62` in full mode.
- Read the complete 1,199-file, 3,670,837-byte exact-SHA capsule plus release and snapshot records at `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/manifest.json`.
- Established the cumulative native source and package-qualified release ledger at exact SHA `5314fad1389a8def9d8e3377f27f7405e303faba`.
- Recorded Drop-in, Sessions, View and Compose Components, cards and encryption, stored and partial payments, actions, local payment methods, analytics, and delegated dependency boundaries.
- Isolated the exact `5.20.0` compile and target SDK 36 change from broader cumulative SDK behavior; created [[adyen-android-sdk]] and updated [[co-badged-cards]], the Adyen company page, and provider index.

## [2026-08-01] ingest | Adyen/adyen-ios `5.25.1`

- Approved and processed work item `github-0f505b736a8fbe7628ca` in full mode.
- Read the complete 686-file, 2,126,088-byte exact-SHA capsule plus three release and snapshot records at `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/manifest.json`.
- Established the cumulative native source and package-qualified release ledger at exact SHA `5f6779b31299e3067de3a5279a816f3b8d2fbdf3`.
- Recorded Drop-in and Components, Session and advanced flows, cards and encryption, stored and partial payments, Apple Pay, actions, native app handoffs, analytics, privacy, and delegated dependency boundaries.
- Isolated the exact `5.25.1` cross-platform form-layout fix from broader cumulative SDK behavior; created [[adyen-ios-sdk]] and updated the Adyen company and provider index.

## [2026-07-26] ingest | Adyen/adyen-web `6.41.0`

- Approved and processed work item `github-9f56dfbe62e4e84b03c7` in full mode.
- Read the complete 219-file, 638,517-byte exact-SHA capsule at `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/manifest.json`; 48 tests were excluded by policy and 17 stories were retained.
- Established the cumulative source and package-qualified release ledger at exact SHA `b19eec7054340a1526c87d450fd7dfff75794ed9`.
- Recorded Drop-in and Components architecture, Sessions and advanced flows, card funding-source behavior, 3DS2 safeguards, accessibility, analytics exclusions, and the delegated PayPal Fastlane boundary.
- Created the Adyen company and provider index; added version-qualified dual-brand evidence to [[co-badged-cards]].
