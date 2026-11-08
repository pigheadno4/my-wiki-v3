---
title: "Stripe Billing — Entitlements"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/entitlements"
raw_files:
  - "stripe-billing-entitlements-2026.md"
tags: [stripe, billing, entitlements, subscriptions, feature-flags, provisioning]
---

## Summary

As documented in Stripe's 2026-05-13 Dashboard and API guide, Stripe Entitlements maps internal product features to Stripe Products and tracks customer entitlements through subscriptions. The guide assumes Stripe Subscription and Customer resources; the application uses entitlement events or a list check to provision access.

## Key concepts

- **Feature**: a named capability with a unique `lookup_key` (e.g. `premium-support`, `advanced-reporting`). The lookup key is the stable identifier used to gate access in application code.
- **Product-feature attachment**: a feature can be attached to multiple products. When a customer subscribes to a product, they gain entitlements to all attached features.
- **Active entitlement**: an `entitlements.active_entitlement` object that is live as long as the customer maintains an active subscription for the corresponding product.

## Billing period lag

In the 2026-05-13 Dashboard and API guide, existing subscriptions pick up product-feature mapping changes at the **start of the next billing period**, not immediately.

## Provisioning workflow

1. Create features via API (`stripe.entitlements.features.create`) or Dashboard.
2. Attach features to products (`stripe.products.createFeature`).
3. Listen for `entitlements.active_entitlement_summary.updated` webhook to drive provisioning:
   - **Grant access**: feature appears in `entitlements.data`
   - **Revoke access**: reconcile against the complete active-entitlement list before disabling a feature absent from `entitlements.data` when the summary may be truncated (up to 10 entries); use `entitlements.url` to fetch all pages for a customer with more than 10 active entitlements. Absence from a capped summary alone is not proof of revocation.

## Webhook: `entitlements.active_entitlement_summary.updated`

In the 2026-05-13 API variant, this event is used when entitlements change through subscription creation, updates, or cancellation. Its `entitlements.active_entitlement_summary` payload contains a current summary, but `entitlements.data` is capped at 10 items and may omit active features.

- `entitlements.data` max 10 items in summary payload — use `entitlements.url` for the complete paginated list if the customer has more than 10 active entitlements.
- `previous_attributes.entitlements.data` shows what changed (useful for diffing).

## Polling API

```js
stripe.entitlements.activeEntitlements.list({ customer: '{{CUSTOMER_ID}}' })
```

In the 2026-05-13 API variant, this returns paginated `entitlements.active_entitlement` objects. Use for startup checks, authorization gates, or reconciliation after webhook delivery failure. Stripe recommends persisting entitlements locally for faster resolution.

## Feature management

The following management limits come from the 2026-05-13 Dashboard variant.

| Action | Notes |
|---|---|
| Edit feature | Can change name and metadata; **lookup key cannot be changed after creation** |
| Remove from product | Detaches feature; existing subscribers unaffected until next billing period |
| Archive feature | Irreversible. Archived features still generate entitlements on existing products. Archived lookup key can be reused. |

## Related pages

- [[stripe-entitlements]] — concept page
- [[stripe]] — company page
- [[stripe-subscriptions]] — subscriptions overview

## Related raw API references

- [[raw/stripe-billing-entitlements-2026-11-07|2026-11-07 variant index]] — links to Dashboard and API variants; their current contents were not captured here.

## Raw Sources

- [[raw/stripe-billing-entitlements-2026|2026-05-13 Entitlements guide]] — fully captured Dashboard and API variants behind the dated summary above.
