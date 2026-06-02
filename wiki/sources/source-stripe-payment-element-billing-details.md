---
title: "Control Billing Details Collection in the Payment Element"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-payment-element-billing-details-2025.md"
tags: [stripe, payment-element, billing-details, address-collection, fields, if_required, never, auto]
---

## Summary

Reference guide for the `fields.billingDetails` option on the Payment Element. Three modes control how billing details (address, name, email) are collected.

## The Three Modes

| Mode | Behavior | Trade-off |
| --- | --- | --- |
| `auto` (default) | Stripe decides per payment method based on friction vs auth rate | Best balance |
| `never` | Field hidden for all payment methods; **must** pass value manually at confirm time | Requires manual injection at confirm |
| `if_required` | Collect only fields strictly required per payment method | Higher network fees (IC+ pricing); potential auth rate impact |

Can be set globally (all billing fields) or per-field: `address`, `name`, `email`.

## `never` Pattern

```js
// Create — hide address
elements.create('payment', { fields: { billingDetails: { address: 'never' } } });

// Confirm — must manually supply hidden fields
stripe.confirmPayment({
  payment_method: {
    billing_details: {
      address: { line1: '123 Main Street', city: 'Anytown', country: 'US', postal_code: '12345' }
    }
  }
});
```

**Critical**: failing to pass hidden fields at confirm time will break payment methods that require them.

## `if_required` Pattern

```js
elements.create('payment', { fields: { billingDetails: { address: 'if_required' } } });
```

Reduces friction but may increase network fees (IC+ pricing plans) and affect authorization rates.

## Address Element Integration

For full billing address collection, use the Address Element in billing mode alongside the Payment Element — billing details attach automatically at confirmation.

## Related Pages

- [[source-stripe-payment-element]] — primary Payment Element source
- [[stripe-address-element]] — Address Element for full billing address collection

## Raw Sources

- [[stripe-payment-element-billing-details-2025]] — verbatim billing details control guide
