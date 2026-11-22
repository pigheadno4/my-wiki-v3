---
title: "Stripe Docs — Set up future payments with Naver Pay"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-naver-pay-set-up-future-payments-2025.md"
tags: [stripe, south-korea, krw, naver-pay, recurring, setup-intents, mandate, accounts-v2, nicepay]
---

## Summary

Guide for saving Naver Pay (`naver_pay`) for future or recurring payments. Mirrors the kr_card and kakao_pay set-up-future-payments structure with Accounts v2 + v1 dual-path throughout.

## Key Details

- **Mandate required**: written customer agreement before saving
- **Checkout framing**: customer must authorize their NICEPAY account for future Naver Pay payments
- **Recurring caveat**: `capture_method: 'automatic'` required — manual capture not supported for off-session payments

## Save Paths

### Checkout (setup mode)

- `mode: 'setup'`, `naver_pay` in `payment_method_types`, attach to `customer` or `customer_account`
- Testing: select "Naver Pay" → "Continue to Naver Pay"

### Direct API — SetupIntent path

1. `setupIntents.create({ payment_method_types: ['naver_pay'], payment_method_data: { type: 'naver_pay' }, usage: 'off_session'|'on_session', customer|customer_account })`
2. Client: `stripe.confirmNaverPaySetup(clientSecret, { return_url, mandate_data: { customer_acceptance: { type: 'online', online: { infer_from_client: true } } } })`

### Direct API — PaymentIntent with `setup_future_usage`

- `paymentIntents.create({ payment_method_types: ['naver_pay'], setup_future_usage: 'off_session', confirm: true, return_url, mandate_data: { customer_acceptance: { type: 'online', online: { ip_address, user_agent } } }, customer|customer_account })`

### Using a Saved Payment Method

`paymentIntents.create({ payment_method_types: ['naver_pay'], payment_method: '{{ID}}', off_session: true, confirm: true, capture_method: 'automatic', customer|customer_account })`

## Detach

`detachPaymentMethod` → fires `mandate.updated` + `payment_method.detached`

## Source Bug

`currency: 'ngn'` in both `setup_future_usage` PaymentIntent examples — same copy-paste error as kr_card and kakao_pay set-up guides. Preserved verbatim.

## Related Pages

- [[stripe-korea-payment-methods]] — South Korea payment methods concept page
- [[source-stripe-naver-pay-accept-payment]] — Naver Pay accept-a-payment (one-time + funding source)
- [[source-stripe-kakao-pay-set-up-future-payments]] — Kakao Pay save/recurring (same pattern)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-naver-pay-set-up-future-payments-2025]] — verbatim webpage content
