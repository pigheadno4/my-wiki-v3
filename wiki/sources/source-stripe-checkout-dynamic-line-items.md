---
title: "Dynamically Update Line Items"
type: source
date_ingested: 2026-04-21
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/checkout/dynamically-update-line-items"
raw_files:
  - "stripe-checkout-dynamic-line-items-2025.md"
tags: [stripe, checkout-sessions, line-items, dynamic-updates, runServerUpdate, beta, subscription, payment-intents]
---

## Summary

The 2026-04-21 full guide demonstrates a subscription interval toggle in Checkout Sessions with `ui_mode: "elements"`: the client requests a server update, the server changes the Session's line items, and `runServerUpdate` refreshes the client Session. The 2026-11-07 capture at this URL is only an index for Full page and Embedded form variants. It does not confirm their implementation steps, UI support, mode scope, or current version requirements.

## Dated scope and prerequisites

- The existing source labels this feature beta, but the pinned April guide does not establish a beta gate. That guide says to use `2025-03-31.basil` or later as an SDK version; its Node sample sets `apiVersion: "2025-03-31.basil"`. The capture does not identify a server SDK package version by that string. Check the relevant API and SDK compatibility before implementation (old raw lines 23-45).
- The concrete April Session uses `ui_mode: "elements"`, `mode: "subscription"`, a Price and quantity in `line_items`, and a `return_url` (old raw lines 47-63). This example demonstrates subscription mode; neither it nor the November variant labels proves payment-mode support.
- The separate April 20 shipping source describes an `embedded_page` shipping callback and records a dated hosted/embedded line-item limitation. Its UI and `onShippingDetailsChange` callback are distinct from this Elements `runServerUpdate` example. The November “Embedded form” label alone does not resolve that scope (old raw lines 47-63; new raw lines 9-14).
- For the Payment Intents API, the April guide says to track line-item updates manually and either modify an existing PaymentIntent amount or create a new PaymentIntent with adjusted amounts (old raw lines 19-21). A new Intent is not mandatory in the cited wording.

## Server update and trust boundary

The April guide recommends action-specific endpoints, such as changing a subscription interval. It warns that client data can be modified; pass a Session ID and retrieve authoritative Session state from Stripe instead of trusting client-passed Session data (old raw lines 65-75). Validate the caller's authority over the target Session.

The illustrative endpoint checks for a nonempty client-supplied `checkout_session_id` and a `monthly` or `yearly` interval, selects a trusted server-side Price ID, and calls `stripe.checkout.sessions.update(checkout_session_id, { line_items })`. It handles Stripe invalid-request and unexpected errors (old raw lines 93-140). The sample does **not** show the recommended Session retrieval or an ownership/authorization check before updating the named Session. Its `{type: "success"}` response therefore proves neither target authorization nor a completed payment or subscription.

## Complete line-item array rule

The April update operation requires retransmitting the entire `line_items` array. Keep an item by its ID; update it by ID plus changed fields; add with `price` and `quantity` but no ID; remove by omitting its ID; reorder by putting its ID at the desired position (old raw lines 143-149).

## Client `runServerUpdate` pattern

The dated HTML/JS example sends `actions.getSession().id` and the selected interval to its endpoint inside `checkout.runServerUpdate`; React uses `checkoutState.checkout.runServerUpdate` and the checkout ID (old raw lines 170-174, 184-223, 226-287). The method gives the update function 20 seconds; catch rejected promises/timeouts and handle non-OK responses. The samples change the local toggle only after an OK response. A successful response refreshes the client Session object with new line items; it is not payment or subscription completion (old raw lines 174-176, 205-223, 228-230, 260-274).

## Dated use cases

The April guide illustrates a monthly/yearly subscription price toggle and lists inventory checks on quantity changes, complimentary products at an order threshold, shipping-rate recalculation combined with separate shipping guidance, and tax-rate updates when Stripe Tax is not used (old raw lines 10-17). These examples do not establish November Full page or Embedded form support.

## Related Pages

- [[source-stripe-checkout-custom-shipping-options]] — separate April Embedded Checkout shipping callback and dated line-item limitation
- [[source-stripe-checkout-dynamic-shipping]] — related dynamic shipping pattern with its own UI scope
- [[stripe-checkout]] — Checkout concept and dated UI boundaries
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-checkout-dynamic-line-items-2025|Dynamic line-items full guide, captured 2026-04-21]] — dated Elements subscription example, server update, and client refresh

## Related raw API references

- [[raw/stripe-payments-checkout-dynamically-update-line-items-2026-11-07|Dynamic line-items variant index, captured 2026-11-07]] — navigation only; Full page and Embedded form links
