---
title: "Stripe Subscriptions — Set Up Bank Transfer Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-bank-transfers-2026.md"
tags: [stripe, billing, subscriptions, bank-transfers, customer-balance, send-invoice]
---

## Summary

Short integration guide for bank transfer subscriptions. Key constraints: `send_invoice` only, `customer_balance` PM type, cash balance required, customer/account association mandatory.

## Required subscription parameters

```js
stripe.subscriptions.create({
  customer: customerId,       // or customer_account for Accounts v2
  items: [{ price: priceId }],
  collection_method: 'send_invoice',  // REQUIRED — charge_automatically not supported
  days_until_due: 30,                  // customer payment window
  payment_settings: {
    payment_method_types: ['customer_balance']  // REQUIRED
  }
})
```

## How it works

1. Subscription due → Stripe sends invoice to customer's email
2. If cash balance has sufficient funds → invoice auto-marked paid
3. Otherwise → invoice includes bank transfer instructions + Hosted Invoice Page link
4. Funds arrive → Stripe performs automatic or manual reconciliation
5. Subsequent invoices use the same price

## Accounts v2 cash balance note

To manage cash balance for customer-configured Accounts: use `v1/customers/acct_xxxxx/cash_balances` (Customer API with Account ID as path param, not a dedicated Accounts v2 endpoint).

## Subscription schedule

```js
stripe.subscriptionSchedules.create({ from_subscription: subscriptionId })
```

Create from existing subscription to schedule future changes.

## Testing

Use Stripe Dashboard or CLI to simulate inbound fund transfer. Stripe then runs automatic or manual reconciliation on the invoice.

## Related pages

- [[stripe-bank-transfers]] — concept page (updated with subscription facts)
- [[stripe-customer-balance]] — customer cash balance
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-bank-transfers-2026]] — verbatim Stripe docs webpage
