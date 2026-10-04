---
title: "Braintree Android SDK"
type: concept
category: technology
tags: [braintree, android, mobile, kotlin, paypal, venmo, cards, 3d-secure]
---

## Braintree Android SDK

Braintree Android is a modular native SDK for accepting card and alternative payments in Android applications. Payment-specific clients create authorization requests, launch any required wallet, browser, or app-switch experience, and tokenize successful returns into Braintree payment-method nonces for server processing.

## Current Baseline

The first retained modular baseline is `braintree-android@5.30.0` at exact SHA `51f183a48557d0fd00eefa541712df0c4f21ee28`. It supports Android API 23+, Java 11, and Kotlin 1.9.10.

The source includes Card, PayPal, Venmo, Google Pay, Local Payment, SEPA, 3D Secure, Data Collector, Shopper Insights, PayPal Messaging, American Express, and UIComponents modules. Capability in source does not prove merchant or buyer eligibility.

## Redirect and Nonce Model

Redirect-capable modules use a request, launcher, and result pattern. The merchant application must preserve the pending payment request, handle the app-link or deep-link return, and then tokenize the successful result. The resulting nonce belongs to a Braintree server flow, not a direct PayPal Orders API integration.

## PayPal and Venmo Boundary

PayPal and Venmo are separate Braintree modules:

- PayPal supports checkout, vault, checkout-with-vault billing agreements, recurring-billing metadata, and optional PayPal app switch with browser fallback.
- Venmo supports the Venmo app or mobile browser, single-use and multi-use requests, and conditional vaulting with a customer-scoped client token.

Venmo is not a PayPal funding-source enum in this SDK. This Braintree Venmo path is also independent from `paypal/paypal-android@2.3.0`, which does not expose a native Venmo integration in its retained source.

## Drop-in Boundary

Website customization guidance warns against enabling Vault Manager for recurring-billing integrations because customers could delete payment methods associated with subscriptions. This is a Drop-in configuration warning, not evidence of subscription cancellation behavior or exact package compatibility. [[source-braintree-drop-in-customization-android-v5]]

`drop-in@6.17.0` is a separately versioned prebuilt UI pinned to Braintree Android `4.50.0`, not the retained modular `5.30.0` source. It presents eligible cards, PayPal, Venmo, and Google Pay and returns a nonce plus device data for server processing.

At this Drop-in baseline, PayPal defaults to vaulting, Venmo defaults to single use, and Venmo visibility requires remote enablement plus an available Venmo app switch. Saved-method retrieval and deletion require a customer-scoped client token. These statements must not be replaced with newer modular-SDK behavior without a compatible Drop-in release.

## Version Boundary

Release `5.30.0` makes the principal Kotlin suspend functions public, removes the unsupported Visa Checkout module, deprecates its remaining configuration fields, targets Android API 37 for compilation, and fixes PayPal/Venmo button sizing. Historical migration and removal notes remain context until their exact versions are separately retained.

## Related
- [[source-braintree-premium-fraud-management-tools-client-side-android-v5]] - Android v5-routed Data Collector guide for device-data collection, server-request handoff, consent and location-disclosure responsibility, plus a historical mobile-certificate notice; not current package-support or named fraud-product evidence
- [[source-braintree-3d-secure-advanced-options-android-v5]] - Android v5-routed advanced 3DS webpage snapshot for client liability-result handling and specialized verification options; its embedded Drop-in lifecycle notice is not modular SDK package-compatibility evidence
- [[source-braintree-drop-in-customization-android-v5]] - Android v5-routed Drop-in customization guide for saved-method, Vault Manager, card-form, and fraud-tool configuration; source-specific lifecycle and package-version boundaries apply
- [[source-braintree-drop-in-setup-and-integration-android-v5]] - Android v5-routed Drop-in setup snapshot for client authorization, method-specific prerequisites, customer-scoped saved-method lookup, browser-switch overrides, and its source-specific 2026/2027 lifecycle notice; not proof of modular v5 package compatibility or current support

- [[source-braintree-credit-cards-client-side-android-v5]] - Android v5 website guide to standard Card Fields UI ownership, SDK 5.29.0-or-higher `ui-components` prerequisite, client authorization, tokenization and nonce handoff; not current package-support or execution evidence
- [[source-braintree-authorization-tokenization-key-android-v5]] - historical Android v5 client-authorization guide for static reduced-privilege tokenization keys, their lifecycle, environment binding, and capability limits; not current SDK-support evidence
- [[source-braintree-client-sdk-setup-android-v5]] - historical Android client SDK v5 setup snapshot for captured environment requirements, modular dependencies, return routing, authorization choices, and the dated mobile-certificate warning; not current package support
- [[source-braintree-client-sdk-migration-android-v5]] - historical website guide for migrating Braintree Android SDK v4 integrations to v5; not current package-support evidence
- [[source-braintree-client-sdk-deprecation-policy-android-v5]] - historical website-policy snapshot for Android client-SDK semantic versioning, release-time platform support, and status/deprecation-date lookup; current package support remains under separate GitHub evidence
- [[source-braintree-paypal-messaging-javascript-v3]] - snapshot route whose retained body states Pay Later Messaging availability for merchants using the latest native iOS and Android SDKs, requires native-app integration eligibility and excludes Drop-in

- [[source-github-braintree-android]] - cumulative exact-SHA implementation evidence
- [[changelog-github-braintree-android]] - package-qualified release ledger
- [[source-github-braintree-android-drop-in]] - independently versioned prebuilt Android Drop-in baseline
- [[changelog-github-braintree-android-drop-in]] - package-qualified Android Drop-in release ledger
- [[braintree-web-sdk]] - independently versioned browser SDK
- [[braintree-web-drop-in]] - independently versioned prebuilt browser UI
- [[paypal-android-sdk]] - standalone PayPal Android SDK and Venmo contradiction boundary
- [[braintree]] - company page
