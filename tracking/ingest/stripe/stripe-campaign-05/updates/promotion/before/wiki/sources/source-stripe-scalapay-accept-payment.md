---
title: "Stripe: Accept a Payment with Scalapay"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-scalapay-accept-payment-2025.md"
tags: [stripe, bnpl, scalapay, buy-now-pay-later, consumer, installments, checkout, payment-intents]
---

## Summary

Integration guide for Scalapay payments across Checkout, Checkout Sessions API, PaymentIntents API, and Direct API. EUR only. return_url required. 7-day manual capture. Notable: Checkout path restricted to only 8 EU countries despite wider merchant base.

## Key Details

**API enum**: `scalapay`. EUR only. `return_url` required.

**Checkout compatibility**: restricted to **IT, FR, ES, DE, NL, BE, IE, FI** only (8 EU countries) — narrower than the 28-country merchant base in the overview.

**Manual capture**: `capture_method: 'manual'`; 7-day window.

**Error codes**: `payment_intent_invalid_currency`, `payment_intent_authentication_failure`, `payment_intent_redirect_confirmation_without_return_url`.

## Raw Sources

- [[stripe-scalapay-accept-payment-2025]] — verbatim webpage content (1403 lines); fixed `_Prices_` (×2), `_sandbox_` (×2), `_PaymentIntent_` (×2), `_client secret_` (×2), `_webhook_` (×2); downloaded 1 CDN image to `raw/assets/`
