---
title: "Braintree"
type: company
tags: [braintree, payments, checkout, graphql, javascript-sdk, node-js-sdk, php-sdk, ruby-sdk, android-sdk, ios-sdk, popup-bridge, webview, developer-tooling, github-actions]
source_count: 13
---

## Overview

Braintree is represented in this wiki by thirteen independently tracked repositories: the GraphQL API contract, Node.js, PHP, and Ruby server SDKs, modular Braintree Web SDK, prebuilt Braintree Web Drop-in UI, native Braintree Android and iOS SDKs, separately versioned Android and iOS Drop-in UIs, independent Android and iOS PopupBridge WebView transports, and shared mobile SDK review tooling. Client SDKs produce payment-method nonces for server processing; the server SDKs perform gateway operations; PopupBridge only transports browser popup results; and mobile SDK tooling only coordinates engineering review. The GraphQL schema describes a separate API contract. Their commit or package identities and evidence histories remain separate.

## GraphQL API Contract

The `braintree/graphql-api` baseline at exact commit `3a89f42` exposes the GraphQL contract for transaction authorization, charge, capture, partial capture, refunds and voids; client tokens, tokenization and vaulting; PayPal one-time payments and billing agreements; Venmo payment contexts; 3D Secure; and recurring billing plans and subscriptions.

The schema is field-level contract evidence, not proof of merchant enablement or client-SDK support. Integration questions should combine it with the appropriate Web, Android, iOS, or server SDK source rather than treating schema presence as an end-to-end capability claim.

## Node.js Server SDK Surface

`braintree@3.39.0` provides gateway configuration, client-token generation, customer and payment-method vault operations, transaction authorization and settlement, refunds and voids, PayPal and Venmo instruments, card verification and 3DS data, plans and subscriptions, and signed webhook parsing.

The server SDK does not render checkout. Browser or native SDKs collect approval or payment data and return a nonce or token to the merchant server. PayPal customer sessions are restricted to authorized merchants, and legacy Venmo SDK transaction parameters warn merchants to migrate to Pay with Venmo.

## PHP Server SDK Surface

`braintree_php@6.37.0` provides PHP gateway configuration, client-token generation, customer and payment-method vault operations, transaction authorization and settlement, refunds and voids, PayPal and Venmo instruments, plans and subscriptions, and signed webhook parsing.

The PHP package requires PHP 7.3 or later and supports key credentials or OAuth credentials without mixing them. Webhook signature verification specifically requires public/private API keys. The exact release hardens Address and Dispute path IDs, adds PayPal email validation codes, and adds preferred-payment-method context to client-token generation.

## Ruby Server SDK Surface

`braintree@4.40.0` provides Ruby gateway configuration, client-token generation, customer and payment-method vault operations, transaction authorization and settlement, refunds and voids, PayPal and Venmo instruments, plans and subscriptions, and signed webhook parsing.

The active 4.x package requires Ruby 2.6 or later and supports key credentials or OAuth credentials without mixing them. Its exact release hardens Address and Dispute path IDs, adds PayPal email validation codes, and adds network-qualified 3DS pass-through fields. Unlike the retained Node and PHP baselines, its client-token signature does not expose `preferredPaymentMethodToken`.

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

## iOS PopupBridge Surface

`PopupBridge@3.1.0` adapts PayPal or Braintree web checkout running inside `WKWebView`: JavaScript requests a popup, native code opens `ASWebAuthenticationSession`, and the validated return URL is delivered to the page. It requires iOS 16+, Xcode 16.2+, and Swift 5.10+.

Exact release `3.1.0` adds a merchant return-scheme initializer for Venmo app switch. The bridge reports whether Venmo is installed and can advertise the merchant scheme to Braintree Web, but it does not enable Venmo, create a payment session, tokenize a payment, or process a transaction. Its README lists PayPal SDK v5 as supported and v6 or later as unsupported.

The retained podspec, privacy manifest, and PayPal data-collector guide conflict with the exact runtime: the podspec names the replaced browser controller, the privacy manifest has blank declarations despite analytics metadata transmission, and the guide uses delegate callbacks removed in v2. See [[source-github-popup-bridge-ios]] for the exact boundaries.

## Android PopupBridge Surface

`popup-bridge@5.3.0` adapts a web checkout running inside an Android WebView by exposing a JavaScript interface, opening popup URLs through Braintree Browser Switch, persisting the pending request, and returning deep-link data to the page. The exact build requires Android API 23+, targets API 37, and uses Browser Switch `3.5.1`.

The host activity owns the deep link, must use `PopupBridgeWebViewClient`, and must forward return intents through `handleReturnToApp()`. Venmo installation state is injected after page load. As on iOS, this is transport evidence rather than payment-session, tokenization, merchant-enablement, or processing evidence.

The retained Android README and migration guides conflict with the exact runtime on minimum SDK, lifecycle handling, version status, and data-collector APIs. See [[source-github-popup-bridge-android]] for the exact `5.3.0` behavior.

## Mobile SDK Developer Tooling

