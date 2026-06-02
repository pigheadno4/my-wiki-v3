---
title: "Dynamically Update Discounts"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-checkout-dynamic-discounts-2025.md"
tags: [stripe, checkout-sessions, discounts, coupons, dynamic-updates, runServerUpdate, private-preview, coupon-data]
---

## Summary

Private preview feature for dynamically applying or removing discounts on a Checkout Session from the server, triggered by client-side actions. Uses the same `runServerUpdate` pattern as dynamic shipping, line items, and trial durations.

## Key Constraints

- **Private preview**: SDK `stripe -v 15.1.0-beta.2`; API version `2025-03-31.basil; checkout_server_update_beta=v1;`
- **`permissions.update_discounts: 'server_only'`** on session creation — disables client-side discount application
- Same `betas: ['custom_checkout_server_updates_1']` client beta flag
- Payment Intents: manually calculate and modify the payment amount, or create a new PaymentIntent

## Session Setup

```js
stripe.checkout.sessions.create({
  ui_mode: 'elements',
  permissions: { update_discounts: 'server_only' },
  // ...
});
```

## Applying Discounts

Discounts can be applied inline with `coupon_data` — no pre-existing Coupon object needed:

```js
stripe.checkout.sessions.update(checkout_session_id, {
  discounts: [{
    coupon_data: {
      name: 'Customer Discount',
      amount_off: 1000,  // in cents
      currency: 'usd',
    }
  }]
});
```

To remove all discounts: `discounts: []`

> **Note**: The update response doesn't include the `discounts` field by default — use `expand` to see it.

## Server Endpoint Pattern

```
POST /apply-customer-discount
Body: { checkout_session_id }

1. Retrieve session: checkout.sessions.retrieve(id)
2. Validate discount request (custom logic)
3. Recompute discounts: calculate_customer_discount(customer_id, cart_total)
4. Update session: checkout.sessions.update(id, { discounts })

Response: { type: 'object', value: { succeeded: true } }
       or: { type: 'error', message: '...' }
```

## Client `runServerUpdate` Pattern

```js
// HTML+JS
const response = await checkout.runServerUpdate(() => fetch('/apply-customer-discount', {
  method: 'POST', headers: { 'Content-type': 'application/json' },
  body: JSON.stringify({ checkout_session_id: actions.getSession().id })
}));

// React: runServerUpdate from checkoutState.checkout.runServerUpdate(...)
```

## Use Cases

| Use case | Example |
| --- | --- |
| Loyalty discounts | Auto-apply based on customer tier |
| Cart value promotions | 10 USD off orders over 100 USD |
| Time-sensitive offers | Apply/remove promotional codes |
| Location-based discounts | Region-specific rates based on shipping address |
| Customer-specific offers | Personalized by segment or purchase history |

## Security Guidelines (Same as all runServerUpdate features)

- Specific endpoints per action, not generic "update"
- Pass only `session.id` from client; retrieve session data server-side

## Related Pages

- [[source-stripe-checkout-dynamic-line-items]] — companion feature (line items)
- [[source-stripe-checkout-dynamic-trials]] — companion feature (trial durations)
- [[source-stripe-checkout-dynamic-shipping]] — companion feature (shipping)
- [[stripe-checkout]] — Checkout concept page

## Raw Sources

- [[stripe-checkout-dynamic-discounts-2025]] — verbatim dynamic discounts guide
