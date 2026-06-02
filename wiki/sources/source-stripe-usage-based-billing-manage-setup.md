---
title: "Stripe: Manage Your Usage-Based Billing Setup"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-usage-based-billing-manage-setup-2025.md"
tags: [stripe, billing, usage-based, subscriptions, pricing, cancellation]
---

## Summary

Covers post-setup management tasks for UBB: transform_quantity for package pricing, mid-cycle price updates (flexible vs classic behavior), backdated subscriptions, and cancellation.

## Key Details

**Transform quantity** — divide reported usage before pricing:

```js
transform_quantity: { divide_by: 60, round: 'up' }
```

Not compatible with tiered pricing.

**Mid-cycle price updates:**

| Mode | Behavior on price change |
| --- | --- |
| `billing_mode=flexible` | Creates invoice item for prior metered usage immediately. `proration_behavior='none'` skips billing the removed price. |
| `billing_mode=classic` | Only usage after the update is billed at new price. Pre-update usage is lost unless you re-report it or reset `billing_cycle_anchor=now`. |

Classic exception: threshold invoices issued at old price are still charged; they don't offset end-of-period usage at the new price.

Adding a new subscription item mid-period (classic): only usage from the add date is captured.

**Backdated subscriptions** — record usage before subscription exists, then create subscription with `backdate_start_date` (Unix timestamp):
- Flexible: backdated usage appears on first invoice
- Classic: backdated usage appears on next cycle invoice

**Cancellation**:
- No proration supported with UBB
- Canceled subscriptions can't be reactivated — create a new subscription
- `cancel_at_period_end=true` can be reversed by setting it to `false` before period end
- Final invoice on cancellation includes all metered usage from last billing period

## Raw Sources

- [[stripe-usage-based-billing-manage-setup-2025]] — verbatim webpage content (138 lines)
