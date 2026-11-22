---
title: "Stripe Docs — Link in the Payment Request Button"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/link/payment-request-button-link"
raw_files:
  - "stripe-payments-link-payment-request-button-link-2026-11-07.md"
  - "stripe-payment-request-button-link-2025.md"
tags: [stripe, link, payment-request-button, deprecated, connect]
---

## Summary

The November 7, 2026 guide marks the Web Elements Payment Request Button deprecated and unsupported in Stripe.js Endive or later. It continues to work in earlier Stripe.js versions for as long as those versions are supported. Stripe recommends migrating to Express Checkout Element, or using another preferred Link integration such as Contact Details Element or Payment Element.

## Version and migration

- **May 8, 2026.** Stripe already advised against using the Payment Request Button in Web Elements and named Link Authentication Element, Express Checkout Element and Payment Element.
- **Endive.** The September 30, 2026 changelog says `elements.create('paymentRequestButton')` throws starting with Endive and React integrations rendering `PaymentRequestButtonElement` are affected. It names versions through Dahlia as retaining the Element. The November Link guide qualifies this by continued earlier-version support. This cutoff applies to the Web Elements runtime. See [[stripe-express-checkout-element]] for the separate package declarations and React wrapper changes.
- **Preferred routes.** The November migration capture indexes Checkout Sessions and Payment Intents variants. The full April 21, 2026 Payment Intents migration requires integrations using the Charges API with tokens to migrate to Payment Intents first. See [[source-stripe-express-checkout-element-migration]]. The separate November Contact Details guide calls it the former Link Authentication Element and documents a distinct email-collection and Link authentication flow ahead of Payment Element.

## Existing integrations on supported pre-Endive Stripe.js

- **Customer and authentication flow.** A customer new to the merchant can already have saved Link payment details. Returning Link customers click the Link button and enter an SMS or email code. Link then loads their saved payment details for one-click checkout. If they authenticated at this merchant or another Link-enabled business in the previous 90 days, they can skip reauthentication. A customer new to Link is prompted to save their information when clicking Link. Authentication, credential loading and the one-click option do not establish a successful charge.
- **Features and settings.** The guides describe compatibility with existing card features such as subscriptions, no additional Link fees, and on/off control through payment method settings. These details apply to this legacy client Element.
- **Connect.** Link is automatically available to connected accounts accessing the supported Payment Request Button through a Connect platform integration. The platform manages Link for payments it processes. For payments processed independently, the connected account manages Link through payment method settings in its own Dashboard. The captures specify no Connect charge type.

## CDN Assets

- `raw/assets/stripe-link-payment-request-button.png` — Payment Request Button with Link (145 KB)

## Related Pages

- [[stripe-link]] — Link integration concept
- [[source-stripe-express-checkout-link]] — Link in Express Checkout Element
- [[source-stripe-payment-element-link]] — Link in Payment Element
- [[raw/stripe-payments-link-contact-details-element-2026-11-07|November Contact Details Element guide]] — email collection and Link authentication
- [[raw/stripe-changelog-endive-2026-09-30-deprecate-payment-request-button-2026-11-07|September 30 Endive changelog captured 2026-11-07]] — Web Elements runtime cutoff
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payments-link-payment-request-button-link-2026-11-07|Link in the Payment Request Button, captured 2026-11-07]] — full captured page (36 lines)
- [[raw/stripe-payment-request-button-link-2025|Link in the Payment Request Button, captured 2026-05-08]] — verbatim webpage content (31 lines)
