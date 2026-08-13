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

`drop-in@6.17.0` is a separately versioned prebuilt UI pinned to Braintree Android `4.50.0`, not the retained modular `5.30.0` source. It presents eligible cards, PayPal, Venmo, and Google Pay and returns a nonce plus device data for server processing.

At this Drop-in baseline, PayPal defaults to vaulting, Venmo defaults to single use, and Venmo visibility requires remote enablement plus an available Venmo app switch. Saved-method retrieval and deletion require a customer-scoped client token. These statements must not be replaced with newer modular-SDK behavior without a compatible Drop-in release.

## Version Boundary

Release `5.30.0` makes the principal Kotlin suspend functions public, removes the unsupported Visa Checkout module, deprecates its remaining configuration fields, targets Android API 37 for compilation, and fixes PayPal/Venmo button sizing. Historical migration and removal notes remain context until their exact versions are separately retained.

## Related

- [[source-github-braintree-android]] - cumulative exact-SHA implementation evidence
- [[changelog-github-braintree-android]] - package-qualified release ledger
- [[source-github-braintree-android-drop-in]] - independently versioned prebuilt Android Drop-in baseline
- [[changelog-github-braintree-android-drop-in]] - package-qualified Android Drop-in release ledger
- [[braintree-web-sdk]] - independently versioned browser SDK
- [[braintree-web-drop-in]] - independently versioned prebuilt browser UI
- [[paypal-android-sdk]] - standalone PayPal Android SDK and Venmo contradiction boundary
- [[braintree]] - company page
