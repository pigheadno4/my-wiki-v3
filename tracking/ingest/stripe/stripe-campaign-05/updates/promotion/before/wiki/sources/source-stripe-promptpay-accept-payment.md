---
title: "Stripe: Accept a PromptPay Payment"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-promptpay-accept-payment-2025.md"
tags: [stripe, real-time-payments, promptpay, thailand, thb, checkout, direct-api, qr-code]
---

## Summary

Integration guide for PromptPay via Checkout and Direct API. Uses `stripe.confirmPromptPayPayment()` — a PromptPay-specific method that opens an inline QR modal. Only requires customer email (simpler than PayNow or Pix). No Elements path.

## Key Details

**Two integration paths**: Checkout and Direct API only — no Elements path (same structure as PayNow).

**Checkout**: `payment_method_types: ['promptpay']`, THB only, TH business locations only. Test via **Generate QR code** → scan URL → authorize or fail.

**Direct API**: `stripe.confirmPromptPayPayment(clientSecret, { payment_method: { type: 'promptpay', billing_details: { email } } })` — PromptPay-specific method. Opens inline QR modal; promise resolves when customer scans (`succeeded`) or closes modal (cancelled). Only billing field required: `email`.

**Test**: *Sandboxes* show **Simulate scan** button instead of real QR code.

**Fulfillment**: via `payment_intent.succeeded` webhook — do not rely on customer returning to page.

## Raw Sources

- [[stripe-promptpay-accept-payment-2025]] — verbatim webpage content (318 lines); fixed `*Prices*` ×1, `*subscription*` ×1, `*client secret*` ×1, `*fulfillment*` ×1, `*webhook*` ×1, `*Sandboxes*` ×1
