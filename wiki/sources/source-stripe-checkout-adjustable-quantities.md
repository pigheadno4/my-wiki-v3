---
title: "Make Line Item Quantities Adjustable"
type: source
date_ingested: 2026-04-21
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/checkout/adjustable-quantity"
raw_files:
  - "stripe-checkout-adjustable-quantities-2025.md"
tags: [stripe, checkout-sessions, line-items, adjustable-quantity, updateLineItemQuantity, fulfillment]
---

## Summary

The full 2026-04-21 guide describes quantity adjustment for Checkout Session line items. Its server and client examples use the Checkout Elements path (`ui_mode: "elements"`). The 2026-11-07 capture at this URL is only a variant index for Full page and Embedded form; it does not contain either variant body or renew the April API, bounds, or lifecycle details. The April integration changes quantities, not the set of line items.

## Session Setup (2026-04-21 Elements example)

Set `line_items[].adjustable_quantity.enabled: true` while creating the Checkout Session on the server. The captured Node example uses `mode: "payment"`, `ui_mode: "elements"`, and a `return_url`:

```js
stripe.checkout.sessions.create({
  line_items: [{
    price_data: { /* currency, product_data, unit_amount */ },
    quantity: 1,
    adjustable_quantity: {
      enabled: true,
      minimum: 0,   // default: 0
      maximum: 100, // example override; default: 99; allowed up to 999999
    },
  }],
  mode: "payment",
  ui_mode: "elements",
  return_url: "{{RETURN_URL}}",
});
```

The April guide says the default minimum is 0 and maximum is 99; `adjustable_quantity.maximum` may be set up to 999999. Checkout prevents removal of the last remaining item. Adding a new line item is outside this quantity-only integration. See old raw lines 14-49.

## Client Quantity Update (2026-04-21 Elements example)

The April HTML/JS example initializes `stripe.initCheckoutElementsSdk({ clientSecret })`, calls `loadActions()`, takes a line-item ID and current quantity from the loaded Session's `lineItems`, and calls `actions.updateLineItemQuantity({ lineItem, quantity })` on interaction. Its React example uses `useCheckout` and `checkoutState.checkout.updateLineItemQuantity`. These calls are shown for that captured Elements/custom Checkout route; the November variant index does not establish them for both linked UI variants. See old raw lines 51-110.

```js
actions.updateLineItemQuantity({ lineItem: lineItemId, quantity: newQty });
// React example: checkoutState.checkout.updateLineItemQuantity({ lineItem: props.lineItem, quantity: props.quantity + 1 });
```

The `lineItem` argument is the Checkout Session line-item ID, not a Product or Price ID.

## Payment Intents Boundary (2026-04-21)

The guide separately says Payment Intents API integrations must track line-item changes themselves and modify the payment amount or create a new PaymentIntent with adjusted amounts. This is distinct from `updateLineItemQuantity` on the Checkout Session client path. See old raw lines 8-12.

## Post-Payment Reconciliation (2026-04-21)

After payment completes, the guide says to request finalized line items and quantities. A removed item is absent from the line-items response. Its Node `checkout.session.completed` webhook example calls `stripe.checkout.sessions.listLineItems(session.id, { limit: 100 }, ...)`; the suggested `checkout_session.metadata` and `price.metadata` map those items to an internal order. The example's `fulfillOrder` is an unfinished TODO that throws, so the snippet illustrates reconciliation plumbing rather than successful fulfillment of an order. It does not establish any observed payment outcome. See old raw lines 113-181.

## November Variant Index

The 2026-11-07 root capture gives a short purpose sentence and links to `?ui=full-page` and `?ui=checkout-form` versions. Neither linked body is pinned here. Their current setup, controls, bounds, and payment lifecycle remain unresolved from this capture.

## Related Pages

- [[stripe]] — Stripe company route.
- [[stripe-checkout]] — Checkout concept and reciprocal dated quantity scope.
- [[source-stripe-how-checkout-works]] — broader Checkout overview.
- [[source-stripe-checkout-dynamic-amounts]] — separately scoped dynamic amount updates.

## Related raw API references

- [[raw/stripe-payments-checkout-adjustable-quantity-2026-11-07|2026-11-07 adjustable-quantity variant index]] — navigation only; links to Full page and Embedded form variants without their bodies.

## Raw Sources

- [[raw/stripe-checkout-adjustable-quantities-2025|2026-04-21 full adjustable-quantity guide]] — dated factual evidence for the Elements example and reconciliation pattern.
