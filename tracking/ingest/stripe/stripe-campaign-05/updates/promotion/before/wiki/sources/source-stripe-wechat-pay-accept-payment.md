---
title: "Stripe Docs — Accept a WeChat Pay payment"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-wechat-pay-accept-payment-2025.md"
tags: [stripe, wechat-pay, wallets, china, digital-wallet, payment-intents, checkout]
---

## Summary

Integration guide for WeChat Pay covering two paths: Checkout (hosted and embedded page) and Direct API (web only). WeChat Pay is web-only for Direct API; Terminal is handled separately.

## Integration Paths

### Checkout

- Add `wechat_pay` to `payment_method_types`
- Set `payment_method_options.wechat_pay.client = 'web'`
- All line items must use the same currency
- No setup mode or subscription mode support
- Testing: click Pay → QR rendered in Checkout → scan routes to Stripe-hosted simulation page

### Direct API (web only)

1. Create `PaymentIntent` server-side with `payment_method_types: ['wechat_pay']`
2. Pass `client_secret` to client (SPA fetch or server-side render)
3. Call `stripe.confirmWechatPayPayment(clientSecret, { payment_method_options: { wechat_pay: { client: 'web' } } })`
4. Render QR code from `next_action.wechat_pay_display_qr_code`:
   - `.data` — convert to QR image yourself
   - `.image_data_url` — use directly as `<img src>` (simpler)
5. Wait on QR page; fulfill order via `payment_intent.succeeded` webhook
6. Testing: scan QR with any QR scanner app → Stripe-hosted test page (authorize or fail)

## Key Details

- **Supported business locations (Checkout)**: 37 countries — AU, AT, BE, BG, CA, CY, CZ, DK, EE, FI, FR, DE, GR, HK, HU, IE, IT, JP, LV, LT, LU, MT, NL, NO, PL, PT, RO, SG, SK, SI, ES, SE, CH, GB, US (more than the 22 listed on the overview page)
- **Supported currencies**: `aud, cad, cny, eur, gbp, hkd, jpy, sgd, usd, dkk, nok, sek, chf`
- **Web only**: Direct API path is web only; mobile SDK not supported
- **Fulfillment**: webhook-based — `payment_intent.succeeded` / `payment_intent.payment_failed`
- Customer always sees amount in CNY in WeChat Pay app regardless of charge currency

## Related Pages

- [[stripe-wallets]] — wallet payment methods overview; WeChat Pay Details section
- [[source-stripe-wechat-pay]] — WeChat Pay overview (business locations, currencies, Connect, refunds)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-wechat-pay-accept-payment-2025]] — verbatim webpage content
