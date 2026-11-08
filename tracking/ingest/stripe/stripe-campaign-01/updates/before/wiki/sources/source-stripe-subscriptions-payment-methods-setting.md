---
title: "Stripe Subscriptions — Set Payment Methods Per-Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-payment-methods-setting-2026.md"
tags: [stripe, billing, subscriptions, payment-methods, payment-settings, payment-update-link]
---

## Summary

Guide to `payment_settings.payment_method_types` — per-subscription override of which payment methods a customer can use. Also covers payment update links (Dashboard-only) and the `save_default_payment_method` flag.

## Per-subscription payment method override

```js
stripe.subscriptions.update(subId, {
  payment_settings: {
    payment_method_types: ['card', 'customer_balance']
  }
})
```

Passed to the subscription's SetupIntent and all generated invoices.

**Critical pitfall**: if a `default_payment_method` is already set on the customer or subscription, it must be included in `payment_method_types`. If omitted, that PM won't be used and payment may fail.

## Payment method priority

1. Subscription `payment_settings.payment_method_types` (per-subscription, highest)
2. Account Invoice default PM configuration
3. Legacy `customer.default_source`

## `save_default_payment_method`

When enabled (via Dashboard invoice settings or `payment_settings.save_default_payment_method` on subscription), any PM the customer uses to pay becomes the new subscription default.

## Payment update links (Dashboard only)

Single-use links for customers to update their payment method on a `charge_automatically` subscription.

Restrictions:
- Subscription status must be `active`, `past_due`, or `trialing` — not `unpaid` or ended
- New PM must be a **card** (not other PM types)
- Single-use — each link allows one update
- Expires after **30 days** if unused
- Does NOT change the customer's default PM — only the subscription's PM

## Error scenarios

- PM restricted by currency or amount limitations → subscription creation fails
- PM not activated for account → error
- PM can't finalize invoice → payment-time error (see invoicing payment method errors docs)

## Related pages

- [[stripe-subscriptions-invoices]] — payment collection priority chain
- [[source-stripe-billing-collection-method]] — collection methods overview
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-payment-methods-setting-2026]] — verbatim Stripe docs webpage
