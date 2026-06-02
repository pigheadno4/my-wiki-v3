---
title: "Stripe: Accept a Bancontact Payment"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-bancontact-accept-payment-2025.md"
tags: [stripe, bancontact, belgium, eur, checkout, elements, ios, android, react-native]
---

## Summary

Multi-platform integration guide for accepting Bancontact payments: Checkout, Direct API (Elements + React), iOS, Android, and React Native. Covers PaymentIntent creation, `preferred_language`, bank account details on charge, and optional server-side redirect flow.

## Key Details

### Checkout path

- `payment_method_types: ['card', 'bancontact']`, `eur` only
- Payment/setup/subscription modes all supported
- No special test numbers — select Bancontact and click Pay

### Direct API path

- `stripe.confirmBancontactPayment(clientSecret, { payment_method: { billing_details: { name } }, return_url })` — redirects to Bancontact, immediate result on return
- `preferred_language`: `fr`, `nl`, `de`, or `en` (default) — set via `payment_method_options.bancontact.preferred_language`
- Bank account details on charge: `bank_code`, `bank_name`, `bics`, `iban_last4`, `preferred_language`, `verified_name`
- Optional server-side redirect: create + confirm PaymentIntent, check `requires_action` + `redirect_to_url`, redirect manually; retrieve status via `retrievePaymentIntent` on return

### iOS

- `STPPaymentMethodBancontactParams` + `STPPaymentMethodBillingDetails` (name required) + `STPPaymentHandler.confirmPayment()` → webview redirect

### Android

- `PaymentMethodCreateParams.createBancontact(billingDetails)` + `PaymentLauncher.confirm()`

### React Native

- `confirmBancontactPayment()` (truncated in paste — same pattern as iOS/Android)

## Raw Sources

- [[stripe-bancontact-accept-payment-2025]] — verbatim webpage content (1425 lines, Checkout + Direct API + iOS + Android + React Native sections)
