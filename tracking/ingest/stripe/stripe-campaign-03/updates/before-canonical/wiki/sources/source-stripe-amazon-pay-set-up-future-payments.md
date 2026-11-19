---
title: "Stripe: Set Up Future Amazon Pay Payments"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-amazon-pay-set-up-future-payments-2025.md"
tags: [stripe, wallets, amazon-pay, setup-intent, recurring, off-session, mandates, ios, android]
---

## Summary

Guide for saving Amazon Pay for future charges via Checkout (setup mode), Direct API (SetupIntent or PaymentIntent+setup_future_usage), iOS, and Android. Uses `stripe.confirmAmazonPaySetup()`. `next_action.type: 'redirect_to_url'`. Authorization text required before first save. Detach triggers mandate.updated + payment_method.detached events.

## Key Details

**Four paths**: Checkout, Direct API, iOS, Android.

**Checkout**: `mode: 'setup'`, `payment_method_types: ['amazon_pay']` — customer authorizes mandate on hosted Checkout.

**Direct API — SetupIntent**: `stripe.confirmAmazonPaySetup(clientSecret, { return_url, mandate_data: { customer_acceptance: { type: 'online', online: { infer_from_client: true } } } })`.

**Direct API — PaymentIntent + setup_future_usage**: `setup_future_usage: 'off_session'` + `mandate_data`. Off-session charge: `paymentIntents.create({ payment_method, off_session: true, confirm: true })`.

**`next_action.type: 'redirect_to_url'`**: Amazon Pay's next_action (different from voucher methods that use display_details).

**Authorization text required**: merchant must display specific language ("By continuing, you authorize [Business] to debit your Amazon Pay account...") before first save.

**iOS**: `STPPaymentHandler.confirmSetupIntent()` with `STPPaymentMethodAmazonPayParams()`.

**Android**: `PaymentLauncher.confirm()` with `PaymentMethodCreateParams.createAmazonPay()`.

**Detach**: `detachPaymentMethod` → `mandate.updated` + `payment_method.detached` events.

## Raw Sources

- [[stripe-amazon-pay-set-up-future-payments-2025]] — verbatim webpage content (1,143 lines); fixed `*off-session*` ×3, `*subscription*` ×2, `*client secret*` ×2, `*confirm*` ×1
