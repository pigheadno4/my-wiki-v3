---
title: "Stripe Collection and Ingest Log"
type: log
tags: [stripe, github-repository, operations]
---

> Stripe-specific collection and ingest history. The root [[log]] keeps a concise cross-provider chronology.

## [2026-09-21] ingest | Stripe Node `22.6.2`

- Delta-ingested `github-c5fa7a0352b6764a7481` with approved focused reading, exact SHA `d9d092737b4a891f0beaf47c26c222972a4c7b0f`. Both 68-file snapshots verified; 11 modified, 57 unchanged. Older changelog identical; version-only core/package changes mechanically checked.
- Recorded sync/async missing-secret guards, error-order/format limits and framework-specific example failure handling. API pin, checkout contracts and earlier caveats unchanged. Updated concept first, cumulative source/changelog, company/provider index and logs; no source count change or cross-company comparison.
- Review: `tracking/github/repos/stripe/stripe-node/ingest-review-c5fa7a03.md`. No upstream SDK tests, commit or push. This finishes the currently collected Stripe Node release queue, not a new upstream freshness check.

## [2026-09-21] ingest | Stripe Node `22.6.1`

- Approved delta `github-2402efbbc4962288beb9`, `stripe@22.6.0` -> `stripe@22.6.1`, SHA `9f82c466c0a5913906ab1bf39790edd4d231ee5d`, with explicit focused-reading approval for this release. Changed implementation and complete diff read; both 68-file snapshots verified by hash/size. 13 modified, 55 unchanged; older changelog byte-identical.
- Recorded secure multipart boundaries and MIME header protection, path validation/event-ID encoding, GET/DELETE schema coercion, and enum documentation clarification. Distinguished existing filename escaping and idempotency-key fallback. No API pin or generated checkout changes; no upstream SDK/test execution.
- Updated Stripe Node concept first, cumulative source/changelog, company/provider index and logs. Prior history and source count preserved. No cross-company comparison; older caveats retained. Review: `tracking/github/repos/stripe/stripe-node/ingest-review-2402efbb.md`.
- `22.6.2` remains awaiting approval. No commit or push in this operation.

## [2026-09-21] ingest | Stripe Node `22.6.0`

- Full-mode ingest of approved `github-436c32c59360977be8fa`, `stripe@22.5.0` -> `stripe@22.6.0`, SHA `2f64e7ac920bd6863fdb851f4fb1fcc6190d963f`, with the explicitly approved focused-reading exception. Both 68-file snapshots passed hash/size checks; 33 modified, 35 unchanged. Earlier changelog text preserved. Two approved implementation supplements are linked canonically and read fully.
- Added handler lifecycle/context caveats, V2 coercion, exact body-error/timeout behavior, unconditional V1 POST idempotency, new API pin and generated checkout/billing contract changes. Recorded sample limitations; no SDK execution or live payment proof.
- Updated concepts before cumulative source/changelog, then company/index/logs. All earlier version history preserved; no new source page or cross-company comparison. Review: `tracking/github/repos/stripe/stripe-node/ingest-review-436c32c5.md`.
- `22.6.1` and `22.6.2` remain awaiting approval. No commit or push in this operation.

## [2026-09-21] ingest | Stripe Node `22.5.0`

- Delta-ingested approved `github-fdb611aa510b593685f6`, `stripe@22.4.0` -> `stripe@22.5.0`, exact SHA `65d99a2b76d0786d7cec8544920affadccc8b670`. User authorized focused reading for this release only: changed implementation and full 3,575-line diff read; both manifest inventories/all file hashes and 4,868 unchanged historical changelog lines verified mechanically. Two added, 12 modified, 54 unchanged retained files.
- Recorded unverified snapshot/thin parsing with cloud-envelope extraction, static API-family constant, opt-in extensibility transport and runtime-error behavior, plus the initialization stderr hint. API pin and generated checkout resources unchanged; older source/changelog knowledge preserved.
- Recorded wrong helper/constant names in upstream prose, low-level tolerance caveat, core/Node ESM object-check divergence and continuing README/retry-default conflict. Excluded entrypoint/emitter/test changes were reviewed in the diff; no build, upstream test, or live payment execution.
- Updated Stripe Node concept first, then cumulative source/changelog, company/index and logs. Company source count unchanged at 666. No cross-company comparison warranted. Review: `tracking/github/repos/stripe/stripe-node/ingest-review-fdb611aa.md`.
- `22.6.0`, `22.6.1` and `22.6.2` remain collected, awaiting approval; this ingest does not advance their state.

