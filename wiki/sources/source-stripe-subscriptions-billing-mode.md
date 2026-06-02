---
title: "Stripe — Flexible Billing Mode for Subscriptions"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-billing-mode-2026.md"
tags: [stripe, subscriptions, flexible-billing, billing-mode, proration-discounts, api-version]
---

## Summary

Comprehensive guide to flexible vs classic billing mode. Covers API version defaults, migration API, proration discounts, subscription schedule inheritance, and Dashboard default settings.

## Key Facts

- **Cannot migrate back** from flexible to classic
- **Requires API 2025-06-30.basil+** to use flexible programmatically
- **API default**: `2025-09-30.clover`+ → flexible; earlier → classic
- Flexible unlocks: mixed intervals, accurate prorations, new trial settings

## Migration API

```js
stripe.subscriptions.migrate('sub_xxx', { billing_mode: { type: 'flexible' } })
```
- Flexible behaviors apply to new activity only (pre-migration resources not recalculated)

## Proration Discounts

`billing_mode.flexible.proration_discounts`:
- `itemized` (recommended): gross amounts + accurate discount line items
- `included` (default): net amount, zero discount amounts (backward compat)

## Subscription Schedule Inheritance

Don't set `billing_mode` when using `from_subscription` — schedule inherits from existing subscription. Setting `billing_mode` with `from_subscription` returns an error.

## Dashboard Default Setting

3 options: Classic default, Flexible default, Flexible-only (hide classic). Applies to Dashboard-created subs, Payment Links, and Pricing Tables. Does not affect API-created subs.

## Related Pages

- [[stripe-subscriptions]] — concept page (updated with billing mode migration details)

## Raw Sources

- [[stripe-subscriptions-billing-mode-2026]] — verbatim billing mode guide (966 lines, includes full API response examples)
