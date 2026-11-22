---
title: "Stripe: Accept a Payment with Kriya"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-kriya-accept-payment-2025.md"
tags: [stripe, bnpl, kriya, buy-now-pay-later, b2b, uk, checkout, payment-intents, elements]
---

## Summary

Integration guide for Kriya payments across Checkout, Checkout Sessions API, PaymentIntents API, and Direct API. GBP only, UK only. Mirrors Billie/Alma structure.

## Key Details

**API enum**: `kriya`. GBP only, UK only. `return_url` required.

**Manual capture**: `capture_method: 'manual'`; 7-day window. Same as Billie/Alma.

**Error codes**: `payment_intent_invalid_currency`, `payment_intent_authentication_failure`, `payment_intent_redirect_confirmation_without_return_url`.

## Raw Sources

- [[stripe-kriya-accept-payment-2025]] — verbatim webpage content (1390 lines); fixed `_Prices_` (×2), `_sandbox_` (×2), `_PaymentIntent_` (×2), `_client secret_` (×2), `_webhook_` (×2); downloaded 1 CDN image to `raw/assets/`