## [2026-09-15] ingest | React Stripe.js 6.10.0

- Delta-ingested approved `github-21eb12ac207dc1342925`, 6.9.0 to exact SHA `d1750b056f363f9a44fd70ecbe8d0a1bba3e3f4d`, after full serial reading of assigned raw files, manifests, comparison and cumulative wiki context.
- Recorded beta Link Signup root/Checkout wrappers, Checkout Form exclusion, callback/lookup contract and Stripe JS peer floor 9.16.0. Six retained files changed; 54 unchanged. Tests/mocks/lockfile remain comparison-only evidence; no upstream test/build/browser/payment execution.
- Updated existing Elements, Checkout and Link concepts before source/changelog, then company, index and logs. Preserved older versions and source count. No new contradiction or cross-company comparison. Both collected September React releases are now ingested.
- System Python encountered an Xcode-license prerequisite; used bundled Python for offline workflow and validation without modifying system settings.

## [2026-09-15] ingest | React Stripe.js 6.9.0

- Delta-ingested `github-d595e0d1b2664c8307ad`, 6.8.2 to exact SHA `d270c7e5f01e1b8c3614aefc39eb5c57e7131c19`, after serial assigned-evidence reading.
- Recorded Stripe JS peer floor 9.10.0, unchanged React peers/runtime, comparison-only CI and lockfile changes. Capsule: one modified file and 59 unchanged. No upstream test/build/payment execution.
- Updated existing Elements concept first, source/changelog, company, index and logs; preserved older versions and source count. No new contradiction or comparison. 6.10.0 remains collected, not ingested.

## [2026-09-15] ingest | stripe/stripe-js `@stripe/stripe-js@9.16.0`

- Delta-ingested approved work item `github-3d250b234dd9acbad2a0`, 9.15.0 to exact SHA `e03ec565455178cd2b236f6b495ddc952397c3f0`, after serial reading of assigned current declarations, prior source/changelog and comparison evidence.
- Added beta Link Signup lifecycle/API boundaries and Checkout tiered/package pricing response shapes, including required-nullable mock migration and expanded type unions. Loader, dependencies and hosted runtime boundary remain unchanged.
- Updated existing Link, Elements and Checkout concepts first, then cumulative source/changelog, company and index. Preserved prior versions; no new source count or cross-company comparison. No new contradiction found.
- Capsule: 80 files, four modified, one added and 75 unchanged. Type tests are comparison-only policy exclusions and were not executed; no browser/payment or beta eligibility verification.

## [2026-09-05] ingest | stripe/stripe-react-native `@stripe/stripe-react-native@0.75.0`

- Delta-ingested `github-295368ae3c6235174ae0` from `0.74.0` to exact SHA `e0a845f40749703480146c9d70721b9007d0516d` using the 19-path packet.
- Added Android Samsung Pay for Crypto Onramp, five wallet-verification error discriminants, and native pins Stripe Android `23.16.0`/Stripe iOS `26.7.0`.
- Updated existing concepts, cumulative source, separate changelog, company and provider index. Preserved previous history, app-supplied Samsung SDK requirements, sample pricing limitations, and comparison-only Android implementation evidence. Source count is unchanged.

## [2026-09-01] ingest | stripe/stripe-react-native `@stripe/stripe-react-native@0.74.0`

