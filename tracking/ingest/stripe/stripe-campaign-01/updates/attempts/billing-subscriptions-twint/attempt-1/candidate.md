---
title: "Stripe Subscriptions — Set Up TWINT Subscription"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/twint"
raw_files:
  - "stripe-subscriptions-twint-2026.md"
tags: [stripe, billing, subscriptions, twint, checkout, setup-intents, mandate, qr-code]
---

## Summary

The May 13, 2026 guide describes three TWINT subscription examples: Stripe-hosted Checkout, Setup Intents API, and Subscriptions API. The November 7 capture of the same canonical URL contains only an index linking those three variants. It establishes their navigation targets, not a current change in TWINT requirements, eligibility, currency, QR presentation, or payment outcomes. This page preserves the May flows as dated examples; the linked variant bodies were not captured in November.

## May 2026 example: Stripe-hosted Checkout

The Checkout example creates a server-side Session with `mode=subscription`, `payment_method_types=["card","twint"]`, a recurring price, and a success URL, then redirects the customer to the Session URL (May raw lines 34–70). It says the customer authorizes future use of their TWINT account. In the guide's test-mode instructions, accepting the redirect-page mandate moves a **SetupIntent** from `requires_action` to `succeeded`; declining moves it to `requires_payment_method` (May raw lines 73–75). Neither transition alone proves a paid first invoice or an active subscription.

The Checkout Session example does not show `mandate_data` or `return_url` fields. Do not infer from the direct API examples that they are universal Checkout request requirements.

## May 2026 example: Setup Intents API

The server-side SetupIntent example uses `confirm=true`, `usage=off_session`, TWINT payment data, a `return_url`, and online `mandate_data.customer_acceptance` values (May raw lines 101–128). The described `requires_action` result supplies `next_action.redirect_to_url.url` for a TWINT-hosted page displaying a QR code. After authentication and return, the **SetupIntent** reaches `succeeded` (May raw lines 130–136).

The next step creates a subscription using that SetupIntent's PaymentMethod ID as `default_payment_method`. The first subscription **PaymentIntent** still has a client secret to send to the frontend to complete payment (May raw lines 138–158). Setup success establishes payment-method setup in the described flow, not payment success or subscription activation.

## May 2026 example: Subscriptions API

The example creates a subscription with `payment_behavior=default_incomplete` and `payment_settings.save_default_payment_method=on_subscription`, producing an initial invoice and PaymentIntent. It gets the PaymentIntent ID from `latest_invoice.payments` and returns the confirmation secret client secret for frontend payment completion (May raw lines 162–212).

The separate PaymentIntent confirmation example supplies TWINT payment data, `return_url`, and online `mandate_data` (May raw lines 216–231). When the **PaymentIntent** is `requires_action`, the example redirects to its `next_action.redirect_to_url.url`, a TWINT-hosted QR page. The guide describes the PaymentIntent reaching `succeeded` after authentication; only **after successful payment** does it say the subscription becomes active and saves the method as default (May raw lines 233–237). A displayed QR or redirect alone is not a success signal.

## Scope of parameters, QR, and eligibility

> [!warning] Contradiction
> The former source summary called `mandate_data` and `return_url` required for every TWINT subscription path. The May Checkout Session example has neither, while its direct SetupIntent and PaymentIntent confirmation examples contain both. Those examples do not provide an exhaustive API requiredness schema. The separate [[stripe-twint]] concept also states a saved-method reuse condition for `return_url`; do not collapse that condition into these first-setup examples.

The May direct API flows explicitly describe redirects to a TWINT-hosted page that displays the QR code. This supports those examples, not a claim that all client-side QR presentations are impossible. The May guide's 15 CHF monthly stock-photo price is an **example**, not evidence here of a universal CHF-only subscription or Switzerland-only eligibility rule. Separate primary TWINT sources need their own verification for those product limits.

## November 2026 navigation

The November same-URL index lists [Stripe-hosted page](https://docs.stripe.com/billing/subscriptions/twint.md?api-integration=checkout), [Setup Intents API](https://docs.stripe.com/billing/subscriptions/twint.md?api-integration=setupintents), and [Subscriptions API](https://docs.stripe.com/billing/subscriptions/twint.md?api-integration=subscription). Their current bodies were not included in the pinned index and were not used as factual evidence here.

## Related pages

- [[stripe-twint]] — TWINT concept and separately sourced product characteristics
- [[stripe-subscriptions]] — subscription concept
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-subscriptions-twint-2026|Stripe TWINT subscription guide, May 13 2026]] — dated full combined guide

## Related raw API references

- [[raw/stripe-billing-subscriptions-twint-2026-11-07|TWINT subscription variant index, November 7 2026]] — navigation only
