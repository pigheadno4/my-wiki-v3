---
title: "Stripe Subscriptions — Set Up Naver Pay Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-naver-pay-2026.md"
tags: [stripe, billing, subscriptions, naver-pay, south-korea, krw, setup-intents, mandate]
---

## Summary

Integration guide for Naver Pay subscriptions. Structurally identical to the KR card and Kakao Pay subscription guides — same 3 paths, same KRW-only constraint, same `off_session=true` + `mandate_data` requirements. PM type: `naver_pay`.

## Key constraints

- **KRW only** — prices must be converted to KRW
- `off_session=true` required on subscription create (SetupIntents path)
- `mandate_data` required

## Three integration paths

### Path 1: SetupIntents API

SetupIntent with `payment_method_data[type]=naver_pay` + `mandate_data` + `usage=off_session` → customer redirected to Naver Pay → SetupIntent `succeeded` → create subscription with `default_payment_method` + `off_session=true`

### Path 2: Subscriptions API

Create subscription: `default_incomplete` + `save_default_payment_method='on_subscription'` → confirm PaymentIntent: `payment_method_data[type]=naver_pay` + `mandate_data` → `requires_action` → activates

### Path 3: Checkout

`payment_method_types=['card','naver_pay']`, `mode='subscription'`

## Related pages

- [[stripe-korea-payment-methods]] — concept page (updated)
- [[source-stripe-subscriptions-kakao-pay]] — identical structure
- [[source-stripe-subscriptions-kr-card]] — identical structure
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-naver-pay-2026]] — verbatim Stripe docs webpage
