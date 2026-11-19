---
title: "Stripe: Accept a Klarna Payment"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/klarna/accept-a-payment"
raw_files:
  - "stripe-klarna-accept-payment-2025.md"
tags: [stripe, bnpl, klarna, buy-now-pay-later, checkout, payment-intents, elements, ios, android, react-native, testing]
---

## Overview

May 6, 2026 Klarna acceptance guide for [[stripe]], with Checkout, Elements, Direct API, iOS, Android, and React Native variants. The November 7 capture of the same unparameterized URL is a variant index only. It links to those six paths but supplies no replacement instructions or evidence that the older behavior remains current. See [[stripe-klarna]] and [[stripe-bnpl]].

## Key takeaways from the May 2026 capture

- Before integration, the guide says to check Klarna eligibility in the account's Payment methods settings. It recommends Stripe Checkout if there is no existing Stripe integration. This is dated guidance, not a current account-eligibility determination.
- Checkout's hosted and embedded examples create Checkout Sessions in `mode: "payment"`; its Elements variant also creates a Checkout Session with `ui_mode: "elements"`. If manually listing methods, the examples include `klarna` in `payment_method_types`; the guide recommends dynamic payment methods. The Direct API and mobile variants instead create server-side PaymentIntents and hand a client secret to the client.
- The Direct API path recommends `shipping`, `amount_details.line_items`, and `payment_method_data.billing_details` to help acceptance and reduce disputes. Its deferred-payment prefill example passes billing details and `payment_method_data.klarna.dob` when creating and confirming a PaymentIntent. The prior summary's `payment_method_options.klarna` prefill attribution was incorrect for this example; the field paths are path-specific, not a universal instruction for Checkout or Elements.
- Optional separate authorization and capture uses PaymentIntent `capture_method: "manual"`. After authorization the PaymentIntent moves to `requires_capture`; a capture request is still needed. The May guide gives a 28-day capture deadline, after which authorization automatically cancels and cannot be captured. It advises cancelling unfulfillable authorizations promptly because they count against the customer's Klarna purchasing power.
- In the manual Direct API redirect example, confirmation first returns `requires_action` with `next_action.redirect_to_url`; returning with `payment_intent` and `payment_intent_client_secret` parameters is a route to query status, not evidence of success. The guide recommends webhook verification and says `payment_intent.succeeded` is sent when payment completes. After a Klarna decline, or 48 hours of inaction following redirect, the PaymentMethod detaches and the PaymentIntent moves to `requires_payment_method`. Before API version `2023-08-16`, the guide says Klarna failures reported as `payment_intent_authentication_failure` rather than its listed detailed codes.
- The iOS, Android, and React Native variants describe webview authentication followed by their respective client confirmation handlers. The May examples mention iOS 13+, Android SDK `23.7.0`, and a `dahlia` Stripe.js script in Direct API; none is revalidated by the November index. A client handler or a returned page should not be used alone as an authoritative payment-completion signal.
- The May capture includes approved and denied sandbox data for 23 customer countries, cookie-session advice, six-digit two-step test codes (`999999` fails), and repayment test values. Separately, its production-testing tip says amount `3500` in local currency can exercise options except Financing. These are dated test instructions, not a current live-country or payment-success guarantee.

## Detail locators

- May guide eligibility, Checkout recommendation, hosted/embedded Sessions: [[raw/stripe-klarna-accept-payment-2025|May 2026 guide]], lines 8-73.
- Elements Checkout Session: same raw, lines 436-466. iOS PaymentIntent/client secret/webview handler: lines 830-989. Android SDK sample and handler: lines 1500-1657. React Native PaymentIntent/client secret/handler: lines 2167-2317.
- Direct API PaymentIntent, billing and shipping recommendations, Stripe.js confirmation and return status query: same raw, lines 2827-3014. Capture, redirect states, post-payment webhooks, and prefill: lines 3422-3645.
- Per-country test tables, authentication and repayment values: same raw, lines 75-434, repeated in later variants; production-testing amount: lines 414-418 and 3400-3404.

## Related raw API references

- [[raw/stripe-payments-klarna-accept-a-payment-2026-11-07|November 7, 2026 variant index]] — navigation only for Checkout, Elements, Direct API, iOS, Android, and React Native; variant contents were not captured here.

## Raw Sources

- [[raw/stripe-klarna-accept-payment-2025|May 6, 2026 Klarna acceptance guide]] — detailed factual capture (the filename ends in 2025, but its fetched header is 2026-05-06).
