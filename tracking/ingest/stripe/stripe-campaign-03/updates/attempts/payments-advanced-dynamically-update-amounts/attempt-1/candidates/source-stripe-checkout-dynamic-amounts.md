---
title: "Dynamically Update Payment Amounts"
type: source
date_ingested: 2026-04-21
date_updated: 2026-11-15
canonical_url: https://docs.stripe.com/payments/advanced/dynamically-update-amounts
original_format: webpage
raw_files:
  - "stripe-checkout-dynamic-amounts-2025.md"
tags: [stripe, checkout-sessions, payment-intents, dynamic-amounts, runServerUpdate, line-items, price-data]
---

## Summary

The April 21, 2026 full guide describes two dated paths for changing totals while a customer changes selections: Checkout Sessions with client `runServerUpdate` and server `line_items`/`price_data`, and PaymentIntents with server `paymentIntents.update({ amount })` followed by client refresh. Both require trusted server recalculation and authorization. The November 7 capture at this canonical URL is only a variant index linking Checkout Sessions embedded components and Payment Intents Elements; it contains no refreshed implementation or state rules.

## Security and state boundaries (April 21 guide)

- For both API paths, recalculate amounts **server-side** from trusted catalog and business rules; do not trust client prices or totals. Authorize the requested change, including quantity limits.
- For Checkout Sessions, update only an active Session that has not completed or expired. The dated sample retrieves the Session and checks `status === 'complete'` and `expires_at` before updating. These are Checkout Session fields and checks, not a PaymentIntent status/expiry rule.
- For a PaymentIntent, the guide gives awaiting-payment examples `requires_payment_method` and `requires_confirmation`. It says that after confirmation the amount **generally** cannot be increased; this dated qualification does not identify exceptions. Do not project a Session's `complete` or `expires_at` fields onto an Intent.

## Checkout Sessions path (April 21 full variant)

Uses `runServerUpdate` + `line_items` with `price_data`:

```js
// Client wraps server call
const response = await actions.runServerUpdate(() =>
  fetch('/update-custom-amount', {
    method: 'POST',
    body: JSON.stringify({ checkout_session_id: session.id, product_id: 'gift_wrap' })
  })
);

// Dated server example submits one illustrative ad-hoc line item
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

In the April example, `price_data` supplies an ad-hoc charge without a pre-created Price. Updating `line_items` or `price_data` recalculates the Session total and taxes. The snippet submits one illustrative item and does not prove preservation of other cart items; the merchant must validate the complete cart and amount on the server. A successful Session update refreshes checkout state but is not payment confirmation.

## Payment Intents path (April 21 full variant)

The server receives a selection change, recomputes the total from trusted data, updates the PaymentIntent amount while it is in an updatable state, then returns the Intent or client secret. The client refreshes its displayed total and confirms only when the customer is ready. The raw guide's `computeOrderAmount` is a TODO placeholder, not a finished pricing implementation.

Dated server sketch:

```js
// Server
const pi = await stripe.paymentIntents.update(payment_intent_id, { amount });
return res.json({ id: pi.id, amount: pi.amount, client_secret: pi.client_secret });

// Client: refresh UI, then confirm when ready
// Developer is responsible for keeping client and server in sync
```

No `runServerUpdate` here — developer owns the full update + confirm cycle.

## Timing constraints (April 21 guide)

| Object or phase | Dated rule |
| --- | --- |
| PaymentIntent awaiting payment | `requires_payment_method` and `requires_confirmation` are examples of states in which an amount may be updated. |
| After confirmation | The guide says the amount **generally** cannot be increased; it does not specify exceptions. |
| Checkout Session | Update only while active, before completion or expiry; the example checks Session `status` and `expires_at`. |

The November variant index does not verify these rules for the linked bodies.

## Use Cases

- Add/remove add-ons (gift wrap, warranty)
- Change shipping method or delivery speed
- Add additional services or charges
- Apply/remove discount codes or store credit

## Related Pages

- [[stripe]] — Stripe company route.
- [[source-stripe-checkout-dynamic-line-items]] — companion feature (line item updates via runServerUpdate)
- [[source-stripe-checkout-dynamic-discounts]] — companion feature (discount updates)
- [[stripe-checkout]] — Checkout concept page
- [[stripe-payment-intents]] — Payment Intents concept page

## Raw Sources

- [[raw/stripe-checkout-dynamic-amounts-2025|2026-04-21 full dynamic amounts guide]] — dated Checkout Sessions embedded-components and Payment Intents Elements variants; server/client examples and timing qualifications

## Related raw API references

- [[raw/stripe-payments-advanced-dynamically-update-amounts-2026-11-07|2026-11-07 dynamic-amounts variant index]] — navigation-only capture linking Checkout Sessions API (`payment-ui=embedded-components`) and Payment Intents API (`payment-ui=elements`); no linked variant behavior inferred.
