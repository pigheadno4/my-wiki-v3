---
title: "Stripe: Set Up Future Cash App Pay Payments"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-cash-app-pay-set-up-payment-2025.md"
tags: [stripe, wallets, cash-app-pay, setup-intent, recurring, off-session, mandate, cashtag, ios, android]
---

## Summary

Guide for saving Cash App Pay for future charges via Checkout (setup mode), Direct API (SetupIntent or PaymentIntent+setup_future_usage), iOS, and Android. Uses `stripe.confirmCashappSetup()`. `mobile_auth_url` expires in 30 seconds. Authorization text required. Revocation via Cash App app or detachPaymentMethod.

## Key Details

**Three paths**: Checkout, Direct API, iOS/Android.

**Checkout**: `mode: 'setup'`, `payment_method_types: ['cashapp']`.

**Direct API — SetupIntent**: `stripe.confirmCashappSetup(clientSecret, { payment_method: { type: 'cashapp' }, return_url })`. 10-minute session. Desktop QR: refreshable 20×. `mobile_auth_url` expires **30 seconds** — must redirect immediately; call `retrieveSetupIntent` to get new one if expired.

**`next_action.cashapp_handle_redirect_or_display_qr_code`**: `mobile_auth_url`, `qr_code.image_url_svg/png`, `qr_code.expires_at`, `hosted_instructions_url`.

**Authorization text required**: "By continuing, you authorize [Business] to debit your Cash App account..." — only required on first save of customer's $Cashtag.

**PaymentMethod revocation**: customer via Cash App app → `mandate.updated` → call `detachPaymentMethod`. Or customer via merchant UI → call `detachPaymentMethod`. Both trigger `payment_method.detached`.

**iOS**: `STPPaymentHandler.confirmSetupIntent()` with `STPPaymentMethodCashAppParams()`.

**Android**: `PaymentLauncher.confirm()` with `PaymentMethodCreateParams.createCashAppPay()`.

## Raw Sources

- [[stripe-cash-app-pay-set-up-payment-2025]] — verbatim webpage content (850 lines); fixed `*Customer*` ×3, `*off-session*` ×3, `*subscription*` ×2, `*client secret*` ×3
