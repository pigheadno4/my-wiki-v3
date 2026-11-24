---
title: "Stripe Terminal: Display Cart Details"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/features/display"
raw_files:
  - "stripe-terminal-display-cart-2025.md"
tags: [stripe, stripe-terminal, reader-display, cart, pre-dip, checkout]
---

## Summary

The 2026-05-01 [[stripe]] [[stripe-terminal|Terminal]] guide describes displaying cart line items and totals on the Verifone P400, BBPOS WisePOS E, and Stripe Reader S700/S710. The 2026-11-07 capture gives the cart-display purpose and an index for the Server-driven, JavaScript, iOS, Android, and React Native variants. The behavior below comes from the May guide.

## Set the Reader Display

The integration sets the display before processing the payment, supplying the cart's line items, currency, tax, and total in the form expected by its integration. The application calculates tax and total, optionally using Stripe Tax. The displayed amount must match the independently charged amount. Setting the display does not control what the customer is charged.

May shows setting the display from server-driven, JavaScript, iOS, Android, and React Native integrations. It also links a Java `setReaderDisplay` reference. The November index gives no standalone Java variant and establishes no change in Java support.

The May guide distinguishes the display reset by integration.

- **Server-driven** — `cancel_action` endpoint.
- **JavaScript, iOS, and Android** — `clearReaderDisplay` returns the display to the splash screen. The Android paragraph names the method, although its link points to `create-payment-intent`. The separate November [[source-stripe-terminal-js-sdk-reference|JavaScript SDK reference]] also describes `clearReaderDisplay`.

The May React Native variant shows `setReaderDisplay`. Its reset behavior remains unresolved in these captures.

## Pre-Dip (US only)

The May guide describes pre-dip, pre-tap, or pre-swipe for US payments on the Verifone P400, BBPOS WisePOS E, and Stripe Reader S700/S710.

- Calling `setReaderDisplay` prepares the reader. The customer can present a payment method before the amount is finalized, and the reader retains it for later use. Updating the cart display does not invalidate the pre-dip.
- Stripe provides no update or event to the integration when the customer pre-dips. The merchant can complete the transaction through the ordinary `PaymentIntent` flow.
- Where pre-dip is unavailable, the cart screen shows subtotal and line items without the early card presentation step. Ordinary payment processing is a separate flow.

## Raw Sources

- [[raw/stripe-terminal-display-cart-2025|2026-05-01 display-cart guide]] — five variant bodies

## Related raw API references

- [[raw/stripe-terminal-features-display-2026-11-07|2026-11-07 display-cart platform variant index]]
