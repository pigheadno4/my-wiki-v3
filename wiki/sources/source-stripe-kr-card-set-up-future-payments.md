---
title: "Stripe Docs — Set up future payments with South Korean cards"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-kr-card-set-up-future-payments-2025.md"
tags: [stripe, south-korea, krw, kr-card, recurring, setup-intents, mandate, accounts-v2]
---

## Summary

Guide for saving South Korean cards (`kr_card`) for future or recurring payments. Notable for supporting both Accounts v2 (`customer_account`) and Customers v1 (`customer`) throughout. Mirrors the Nigerian card save flow but adds Accounts v2 support and includes a recurring capture caveat.

## Key Facts

- **Accounts v2 supported**: `customer_account` (GA for Connect, public preview for others) alongside Customers v1 `customer` — both variants shown for every API call
- **Mandate required**: written customer agreement before saving (frequency, timing, amount, cancellation policy)
- **Recurring caveat**: `capture_method: 'automatic'` required — manual capture not supported for off-session recurring payments

## Save Paths

### Checkout (setup mode)

- `mode: 'setup'`, `kr_card` in `payment_method_types`, attach to `customer` or `customer_account`
- Testing: select "Local card" → "Continue to Local card" → Stripe-hosted redirect page

### Direct API — SetupIntent path

1. `setupIntents.create({ payment_method_types: ['kr_card'], payment_method_data: { type: 'kr_card' }, usage: 'off_session'|'on_session', customer|customer_account })`
2. Client: `stripe.confirmKrCardSetup(clientSecret, { return_url, mandate_data: { customer_acceptance: { type: 'online', online: { infer_from_client: true } } } })`

### Direct API — PaymentIntent with `setup_future_usage`

- `paymentIntents.create({ payment_method_types: ['kr_card'], setup_future_usage: 'off_session', confirm: true, return_url, mandate_data: { customer_acceptance: { type: 'online', online: { ip_address, user_agent } } }, customer|customer_account })`

### Manual server-side redirect

- Create PaymentIntent with `confirm: true`; check `next_action.type === 'redirect_to_url'`; redirect to `next_action.redirect_to_url.url`

## Using a Saved Payment Method

`paymentIntents.create({ payment_method_types: ['kr_card'], payment_method: '{{ID}}', off_session: true, confirm: true, capture_method: 'automatic', customer|customer_account })`

## Detach

`detachPaymentMethod` → fires `mandate.updated` + `payment_method.detached`

## Source Bug

The Stripe docs use `currency: 'ngn'` (Nigerian Naira) in both `setup_future_usage` PaymentIntent examples — should be `currency: 'krw'`. Preserved verbatim.

## Related Pages

- [[stripe-korea-payment-methods]] — South Korea payment methods concept page
- [[source-stripe-kr-card-accept-payment]] — KR card accept-a-payment (one-time)
- [[source-stripe-korea-payment-methods]] — South Korea overview
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-kr-card-set-up-future-payments-2025]] — verbatim webpage content
