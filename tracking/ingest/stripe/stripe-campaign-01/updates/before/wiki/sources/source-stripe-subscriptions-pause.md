---
title: "Stripe Subscriptions — Pause Subscriptions"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-pause-2026.md"
tags: [stripe, billing, subscriptions, pause, flexible-billing, webhooks]
---

## Summary

Guide to the "true pause" endpoint (`POST /v1/subscriptions/:id/pause`) introduced with flexible billing mode. Distinct from pause payment collection. Halts both service delivery and invoice generation.

## Three pause-like behaviors compared

| Behavior | Invoices generated? | Service delivery? | Trigger |
|---|---|---|---|
| **True pause** (this page) | No | Halted | Manual API call; flexible billing only |
| Pause payment collection | Yes (not collected) | Continues | Manual API |
| Trial-end pause | No | Halted | System-triggered (no PM at trial end) |

## Requirements

- `billing_mode=flexible` — mandatory
- `collection_method=charge_automatically`
- Subscription must not be: `send_invoice`, classic billing mode, in trial, already paused/incomplete/canceled, attached to schedule or cadence

## Pause behavior

- Status → `paused` immediately
- `current_period_end` updated to pause timestamp
- Invoice generation halted for pause duration (existing invoices still advance)
- `bill_for` parameter controls billing at pause time:
  - Credit prorations for unused licensed time
  - Debits for metered usage in current period
  - `invoicing_behavior`: `pending_invoice_item` or immediate invoice

```bash
POST /v1/subscriptions/sub_xxx/pause
Stripe-Version: preview

bill_for[unused_time_from][type]=now
bill_for[outstanding_usage_through][type]=now
invoicing_behavior=pending_invoice_item
```

**Coupon behavior**: pause doesn't extend coupon duration — coupon retains original validity window.

**Customer portal**: displays paused state but customers cannot self-pause.

## Cannot pause if subscription has

- `send_invoice` collection method
- `billing_mode=classic`
- Active trial or active trial offer
- Status: `paused`, `incomplete`, `incomplete_expired`, or `canceled`
- Attached subscription schedule
- Attached cadence

Cannot attach schedule or cadence to a paused subscription either.

## Resume behavior

```bash
POST /v1/subscriptions/sub_xxx/resume
Stripe-Version: preview

billing_cycle_anchor=unchanged
proration_behavior=create_prorations
```

- Manual only — no auto-resume
- `charge_automatically` only
- If no invoice generated → status → `active` immediately
- If resume invoice generated:
  - Finalized immediately
  - Payment NOT attempted automatically — must call `POST /v1/invoices/:id/pay`
  - Paid or uncollectible → `active`
  - Payment fails → `past_due`
  - Void invoice before payment → stays `paused`
  - No payment within **23 hours** → Stripe voids invoice, stays `paused`

## Webhooks

| Event | When |
|---|---|
| `customer.subscription.paused` | Subscription pauses |
| `customer.subscription.resumed` | Subscription resumes |
| `customer.subscription.updated` | Either pause or resume |
| `entitlements.active_entitlement_summary.updated` | Entitlements change due to pause/resume |

## Related pages

- [[stripe-subscriptions-pause]] — concept page
- [[stripe-subscriptions-cancel]] — cancellation patterns
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-pause-2026]] — verbatim Stripe docs webpage
