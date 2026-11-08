---
title: "Stripe — Compare Classic and Flexible Billing Mode"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-billing-mode-compare-2026.md"
tags: [stripe, subscriptions, flexible-billing, billing-mode, prorations, usage-based, mixed-intervals]
---

## Summary

Detailed classic vs flexible billing mode comparison across 10 behavioral areas. Essential reference before migrating from classic to flexible.

## Key Differences

| Area | Classic | Flexible |
| --- | --- | --- |
| **Credit prorations** | Uses current price/tax/quantity | Uses original debited amount; multiple credits if multi-debit period |
| **Discount on prorations** | Evenly distributed | Proportional per item |
| **Usage $0 line items** | Created | Suppressed; no invoice if empty |
| **Usage billing price** | Most recent price only | Price at time of reporting |
| **Unbilled usage on removal** | No invoice item (API); invoice only (schedule) | Invoice item based on `proration_behavior` |
| **Billing cycle anchor auto-reset** | On interval change, $0→paid, cancel_at | Never automatically reset |
| **Schedule phase transitions** | Two invoices | Single consolidated invoice |
| **Customer Portal cancellation** | `cancel_at_period_end=true`, `cancel_at` tracks period | `cancel_at_period_end=false`, fixed `cancel_at` |
| **`trial_start` on re-trials** | Always first trial start | Most recent trial start |
| **`trial_end` + `cancel_at`** | `cancel_at` < `trial_end` overwrites `trial_end` | `cancel_at` never alters `trial_end` |
| **Mixed intervals** | Not supported | Supported (monthly + annual on same sub) |
| **Pending invoice items** | Only when proration_behavior ≠ always_invoice | Always included |

## Related Pages

- [[stripe-subscriptions]] — concept page
- [[source-stripe-subscriptions-billing-mode]] — billing mode guide (how to enable/migrate)

## Raw Sources

- [[stripe-subscriptions-billing-mode-compare-2026]] — verbatim comparison guide (218 lines)
