---
title: "PayPal: Void an Authorized Payment"
type: source
date_ingested: 2026-04-17
original_format: webpage
raw_files:
  - "paypal-void-authorization.md"
tags: [paypal, void, authorization, payments-api, capture]
---

## Summary

Integration guide for voiding PayPal authorized payments using **Payments API v2** (`/v2/payments/authorizations/{authorization_id}/void`). Voiding cancels an authorization before capture, releasing held funds and saving processing fees. Builds on the [[source-paypal-payments-quickstart]] integration.

## Key takeaways

- **Endpoint**: `POST /v2/payments/authorizations/{authorization_id}/void` with empty body `{}`
- Requires `AUTHORIZE` intent on order creation — you need the **authorization ID**, not the order ID
- **All-or-nothing**: cannot partially void; entire authorized amount is released
- **Permanent**: once voided, the authorization cannot be captured — attempting capture will fail
- Saves up to ~3% in processing fees vs refunding a captured payment

## Authorization expiry

| Period | Duration |
| --- | --- |
| Standard | 3 days |
| Honor period | Up to 29 days |

Void promptly — don't let authorizations expire without explicit action.

## Fund release timing

- Sandbox: immediate
- Production: up to 24 hours depending on customer's bank

## Error codes

| Error code | HTTP status | Meaning |
| --- | --- | --- |
| `AUTHORIZATION_ALREADY_CAPTURED` | 422 | Already captured — use refund instead |
| `AUTHORIZATION_VOIDED` | 422 | Already voided |
| `AUTHORIZATION_EXPIRED` | 422 | Authorization has expired |
| `RESOURCE_NOT_FOUND` | 404 | Authorization ID not found |
| `PERMISSION_DENIED` | 403 | Account not authorized to void |
| `INTERNAL_SERVER_ERROR` | 500 | Generic server error |

## Void vs refund

| Scenario | Action |
| --- | --- |
| Payment authorized, not yet captured | Void (saves processing fees) |
| Payment already captured | Refund |

## Best practices

- Store authorization IDs immediately in database on order creation
- Void immediately when an order won't be fulfilled (don't let authorizations sit or expire)
- Automate void triggers for out-of-stock and fraud detection scenarios
- Train support team: target 80% void vs refund ratio
- Track void reasons for analytics

## Related pages

- [[source-paypal-refund-payment]] — Refund guide (for captured payments)
- [[source-paypal-payments-quickstart]] — Base integration this builds on
- [[source-paypal-standard-payments]] — Authorization vs. capture overview
- [[paypal-checkout]] — PayPal Checkout concept page

## Raw Sources

- [[paypal-void-authorization]] — verbatim void authorization integration guide
