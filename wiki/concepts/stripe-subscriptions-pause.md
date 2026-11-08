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
| **True pause** (`/pause` endpoint) | No new invoices | Halted | Immediate API or Dashboard pause, configured customer-portal self-pause; flexible billing only. Linked schedule guide covers future attempts. |
| Pause payment collection | Yes (active collection paused; existing customer balance may pay an invoice under `mark_uncollectible`) | Continues | Dashboard or API; optional `resumes_at` |
| Trial-end pause (no payment method) | No | Halted | System-triggered at trial end |

## Prerequisites

- `billing_mode=flexible` — required
- `collection_method=charge_automatically`

## Blocking conditions (cannot pause if)

- `collection_method=send_invoice`
- `billing_mode=classic`
- Active subscription-level free trial configured with `trial_end` or `trial_period_days`; November expressly exempts item-level trial offers
- Status: `unpaid`, `paused`, `incomplete`, `incomplete_expired`, or `canceled`
- Attached subscription schedule or active billing schedule; the November guide describes schedule-based pause or release, and clearing billing schedules respectively

> [!warning] Contradiction
> The May 13 capture broadly excluded active trial offers, listed attached cadences, and said schedules or cadences could not be attached while paused. The November 7 guide expressly exempts item-level trial offers and does not repeat the cadence or reverse-attachment statements. Omission alone does not prove those historical restrictions were removed. See [[source-stripe-subscriptions-pause]] and its dated raw captures.

## Pause API

The `Stripe-Version: preview` line below is from the May 13, 2026 captured example. November's same-URL example omits it while linking to an API page with `api-version=2026-07-29.preview`; the captures do not establish a current required header or endpoint availability. See [[source-stripe-subscriptions-pause]].

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

**Customer portal**: The November guide says merchants can let customers pause their own subscriptions through a configured customer portal. The May capture described a display-only portal; configuration details are in a linked guide not reviewed here.

## Resume API

The `Stripe-Version: preview` line below is from the May 13, 2026 captured example. November's resume example omits it; the captures do not establish a current required header or invalidate the May form. See [[source-stripe-subscriptions-pause]].

```bash
POST /v1/subscriptions/:id/resume
Stripe-Version: preview
```

Key parameters: `billing_cycle_anchor`, `proration_behavior`

- Only available with `charge_automatically`
- Resume through Dashboard or API; the November guide also links to scheduled resume attempts. A scheduled attempt does not guarantee an active subscription or successful payment.

### Resume invoice flow

| Scenario | Result |
|---|---|
| No invoice generated | Status → `active` immediately |
| Invoice generated, paid | Status → `active` |
| Invoice generated, marked uncollectible | Status → `active` |
| Invoice generated, payment fails | Depends on `payment_behavior`: `past_due` with default `resume_on_payment_attempt`; `paused` with `resume_on_payment_success` |
| Invoice voided before payment | Stays `paused` |
| Pending update expires | Default `resume_on_payment_attempt`: 23 hours; `resume_on_payment_success`: 1 year. Stripe voids the invoice and leaves the subscription paused. |

With default `resume_on_payment_attempt`, the resume request does not attempt payment; use `POST /v1/invoices/:id/pay`. With `resume_on_payment_success`, Stripe attempts payment when a default payment method or sufficient cash balance is available; otherwise it returns an error. Failed payment on this branch leaves the subscription paused and invoice retries may occur unless disabled. Inspect `status` and `pending_update` even after HTTP 200. See [[source-stripe-subscriptions-pause]] for the dated May and November evidence.

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
| `void` | Invoices created during the collection-pause period are voided, with no record of charges for those periods (2026-11-07 guide). The 2026-05-13 guide described them as immediately voided. Invoices created before pausing can still be retried unless separately voided. |
| `keep_as_draft` | Stays draft, `auto_advance=false`; collect later by setting `auto_advance=true` |
| `mark_uncollectible` | Marked uncollectible (unless customer balance covers full amount → `paid`) |

Unset: `stripe.subscriptions.update(id, { pause_collection: '' })` — only affects future invoices.

Pre-pause invoices: still retried unless manually voided.

## Sources

- [[source-stripe-subscriptions-pause]] — May and November 2026 Stripe pause guide captures: flexible billing, pause billing, eligibility, portal and resume payment branches
- [[source-stripe-subscriptions-pause-payment]] — May/November 2026 `pause_collection` guide: three invoice behaviors, Dashboard/API pause and resume, optional `resumes_at`, schedule phase boundary, and separate draft-invoice collection
