---
title: "Accept Crypto Payments (Pay with Crypto)"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-crypto.md"
  - "paypal-apm-crypto-orders-api.md"
tags: [paypal, apm, crypto, bitcoin, ethereum, pyusd, cryptocurrency, us-merchants, orders-api]
---

## Overview

PayPal's Pay with Crypto enables US merchants to accept ~100 cryptocurrencies from global buyers, with automatic settlement in the merchant's local currency. **Not in the APM overview table** — added January 2026, after the overview was last updated.

Source URL: <https://developer.paypal.com/docs/checkout/apm/crypto/>

Last updated: 2026-01-29

## Key Details

| Field | Value |
| --- | --- |
| Merchant countries | **US only** |
| Buyer countries | **Global** |
| Payment type | Cryptocurrency |
| Payment flow | Redirect |
| Settlement | **Local currency** (auto-converted by PayPal) |
| Minimum | 0.01 USD |
| Refunds | Yes, in **PYUSD** (stablecoin) |
| Buyer PayPal account | **Not required** |

## Completely Different from Other APMs

| Aspect | Crypto | Bank redirect APMs |
| --- | --- | --- |
| Merchant geography | US only | Global (ex RU/JP/BR) |
| Buyer geography | Global | Specific country |
| Payment method | ~100 cryptocurrencies | Local bank |
| Settlement | Auto-converted to local currency | Direct EUR/PLN/etc. |
| Refunds | PYUSD stablecoin | Same currency |
| Authorization | Capture only | Capture only |

## Key Features

- **~100 supported cryptocurrencies**: BTC, ETH, SOL, XRP, USDT, DOGE, PYUSD, and ~95 others
- **Two buyer flows**: self-custody wallet (Metamask etc.) OR exchange account (Coinbase etc.)
- **No PayPal account needed** for buyers
- **650M+ pro-crypto consumers** addressable globally
- **Lower fees** than cross-border card transactions

## Limitations

- No billing agreements, recurring payments, chargebacks, multi-seller
- **Capture-only** — no authorization+capture flow
- No vaulting
- US merchants only

## PYUSD

PayPal USD (PYUSD) is a stablecoin backed 1:1 with USD deposits, US treasuries, and cash equivalents. Used for refunds. Merchants receive settlements in their local currency — not in PYUSD.

## Top Supported Cryptocurrencies

BTC, ETH, XRP, USDT, SOL, BNB, USDC, DOGE, ADA, TRX, PYUSD — plus ~90 others. Full list of 99 in raw file.

## Integration

Orders V2 API only (no JS SDK).

## Orders API Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/crypto/orders-api/>

Last updated: 2026-01-29

### Create Order payload

```json
{
  "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
  "intent": "CAPTURE",
  "purchase_units": [{ "amount": { "currency_code": "USD", "value": "100.00" } }],
  "payment_source": {
    "crypto": {
      "country_code": "US",
      "name": { "given_name": "John", "surname": "Doe" },
      "experience_context": {
        "locale": "en-US",
        "return_url": "https://example.com/return",
        "cancel_url": "https://example.com/cancel"
      }
    }
  }
}
```

**USD only** — only supported `currency_code` for crypto. Response: `PAYER_ACTION_REQUIRED` → `payer-action` link → `https://www.paypal.com/payment/crypto?token=...`

> [!info] `cancel_url` also handles errors
> The `cancel_url` is used for both buyer cancellations AND errors during the crypto payment experience. Ensure your cancel page handles both scenarios and check query parameters for error codes.

### Onboarding

Two paths:

1. **Self-serve**: Account Settings > Products & Services > Payment Methods > Pay with crypto > Get Started
2. **Approval request**: sandbox/live approval links (`product=CRYPTO_PYMTS`)

Compliance review required. Account must be configured to accept/convert payments to USD.

### Refunds

- **Full refund**: `POST /v2/payments/captures/{id}/refund` with empty body
- **Partial refund**: same endpoint with `{ "amount": { "value": "10.99", "currency_code": "USD" } }`

Refunds issued in PYUSD (not in the original crypto).

### Webhooks

`PAYMENT.CAPTURE.COMPLETED`, `PAYMENT.CAPTURE.DENIED`, `CHECKOUT.ORDER.DECLINED` (with `most_recent_errors`). Error codes also appended as query params to `cancel_url`.

## Raw Sources

- [[paypal-apm-crypto]] — verbatim overview page with 99-currency table and 7 buyer flow screenshots
- [[paypal-apm-crypto-orders-api]] — Orders API integration: Create Order payload, cancel_url error handling, refunds in PYUSD, self-serve onboarding, compliance review

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview (note: crypto not in the original 11-APM table — added Jan 2026)
- [[paypal]] — PayPal company overview
