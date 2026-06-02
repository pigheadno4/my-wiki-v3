---
title: "PayPal Payments Quick Start Integration"
type: source
date_ingested: 2026-04-17
original_format: webpage
raw_files:
  - "paypal-payments-quickstart.md"
tags: [paypal, checkout, javascript-sdk, orders-api, quickstart, integration, negative-testing]
---

## Summary

Comprehensive quickstart guide for accepting PayPal payments, covering both a **JavaScript SDK v6** integration (full stack) and an **API-only** (REST/curl) integration. Part of the new `docs.paypal.ai` documentation site. Includes server setup in 6 languages (Node.js, Python, Java, PHP, Ruby, cURL), negative testing, go-live checklist, and post-launch monitoring guidance.

## Key takeaways

### JS SDK v6 integration

- Client-side uses `window.paypal.createInstance({ clientId, components: ["paypal-payments"] })`
- Flow: `createInstance` → `findEligibleMethods` → `createPayPalOneTimePaymentSession` → button click → `paypalCheckoutSession.start()`
- **Critical**: Pass the `createOrder` promise to `start()` without `await` — awaiting before `start()` causes transient activation issues in browsers
- SDK loaded from `https://www.sandbox.paypal.com/web-sdk/v6/core` with `onload` callback

### API-only integration (Orders v2)

- Three multi-step flows:
  1. **Payment source in create** — pass `payment_source` in create order request → redirect to RYP page → capture/authorize
  2. **Confirm payment source** — create order → confirm payment source separately → redirect → capture
  3. **Authorize then capture** — create order → redirect → authorize → capture
- Intent options: `CAPTURE` (immediate) or `AUTHORIZE` (hold for up to 29 days)
- `user_action`: `CONTINUE` (default, buyer reviews on merchant site) or `PAY_NOW` (single page, skip merchant review)
- Order lives in `CREATED` state for 3 hours; extendable to 72 hours (requires TAM)
- HATEOAS: `payer-action` link in create response provides buyer approval URL

### Shipping preferences

| Value | Behavior |
| --- | --- |
| `GET_FROM_FILE` | Default — use buyer's PayPal shipping address |
| `SET_FROM_PROVIDER` | Merchant-provided address via `purchase_units.shipping`; buyer cannot edit |
| `NO_SHIPPING` | For digital goods / no physical delivery |

### Negative testing

Enabled via `PayPal-Mock-Response: {"mock_application_codes": "..."}` header. Automatically disabled in production. Requires enabling in sandbox business account settings.

| Error code | Trigger point |
| --- | --- |
| `INSUFFICIENT_FUNDS` | Capture |
| `INSTRUMENT_DECLINED` | Capture |
| `TRANSACTION_REFUSED` | Capture |
| `INTERNAL_SERVER_ERROR` | Create or capture |
| `DUPLICATE_INVOICE_ID` | Create |

### Best practices

- Never create orders client-side — always use server endpoints
- Never hardcode credentials — use environment variables
- Store capture IDs for refunds, disputes, and record keeping
- Test in sandbox before going live

### Go-live checklist

- All sandbox test scenarios pass
- Switch `.env` from development to production section
- Update HTML client ID to production
- Add HTTPS certificate
- Test with real $1 transaction

### Post-launch monitoring targets (suggested, not guaranteed by PayPal)

| Metric | Target |
| --- | --- |
| Payment success rate | 95% |
| Cancel rate | <20% |
| Error rate | <2% |
| Order creation response time | <2 seconds |
| Capture response time | <3 seconds |

## Images

- ![PayPal order processing flow](../raw/assets/paypal-orders-api-standard-flow.png)
- ![PayPal checkout sequence diagram — consumer to merchant to PayPal](../raw/assets/paypal-orders-api-merchant-website-flow.png)
- ![Single-step buyer approval page](../raw/assets/paypal-orders-api-single-step-buyer-approval.png)

## Related pages

- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-standard-payments]] — Overview page for standard payments features
- [[paypal]] — PayPal company page

## Raw Sources

- [[paypal-payments-quickstart]] — verbatim quickstart integration guide
