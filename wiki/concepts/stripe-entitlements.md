---
title: "Stripe Entitlements"
type: concept
category: framework
tags: [stripe, billing, entitlements, subscriptions, feature-flags, provisioning, webhooks]
---

## Overview

Stripe Entitlements is a feature-gating layer built into Stripe Billing. It lets you map internal product features to Stripe Products so that Stripe automatically tracks which customers should have access to which capabilities based on their active subscription status — without custom database tables or manual provisioning logic.

Core value prop: decouple pricing changes from code changes. When you restructure your plan tiers, you update product-feature mappings in Stripe rather than deploying new feature flag logic.

## Key objects

| Object | Description |
|---|---|
| `entitlements.feature` | A named capability with a unique `lookup_key`. Created once; referenced by product attachments. |
| `product_feature` | The join between a feature and a product. One feature can attach to many products. |
| `entitlements.active_entitlement` | A live entitlement for a customer. Exists as long as the customer has an active subscription to a product that includes the feature. |
| `entitlements.active_entitlement_summary` | The full entitlement snapshot for a customer; returned in webhook payloads and the polling API. |

## Lookup key

The `lookup_key` is the stable, code-facing identifier for a feature (e.g. `premium-support`, `advanced-reporting`). Rules:

- Unique per feature; cannot be changed after creation
- Can be reused only after the feature is archived
- Used in application code to gate feature access (check if `lookup_key` appears in customer's active entitlements)

## Provisioning lifecycle

1. Create features via `stripe.entitlements.features.create({ name, lookup_key })`
2. Attach to products via `stripe.products.createFeature(productId, { entitlement_feature: featureId })`
3. When customer subscribes → Stripe creates active entitlements
4. Listen to `entitlements.active_entitlement_summary.updated` webhook
5. **Grant**: feature present in `entitlements.data` → enable access
6. **Revoke**: feature absent from `entitlements.data` → disable access

## Billing period lag

Changes to product-feature mappings apply to **existing subscriptions at the start of their next billing period**, not immediately.

## Webhook: `entitlements.active_entitlement_summary.updated`

Fires whenever a customer's entitlements change (subscribe, upgrade, downgrade, cancel). Payload is the full current entitlement state.

- `entitlements.data`: up to **10 items** max. If customer has >10 active entitlements, use `entitlements.url` to fetch the full paginated list.
- `previous_attributes.entitlements.data`: prior state, useful for diffing what was added or removed.

## Polling API

```js
stripe.entitlements.activeEntitlements.list({ customer: customerId })
```

Returns paginated `active_entitlement` objects. Use for:
- Application startup (load entitlements on boot)
- Authorization checks (inline gating)
- Reconciliation after webhook delivery failure

Stripe recommends persisting entitlements locally for faster resolution.

## Feature management

| Operation | Behavior |
|---|---|
| Edit | Name and metadata editable; lookup key is immutable |
| Remove from product | Detaches; existing subscriber entitlements change at next billing period |
| Archive | Irreversible. Still generates entitlements on existing product attachments. Lookup key can be reused after archiving. |

## Sources

- [[source-stripe-billing-entitlements]] — Stripe docs: Entitlements guide (Dashboard + API tabs, full webhook payloads)
- [[source-stripe-billing-ios-sdk]] — BillingSDK for iOS: entitlement checking via hasEntitlement/getActiveEntitlements, change listener, unauthenticated behavior
