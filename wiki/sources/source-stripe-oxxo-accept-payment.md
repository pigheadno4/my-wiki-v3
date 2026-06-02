---
title: "Stripe: Accept an OXXO Payment"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-oxxo-accept-payment-2025.md"
tags: [stripe, vouchers, oxxo, mexico, mxn, checkout, elements, direct-api, ios, android, expires-after-days]
---

## Summary

Integration guide for OXXO via Checkout, Checkout Sessions API, Payment Intents API, Direct API (web), iOS, and Android. `hosted_voucher_url` redirect. `expires_after_days`: 1–7 days, default 3. `stripe.confirmOxxoPayment()` for Direct API. `next_action.oxxo_display_details.expires_after` (not `expires_at`). Legacy section marked deprecated.

## Key Details

**Four web integration paths + iOS + Android** — broadest coverage of any voucher method.

**Checkout**: `payment_method_types: ['oxxo']`, MXN only, MX only. No subscription mode. `hosted_voucher_url` redirect. Same 3 async webhook events. `expires_after_days`: 1–7 days, default 3, expiry at 23:59 America/Mexico_City (UTC-6).

**`next_action.oxxo_display_details`**: `hosted_voucher_url`, `expires_after` (note: field name is `expires_after`, not `expires_at` as with Multibanco/Konbini).

**Direct API**: `stripe.confirmOxxoPayment()` — OXXO-specific method. Email only required in `billing_details`.

**`fill_never` test**: expires after 1 business day + 2 calendar days.

**Legacy section**: present in the guide; marked deprecated — not the recommended integration path.

## Raw Sources

- [[stripe-oxxo-accept-payment-2025]] — verbatim webpage content (2,513 lines); fixed `*Customers*` ×2, `*Prices*` ×1, `*subscription*` ×1, `*webhooks*` ×1, `*fulfillment*` ×1, `*sandbox*` ×2, `*PaymentIntent*` ×2, `*client secret*` ×4, `*webhook*` ×1, `*Legacy*` ×1
