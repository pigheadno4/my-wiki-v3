---
title: "Stripe Docs — South Korean payment methods"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-korea-payment-methods-2025.md"
tags: [stripe, south-korea, krw, local-payment-methods, kakao-pay, naver-pay, samsung-pay, payco, wallets, installments]
---

## Summary

Stripe supports South Korean local payment methods via a local processor partner — no local entity required. Covers all locally-issued KR cards plus Kakao Pay, Naver Pay, Samsung Pay, and PAYCO.

## Key Facts

- **Local processor model** (not MoR): Stripe + local processor partner
- **Currency**: KRW only; **28 merchant countries**; **Payout**: T+4 US / T+7 elsewhere
- **4-day funding** after payment approval
- **Payment methods**:
  - All local KR cards — one-time + recurring
  - Kakao Pay — one-time + recurring (not SG)
  - Naver Pay — one-time + recurring
  - Samsung Pay — one-time only
  - PAYCO — one-time only
- **Manual capture**: Yes; **Partial capture**: No; **Connect**: Yes
- **Disputes**: Yes — 365-day customer window, **7 days** to respond, 45-day decision, final; 7 reason codes
- **Refunds**: Full + partial, 365-day window; Korean consumer law mandates 7-day right for goods/services, pro-rated for subscriptions
- **Installments**: ≥50,000 KRW; merchant gets full amount upfront; customer repays issuer
- **Subscription requirements**: 30-day notice before price change, 7-day payment reminder

## CDN Assets

- `raw/assets/stripe-korea-payment-flow.mp4` — payment flow demo video (6.5 MB)

## Related Pages

- [[stripe-korea-payment-methods]] — concept page
- [[source-stripe-local-payment-methods-by-country]] — hub page linking Nigeria + South Korea guides
- [[stripe-wallets]] — Samsung Pay also appears as a Stripe wallet PM
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-korea-payment-methods-2025]] — verbatim webpage content
