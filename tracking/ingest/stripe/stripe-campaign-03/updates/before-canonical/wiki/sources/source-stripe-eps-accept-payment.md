---
title: "Stripe: Accept an EPS Payment"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-eps-accept-payment-2025.md"
tags: [stripe, eps, austria, eur, checkout, ios, android, react-native, elements]
---

## Summary

Multi-platform integration guide for accepting EPS payments: Checkout, iOS, Android, React Native, and Elements (legacy). EPS requires customer name in billing details; no special test numbers for Checkout.

## Key Details

### Checkout path

- `payment_method_types: ['eps']`, `eur` only, payment mode only (no setup/subscription)
- No special test numbers — select EPS and click Pay

### iOS

- `STPPaymentMethodEPSParams()` + billing name + `STPPaymentHandler.confirmPayment()`

### Android

- `PaymentMethodCreateParams.createEps(billingDetails)` + `PaymentLauncher.confirm()`

### React Native

- `confirmPayment(clientSecret, { paymentMethodType: 'Eps', paymentMethodData: { billingDetails } })`
- Requires deep linking setup (custom URL scheme, not universal links)

### Elements (Legacy)

- `epsBank` element (legacy, not recommended) + `stripe.confirmEpsPayment()`
- EPS PaymentMethods are single-use — cannot be reused or saved to customers

## Raw Sources

- [[stripe-eps-accept-payment-2025]] — verbatim webpage content (1623 lines, Checkout + iOS + Android + React Native + Elements legacy)
