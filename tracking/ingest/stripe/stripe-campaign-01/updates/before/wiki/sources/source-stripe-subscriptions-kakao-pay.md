---
title: "Stripe Subscriptions — Set Up Kakao Pay Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-kakao-pay-2026.md"
tags: [stripe, billing, subscriptions, kakao-pay, south-korea, krw, setup-intents, mandate]
---

## Summary

Integration guide for Kakao Pay subscriptions. Structurally identical to the KR card subscription guide — same 3 paths (SetupIntents, Subscriptions API, Checkout), same KRW-only constraint, same `off_session=true` + `mandate_data` requirements. PM type: `kakao_pay`.

## Key constraints

- **KRW only** — must convert prices to KRW
- **South Korea** — redirect to Kakao Pay for authorization
- `off_session=true` required on subscription create (SetupIntents path)
- `mandate_data` required

## Three integration paths

### Path 1: SetupIntents API

SetupIntent with `payment_method_data[type]=kakao_pay` + `mandate_data` + `usage=off_session` → customer authorizes mandate in Kakao Pay → create subscription with `default_payment_method` + `off_session=true`

### Path 2: Subscriptions API

Create subscription: `default_incomplete` + `save_default_payment_method='on_subscription'` → confirm PaymentIntent: `payment_method_data[type]=kakao_pay` + `mandate_data` → `requires_action` → customer authenticates → activates

### Path 3: Checkout

`payment_method_types=['card','kakao_pay']`, `mode='subscription'`

## Related pages

- [[stripe-korea-payment-methods]] — concept page (updated)
- [[source-stripe-subscriptions-kr-card]] — KR card subscription (identical structure)
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-kakao-pay-2026]] — verbatim Stripe docs webpage
