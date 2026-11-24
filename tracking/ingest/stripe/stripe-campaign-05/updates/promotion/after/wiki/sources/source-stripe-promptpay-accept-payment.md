---
title: "Stripe: Accept a PromptPay Payment"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/payments/promptpay/accept-a-payment
raw_files:
  - "stripe-promptpay-accept-payment-2025.md"
tags: [stripe, real-time-payments, promptpay, thailand, thb, checkout, direct-api, qr-code]
---

## Summary

The May 6, 2026 [[stripe|Stripe]] acceptance guide contains Checkout and Direct API instructions for PromptPay, a Thai QR-based payment method. The November 7 capture links those same two variants. The May Direct API guide refers readers with an existing Elements implementation to Payment Element migration. See the separate method overviews for Elements and Mobile Payment Element product support.

## Checkout

The May guide covers Thailand business locations, THB presentment and payment mode with one-time line items in one currency. It excludes setup and subscription modes for these Checkout routes. Stripe can choose dynamic payment methods, or the merchant can include `promptpay` in the Checkout Session's `payment_method_types`. Its hosted example uses a `success_url`; its full embedded example uses a `return_url`. The customer scans the QR, authorizes in a participating app and returns to the merchant site. See May lines 12–103.

## Direct API

The May guide recommends Stripe's general acceptance integration unless the merchant needs manual server confirmation or a separately presented payment method. In the custom direct flow, the merchant server creates a THB PaymentIntent and passes its client secret to the browser. The May sample explicitly lists `promptpay`. The customer email is the only billing-detail field in this sample's new-method form. The browser calls `stripe.confirmPromptPayPayment(clientSecret, {payment_method: {type: 'promptpay', billing_details: {email}}})` and Stripe.js displays a QR modal. See May lines 122–165 and 230–296.

The customer scans the code and authorizes in a participating banking or payment app. The May guide says the modal closes automatically a few seconds after successful authentication. It also illustrates a user-close branch without specifying a terminal PaymentIntent state for closure. Fulfill server-side after verified payment completion, such as observing `payment_intent.succeeded` and its corresponding `succeeded` PaymentIntent. A scan, closed modal and browser return are customer steps and signals. See May lines 275–310.

The separate [[raw/stripe-js-payment-intents-confirm-promptpay-payment-2026-11-07|November Stripe.js reference]] (lines 7–33) describes calling without additional data when a PaymentMethod is already attached. The merchant can handle QR display by passing `handleActions: false`. These are Stripe.js reference details. The November acceptance capture lists the route links.

## Testing

The May Checkout sandbox uses **Generate QR code**, followed by scanning the test URL to authorize or fail on a Stripe-hosted page. In the May Direct API sandbox with Stripe-displayed QR, **Simulate scan** opens the Stripe-hosted test page. A scan of a manually displayed test QR code opens the same page. In live mode, the customer uses a supported banking or payment app. See May lines 109–115 and 312–318.

## Separate method documentation

The May and November [[source-stripe-promptpay|PromptPay method overviews]] list Elements product support, exclude Express Checkout Element, and restrict Mobile Payment Element to iOS (May overview lines 56–68, November overview lines 57–69). Subscriptions and Invoicing support only the `send_invoice` collection method. The May Checkout setup and subscription mode exclusions apply to Checkout Sessions. The November overview describes a reviewed waitlist for US-based Stripe accounts in private preview (lines 71–73).

The November overview also describes repeated QR use after payment. A rescan can deduct funds again. When Stripe receives excess funds, it returns the amount to the merchant balance and notifies the merchant, who refunds the customer outside Stripe (November overview lines 124–130).

## Related Pages

- [[stripe]] — provider overview
- [[stripe-real-time-payments#PromptPay Details|PromptPay in Stripe real-time payments]]
- [[source-stripe-promptpay]] — method eligibility and product support

## Raw Sources

- [[raw/stripe-promptpay-accept-payment-2025]] — May 6, 2026 full Checkout and Direct API guide

## Related raw API references

- [[raw/stripe-payments-promptpay-accept-a-payment-2026-11-07]] — November 7, 2026 selector for Checkout and Direct API
