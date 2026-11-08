---
title: "Stripe Subscriptions — Set Up Kakao Pay Subscription"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/kakao-pay"
raw_files:
  - "stripe-subscriptions-kakao-pay-2026.md"
tags: [stripe, billing, subscriptions, kakao-pay, south-korea, krw, setup-intents, mandate]
---

## Summary

The 2026-05-13 capture is a full Kakao Pay subscription guide with SetupIntents-labeled, Subscriptions API, and Stripe-hosted Checkout variants. It documents an illustrative 100,000 KRW monthly price and says to convert prices to KRW for this payment method (old lines 8–32, 91–217). Its paths have different request examples and must not be collapsed into universal parameter requirements. The 2026-11-07 capture at the same canonical URL is **only a variant index** (new lines 5–13); it supplies navigation, not current API parameters, currency eligibility, payment outcomes, or evidence that the old content was deprecated.

## May 2026 guide: path-specific evidence

### SetupIntents-labeled variant

The section's concrete steps show a **server-side SetupIntent** example containing `payment_method_data[type]=kakao_pay`, `payment_method_types[]=kakao_pay`, `usage=off_session`, and online `mandate_data.customer_acceptance` fields (old lines 34–50). It says the SetupIntent `client_secret` goes to Stripe.js on the client side to redirect the buyer to Kakao Pay for mandate authorization (old line 52). A later **subscription-create** example uses the returned PaymentMethod ID as `default_payment_method` and includes `off_session: true` on that request (old lines 54–73). These fields are shown on distinct example requests; the capture does not separately establish `usage=off_session` or `off_session=true` as universal across every implementation.

The prose at old line 12 says the first call creates a Subscription and PaymentIntent, while the concrete section at old lines 34–73 starts with a SetupIntent and then creates a subscription. This internal conflict is unresolved. Do not use the summary sentence to assert a definitive runnable sequence.

The old confirmation paragraph says to set `payment_method_types=kakao_pay`, but its shown command uses unusual `payment_method_data[]` fields instead (old lines 77–87). That mismatch has not been resolved or executed. The paragraph says a `requires_action` response calls for the customer to complete Kakao Pay payment; **only after successful payment** does it describe the subscription becoming Active and saving the default method (old lines 89). No live payment or future recurring success is shown.

### Subscriptions API variant

The old guide describes subscription creation with `payment_behavior=default_incomplete`, `payment_settings.save_default_payment_method=on_subscription`, and expansion of first-invoice payment and confirmation-secret fields (old lines 91–142). It then describes confirming the PaymentIntent with Kakao Pay, a return URL, and online `mandate_data` in its example (old lines 144–157). The prose says to set `payment_method_types` on confirmation, while the command shows `payment_method_data[type]=kakao_pay`; this is an unresolved prose/example mismatch, not a verified request contract. The documented `requires_action` state calls for customer authentication; **after successful payment**, the guide says the subscription becomes active and saves the payment method (old line 159).

### Stripe-hosted Checkout variant

The May page uses a Checkout Session in `subscription` mode with `card` and `kakao_pay` in the example's `payment_method_types` and a recurring price line item (old lines 161–213). It says the customer must authorize future use of Kakao Pay through Checkout (old lines 185–187). Its test description has a successful authentication case moving the PaymentIntent from `requires_action` to `succeeded` (old lines 215–217). The Checkout sample does not show the direct-path `usage=off_session`, `off_session=true`, or `mandate_data` fields; absence in a sample does not establish a prohibition or default.

## Scope and unresolved verification

The May capture's KRW instruction is dated evidence; the November index gives no currency statement. Neither capture proves any merchant's Kakao Pay eligibility, a successful live mandate or payment, settlement, or future recurring charge. The three linked November variant pages were not read for this source update, so their current client/server sequence, parameters, state behavior, and currency requirements remain unverified.

The source is comparable to [[source-stripe-subscriptions-kr-card]] only at the level of the observed **three-path organization**. This Kakao Pay evidence does not establish identical parameters, eligibility, or payment behavior across the two methods.

## Related pages

- [[stripe-korea-payment-methods]] — Korea payment-method concept
- [[stripe-subscriptions]] — subscription concept
- [[stripe]] — company page

## Related raw API references

The 2026-11-07 index [[raw/stripe-billing-subscriptions-kakao-pay-2026-11-07|Kakao Pay variant index]] points to these **unread** variant URLs for separate collection; it is navigation only and is not part of factual `raw_files` provenance:

- [SetupIntents API variant](https://docs.stripe.com/billing/subscriptions/kakao-pay.md?api-integration=setupintents)
- [Subscriptions API variant](https://docs.stripe.com/billing/subscriptions/kakao-pay.md?api-integration=subscription)
- [Stripe-hosted page variant](https://docs.stripe.com/billing/subscriptions/kakao-pay.md?api-integration=checkout)

## Raw Sources

- [[raw/stripe-subscriptions-kakao-pay-2026|2026-05-13 full Kakao Pay subscription guide]]
