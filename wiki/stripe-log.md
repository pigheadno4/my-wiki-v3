---
title: "Stripe Collection and Ingest Log"
type: log
tags: [stripe, github-repository, operations]
---

> Stripe-specific collection and ingest history. The root [[log]] keeps a concise cross-provider chronology.

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
