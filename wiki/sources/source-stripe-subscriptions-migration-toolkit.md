---
title: "Stripe — Billing Migration Toolkit"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-subscriptions-migration-toolkit-2026.md"
tags: [stripe, subscriptions, migration, billing-toolkit, csv, subscription-schedule, pan-import]
---

## Summary

Full guide for the no-code Billing migration toolkit. Covers three CSV template types, migration timing, Subscription Schedule-based buffering, cancel window, validation error resolution, and use-case examples.

## Three CSV Templates

| Template | Key fields |
| --- | --- |
| Basic | `customer`, `start_date`, `price`, `quantity`, `billing_cycle_anchor`, `trial_end`, `backdate_start_date`, `coupon` |
| Multi-price items | `items.0.price`, `items.1.price`, `items.N.quantity`, `add_invoice_items.0.{amount,product,currency}` |
| Ad-hoc pricing | `adhoc_items.0.{amount, product, interval, currency}` |

## Key Constraints

- `start_date` must be ≥24h in future (≥1h in sandbox)
- `backdate_start_date` requires `proration_behavior: none`
- CSV file limit: 120 MB
- `metadata.source: internal:Stripe` for Stripe-to-Stripe migrations

## Timing Advice

Create new subscriptions in Stripe **before** canceling old ones (avoid missing billing period). Cancel old system subscriptions before their charge date (avoid double billing). For close billing dates, schedule after the cycle.

## Migration Uses Subscription Schedules

24-hour buffer before subscriptions go live (1 hour in sandbox). **10-hour cancel window** from scheduling. After 10h, must cancel via API or Dashboard individually.

## Validation Error Resolution

Download error file → check `processing_error` column → fix → re-upload. Common errors: non-epoch dates, start_date <24h, missing required fields, incompatible price/tax `tax_behavior`.

## Related Pages

- [[stripe-subscriptions]] — concept page
- [[source-stripe-subscriptions-migration]] — migration overview

## Raw Sources

- [[stripe-subscriptions-migration-toolkit-2026]] — verbatim toolkit guide (459 lines)
