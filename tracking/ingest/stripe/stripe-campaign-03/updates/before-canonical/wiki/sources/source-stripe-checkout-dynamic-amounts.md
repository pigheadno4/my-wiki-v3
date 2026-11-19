---
title: "Dynamically Update Payment Amounts"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-checkout-dynamic-amounts-2025.md"
tags: [stripe, checkout-sessions, payment-intents, dynamic-amounts, runServerUpdate, line-items, price-data]
---

## Summary

Reference guide for dynamically updating payment amounts on both Checkout Sessions (via `runServerUpdate` + `line_items`) and Payment Intents (`paymentIntents.update({ amount })`). Both paths require server-side calculation — never trust client-provided amounts.

## Security Rules (Both Paths)

- Recalculate amounts **server-side only** — never trust client prices
- Authorize updates per business rules (e.g. max quantities)
- Only update sessions/intents that are active: check `status !== 'complete'` and `expires_at`
- Cannot increase amount **after confirmation**

## Checkout Sessions Path

Uses `runServerUpdate` + `line_items` with `price_data`:

```js
// Client wraps server call
const response = await actions.runServerUpdate(() =>
  fetch('/update-custom-amount', {
    method: 'POST',
    body: JSON.stringify({ checkout_session_id: session.id, product_id: 'gift_wrap' })
  })
);

// Server adds ad-hoc line item
await stripe.checkout.sessions.update(checkout_session_id, {
  line_items: [{
    price_data: {
      currency: 'usd',
      product_data: { name: 'Gift Wrap' },
      unit_amount: 500,
    },
    quantity: 1,
  }],
});
// Returns updated.amount_total — taxes recalculated automatically
```

Key: `price_data` enables ad-hoc charges without pre-creating a Price object. Updating `line_items` recalculates session total and taxes automatically.

## Payment Intents Path

Simpler — directly update the amount on the PaymentIntent:

```js
// Server
const pi = await stripe.paymentIntents.update(payment_intent_id, { amount });
return res.json({ id: pi.id, amount: pi.amount, client_secret: pi.client_secret });

// Client: refresh UI, then confirm when ready
// Developer is responsible for keeping client and server in sync
```

No `runServerUpdate` here — developer owns the full update + confirm cycle.

## Timing Constraint

| State | Can update? |
| --- | --- |
| `requires_payment_method` | ✓ Yes |
| `requires_confirmation` | ✓ Yes |
| After confirmation | ✗ Cannot increase amount |
| `complete` / expired | ✗ No |

## Use Cases

- Add/remove add-ons (gift wrap, warranty)
- Change shipping method or delivery speed
- Add additional services or charges
- Apply/remove discount codes or store credit

## Related Pages

- [[source-stripe-checkout-dynamic-line-items]] — companion feature (line item updates via runServerUpdate)
- [[source-stripe-checkout-dynamic-discounts]] — companion feature (discount updates)
- [[stripe-checkout]] — Checkout concept page
- [[stripe-payment-intents]] — Payment Intents concept page

## Raw Sources

- [[stripe-checkout-dynamic-amounts-2025]] — verbatim dynamic amounts guide (both API paths)
