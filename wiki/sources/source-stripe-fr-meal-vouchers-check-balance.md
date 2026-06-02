---
title: "Stripe: Check French Meal Vouchers Balances"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-fr-meal-vouchers-check-balance-2025.md"
tags: [stripe, meal-vouchers, france, titres-restaurant, balance-check, split-tender]
---

## Summary

How to check the available balance on a French meal voucher before payment. Covers the balance check API, response structure, test card, and recommended split tender ordering.

## Key Details

**Balance check is non-binding**: doesn't hold funds; concurrent purchases can deplete balance between check and charge.

**Prerequisite**: card must be saved as a payment method first.

**API**: `POST /v1/payment_methods/:id/check_balance`

**Response**:
```json
{
  "object": "payment_method_balance",
  "as_of": 1750768577,
  "balance": {
    "fr_meal_voucher": {
      "available": [{ "amount": 2500, "currency": "eur" }]
    }
  }
}
```
`as_of` is the Unix timestamp when balance was retrieved; balance may change after.

**Test**: `pm_card_conecs_fr_frMealVoucher` always returns 10.00 EUR in sandbox.

**Split tender order**: always charge secondary payment method first (meal vouchers can't be refunded); alternatively use auth+capture for meal voucher portion after secondary payment succeeds.

## Raw Sources

- [[stripe-fr-meal-vouchers-check-balance-2025]] — verbatim webpage content (89 lines)
