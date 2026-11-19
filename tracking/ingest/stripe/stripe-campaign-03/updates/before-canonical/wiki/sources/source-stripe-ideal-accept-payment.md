---
title: "Stripe: Accept an iDEAL | Wero Payment"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-ideal-accept-payment-2025.md"
tags: [stripe, ideal, wero, netherlands, eur, checkout, elements, ios, android, react-native]
---

## Summary

Multi-platform integration guide for accepting iDEAL | Wero payments: Checkout (all modes), iOS, Android, React Native, and Elements. No minimum charge amount. 14-bank reference table. Test: "Authorize/Fail test payment" buttons on redirect page.

## Key Details

### Checkout path

- `payment_method_types: ['ideal']`, `eur`, payment/setup/subscription all supported

### iOS

- `STPPaymentMethodParams(billingDetails:)` (requires name) + `STPPaymentHandler.confirmPayment()` → webview

### Android

- `PaymentMethodCreateParams.create(ideal:, billingDetails:)` + `PaymentLauncher.confirm()`

### React Native

- `confirmPayment(clientSecret, { paymentMethodType: 'Ideal' })` + deep linking required

### Elements

- Payment Element with `automatic_payment_methods` (recommended) or manual `payment_method_types: ['ideal']`
- Also supports legacy `idealBank` element + `stripe.confirmIdealPayment()` (server-side manual redirect)
- No minimum charge amount

### 14 supported banks

abn_amro, asn_bank, bunq, ing, knab, n26, nn, rabobank, revolut, regiobank, sns_bank, triodos_bank, van_lanschot, yoursafe

## Raw Sources

- [[stripe-ideal-accept-payment-2025]] — verbatim webpage content (1497 lines, Checkout + iOS + Android + React Native + Elements)
