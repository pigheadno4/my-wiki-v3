---
title: "Braintree"
type: company
tags: [braintree, payments, checkout, javascript-sdk, android-sdk, ios-sdk]
source_count: 4
---

## Overview

Braintree is represented in this wiki by four independently versioned repositories: the modular Braintree Web SDK, the prebuilt Braintree Web Drop-in UI, and the native Braintree Android and iOS SDKs. All produce or support Braintree payment-method nonces for server processing, but their package versions and evidence histories must remain separate.

## Web SDK Surface

- Hosted Fields provides merchant-styled, Braintree-hosted card inputs.
- 3D Secure verifies card nonces and reports liability-shift outcomes.
- PayPal Checkout v6, Venmo, Fastlane, Apple Pay, and Google Pay connect external wallet experiences to Braintree processing.
- Local Payment, SEPA, US bank account, and Instant Verification cover additional payment and bank-verification paths.
- Data Collector, Payment Ready, and preferred-method signals support risk and presentation decisions but do not themselves prove eligibility.

## Drop-in Surface

`braintree-web-drop-in@1.47.0` provides an opinionated UI for cards, PayPal, PayPal Credit, Venmo, Apple Pay, and Google Pay, with vaulted-method display, optional Data Collector output, and 3D Secure verification. It pins `braintree-web@3.123.2`, not the separately retained `3.144.0` modular SDK.

The repository schedules Drop-in deprecation for 2026-09-01 and unsupported status for 2027-09-01 and directs merchants to migrate to the modular Braintree SDK. Its notice says processing will be supported for one year after deprecation, while processing on unsupported SDKs may be suspended at any time. Current support status should be rechecked for time-sensitive guidance.

## Android SDK Surface

`braintree-android@5.30.0` provides modular native clients for cards, PayPal, Venmo, Google Pay, local payments, SEPA, 3D Secure, fraud data, and payment-method presentation. Redirect-capable methods use a request/launcher/result pattern with app-link or deep-link return handling before nonce tokenization.

PayPal and Venmo are separate Braintree modules. Venmo can launch the Venmo app or a mobile browser and supports conditional multi-use vaulting with a customer-scoped client token. This is distinct from the standalone `paypal/paypal-android` SDK, whose retained `2.3.0` source does not establish a native Venmo path.

## iOS SDK Surface

`braintree-ios@7.9.0` provides modular native clients for cards, PayPal, Venmo, Apple Pay, local payments, SEPA, 3D Secure, fraud data, Shopper Insights, messaging, and payment UI. It requires iOS 16+, Xcode 16.2+, and Swift 5.10+.

PayPal supports separate checkout and vault requests, including billing-agreement consent and recurring metadata. Venmo is a separate native Braintree module using universal-link app switch with browser fallback and conditional multi-use vaulting. Apple Pay support creates and tokenizes a native payment request; the demo's recurring sheet does not by itself establish later merchant charges.

## Versioned Implementation Knowledge

The retained history begins with `braintree-web@3.143.0` and currently reaches `3.144.0` at exact SHA `41460fba05c1ea1222e795b36a10765a6699b8e7`. The newer release adds PayPal View/Edit Funding Instrument, expands PayPal Checkout v6 session options, and prevents failed incognito detection from aborting Venmo creation while preserving the 23-component architecture.

Repository evidence is not current enablement guidance. PayPal, Venmo, and Fastlane modules have configuration or delegated-runtime boundaries, and legacy source modules should not be treated as recommendations for new integrations.

## Knowledge Status

- Ingested cumulative GitHub repository sources: 4
- Ingested package releases: 5
- Latest retained Braintree Web release: `braintree-web@3.144.0` at `41460fba05c1ea1222e795b36a10765a6699b8e7`
- Latest retained Drop-in release: `braintree-web-drop-in@1.47.0` at `ec1c7c533c2e878545f2b25505c56b7e22dc1c17`
- Latest retained Android release: `braintree-android@5.30.0` at `51f183a48557d0fd00eefa541712df0c4f21ee28`
- Latest retained iOS release: `braintree-ios@7.9.0` at `4e987ca19f03b65a0d303b4c3ec95e0c723be971`

## Sources

- [[source-github-braintree-web]] — cumulative Braintree Web implementation baseline
- [[changelog-github-braintree-web]] — package-qualified release ledger
- [[source-github-braintree-web-drop-in]] - cumulative Drop-in implementation baseline
- [[changelog-github-braintree-web-drop-in]] - package-qualified Drop-in release ledger
- [[source-github-braintree-android]] - cumulative native Android implementation baseline
- [[changelog-github-braintree-android]] - package-qualified Android release ledger
- [[source-github-braintree-ios]] - cumulative native iOS implementation baseline
- [[changelog-github-braintree-ios]] - package-qualified iOS release ledger

## Related

- [[braintree-index]] — Braintree catalog and operations links
- [[braintree-log]] — collection and ingest history
- [[braintree-web-sdk]] — browser SDK concept
- [[braintree-web-drop-in]] - prebuilt checkout UI and migration boundary
- [[braintree-android-sdk]] - native Android request, launcher, nonce, PayPal, and Venmo model
- [[braintree-ios-sdk]] - native iOS nonce, PayPal, Venmo, Apple Pay, and migration model
- [[paypal-braintree-integration]] — Braintree PayPal v6 processing boundary
