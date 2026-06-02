---
title: "GitHub: paypal-examples/v6-web-sdk-sample-integration"
type: source
date_ingested: 2026-04-17
original_format: github-repo
raw_files:
  - "github-paypal-v6-samples.md"
tags: [paypal, javascript-sdk-v6, samples, node-js, express, card-fields, venmo, google-pay, apple-pay, ach, sepa, apm, subscriptions, pay-later, vault, fastlane]
---

## Summary

Full working sample integration for PayPal JS SDK v6. Node.js/Express backend using `@paypal/paypal-server-sdk`, vanilla JS/HTML frontend. 36 files saved covering all major payment flows and APMs.

## Server architecture

- `paypalServerSdkClient.ts` — initializes PayPal server SDK with env credentials
- `authRouteHandler.ts` — `GET /paypal-api/auth/browser-safe-client-token` (for clientToken auth)
- `ordersRouteHandler.ts` — `POST /paypal-api/checkout/orders/create-with-sample-data`, `POST /paypal-api/checkout/orders/:id/capture`
- `vaultRouteHandler.ts` — `POST /paypal-api/vault/setup-token/create`, `POST /paypal-api/vault/payment-token/create`

## Client payment flows covered

### PayPal payments
- **Recommended**: standard `createPayPalOneTimePaymentSession` → `paypal-button` click → `session.start()`
- **Advanced patterns**: redirect, directAppSwitch, hydrateEligibleMethods (server-side eligibility), merchantAsyncValidation, paymentHandler, sandboxedIframe
- **TypeScript variant**: same pattern in TS
- **One-time + vault**: vault during payment capture
- **Save without purchase**: `VAULT_WITHOUT_PAYMENT` flow

### Card Fields
- One-time payment (recommended)
- One-time with 3DS
- Save/vault without purchase

### Other payment methods
| Method | Notes |
| --- | --- |
| Venmo | US only, `createVenmoOneTimePaymentSession` |
| Google Pay | `createGooglePayOneTimePaymentSession`, `getGooglePayConfig()` |
| Apple Pay | `createApplePayOneTimePaymentSession`, `validateMerchant`, `confirmOrder` |
| Guest Payments | 3 patterns: recommended, auto-start on load, with shipping callbacks |
| Subscriptions | `createPayPalSubscriptionPaymentSession` |
| Pay Later Messages | recommended + advanced |
| ACH Bank | US bank payments |
| SEPA | EU direct debit |
| Bancontact | Belgium |
| BLIK | Poland |
| EPS | Austria |
| iDEAL | Netherlands |
| P24 | Przelewy24 (Poland) |

## Key patterns to reference

- **`hydrateEligibleMethods`** — server pre-fetches eligibility, passes to client to avoid extra round-trip
- **`merchantAsyncValidation`** — validate order server-side before checkout opens
- **`sandboxedIframe`** — embedding PayPal in a sandboxed iframe context

## Related pages

- [[source-github-paypal-js-v6]] — React wrapper source code (implementation)
- [[source-npm-react-paypal-js-v9]] — npm README for @paypal/react-paypal-js v9.1.1
- [[source-paypal-payments-quickstart]] — Official quickstart docs
- [[paypal-checkout]] — PayPal Checkout concept page

## Raw Sources

- [[github-paypal-v6-samples]] — stub file with full file list and "What each file covers" table
