---
title: "Stripe: Use iDEAL | Wero to Set Up Future SEPA Direct Debit Payments"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-ideal-set-up-payment-2025.md"
tags: [stripe, ideal, wero, netherlands, eur, sepa-debit, iban, setup-intents, mandates, ios, android, react-native]
---

## Summary

Guide for using iDEAL | Wero with a SetupIntent to save IBAN as SEPA mandate **without an initial payment**. Key difference from save-during-payment: Stripe charges 0.01 EUR then immediately refunds — customer only authorizes. Covers Checkout, Elements, iOS, Android, React Native.

## Key Details

### Key distinction from save-during-payment

- **This guide**: SetupIntent — no real payment, 0.01 EUR charged and refunded, mandate-only authorization
- **Save-during-payment**: PaymentIntent — real payment + mandate simultaneously

### Checkout setup mode

- `mode: 'setup'`, `payment_method_types: ['ideal']`, `customer_account`/`customer`
- After: retrieve SetupIntent with `expand: ['latest_attempt']` → `generated_sepa_debit`

### Elements/iOS/Android/React Native

- `setupIntents.create({ payment_method_types: ['ideal'], customer_account/customer })`
- `stripe.confirmSetup()` / `STPPaymentHandler.confirmSetupIntent()` / `PaymentLauncher.confirm()`
- Must display SEPA mandate text (7 languages) — same as save-during-payment
- Webhook: `setup_intent.succeeded`

### Same 6 test email + 6 token patterns as save-during-payment

## Raw Sources

- [[stripe-ideal-set-up-payment-2025]] — verbatim webpage content (1777 lines, Checkout + Elements + iOS + Android + React Native)
