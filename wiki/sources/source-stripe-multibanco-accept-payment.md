---
title: "Stripe: Accept a Multibanco Payment"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-multibanco-accept-payment-2025.md"
tags: [stripe, vouchers, multibanco, portugal, eur, checkout, direct-api, ios, android, entity-reference, expiry]
---

## Summary

Integration guide for Multibanco via Checkout, Direct API (web), and iOS/Android SDK. `hosted_voucher_url` redirect pattern. 7-day voucher expiry + 4-day bank transfer buffer. `stripe.confirmMultibancoPayment()` for Direct API. Per-field `entity` + `reference` in `next_action.multibanco_display_details`. Cancelation auto-refunds mispaid amounts.

## Key Details

**Three integration paths**: Checkout, Direct API (web), iOS SDK (Android also covered).

**Checkout**: `payment_method_types: ['multibanco']`, EUR only. No subscription mode. `hosted_voucher_url` redirect (not `success_url`). Same 3 async webhook events as Boleto/Konbini.

**`next_action.multibanco_display_details`**: `entity`, `reference`, `expires_at`, `hosted_voucher_url`.

**Voucher expiry**: 7 days after creation. Lifecycle:
1. Expiry → `requires_action` → `processing` (4-day buffer for bank transfer delays)
2. Buffer expires → `requires_payment_method`
3. If funds arrive after buffer → Stripe auto-refunds

**Direct API**: `stripe.confirmMultibancoPayment()` — email only required in `billing_details`. Opens inline modal. `handleActions: false` to display manually.

**iOS SDK**: `STPPaymentHandler.confirmPayment()` with `STPPaymentMethodMultibancoParams` — presents webview.

**Cancelation**: invalidates voucher — must inform customer. If funds still arrive → Stripe auto-refunds.

**Test scenarios**: `fill_never@*` simulates 11-day expiry (live mode behavior).

## Raw Sources

- [[stripe-multibanco-accept-payment-2025]] — verbatim webpage content (1,166 lines); fixed `*Prices*` ×1, `*subscription*` ×1, `*webhooks*` ×1, `*fulfillment*` ×1, `*client secret*` ×3, `*PaymentMethod*` ×1, `*webhook*` ×3, `*sandbox*` ×2, `*confirm*` ×2
