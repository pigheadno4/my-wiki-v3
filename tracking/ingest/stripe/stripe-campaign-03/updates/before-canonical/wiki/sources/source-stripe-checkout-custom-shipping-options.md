---
title: "Stripe Checkout: Dynamically Customize Shipping Options"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-custom-shipping-options-2025.md"
  - "stripe-checkout-dynamic-line-items-2025.md"
tags: [stripe, checkout, shipping, dynamic-shipping, embedded, checkout-sessions, onShippingDetailsChange, dynamic-line-items]
---

## Summary

Guide for dynamically updating shipping options based on a customer's address in Checkout. Embedded page only; uses a server-side endpoint + client-side `onShippingDetailsChange` callback to validate addresses, compute rates, and update the Checkout Session.

## Key Takeaways

- **Embedded page only** — hosted page explicitly unsupported; payment mode only (not subscription)
- **`permissions.update_shipping_details: 'server_only'`** — disables Checkout's automatic client-side shipping update; only your server (via secret key) can update shipping details
- **Session setup**: `ui_mode: 'embedded_page'` + `permissions.update_shipping_details: 'server_only'` + `shipping_address_collection.allowed_countries` + a dummy `$0` shipping option as placeholder
- **Server endpoint flow**: (1) retrieve session, (2) validate address, (3) calculate options, (4) update session with `collected_information.shipping_details` + `shipping_options`
- **Client callback**: `onShippingDetailsChange` in `stripe.createEmbeddedCheckoutPage()` or `EmbeddedCheckoutProvider options`; receives `{checkoutSessionId, shippingDetails}`; must return a Promise resolving to `{type: "accept"}` or `{type: "reject", errorMessage}`

## Use Cases

- **Address validation**: confirm shippability with custom rules; optionally show custom UI for address confirmation
- **Region-based methods**: show only available methods (e.g., overnight only for domestic)
- **Dynamic rate calculation**: compute fees from customer's delivery address
- **Order-total thresholds**: free shipping for orders over $X (for quantity/cross-sell changes, see dynamically updating line items)

## Integration Pattern

```
Session create (server)
  └─ ui_mode: embedded_page
  └─ permissions.update_shipping_details: server_only
  └─ shipping_options: [{ dummy $0 rate }]
  └─ shipping_address_collection.allowed_countries: [...]

Customer enters shipping address
  └─ Checkout calls onShippingDetailsChange(event)
       └─ event: { checkoutSessionId, shippingDetails }
       └─ POST /calculate-shipping-options (server)
            └─ Retrieve session
            └─ Validate address
            └─ Calculate options
            └─ stripe.checkout.sessions.update(id, {
                 collected_information: { shipping_details },
                 shipping_options: [...]
               })
       └─ Return { type: "accept" } or { type: "reject", errorMessage }
```

## Client Setup

**Vanilla JS**: `stripe.createEmbeddedCheckoutPage({ fetchClientSecret, onShippingDetailsChange })`

**React**: `<EmbeddedCheckoutProvider stripe={stripePromise} options={{ fetchClientSecret, onShippingDetailsChange }}>`

> Always return a Promise from `onShippingDetailsChange`. Resolve with `{type: "accept"}` (Checkout renders new options) or `{type: "reject", errorMessage}` (Checkout shows error).

## Dynamic Line Items (Limitation)

Dynamic line item updates (add/remove/update items during checkout) are **not supported** in either Checkout mode as of 2026-04-20:

- **Hosted**: explicitly unsupported
- **Embedded**: in development, not yet released

For this feature, use **Elements with the Checkout Sessions API** instead. Use cases: inventory holds on quantity changes, add complimentary products past order threshold, dynamically update shipping rates or manual tax rates based on order total.

## Related Pages

- [[source-stripe-checkout-shipping]] — Static ShippingRate API (pre-created rates, fixed amounts)
- [[stripe-checkout]] — Stripe Checkout concept page

## Raw Sources

- [[stripe-checkout-custom-shipping-options-2025]] — Dynamic shipping: embedded only, permissions.update_shipping_details, onShippingDetailsChange callback, server endpoint pattern, React + vanilla JS client setup
- [[source-stripe-checkout-dynamic-line-items]] — Dynamic line items: supported in Elements path via beta `runServerUpdate` pattern; use cases: inventory, cross-sells, subscription toggle, shipping + tax rate updates
