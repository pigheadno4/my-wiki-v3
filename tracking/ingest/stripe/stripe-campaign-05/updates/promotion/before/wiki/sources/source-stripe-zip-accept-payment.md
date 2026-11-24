---
title: "Stripe: Accept a Zip Payment"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-zip-accept-payment-2025.md"
tags: [stripe, bnpl, zip, buy-now-pay-later, consumer, australia, us, checkout, payment-intents]
---

## Summary

Integration guide for Zip payments via Checkout (recommended) and legacy Direct API. `return_url` required. No manual capture. Direct API uses deprecated `stripe.confirmZipPayment()` method.

## Key Details

**API enum**: `zip`. AUD or USD only. `return_url` required. **No manual capture**.

**Two integration paths**:
- **Checkout** (recommended): standard Checkout Session with `payment_method_types: ['zip']`
- **Direct API** (legacy/deprecated): `stripe.confirmZipPayment()` — Stripe may end support

**`stripe.confirmZipPayment()`**: Zip-specific Direct API method; accepts `billing_details` and `return_url`.

## Raw Sources

- [[stripe-zip-accept-payment-2025]] — verbatim webpage content (385 lines); fixed `_Prices_`, `_Legacy_`, `_client secret_`, `_PaymentMethod_`, `_webhook_` → `*italic*`
