---
title: "Stripe: Use Bancontact to Set Up Future SEPA Direct Debit Payments"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-bancontact-set-up-payment-2025.md"
tags: [stripe, bancontact, belgium, eur, sepa-debit, iban, setup-intents, mandates, ios, android, react-native]
---

## Summary

Guide for using Bancontact with a SetupIntent (no real payment) to save customer's IBAN as a SEPA Direct Debit PaymentMethod for future charges. Stripe charges 0.02 EUR then immediately refunds it. Key difference from save-during-payment: uses `confirmBancontactSetup()` (not `confirmBancontactPayment`). Covers Checkout, Direct API, iOS, Android, React Native.

## Key Details

### Key distinction from save-during-payment

- **This guide**: SetupIntent — no initial payment, Stripe charges/refunds 0.02 EUR to verify IBAN
- **Save-during-payment**: PaymentIntent with `setup_future_usage: 'off_session'` — saves IBAN as side effect of actual payment

### Checkout path

- `mode: 'setup'`, `payment_method_types: ['bancontact']`, `customer` required
- After: retrieve SetupIntent with `expand: ['latest_attempt']` → `generated_sepa_debit` ID

### Direct API path

- `stripe.confirmBancontactSetup(clientSecret, { payment_method: { billing_details: { name, email } }, return_url })`
- SetupIntent webhook: `setup_intent.succeeded`
- Must display SEPA mandate text (7 languages) before setup

### Future charges

Retrieve SetupIntent with `expand: ['latest_attempt']` → get `generated_sepa_debit` → create SEPA PaymentIntent with `confirm: true`

### Test patterns

Same 6 test email patterns + 6 `pm_bancontact_generatedSepaDebitIntents*` tokens as save-during-payment source.

## Raw Sources

- [[stripe-bancontact-set-up-payment-2025]] — verbatim webpage content (1679 lines, Checkout + Direct API + iOS + Android + React Native)
