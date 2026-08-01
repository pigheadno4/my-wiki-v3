---
title: "Braintree iOS SDK"
type: concept
category: technology
tags: [braintree, ios, mobile, swift, paypal, venmo, apple-pay, cards, 3d-secure]
---

## Braintree iOS SDK

Braintree iOS is a modular native SDK for accepting cards and alternative payment methods in iOS applications. Payment-specific clients use a Braintree client token or tokenization key, perform any required native, browser, or app-switch flow, and return a Braintree payment-method nonce for merchant-server processing.

## Current Baseline

The first retained baseline is `braintree-ios@7.9.0` at exact SHA `4e987ca19f03b65a0d303b4c3ec95e0c723be971`. It requires iOS 16+, Xcode 16.2+, and Swift 5.10+.

The package exposes separate modules for Core, Card, Apple Pay, PayPal, Venmo, Local Payment, SEPA Direct Debit, 3D Secure, Data Collector, Shopper Insights, American Express, PayPal Messaging, and UIComponents. Source availability does not establish merchant configuration, buyer eligibility, or regional availability.

## Authorization and Nonce Boundary

Feature clients initialize directly from a client token or tokenization key. Successful card, wallet, and alternative-payment flows return typed subclasses of `BTPaymentMethodNonce`; the merchant sends the nonce to a Braintree server integration to create the transaction.

Some capabilities require stronger authorization context. For example, 3D Secure lookup requires a client token, and client-side Venmo vaulting requires a client token generated with a customer ID.

## PayPal and Venmo

PayPal and Venmo are independent Braintree modules, not funding-source variants of one native client:

- PayPal supports checkout, vault, checkout-with-vault billing agreement consent, recurring-billing metadata, Pay Later or Credit offers, and an optional PayPal app-switch path. The v7 app-switch API is beta and its source comments limit it to production.
- Venmo uses a merchant HTTPS universal link, opens the Venmo app when installed, and otherwise falls back to the buyer's default browser. Requests distinguish `.singleUse` from `.multiUse`.
- Client-side Venmo vaulting requires `paymentMethodUsage: .multiUse`, `vault: true`, and a customer-scoped client token. A multi-use nonce may instead be vaulted by the merchant server; a single-use request cannot be vaulted.

The removed PayPal Native Checkout module is not the replacement path. The v7 migration guide directs merchants to Braintree's PayPal web flow.

## Apple Pay and Recurring Boundary

`BTApplePayClient` checks merchant and device support, creates a partially configured `PKPaymentRequest`, and tokenizes an authorized `PKPayment` into a Braintree Apple Pay nonce. The merchant still supplies summary items and presents the Apple Pay sheet.

The demo attaches a `PKRecurringPaymentRequest`, but the retained SDK source does not implement a subscription scheduler or a complete merchant-initiated stored-token lifecycle. Treat the recurring sheet as buyer-facing Apple Pay request metadata, not proof that subsequent charges are configured.

## Cards, 3D Secure, and UI

Card tokenization selects GraphQL when the remote Braintree configuration enables it and otherwise uses the REST card endpoint. UIComponents supplies a SwiftUI `CardFields` form with validation and merchant-controlled submission, plus branded PayPal and Venmo buttons that invoke the corresponding tokenize flows.

The 3D Secure module performs a v2 lookup and optional Cardinal challenge around a card nonce. It requires the merchant configuration JWT and a request delegate; 3D Secure v1 is explicitly unsupported.

## Version Boundary

The v7 migration moves request properties into initializers, changes feature clients to direct authorization initializers, renames Local Payment and 3D Secure start methods, requires universal-link handling for Venmo, and removes PayPal Native Checkout. Exact release `7.9.0` only aligns the BraintreeUIComponents minimum deployment target with iOS 16; broader v7 behavior comes from the cumulative exact-SHA baseline.

## Related

- [[source-github-braintree-ios]] - cumulative exact-SHA implementation evidence
- [[changelog-github-braintree-ios]] - package-qualified release ledger
- [[braintree-android-sdk]] - independently versioned native Android SDK
- [[braintree-web-sdk]] - independently versioned browser SDK
- [[paypal-braintree-integration]] - Braintree PayPal processing boundary
- [[recurring-payments]] - consent, storage, and later-charge requirements
- [[braintree]] - company page
