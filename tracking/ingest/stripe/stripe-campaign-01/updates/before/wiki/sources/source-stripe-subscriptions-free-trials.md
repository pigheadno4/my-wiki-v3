---
title: "Stripe — Free Trial Periods on Subscriptions (Legacy trial_end)"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-subscriptions-free-trials-2026.md"
tags: [stripe, subscriptions, free-trials, legacy, trial-end, trial-period-days, pause, resume]
---

## Summary

**Legacy** — new integrations should use Trial Offers API. Documents `trial_end`/`trial_period_days` free trials, `missing_payment_method` behavior (cancel/pause/create_invoice), resume flow, and combining trials with billing cycle anchors.

## Key Facts

- `trial_end` (Unix timestamp) OR `trial_period_days` (integer); max 730 days
- No payment method required; $0 invoice created with "Free trial" description
- End early: `update({ trial_end: 'now' })`
- Usage during trial: not billed but viewable in meter event summary

## `missing_payment_method` Options

- `cancel` — subscription cancels at trial end
- `pause` — subscription pauses; resumes when PM added; supports customer portal, Hosted Invoice Page, Dashboard, API resume endpoint
- `create_invoice` — invoices at trial end; goes `past_due` without PM

**Checkout**: use `payment_method_collection: 'if_required'`

## Paused Subscription Resume

API `resume` endpoint; 23-hour window for invoice payment before auto-void. `billing_cycle_anchor: now` (default) starts new cycle; `unchanged` prorates.

## Combine with `billing_cycle_anchor`

`trial_end` + `billing_cycle_anchor` = free period → prorated period → fixed billing cycle.

## `trial_start` with Flexible Billing

With `billing_mode: flexible` + API 2025-04-30, `trial_start` reflects most recent trial (not first).

## Related Pages

- [[stripe-subscriptions]] — concept page
- [[stripe-subscriptions-trial-offers]] — new Trial Offers API (recommended)

## Raw Sources

- [[stripe-subscriptions-free-trials-2026]] — verbatim legacy free trials guide (489 lines)
