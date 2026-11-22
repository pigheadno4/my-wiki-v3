---
title: "Stripe Docs — Accept a payment using Naver Pay in South Korea"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-naver-pay-accept-payment-2025.md"
tags: [stripe, south-korea, krw, naver-pay, local-payment-methods, nicepay, payment-intents, checkout]
---

## Summary

Integration guide for Naver Pay (`naver_pay`) in South Korea via Stripe's local processor partner (NICEPAY). Covers Checkout and Direct API paths. Key differentiator: funding source parameter allowing card or Naver Pay points.

## Key Facts

- **PM type**: `naver_pay`
- **Currency**: KRW only; **28 business locations** (all 28 KR card countries including Singapore — unlike Kakao Pay which excludes SG)
- **Minimum**: 100 KRW; stored value top-up max: 2,000,000 KRW (no max for card passthrough)
- **Modes**: payment ✓, setup ✓, subscription ✓ (recurring supported)
- **No buyer email required** — unlike Kakao Pay
- **Naver Pay points**: customers can optionally use Naver Pay Points balance to pay

## Unique: Funding Source Parameter

`payment_method_data.naver_pay.funding`:
- `'card'` (default) — buyer uses their linked Naver Pay card
- `'points'` — buyer uses their Naver Pay Points balance

## Integration Paths

### Checkout

- Add `naver_pay` to `payment_method_types`; all line items in `krw`
- Testing: select "Naver Pay" → Stripe-hosted redirect page → authorize or fail

### Direct API

1. Create PaymentIntent: `payment_method_types: ['naver_pay']` + `payment_method_data: { type: 'naver_pay', naver_pay: { funding: 'card' } }`
2. Client: `stripe.confirmPayment()` with `payment_method_data.type: 'naver_pay'` + `return_url`
3. NICEPAY disclosure required on checkout page
4. Post-payment: `payment_intent.succeeded` webhook

## Compliance Requirements

- **NICEPAY disclosure**: same required text as kr_card and kakao_pay
- **Naver Pay branding**: must comply with [overseas brand guidelines](https://developers.pay.naver.com/design/brand/overseas)

## Related Pages

- [[stripe-korea-payment-methods]] — South Korea payment methods concept page
- [[source-stripe-korea-payment-methods]] — South Korea overview
- [[source-stripe-kakao-pay-accept-payment]] — Kakao Pay integration for comparison
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-naver-pay-accept-payment-2025]] — verbatim webpage content
