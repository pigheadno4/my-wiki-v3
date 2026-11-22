---
title: "Stripe: Accept a Przelewy24 Payment"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-p24-accept-payment-2025.md"
tags: [stripe, p24, przelewy24, poland, eur, pln, checkout, ios, android, react-native, elements]
---

## Summary

Multi-platform integration guide for accepting P24 payments: Checkout, iOS, Android, React Native, and Elements (legacy). Key: billing email required; statement descriptor limited to 14 chars; P24 regulations consent required.

## Key Details

### Checkout path

- `payment_method_types: ['p24']`, EUR or PLN, payment mode only
- No special test numbers — select P24 and click Pay

### iOS

- `STPPaymentMethodPrzelewy24Params()` + `billing_details.email` (required) + `STPPaymentHandler.confirmPayment()`

### Android

- `PaymentMethodCreateParams.createP24(billingDetails)` + `PaymentLauncher.confirm()`

### React Native

- `confirmPayment(clientSecret, { paymentMethodType: 'P24' })` + deep linking required

### Elements (Legacy)

- `p24Bank` element + `stripe.confirmP24Payment()` + `return_url`; customer email required
- Also: optional `tos_shown_and_accepted: true` in P24 params if accepting regulations terms on customer's behalf

### Statement descriptor

- Max **14 characters**
- Appears on bank statement as: `/OPT/X/////P24-XXX-XXX-XXX {descriptor}`

## Raw Sources

- [[stripe-p24-accept-payment-2025]] — verbatim webpage content (1587 lines, Checkout + iOS + Android + React Native + Elements legacy)
