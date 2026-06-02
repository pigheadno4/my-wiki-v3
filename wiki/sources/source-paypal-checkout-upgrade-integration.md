---
title: "PayPal Checkout: Upgrade Integration (checkout.js → JS SDK)"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-upgrade-integration.md"
tags: [paypal, checkout, migration, checkout-js, express-checkout, javascript-sdk, legacy, deprecation]
---

## PayPal Checkout: Upgrade Integration (checkout.js → JS SDK)

Official PayPal migration guide from legacy `checkout.js` / Express Checkout integrations to the current JavaScript SDK. Includes a full deprecation mapping table.

Source URL: <https://developer.paypal.com/docs/checkout/standard/upgrade-integration/>

Last updated: 2025-05-09

## Key Takeaways

### Why upgrade

| Old behaviour | New behaviour |
| ------------- | ------------- |
| Static button images | Dynamically rendered buttons |
| Redirect to new page | Pop-up window |
| Limited button style control | Full style customisation |

### Pay Later migration note

If migrating from Billing Agreement and want to keep Pay Later: use **Billing With Purchase** instead — same features, compatible with current payment options.

### Complete callback migration map

| Old (`checkout.js`) | New (JS SDK) |
| ------------------- | ------------ |
| `payment()` | `createOrder()` |
| `actions.payment.create()` | Server-side `POST /v2/checkout/orders` |
| `onAuthorize()` | `onApprove()` |
| `actions.payment.execute()` | Server-side `POST /v2/checkout/orders/:id/capture` |
| `actions.redirect()` in callbacks | `window.location.href` |

### Script tag migration

| Old | New |
| --- | --- |
| `paypalobjects.com/api/checkout.js` | `paypalobjects.com/sdk/js` |
| `client` option in `render()` | `client-id=xyz` in script tag |
| `commit: true/false` in `render()` | `commit=true/false` in script tag |
| `env` option | Auto-detected from `client-id` |
| `locale` option in `render()` | `locale=xx_XX` in script tag |
| `funding.disallowed` | `disable-funding` / `disable-card` in script tag |
| `paypal.request` | Browser `fetch()` |
| `paypal.Promise` | Browser `Promise` |
| `style.size` (small/medium/large) | Container element CSS size |
| `funding.allowed` | Removed — PayPal auto-selects optimal buttons |

### Node.js patterns included

The guide includes raw `fetch`-based Node.js implementations for both `createOrder` and `capturePayment`, including `generateAccessToken()` via Basic auth. These are simpler than the Server SDK approach in the main integration guide — useful as a reference for minimal dependency setups.

## Images

- `raw/assets/paypal-checkout-upgrade-flow-diagram.svg` — diagram showing the new checkout flow (payer selects button → logs in → approves → returns to site)

## Raw Sources

- [[paypal-checkout-upgrade-integration]] — verbatim webpage content + downloaded SVG

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-integrate-one-time-payment]] — the current integration this guide upgrades to
