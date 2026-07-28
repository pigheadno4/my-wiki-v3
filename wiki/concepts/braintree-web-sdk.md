---
title: "Braintree Web SDK"
type: concept
category: technology
tags: [braintree, javascript-sdk, checkout, hosted-fields, wallets, venmo, 3d-secure]
---

## Braintree Web SDK

Braintree Web is a modular browser SDK. A merchant creates a Braintree client from a tokenization key or client token, adds only the payment components needed by the checkout, receives a payment-method nonce from the browser flow, and sends that nonce to a Braintree server integration for transaction processing.

## Integration Model

The `braintree-web` package exposes separate components rather than a ready-made checkout UI. Hosted Fields provides merchant-styled card fields backed by Braintree-hosted iframes; Braintree Web Drop-in is a separate repository and product.

At `braintree-web@3.143.0`, the package exports 23 components covering:

- cards through Hosted Fields, 3D Secure, UnionPay, and American Express verification;
- PayPal Checkout, PayPal Checkout v6, Venmo, Fastlane, Apple Pay, and Google Pay;
- local payments, SEPA, US bank account verification, and Payment Request;
- data collection, vaulted-method management, preferred-method signals, and Payment Ready recommendations.

Component presence proves an SDK integration surface at this exact version. It does not prove merchant enablement, buyer eligibility, regional availability, or that a legacy component remains recommended.

## Card and Authentication Boundary

Hosted Fields keeps sensitive card inputs inside injected Braintree frames while exposing styling, validation-state events, card-type changes, BIN availability, and tokenization to the merchant page. Direct card submission through the lower-level client API is a different PCI scope.

The 3D Secure component verifies a card nonce and BIN, can collect device data, supports lookup inspection before challenge continuation, and returns liability-shift indicators. The merchant still decides whether a result without liability shift is acceptable.

## Wallet and PayPal Boundary

Wallet modules adapt external wallet SDKs or browser APIs into Braintree payment-method nonces. In particular:

- PayPal Checkout v6 loads PayPal Web SDK v6, creates one-time, Pay Later, checkout-with-vault, and billing-agreement sessions, checks eligible methods, and tokenizes approval data.
- Venmo supports mobile app switch plus optional desktop QR or desktop web-login paths. `paymentMethodUsage` distinguishes `single_use` from `multi_use`.
- Fastlane is a Braintree loader and initialization bridge; the delegated PayPal Fastlane runtime remains a separate evidence boundary.

These are Braintree processing paths. They must not be described as direct PayPal Orders API integrations.

## Versioned Evidence

The first retained baseline is `braintree-web@3.143.0` at SHA `bae582d791026c143abb91c3bdcada92b8c060f6`. The exact patch changes dependencies: `credit-card-type` moves to `10.2.0`, and the Fastlane loader package changes to `@paypal/fastlane-sdk-loader`. Broader behavior on the cumulative source page describes implementation present at that SHA, not changes introduced by this patch.

## Related

- [[source-github-braintree-web]] — cumulative exact-SHA implementation evidence
- [[changelog-github-braintree-web]] — package-qualified release ledger
- [[paypal-braintree-integration]] — PayPal v6 and Braintree nonce-processing boundary
- [[paypal-fastlane]] — delegated Fastlane product concept
