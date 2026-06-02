---
title: "Stripe: Accept Titres-Restaurant Payments"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-fr-meal-vouchers-accept-payment-2025.md"
tags: [stripe, meal-vouchers, france, titres-restaurant, payment-intents, elements]
---

## Summary

Integration guide for French meal vouchers payments via Payment Element (Elements path). Covers PaymentIntent creation with SIRET, save-for-future-use CVC requirement, and test data.

## Key Details

**Applies to**: Bimpli, Pluxee, Up Déjeuner only (not Swile).

**Prerequisite**: SIRET must be provisioned with Stripe before use.

**PaymentIntent creation** (EUR only):
```
POST /v1/payment_intents
  amount=1211
  currency=eur
  payment_details[benefit][fr_meal_voucher][siret]=42424242424242
```

**Save for future use**: CVC required on first payment. Can be reused without CVC after that.

**Complete payment**: `confirmPayment` via Payment Element with `return_url`.

**Test data**:

| Issuer | Card number | CVC | Expiry |
| --- | --- | --- | --- |
| Bimpli with Conecs | `4000002501000002` | Any 3 digits | Any future date |

Test SIRETs: `42424242424242` (valid provisioned), `00000000000000` (invalid).

## Raw Sources

- [[stripe-fr-meal-vouchers-accept-payment-2025]] — verbatim webpage content (70 lines)
