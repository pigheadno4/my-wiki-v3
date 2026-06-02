---
title: "Stripe Subscriptions — Bill Customers in Advance (Prebilling)"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-prebilling-2026.md"
tags: [stripe, billing, subscriptions, prebilling, flexible-billing, preview]
---

## Summary

Guide to Stripe's prebilling feature (public preview) — bill customers now for multiple future service periods. Requires `billing_mode=flexible` and API version `2025-09-30.preview` or later.

## Concept

Prebilling charges customers upfront for future service periods rather than the standard one-period-at-a-time billing. Use cases:
- Monthly subscription, prebill first 45 days
- Renewal is 7 days away — send the invoice now
- Prebill for next 2 months at renewal

## Requirements

- `billing_mode=flexible`
- API version `2025-09-30.preview` or later

## Key API parameters

`billing_schedules[]` on Create/Update Subscription:
- `applies_to[]` — array of `{type: "price", price: "price_xxx"}` to target specific prices; omit to apply to all licensed items
- `bill_until.type` — `duration` (relative from billing cycle start) or `timestamp` (exact Unix timestamp)
- `bill_until.duration.interval` / `interval_count` — e.g. `month` + `2` for 2 months

`proration_behavior`:
- `always_invoice` → generate invoice immediately
- `create_prorations` → generate at next billing cycle date

## End date constraints

- **Minimum**: at least 1 cycle of the shortest billing period (e.g. monthly subscription → at least 1 month)
- **Maximum**: at most 12 cycles of the shortest billing period (e.g. monthly → at most 12 months)

## 8 limitations (public preview)

1. Not available for subscription schedules or schedule-backed subscriptions
2. Only `percent_off` coupons with `duration=once` or `forever`
3. Applied immediately on create/update when `billing_schedules` is configured
4. Cannot use on subscriptions migrated from classic → flexible billing mode
5. Cannot prebill if ALL items are usage-based; `usage_type=metered` prices are always excluded
6. `proration_behavior` cannot be `none`
7. If subscription has a scheduled cancellation, prebilling cannot extend beyond that date
8. Cannot use with `payment_behavior=pending_if_incomplete`

## Preview before committing

```bash
POST /v1/invoices/create_preview
subscription_details.billing_schedules=...
```

Returns the prebilling invoice before any subscription changes are applied.

## Related pages

- [[stripe-subscriptions-prebilling]] — concept page
- [[stripe-subscriptions]] — concept page
- [[source-stripe-subscriptions-billing-mode]] — flexible billing mode (prerequisite)
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-prebilling-2026]] — verbatim Stripe docs webpage
