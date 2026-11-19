---
title: "Dynamically Customize Shipping Options"
type: source
date_ingested: 2026-04-21
date_updated: 2026-11-15
canonical_url: https://docs.stripe.com/payments/checkout/custom-shipping-options
original_format: webpage
raw_files:
  - "stripe-checkout-dynamic-shipping-2025.md"
tags: [stripe, checkout-sessions, shipping, dynamic-shipping, server-side, runServerUpdate, beta, payment-intents]
---

## Summary

The April 21, 2026 full guide documents a beta Checkout Sessions `ui_mode: 'elements'` path for address-based server updates to shipping details and options. Its merchant-owned validation and calculation can produce region-specific or order-total-based rates. The November 7 capture at this canonical URL is a 14-line variant index linking Full page and Embedded form; it provides no current implementation contract for either linked body.

## Key Constraints

- **April 21 Elements example: payment mode only** — its guide says this dynamic shipping path is unavailable in subscription mode; November's linked variant bodies are uncaptured.
- **April 21 beta example**: initializes Stripe.js with `betas: ['custom_checkout_server_updates_1']`; the November index does not establish whether either linked variant needs that header.
- **April 21 React sample**: suggests `@stripe/react-stripe-js@^5.0.0` and `@stripe/stripe-js@^8.0.0`; these are dated sample versions, not a verified November requirement.
- **Payment Intents alternative in the April guide**: manually update shipping options and modify the existing PaymentIntent amount after selection, or create a new PaymentIntent with adjusted amounts. The guide does not provide a Checkout Session shipping update for that API path.

## April 21 Elements setup

The following Session and client examples are dated to the full April capture. The server owns shipping validation, rate calculation, and the Session update; the client submits completed address details and refreshes local Session state after a successful server update. That update does not complete an order or prove payment success.

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

`runServerUpdate` wraps the server call and refreshes the local Session shipping state after a successful server update. The April Ruby endpoint leaves validation and calculation as `NotImplementedError` placeholders. Its React example checks `response.type` without parsing the response and returns an undefined `result`; the vanilla JS example interpolates address fields into `innerHTML`. Repair and review the sample before implementation rather than copying those fragments as verified production code.

## Use Cases

| Use case | Description |
| --- | --- |
| Address validation | Block shipping to unsupported addresses; show custom error |
| Region-based options | Show overnight only for domestic, exclude international options |
| Dynamic rate calculation | Calculate fee based on address (distance, zone, weight) |
| Order-total-based rates | Free shipping over $100; read `session.lineItems` on server |

## Related Pages

- [[stripe]] — Stripe company route.
- [[source-stripe-checkout-custom-shipping-options]] — separate April 20, 2026 Embedded Checkout `onShippingDetailsChange` path; that callback is deprecated in Stripe.js 9.14.0 and is distinct from this April 21 Elements `runServerUpdate` example.
- [[source-stripe-charge-shipping]] — basic static shipping rates
- [[stripe-checkout]] — Checkout concept page

## Raw Sources

- [[raw/stripe-checkout-dynamic-shipping-2025|2026-04-21 full dynamic shipping guide]] — dated Elements beta, payment-mode, server_only and runServerUpdate example

## Related raw API references

- [[raw/stripe-payments-checkout-custom-shipping-options-2026-11-07|2026-11-07 shipping-options variant index]] — navigation-only capture linking Full page (`ui=full-page`) and Embedded form (`ui=checkout-form`); no linked body was captured and neither path's API behavior is inferred.
