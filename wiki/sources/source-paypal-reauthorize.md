---
title: "PayPal: Extend an Authorization (Reauthorize)"
type: source
date_ingested: 2026-04-17
original_format: webpage
raw_files:
  - "paypal-reauthorize.md"
tags: [paypal, authorization, reauthorize, payments-api, delayed-capture]
---

## Summary

Integration guide for reauthorizing (extending) an existing PayPal authorization when fulfillment takes longer than the initial hold period. Uses **Payments API v2** (`/v2/payments/authorizations/{authorization_id}/reauthorize`). No customer re-approval required. Builds on the [[source-paypal-delayed-capture]] pattern.

## Key takeaways

- **Endpoint**: `POST /v2/payments/authorizations/{authorization_id}/reauthorize`
- Returns a **new authorization ID** (`newAuthorizationId`) — update the stored auth ID immediately
- Response also includes `expirationTime` for the new authorization
- Can reauthorize for up to **115% of original amount** (regional limits may vary)
- **No customer interaction required** — server-side only; notify customers as courtesy

## Authorization validity by region

| Region | Initial validity |
| --- | --- |
| United States | 3 days |
| Most other regions | Up to 29 days |

## Reauthorization constraints

| Constraint | Detail |
| --- | --- |
| Timing window | Days 4–29 only (too soon or too late both fail) |
| Single use | Each authorization can be reauthorized **once only** |
| Amount limit | Up to 115% of original authorized amount |
| Expiry fallback | Void and create new order if reauthorization fails or window passes |

## Error codes

| Error code | Meaning |
| --- | --- |
| `AUTHORIZATION_ALREADY_COMPLETED` | Already captured or voided |
| `REAUTHORIZE_NOT_ALLOWED` | Attempted before day 4 or after day 29 |

## Best practices

- Monitor authorization creation dates; trigger reauthorization before day 29
- Update stored authorization ID to `newAuthorizationId` after successful reauthorization
- If reauthorization fails, void original authorization and request new payment from customer
- Test using sandbox "time machine" to simulate 4+ day old authorizations

## Related pages

- [[source-paypal-delayed-capture]] — Base authorize-then-capture pattern
- [[source-paypal-void-authorization]] — Voiding if reauthorization fails or not needed
- [[source-paypal-bopis]] — BOPIS pattern that may need reauthorization for unclaimed orders

## Raw Sources

- [[paypal-reauthorize]] — verbatim reauthorization integration guide
