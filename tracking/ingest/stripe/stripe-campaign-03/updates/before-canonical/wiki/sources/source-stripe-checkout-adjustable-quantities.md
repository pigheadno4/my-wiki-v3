---
title: "Make Line Item Quantities Adjustable"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-checkout-adjustable-quantities-2025.md"
tags: [stripe, checkout-sessions, line-items, adjustable-quantity, updateLineItemQuantity, fulfillment]
---

## Summary

Reference guide for client-side line item quantity adjustment in Checkout Sessions. Covers session setup, the `updateLineItemQuantity` client API, and post-payment reconciliation. **Quantity changes only** — adding new line items is not supported via this integration.

## Session Setup

```js
stripe.checkout.sessions.create({
  line_items: [{
    price_data: { ... },
    quantity: 1,
    adjustable_quantity: {
      enabled: true,
      minimum: 0,   // default: 0
      maximum: 100, // default: 99; absolute max: 999,999
    },
  }],
  mode: 'payment',
  ui_mode: 'elements',
});
```

Checkout prevents removing the last item (customer must always have ≥1 item).

## Client Update API

```js
// HTML+JS
actions.updateLineItemQuantity({ lineItem: lineItemId, quantity: newQty });

// React
checkoutState.checkout.updateLineItemQuantity({ lineItem: props.lineItem, quantity: props.quantity + 1 });
```

Line item `id` comes from `session.lineItems[n].id`.

## Post-Payment Reconciliation

```js
// In checkout.session.completed webhook handler
stripe.checkout.sessions.listLineItems(session.id, { limit: 100 }, (err, lineItems) => {
  fulfillOrder(session, lineItems);
});
```

- Removed items are absent from the response
- Store internal order/item IDs in `checkout_session.metadata` and `price.metadata` for reconciliation

## Limitations

- **Quantity changes only** — cannot add new line items
- Payment Intents: must manually track updates and modify the payment amount

## Related Pages

- [[source-stripe-how-checkout-works]] — also covers adjustable_quantity basics
- [[source-stripe-checkout-dynamic-amounts]] — dynamic amount updates (broader)
- [[stripe-checkout]] — Checkout concept page

## Raw Sources

- [[stripe-checkout-adjustable-quantities-2025]] — verbatim adjustable quantities guide
