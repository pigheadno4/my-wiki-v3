---
title: "Stripe: Accept a MB WAY Payment"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-mb-way-accept-payment-2025.md"
tags: [stripe, wallets, mb-way, portugal, eur, checkout, elements, direct-api, beta, phone-number, test-numbers]
---

## Summary

Integration guide for MB WAY via Checkout, Elements (beta), and Direct API. Elements requires beta flag. Direct API uses `stripe.confirmMbWayPayment()` with phone number required. 5 specific test phone numbers documented.

## Key Details

**Three integration paths**: Checkout, Elements (PaymentIntents), Direct API.

**Checkout**: `payment_method_types: ['mb_way']`, EUR only. No subscription/setup mode.

**Elements beta**: requires `Stripe(key, { betas: 'mb_way_pm_beta_1' })` — MB WAY in beta for Elements path.

**Direct API**: `stripe.confirmMbWayPayment(clientSecret, { payment_method: { billing_details: { phone } } })`. Phone number required. Stripe.js polls automatically; `handleActions: false` to disable.

**Test phone numbers**:

| Number | Behavior |
| --- | --- |
| `+351911111112` | Succeeds after ~30 seconds |
| `+351911111113` | `payment_method_not_available` |
| `+351911111114` | `payment_method_provider_decline` |
| `+351911111115` | `payment_intent_payment_attempt_expired` |
| `+351911111116` | `payment_method_customer_decline` |
| Any other | Succeeds immediately |

## Raw Sources

- [[stripe-mb-way-accept-payment-2025]] — verbatim webpage content (732 lines); fixed `*sandbox*` ×1, `*Prices*` ×1, `*client secret*` ×2, `*webhook*` ×2
