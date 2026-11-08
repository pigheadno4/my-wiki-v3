---
title: "Stripe Subscription Pause (True Pause)"
type: concept
category: framework
tags: [stripe, billing, subscriptions, pause, flexible-billing, webhooks]
---

## Overview

Stripe's "true pause" (`POST /v1/subscriptions/:id/pause`) halts both service delivery AND invoice generation for a subscription. Requires `billing_mode=flexible`. Distinct from two other pause-like behaviors that existed before this endpoint.

## Three pause behaviors compared

| Behavior | Invoice generated? | Service delivery? | How triggered |
|---|---|---|---|
| **True pause** (`/pause` endpoint) | No | Halted | Manual API; flexible billing only |
| Pause payment collection | Yes (not collected) | Continues | Manual API |
| Trial-end pause (no payment method) | No | Halted | System-triggered at trial end |

## Prerequisites

- `billing_mode=flexible` — required
- `collection_method=charge_automatically`

## Blocking conditions (cannot pause if)

- `collection_method=send_invoice`
- `billing_mode=classic`
- Active trial period or active trial offer
- Status already: `paused`, `incomplete`, `incomplete_expired`, or `canceled`
- Subscription has attached schedule or cadence

Cannot attach a schedule or cadence to a paused subscription either.

## Pause API

```bash
POST /v1/subscriptions/:id/pause
Stripe-Version: preview
```

Key parameters:
- `bill_for[unused_time_from][type]` — credit proration for unused licensed time
- `bill_for[outstanding_usage_through][type]` — debit for metered usage in current period
- `invoicing_behavior` — `pending_invoice_item` (accumulate) or immediate invoice

Effects:
- Status → `paused` immediately
- `current_period_end` → pause timestamp
- Invoice generation halted; existing invoices still advance

**Coupon behavior**: pause does NOT extend coupon duration — coupon retains original validity.

**Customer portal**: displays paused status; customers cannot self-pause.

## Resume API

```bash
POST /v1/subscriptions/:id/resume
Stripe-Version: preview
```

Key parameters: `billing_cycle_anchor`, `proration_behavior`

- Only available with `charge_automatically`
- Manual only — no auto-resume

### Resume invoice flow

| Scenario | Result |
|---|---|
| No invoice generated | Status → `active` immediately |
| Invoice generated, paid | Status → `active` |
| Invoice generated, marked uncollectible | Status → `active` |
| Invoice generated, payment fails | Status → `past_due` |
| Invoice voided before payment | Stays `paused` |
| No payment within 23 hours | Stripe voids invoice; stays `paused` |

Resume does NOT auto-attempt payment — must call `POST /v1/invoices/:id/pay` separately.

## Webhooks

| Event | Trigger |
|---|---|
| `customer.subscription.paused` | Subscription pauses |
| `customer.subscription.resumed` | Subscription resumes |
| `customer.subscription.updated` | Either pause or resume |
| `entitlements.active_entitlement_summary.updated` | Entitlements change due to pause/resume |

## Use cases

- Retention flows: pause instead of cancel for vacation or temporary non-usage
- Support tooling: API-controlled lifecycle without cancellation
- Billing validation: test entitlement revocation and webhook handling for paused windows

## Pause payment collection (distinct feature)

`pause_collection` on a subscription stops payment collection while **invoices still generate and service delivery continues**. Three behaviors:

| Behavior | Invoice handling |
|---|---|
| `void` | Immediately voided; customer never charged |
| `keep_as_draft` | Stays draft, `auto_advance=false`; collect later by setting `auto_advance=true` |
| `mark_uncollectible` | Marked uncollectible (unless customer balance covers full amount → `paid`) |

Unset: `stripe.subscriptions.update(id, { pause_collection: '' })` — only affects future invoices.

Pre-pause invoices: still retried unless manually voided.

## Sources

- [[source-stripe-subscriptions-pause]] — Stripe docs: true pause endpoint (flexible billing only, bill_for, resume flow, webhooks)
- [[source-stripe-subscriptions-pause-payment]] — pause payment collection: 3 behaviors (void/keep_as_draft/mark_uncollectible), resumes_at, unpausing, schedule interaction
