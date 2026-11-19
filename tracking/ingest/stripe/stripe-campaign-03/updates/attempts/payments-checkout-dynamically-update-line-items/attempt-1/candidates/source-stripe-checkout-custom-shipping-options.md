---
title: "Stripe Checkout: Dynamically Customize Shipping Options"
type: source
date_ingested: 2026-04-20
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/checkout/custom-shipping-options"
raw_files:
  - "stripe-checkout-custom-shipping-options-2025.md"
  - "stripe-checkout-dynamic-line-items-2025.md"
tags: [stripe, checkout, shipping, dynamic-shipping, embedded, checkout-sessions, onShippingDetailsChange, dynamic-line-items]
---

## Summary

The separate 2026-04-20 shipping guide describes updating shipping options from a customer's address in an Embedded Checkout page using a server endpoint and client `onShippingDetailsChange` callback. Its payment-mode shipping flow is distinct from the 2026-04-21 Elements Checkout Sessions line-item update example. The 2026-11-07 capture at the line-items URL is a Full page/Embedded form variant index only; it does not establish current support or a replacement shipping flow.

## Key Takeaways

- **Dated UI and mode scope**: The April shipping guide says hosted Checkout does not support dynamically customizing shipping options, directs this use case to Embedded page or Checkout Elements, and limits its embedded shipping example to payment mode (shipping raw lines 8-29). These are April claims, not current support verification.
- **Session setup**: Use `ui_mode: "embedded_page"`, `permissions.update_shipping_details: "server_only"`, `shipping_address_collection.allowed_countries`, and an initial zero-amount shipping option. The server-only permission prevents automatic client-side shipping-detail updates (shipping raw lines 32-79).
- **Server endpoint**: Retrieve the Checkout Session by ID, validate the submitted address, calculate shipping options, and update `collected_information.shipping_details` plus `shipping_options` with the secret key (shipping raw lines 81-149).
- **Client callback**: The dated vanilla JS `stripe.createEmbeddedCheckoutPage()` and React `EmbeddedCheckoutProvider` examples pass `onShippingDetailsChange`, which receives the Session ID and shipping details. Return a Promise resolving to `{type: "accept"}` for rendered options or `{type: "reject", errorMessage}` for an error (shipping raw lines 177-223, 244-307). Callback acceptance is a shipping UI result, not payment success.

## Use Cases

- Validate a shipping address and let the customer choose a preferred address.
- Show region-specific methods and calculate rates from the entered address.
- Offer an order-total threshold such as free shipping. The April shipping guide points to the separate dynamic line-items guide for quantity or cross-sell changes (shipping raw lines 20-25).

## Integration Pattern

```
Server creates an embedded-page, payment-mode Checkout Session
  -> Customer enters shipping address
  -> onShippingDetailsChange sends checkoutSessionId and shippingDetails to server
  -> Server retrieves Session, validates address, calculates options
  -> Server updates collected_information.shipping_details and shipping_options
  -> Client callback resolves accept or reject for the shipping UI
```

The April server and client examples are illustrative; validate the caller and target Session before a server-side update. A successful UI callback alone does not establish order completion.

## Dynamic Line Items: Dated UI Scope

As of this source's 2026-04-20 snapshot, the shipping summary recorded dynamic line-item updates as unsupported in hosted Checkout and still developing for embedded Checkout. The separate 2026-04-21 line-items capture demonstrates `ui_mode: "elements"` with a server `sessions.update` and client `runServerUpdate` in a subscription example (line-items raw lines 47-63, 65-149, 170-287). That Elements path is not the `embedded_page` shipping callback above. The November 2026 line-items index labels Full page and Embedded form variants but contains no variant body or support matrix (new raw lines 9-14). Do not infer that the April UI limitation persists, was reversed, or that “Embedded form” equals April `ui_mode: "elements"`.

## Related Pages

- [[source-stripe-checkout-shipping]] — Static ShippingRate API
- [[source-stripe-checkout-dynamic-line-items]] — April Elements line-item update example and November variant navigation
- [[stripe-checkout]] — Checkout concept and dated UI qualifications
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-checkout-custom-shipping-options-2025|Dynamic shipping guide, captured 2026-04-20]] — Embedded page shipping callback and server update
- [[raw/stripe-checkout-dynamic-line-items-2025|Dynamic line-items guide, captured 2026-04-21]] — separate Elements Checkout Session example used for the dated comparison

## Related raw API references

- [[raw/stripe-payments-checkout-dynamically-update-line-items-2026-11-07|Dynamic line-items variant index, captured 2026-11-07]] — navigation only; Full page and Embedded form links
