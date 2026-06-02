---
title: "GitHub: paypal/postman-collections"
type: source
date_ingested: 2026-04-16
original_format: github-repo
raw_files:
  - "github-paypal-postman-collections.md"
tags: [paypal, postman, api, testing, oauth, orders, payouts, subscriptions, webhooks]
---

## Summary

PayPal's official Postman collections repository. Contains three API collections (Public APIs, Checkout Flows, Partner APIs) and a TypeScript helper library (`paypal-postman-lib`) for Postman scripts. The collections are the canonical reference for real API request shapes, headers, and multi-step flows.

## Key Takeaways

- **Recommended**: fork from [postman.com/paypal](https://postman.com/paypal) to receive updates; importing JSON directly means no future sync
- **paypal-postman-lib**: TypeScript library used in Postman pre-request/test scripts; handles OAuth token refresh, sandbox detection, debug ID extraction, JWT creation, auth assertion generation
- **Collections cover**: Auth, Orders, Payments, Invoices, Subscriptions (products/plans/subscriptions), Payouts, Webhooks, vault flows, FXaaS, Payment Links, Partner APIs

## paypal-postman-lib Functions

### Authentication
- `needsNewAccessToken(config)` — checks if token needs refresh
- `refreshAccessToken(config, callback?)` — refreshes OAuth2 token
- `storeAccessToken(response, config)` — stores token from OAuth response

### Utilities
- `isSandbox()` — detects sandbox vs production environment
- `getPayPalDebugId()` — extracts `PayPal-Debug-Id` from response headers
- `base64Url(string)` — Base64URL encoding
- `getJWT(iss, data, alg, secret?)` — JWT creation
- `getAuthAssertionFor(clientId, payerId)` — generates PayPal auth assertion header

### Usage in Postman scripts
```javascript
eval(pm.collectionVariables.get("paypal_postman_scripts"));

if (this.PayPalPostmanUtils.needsNewAccessToken({...})) {
  this.PayPalPostmanUtils.refreshAccessToken({...});
}
const debugId = this.PayPalPostmanUtils.getPayPalDebugId();
```

## Collection API Coverage

| Collection | Key flows |
| --- | --- |
| PayPal_Public_APIs.json | Auth, Orders full lifecycle, Payments, Invoices+Templates, Subscriptions (products/plans/subs), Payouts, Webhooks |
| PayPal_Checkout_Flows.json | Card vault (non-3DS/3DS), PayPal vault (before/during purchase), recurring revenue, FXaaS, Payment Links |
| PayPal_Partner_APIs.json | Marketplace/partner APIs |

## Related Pages

- [[paypal]] — company page
- [[paypal-payouts]] — Payouts concept
- [[paypal-vault]] — Vault concept
- [[paypal-fxaas]] — FXaaS concept
- [[source-paypal-payouts-overview]] — full Payouts docs

## Raw Sources

- [[github-paypal-postman-collections]] — stub file pointing to detail directory
