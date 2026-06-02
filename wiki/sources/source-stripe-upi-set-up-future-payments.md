---
title: "Stripe: Set Up Future UPI Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-upi-set-up-future-payments-2025.md"
tags: [stripe, real-time-payments, upi, india, inr, setup-intent, e-mandate, recurring, off-session, upi-autopay]
---

## Summary

Guide for saving UPI payment details for future charges via Checkout (setup mode) and Direct API (SetupIntent or PaymentIntent+setup_future_usage). Uses `stripe.confirmUpiSetup()`. `next_action.upi_handle_redirect_or_display_qr_code` exposes QR data. Full address required.

## Key Details

**Two integration paths**: Checkout and Direct API.

**Checkout**: `mode: 'setup'`, `payment_method_types: ['upi']` — customer authorizes e-mandate on hosted checkout page.

**Direct API — SetupIntent**: `stripe.confirmUpiSetup(clientSecret, { return_url, mandate_data: { customer_acceptance: { type: 'online', online: { infer_from_client: true } } } })` — UPI-specific method. Full billing address required (name, line1, line2, city, state, postal_code, country='IN').

**Direct API — PaymentIntent + `setup_future_usage: 'off_session'`**: charges immediately and saves for future. Same billing address requirement.

**`next_action.upi_handle_redirect_or_display_qr_code`**: `hosted_instructions_url`, `qrcode.image_url_png`, `qrcode.image_url_svg`, `qrcode.expires_at` (parallel structure to Swish).

**On-session saved payments still redirect to UPI app** — even with saved payment method, on-session confirmation always redirects.

**Detach**: `detachPaymentMethod` API → triggers `mandate.updated` + `payment_method.detached` events.

## Raw Sources

- [[stripe-upi-set-up-future-payments-2025]] — verbatim webpage content (571 lines); fixed `*subscription*` ×2, `*client secret*` ×2, `*confirm*` ×1
