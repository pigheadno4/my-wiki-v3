---
title: "Stripe: Accept a Payment with SeQura"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/sequra/accept-a-payment"
raw_files:
  - "stripe-sequra-accept-payment-2025.md"
tags: [stripe, bnpl, sequra, buy-now-pay-later, consumer, spain, checkout, payment-intents]
---

## Summary

The 2026-05-06 guide describes SeQura (`sequra`) as a single-use payment method with 7–120 day terms. Customers leave the merchant site or app to authorize with SeQura, then return. The guide describes immediate success or failure notifications. The separate May [[source-stripe-sequra|SeQura overview]] describes Pay in 3 interest-free or up to 12 installments. Duration and installment count measure different things, and the captures leave their precise product mapping open.

## Dated integration guidance

- **Hosted Checkout.** The May guide assumes an existing Checkout integration. It uses EUR line items in one currency, supports payment mode and excludes setup and subscription modes. Its manual configuration example lists SeQura on the Checkout Session and uses `success_url`.
- **Checkout Sessions API with Elements.** The May examples create a Session on the server with `ui_mode: 'elements'`, use its Session client secret and set a Session `return_url` containing `{CHECKOUT_SESSION_ID}`.
- **Payment Intents API with Elements and Direct API.** The May routes use a server-created PaymentIntent and its client secret. The web confirmation examples include a PaymentIntent `return_url`. An optional Direct API server redirect uses the link in `next_action.redirect_to_url` when the Intent requires action. Check verified Intent status for return-page messaging and use the relevant Stripe success event for completion workflows.
- **Optional capture.** The May Payment Intents API with Elements guide shows `capture_method=manual`, a transition to `requires_capture` after successful authorization and an explicit PaymentIntent capture call. Stripe documents cancellation and `payment_intent.canceled` when the payment remains uncaptured for seven days. Merchant cancellation is available before that window elapses where the Intent is eligible.
- **Sandbox versus live.** The May Checkout Sessions and Payment Intents examples let testers approve or decline on a sandbox test page. Live redirects to SeQura.

The May Checkout compatibility sections label the business location “Europe.” The May Direct API currency mapping lists EUR for ES, and the May method overview explicitly lists Spain as the Stripe account location. Treat these as distinct documented descriptions. The broader Checkout wording leaves actual country eligibility unresolved.

## Detail locators

- May raw lines 8–85 cover hosted Checkout, eligibility and fulfillment. Lines 87–568 cover Checkout Sessions API with Elements.
- May raw lines 570–1158 cover Payment Intents API with Elements, including client confirmation, events and optional authorization/capture. Lines 1160–1390 cover Direct API, redirects and country mapping.
- The May PaymentIntent error tables at lines 1148–1158 and 1380–1390 include `payment_intent_invalid_currency`, `payment_intent_authentication_failure`, and `payment_intent_redirect_confirmation_without_return_url`.

## Related Pages

- [[stripe]] — Stripe company page
- [[stripe-bnpl#SeQura Details|Stripe BNPL and SeQura]]
- [[source-stripe-sequra]] — SeQura method overview

## Raw Sources

- [[raw/stripe-sequra-accept-payment-2025|2026-05-06 full SeQura acceptance guide]] — four historical web integration routes

## Related raw API references

- [[raw/stripe-payments-sequra-accept-a-payment-2026-11-07|2026-11-07 SeQura acceptance variant index]] — hosted Checkout, Checkout Sessions API and Payment Intents API with Elements, Direct API, iOS, and Android
