---
title: "Stripe: Save SEPA Direct Debit Details for Future Payments"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-sepa-set-up-payment-2025.md"
tags: [stripe, sepa, sepa-debit, eu, eur, iban, checkout, setup-intents, elements, ios, android, mandates]
---

## Summary

Guide for saving SEPA Direct Debit payment method details for future payments using Checkout setup mode or SetupIntents (Elements, iOS, Android). Includes same 19-country IBAN test table and mandate reference_prefix as the accept-a-payment source.

## Key Details

### Checkout setup mode

- `mode: 'setup'`, `customer` required, `payment_method_types: ['card', 'sepa_debit']`
- Stripe-hosted and embedded page variants

### Elements (SetupIntent) path

- Create SetupIntent → pass `clientSecret` → `stripe.confirmSetup()` / `stripe.confirmSepaDebitSetup()` opens IBAN collection modal with mandate
- SetupIntent webhooks: `setup_intent.succeeded` / `setup_intent.setup_failed`

### Mandate reference_prefix

- Same as accept-a-payment: 12 chars max, uppercase/numbers/spaces/`./_/-/&`, not starting with `STRIPE`
- Applies to PaymentIntent, SetupIntent, Checkout payment mode, Checkout setup mode

### Test IBANs

Same 19-country table as [[source-stripe-sepa-accept-payment]] — identical IBAN numbers and tokens.

## Raw Sources

- [[stripe-sepa-set-up-payment-2025]] — verbatim webpage content (1578 lines, Checkout + Elements + iOS + Android sections)