- Delta-ingested work item `github-8c278ff4d85ab465db92` from `0.73.0` to exact SHA `a628bc062f7018946d306e9e41b6ed5d75560cbc` after serial review of all 21 required evidence and context paths.
- Added per-request iOS Apple Pay `supportedNetworks` restriction and native dependency updates to Stripe Android `23.15.0` and Stripe iOS `26.6.0`.
- Recorded the exact-SHA experimental Connect notification-banner implementation while preserving its non-root-exported, non-GA boundary.

## [2026-09-01] ingest | stripe/stripe-react-native `@stripe/stripe-react-native@0.73.0`

- Delta-ingested work item `github-0d48eb279179bbd22a39` from `0.72.0` to exact SHA `8b1bc1370bd493baee8e692dbff54c973e311db2` after serial review of all 20 required evidence and context paths.
- Added private-preview Link billing collection and appearance controls, Crypto Onramp Tempo typing, and native dependency updates to Stripe Android `23.14.0` and Stripe iOS `26.5.0`.
- Recorded the implementation-backed iOS correction that reads deferred-intent `captureMethod` from `intentConfiguration.mode`, while preserving preview, eligibility, and delegated-native-runtime boundaries.

## [2026-09-01] ingest | stripe/react-stripe-js `@stripe/react-stripe-js@6.8.2`

- Delta-ingested work item `github-63d1c788da3330896fd0` from `6.8.1` to exact SHA `c48d6515c48da2fa5e2eefc9c8168b95e3026ef2` after serial review of all 11 required evidence and context paths.
- Added trusted-pricing, client-secret, readiness, loading, duplicate-submit, confirmation-error, and server-response checks from the strengthened Checkout Sessions example.
- Preserved the runtime boundary: only README guidance and the package version changed, and removing the full Payment Intents snippet does not establish deprecation.

## [2026-09-01] ingest | stripe/react-stripe-js `@stripe/react-stripe-js@6.8.1`

- Delta-ingested work item `github-87a18c639834d62a679f` from `6.8.0` to exact SHA `e8146742ffe374ff54301cbdc6fb566e3218a220` after serial review of all 69 required evidence and context paths.
- Recorded Checkout Sessions with `ui_mode: 'elements'` as the recommended path for most new custom React checkout pages while preserving the lower-level Payment Intents path for existing or finer-control integrations.
- Recorded typed TSX demos, Storybook 10, Node 24, and development-dependency updates while preserving the evidence boundary that public-source edits were formatting-only and no public runtime API or peer range changed.

## [2026-09-01] ingest | stripe/stripe-js `@stripe/stripe-js@9.15.0`

- Delta-ingested work item `github-7744a04feefa263d4371` from `9.14.0` to exact SHA `9c83132a5333ffd757be55c75f44524023b5a39e` after serial review of all 12 required evidence and context paths.
- Added `metadata?: MetadataParam` to the retained `stripe.createConfirmationToken()` parameter contract and `buttonBoxShadow?: string` to Elements appearance variables.
- Preserved the loader/runtime boundary: no dependency, loader, removal, or hosted-runtime implementation change was established, and declaration presence does not prove rollout or merchant eligibility.

## [2026-08-31] ingest | stripe/stripe-terminal-android `stripeterminal@5.8.0`

- Full-ingested work item `github-647016eaa69d9b32d93d` at exact SHA `b3de15b57201df0aa0e0235ccbe8e81bf9abaa8f` after serial review of all 88 required evidence paths.
- Established cumulative and package-qualified pages for Android permissions and lifecycle, initialization, reader discovery and connection, Tap to Pay, payments, SetupIntents, refunds, offline forwarding, reader settings and updates, and support lifecycle.
- Preserved the proprietary-runtime boundary, backend ConnectionToken/capture/reconciliation responsibilities, device and merchant eligibility constraints, and patch-versus-baseline attribution.
- Attributed coarse-location sufficiency, Bluetooth manifest changes, buzzer controls, printer low-battery handling, and Keystore, slow-update, and Tap to Pay PIN fixes specifically to `5.8.0`.

