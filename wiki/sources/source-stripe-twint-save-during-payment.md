---
title: "Stripe: Save Payment Details During a TWINT Payment"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/twint/save-during-payment"
raw_files:
  - "stripe-twint-save-during-payment-2025.md"
tags: [stripe, twint, switzerland, chf, recurring, setup-intents, save-payment-method]
---

## Summary

The full 2026-05-03 guide describes taking an initial CHF payment, having the customer authorize future use of TWINT, and saving the resulting TWINT PaymentMethod for later off-session payments. Before reuse, associate the method with the same customer identity. The examples distinguish an Accounts v2 customer-configured Account (`customer_account`) from a Customers v1 Customer (`customer`). The May guide describes Accounts v2 as generally available to Connect users and in public preview for other Stripe users, who must specify a preview version when participating.

## Initial payment and authorization

- **Hosted Checkout.** Create a server-side payment-mode Checkout Session with CHF line items, TWINT, the customer identity and `payment_intent_data.setup_future_usage=off_session`. The customer authorizes future use through Checkout. Retrieve the Session’s PaymentIntent and `payment_method` via the `checkout.session.completed` event or retrieve the Session with the ID in the `success_url`. The redirect supplies a lookup path. It can be visited directly or missed when the customer closes the browser.
- **Elements.** Set `setup_future_usage=off_session` on the server-created PaymentIntent and use its client secret. The May web examples use `stripe.confirmPayment()` with `return_url`.
- **Direct API.** The May guide illustrates `payment_method_data.type=twint` and `setup_future_usage=off_session`. The client route uses `stripe.confirmTwintPayment()` with the PaymentIntent secret and `return_url`. The optional server-confirmed route supplies `mandate_data`, with IP address and user agent in the example’s online acceptance data, plus `return_url`. When the Intent is `requires_action`, send the customer to `next_action.redirect_to_url.url` to authorize with TWINT.

Verify mandate authorization from Stripe state or verified events. The May guide instructs merchants to save the resulting `payment_method` ID after `payment_intent.succeeded` and describes `payment_intent.payment_failed` with the Intent returning to `requires_payment_method` when authorization fails.

## Later off-session charging

List the customer’s attached `twint` methods and create and confirm a new CHF PaymentIntent with the matching customer and saved method IDs, `off_session=true` and `confirm=true`. The May guide makes `return_url` optional specifically for a TWINT method already set up by a SetupIntent or a PaymentIntent with `setup_future_usage`.

## Detail locators

- May raw lines 8–324 cover hosted Checkout, lookup, mandate events and reuse. Lines 331–864 cover Elements. Lines 866–1222 cover Direct API, including both confirmation paths.
- May sandbox examples describe authorization changing `requires_action` to `succeeded` or `requires_payment_method`. The May Direct API test fixtures at lines 1209–1222 simulate generic decline and mandate revocation. They use the spelling `payment_intent.failed`, while the guide’s general authorization monitor at lines 1129–1135 names `payment_intent.payment_failed`. The fixture spelling leaves the event contract unverified.

## Related Pages

- [[stripe]] — Stripe company page
- [[stripe-twint#Integration|TWINT integration]]
- [[source-stripe-twint-set-up-future-payments]] — setup without an initial payment
- [[source-stripe-twint-accept-payment]] — TWINT payment acceptance

## Raw Sources

- [[raw/stripe-twint-save-during-payment-2025|2026-05-03 full TWINT save-during-payment guide]] — Checkout, Elements and Direct API implementations

## Related raw API references

- [[raw/stripe-payments-twint-save-during-payment-2026-11-07|2026-11-07 TWINT save-during-payment variant index]] — Checkout, Elements and Direct API
