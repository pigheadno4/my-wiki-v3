---
title: "PayPal: Buy Online, Pick Up In Store (BOPIS)"
type: source
date_ingested: 2026-04-17
original_format: webpage
raw_files:
  - "paypal-bopis.md"
tags: [paypal, bopis, authorization, capture, retail, omnichannel]
---

## Summary

Integration guide for Buy Online, Pick Up In Store (BOPIS) payments using PayPal. Authorizes payment at checkout and captures funds only after verifying customer pickup. Uses `intent: "AUTHORIZE"` with a pickup code stored in `custom_id`, then captures via `AuthorizationsCaptureRequest` after pickup verification. Builds on the [[source-paypal-delayed-capture]] pattern.

## Key takeaways

- **Flow**: Authorize at checkout → store pickup code in `custom_id` → verify customer at pickup → capture
- Capture endpoint: `POST /v2/payments/authorizations/{auth_id}/capture`
- `custom_id` field on `purchase_units` used to store pickup code (e.g. `"PICKUP-PICK789"`)
- **Never capture before pickup verification** — protects against fraud
- Partial pickups: capture the available amount, void the remainder

## Pickup verification

Verify customer identity before capturing — acceptable methods:
- Order number + pickup code
- Photo ID
- App confirmation

Capture returns `status: "PICKED_UP"` and `captureId` on success.

## Typical hold windows

| Scenario | Recommended hold |
| --- | --- |
| Retail / click-and-collect | 7 days |
| Restaurants / groceries | 24 hours |

Auto-void unclaimed orders when the hold window expires.

## Monitoring targets

| Metric | Target |
| --- | --- |
| Authorization success rate | 95% |
| Capture success at pickup | 90% |
| Authorization expiration rate | <15% (higher than standard due to unclaimed orders) |
| Void success rate (abandoned) | 98% |

## Error codes

| Error code | HTTP status | Meaning |
| --- | --- | --- |
| `AUTHORIZATION_EXPIRED` | 422 | Hold window expired |
| `AUTHORIZATION_ALREADY_CAPTURED` | 422 | Already picked up |

## Related pages

- [[source-paypal-delayed-capture]] — General authorize-then-capture pattern this builds on
- [[source-paypal-void-authorization]] — Voiding abandoned BOPIS orders
- [[source-paypal-payments-quickstart]] — Base integration

## Raw Sources

- [[paypal-bopis]] — verbatim BOPIS integration guide
