---
title: "Stripe: Accept a Payment with SeQura"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-sequra-accept-payment-2025.md"
tags: [stripe, bnpl, sequra, buy-now-pay-later, consumer, spain, checkout, payment-intents]
---

## Summary

Integration guide for SeQura payments across Checkout, Checkout Sessions API, PaymentIntents API, and Direct API. EUR only. return_url required. 7-day manual capture. Clarifies 7-120 day payment terms.

## Key Details

**API enum**: `sequra`. EUR only. `return_url` required.

**Payment terms**: 7–120 days (per integration guide description — not fixed 3/12 installments as the overview implies).

**Manual capture**: `capture_method: 'manual'`; 7-day window.

**Error codes**: `payment_intent_invalid_currency`, `payment_intent_authentication_failure`, `payment_intent_redirect_confirmation_without_return_url`.

## Raw Sources

- [[stripe-sequra-accept-payment-2025]] — verbatim webpage content (1390 lines); fixed `_Prices_` (×2), `_sandbox_` (×2), `_PaymentIntent_` (×2), `_client secret_` (×2), `_webhook_` (×2); downloaded 1 CDN image to `raw/assets/`
