---
title: "Stripe: Accept a GrabPay Payment"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-grabpay-accept-payment-2025.md"
tags: [stripe, wallets, grabpay, singapore, malaysia, checkout, ios, android, react-native, direct-api, no-minimum]
---

## Summary

Integration guide for GrabPay via Checkout, iOS, Android, React Native, and Direct API. No minimum charge amount. Subscriptions explicitly not supported. Direct API uses `stripe.confirmGrabPayPayment()`. Android requires billing details name.

## Key Details

**Four integration paths**: Checkout, iOS, Android, React Native, Direct API.

**No minimum charge amount** — can be as low as 1 SGD/MYR.

**Subscriptions not supported** — explicitly stated in opening callout.

**Checkout**: `payment_method_types: ['grabpay']`. SGD (SG) or MYR (MY). No subscription/setup mode.

**iOS**: `STPPaymentHandler.confirmPayment()` with `STPPaymentMethodGrabPayParams()`. Custom URL scheme required. Webview presents GrabPay site.

**Android**: `PaymentLauncher.confirm()` with `PaymentMethodCreateParams.createGrabPay(billingDetails)`. `name` required in billing details.

**React Native**: `confirmPayment()` with `paymentMethodType: 'GrabPay'`. Custom URL scheme + `handleURLCallback()` required.

**Direct API**: `stripe.confirmGrabPayPayment(clientSecret, { return_url })`. Test: Stripe-hosted GrabPay test page with approve/fail options.

## Raw Sources

- [[stripe-grabpay-accept-payment-2025]] — verbatim webpage content (1,134 lines); fixed `*Subscriptions*` ×1, `*Prices*` ×1, `*subscription*` ×1, `*client secret*` ×2, `*webhook*` ×4, `*require*` ×1
