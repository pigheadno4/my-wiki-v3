---
title: "Stripe Docs — Set up future payments with Kakao Pay"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-kakao-pay-set-up-future-payments-2025.md"
tags: [stripe, south-korea, krw, kakao-pay, recurring, setup-intents, mandate, accounts-v2, nicepay]
---

## Summary

Guide for saving Kakao Pay (`kakao_pay`) for future or recurring payments. Mirrors the kr_card set-up-future-payments structure with Accounts v2 + v1 dual-path throughout.

## Key Details

- **Mandate required**: written customer agreement before saving
- **Checkout framing**: customer must explicitly authorize their NICEPAY account for future Kakao Pay payments
- **Recurring caveat**: `capture_method: 'automatic'` required — manual capture not supported for off-session payments

## Save Paths

### Checkout (setup mode)

- `mode: 'setup'`, `kakao_pay` in `payment_method_types`, attach to `customer` or `customer_account`
- Testing: select "Kakao Pay" → "Continue with Kakao Pay"

### Direct API — SetupIntent path

1. `setupIntents.create({ payment_method_types: ['kakao_pay'], payment_method_data: { type: 'kakao_pay' }, usage: 'off_session'|'on_session', customer|customer_account })`
2. Client: `stripe.confirmKakaoPaySetup(clientSecret, { return_url, mandate_data: { customer_acceptance: { type: 'online', online: { infer_from_client: true } } } })`

### Direct API — PaymentIntent with `setup_future_usage`

- `paymentIntents.create({ payment_method_types: ['kakao_pay'], setup_future_usage: 'off_session', confirm: true, return_url, mandate_data: { customer_acceptance: { type: 'online', online: { ip_address, user_agent } } }, customer|customer_account })`

### Manual server-side redirect

- Create PaymentIntent with `confirm: true`; check `next_action.type === 'redirect_to_url'`; redirect to `next_action.redirect_to_url.url`

## Using a Saved Payment Method

`paymentIntents.create({ payment_method_types: ['kakao_pay'], payment_method: '{{ID}}', off_session: true, confirm: true, capture_method: 'automatic', customer|customer_account })`

## Detach

`detachPaymentMethod` → fires `mandate.updated` + `payment_method.detached`

## Source Bugs

- `currency: 'ngn'` in both `setup_future_usage` PaymentIntent examples — should be `krw` (same copy-paste error as kr_card set-up guide, preserved verbatim)
- Accounts v2 saved PM uses `{{PAYMENTMETHOD_ID}}` vs Customers v1 `{{PAYMENT_METHOD_ID}}` — inconsistent placeholder naming in source

## Related Pages

- [[stripe-korea-payment-methods]] — South Korea payment methods concept page
- [[source-stripe-kakao-pay-accept-payment]] — Kakao Pay accept-a-payment (one-time)
- [[source-stripe-kr-card-set-up-future-payments]] — KR card save/recurring (same pattern)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-kakao-pay-set-up-future-payments-2025]] — verbatim webpage content
