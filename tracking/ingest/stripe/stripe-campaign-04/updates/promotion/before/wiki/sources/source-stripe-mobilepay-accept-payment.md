---
title: "Stripe: Accept a MobilePay Payment"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-mobilepay-accept-payment-2025.md"
tags: [stripe, wallets, mobilepay, denmark, finland, checkout, elements, direct-api, ios, android, manual-capture, 5-minute-window]
---

## Summary

Integration guide for MobilePay via Checkout, Elements, Direct API, iOS, and Android. 5-minute authorization window across all paths. Manual capture supported (full amount only). `next_action.redirect_to_url` for Direct API. Refunds/disputes subject to Visa/Mastercard rules.

## Key Details

**Four web integration paths + iOS + Android**.

**Checkout**: `payment_method_types: ['mobilepay']`, EUR/DKK/SEK/NOK, EEA. No subscription/setup mode. Manual capture via `payment_intent_data.capture_method: 'manual'`.

**5-minute authorization window** — consistent across all paths. PaymentIntent reverts to `requires_payment_method` on timeout.

**Direct API**: `payment_method_types: ['mobilepay']` + `payment_method_data: { type: 'mobilepay' }`. `next_action.redirect_to_url`. Full amount capture only (no partial manual capture).

**iOS**: `STPPaymentHandler.confirmPayment()` with `STPPaymentMethodMobilePayParams`. Custom URL scheme required.

**Android**: `PaymentLauncher.confirm()` with standard `ConfirmPaymentIntentParams`.

**Cancellation**: `PaymentIntents.cancel()`.

**Refunds/disputes**: subject to Visa/Mastercard network rules.

## Raw Sources

- [[stripe-mobilepay-accept-payment-2025]] — verbatim webpage content (1,888 lines); fixed `*Prices*` ×1, `*webhook*` ×4, `*client secret*` ×4, `*confirm*` ×3, `*PaymentMethod*` ×2, `*require*` ×1
