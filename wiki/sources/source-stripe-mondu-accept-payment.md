---
title: "Stripe: Accept a Payment with Mondu"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-mondu-accept-payment-2025.md"
tags: [stripe, bnpl, mondu, buy-now-pay-later, b2b, europe, checkout, payment-intents, elements]
---

## Summary

Integration guide for Mondu payments across Checkout, Checkout Sessions API, PaymentIntents API, and Direct API. EUR only for Checkout path. Mirrors Billie/Kriya structure.

## Key Details

**API enum**: `mondu`. EUR only for Checkout integration. `return_url` required.

**Manual capture**: `capture_method: 'manual'`; 7-day window. Same as Billie/Kriya.

**Error codes**: `payment_intent_invalid_currency`, `payment_intent_authentication_failure`, `payment_intent_redirect_confirmation_without_return_url`.

## Raw Sources

- [[stripe-mondu-accept-payment-2025]] — verbatim webpage content (1392 lines); fixed `_Prices_` (×2), `_sandbox_` (×2), `_PaymentIntent_` (×2), `_client secret_` (×2), `_webhook_` (×2); downloaded 1 CDN image to `raw/assets/`
