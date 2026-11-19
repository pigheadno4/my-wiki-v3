---
title: "Stripe: Accept a Payment with Amazon Pay"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-amazon-pay-accept-payment-2025.md"
tags: [stripe, wallets, amazon-pay, checkout, elements, direct-api, ios, android, manual-capture, authorization]
---

## Summary

Integration guide for Amazon Pay via Checkout, Elements (PaymentIntents), Direct API, iOS, and Android. 10-minute authorization window. Separate authorization + capture supported (7-day capture window). Error code note: docs say `payment_intent_invalid_currency` only supports USD — contradicts multi-currency overview.

## Key Details

**Four web integration paths + iOS + Android**.

**Checkout**: `payment_method_types: ['amazon_pay']`. Redirect to Amazon.

**Elements (PaymentIntents)**: `stripe.confirmPayment` with `return_url`. **10-minute authorization window** — PaymentIntent reverts to `requires_payment_method` if not completed.

**Separate authorization + capture**: `capture_method: 'manual'`. 7-day capture window; `payment_intent.canceled` if window expires. Can partially capture with `amount_to_capture`.

**Direct API**: `stripe.confirmPayment` with `payment_method_data: { type: 'amazon_pay' }` + `return_url`.

**iOS**: Mobile Payment Element recommended (standard `STPPaymentHandler`).

**Error code note**: `payment_intent_invalid_currency` description says "only supports usd" — likely a doc error given the multi-currency table in the overview page.

**Error codes**: `payment_intent_invalid_currency`, `missing_required_parameter`, `payment_intent_payment_attempt_failed`, `payment_intent_redirect_confirmation_without_return_url`.

## Raw Sources

- [[stripe-amazon-pay-accept-payment-2025]] — verbatim webpage content (1,381 lines); fixed `*Prices*` ×1, `*client secret*` ×4, `*webhook*` ×4; 1 PNG screenshot downloaded to assets/
