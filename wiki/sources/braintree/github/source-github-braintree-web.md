---
title: "GitHub: braintree/braintree-web"
type: source
date_ingested: 2026-07-28
original_format: github-repo
raw_files:
  - "github/braintree/braintree-web/snapshots/2026-07-27-bae582d/manifest.json"
tags: [braintree, javascript-sdk, checkout, hosted-fields, venmo, paypal, 3d-secure, github-repository]
---

## Overview

`braintree/braintree-web` contains Braintree's modular browser SDK. The first retained baseline is package-qualified release `braintree-web@3.143.0` at exact SHA `bae582d791026c143abb91c3bdcada92b8c060f6`.

Repository: <https://github.com/braintree/braintree-web>

## Evidence Boundary

- The snapshot proves implementation present in `braintree-web@3.143.0`, released on 2026-06-11. It does not replace current product documentation or prove merchant, buyer, country, or payment-method eligibility.
- The package exposes SDK components, not Braintree Web Drop-in. Drop-in is a separately versioned repository.
- The 27 retained stories show intended integration scenarios. Tests, fixtures, and mocks are excluded, so test-only behavior is outside this capsule.
- PayPal Checkout v6 and Fastlane delegate runtime behavior to PayPal SDKs. This source covers the Braintree adapters and nonce boundary, not the complete delegated runtimes.
- Legacy modules retained in source, including Masterpass and Visa Checkout, are implementation history rather than evidence that merchants should start new integrations with them.

## Grounding Excerpts

> "A suite of tools for integrating Braintree in the browser."
>
> `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/README.md:3`

> "For a ready-made payment UI, see Braintree Web Drop-in."
>
> `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/README.md:7`

> "Instances of this class can load the PayPal SDK, create payment sessions, and tokenize payments."
>
> `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/src/paypal-checkout-v6/paypal-checkout-v6.js:31`

> "single_use - intended as a one time transaction"
>
> `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/src/venmo/index.js:50-52`

> "Update Fastlane SDK loader package from `@paypal/accelerated-checkout-loader` to `@paypal/fastlane-sdk-loader`"
>
> `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/CHANGELOG.md:5-7`

## Package and Client Architecture

The top-level package exports 23 components. Each component can be consumed from the aggregate `braintree-web` package or as an individual browser/CommonJS/AMD module. Most creation methods accept either an existing `Client` or authorization from which the SDK creates a deferred client, and asynchronous methods support promises when no callback is supplied.

The client parses a tokenization key or client token, retrieves gateway configuration, and provides REST and GraphQL request paths. Browser metadata and SDK version are attached to requests. The merchant server remains responsible for generating client tokens when required and for consuming browser-generated payment-method nonces.

## Hosted Fields and Cards

Hosted Fields injects Braintree-hosted frames into merchant-selected containers for card number, CVV, expiration, postal code, and cardholder name. The merchant controls supported styling and listens for focus, emptiness, validity, card-type, submit-request, and BIN events without hosting sensitive field inputs directly.

`tokenize()` validates field state, sends the card data through the client, and returns a payment-method nonce and card details. A CVV-only path can tokenize against an existing authorization fingerprint. The README distinguishes this iframe model from direct card submission through the lower-level client API, which changes PCI scope.

The broader card surface includes American Express rewards-balance verification and UnionPay capability, enrollment, and tokenization flows. Vault Manager can delete a vaulted payment method, but this client operation does not describe the server-side vault lifecycle.

## 3D Secure

The 3D Secure component verifies a card nonce and BIN with transaction amount and optional account, exemption, challenge, customer, billing, shipping, device, and custom-field data. A merchant can inspect lookup data before calling `next()` to continue a challenge, initialize a challenge from a server-side lookup response, or prepare browser data for a server lookup.

