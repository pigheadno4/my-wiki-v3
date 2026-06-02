---
title: "PayPal: Authorize and Delay Capture"
type: source
date_ingested: 2026-04-17
original_format: webpage
raw_files:
  - "paypal-delayed-capture.md"
tags: [paypal, authorization, capture, delayed-capture, orders-api, payments-api]
---

## Summary

Integration guide for authorizing a PayPal payment and capturing it later using **Orders API v2** (authorize) and **Payments API v2** (capture). Change `intent` from `CAPTURE` to `AUTHORIZE` to reserve funds for up to 29 days. Builds on the [[source-paypal-payments-quickstart]] integration.

## Key takeaways

- **Create order**: `intent: "AUTHORIZE"` — reserves funds, does not charge
- **Capture later**: `POST /v2/payments/authorizations/{authorization_id}/capture`
- **Authorization ID location**: `purchase_units[0].payments.authorizations[0].id` in the order approval response — store immediately in database
- **Partial captures**: capture any amount up to the authorized total; useful for split shipments or partial fulfillment

## Authorization lifecycle

| Period | Duration | Notes |
| --- | --- | --- |
| Honor period | 3 days | Highest capture success rate; ship within this window |
| Extended | Days 4–29 | Use reauthorization to extend; lower success rate |
| Expiry | Day 29 | Authorization auto-expires; must create new order to charge |

Sandbox authorizations don't expire after 29 days — use negative testing to simulate expiry.

## Common use cases

- Pre-orders shipping in the future
- Made-to-order items (charge after production)
- Hotels/rentals (authorize at booking, capture at check-in/check-out)
- High-value item verification before charging

## Error codes

| Error code | HTTP status | Meaning |
| --- | --- | --- |
| `AUTHORIZATION_EXPIRED` | 422 | Authorization past 29-day window |
| `AUTHORIZATION_ALREADY_CAPTURED` | 422 | Already captured |

## Best practices

- Capture within the 3-day honor period for best success rates
- Store authorization creation date — alert when approaching day 29
- Void uncaptured authorizations promptly when order can't be fulfilled
- Communicate to customers that their payment is held but not yet charged
- Monitor authorization validity — banks or PayPal can void authorizations

## Related pages

- [[source-paypal-void-authorization]] — Void an authorization (cancel before capture)
- [[source-paypal-payments-quickstart]] — Base integration
- [[source-paypal-standard-payments]] — Authorization vs. capture overview

## Raw Sources

- [[paypal-delayed-capture]] — verbatim authorize and delay capture integration guide
