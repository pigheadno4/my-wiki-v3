---
title: "Stripe: Accept a Payment with Sunbit"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-sunbit-accept-payment-2025.md"
tags: [stripe, bnpl, sunbit, buy-now-pay-later, consumer, us, checkout, payment-intents]
---

## Summary

Integration guide for Sunbit payments across Checkout, Checkout Sessions API, PaymentIntents API, and Direct API. USD only. `return_url` required. No manual capture (confirmed). $60-$20k enforced in Checkout Session.

## Key Details

**API enum**: `sunbit`. USD only. `return_url` required. **No manual capture**.

**Checkout constraints**: $60–$19,999.99 USD enforced in Session creation.

**Error codes**: `payment_intent_invalid_currency`, `payment_intent_authentication_failure`, `payment_intent_redirect_confirmation_without_return_url`.

## Raw Sources

- [[stripe-sunbit-accept-payment-2025]] — verbatim webpage content (1839 lines); fixed `_Prices_` (×2), `_sandbox_` (×2), `_PaymentIntent_` (×2), `_client secret_` (×4), `_webhook_` (×3); downloaded 1 CDN image to `raw/assets/`
