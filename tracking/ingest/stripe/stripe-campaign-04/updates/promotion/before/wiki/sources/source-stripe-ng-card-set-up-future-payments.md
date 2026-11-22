---
title: "Stripe Docs — Set up future payments with Naira card"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-ng-card-set-up-future-payments-2025.md"
tags: [stripe, nigeria, naira, ng-card, recurring, setup-intents, mandate, merchant-of-record]
---

## Summary

Guide for saving Naira card (`ng_card`) for future or recurring payments via SetupIntent API, PaymentIntent with `setup_future_usage`, and Checkout setup mode.

## Key Facts

- **Mandate required**: must collect written customer agreement (frequency, timing, amount, cancellation policy) before saving

## Save Paths

### Checkout (setup mode)

- `mode: 'setup'`, `ng_card` in `payment_method_types`, attach to `customer`
- Customer clicks "Continue to Naira card" → authenticates on redirect page → `requires_action` → `succeeded`

### Direct API — SetupIntent path

1. `stripe.setupIntents.create({ payment_method_types: ['ng_card'], usage: 'off_session'|'on_session', customer })`
2. Client: `stripe.confirmNgCardSetup(clientSecret, { return_url, mandate_data: { customer_acceptance: { type: 'online', online: { infer_from_client: true } } } })`
3. Redirect to MoR partner; SetupIntent transitions to `succeeded`

### Direct API — PaymentIntent with `setup_future_usage`

- `paymentIntents.create({ payment_method_types: ['ng_card'], setup_future_usage: 'off_session', confirm: true, return_url, mandate_data: { customer_acceptance: { type: 'online', online: { ip_address, user_agent } } }, customer })`
- Note: `mandate_data` requires explicit `ip_address` + `user_agent` here (unlike SetupIntent which can use `infer_from_client`)

### Manual server-side redirect

- Create PaymentIntent with `confirm: true`; check `next_action.type === 'redirect_to_url'`; redirect to `next_action.redirect_to_url.url`

## Using a Saved Payment Method

`paymentIntents.create({ payment_method_types: ['ng_card'], payment_method: '{{ID}}', off_session: true, confirm: true, customer })`

## Detach

Call `detachPaymentMethod` → fires `mandate.updated` + `payment_method.detached` events.

## Related Pages

- [[stripe-nigeria-payment-methods]] — Nigeria payment methods concept page
- [[source-stripe-ng-card-accept-payment]] — Naira card accept-a-payment (one-time)
- [[source-stripe-nigeria-payment-methods]] — Nigeria overview
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-ng-card-set-up-future-payments-2025]] — verbatim webpage content