## [2026-08-31] ingest | stripe/stripe-terminal-ios `StripeTerminal@5.8.0`

- Full-ingested work item `github-7b9dc5a5eae785348011` at exact SHA `c027d6dc2258c774412cb7933cbb959488c16b63` after serial review of all 196 required evidence paths.
- Established cumulative and package-qualified pages for initialization, reader discovery and connection, Tap to Pay, payments, SetupIntents, in-person refunds, offline forwarding, reader updates, QR methods, and support lifecycle.
- Preserved the proprietary-runtime boundary, backend ConnectionToken/capture/reconciliation responsibilities, preview and firmware constraints, and conditional iOS USB evidence.
- Attributed buzzer controls, expanded SetupIntent PaymentMethods, granular logging, unknown-device handling, printer low-battery error, disconnect corrections, and the Tap to Pay crash fix specifically to `5.8.0`.

## [2026-08-28] ingest | stripe/stripe-apps `default-branch@9b14b71`

- Full-ingested work item `github-963480d18adba0763347` at exact SHA `9b14b71be496ca299401b3303b572856fd19baf4` after serial review of the complete 72-file retained capsule and required Stripe context.
- Established cumulative and commit-qualified sources plus [[stripe-apps]] for standard, local-development, and extension manifests; Dashboard UI-extension architecture; and the complete retained full-page example.
- Preserved the mock-only data boundary, independent `@stripe/ui-extension-sdk` release history, preview-mode warning, and payment-permission versus payment-behavior distinction.
- Recorded the contradiction between the retained standard schema and example manifest instead of presenting the example as a universal template.

## [2026-08-27] ingest | stripe/sync-engine `default-branch@93321ab`

- Full-ingested work item `github-d7a121b45c762cec959d` at exact SHA `93321ab3644d5460213725abe0595247c403eb46` after serial full reading of all 105 required evidence and context paths.
- Established cumulative and commit-qualified sources for OpenAPI-driven Stripe discovery, account-qualified records, resumable backfill, live events and verified webhooks, PostgreSQL destination/state behavior, and Temporal lifecycle workflows.
- Preserved the experimental/internal deployment boundary, unauthenticated `/internal/query` risk, partial-stream failure semantics, active-fork separation, and documentation drift.
- Recorded workspace version `0.2.5` only as metadata; the retained baseline remains default-branch commit `93321ab` because no matching release tag was collected.

## [2026-08-15] ingest | stripe/link-cli `@stripe/link-cli@0.13.0`

- Full-ingested work item `github-62b2da34c81f87c986c9` at exact SHA `d540389e030d0f475a6b85cd64ccaf978ff498ac` after serial full reading of all 110 required evidence paths.
- Established the cumulative source, package-qualified changelog, and [[stripe-link-cli]] concept for device authentication, approval-gated spend requests, virtual cards, SPT/MPP, Link Pay Token, MCP modes, and financial insights.
- Preserved the consumer-wallet and US-account boundaries, private internal SDK status, disabled Web Bot Auth command registration, one-time SPT rule, credential/server security constraints, and stale `0.11.0` metadata in skill files retained at package release `0.13.0`.
- Attributed only financial-insight command exposure and duplicate spend-request messaging to exact release `0.13.0`; broader behavior remains initial baseline evidence.

## [2026-08-15] ingest | stripe/stripe-php `stripe-php@21.2.0`