`braintree/mobile-sdk-tooling` at `default-branch@a3b0ffe` provides a shared GitHub Actions review digest for configured Braintree mobile SDK repositories. It authenticates with a GitHub App, reduces each reviewer's full history to the latest decisive state, applies CODEOWNER-aware approval counting and inner-source routing, and posts qualifying pull requests to Slack.

This is engineering-operations evidence only. It does not establish SDK implementation behavior, release readiness, merchant eligibility, or payment processing. Its current limitations include a 100-open-pull-request cap per repository, manual daylight-saving cron maintenance, individual-only CODEOWNER extraction, and Ubuntu/GNU shell assumptions.

## Versioned Implementation Knowledge

The retained history begins with `braintree-web@3.143.0` and currently reaches `3.144.0` at exact SHA `41460fba05c1ea1222e795b36a10765a6699b8e7`. The newer release adds PayPal View/Edit Funding Instrument, expands PayPal Checkout v6 session options, and prevents failed incognito detection from aborting Venmo creation while preserving the 23-component architecture.

Repository evidence is not current enablement guidance. PayPal, Venmo, and Fastlane modules have configuration or delegated-runtime boundaries, and legacy source modules should not be treated as recommendations for new integrations.

## Knowledge Status

- Ingested cumulative GitHub repository sources: 13
- Ingested package releases: 12
- Latest retained GraphQL API ref: `default-branch@3a89f42` at `3a89f427466a0a978dbfcfd953913f4e76c3264a`
- Latest retained Braintree Node release: `braintree@3.39.0` at `7a9270aaf31eb87819add64a768652243f90007c`
- Latest retained Braintree PHP release: `braintree_php@6.37.0` at `0f53ece38397c9fed05b94620634a5a23ef8ee48`
- Latest retained Braintree Ruby release: `braintree@4.40.0` at `1217992763cc13f33dbd8b6c51ad2ae058ddd2a8`
- Latest retained Braintree Web release: `braintree-web@3.144.0` at `41460fba05c1ea1222e795b36a10765a6699b8e7`
- Latest retained Drop-in release: `braintree-web-drop-in@1.47.0` at `ec1c7c533c2e878545f2b25505c56b7e22dc1c17`
- Latest retained Android release: `braintree-android@5.30.0` at `51f183a48557d0fd00eefa541712df0c4f21ee28`
- Latest retained Android Drop-in release: `drop-in@6.17.0` at `da8a702bb37e3a4567e5ba4dd8cbc2257acc37c7`
- Latest retained iOS release: `braintree-ios@7.9.0` at `4e987ca19f03b65a0d303b4c3ec95e0c723be971`
- Latest retained iOS Drop-in release: `BraintreeDropIn@9.14.0` at `d951d104ac960188824bda191be2f57c57351a31`
- Latest retained iOS PopupBridge release: `PopupBridge@3.1.0` at `00256b4b8c58367287fe35a442a33cd7c010a94f`
- Latest retained Android PopupBridge release: `popup-bridge@5.3.0` at `f30654168b997ea1dd95ebc61901582ae00bebb0`
- Latest retained mobile SDK tooling ref: `default-branch@a3b0ffe` at `a3b0ffe7931cde179f8b0dfdd5162979adf81683`

## Sources

- [[source-github-graphql-api]] - commit-qualified GraphQL API contract
- [[changelog-github-graphql-api]] - GraphQL schema history
- [[source-github-braintree-node]] - cumulative Node.js server SDK implementation baseline
- [[changelog-github-braintree-node]] - package-qualified Node.js release ledger
- [[source-github-braintree-php]] - cumulative PHP server SDK implementation baseline
- [[changelog-github-braintree-php]] - package-qualified PHP release ledger
- [[source-github-braintree-ruby]] - cumulative Ruby server SDK implementation baseline
- [[changelog-github-braintree-ruby]] - package-qualified Ruby release ledger
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
- [[source-github-popup-bridge-ios]] - cumulative iOS WebView popup transport baseline
- [[changelog-github-popup-bridge-ios]] - package-qualified iOS PopupBridge release ledger
- [[source-github-popup-bridge-android]] - cumulative Android WebView popup transport baseline
- [[changelog-github-popup-bridge-android]] - package-qualified Android PopupBridge release ledger
- [[source-github-mobile-sdk-tooling]] - cumulative mobile SDK review-automation baseline
- [[changelog-github-mobile-sdk-tooling]] - commit-qualified mobile SDK tooling history

## Related

- [[braintree-index]] — Braintree catalog and operations links
- [[braintree-log]] — collection and ingest history
- [[braintree-web-sdk]] — browser SDK concept
- [[braintree-server-sdk]] - shared server integration boundary and package-qualified evidence rules
- [[braintree-web-drop-in]] - prebuilt checkout UI and migration boundary
- [[braintree-android-sdk]] - native Android request, launcher, nonce, PayPal, and Venmo model
- [[braintree-ios-sdk]] - native iOS nonce, PayPal, Venmo, Apple Pay, and migration model
- [[braintree-popup-bridge]] - WebView popup transport and payment-processing boundary
- [[paypal-braintree-integration]] — Braintree PayPal v6 processing boundary
