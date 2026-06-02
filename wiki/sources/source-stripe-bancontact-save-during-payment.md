---
title: "Stripe: Save Bank Details During a Bancontact Payment"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-bancontact-save-during-payment-2025.md"
tags: [stripe, bancontact, belgium, eur, sepa-debit, iban, mandates, save-payment-method, ios, android, react-native]
---

## Summary

Guide for using a Bancontact payment to save the customer's IBAN as a SEPA Direct Debit PaymentMethod for future recurring charges. Covers Direct API, iOS, Android, and React Native. Key flow: Bancontact payment with `setup_future_usage: 'off_session'` → get `generated_sepa_debit` PaymentMethod ID from charge → use for future SEPA payments.

## Key Details

### Flow

1. Create Customer
2. Create PaymentIntent: `payment_method_types: ['bancontact']`, `setup_future_usage: 'off_session'`, `customer`
3. Display SEPA mandate text (7 languages: de/en/es/fi/fr/it/nl) — required
4. `stripe.confirmBancontactPayment()` with `billing_details.name` + `billing_details.email`
5. On return: retrieve PaymentIntent with `expand: ['latest_charge']` → find `generated_sepa_debit` ID under `payment_method_details.bancontact`
6. Charge future payments: create SEPA PaymentIntent with `payment_method_types: ['sepa_debit']` + `payment_method: '{{SEPA_DEBIT_PM_ID}}'`

### Mandate text

Must display SEPA mandate authorization text before payment. Standard text authorizes both the merchant and Stripe to debit the account; customer agrees to receive pre-debit notifications up to 2 days before each charge.

### Test via email / PaymentMethod

**6 test email patterns**: `generatedSepaDebitIntentsSucceed@example.com`, `...SucceedDelayed@example.com`, `...Fail@example.com`, `...FailDelayed@example.com`, `...SucceedDisputed@example.com`, `...FailsDueToInsufficientFunds@example.com`

**6 test PaymentMethod tokens**: `pm_bancontact_generatedSepaDebitIntentsSucceed` (and variants)

## Raw Sources

- [[stripe-bancontact-save-during-payment-2025]] — verbatim webpage content (1864 lines, Direct API + iOS + Android + React Native)
