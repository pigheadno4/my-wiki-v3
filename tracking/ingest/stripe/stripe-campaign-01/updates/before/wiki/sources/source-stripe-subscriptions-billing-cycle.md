---
title: "Stripe — Set the Subscription Billing Renewal Date"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-subscriptions-billing-cycle-2026.md"
tags: [stripe, subscriptions, billing-cycle, billing-cycle-anchor, proration, trial]
---

## Summary

Comprehensive guide to billing cycle anchors. Two methods for new subscriptions, two for changing existing ones. Covers proration behavior, Checkout limitations, and auto-reset scenarios.

## `billing_cycle_anchor_config` (recommended for monthly/yearly)

```js
{ day_of_month: 31 }         // end of month (handles short months)
{ month: 7, day_of_month: 1 } // July 1 for yearly
{ day_of_month: 15, hour: 12, minute: 30, second: 0 }  // align with existing sub
```
- Defaults unspecified h/m/s to creation time; UTC
- Cannot use with backdated start dates
- May set anchor >1 period in future — but first invoice always within 1 period

## `billing_cycle_anchor` (all intervals including daily/weekly)

Direct Unix timestamp on create or update.

## Change Existing Billing Period

**Reset to now**: `update({ billing_cycle_anchor: 'now', proration_behavior: 'create_prorations' })`

**Via trial**: `update({ trial_end: timestamp, proration_behavior: 'none' })` → sets anchor to trial end date

## Auto-Reset Scenarios

Anchor resets when: switching to price with different `recurring.interval`; `cancel_at` is before next renewal + anchor in future of new `cancel_at`.

**`billing_mode[type]=flexible`**: billing cycle anchor stays unchanged when billing period changes.

## Proration Behavior

Default: creates prorated invoice for period between creation and first full invoice. `proration_behavior: 'none'` → initial period free, no invoice until first full billing period.

**Checkout limitation**: cannot combine trial with billing cycle anchor.

## Related Pages

- [[stripe-subscriptions]] — concept page

## Raw Sources

- [[stripe-subscriptions-billing-cycle-2026]] — verbatim billing cycle anchor guide (303 lines)