The result includes a new nonce plus `liabilityShifted` and `liabilityShiftPossible`; source examples explicitly leave acceptance decisions to the merchant when liability does not shift. The retained implementation supports 3DS2 framework and modal/iframe orchestration and includes historical 3DS1 compatibility notes.

## PayPal Checkout v6

`paypalCheckoutV6` coordinates Braintree with PayPal Web SDK v6. It can:

- load and initialize the PayPal SDK;
- discover eligible PayPal, Pay Later, and Credit methods;
- create one-time, Pay Later, checkout-with-vault, and billing-agreement sessions;
- create PayPal Messages;
- start, focus, and close vault-initiated checkout for repeat purchases; and
- convert approval identifiers or billing tokens into Braintree payment-method nonces.

Session options cover amount, currency, intent, shipping callbacks, contact preferences, address overrides, commit behavior, and billing-agreement plan metadata where applicable. Eligibility and method presence in code do not establish account enablement.

## Venmo

The standalone Venmo component tokenizes through mobile app switch and optional fallback experiences. Browser support is configuration-sensitive: merchants can restrict new tabs and webviews, allow non-default browsers, choose iOS redirect/manual-return handling, and control cancellation when the buyer returns early.

Desktop support can render a QR flow, while optional desktop or mobile web login provides a non-app path. `paymentMethodUsage` declares `single_use` or `multi_use`; the latter is intended for a nonce that will be vaulted and reused through Braintree. Merchant eligibility, supported environments, and server processing still require product guidance beyond this source snapshot.

## Other Payment and Decision Surfaces

- Apple Pay and Google Pay adapters build wallet configuration and parse wallet responses into Braintree nonces.
- Local Payment starts popup, redirect, app-switch, and selected QR flows for configured local methods; retained code includes Swish, crypto, BLIK, MB WAY, Bancomat Pay, and pay-upon-invoice branches.
- US bank account and Instant Verification cover bank login/verification and ACH mandate details; SEPA creates mandate and nonce data.
- Data Collector combines enabled fraud-device signals into device data for server transactions.
- Payment Ready creates or updates a customer session from hashed identifiers and device/app signals, then requests payment recommendations.
- Preferred Payment Methods supplies browser/device preference signals; it is not payment-method eligibility.

## Fastlane Dependency

The Braintree Fastlane component loads and initializes the external Fastlane SDK with Braintree configuration and optional device data. At `3.143.0`, the package depends on `@paypal/fastlane-sdk-loader@1.2.1`.

The exact release replaces the previous loader package name but does not establish a Fastlane product-behavior change. Questions about identity, profile, checkout UI, or delegated payment behavior must also consult current Fastlane documentation or an independently retained runtime source.

## `3.143.0` Release Findings

The release updates `credit-card-type` to `10.2.0` and replaces `@paypal/accelerated-checkout-loader` with `@paypal/fastlane-sdk-loader`. No migration action or direct payment-flow change is documented in the release notes.

All broader findings above are the cumulative baseline present at the exact release SHA, not changes introduced by `3.143.0`.

## Related

- [[changelog-github-braintree-web]] — package-qualified release ledger
- [[braintree]] — company and knowledge-status page
- [[braintree-web-sdk]] — product concept and integration boundaries
- [[paypal-braintree-integration]] — PayPal v6/Braintree nonce flow
- [[paypal-fastlane]] — delegated Fastlane product concept

## Raw Sources

- Snapshot manifest: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/manifest.json`
- Release manifest: `raw/github/braintree/braintree-web/releases/braintree-web/3.143.0/2026-07-27/manifest.json`
- Release notes: `raw/github/braintree/braintree-web/releases/braintree-web/3.143.0/2026-07-27/release-notes.md`
- Package manifest: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/package.json`
- Component registry: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/components.json`
- Hosted Fields: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/src/hosted-fields/`
- 3D Secure: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/src/three-d-secure/`
- PayPal Checkout v6: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/src/paypal-checkout-v6/`
- Venmo: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/src/venmo/`
