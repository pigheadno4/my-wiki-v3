---
title: "Braintree"
type: company
tags: [braintree, payments, checkout, graphql, javascript-sdk, node-js-sdk, php-sdk, android-sdk, ios-sdk]
source_count: 9
---

## Overview

Braintree is represented in this wiki by nine independently tracked repositories: the GraphQL API contract, Node.js and PHP server SDKs, modular Braintree Web SDK, prebuilt Braintree Web Drop-in UI, native Braintree Android and iOS SDKs, and separately versioned Android and iOS Drop-in UIs. Client SDKs produce payment-method nonces for server processing; the server SDKs perform gateway operations. The GraphQL schema describes a separate API contract. Their commit or package identities and evidence histories remain separate.

## GraphQL API Contract

The `braintree/graphql-api` baseline at exact commit `3a89f42` exposes the GraphQL contract for transaction authorization, charge, capture, partial capture, refunds and voids; client tokens, tokenization and vaulting; PayPal one-time payments and billing agreements; Venmo payment contexts; 3D Secure; and recurring billing plans and subscriptions.

The schema is field-level contract evidence, not proof of merchant enablement or client-SDK support. Integration questions should combine it with the appropriate Web, Android, iOS, or server SDK source rather than treating schema presence as an end-to-end capability claim.

## Node.js Server SDK Surface

`braintree@3.39.0` provides gateway configuration, client-token generation, customer and payment-method vault operations, transaction authorization and settlement, refunds and voids, PayPal and Venmo instruments, card verification and 3DS data, plans and subscriptions, and signed webhook parsing.

The server SDK does not render checkout. Browser or native SDKs collect approval or payment data and return a nonce or token to the merchant server. PayPal customer sessions are restricted to authorized merchants, and legacy Venmo SDK transaction parameters warn merchants to migrate to Pay with Venmo.

## PHP Server SDK Surface

`braintree_php@6.37.0` provides PHP gateway configuration, client-token generation, customer and payment-method vault operations, transaction authorization and settlement, refunds and voids, PayPal and Venmo instruments, plans and subscriptions, and signed webhook parsing.

The PHP package requires PHP 7.3 or later and supports key credentials or OAuth credentials without mixing them. Webhook signature verification specifically requires public/private API keys. The exact release hardens Address and Dispute path IDs, adds PayPal email validation codes, and adds preferred-payment-method context to client-token generation.

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

## Android Drop-in Surface

`drop-in@6.17.0` provides a prebuilt Android payment-selection experience for cards, PayPal, Venmo, Google Pay, saved methods, vault management, card 3D Secure, and device-data collection. It requires Android API 21+ and pins Braintree Android `4.50.0`, so behavior from the independently retained `braintree-android@5.30.0` modular SDK cannot be attributed to it.

Most selections return a nonce for server processing. PayPal defaults to a vault request, Venmo defaults to single use, and Venmo visibility requires remote enablement plus an available Venmo app switch at this baseline. Customer-scoped client tokens enable saved-method retrieval and deletion.

## iOS SDK Surface

`braintree-ios@7.9.0` provides modular native clients for cards, PayPal, Venmo, Apple Pay, local payments, SEPA, 3D Secure, fraud data, Shopper Insights, messaging, and payment UI. It requires iOS 16+, Xcode 16.2+, and Swift 5.10+.

PayPal supports separate checkout and vault requests, including billing-agreement consent and recurring metadata. Venmo is a separate native Braintree module using universal-link app switch with browser fallback and conditional multi-use vaulting. Apple Pay support creates and tokenizes a native payment request; the demo's recurring sheet does not by itself establish later merchant charges.

## iOS Drop-in Surface

`BraintreeDropIn@9.14.0` provides a prebuilt UIKit payment-selection experience for cards, PayPal, Venmo, Apple Pay, saved methods, vault management, and card 3D Secure. It supports iOS 12+ and requires `braintree_ios` 5.27.0, so behavior from the independently retained `braintree-ios@7.9.0` modular SDK cannot be attributed to it.

Most selections return a nonce for server processing. Apple Pay selection returns only a method type and requires the merchant to present and tokenize the Apple Pay sheet separately. Venmo visibility additionally requires remote enablement and an installed Venmo app at this baseline.

