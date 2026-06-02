---
title: "Stripe: Customer Balance"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-customer-balance-2025.md"
tags: [stripe, customer-balance, bank-transfers, payments, reconciliation, invoicing]
---

## Summary

Overview of the Stripe customer balance system: cash vs invoice balance distinctions, how to retrieve balances, how to make payments directly from the cash balance, and the 7 cash balance transaction types.

## Key Details

**Two balance types**:
- **Cash balance**: bank transfer funds held for reconciliation. Not a wallet/e-money. Per-currency. Usable for future payments or returned to bank.
- **Invoice balance**: liability offset; applies to future invoices only; not usable for direct payment.

**Retrieve cash balance**: `stripe.customers.retrieve(id, { expand: ['cash_balance'] })`. Returns `cash_balance.available.{currency}` amount and `cash_balance.settings.reconciliation_mode`. Works for Accounts v2 via `/v1/customers/acct_xxxxx`.

**Pay from cash balance**:
```js
stripe.paymentIntents.create({
  amount, currency,
  customer: customer.id,           // or customer_account for Accounts v2
  payment_method_types: ['customer_balance'],
  payment_method_data: { type: 'customer_balance' },
  confirm: true,
})
```
Succeeds immediately if sufficient balance; fails otherwise.

**7 cash balance transaction types**:

| Type | Cause |
| --- | --- |
| `funded` | Incoming bank transfer |
| `applied_to_payment` | Funds applied to PaymentIntent |
| `unapplied_from_payment` | Partially funded PI modified/canceled |
| `refunded_from_payment` | Successful PI refunded to cash balance |
| `return_initiated` | Unspent funds being returned to bank |
| `return_canceled` | Return attempt failed/canceled |
| `transferred_to_balance` | Swept to Stripe balance (failed refund) |

## Raw Sources

- [[stripe-customer-balance-2025]] — verbatim webpage content (186 lines); fixed `_invoice balance_` and `_Invoices_` → `*italic*`
