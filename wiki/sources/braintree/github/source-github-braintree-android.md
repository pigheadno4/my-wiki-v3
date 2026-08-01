---
title: "GitHub: braintree/braintree_android"
type: source
date_ingested: 2026-08-01
original_format: github-repo
raw_files:
  - "github/braintree/braintree_android/snapshots/2026-08-01-51f183a/manifest.json"
tags: [braintree, android, mobile-sdk, paypal, venmo, cards, 3d-secure, github-repository]
---

## Overview

`braintree/braintree_android` contains Braintree's modular native Android SDK. The first retained baseline is package-qualified release `braintree-android@5.30.0` at exact SHA `51f183a48557d0fd00eefa541712df0c4f21ee28`.

Repository: <https://github.com/braintree/braintree_android>

## Evidence Boundary

- This exact-SHA snapshot proves implementation present in `braintree-android@5.30.0`, released on 2026-07-21. It does not prove merchant-account enablement, buyer eligibility, regional availability, or production approval for any payment method.
- Braintree Android is independent from both `paypal/paypal-android` and Braintree's browser repositories. Similar product names do not make their APIs, versions, or release histories interchangeable.
- The capsule retains production source, resources, README, changelog, migration guides, demo integration code, and stories. Tests, fixtures, generated documentation, CI, and unrelated tooling are excluded.
- The repository changelog supplies historical migration context. Only the release notes and exact `5.30.0` source establish this retained release's current delta and behavior.

## Grounding Excerpts

> "This library will help you accept card and alternative payments in your Android app."
>
> `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/README.md:6`

> "The Braintree SDK supports Android API 23 and above."
>
> `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/README.md:10`

> "If set to true, this enables the Checkout with Vault flow, where the customer will be prompted to consent to a billing agreement during checkout."
>
> `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/PayPal/src/main/java/com/braintreepayments/api/paypal/PayPalCheckoutRequest.kt:53-56`

> "Venmo app or mobile browser"
>
> `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/Venmo/src/main/java/com/braintreepayments/api/venmo/VenmoClient.kt:153-157`

> "Vaulting will only occur if a client token with a customer ID is being used."
>
> `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/Venmo/src/main/java/com/braintreepayments/api/venmo/VenmoRequest.kt:15-21`

## Platform and Integration Model

The SDK supports Android API 23+, requires Java 11, and uses Kotlin 1.9.10. Merchants install only the Gradle modules needed for their checkout. A `BraintreeClient`, created from a tokenization key, client token, or token provider, retrieves merchant configuration and supports authorization for the payment-specific clients.

Payment clients create a payment-authorization request, a launcher presents any browser, wallet, or app-switch experience, and the client tokenizes the successful return into a Braintree payment-method nonce. Redirect-capable modules preserve a pending request and resolve the app-link or deep-link return before tokenization. The nonce is then sent to the merchant's Braintree server integration for processing.

## Modules and Payment Surfaces

The retained source includes:

- Card tokenization plus `CardFields`, a native complete-card form with number, expiration, CVV, validation, and XML support.
- PayPal checkout, PayPal vault, checkout-with-vault, Pay Later or Credit offers, app switch, recurring-billing metadata, and dedicated XML and Compose buttons.
- Venmo single-use and multi-use requests, Venmo app or mobile-browser launch, optional vaulting, address enrichment, and dedicated XML and Compose buttons.
- Google Pay readiness, request creation, wallet-sheet launch, and tokenization to a Braintree card or PayPal nonce.
- Local Payment and SEPA flows, including browser mandate handling where required.
- 3D Secure v2 lookup, challenge, tokenization, and liability-shift results.
- Data Collector device data, American Express rewards-balance lookup, PayPal Messaging, and beta Shopper Insights recommendations.

Module presence is SDK capability evidence. Runtime configuration such as `isPayPalEnabled`, `isVenmoEnabled`, and Google Pay readiness still gates presentation, and none of those checks alone proves that a merchant should be sold or activated for the method.

## PayPal Flows

