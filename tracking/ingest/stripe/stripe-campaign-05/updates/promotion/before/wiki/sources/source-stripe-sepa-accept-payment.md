---
title: "Stripe: Accept a SEPA Direct Debit Payment"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-sepa-accept-payment-2025.md"
tags: [stripe, sepa, sepa-debit, eu, eur, iban, checkout, elements, ios, android, mandates, test-ibans]
---

## Summary

Multi-platform integration guide for accepting SEPA Direct Debit payments: Checkout, Elements (Payment Element), iOS, and Android. Includes the comprehensive per-country IBAN test table (17 countries, 8 scenarios each), mandate reference_prefix customization, and target_date.

## Key Details

### Checkout path

- `payment_method_types: ['sepa_debit']` (or alongside `'card'`)
- All line items in `eur`; payment/setup/subscription modes supported
- Optional `reference_prefix` (12 chars, uppercase/numbers/spaces/`./_/-/&`, not starting with `STRIPE`) → 24-char mandate reference
- Optional `target_date`: 3–15 days out

### Elements (PaymentElement) path

- `stripe.confirmPayment({ elements, return_url })` — automatically collects IBAN + mandate
- PaymentIntent webhooks: `payment_intent.processing` / `payment_intent.succeeded` / `payment_intent.payment_failed`
- Wait at least 6 business days before considering payment successful

### iOS path

- `STPPaymentHandler` with `paymentIntentParams` (same flow as AU/NZ BECS)

### Test IBANs — 8 scenarios per country

| Scenario | Token pattern | Behavior |
| --- | --- | --- |
| success | `pm_success_{cc}` | Succeeds |
| successDelayed | `pm_successDelayed_{cc}` | Succeeds after 3+ min |
| failed | `pm_failed_{cc}` | Fails immediately |
| failedDelayed | `pm_failedDelayed_{cc}` | Fails after 3+ min |
| disputed | `pm_disputed_{cc}` | Succeeds then dispute |
| exceedsWeeklyVolumeLimit | `pm_exceedsWeeklyVolumeLimit_{cc}` | Fails: `charge_exceeds_source_limit` |
| exceedsWeeklyTransactionLimit | `pm_exceedsWeeklyTransactionLimit_{cc}` | Fails: `charge_exceeds_weekly_limit` |
| insufficientFunds | `pm_insufficientFunds_{cc}` | Fails: `insufficient_funds` |

Country codes: `at`, `be`, `hr`, `ee`, `fi`, `fr`, `de`, `gi`, `ie`, `li`, `lt`, `lu`, `nl`, `no`, `pt`, `es`, `se`, `ch`, `gb` (19 countries).

## Raw Sources

- [[stripe-sepa-accept-payment-2025]] — verbatim webpage content (1678 lines, Checkout + Elements + iOS + Android sections)
