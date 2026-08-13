---
title: "Braintree Collection and Ingest Log"
type: log
tags: [braintree, github-repository, operations]
---

> Braintree-specific collection and ingest history. The root [[log]] keeps a concise cross-provider chronology.

## [2026-08-13] ingest | braintree/braintree-android-drop-in `drop-in@6.17.0`

- Approved and processed work item `github-64aa2131b6b057d2f41c` in full mode at exact SHA `da8a702bb37e3a4567e5ba4dd8cbc2257acc37c7`.
- Read and hash-audited the complete 168-path, 506,105-byte retained packet, including implementation, public API, demo, localization, Gradle metadata, migration guidance, changelog, and presentation resources.
- Established an independent cumulative source and package-qualified changelog for payment selection, nonce handoff, cards, PayPal, Venmo, Google Pay, saved methods, vault management, 3DS, device data, and redirect handling.
- Preserved the critical dependency boundary: `6.17.0` pins Braintree Android `4.50.0` and must not inherit behavior from the independently retained `braintree-android@5.30.0` source.

## [2026-08-13] ingest | braintree/braintree-ios-drop-in `BraintreeDropIn@9.14.0`

- Approved and processed work item `github-92242b9e450d596215e2` in full mode at exact SHA `d951d104ac960188824bda191be2f57c57351a31`.
- Read and hash-audited the complete 203-file retained capsule, including implementation, public API, demos, localization, package metadata, changelog, and generated presentation assets.
- Established an independent cumulative source and package-qualified changelog for payment selection, nonce handoff, cards, PayPal, Venmo, Apple Pay, saved methods, vault management, 3DS, device data, and UIKit customization.
- Preserved the critical dependency boundary: `9.14.0` requires `braintree_ios` 5.27.0 and must not inherit behavior from the independently retained `braintree-ios@7.9.0` source.

## [2026-08-11] ingest | braintree/graphql-api `default-branch@3a89f42`

- Approved and processed work item `github-d36f782cded039bfef90` in full mode at exact SHA `3a89f427466a0a978dbfcfd953913f4e76c3264a`.
- Read and hash-verified the three-file, 598,607-byte capsule containing the complete GraphQL schema, upstream changelog, and README.
- Established an independent cumulative API-contract source and commit-qualified changelog for transactions, client tokens, vaulting, PayPal, Venmo, 3DS, recurring billing, and broader inventory-level domains.
- Kept schema presence separate from merchant enablement and SDK implementation, and updated the Braintree company and provider index without merging this evidence into `braintree_node`.

## [2026-08-09] ingest | braintree/braintree_node `3.39.0`

- Approved and processed work item `github-a3e31c47bd77ac327a7b` in full mode.
- Read and hash-verified all 173 required paths, including the complete 170-file, 365,394-byte exact-SHA capsule at `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/manifest.json`.
- Established the cumulative Node.js server source and package-qualified release ledger; recorded gateway transport, client tokens, vaulting, transaction lifecycle and idempotency, PayPal/Venmo boundaries, cards and 3DS, subscriptions, webhooks, and error semantics.
- Isolated exact `3.39.0` scope to PayPal email validation codes, 3DS pass-through network fields, and preferred-payment-method client-token support; the upstream release-note body was unavailable.
- Kept disputes, OAuth, onboarding, reporting, disbursement, and facilitator APIs at inventory depth and updated the Braintree company and provider index.

## [2026-08-01] ingest | braintree/braintree_ios `7.9.0`

- Approved and processed work item `github-2968099ae6a7549cd6a9` in full mode.
- Read and hash-verified the complete 285-file, 1,063,508-byte exact-SHA capsule at `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/manifest.json` plus its release record and snapshot manifest.
- Established the cumulative iOS source and release ledger; recorded authorization and nonce boundaries, modular payment clients, PayPal checkout/vault/app switch, native Venmo app/browser and vaulting rules, Apple Pay, cards, 3DS, Shopper Insights, UI components, and server responsibilities.
- Isolated exact `7.9.0` scope to the BraintreeUIComponents iOS 16 deployment-target correction and kept broader v7 migration behavior as cumulative baseline context.
- Created the iOS SDK concept and updated Braintree, PayPal/Braintree, recurring-payment, company, and provider-index knowledge without conflating standalone PayPal iOS evidence.

## [2026-08-01] ingest | braintree/braintree_android `5.30.0`

- Approved and processed work item `github-8bf8fabdfdc1687790bd` in full mode.
- Read and hash-verified the complete 388-file, 1,171,992-byte exact-SHA capsule at `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/manifest.json`.
- Established the cumulative Android source and release ledger; recorded native request/launcher/result handling, card and 3DS paths, PayPal checkout and vaulting, separate Venmo app/browser and multi-use vault behavior, Shopper Insights, UI components, and merchant-enablement boundaries.
- Isolated exact `5.30.0` changes: public suspend APIs, Visa Checkout removal and configuration deprecation, Android API 37 build targets, and PayPal/Venmo button sizing.
- Created the Android SDK concept and updated the Braintree company and provider index without merging standalone PayPal Android evidence.

## [2026-07-28] ingest | braintree/braintree-web-drop-in `1.47.0`

- Approved and processed work item `github-88d13a8f0c219387aab4` in full mode.
- Read and hash-verified the complete 86-file, 466,847-byte exact-SHA capsule at `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/manifest.json`.
- Established an independent cumulative source and release ledger for the prebuilt UI; recorded payment views, vaulted-method handling, 3DS, fraud data, localization, and sanitization changes.
- Recorded the `braintree-web@3.123.2` dependency boundary and scheduled 2026 deprecation/2027 unsupported milestones; created the Drop-in concept and updated the Braintree company and provider index.

## [2026-07-28] ingest | braintree/braintree-web `3.144.0`

- Approved and processed work item `github-236dd1f1ac8a3f30f537` in full mode.
- Verified the 330-file exact-SHA capsule at `raw/github/braintree/braintree-web/snapshots/2026-07-28-41460fb/manifest.json`: 319 files are byte-identical to `3.143.0`, 10 changed, and one Edit FI story was added.
- Preserved the `3.143.0` baseline while adding PayPal View/Edit Funding Instrument, PayPal Checkout v6 session options, the Venmo incognito-detection fallback, and the `framebus@6.1.0` update.
- Updated the cumulative source, release ledger, Braintree company, two existing concepts, and provider index; no new source or concept page was required.

## [2026-07-28] ingest | braintree/braintree-web `3.143.0`

- Approved and processed work item `github-1ab2662d292502a53058` in full mode.
- Read and hash-verified the complete 329-file, 2,162,444-byte exact-SHA capsule at `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/manifest.json`; 27 stories were retained and five mocks were excluded as tests.
- Established the cumulative source and package-qualified release ledger at exact SHA `bae582d791026c143abb91c3bdcada92b8c060f6`.
- Recorded client/nonce architecture, Hosted Fields, 3D Secure, PayPal Checkout v6, Venmo, wallets, local and bank methods, risk data, Payment Ready, and delegated runtime boundaries.
- Created the Braintree company, concept, and provider index; extended [[paypal-braintree-integration]] with independent Braintree Web evidence.
