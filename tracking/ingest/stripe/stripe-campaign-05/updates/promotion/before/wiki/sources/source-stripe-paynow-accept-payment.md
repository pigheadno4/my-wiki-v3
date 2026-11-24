---
title: "Stripe: Accept a PayNow Payment"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-paynow-accept-payment-2025.md"
tags: [stripe, real-time-payments, paynow, singapore, sgd, qr-code, checkout, direct-api]
---

## Summary

Integration guide for PayNow via Checkout and Direct API. Uses `stripe.confirmPayNowPayment()` for Direct API — a PayNow-specific method that renders a QR code inline without redirecting. No Elements path.

## Key Details

**Two integration paths**: Checkout and Direct API only — no Elements path.

**Checkout**: `payment_method_types: ['paynow']`, SGD only, SG business locations only. Test via **Generate QR code** button → scan URL → authorize or fail on Stripe-hosted test page.

**Direct API**:
- PaymentIntent requires both `payment_method_types: ['paynow']` and `payment_method_data: { type: 'paynow' }`
- Client-side: `stripe.confirmPayNowPayment(clientSecret)` — PayNow-specific method (not generic `confirmPayment`)
- Renders QR code **inline on the page** — no redirect. Page must remain open while customer scans
- Promise resolves when customer scans (`succeeded`) or closes modal (cancelled)
- Fulfillment via webhook (`payment_intent.succeeded`) — do not rely on customer returning to page

## Raw Sources

- [[stripe-paynow-accept-payment-2025]] — verbatim webpage content (289 lines); fixed `*Prices*` ×1, `*subscription*` ×1, `*client secret*` ×1, `*fulfillment*` ×1, `*webhook*` ×1
