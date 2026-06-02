---
title: "Stripe: Save Payment Details with Pix"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-pix-save-payment-details-2025.md"
tags: [stripe, real-time-payments, pix, brazil, brl, setup-intent, mandates, pix-automatico, recurring, off-session]
---

## Summary

Guide for saving Pix payment details for recurring use via Checkout and Direct API. Requires Pix Automático mandate. Uses Pix-specific JS methods: `stripe.confirmPixSetup()` and `stripe.confirmPixPayment()`. QR code data exposed via `next_action.pix_display_qr_code`.

## Key Details

**Saving Pix requires Pix Automático mandate** — must specify `mandate_options` (at minimum `amount` and `payment_schedule`) in `payment_method_options.pix`. Mandate can be revoked by customer in banking app → Stripe sends `mandate.updated` → bring customer back on-session.

**Two integration paths**: Checkout and Direct API (no Elements path).

**Checkout paths**:
- **Save without charging** (`mode: 'setup'`): creates SetupIntent; customer authorizes mandate; PaymentMethod attached to Customer
- **Save while charging** (`mode: 'payment'` + `setup_future_usage: 'off_session'`): charges first payment and saves for future

**Direct API — SetupIntent**: `stripe.confirmPixSetup(clientSecret, { payment_method: { billing_details: { name, email, tax_id } }, return_url })`. Returns `next_action.pix_display_qr_code`.

**Direct API — PaymentIntent**: `stripe.confirmPixPayment(clientSecret, { payment_method: { billing_details: { name, email, tax_id } }, return_url })`. Same `next_action` structure.

**`next_action.pix_display_qr_code` fields**:
- `data` — Pix copy-paste string (EMV)
- `image_url_svg`, `image_url_png` — QR code images
- `expires_at` — expiration unix timestamp
- `hosted_instructions_url` — Stripe-hosted QR page

Use `handleActions: false` to render QR code manually instead of Stripe's modal.

**Off-session recurring charge**: `PaymentIntents.create({ payment_method, off_session: true, confirm: true })`.

**Test email scenarios for save/recurring** (extend one-time scenarios):
- `succeed_mandate_expire_payments_immediately@*` — mandate created; recurring payments expire immediately
- `succeed_mandate_expire_payments_with_delay@*` — mandate created; recurring payments expire after 3 minutes
- `succeed_immediately@*` — mandate created; recurring payments succeed immediately

## Raw Sources

- [[stripe-pix-save-payment-details-2025]] — verbatim webpage content (870 lines); fixed `*webhook*` ×14 (approx), `*subscription*` ×1, `*client secret*` ×2
