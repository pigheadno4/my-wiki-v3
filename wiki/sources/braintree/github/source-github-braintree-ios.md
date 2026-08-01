---
title: "GitHub: braintree/braintree_ios"
type: source
date_ingested: 2026-08-01
original_format: github-repo
raw_files:
  - "github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/manifest.json"
tags: [braintree, ios, mobile-sdk, swift, paypal, venmo, apple-pay, github-repository]
---

## Overview

`braintree-ios@7.9.0` is the first retained exact-SHA baseline for Braintree's modular native iOS SDK. It accepts client authorization, runs payment-method-specific native or redirect flows, and returns Braintree payment-method nonces for merchant-server processing.

## Baseline and Package Structure

The retained release resolves to SHA `4e987ca19f03b65a0d303b4c3ec95e0c723be971` and requires iOS 16+, Xcode 16.2+, and Swift 5.10+. Swift Package Manager exposes separate American Express, Apple Pay, Card, Core, Data Collector, Local Payment, PayPal, PayPal Messaging, SEPA Direct Debit, Shopper Insights, 3D Secure, Venmo, and UIComponents products.

Swift Package Manager is the recommended integration path. CocoaPods remains represented but the README says support will be removed in late 2026; Carthage is supported without a long-term guarantee. These repository statements should be rechecked before time-sensitive migration guidance.

## Authorization, Configuration, and Server Handoff

Feature clients initialize with a Braintree client token or tokenization key and load merchant configuration before capability-sensitive operations. Successful flows return typed subclasses of `BTPaymentMethodNonce`. The demo sends the nonce to a merchant endpoint that creates the transaction, demonstrating that the mobile SDK is the client/tokenization layer rather than the transaction-processing server.

Authorization is not interchangeable for every feature. The retained 3D Secure implementation requires a client token for lookup. Client-side Venmo vaulting requires a client token generated with a customer ID, while ordinary tokenization surfaces can accept either authorization type.

## PayPal Checkout, Vault, and App Switch

`BTPayPalClient` supports separate Checkout and Vault request types:

- Checkout accepts amount, authorize/sale/order intent, Pay Later or Credit offers, shipping and contact controls, line items, optional billing-agreement consent, and recurring-billing metadata.
- Vault creates billing-agreement consent without a checkout amount and can also carry recurring-plan metadata.
- Both flows return a `BTPayPalAccountNonce` for Braintree server processing.

The optional PayPal app-switch path uses a merchant universal link and optional registered fallback URL scheme. Source comments mark the app-switch initializer beta and production-only. Braintree iOS v7 removes the former PayPal Native Checkout module and directs merchants to the PayPal web flow; it is not evidence for standalone `paypal/paypal-ios` behavior.

Recurring metadata and billing-agreement consent do not schedule or execute later charges. The merchant's Braintree server integration remains responsible for storing the resulting payment method and performing future transactions.

## Native Venmo Flow and Vaulting

Venmo is a dedicated Braintree module. `BTVenmoClient` requires a valid HTTPS universal link dedicated to Braintree app-switch returns. The v7 flow opens the Venmo app when installed and otherwise falls back to the buyer's default browser.

`BTVenmoRequest` distinguishes `.singleUse` from `.multiUse`. A single-use request cannot be vaulted. Automatic client-side vaulting requires `.multiUse`, `vault: true`, and a customer-scoped client token; when `vault` is false, a multi-use nonce can still be vaulted by the merchant server.

The request can carry a Venmo profile, risk correlation ID, billing or shipping address collection, final-amount status, amount breakdown, and up to 249 line items. Availability still depends on Braintree configuration and buyer eligibility. A rendered Venmo button or retained module does not prove that a merchant can present or process Venmo.

## Apple Pay Boundary

`BTApplePayClient` checks merchant/device support, creates a `PKPaymentRequest` populated with Braintree configuration, and tokenizes an authorized `PKPayment` through `v1/payment_methods/apple_payment_tokens`. The merchant supplies payment summary items and presents the Apple Pay sheet.

