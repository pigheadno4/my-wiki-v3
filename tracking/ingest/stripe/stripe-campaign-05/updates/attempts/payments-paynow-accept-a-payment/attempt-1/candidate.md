---
title: "Stripe: Accept a PayNow Payment"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/paynow/accept-a-payment"
raw_files:
  - "stripe-paynow-accept-payment-2025.md"
tags: [stripe, real-time-payments, paynow, singapore, sgd, qr-code, checkout, direct-api]
---

## Overview

The May 6, 2026 acceptance guide covers online single-use PayNow payments through Checkout and Direct API. The November 7, 2026 capture indexes those two variants. For separate product coverage, the May and November [[source-stripe-paynow|PayNow overviews]] describe Elements support with Express Checkout Element excluded. The November overview specifically lists Payment Element. For in-person acceptance, see the separate [[source-stripe-terminal-additional-payment-methods|Terminal guide]].

## May 2026 Checkout

The May guide documents Singapore businesses, SGD across all line-item prices, and one-time line items in payment mode. The captured PayNow Checkout path excludes setup and subscription modes. The method overview separately describes subscriptions and invoices with `send_invoice`.

Stripe can select payment methods dynamically. In the May manual examples, add `paynow` to the Checkout Session's payment method list. Both examples show it alongside `card`. The Stripe-hosted example sets `success_url`. The full embedded example sets `ui_mode: embedded_page` and `return_url`.

The customer scans the Checkout QR code and completes payment before Checkout redirects to the merchant site. For testing, select PayNow and use **Generate QR code**. Scanning opens a Stripe-hosted page where the tester can authorize or fail the payment. In live mode, customers use a participating banking or payment app. Follow the Checkout fulfillment guidance for order completion.

## May 2026 Direct API

The merchant needs a Stripe account and creates an SGD PaymentIntent on its server. The May guide tells existing Payment Intents integrations to add `paynow` to their method list. Its create example also sets `payment_method_data.type` to `paynow`. These are fields in the dated example. The server passes the PaymentIntent client secret to the customer’s browser through a single-page app endpoint or server rendering.

In the captured flow, Stripe.js `confirmPayNowPayment(clientSecret)` displays the QR code inline. The customer scans and authenticates in an app from a participating bank or non-bank financial institution. Keep the page open while awaiting the payment outcome. The browser sample checks for `succeeded` and includes an alternate branch with a modal-closure comment. A QR scan and modal closure each leave the formal PaymentIntent outcome undetermined.

For fulfillment, verify success on the server. When the customer completes payment, the guide says the PaymentIntent becomes `succeeded` and Stripe emits `payment_intent.succeeded`. The Direct API sandbox QR leads to Stripe’s authorize-or-fail test page. In the live flow, customers scan with their participating app.

## Related

- [[stripe-real-time-payments]] — Stripe real-time methods and PayNow integration scope
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-paynow-accept-payment-2025|May 6, 2026 PayNow acceptance guide]] — full Checkout and Direct API capture.

## Related raw API references

- [[raw/stripe-payments-paynow-accept-a-payment-2026-11-07|November 7, 2026 PayNow acceptance variant index]] — navigation to Checkout and Direct API.
