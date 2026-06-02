---
title: "PayPal: Split Shipments"
type: source
date_ingested: 2026-04-17
original_format: webpage
raw_files:
  - "paypal-split-shipments.md"
tags: [paypal, split-shipments, orders-api, purchase-units, shipping]
---

## Summary

Integration guide for shipping items from a single PayPal order to multiple addresses. Uses multiple `purchase_units` in a single `POST /v2/checkout/orders` request, each with its own `shipping.address`. Customer pays once; each unit ships independently.

## Key takeaways

- **Endpoint**: `POST /v2/checkout/orders` with multiple `purchase_units`
- Each purchase unit has its own `reference_id`, `amount`, and `shipping.address`
- Amounts are independent per unit — set each unit's amount for its shipment leg
- `reference_id` (e.g. `"SHIPMENT_1"`) used to track and identify each leg
- Works with `intent: "CAPTURE"` for immediate payment
- No additional API calls beyond the standard orders flow — the multi-address logic is entirely in the order creation payload

## Example structure

```json
{
  "intent": "CAPTURE",
  "purchase_units": [
    { "reference_id": "SHIPMENT_1", "amount": {...}, "shipping": { "address": {...} } },
    { "reference_id": "SHIPMENT_2", "amount": {...}, "shipping": { "address": {...} } }
  ]
}
```

## Use cases

- Holiday gifts to different recipients
- Corporate orders to multiple office locations
- Drop shipping to different addresses

## Related pages

- [[source-paypal-payments-quickstart]] — Base integration
- [[source-paypal-standard-payments]] — Standard payments overview

## Raw Sources

- [[paypal-split-shipments]] — verbatim split shipments integration guide
