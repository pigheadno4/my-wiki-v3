---
title: "Integrate Apple Pay with JS SDK for Direct Merchants"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-apple-pay.md"
  - "paypal-applepay-sdk-v6.md"
tags: [paypal, apple-pay, apm, javascript-sdk, javascript-sdk-v6, orders-api, domain-validation, safari, ios, direct-merchant]
---

## Overview

Full integration guide for accepting Apple Pay as a one-time payment method on the web using the PayPal JS SDK and Orders v2 API. Covers sandbox setup, domain validation, SDK integration, payment sheet customization, and go-live steps.

Source URL: <https://developer.paypal.com/docs/checkout/apm/apple-pay/>

Last updated: 2025-08-06

## Key Takeaways

### Availability

**34 countries, 22 currencies** — includes Greece (not in the standard 35-country vault list). Countries: AU, AT, BE, BG, CA, CN, CY, CZ, DK, EE, FI, FR, DE, **GR**, HK, HU, IE, IT, JP, LV, LI, LT, LU, MT, NL, NO, PL, PT, RO, SG, SK, SI, ES, SE, US, GB.

Currencies: AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD, USD.

> [!warning] Contradiction — "Safari only" claim
> The existing [[paypal-apple-pay]] concept page states "Safari only." This guide clarifies: **with the latest Apple Pay SDK** (`applepay.cdn-apple.com/jsapi/1.latest/apple-pay-sdk.js`), customers can also pay using **non-Safari browsers**. The Safari-only restriction applies only without the latest SDK.

### Device requirements

- iOS 12.1 or later
- macOS 10.14.1 or later
- Must support Apple Pay

### iframe support

- iframe tag must have `allow="payment"` attribute
- Parent domain must be validated with PayPal

### Scope

**One-time payments with buyer present only.** Apple Pay Recurring for Japan not supported.

### Domain validation (critical prerequisite)

Domain must be registered before Apple Pay works. Requirements:
1. Download domain association file and host at `/.well-known/apple-developer-merchantid-domain-association`
2. No HTTP redirects (3XX); must be HTTPS 1.1; served with `Content-Type: application/octet-stream`
3. Register all high-level domains and subdomains in Developer Dashboard

### 4 integration touchpoints

| Touchpoint | API | Purpose |
| --- | --- | --- |
| Eligibility check | `paypal.Applepay().config()` | Returns `isEligible`, `countryCode`, `merchantCapabilities`, `supportedNetworks` |
| Session creation | `new ApplePaySession(4, paymentRequest)` | Must be inside user gesture (onclick); throws exception otherwise |
| Merchant validation | `paypal.Applepay().validateMerchant()` | Called in `onvalidatemerchant` callback |
| Payment confirmation | `paypal.Applepay().confirmOrder()` | Called in `onpaymentauthorized` with `orderId`, `token`, `billingContact` |

### SDK script tags (both required)

```html
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&currency=USD&components=applepay"></script>
<script src="https://applepay.cdn-apple.com/jsapi/1.latest/apple-pay-sdk.js"></script>
```

### Payment sheet customization

Configurable via Apple Pay JS SDK: `lineItems`, `requiredBillingContactFields`, `requiredShippingContactFields`, `billingContact`, `onshippingcontactselected`, `onshippingmethodselected`.

### Go-live requirements

- Production onboarding: `paypal.com/bizsignup/add-product?product=payment_methods&capabilities=APPLE_PAY`
- Download and host **live** domain association file (different from sandbox)
- Register live domains in PayPal Developer Dashboard

## Raw Sources

- [[paypal-apm-apple-pay]] — verbatim integration guide with full code samples

## Relevant Wiki Pages

- [[paypal-apple-pay]] — Apple Pay concept page (vault flow, recurring charges, key constraints)
- [[paypal-apm]] — APM overview with all 11 supported methods
- [[source-paypal-save-applepay-js-sdk]] — Apple Pay vault integration (save for future charges)
- [[paypal-applepay-sdk-v6]] — SDK v6 integration (docs.paypal.ai): `applepay-payments` component, `createApplePayOneTimePaymentSession`, `config()` → merchantCapabilities/supportedNetworks, `confirmOrder({orderId, token, billingContact})`, ngrok setup for local dev
