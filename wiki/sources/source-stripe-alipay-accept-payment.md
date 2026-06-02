---
title: "Stripe: Accept an Alipay Payment"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-alipay-accept-payment-2025.md"
tags: [stripe, wallets, alipay, china, checkout, ios, android, react-native, direct-api, custom-url-scheme]
---

## Summary

Integration guide for Alipay via Checkout, iOS (Swift), Android (Kotlin), React Native, and Direct API. All paths redirect to Alipay for authentication. iOS/React Native require custom URL scheme with `safepay/` host. Android offers Alipay SDK (app-to-app) or WebView fallback. Android SDK cannot test in sandbox — requires live mode.

## Key Details

**Five integration paths**: Checkout, iOS, Android, React Native, Direct API.

**Checkout**: `payment_method_types: ['alipay']`, any of 10 supported currencies. No subscription mode. Redirect-based.

**iOS (Swift)**: `STPPaymentHandler.confirmPayment()` with `STPPaymentMethodAlipayParams`. Return URL: custom URL scheme + `safepay/` host (e.g., `myapp://safepay/`).

**Android (Kotlin)**: Two options:
- Alipay SDK integration (app-to-app, more seamless): `confirmAlipayPayment()` with `AlipayAuthenticator` calling `PayTask.payV2()`
- WebView fallback: `stripe.confirmPayment()` — no Alipay SDK needed

**Android test limitation**: Alipay Android SDK does NOT support test payments — must use live mode to test the native app-to-app flow.

**React Native**: `confirmPayment()` with `paymentMethodType: 'Alipay'`. Custom URL scheme + `handleURLCallback()` required. `safepay/` return URL host.

**Direct API (web)**: `stripe.confirmAlipayPayment()` — standard redirect flow.

## Raw Sources

- [[stripe-alipay-accept-payment-2025]] — verbatim webpage content (1,139 lines); fixed `*Prices*` ×1, `*subscription*` ×1, `*webhook*` ×4, `*require*` ×1, `*client secret*` ×1; 1 PNG screenshot downloaded to assets/
