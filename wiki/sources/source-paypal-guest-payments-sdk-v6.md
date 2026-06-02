---
title: "PayPal Standalone Payment Buttons (Guest Payments) with JS SDK v6"
type: source
date_ingested: 2026-04-17
original_format: webpage
raw_files:
  - "paypal-guest-payments-sdk-v6.md"
tags: [paypal, guest-payments, javascript-sdk-v6, card-payments, standalone-button, shipping]
---

## Summary

Integration guide for accepting card/debit payments without requiring payers to log in or create a PayPal account, using **JS SDK v6** standalone payment buttons. Uses `"paypal-guest-payments"` component and `<paypal-basic-card-button>` custom element.

## Key takeaways

- **Component**: `"paypal-guest-payments"` in `createInstance`
- **Custom elements**: `<paypal-basic-card-container>` + `<paypal-basic-card-button>`
- **Session**: `createPayPalGuestOneTimePaymentSession({onApprove, onCancel, onComplete, onError, onWarn})`
- `createOrder()` returns `{ orderId: id }` — **object**, not plain string (differs from card fields)
- Presentation modes: `"auto"`, `"modal"`, `"popup"`, `"redirect"` (more options than Venmo which only has `"auto"`)

## 3 integration patterns

| Pattern | Description | Use when |
| --- | --- | --- |
| Standard button | User clicks button to start flow | Most cases (recommended) |
| Auto-start on load | Flow launches automatically on page load | Dedicated checkout page |
| Shipping callbacks | Validates address/options during checkout | Physical goods with shipping |

## Callbacks

| Callback | Required | Notes |
| --- | --- | --- |
| `onApprove(data)` | Yes | `data.orderId` available; capture server-side |
| `onCancel(data)` | Yes | Buyer cancelled |
| `onComplete(data)` | Yes | Flow completed (success/redirect) |
| `onError(data)` | Yes | Payment error |
| `onWarn(data)` | Yes | Buyer hit form submit error (card decline, name/address format) |
| `onShippingAddressChange(data)` | No | Throw `data.errors.COUNTRY_ERROR` to reject |
| `onShippingOptionsChange(data)` | No | Throw `data.errors.METHOD_UNAVAILABLE` to reject |

### `onWarn` shape

```json
{
  "message": "PayPalGuestCheckoutSession form submit failed: GUEST_CHECKOUT_INLINE_FORM_SUBMIT_FAILURE",
  "name": "PaymentFlowWarning",
  "code": "WARN_FLOW_GUEST_CHECKOUT_SUBMIT_ERROR"
}
```

## Shipping options structure

```json
{
  "id": "SHIP_FRE",
  "label": "Free",
  "type": "SHIPPING",
  "selected": true,
  "amount": { "value": "0.00", "currencyCode": "USD" }
}
```

## Backend endpoints

| Route | Purpose |
| --- | --- |
| `POST /paypal-api/checkout/orders/create-with-sample-data` | Creates order, returns `{ id }` |
| `POST /paypal-api/checkout/orders/create` | Creates order with custom payload |
| `POST /paypal-api/checkout/orders/{order-id}/capture` | Captures payment |

## Related pages

- [[source-paypal-card-fields-sdk-v6]] — Card fields (hosted iframes) — alternative card integration pattern
- [[source-paypal-payments-quickstart]] — Standard PayPal button quickstart
- [[source-paypal-venmo-sdk-v6]] — Venmo SDK v6 (US-only, similar pattern)
- [[paypal-expanded-checkout]] — Expanded checkout concept page

## Raw Sources

- [[paypal-guest-payments-sdk-v6]] — verbatim standalone payment buttons integration guide
