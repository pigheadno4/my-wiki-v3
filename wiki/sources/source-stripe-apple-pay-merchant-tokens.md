---
title: "Stripe: Apple Pay Merchant Tokens"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-apple-pay-merchant-tokens-2025.md"
tags: [stripe, wallets, apple-pay, mpan, merchant-tokens, recurring, deferred, automatic-reload, express-checkout-element, sigma]
---

## Summary

Technical guide for Apple Pay merchant tokens (MPANs). Three request types: recurring, automatic reload, deferred. Configure via `applePay` object in Express Checkout Element or Payment Element. Checkout handles automatically. Sigma `card_token_type` field for auth rate monitoring.

## Key Details

**Three MPAN request types** (all iOS 16+, Apple Pay on Web):

| Type | Use case | Key params |
| --- | --- | --- |
| `recurringPaymentRequest` | Subscriptions | `regularBilling`: start/end date, interval unit/count |
| `automaticReloadPaymentRequest` | Store card top-ups, prepaid | `automaticReloadBilling`: amount, threshold |
| `deferredPaymentRequest` | Hotel reservations, bookings | `deferredBilling.deferredPaymentDate`, `freeCancellationDate`, `billingAgreement`; iOS 16.4+ required |

**Fallback**: if issuer doesn't support MPAN → falls back to DPAN automatically.

**Integration**: pass `applePay: { recurringPaymentRequest | automaticReloadPaymentRequest | deferredPaymentRequest }` to Express Checkout Element or Payment Element. Checkout handles automatically.

**Payment Request Button**: recommend migrating to Express Checkout Element for better MPAN support.

**Sigma monitoring**: `charges` table has `card_token_type` enum (`mpan` or `dpan`). Filter `c.card_token_type = 'mpan'` to calculate MPAN auth rate.

## Raw Sources

- [[stripe-apple-pay-merchant-tokens-2025]] — verbatim webpage content (191 lines); no italic fixes needed
