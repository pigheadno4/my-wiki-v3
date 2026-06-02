---
title: "Stripe Subscriptions — Set Up Amazon Pay Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-amazon-pay-2026.md"
tags: [stripe, billing, subscriptions, amazon-pay, setup-intents, payment-intents, checkout]
---

## Summary

Integration guide for Amazon Pay subscriptions. Three integration paths: SetupIntents API (pre-authorize then subscribe), Payment Intents API (create + confirm in two calls), and Checkout (hosted page).

## Three integration paths

### Path 1: SetupIntents API

1. Server: Create SetupIntent with `payment_method_types=['amazon_pay']`, `confirm=true`, `usage=off_session`, `mandate_data`, `return_url`
2. Client: `stripe.confirmAmazonPaySetup(clientSecret, { return_url, mandate_data })` → redirects to Amazon for authorization
3. Server: After redirect, create subscription with `default_payment_method` from SetupIntent PM, `off_session=true`

```js
// Step 3 - create subscription after SetupIntent succeeds
stripe.subscriptions.create({
  customer: customerId,
  items: [{ price: priceId }],
  default_payment_method: paymentMethodId, // from SetupIntent
  off_session: true
})
```

### Path 2: Payment Intents API

1. Server: Create subscription with `payment_behavior=default_incomplete`, `payment_settings.payment_method_types=['amazon_pay','card']`, `payment_settings.save_default_payment_method='on_subscription'`; expand `latest_invoice.payments` + `latest_invoice.confirmation_secret`
2. Return `confirmation_secret.client_secret` to frontend
3. Server: `POST /v1/payment_intents/:id/confirm` with `payment_method_data[type]=amazon_pay`, `mandate_data`, `return_url`
4. Response `status=requires_action` → customer authenticates at Amazon; subscription activates on success

### Path 3: Checkout (hosted)

```js
stripe.checkout.sessions.create({
  payment_method_types: ['card', 'amazon_pay'],
  line_items: [{ price: priceId, quantity: 1 }],
  mode: 'subscription',
  success_url: '...'
})
```

Minimal: just add `amazon_pay` to `payment_method_types`. Test by selecting Amazon Pay and authenticating on the redirect page.

## Key parameters

- `mandate_data` — required for Amazon Pay; captures customer acceptance (type=online, IP, user agent, timestamp)
- `return_url` — required; where Amazon redirects after authorization
- `usage=off_session` — for recurring charges without customer present
- `save_default_payment_method='on_subscription'` — auto-saves PM when subscription activates (PaymentIntents path)

## Related pages

- [[stripe-amazon-pay]] — concept page
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-amazon-pay-2026]] — verbatim Stripe docs webpage
