---
title: "Stripe Checkout: Save Payment Details During Payment"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-save-during-payment-2025.md"
tags: [stripe, checkout, save-payment, setup-future-usage, payment-methods, allow-redisplay, off-session, customer-creation]
---

## Summary

Guide for saving customer payment details during a one-time Checkout payment. Covers two save strategies (`setup_future_usage` vs `saved_payment_method_options`), the `allow_redisplay` field that controls prefill behavior, customer creation requirements, PM removal, and legal compliance notes.

## Key Takeaways

- **Default**: payment methods used in one-time payment mode are NOT saved for future use
- **Two paths to save**:
  1. `payment_intent_data.setup_future_usage: 'off_session'` — saves for off-session charging; `allow_redisplay: 'limited'` (won't prefill at next checkout)
  2. `saved_payment_method_options.payment_method_save: 'enabled'` — optional checkbox for customer; `allow_redisplay: 'always'` (will prefill); no `setup_future_usage` needed
- **`customer_creation: 'always'`** required when no existing customer is passed (otherwise session won't save PM)
- **Subscription mode**: auto-saves PM with `allow_redisplay: 'limited'`
- **`allow_redisplay`**: `always` = prefills at next checkout; `limited` = blocked from prefill (complies with card network rules + data protection)
- **Card-only prefill**: Checkout only prefills saved cards, not other PM types
- **Remove saved PM**: `saved_payment_method_options.payment_method_remove: 'enabled'`; customer can't remove if tied to active subscription with no backup PM
- **Legal**: consult legal team before `setup_future_usage` — GDPR implications (EDPB guidance on storing card data)

## `allow_redisplay` Semantics

| Value | Source | Prefills in Checkout | Notes |
| --- | --- | --- | --- |
| `always` | `payment_method_save: 'enabled'` + customer checks box | Yes | Explicitly consented |
| `limited` | `setup_future_usage` or subscription mode | No | Complies with card network/data rules |

## Path 1: `setup_future_usage`

```js
stripe.checkout.sessions.create({
  customer_creation: 'always',  // or pass existing customer
  mode: 'payment',
  payment_intent_data: { setup_future_usage: 'off_session' },
  ...
})
```

Saved PM: available for off-session charging. Won't prefill in Checkout. Recommend using `custom_text` to disclose saved PM terms.

## Path 2: `saved_payment_method_options`

```js
stripe.checkout.sessions.create({
  customer_creation: 'always',
  mode: 'payment',  // or 'subscription'
  saved_payment_method_options: {
    payment_method_save: 'enabled',
    payment_method_remove: 'enabled',  // optional
  },
  ...
})
```

Displays optional checkbox. Customer consent → `allow_redisplay: 'always'` → prefills at next checkout. No `setup_future_usage` needed.

## Accounts v2

Use `customer_account` instead of `customer`. Same `saved_payment_method_options` params apply.

## Related Pages

- [[stripe-saved-payment-methods]] — concept page
- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-checkout-save-and-reuse]] — Setup mode (save WITHOUT initial payment)

## Raw Sources

- [[stripe-checkout-save-during-payment-2025]] — Save during payment: two save strategies, allow_redisplay, customer_creation, PM removal, subscription auto-save, card-only prefill, legal/GDPR note, hosted + embedded variants