- Full-ingested work item `github-0ff215c1739732ae4751` at exact SHA `edf8118f0b96d69f06f372da9168d613d1aed072` after serial full reading of all 470 required evidence paths.
- Established the cumulative PHP server SDK source, package-qualified changelog, and [[stripe-php-sdk]] concept for client services, v1/v2 encoding, errors, retries/idempotency, webhooks, Checkout, PaymentIntents, billing, and Terminal.
- Recorded PHP 7.2+ support, API `2026-07-29.dahlia`, default telemetry, timeout reconciliation risk, and the trust boundary around v21.2.0 event parsers that skip verification.
- Attributed only the event-notification, parser, signature-generation, annotation, and major-version-constant items to the exact 21.2.0 release; broader behavior remains initial baseline evidence.

## [2026-08-14] ingest | stripe/stripe-cli `stripe-cli@1.50.0`

- Full-ingested work item `github-feef8fcc377f52acf591` at exact SHA `a6f40658b99e4142fd63b2e4b560aa9c7ae337b1` after the ordered full-byte read and hash check of all 147 required evidence paths.
- Established the cumulative source, package-qualified changelog, and [[stripe-cli]] concept for API commands, fixtures, triggers, webhook forwarding, authentication contexts, and request controls.
- Preserved fixture payloads as test recipes rather than canonical API guarantees and recorded the one-time 28-test-file capsule exception.
- Attributed only agent host and self-reported agent identifiers to the exact `1.50.0` release note; the broader capabilities remain baseline evidence.

## [2026-08-13] ingest | stripe/ai `main@1953b6c`

- Full-ingested work item `github-39ab9debac014faec1c5` at exact SHA `1953b6cce7344d880a054c42b8dd21ca3e50ebd5` after serial full reading of all 212 required evidence paths.
- Added an independently package-qualified baseline for `@stripe/ai-sdk@0.1.3`, `@stripe/token-meter@0.1.0`, `@stripe/mcp@0.3.3`, `@stripe/agent-toolkit@0.9.1`, and `stripe-agent-toolkit@0.7.0`, plus skills, provider manifests, and benchmarks.
- Recorded private-preview access, proxy tool-calling limits, fire-and-forget meter-delivery risk, remote MCP dependency, toolkit migration requirements, and benchmark methodology.
- Preserved contradictions between runtime source and examples/readmes instead of promoting stale guidance as package behavior.

## [2026-08-08] ingest | stripe/stripe-node `22.4.0`

- Approved and processed work item `github-e923ffd86b6fd634a620` in full mode at exact SHA `57626dcdfb94164fc9f112dfaa3c57aec5130e4f`.
- Read the retained release records and exact-SHA source capsule, including repository metadata, runtime and transport implementation, generated checkout/payment/billing resources, webhook examples, and complete upstream version inventory.
- Migrated the legacy `wiki/sources/source-github-stripe-node.md` page to `wiki/sources/stripe/github/source-github-stripe-node.md`, preserving the validated `stripe@22.1.1` baseline rather than overwriting it.
- Added [[changelog-github-stripe-node]] and advanced the retained package/API baseline to `stripe@22.4.0`, Stripe API `2026-07-29.dahlia`, and OpenAPI marker `v2349`.
- Recorded server-versus-browser responsibility, runtime exports, typed resource methods, retries/idempotency, webhook and V2 event verification, pagination/search boundaries, TypeScript versioning, and release-specific Checkout, PaymentIntent, SetupIntent, Payment Link, subscription, invoice, and refund changes.
- Corrected stale concept claims and preserved the v22.4.0 contradiction between the README's one-retry default and the constructor source's fallback value of two; deterministic integrations should configure the value explicitly.

## [2026-05-08] ingest | stripe/stripe-node `22.1.1`

- Cloned exact SHA `1899375db06ae1e102a93637e193f8c9cb1de831` and retained 14 key files under `raw/github-stripe-node/` plus navigation record `raw/github-stripe-node.md`.
- Established the initial Stripe Node source and [[stripe-node-sdk]] concept against OpenAPI marker `v2252`.
- Recorded the resource pattern, seven common error classes, V1 webhook verification, automatic pagination, retry/idempotency behavior, and PaymentIntent and Checkout Session methods.
