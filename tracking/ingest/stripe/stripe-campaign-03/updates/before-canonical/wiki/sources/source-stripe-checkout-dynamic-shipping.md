---
title: "Dynamically Customize Shipping Options"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-checkout-dynamic-shipping-2025.md"
tags: [stripe, checkout-sessions, shipping, dynamic-shipping, server-side, runServerUpdate, beta, payment-intents]
---

## Summary

Beta feature for dynamically updating shipping options server-side based on the customer's address in Checkout Sessions. Enables address validation, region-specific options, and dynamic rate calculation (including order-total-based rates).

## Key Constraints

- **Payment mode only** — not available in subscription mode
- **Beta**: requires `betas: ['custom_checkout_server_updates_1']` on Stripe instance
- **React**: requires `@stripe/react-stripe-js@^5.0.0` + `@stripe/stripe-js@^8.0.0`
- **Payment Intents**: no built-in support — must manually create a new PaymentIntent with adjusted amounts

## Setup

### Session Creation

```js
stripe.checkout.sessions.create({
  ui_mode: 'elements',
  permissions: { update_shipping_details: 'server_only' }, // disables client-side updateShippingAddress
  shipping_address_collection: { allowed_countries: ['US'] },
  mode: 'payment',
  // ...
});
```

`server_only` disables the client-side `updateShippingAddress` method and enables server-side updates.

### Client Beta Flag

```js
// HTML+JS
const stripe = Stripe('PK', { betas: ['custom_checkout_server_updates_1'] });

// React
const stripe = loadStripe('PK', { betas: ['custom_checkout_server_updates_1'] });
```

## Server Endpoint Pattern

```
POST /calculate-shipping-options
Body: { checkout_session_id, shipping_details }

1. Retrieve session: stripe.checkout.sessions.retrieve(id)
2. Validate shipping_details (custom business logic)
3. Calculate shipping_options (custom business logic)
4. Update session:
   stripe.checkout.sessions.update(id, {
     collected_information: { shipping_details },
     shipping_options: [...],
   })

Response: { type: 'object', value: { succeeded: true } }
       or: { type: 'error', message: '...' }
```

## Client `runServerUpdate` Pattern

```js
// HTML+JS
await checkout.runServerUpdate(() => updateShippingOptions(addressValue));

// React
const { runServerUpdate } = checkoutState.checkout;
await runServerUpdate(() => updateShippingOptions(aeValue.value));
```

`runServerUpdate` wraps the server call and updates the local session object (`session.shippingOptions`, `session.shippingAddress`) on success.

## Use Cases

| Use case | Description |
| --- | --- |
| Address validation | Block shipping to unsupported addresses; show custom error |
| Region-based options | Show overnight only for domestic, exclude international options |
| Dynamic rate calculation | Calculate fee based on address (distance, zone, weight) |
| Order-total-based rates | Free shipping over $100; read `session.lineItems` on server |

## Related Pages

- [[source-stripe-charge-shipping]] — basic static shipping rates
- [[stripe-checkout]] — Checkout concept page

## Raw Sources

- [[stripe-checkout-dynamic-shipping-2025]] — verbatim dynamic shipping guide