## Versioned Implementation Knowledge

The retained history begins with `braintree-web@3.143.0` and currently reaches `3.144.0` at exact SHA `41460fba05c1ea1222e795b36a10765a6699b8e7`. The newer release adds PayPal View/Edit Funding Instrument, expands PayPal Checkout v6 session options, and prevents failed incognito detection from aborting Venmo creation while preserving the 23-component architecture.

Repository evidence is not current enablement guidance. PayPal, Venmo, and Fastlane modules have configuration or delegated-runtime boundaries, and legacy source modules should not be treated as recommendations for new integrations.

## Knowledge Status

- Ingested cumulative GitHub repository sources: 9
- Ingested package releases: 9
- Latest retained GraphQL API ref: `default-branch@3a89f42` at `3a89f427466a0a978dbfcfd953913f4e76c3264a`
- Latest retained Braintree Node release: `braintree@3.39.0` at `7a9270aaf31eb87819add64a768652243f90007c`
- Latest retained Braintree PHP release: `braintree_php@6.37.0` at `0f53ece38397c9fed05b94620634a5a23ef8ee48`
- Latest retained Braintree Web release: `braintree-web@3.144.0` at `41460fba05c1ea1222e795b36a10765a6699b8e7`
- Latest retained Drop-in release: `braintree-web-drop-in@1.47.0` at `ec1c7c533c2e878545f2b25505c56b7e22dc1c17`
- Latest retained Android release: `braintree-android@5.30.0` at `51f183a48557d0fd00eefa541712df0c4f21ee28`
- Latest retained Android Drop-in release: `drop-in@6.17.0` at `da8a702bb37e3a4567e5ba4dd8cbc2257acc37c7`
- Latest retained iOS release: `braintree-ios@7.9.0` at `4e987ca19f03b65a0d303b4c3ec95e0c723be971`
- Latest retained iOS Drop-in release: `BraintreeDropIn@9.14.0` at `d951d104ac960188824bda191be2f57c57351a31`

## Sources

- [[source-github-graphql-api]] - commit-qualified GraphQL API contract
- [[changelog-github-graphql-api]] - GraphQL schema history
- [[source-github-braintree-node]] - cumulative Node.js server SDK implementation baseline
- [[changelog-github-braintree-node]] - package-qualified Node.js release ledger
- [[source-github-braintree-php]] - cumulative PHP server SDK implementation baseline
- [[changelog-github-braintree-php]] - package-qualified PHP release ledger
- [[source-github-braintree-web]] — cumulative Braintree Web implementation baseline
- [[changelog-github-braintree-web]] — package-qualified release ledger
- [[source-github-braintree-web-drop-in]] - cumulative Drop-in implementation baseline
- [[changelog-github-braintree-web-drop-in]] - package-qualified Drop-in release ledger
- [[source-github-braintree-android]] - cumulative native Android implementation baseline
- [[changelog-github-braintree-android]] - package-qualified Android release ledger
- [[source-github-braintree-android-drop-in]] - cumulative prebuilt Android Drop-in implementation baseline
- [[changelog-github-braintree-android-drop-in]] - package-qualified Android Drop-in release ledger
- [[source-github-braintree-ios]] - cumulative native iOS implementation baseline
- [[changelog-github-braintree-ios]] - package-qualified iOS release ledger
- [[source-github-braintree-ios-drop-in]] - cumulative prebuilt iOS Drop-in implementation baseline
- [[changelog-github-braintree-ios-drop-in]] - package-qualified iOS Drop-in release ledger

## Related

- [[braintree-index]] — Braintree catalog and operations links
- [[braintree-log]] — collection and ingest history
- [[braintree-web-sdk]] — browser SDK concept
- [[braintree-server-sdk]] - shared server integration boundary and package-qualified evidence rules
- [[braintree-web-drop-in]] - prebuilt checkout UI and migration boundary
- [[braintree-android-sdk]] - native Android request, launcher, nonce, PayPal, and Venmo model
- [[braintree-ios-sdk]] - native iOS nonce, PayPal, Venmo, Apple Pay, and migration model
- [[paypal-braintree-integration]] — Braintree PayPal v6 processing boundary
