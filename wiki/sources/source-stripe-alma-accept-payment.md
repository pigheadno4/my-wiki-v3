---
title: "Stripe: Accept a Payment with Alma"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-alma-accept-payment-2025.md"
tags: [stripe, bnpl, alma, buy-now-pay-later, checkout, payment-intents, elements, ios]
---

## Summary

Integration guide for Alma payments across four paths: Checkout, Elements, Direct API, and iOS Mobile Payment Element. Covers Alma-specific auth flows, 1-hour expiry, QR code desktop auth, manual capture, and error codes.

## Key Details

**1-hour expiry**: PaymentIntents in `requires_action` expire after **1 hour** (shortest of all BNPL methods: Affirm 12h, Afterpay 3h).

**`return_url` required** for Alma — must be provided when confirming.

**Two authentication modes**:
- **Mobile app**: customer redirected to Alma → authorizes → redirected back.
- **Desktop/web**: QR code displayed on page → customer scans with Alma app → payment confirmed. Session expires after 1 hour; QR can be refreshed up to 20 times.

**Manual capture**: `capture_method: 'manual'`; 7-day capture window; Stripe auto-cancels if not captured.

**Error codes**: `payment_intent_invalid_currency` (EUR only), `payment_intent_redirect_confirmation_without_return_url`.

## Raw Sources

- [[stripe-alma-accept-payment-2025]] — verbatim webpage content (1437 lines); fixed `_Prices_`, `_client secret_` (4×), `_webhook_` (4×); downloaded 1 CDN image to `raw/assets/`
