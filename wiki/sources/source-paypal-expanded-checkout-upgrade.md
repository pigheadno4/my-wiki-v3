---
title: "PayPal Expanded Checkout: Upgrade Guide"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-upgrade.md"
tags: [paypal, expanded-checkout, migration, express-checkout, nvp-soap, orders-api, javascript-sdk, upgrade]
---

## PayPal Expanded Checkout: Upgrade Guide

Migration guide from Express Checkout (NVP/SOAP) or PayPal Checkout (JS SDK) to Expanded Checkout. Covers two distinct upgrade paths with different complexity levels, plus NVP/SOAP → Orders v2 API method mapping.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/upgrade/>

Last updated: 2025-05-12

## Key Takeaways

### Two upgrade paths — very different effort

| From | API changes needed | Frontend changes |
| ---- | ------------------ | ---------------- |
| **PayPal Checkout** | None — same APIs | Add `components=buttons,card-fields` to script tag; add CardFields HTML + JS |
| **Express Checkout (NVP/SOAP)** | Full migration to Orders v2 REST + OAuth2 | Add `components=buttons,card-fields`; add CardFields HTML + JS |

### PayPal Checkout → Expanded Checkout (easy)

1. Add `&components=buttons,card-fields` to the JS SDK script tag
2. Add CardFields HTML container + submit button
3. Initialize `paypal.CardFields({ createOrder })` and `.render('#card-fields')`
4. Wire submit button to `paypal.CardFields().submit()`

No server-side changes needed.

### Express Checkout NVP/SOAP → Expanded Checkout (full migration)

#### API method mapping

| NVP/SOAP | Orders v2 REST |
| -------- | -------------- |
| `SetExpressCheckout` | `POST /v2/checkout/orders` |
| `GetExpressCheckoutDetails` | `GET /v2/checkout/orders/{id}` |
| `DoExpressCheckoutPayment` (capture) | `POST /v2/checkout/orders/{id}/capture` |
| `DoExpressCheckoutPayment` (update + capture) | **Two calls**: `PATCH /v2/checkout/orders/{id}` + `POST /v2/checkout/orders/{id}/capture` |

> [!warning] Update + capture now requires 2 API calls
> In NVP/SOAP, `DoExpressCheckout` could update order details and capture payment in a single call. In Orders v2, these are separate operations — PATCH to update, then POST to capture.

#### Auth migration: credentials → OAuth2

NVP/SOAP sent `USER`, `PWD`, `SIGNATURE` inline. Orders v2 uses OAuth2 access tokens:

```javascript
const auth = Buffer.from(CLIENT_ID + ":" + CLIENT_SECRET).toString("base64");
const response = await fetch(`${base}/v1/oauth2/token`, {
  method: "POST",
  body: "grant_type=client_credentials",
  headers: { Authorization: `Basic ${auth}` }
});
const { access_token } = await response.json();
```

#### Tools available

- **Parameter Mapping Tool**: `/tools/limited/api-transformer/mapping/` — maps NVP/SOAP params to Orders v2 fields
- **API Transformer**: `/tools/limited/api-transformer/converter/` — converts full NVP/SOAP request bodies to Orders v2 format

### Sandbox capability requirement

Sandbox business account must have **Expanded Credit and Debit Card Payments** enabled:
Developer Dashboard → Apps & Credentials → select app → Features → Accept payments → enable checkbox.

If created via sandbox.paypal.com and disabled, complete sandbox onboarding at `sandbox.paypal.com/bizsignup/`.

## Raw Sources

- [[paypal-expanded-checkout-upgrade]] — verbatim webpage content with full NVP/SOAP payload examples, SDK script tag diffs, server-side code samples

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[source-paypal-checkout-upgrade-integration]] — Standard Checkout upgrade guide (checkout.js → JS SDK migration)
- [[source-paypal-expanded-checkout-eligibility]] — country/currency/payment method support for Expanded Checkout
- [[source-paypal-expanded-checkout-integrate]] — full Expanded Checkout integration guide
