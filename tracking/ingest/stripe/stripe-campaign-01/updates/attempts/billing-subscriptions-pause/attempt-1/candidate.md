---
title: "Stripe Subscriptions — Pause Subscriptions"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/pause"
raw_files:
  - "stripe-billing-subscriptions-pause-2026-11-07.md"
  - "stripe-subscriptions-pause-2026.md"
tags: [stripe, billing, subscriptions, pause, flexible-billing, webhooks]
---

## Summary

The November 7 Stripe guide describes true subscription pause: `POST /v1/subscriptions/:id/pause` suspends service delivery and new invoice generation without canceling the subscription. Existing invoices continue to advance. This differs from `pause_collection`, which leaves access and invoice generation running, and from Stripe's automatic trial-end pause when no payment method is on file.

## Three pause-like behaviors compared

| Behavior | Invoices generated? | Service delivery? | Trigger |
|---|---|---|---|
| **True pause** (this page) | No new invoices during pause | Halted | Immediate API or Dashboard pause; configurable customer-portal self-pause; flexible billing required. A linked schedule guide covers future pause and resume attempts. |
| Pause payment collection | Yes (collection paused) | Continues | Separate payment-collection setting |
| Trial-end pause without payment method | No | Halted | System-triggered at trial end; not the Pause subscription endpoint |

> [!warning] Contradiction
> The May 13 capture said the portal only displayed paused status and subscribers could not self-pause, and described manual API resumption. The November 7 same-URL guide explicitly permits configured customer-portal self-pause and points to scheduled pause and resume attempts. The linked portal and schedule guides were not reviewed here, so their detailed eligibility, configuration, and outcome are not established by this page.

## Requirements and limitations

- The pause endpoint requires flexible billing mode; resume requires `collection_method=charge_automatically`. Pause is unavailable for `send_invoice` and classic billing mode.
- November's limitation table excludes active **subscription-level** free trials configured with `trial_end` or `trial_period_days`, but expressly exempts item-level trial offers.
- A subscription cannot be paused when status is `unpaid`, `paused`, `incomplete`, `incomplete_expired`, or `canceled`.
- An attached subscription schedule blocks direct pause; the November guide says to add a pause schedule or release the schedule first. An active billing schedule also blocks pause until cleared.
- The May capture additionally listed an attached cadence and said a schedule or cadence could not be attached to a paused subscription. November omits those statements; this is not evidence of their removal or reversal. See both raw captures for the dated wording.
- A coupon keeps its original validity period, which continues to run while paused.

## Pause behavior and billing

The pause takes effect immediately: status becomes `paused`, each item's `current_period_end` moves to the pause time, and new subscription invoices stop for the pause duration. Existing invoices continue advancing. Stripe sends `customer.subscription.paused`, `customer.subscription.updated`, and `entitlements.active_entitlement_summary.updated` for subscription and access handling.

`bill_for.unused_time_from` controls credit for unused licensed time: `now` (default), `item_current_period_start`, or `none`. `bill_for.outstanding_usage_through` controls metered usage: `now` (default) or `none`. `invoicing_behavior` defaults to `pending_invoice_item`; `invoice` invoices credits/debits immediately. The November response includes `status_details.paused.transitioned_at` and a reason such as `pause_requested`, `trial_end_without_payment_method`, or `system`. See new raw lines 65–113 for exact parameters and shape.

The pause invoice preview is non-mutating. It returns an invoice only when `invoicing_behavior=invoice` **and** the `bill_for` settings create billable credits or debits; otherwise Stripe returns 404. A restricted API key needs `subscription_write` to pause or resume and `invoice_read` to preview invoices.

The May API example used `Stripe-Version: preview` and `type=subscription`:

```bash
POST /v1/subscriptions/sub_xxx/pause
Stripe-Version: preview
type=subscription

bill_for[unused_time_from][type]=now
bill_for[outstanding_usage_through][type]=now
invoicing_behavior=pending_invoice_item
```

November's example omits the header and `type` parameter, while its pause API link contains `api-version=2026-07-29.preview`. The omission does not establish that May's parameters are rejected or that the endpoint is generally available.

## Resume behavior

The November guide provides Dashboard and API resume flows and links to a scheduled resume-attempt guide. Resume requires `charge_automatically`. If no resumption invoice is generated, status becomes `active` immediately. If one is generated, Stripe finalizes it; payment or manual uncollectible marking makes the subscription active, while voiding leaves it paused. A `200` response alone can still leave the subscription `paused` pending invoice payment: inspect `status` and `pending_update`.

| Outcome | `resume_on_payment_attempt` (default) | `resume_on_payment_success` (recommended by guide) |
|---|---|---|
| Payment during resume request | None; use Pay invoice endpoint | Attempt with default payment method or sufficient cash balance; otherwise error |
| Failed payment | `past_due`, no automatic return to paused | Remains `paused` |
| Invoice retries | None | Yes, unless retry settings disable them |
| Pending-update expiry | 23 hours after resume request | 1 year after resume request |

The May source's no-attempt, `past_due`, and 23-hour descriptions match the November **default** branch, not every resume. May's example used `Stripe-Version: preview` and `billing_cycle_anchor=unchanged`; November shows `payment_behavior=resume_on_payment_success` and `billing_cycle_anchor[type]=now`. These are dated examples, not proof that either earlier form was invalidated. The resumption invoice preview also does not mutate the subscription; see new raw lines 190–203.

## Webhooks and verification

| Event | When |
|---|---|
| `customer.subscription.paused` | Subscription pauses |
| `customer.subscription.resumed` | Subscription resumes |
| `customer.subscription.updated` | Either transition |
| `entitlements.active_entitlement_summary.updated` | Entitlements change due to pause/resume |

Verify webhook signatures before processing. The guide also supplies an illustrative mid-cycle dollar example, test-clock checks, and a Sigma query for paused status/reason. Those examples do not guarantee a particular invoice amount, eligible account, or successful payment.

## Related pages

- [[stripe-subscriptions-pause]] — concept page
- [[stripe-subscriptions-pause-payment]] — pause collection distinction
- [[stripe-subscriptions-cancel]] — cancellation patterns
- [[stripe-subscriptions]] — subscription concept
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-billing-subscriptions-pause-2026-11-07|Stripe pause guide, November 7 2026]] — updated same-URL capture
- [[raw/stripe-subscriptions-pause-2026|Stripe pause guide, May 13 2026]] — historical capture
