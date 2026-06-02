---
title: "PayPal Checkout: Authorize and Capture"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-authorize-and-capture.md"
tags: [paypal, checkout, authorize-capture, payments-api, orders-api, two-step-payment, reauthorize, idempotency]
---

## PayPal Checkout: Authorize and Capture

Official PayPal guide for implementing the 2-step authorize-and-capture payment flow — place a hold on buyer funds at checkout, capture later after completing business tasks.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/authorization/>

Last updated: 2025-05-09

## Key Takeaways

### Authorization lifecycle

| Period | Description |
| ------ | ----------- |
| **29 days** | Total authorization validity — hold on funds |
| **3 days** | Honor period — must capture within 3 days of authorization (or reauthorize) |
| **Reauthorize** | Resets the 3-day honor period; generates a new authorization ID; can be done multiple times within the 29-day window |

> Edge case: if you reauthorize on day 27, you get only 2 days of honor period (not a full 3).

### Integration changes vs default checkout

Only two changes needed from the standard one-time integration:

1. **Script tag**: add `&intent=authorize`

   ```javascript
   <script src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&intent=authorize">
   ```

2. **`onApprove`**: call your server to authorize (not capture). Returns `authorizationID` for later use.

### API flow

```
JS SDK (intent=authorize)
  → onApprove → POST /my-server/authorize-paypal-order  (server calls Orders API to authorize)
  → server saves orderID + authorizationID
  → [business tasks: verify inventory, etc.]
  → POST /v2/payments/authorizations/{authorizationID}/capture
```

### Key API endpoints (Payments REST API)

| Action | Endpoint |
| ------ | -------- |
| Show order details | `GET /v2/checkout/orders/{order_id}` |
| Reauthorize | `POST /v2/payments/authorizations/{authorization_id}/reauthorize` |
| Capture | `POST /v2/payments/authorizations/{authorization_id}/capture` |
| Void | `POST /v2/payments/authorizations/{authorization_id}/void` |
| Refund | `POST /v2/payments/captures/{capture_id}/refund` |

### Idempotency

Reauthorize and capture requests require a `PayPal-Request-Id` header — a unique alphanumeric ID you generate — to prevent duplicate operations if the API call is interrupted.

### Authorization response structure

The authorization object is nested inside `purchase_units[].payments.authorizations[]` in the Orders API response. Key fields:
- `id` — the authorization ID (use for reauthorize/capture/void)
- `status` — `CREATED` after authorization
- `expiration_time` — when the 29-day hold expires
- `seller_protection.status` — `ELIGIBLE` if covered

### After capture

- Transaction changes from `Pending` → `Completed` in business account
- Response contains `capture_id` — save this for future refunds

## When to use

Use authorize-and-capture when you need to complete business tasks between buyer approval and payment settlement — most commonly: verifying inventory, fraud review, or split fulfilment workflows.

## Raw Sources

- [[paypal-checkout-authorize-and-capture]] — verbatim webpage content with full code samples and API responses

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog
- [[source-paypal-checkout-integrate-one-time-payment]] — base integration this extends
