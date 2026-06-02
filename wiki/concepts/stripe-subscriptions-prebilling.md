---
title: "Stripe Subscription Prebilling"
type: concept
category: framework
tags: [stripe, billing, subscriptions, prebilling, flexible-billing, preview]
---

## Overview

Prebilling (public preview) lets you charge customers now for multiple future service periods — bill upfront for 2 months, send a renewal invoice early, or cover a custom date range. Requires `billing_mode=flexible` and API version `2025-09-30.preview` or later.

## Prerequisites

- `billing_mode=flexible` — required; cannot use on subs migrated classic → flexible
- API version `2025-09-30.preview` or later

## How it works

Set `billing_schedules[]` on Create or Update Subscription:

```bash
billing_schedules[0][applies_to][0][type]=price
billing_schedules[0][applies_to][0][price]={{PRICE_ID}}   # omit to apply to all licensed items
billing_schedules[0][bill_until][type]=duration             # or "timestamp"
billing_schedules[0][bill_until][duration][interval]=month
billing_schedules[0][bill_until][duration][interval_count]=2
```

`proration_behavior` controls invoice timing:
- `always_invoice` — invoice generated immediately
- `create_prorations` — invoice generated at next billing cycle

## End date rules

| Constraint | Rule |
|---|---|
| Minimum | At least 1 full cycle of the shortest billing period on the subscription |
| Maximum | At most 12 cycles of the shortest billing period |

Example: monthly subscription → minimum 1 month, maximum 12 months.

## Item-level scoping

- `applies_to[]` — target specific prices by ID
- Omit `applies_to` → all licensed (non-usage-based) items are prebilled
- Usage-based (`usage_type=metered`) prices are always excluded from prebilling
- Cannot set `applies_to[price]` on a metered price

## `bill_until` types

| Type | Parameters | When to use |
|---|---|---|
| `duration` | `interval` + `interval_count` | Relative from billing cycle start (e.g. 2 months) |
| `timestamp` | Unix timestamp | Exact end date |

## Limitations (public preview)

1. Not available for subscription schedules or schedule-backed subscriptions
2. Only `percent_off` coupons with `duration=once` or `forever`
3. Applied immediately on create/update when `billing_schedules` is configured
4. Cannot use on subscriptions migrated from classic → flexible billing mode
5. Cannot prebill if ALL items are usage-based
6. `proration_behavior` cannot be `none`
7. If subscription has scheduled cancellation, prebilling cannot extend past that date
8. Cannot use with `payment_behavior=pending_if_incomplete`

## Preview before committing

Use `POST /v1/invoices/create_preview` with `subscription_details.billing_schedules` to preview the prebilling invoice before applying changes to the subscription.

## Use cases

- Send renewal invoice 7 days early (before the billing date)
- Monthly subscription: prebill for 45 days at signup
- Annual subscription: collect 2 years upfront

## Sources

- [[source-stripe-subscriptions-prebilling]] — Stripe docs: prebilling guide (public preview, billing_schedules API, limitations, invoice timing)
