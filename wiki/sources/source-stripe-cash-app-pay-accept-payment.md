---
title: "Stripe: Accept a Cash App Pay Payment"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-cash-app-pay-accept-payment-2025.md"
tags: [stripe, wallets, cash-app-pay, checkout, elements, direct-api, ios, android, manual-capture, authorization, qr-code]
---

## Summary

Integration guide for Cash App Pay via Checkout, Checkout Sessions API, Payment Intents API, Direct API, iOS, and Android. 60-minute authorization window. Desktop QR refreshable 20 times. Separate auth+capture (7-day window). Checkout supports setup and subscription modes. Live mode auto-approves after redirect.

## Key Details

**Four web integration paths + iOS + Android**.

**Checkout**: `payment_method_types: ['cashapp']`, USD only. Setup mode and Subscription mode both supported.

**60-minute authorization window** — much longer than Amazon Pay (10 min) or Swish (3 min). Desktop QR refreshable up to **20 times** before expiry.

**Separate authorization + capture**: `capture_method: 'manual'`, 7-day window (same as Amazon Pay).

**Direct API**: `payment_method_data: { type: 'cashapp' }` + `return_url`. Mobile: redirect to Cash App. Desktop: QR code displayed.

**iOS**: standard `STPPaymentHandler` flow.

**Test behavior**: sandbox shows test page with approve/decline button; **live mode auto-approves** after redirect — no in-app approval option.

## Raw Sources

- [[stripe-cash-app-pay-accept-payment-2025]] — verbatim webpage content (2,541 lines); fixed `*Prices*` ×2, `*client secret*` ×5, `*webhook*` ×4, `*PaymentMethod*` ×1, `*confirm*` ×2, `*sandbox*` ×1, `*require*` ×1
