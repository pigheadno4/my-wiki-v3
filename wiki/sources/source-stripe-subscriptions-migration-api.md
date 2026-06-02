---
title: "Stripe — Migrate Subscriptions Using Stripe APIs"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-subscriptions-migration-api-2026.md"
tags: [stripe, subscriptions, migration, api, subscription-schedules, legacy-pricing, test-clocks]
---

## Summary

API-based subscription migration guide. Covers legacy pricing patterns, Subscription Schedules API (recommended for migration), mid-cycle continuity, and sandbox test clock verification.

## Key Patterns

**Legacy pricing**: create placeholder product (`products.create({ id, name: 'Legacy plan', metadata: { OLD_PRODUCT_ID } })`) → use `items.price_data` when creating subscriptions (overrides existing price).

**Use Subscription Schedules API** (not Subscriptions API) — only way to start monthly subscriptions >30 days in future; provides `phases` for granular coupon/tax/collection settings per interval.

**Mid-cycle continuity**: map `billing_cycle_anchor` + `start_date` to match remaining term (e.g., customer with 6 months left on yearly sub).

**Test with test clocks**: simulate subscriptions advancing through time in sandbox before live mode.

**Confirm migration**: `stripe.subscriptions.list({ created: { gt: timestamp } })`

## Related Pages

- [[stripe-subscriptions]] — concept page
- [[source-stripe-subscriptions-migration-toolkit]] — toolkit (no-code) migration

## Raw Sources

- [[stripe-subscriptions-migration-api-2026]] — verbatim API migration guide (160 lines)
