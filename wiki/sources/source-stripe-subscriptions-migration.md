---
title: "Stripe — Migrate Subscriptions to Stripe Billing"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-subscriptions-migration-2026.md"
tags: [stripe, subscriptions, migration, zuora, recurly, chargebee, pan-import, billing-toolkit]
---

## Summary

Overview and decision matrix for migrating subscriptions to Stripe Billing from third-party systems (Zuora, Recurly, Chargify, Chargebee, in-house) or another Stripe account.

## Two Migration Methods

- **Billing migration toolkit**: no-code
- **Stripe APIs**: manual scripts

## Three Migration Stages

1. Set up Stripe Billing integration
2. Migrate customer + payment data (PAN import from external processor, or PAN copy for Stripe-to-Stripe)
3. Import subscriptions via toolkit

## Decision Matrix

| Data location | Source | Steps |
| --- | --- | --- |
| External system | Third party | Set up → PAN import → toolkit |
| Already in Stripe | Third party | Set up → toolkit |
| External system | Another Stripe account | Set up → copy PAN self-serve → toolkit |
| Already in Stripe | Another Stripe account | Set up → copy PAN self-serve → toolkit |

## Related Pages

- [[stripe-subscriptions]] — concept page

## Raw Sources

- [[stripe-subscriptions-migration-2026]] — verbatim migration overview (50 lines)
