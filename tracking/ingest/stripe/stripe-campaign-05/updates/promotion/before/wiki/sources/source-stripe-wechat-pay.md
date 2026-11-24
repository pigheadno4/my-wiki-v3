---
title: "Stripe Docs — WeChat Pay payments"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-wechat-pay-2025.md"
tags: [stripe, wechat-pay, wallets, china, digital-wallet]
---

## Summary

WeChat Pay is the payment wallet inside Tencent's WeChat super app, with over 800 million users. It targets Chinese consumers, overseas Chinese, and Chinese travelers. Stripe supports WeChat Pay in 22 merchant countries.

## Key Facts

- **Customer base**: 800M+ WeChat Pay users inside WeChat's 1B+ MAU ecosystem
- **Default currency**: CNY; also supports AUD, CAD, EUR, GBP, HKD, JPY, SGD, USD, DKK, NOK, SEK, CHF (13 currencies total, mapped to merchant country)
- **Merchant countries**: 22 (AT, AU, BE, CA, CH, DE, DK, ES, FI, FR, GB, HK, IE, IT, JP, LU, NL, NO, PT, SE, SG, US)
- **Payment confirmation**: customer-initiated (app authentication)
- **Recurring payments**: not supported
- **Manual capture**: not supported
- **Disputes**: none — WeChat Pay requires in-app authentication, so fraud/unrecognized payment risk is low; no chargeback process
- **Refunds**: full and partial supported; must be submitted within 180 days of original charge; asynchronous — listen for `refund.updated` or `refund.failed` webhook events; failed refunds return amount to Stripe balance
- **Payout timing**: standard

## Product Support

- **Checkout**: supported (not in subscription or setup mode)
- **Payment Links**: supported
- **Elements**: supported (Express Checkout Element and Mobile Payment Element do not support WeChat Pay)
- **Invoicing**: supported (`send_invoice` collection method only)
- **Terminal**: supported (not available in Japan)

## Connect Support

Partial support depending on charge type:

- **Generally available**: Destination charges, Separate charges and transfers
- **Private preview**: Direct charges, `on_behalf_of`
- Standard Dashboard connected accounts can enable WeChat Pay themselves
- Non-standard accounts: platform requests `wechat_pay_payments` capability (private preview, contact Stripe Support)

## Integration

Dashboard-driven: enable WeChat Pay in Stripe Dashboard → Stripe auto-surfaces it in Checkout/Elements/Payment Links. Manual configuration available for in-person Terminal payments.

## Related Pages

- [[stripe-wallets]] — wallet payment methods overview
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-wechat-pay-2025]] — verbatim webpage content
