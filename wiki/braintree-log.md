---
title: "Braintree Collection and Ingest Log"
type: log
tags: [braintree, github-repository, operations]
---

> Braintree-specific collection and ingest history. The root [[log]] keeps a concise cross-provider chronology.

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
