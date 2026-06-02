---
title: "Stripe: Accept a Konbini Payment"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-konbini-accept-payment-2025.md"
tags: [stripe, vouchers, konbini, japan, jpy, checkout, direct-api, confirmation-number, product-description, expires-after-days]
---

## Summary

Integration guide for Konbini via Checkout and Direct API. Customer redirected to `hosted_voucher_url`. Configurable expiry (1–60 days). `stripe.confirmKonbiniPayment()` for Direct API. Per-store payment codes in `next_action.konbini_display_details`. Optional confirmation number and product description. Refunds require customer bank input (45-day timeout).

## Key Details

**Two integration paths**: Checkout and Direct API (no Elements path).

**Checkout**: `payment_method_types: ['konbini']`, JPY only, JP only. No subscription mode. Customer redirected to `hosted_voucher_url` (not `success_url`). Same 3 async webhook events as Boleto: `checkout.session.completed`, `async_payment_succeeded`, `async_payment_failed`.

**`expires_after_days`**: 1–60 days, default 3. Expiry at 23:59:59 JST. `expires_at` (Unix timestamp) also supported — must be 30+ min from now. Mutually exclusive with `expires_after_days`.

**`product_description`**: up to 22 chars, Shift JIS only, shown at convenience store kiosk. Default: generic Japanese placeholder.

**`confirmation_number`**: 10–11 digit string (commonly customer's phone). If too common across ongoing transactions → rejected (`payment_intent_konbini_rejected_confirmation_number`). All-zeros blocked. Optional on Checkout form; random if not provided.

**Direct API**: `stripe.confirmKonbiniPayment()` — Konbini-specific method; opens inline modal with per-store payment codes. `handleActions: false` to render instructions manually.

**`next_action.konbini_display_details`**: per-store `payment_code` + `confirmation_number`, `expires_at`, `hosted_voucher_url`, `stores` map.

**Expiration buffer**: after `expires_at`, customer can't initiate but may still complete if payment slip already issued. Buffer period avoids premature failures.

**Refund flow**: customer submits bank account → Stripe processes → 45-day timeout → `failed`. Each partial refund may incur fee.

**Optional emails**: payment instruction emails + reminder emails (opt-in via Dashboard Email Settings).

## Raw Sources

- [[stripe-konbini-accept-payment-2025]] — verbatim webpage content (892 lines); fixed `*Prices*` ×1, `*subscription*` ×1, `*webhooks*` ×1, `*fulfillment*` ×1, `*initiate*` ×1, `*complete*` ×1, `*client secret*` ×1, `*unset*` ×2, `*placeholder*` ×1, `*PaymentMethod*` ×1, `*webhook*` ×1
