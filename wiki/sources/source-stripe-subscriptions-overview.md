---
title: "Stripe — How Subscriptions Work"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-subscriptions-overview-2026.md"
tags: [stripe, subscriptions, billing, invoice, payment-intent, statuses, lifecycle, entitlements]
---

## Summary

Comprehensive subscription lifecycle guide. Covers payment behavior options, the 23-hour first payment window, all 8 subscription statuses, payment status matrix, async payment method behavior, and first invoice update constraints.

## Payment Behavior Options

- `default_incomplete` (recommended): creates `incomplete` status if payment required; collect and confirm payment after
- `allow_incomplete`: immediately attempts payment; `incomplete` on failure
- `error_if_incomplete`: subscription creation fails entirely if payment fails

## 23-Hour First Payment Window

Customer has ~23 hours to pay first invoice (on-session assumption). After 23 hours, subscription → `incomplete_expired`, invoice → `void`. If customer returns after 23h, create a new subscription.

## 8 Subscription Statuses

| Status | Description |
| --- | --- |
| `trialing` | Trial period; no payment yet; transitions to `active` on first payment |
| `active` | Good standing; paying invoices |
| `incomplete` | Awaiting first payment (within 23h) or payment requires action |
| `incomplete_expired` | First payment not made within 23h; terminal |
| `past_due` | Latest invoice payment failed; smart retries pending |
| `canceled` | Canceled; terminal; auto_advance=false on invoices |
| `unpaid` | Latest invoice unpaid; new invoices generated but not attempted |
| `paused` | Trial ended without payment method + `missing_payment_method=pause` |

## Payment Status Matrix

| Outcome | PaymentIntent | Invoice | Subscription |
| --- | --- | --- | --- |
| Success | `succeeded` | `paid` | `active` |
| Card error | `requires_payment_method` | `open` | `incomplete` |
| 3DS needed | `requires_action` | `open` | `incomplete` |

## Async Payment Methods (ACH etc.)

Skip `incomplete` entirely — subscription goes directly to `active`. If payment fails later, Stripe voids the invoice but subscription stays `active`. Design access control and retry logic accordingly.

## First Invoice Constraints

- `send_invoice`: 1-hour update window after creation
- `charge_automatically`: finalized and charged immediately (no update possible)
- Subscription schedules: first invoice always open, regardless of collection method

## Key Webhooks

- `invoice.paid` — confirm payment succeeded; provision access
- `invoice.payment_failed` — handle failures + Smart Retry updates
- `invoice.payment_action_required` — 3DS authentication needed

## Related Pages

- [[stripe-subscriptions]] — concept page (updated with statuses, payment behavior, 23h window)

## Raw Sources

- [[stripe-subscriptions-overview-2026]] — verbatim subscription lifecycle guide (180 lines)
