---
title: "PayPal Card Fields: One-Time Checkout with JS SDK v6"
type: source
date_ingested: 2026-04-17
original_format: webpage
raw_files:
  - "paypal-card-fields-sdk-v6.md"
  - "paypal-3ds-sdk-v6.md"
tags: [paypal, card-fields, javascript-sdk-v6, 3ds, sca, pci-dss, advanced-cards, orders-api, vault]
---

## Summary

Integration guide for rendering hosted card fields (number, expiry, CVV) for one-time checkout using **JS SDK v6**. PCI DSS SAQ A-EP compliant — card fields are PayPal-hosted iframes. Handles 3DS automatically via `submit()`.

## Key takeaways

- **Component**: `"card-fields"` in `createInstance`
- **Eligibility**: `isEligible("advanced_cards")` — gate rendering on this
- **Flow**: `createCardFieldsOneTimePaymentSession()` → `createCardFieldsComponent({type, placeholder})` → `appendChild` into containers → `submit(orderId, {billingAddress})` → handle 3 states

## submit() states

| State | Meaning | Action |
| --- | --- | --- |
| `"succeeded"` | Payment approved (3DS may or may not have occurred) | Check `liabilityShift`, then capture server-side |
| `"canceled"` | Buyer dismissed 3DS modal | Show retry option, non-blocking |
| `"failed"` | Validation or processing error | Inspect `data.message`, allow retry |

**`liabilityShift`** — present in `data` on `"succeeded"`, use to decide whether to proceed with capture.

## Critical gotchas

- Pass plain string `orderId` to `submit()` — **not** `{ orderId }` object (common bug)
- Card field containers must have defined height/width — field fills 100% of parent
- Production SDK URL: `https://www.paypal.com/web-sdk/v6/core` (not `sandbox.paypal.com`)
- 30+ CSS properties allowed for styling (font, padding, border, color, etc.); avoid validation-implied colors (red/green) unless synced with real validation state

## Backend requirements

| Route | Method | Purpose |
| --- | --- | --- |
| `/paypal-api/checkout/orders/create-with-sample-data` | POST | Returns `{ id: orderId }` |
| `/paypal-api/checkout/orders/{orderId}/capture` | POST | Captures order, returns capture data |

Uses Orders v2 API with `grant_type=client_credentials` app access token.

## PCI note

Card fields are PayPal-hosted iframes — qualifies for SAQ A-EP. Page must follow security best practices (HTTPS, CSP updated for PayPal domains, CSRF protection on backend routes).

## Related pages

- [[source-paypal-expanded-checkout-card-field-properties]] — Card field properties (SDK v5/expanded checkout)
- [[source-paypal-expanded-checkout-card-fields-events]] — Card fields events
- [[source-paypal-payments-quickstart]] — PayPal button quickstart (different component)
- [[paypal-expanded-checkout]] — Expanded checkout concept page

## Raw Sources

- [[paypal-card-fields-sdk-v6]] — verbatim card fields SDK v6 integration guide
- [[paypal-3ds-sdk-v6]] — 3DS/SCA integration: SCA_ALWAYS vs SCA_WHEN_REQUIRED, one-time + vault flows, createCardFieldsSavePaymentSession, liabilityShift, vaultSetupToken
