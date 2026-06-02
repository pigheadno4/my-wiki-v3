---
title: "Stripe: Save a French Meal Voucher Payment Method"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-fr-meal-vouchers-save-payment-2025.md"
tags: [stripe, meal-vouchers, france, titres-restaurant, setup-intent, save-payment]
---

## Summary

How to save a French meal vouchers card using SetupIntent for future on-session charging. Covers the SetupIntent API shape, subsequent PaymentIntent creation with saved card, temporary auth charge behavior, and test data.

## Key Details

**SetupIntent creation**:
```js
stripe.setupIntents.create({
  customer: CUSTOMER_ID,
  setup_details: {
    benefit: { fr_meal_voucher: { siret: '42424242424242' } }
  }
})
```

**Charging saved card** (on-session, EUR only):
```
POST /v1/payment_intents
  customer, payment_method, confirm=true
  payment_details[benefit][fr_meal_voucher][siret]=42424242424242
```

**Temporary auth charge**: Stripe may send a 0.30 EUR authorization when saving to verify the card. Reversed almost immediately — restored to customer's daily balance.

**Test data**: card `4000002501000002` (Bimpli with Conecs). Test SIRETs: `42424242424242` (valid), `00000000000000` (invalid).

## Raw Sources

- [[stripe-fr-meal-vouchers-save-payment-2025]] — verbatim webpage content (92 lines); fixed `_on-session_` → `*on-session*`
