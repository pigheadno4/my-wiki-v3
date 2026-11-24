---
title: "Stripe: Accept a Payment with Wero"
type: source
date_ingested: 2026-05-05
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/wero/accept-a-payment"
raw_files:
  - "stripe-wero-accept-payment-2025.md"
tags: [stripe, wero, eur, bank-redirect, checkout, elements, payment-intents]
---

## Summary

The 2026-05-05 [[stripe]] integration guide covers Checkout, the web Payment Element with Payment Intents, and Direct API including manual server-side confirmation and redirect. Customers approve a payment in their bank-account-linked Wero wallet. The 2026-11-07 capture is a selector for six routes covering Checkout, Elements with either Checkout Sessions or Payment Intents, Direct API, iOS and Android. The details below come from the May integration guide.

The separate [[source-stripe-wero|Wero payment method profile]] lists Germany for customers in its 2026-05-05 capture and Belgium, France, Germany, Luxembourg and the Netherlands in its 2026-11-07 capture. Both dated profiles list EUR. The November *integration* selector gives navigation. The customer-location list comes from the profile and does not establish an individual account's enrollment.

## May implementation paths

- **Checkout.** Start from an existing Checkout integration and activate Wero in Dashboard payment method settings. Use EUR for every line item and payment mode. The guide describes dynamic method selection and manually adding `wero` to the Checkout Session's `payment_method_types`. The hosted example uses `success_url`, while the `embedded_page` example uses `return_url`. The May guide directs fulfillment to `checkout.session.completed` (lines 8–98).
- **Elements.** The merchant creates the EUR PaymentIntent on the server. The client confirms with `stripe.confirmPayment`, the Payment Element and a `return_url`. The general return table lists `payment_intent` and `payment_intent_client_secret`. The Wero-specific redirect paragraph additionally names `redirect_pm_type` and `redirect_status` (lines 121–167, 386–492 and 599–605).
- **Direct API client.** The merchant creates an EUR PaymentIntent. Stripe.js `confirmWeroPayment` uses the PaymentIntent client secret, customer billing details in the example and a `return_url`. Its return table lists `payment_intent`, `payment_intent_client_secret` and `redirect_status` (lines 650–671 and 740–792).
- **Direct API manual server path.** Set the return URL, create a Wero PaymentMethod with billing details, and confirm the PaymentIntent. When it is in `requires_action` with `next_action.type = redirect_to_url`, redirect the buyer to the corresponding URL. This passage names `payment_intent` and `payment_intent_client_secret` on return (lines 794–850).

The return fields above reflect the dated passages for each path. Retrieve and inspect the PaymentIntent state. Neither browser return nor `redirect_status` proves payment success. For PaymentIntent routes, the guide uses `payment_intent.succeeded` for post-payment business actions (lines 482–492, 607–611, 786–792 and 851–855).

## Authentication, retry and API version

- **Timing and recovery.** May describes typical completion under ten seconds and separately gives an hour for the authentication session to expire. Failed or expired PaymentIntents transition to `requires_payment_method`. Customers should retry with another method. Card is an example of an additional payment option. In the Direct API sandbox, approval maps `requires_action` to `succeeded` and decline maps it back to `requires_payment_method` (lines 14, 599–605 and 877–887).
- **Errors.** See the May table for `payment_intent_invalid_currency`, `payment_method_customer_decline`, `payment_intent_payment_attempt_failed` and `payment_intent_redirect_confirmation_without_return_url` (lines 889–898).
- **Historical manual method lists.** The May PaymentIntent examples write `payment_method_types`. The separate `2026-08-26.preview` changelog removes it from PaymentIntent create, update and confirm requests, with HTTP 400 `payment_method_types_no_longer_supported` if sent. The response property remains read-only. The May Checkout Session parameter belongs to a different resource.

## Related Pages

- [[stripe-wero]] — standalone Wero concept
- [[source-stripe-wero]] — separately dated Wero payment method profiles

## Raw Sources

- [[raw/stripe-wero-accept-payment-2025|Wero acceptance guide, captured 2026-05-05]] — full 898-line capture for Checkout, Elements and Direct API.
- [[raw/stripe-changelog-dahlia-2026-08-26-removes-payment-method-types-parameter-from-payment-intents-setup-intents-2026-11-07|Dahlia preview changelog, captured 2026-11-07]] — versioned Intent method-list change at lines 7–34.

## Related raw API references

- [[raw/stripe-payments-wero-accept-a-payment-2026-11-07|Wero acceptance variant selector, captured 2026-11-07]] — navigation for Checkout, both Elements API options, Direct API, iOS and Android.
