---
title: "Stripe: Apple Pay Merchant Tokens"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/apple-pay/merchant-tokens"
raw_files:
  - "stripe-apple-pay-merchant-tokens-2026-11-07.md"
  - "stripe-apple-pay-merchant-tokens-2025.md"
tags: [stripe, wallets, apple-pay, mpan, merchant-tokens, recurring, deferred, automatic-reload, express-checkout-element, sigma]
---

## Overview

The May 7 and November 7, 2026 [[stripe]] guide captures describe requesting Apple Pay merchant tokens (MPANs) for future merchant-initiated recurring, automatic-reload or deferred payments. A device token (DPAN) is bound to a device and might stop working after a device change or card removal; an MPAN is associated with the customer, underlying card and business. The November guide distinguishes this future MIT continuity concern from one-time customer-initiated transactions. See [[stripe-wallets]]. A request does not guarantee an MPAN for a particular payment.

## Request types and dated support

| Request object | Example use |
| --- | --- |
| `recurringPaymentRequest` | Subscriptions or recurring membership |
| `automaticReloadPaymentRequest` | Stored-balance reload when a threshold is reached |
| `deferredPaymentRequest` | Booking now, charge after a service, such as a hotel stay |

The **May 7 capture's** Apple Pay on the Web/iOS support table lists recurring and automatic-reload requests at iOS **>16.0**, and deferred requests at iOS **>16.4** (plus Xcode 14.3). The November guide does not repeat the version table. These dated support labels do not establish current platform coverage. The May guide also describes mobile Payment Element availability and recommends moving recurring Payment Request Button integrations to Express Checkout Element; omission in November does not establish deprecation.

The May recurring Express Checkout example includes `billingAgreement` and `managementURL`; the November sample retains `managementURL` but omits `billingAgreement`. This sample difference does not establish that `billingAgreement` is required, optional or unsupported in the current Stripe.js API. The May guide says almost all request types can supply `managementURL` to route customers to payment-method management. See the dated raw examples for use-case parameters.

## Integration path and returned credential

For **Elements with the Payment Intents API**, the November guide instructs passing the use-case-specific `applePay` object to Express Checkout Element or web Payment Element and supplying relevant parameters. **Stripe Checkout** and **Elements with the Checkout Sessions API** automatically request merchant tokens when needed, so this guide does not require that manual `applePay` configuration for those paths. The May capture also names mobile Payment Element as a surface; the November guide presents only web Element examples.

After a configured Apple Pay checkout, Stripe requests a merchant token. **If both Apple Pay and the card issuer support merchant tokens**, Apple Pay returns an MPAN; otherwise it returns a DPAN. Stripe stores the returned Apple Pay credential with the resulting `PaymentMethod`. The guide directs integrators to save and reuse that `PaymentMethod` in their standard off-session payment flow, without extra MPAN-specific integration steps after the request configuration. This documented path does not prove a particular off-session charge succeeds.

## Merchant token lifecycle

The November guide adds a `payment_method.automatically_updated` webhook for updates to the underlying card of an **MPAN**. Inspect `data.object.card.exp_month`, `exp_year` and `last4`, and update locally cached values. The guide limits merchant-token notifications to Apple Pay `CardMetadata` properties; it does not promise broader card metadata or that every underlying change arrives in a notification.

## Monitoring and detail locators

For Sigma users, both captures show `charges.card_token_type` distinguishing `mpan` from `dpan`, and an MPAN authorization-rate query filtering `c.card_token_type = 'mpan'`. The query is an example, not an observed rate or a guarantee of MPAN issuance.

- MPAN versus DPAN, MIT use cases and one-time CIT distinction: November raw introduction; compare May raw introduction and "Merchant token types".
- Dated Apple Pay on the Web/iOS version table, mobile Payment Element and Payment Request Button guidance: May raw, "Merchant token types" and "Add Apple Pay merchant tokens".
- Payment Intents Elements configuration and automatic Checkout/Checkout Sessions path: November raw, "Configure your integration to request Apple Pay merchant tokens".
- Use-case object examples and changed `billingAgreement` sample: both raws, recurring/automatic-reload/deferred sections.
- MPAN/DPAN response, PaymentMethod association and off-session reuse: November raw, paragraphs after web Payment Element examples.
- Update webhook and card fields: November raw, "Merchant token lifecycle management".
- Sigma query and field: both raws, "Merchant token auth rate monitoring".

## Related

- [[stripe]] — provider context
- [[stripe-wallets]] — Apple Pay wallet concept and reciprocal source route
- [[source-stripe-apple-pay-recurring]] — separate recurring Apple Pay flow

## Raw Sources

- [[raw/stripe-apple-pay-merchant-tokens-2026-11-07|Stripe merchant-token guide, fetched 2026-11-07]]
- [[raw/stripe-apple-pay-merchant-tokens-2025|Stripe merchant-token guide, fetched 2026-05-07]]
