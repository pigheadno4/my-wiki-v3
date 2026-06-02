---
title: "Stripe: Accept a Payment with Billie"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-billie-accept-payment-2025.md"
tags: [stripe, bnpl, billie, buy-now-pay-later, b2b, checkout, payment-intents, elements]
---

## Summary

Integration guide for Billie payments across Checkout, Checkout Sessions API (Elements), PaymentIntents API, and Direct API paths. Covers Billie-specific constraints, manual capture, and error codes.

## Key Details

**Payment terms**: 7–120 days (not just "Pay in 30" — the full invoice terms range).

**EUR only** for Checkout/Elements integration. `return_url` required.

**Manual capture**: `capture_method: 'manual'`; 7-day window; Stripe auto-cancels if not captured.

**`line_items` data improves approval rates** — include cart details for early access to Unified line items feature.

**Error codes**: `payment_intent_invalid_currency`, `payment_intent_authentication_failure`, `payment_intent_redirect_confirmation_without_return_url`.

## Raw Sources

- [[stripe-billie-accept-payment-2025]] — verbatim webpage content (1914 lines); fixed `_Prices_` (2×), `_sandbox_` (2×), `_PaymentIntent_` (2×), `_client secret_` (4×), `_webhook_` (4×); downloaded 1 CDN image to `raw/assets/`
