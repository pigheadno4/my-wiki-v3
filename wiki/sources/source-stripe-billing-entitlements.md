---
title: "Stripe Billing — Entitlements"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-billing-entitlements-2026.md"
tags: [stripe, billing, entitlements, subscriptions, feature-flags, provisioning]
---

## Summary

Stripe Entitlements is a feature-gating system built into Stripe Billing. It lets you map internal product features to Stripe Products, then have Stripe automatically track which customers are entitled to which features based on their active subscription status.

## Key concepts

- **Feature**: a named capability with a unique `lookup_key` (e.g. `premium-support`, `advanced-reporting`). The lookup key is the stable identifier used to gate access in application code.
- **Product-feature attachment**: a feature can be attached to multiple products. When a customer subscribes to a product, they gain entitlements to all attached features.
- **Active entitlement**: an `entitlements.active_entitlement` object that is live as long as the customer maintains an active subscription for the corresponding product.

## Billing period lag

Existing subscriptions pick up product-feature mapping changes at the **start of the next billing period**, not immediately.

## Provisioning workflow

1. Create features via API (`stripe.entitlements.features.create`) or Dashboard.
2. Attach features to products (`stripe.products.createFeature`).
3. Listen for `entitlements.active_entitlement_summary.updated` webhook to drive provisioning:
   - **Grant access**: feature appears in `entitlements.data`
   - **Revoke access**: feature is absent from `entitlements.data`

## Webhook: `entitlements.active_entitlement_summary.updated`

Fires on any entitlement change: subscribe, upgrade, downgrade, cancel. The payload is an `entitlements.active_entitlement_summary` object containing the customer's **full, up-to-date** entitlement list.

- `entitlements.data` max 10 items in summary payload — use `entitlements.url` for the full paginated list if customer has more than 10 active entitlements.
- `previous_attributes.entitlements.data` shows what changed (useful for diffing).

## Polling API

```js
stripe.entitlements.activeEntitlements.list({ customer: '{{CUSTOMER_ID}}' })
```

Returns paginated `entitlements.active_entitlement` objects. Use for startup checks, authorization gates, or reconciliation after webhook delivery failure. Stripe recommends persisting entitlements locally for faster resolution.

## Feature management

| Action | Notes |
|---|---|
| Edit feature | Can change name and metadata; **lookup key cannot be changed after creation** |
| Remove from product | Detaches feature; existing subscribers unaffected until next billing period |
| Archive feature | Irreversible. Archived features still generate entitlements on existing products. Archived lookup key can be reused. |

## Related pages

- [[stripe-entitlements]] — concept page
- [[stripe]] — company page
- [[stripe-subscriptions]] — subscriptions overview

## Raw Sources

- [[stripe-billing-entitlements-2026]] — verbatim Stripe docs webpage
