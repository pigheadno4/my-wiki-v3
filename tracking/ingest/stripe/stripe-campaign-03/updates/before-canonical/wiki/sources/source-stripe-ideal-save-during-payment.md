---
title: "Stripe: Save Bank Details During an iDEAL | Wero Payment"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-ideal-save-during-payment-2025.md"
tags: [stripe, ideal, wero, netherlands, eur, sepa-debit, iban, mandates, save-payment-method, ios, android, react-native]
---

## Summary

Guide for saving IBAN as a SEPA Direct Debit PaymentMethod during an iDEAL | Wero payment. Same pattern as Bancontact save-during-payment. Covers Elements, iOS, Android, React Native.

## Key Details

### Flow

1. Create Customer
2. Create PaymentIntent: `payment_method_types: ['ideal']`, `setup_future_usage: 'off_session'`, `customer`
3. Display SEPA mandate text (7 languages) — required; collect name + email
4. `stripe.confirmPayment()` → redirect → IBAN saved as `generated_sepa_debit` PaymentMethod
5. Retrieve PaymentIntent with `expand: ['latest_charge']` → get `generated_sepa_debit`
6. Charge future payments: SEPA PaymentIntent with `confirm: true`

### Test patterns (same 6 email + 6 token patterns as Bancontact)

Email: `generatedSepaDebitIntentsSucceed@example.com`, `...SucceedDelayed`, `...Fail`, `...FailDelayed`, `...SucceedDisputed`, `...FailsDueToInsufficientFunds`

Tokens: `pm_ideal_generatedSepaDebitIntents{Succeed|SucceedDelayed|Fail|FailDelayed|SucceedDisputed|FailsDueToInsufficientFunds}`

## Raw Sources

- [[stripe-ideal-save-during-payment-2025]] — verbatim webpage content (1877 lines, Elements + iOS + Android + React Native)
