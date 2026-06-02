---
title: "PayPal JavaScript SDK v6 — Setup Guide"
type: source
date_ingested: 2026-04-19
original_format: webpage
raw_files:
  - "paypal-js-sdk-v6-setup-2025.md"
  - "paypal-js-sdk-v6-iframe-2025.md"
  - "paypal-js-sdk-v6-advanced-config-2025.md"
  - "paypal-js-sdk-v6-test-go-live-2025.md"
  - "paypal-js-sdk-v5-to-v6-upgrade-2025.md"
tags: [paypal, javascript-sdk, sdk-v6, checkout, eligibility, web-components, client-token]
---

## Summary

Canonical developer how-to guide for setting up PayPal JavaScript SDK v6. Covers script inclusion, authentication (clientId vs clientToken), `createInstance()` parameters, eligibility checking, all session creation methods, web components, and security best practices.

## Key Takeaways

- **Script URL**: `https://www.paypal.com/web-sdk/v6/core` (prod), `https://www.sandbox.paypal.com/web-sdk/v6/core` (sandbox)
- **Auth**: use clientId for most integrations; clientToken required only for vaulting + Fastlane
- **clientToken**: expires **15 minutes**; bound to domain; generate with `response_type=client_token` + `domains[]`
- **`createOrder()` must return `{ orderId: "..." }`** — object, not plain string (key v6 change)
- **Security**: NEVER pass item total from browser; validate on server before capture

## SDK Authentication

| Method | When to use |
| --- | --- |
| `clientId` | Standard checkout, one-time payments, card vaulting, most integrations |
| `clientToken` | PayPal payment vaulting + Fastlane **only** |

**Client token generation**:

```bash
curl -X POST 'https://api-m.sandbox.paypal.com/v1/oauth2/token' \
  -u 'CLIENT_ID:CLIENT_SECRET' \
  -d 'grant_type=client_credentials' \
  -d 'domains[]=YOUR_URL' \
  -d 'response_type=client_token'
```

## `createInstance()` Parameters

| Parameter | Required | Notes |
| --- | --- | --- |
| `clientId` | conditional | Mutually exclusive with `clientToken` |
| `clientToken` | conditional | 15min expiry; domain-bound; mutually exclusive with `clientId` |
| `components` | no | Array of components to load; default: `["paypal-payments"]` |
| `pageType` | no | checkout / product-details / cart / mini-cart / home |
| `locale` | no | BCP-47 tag e.g. `"en-US"`; auto-detected if omitted |
| `clientMetadataId` | no | For tracking/debugging; use `crypto.randomUUID()` |
| `merchantId` | yes (partners) | Seller merchant ID for partner integrations |

## 8 Available Components

`paypal-payments`, `venmo-payments`, `paypal-guest-payments`, `paypal-messages`, `card-fields`, `fastlane`, `googlepay-payments`, `applepay-payments`

## Eligibility API

```javascript
const paymentMethods = await sdkInstance.findEligibleMethods({ currencyCode: "USD" });
paymentMethods.isEligible("paypal")    // boolean
paymentMethods.isEligible("paylater")  // boolean
paymentMethods.isEligible("credit")    // boolean
paymentMethods.getDetails("paylater")  // → { productCode, countryCode }
paymentMethods.getDetails("credit")    // → { countryCode }
```

Always check eligibility before rendering payment buttons.

## Session Creation Methods

| Method | Component |
| --- | --- |
| `createPayPalOneTimePaymentSession()` | paypal-payments |
| `createPayLaterOneTimePaymentSession()` | paypal-payments |
| `createPayPalCreditOneTimePaymentSession()` | paypal-payments |
| `createFastlane()` | fastlane |

All sessions share callbacks: `onApprove(data)`, `onCancel(data)`, `onError(error)`.

Start a session: `session.start({ presentationMode: "auto" }, createOrder())`

## Web Components

`<paypal-button>`, `<paypal-pay-later-button>` (needs `productCode` + `countryCode`), `<paypal-credit-button>` (needs `countryCode`)

## Related Pages

- [[paypal]] — company page
- [[paypal-checkout]] — checkout integration concept
- [[source-paypal-payments-quickstart]] — full quickstart with JS SDK v6

## Raw Sources

- [[paypal-js-sdk-v6-setup-2025]] — full 528-line JS SDK v6 setup guide: script URLs, auth options, createInstance params, eligibility API, session methods, web components, security best practices
- [[paypal-js-sdk-v5-to-v6-upgrade-2025]] — v5→v6 migration: script URL loses client-id param; Buttons().render() → custom elements + session.start(); callbacks move to session not button; explicit findEligibleMethods() replaces internal eligibility; Venmo now requires venmo-payments component; clientId works for most (clientToken only for vaulting/Fastlane)
- [[paypal-js-sdk-v6-test-go-live-2025]] — Test + go live checklist: popup blocker, all callbacks, eligibility; production: swap sandbox URLs, configure webhooks, set up monitoring/alerting, test order capture
- [[paypal-js-sdk-v6-advanced-config-2025]] — Advanced config: `error.isRecoverable` for custom presentation mode fallback; try ["payment-handler","popup","modal"] in order; continue on recoverable, throw on non-recoverable
- [[paypal-js-sdk-v6-iframe-2025]] — Sandboxed iframe integration (662 lines): for PCI DSS/SOC 2; merchant(3001)+iframe(3000) architecture; ALWAYS validate postMessage origin; 5 event types; 3 presentation modes; iframe sandbox attrs; CSP + production security headers; Vite build config
