---
title: "Stripe Docs — Standalone 3DS"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/3d-secure/standalone-3d-secure"
raw_files:
  - "stripe-payments-3d-secure-standalone-3d-secure-2026-11-07.md"
  - "stripe-standalone-3ds-2025.md"
tags: [stripe, 3d-secure, standalone-3ds, interchange-plus, authentication, cryptogram, psp, connect]
---

## Summary

Stripe's standalone 3DS API runs EMV 3D Secure authentication separately from payment authorization. A merchant can authenticate through Stripe and then submit the authentication output in a separate authorization request through Stripe's result-import route or another payment service provider. Authentication success and a cryptogram alone do not prove payment authorization, capture, settlement, issuer approval, or liability shift.

## Features in the 2026-11-07 Capture

- **Request control:** request frictionless, challenge, or data-share-only flows, or supply a 3DS reason such as liability shift, processing cost, or regulatory compliance for Stripe's flow selection. These are documented request modes, not a guarantee that every issuer or transaction takes a requested path.
- **Issuer output:** the authentication result, Electronic Commerce Indicator (ECI), Directory Server (DS) Transaction ID, and cryptogram are available for authorization logic and performance analysis.
- **Complex scenarios:** parameters address recurring payments, installments, and card-on-file setups. 3DS Requestor Initiated (3RI) authentication can reference a previous authentication to obtain a new cryptogram for a later authorization when the cardholder is absent, such as travel booking or split shipments.
- **Non-payment use:** authentication for account verification, card enrollment, or identity confirmation without an associated payment amount.
- **Connect:** a platform can run standalone 3DS on behalf of connected accounts.

## Authentication Sequence and Payment Boundary

The 2026-11-07 guide describes creating a 3DS Authentication object with amount, currency, card details, and device browser information; optionally collecting device fingerprint data through an iframe or Stripe.js if the issuer supports it; submitting through the network Directory Server and issuer Access Control Server; presenting an issuer challenge if required, with a completion webhook; and retrieving the outcome. On authentication success, the returned cryptogram, ECI, and DS Transaction ID are available. A separate payment authorization request can then carry the cryptogram, either through Stripe's 3DS result-import path or another PSP. The older 2026-05-08 capture also distinguishes authentication output from later payment authorization. Neither capture documents an executed authorization or payment outcome for any transaction.

## Networks, Geography, and Protocol

The 2026-11-07 page lists Visa, Mastercard, American Express, Discover, and Cartes Bancaires. It describes availability in countries where Stripe supports card payments except Malaysia and Thailand, and Stripe protocol support through version 2.3.1. This geographic statement and protocol ceiling do not establish a particular account's entitlement, network/issuer path, transaction eligibility, or support for every mode on every protocol version.

## Pricing Qualification

The 2026-05-08 capture said standalone 3DS was available to businesses on Interchange Plus pricing. It did **not** state that Interchange Plus was the exclusive tier. The 2026-11-07 capture omits pricing eligibility altogether. Current pricing-tier and account-specific eligibility cannot be resolved from these two captures; the omission is not evidence that the earlier condition was removed.

## Related Pages

- [[stripe-3d-secure]] — 3D Secure concept, including a distinct result-import topic
- [[stripe]] — Stripe company page
- [Import 3D Secure results with Stripe](https://docs.stripe.com/payments/payment-intents/three-d-secure-import) — linked authorization path; its separate availability rules were not assessed in this update

## Raw Sources

- [[raw/stripe-payments-3d-secure-standalone-3d-secure-2026-11-07|2026-11-07 standalone 3DS guide]] — feature modes, workflow, output, networks, geography, and protocol version
- [[raw/stripe-standalone-3ds-2025|2026-05-08 standalone 3DS overview]] — dated Interchange Plus availability and authentication/authorization distinction
