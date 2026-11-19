---
title: "Stripe: Accept an Alipay Payment"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/alipay/accept-a-payment"
raw_files:
  - "stripe-alipay-accept-payment-2025.md"
tags: [stripe, wallets, alipay, china, checkout, ios, android, react-native, direct-api, custom-url-scheme]
---

## Summary

The detailed 2026-05-07 guide describes a single-use Alipay payment: the customer authenticates through Alipay after a website or app redirect, then returns for a payment-status notification. Its five paths are Checkout, iOS, Android, React Native, and Direct API. The 2026-11-07 canonical capture supplies only a purpose sentence and links to those variants. It does not revalidate implementation details, eligibility, SDK versions, or payment outcomes.

## Key Details

### Checkout and currency scope (2026-05-07 guide)

- Checkout lists China as customer geography, ten supported currencies (`aud`, `cad`, `eur`, `gbp`, `hkd`, `jpy`, `nzd`, `sgd`, `usd`, `myr`) and eleven presentment currencies including `cny`. Its listed modes are payment yes, setup no, subscription no. Every line-item Price must use the same currency and be one-time; this is not a blanket ability to use any currency from any merchant account (old raw lines 18-40).
- The hosted and embedded Checkout examples use `mode: "payment"` and include `alipay` in `payment_method_types` alongside `card`. Hosted uses `success_url`; embedded uses `return_url` and `ui_mode: "embedded_page"` (old raw lines 48-105).
- The mobile and Direct API sections say the merchant account must have a bank account for a listed currency, and the currency usable for an Alipay payment maps to the merchant country; their tables separately include `cny`. Customers see their purchase amount in CNY. Preserve this distinction from Checkout's supported-versus-presentment lists rather than promising unrestricted currency or current account eligibility (old raw lines 349-367, 639-657, 885-903, 1121-1139).

### Client and server flows (2026-05-07 guide)

- For iOS, Android, React Native, and Direct API, create a PaymentIntent on the server with `alipay`, amount, and a supported currency; pass its client secret to the client. A created Intent is a payment attempt, not a completed charge (old raw lines 223-237, 466-480, 735-749, 924-942).
- iOS registers a custom URL scheme and forwards the return URL to Stripe; `STPPaymentHandler.confirmPayment` with `STPPaymentMethodAlipayParams` launches the Alipay app or a webview. The old iOS example sets the return URL to `{{URL SCHEME}}://safepay/` (old raw lines 239-322). Its iOS 13 compatibility statement is May-dated (old raw line 151).
- Android app-to-app requires the Alipay SDK; Stripe `confirmAlipayPayment` passes data through an `AlipayAuthenticator` to Alipay `PayTask.payV2`. The May guide says the Alipay Android SDK cannot process test payments, so full testing of that native path uses live mode. A distinct option without the Alipay SDK calls Stripe `confirmPayment` to open an Alipay WebView; do not apply the app-to-app test limitation to every Android flow (old raw lines 439-441, 504-611). The `23.7.0` dependency is a dated example (old raw lines 394-415).
- React Native registers a custom URL scheme, forwards the `safepay/` return URL to `handleURLCallback`, and calls `confirmPayment(clientSecret, { paymentMethodType: "Alipay" })` (old raw lines 751-857).
- Web Direct API passes the PaymentIntent client secret to Stripe.js `stripe.confirmAlipayPayment` with `return_url`. The return page must verify PaymentIntent status rather than treating the return as success. For optional manual server redirect, confirm the Intent with a return URL, check `requires_action` plus `next_action.type: "alipay_handle_redirect"`, and redirect to that action URL (old raw lines 924-1093). The Stripe.js `dahlia` URL is a May example, not a November-confirmed version (old raw lines 1011-1030).
- The guide recommends `payment_intent.succeeded` asynchronous events for fulfillment instead of a client callback. Neither a Session, created/confirmed Intent, redirect, app/browser return, or the November index proves successful payment or settlement (old raw lines 323-327, 613-617, 859-863, 1095-1099).

## Conflict and capture boundary

The existing [[stripe-wallets]] matrix labels Alipay Redirect “No,” while its Alipay section and this dated full guide describe Alipay authentication through a redirect (old raw lines 18, 909, 1030-1052; concept lines 16 and 319). The reciprocal concept row should be corrected with a May-date qualification. The November raw is a five-link variant index; no linked November variant body was captured. The collection diff's wholesale replacement therefore establishes presentation and navigation only, not a new no-redirect path or a deprecation.

## Related

- [[stripe]] — Stripe company route.
- [[stripe-wallets]] — wallet comparison and Alipay concept route.

## Raw Sources

- [[raw/stripe-alipay-accept-payment-2025|2026-05-07 full Alipay acceptance guide]] — factual integration and example evidence; 1,139 lines.

## Related raw API references

- [[raw/stripe-payments-alipay-accept-a-payment-2026-11-07|2026-11-07 Alipay variant index]] — navigation-only capture of Checkout, Direct API, iOS, Android, and React Native links; no linked variant behavior inferred.