The demo attaches a `PKRecurringPaymentRequest`, but the retained SDK implementation only establishes Apple Pay request creation and nonce tokenization. It does not establish a subscription engine or the complete stored-token and merchant-initiated-charge lifecycle.

## Cards, 3D Secure, and Risk

Card tokenization uses GraphQL when remote configuration advertises `tokenize_credit_cards`; otherwise it uses the REST card endpoint. The card model supports billing data and optional authentication insight, while the returned card nonce includes card details and 3D Secure information.

The 3D Secure module performs a version 2 lookup and optional Cardinal challenge around a card nonce. It requires a configuration JWT, non-empty amount, and request delegate; 3D Secure v1 is explicitly unsupported. Client-side liability indicators are flow inputs and do not replace server-side transaction controls.

Data Collector uses the retained PPRiskMagnes binary dependency and returns device data for fraud tooling. Device-data collection is evidence of a risk input, not proof that a particular fraud product or rule set is active.

## Additional Payment and Presentation Modules

- Local Payment uses a web-authentication-session return flow and tokenizes the approved local-payment account.
- SEPA Direct Debit creates mandate and debit-account artifacts and returns a SEPA nonce.
- American Express looks up rewards balance from an already tokenized Amex card nonce.
- Shopper Insights has beta customer-session and recommendation APIs for PayPal and Venmo presentation. Recommendations inform ordering; they do not override merchant configuration or buyer eligibility.
- PayPal Messaging is a beta Pay Later messaging surface, not a payment session.
- UIComponents provides SwiftUI PayPal and Venmo buttons plus a card form with validation, card-brand detection, focus management, and merchant-controlled submission.

## v7 Migration and Exact `7.9.0` Change

The v7 migration moves request properties to initializers, changes feature clients to accept authorization directly, renames the Local Payment and 3D Secure start methods, makes Venmo universal-link handling mandatory, updates the PayPal app query scheme to `paypal`, and removes PayPal Native Checkout.

Exact release `7.9.0` only fixes the BraintreeUIComponents minimum deployment target to iOS 16 so it matches the other modules. Other v7 behavior is cumulative baseline knowledge from the exact-SHA snapshot, not a claim that every behavior was introduced in `7.9.0`.

## Evidence Boundaries

This capsule excludes tests, fixtures, CI, tooling, generated documentation, and binary framework internals. CardinalMobile, PPRiskMagnes, and PayPalMessages behavior beyond their declared versions is delegated evidence. No earlier exact-SHA Braintree iOS snapshot exists in the wiki, so historical changelog entries provide migration context but not retained version-to-version proof.

## Related

- [[changelog-github-braintree-ios]] - package-qualified iOS release ledger
- [[braintree-ios-sdk]] - native iOS SDK concept
- [[paypal-braintree-integration]] - Braintree PayPal boundary
- [[recurring-payments]] - later-charge requirements and evidence boundary
- [[braintree]] - company and knowledge-status page

## Raw Sources

- Snapshot manifest: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/manifest.json`
- Release manifest: `raw/github/braintree/braintree_ios/releases/braintree-ios/7.9.0/2026-08-01/manifest.json`
- Release notes: `raw/github/braintree/braintree_ios/releases/braintree-ios/7.9.0/2026-08-01/release-notes.md`
- README: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/README.md`
- Repository changelog: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/CHANGELOG.md`
- v7 migration guide: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/V7_MIGRATION.md`
- Package manifest: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/Package.swift`
- PayPal source: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/Sources/BraintreePayPal/`
- Venmo source: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/Sources/BraintreeVenmo/`
- Apple Pay source: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/Sources/BraintreeApplePay/`
- 3D Secure source: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/Sources/BraintreeThreeDSecure/`
- UIComponents source: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/Sources/BraintreeUIComponents/`