PayPal is a Braintree payment module with separate request types for checkout and vaulting. `PayPalCheckoutRequest` supports one-time checkout and can set `shouldRequestBillingAgreement` for checkout-with-vault. Both checkout and vault requests can carry recurring-billing details and plan types. These fields describe a billing-agreement request surface; they are not a subscription scheduler or evidence that recurring billing is enabled for a merchant.

`enablePayPalAppSwitch` can request the PayPal app path when the installed app is resolvable. The launcher otherwise uses the browser flow. The SDK returns a Braintree PayPal account nonce rather than a direct PayPal Orders API approval result.

The internal PayPal funding-source enum covers PayPal, Pay Later, and Credit. Venmo is not a PayPal funding-source value in this SDK.

## Venmo Flow and Vault Boundary

Venmo is a dedicated Braintree module. `VenmoClient.createPaymentAuthRequest()` first checks `configuration.isVenmoEnabled`; it then creates a Venmo payment context for launch in the Venmo app or a mobile browser. App links are the preferred return mechanism, with a custom-scheme deep-link fallback.

`VenmoPaymentMethodUsage` distinguishes `SINGLE_USE` and `MULTI_USE`. Automatic vaulting requires all of the following in this retained implementation:

- `shouldVault` is true;
- a client token authorization is used, with the public request documentation specifying a customer ID; and
- payment-method usage is `MULTI_USE`.

Address collection is conditional on enriched customer data being enabled. A visible Venmo button, source module, or recommendation from Shopper Insights therefore must not be treated as proof of merchant or buyer eligibility.

This native Braintree Venmo path must not be conflated with `paypal/paypal-android@2.3.0`, whose retained standalone PayPal SDK source exposes no native Venmo integration.

## Cards, 3D Secure, and Risk

Card tokenization can use the public suspend API or the UIComponents card form. The 3D Secure module performs lookup and optional challenge work against a card nonce and returns liability-shift indicators; the merchant still decides whether to proceed when liability does not shift.

Data Collector uses PayPal's Magnes SDK and accepts user-location consent. Device data is a fraud-input artifact, not proof that a particular fraud product or merchant configuration is active.

## Shopper Insights and Presentation

Shopper Insights is a beta recommendation layer for PayPal and Venmo. Its newer flow creates or updates a customer session and requests payment recommendations. Recommendations can inform ordering or presentation, but they do not override Braintree configuration, merchant eligibility, or buyer eligibility.

The UIComponents module provides XML and Compose PayPal and Venmo buttons. In `5.30.0`, explicit button sizing and `match_parent` behavior are honored. Presentation support remains separate from payment-method activation and transaction processing.

## `5.30.0` Release Findings

The release exposes public Kotlin suspend functions across American Express, Card, Google Pay, Local Payment, PayPal, SEPA, Shopper Insights, 3D Secure, and Venmo. It also updates Android Gradle Plugin to 8.13.2 and compile/target SDK to API 37.

Visa Checkout is no longer supported and its module is removed. Visa-related configuration properties are deprecated for removal in the next major version. The release also corrects PayPal and Venmo button sizing behavior.

These are the exact `5.30.0` findings. Broader v5 architecture, request/launcher migration, and older removals such as PayPal Native Checkout, Samsung Pay, and the UnionPay module are historical context from the cumulative changelog and migration guides.

## Related

- [[changelog-github-braintree-android]] - package-qualified Android release ledger
- [[braintree-android-sdk]] - native Android SDK concept
- [[braintree]] - company and knowledge-status page
- [[paypal-android-sdk]] - independently versioned standalone PayPal Android SDK
- [[paypal-braintree-integration]] - Braintree PayPal processing boundary

## Raw Sources

- Snapshot manifest: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/manifest.json`
- Release manifest: `raw/github/braintree/braintree_android/releases/braintree-android/5.30.0/2026-08-01/manifest.json`
- Release notes: `raw/github/braintree/braintree_android/releases/braintree-android/5.30.0/2026-08-01/release-notes.md`
- README: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/README.md`
- Repository changelog: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/CHANGELOG.md`
- v5 migration guide: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/v5_MIGRATION_GUIDE.md`
- PayPal source: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/PayPal/`
- Venmo source: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/Venmo/`
- Card UI source: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/UIComponents/`
- 3D Secure source: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/ThreeDSecure/`
