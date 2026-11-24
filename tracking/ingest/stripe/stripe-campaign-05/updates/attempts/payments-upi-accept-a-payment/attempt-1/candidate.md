---
title: "Stripe: Accept a UPI Payment"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/upi/accept-a-payment"
raw_files:
  - "stripe-upi-accept-payment-2025.md"
tags: [stripe, real-time-payments, upi, india, inr, checkout, elements, recurring, e-mandate]
---

## Summary

The May 6, 2026 acceptance guide covers three surfaces for UPI in India: Checkout, Elements with the Checkout Sessions API and Elements with the Payment Intents API. The customer authenticates on their mobile device and approves the payment or future charges. The May Checkout and Payment Intents Elements sections describe immediate success or failure notification for one-off payments and cases where the method is saved for future use, and delayed notification for off-session or recurring payments when the customer is absent.

## May integration paths

- **Checkout.** The guide lists US, EU, CA, GB, AU, SG and CH business locations and requires INR for all line items. It describes payment, setup and subscription modes and recurring UPI AutoPay e-mandates. Dynamic configuration is available. For manual configuration, add `upi` to `payment_method_types`. The hosted example uses `success_url`, and the embedded-page example uses `return_url`. The Checkout section says a QR code expires five minutes after creation, at which point Stripe emits `payment_intent.payment_failed` and the expired code cannot complete the payment.
- **Elements with Checkout Sessions API.** The merchant's server creates the Session and returns its client secret. All line items use INR. The guide describes dynamic Dashboard management and manual method listing. The May HTML/JS example initializes `initCheckoutElementsSdk` and the React example uses `CheckoutElementsProvider`. The client confirms via the Checkout instance or its actions. This section describes a 24-hour Checkout Session lifetime, separate from the five-minute UPI QR window.
- **Elements with Payment Intents API.** The server sets the amount and currency on a PaymentIntent and provides its client secret to Elements. The client uses `stripe.confirmPayment` with `return_url`. On return, retrieve the PaymentIntent and inspect its status. The status-display examples handle `succeeded`, `processing` and `requires_payment_method`; the redirect itself does not determine the outcome.

The May Checkout and Checkout Sessions Elements tests use a QR code that opens a Stripe-hosted test page with authorize or expire choices. The May Payment Intents Elements branch ends at the instruction to use test API keys. A separate May guide documents Direct API setup and charge-and-save flows under [[source-stripe-upi-set-up-future-payments]].

## Detail locators

| Topic | May raw lines |
| --- | --- |
| Checkout configuration, modes, QR expiry and test | 8–115 |
| Checkout Sessions create, client SDK and test | 116–581 |
| Server PaymentIntent, client confirmation and status display | 582–1081 |

## Related

- [[stripe-real-time-payments]] — UPI integration context
- [[source-stripe-upi]] — UPI product overview
- [[source-stripe-upi-set-up-future-payments]] — Separate UPI future payments guide, including its Direct API branch
- [[source-stripe-upi-autopay]] — Separate recurring e-mandate guide
- [[stripe]] — Stripe company page

## Related raw API references

- [[raw/stripe-payments-upi-accept-a-payment-2026-11-07|November 7, 2026 variant selector]] — Navigation for Checkout and both Elements APIs.

## Raw Sources

- [[raw/stripe-upi-accept-payment-2025|May 6, 2026 acceptance capture]] — 1,081 lines across Checkout, Checkout Sessions Elements and Payment Intents Elements.
