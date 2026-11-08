---
title: "Stripe Subscriptions — Set Up Amazon Pay Subscription"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/amazon-pay"
raw_files:
  - "stripe-subscriptions-amazon-pay-2026.md"
tags: [stripe, billing, subscriptions, amazon-pay, setup-intents, payment-intents, checkout]
---

## Summary

The 2026-05-13 Stripe guide describes three Amazon Pay subscription paths: Setup Intents API, Payment Intents API, and a Stripe-hosted Checkout page. The 2026-11-07 capture of the same canonical URL is an index linking to those three variants; it does not supply replacement flow or parameter details. The change in the captured page is presentation/navigation, not evidence that a path was deprecated or that its contract changed.

The older guide's 15 USD monthly stock-photo subscription is an example, not a general Amazon Pay price, currency, or billing-interval rule. Its path details below remain dated guidance; the November variant targets were not fetched in this campaign.

## Three integration paths in the 2026-05-13 capture

### Path 1: Setup Intents API

To save an Amazon Pay payment method for future use, the guide says to attach it to a Stripe Customer. Its server SetupIntent step specifies `payment_method_types=amazon_pay`, the Customer ID, and `usage=off_session` **or** `usage=on_session`; the shown server request chooses `off_session`, `confirm=true`, `mandate_data`, and `return_url`. The SetupIntent's `client_secret` is passed to Stripe.js for buyer authorization. The client section separately shows `stripe.confirmAmazonPaySetup(clientSecret, { return_url, mandate_data })` redirecting to Amazon. After obtaining the SetupIntent PaymentMethod ID, the guide's subscription example sets it as `default_payment_method` and uses `off_session=true`. It describes activation after a successful payment.

> [!warning] Contradiction
> The May guide shows `confirm=true` in its server SetupIntent request (lines 56–68) and later shows a client `confirmAmazonPaySetup` call (lines 171–188). The capture does not explain whether both confirmations belong in one runnable sequence. Treat these as documented examples, not a verified combined execution path.

The older source's subscription example:

```js
stripe.subscriptions.create({
  customer: customerId,
  items: [{ price: priceId }],
  default_payment_method: paymentMethodId, // from SetupIntent
  off_session: true
})
```

### Path 2: Payment Intents API

The May guide creates a subscription with `payment_behavior=default_incomplete`, `payment_settings.payment_method_types=['amazon_pay','card']`, and `payment_settings.save_default_payment_method='on_subscription'`. It expands `latest_invoice.payments` and `latest_invoice.confirmation_secret`, obtains the invoice PaymentIntent ID and returns the confirmation secret to the frontend. The subsequent server confirm example sends `payment_method_data[type]=amazon_pay`, `mandate_data`, and `return_url`. A `requires_action` response means the customer still must authenticate with Amazon Pay; the guide says the subscription activates and saves the method only after successful payment.

> [!warning] Contradiction
> For the PaymentIntent **confirm call**, the May prose says to set `payment_method_types=amazon_pay` (line 271), while the adjacent POST example uses `payment_method_data[type]=amazon_pay` and does not show `payment_method_types` on that request (lines 273–281). The intended confirm-call parameter is unresolved by these captures. The `payment_settings.payment_method_types` value on subscription creation is a separate setting.

### Path 3: Checkout (Stripe-hosted)

The May hosted variant creates a Checkout Session on the server in `subscription` mode with a recurring price, quantity, `success_url`, and `payment_method_types` including `amazon_pay`; the customer is redirected to the returned Session URL. The customer must authorize future Amazon-account payments through Checkout. This variant does not show the API-path `mandate_data` and `return_url` parameters; do not impose those parameter names on the hosted flow.

```js
stripe.checkout.sessions.create({
  payment_method_types: ['card', 'amazon_pay'],
  line_items: [{ price: priceId, quantity: 1 }],
  mode: 'subscription',
  success_url: '...'
})
```

The guide describes a **test** in which authenticating on the redirect page moves the PaymentIntent from `requires_action` to `succeeded`. This is test guidance, not a receipt for a live transaction.

## Key parameters by path

- SetupIntents API: the May guide specifies a Customer, `payment_method_types=amazon_pay`, and `usage=off_session` or `usage=on_session`; its server and client examples include `mandate_data` and `return_url`. The `off_session` usage in the sample is an example choice.
- PaymentIntents API: subscription creation configures `payment_settings.payment_method_types` and `save_default_payment_method`; the confirm prose and request example disagree on the Amazon Pay parameter name, while the example also supplies `mandate_data` and `return_url`.
- Hosted Checkout: the shown Checkout Session uses `mode=subscription`, `payment_method_types`, a recurring price and quantity, and `success_url`; customer authorization happens on the hosted path.

## Detail locators and limits

May capture: SetupIntents path and Customer requirement (lines 10–70), Stripe.js/client confirmation and subscription creation (143–216), PaymentIntents creation and confirmation (218–284), hosted Checkout and documented test (286–342). November index: purpose and variant links (lines 5–15). The captures do not establish current variant parameters or availability, account eligibility, completed customer authorization, a successful real payment, settlement, or future billing.

## Related pages

- [[stripe-amazon-pay]] — concept page
- [[stripe-subscriptions]] — subscription concept page
- [[stripe]] — company page

## Related raw API references

- [[raw/stripe-billing-subscriptions-amazon-pay-2026-11-07|2026-11-07 variant index; navigation only]]
- [Setup Intents API variant](https://docs.stripe.com/billing/subscriptions/amazon-pay.md?api-integration=setupintents) — linked by the November index; detailed target not fetched here
- [Payment Intents API variant](https://docs.stripe.com/billing/subscriptions/amazon-pay.md?api-integration=subscription) — linked by the November index; detailed target not fetched here
- [Stripe-hosted page variant](https://docs.stripe.com/billing/subscriptions/amazon-pay.md?api-integration=checkout) — linked by the November index; detailed target not fetched here

## Raw Sources

- [[raw/stripe-subscriptions-amazon-pay-2026|Stripe Amazon Pay subscription guide, captured 2026-05-13]]
