---
title: "Stripe Subscriptions — Bill Customers in Advance (Prebilling)"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/prebilling"
raw_files:
  - "stripe-billing-subscriptions-prebilling-2026-11-07.md"
  - "stripe-subscriptions-prebilling-2026.md"
tags: [stripe, billing, subscriptions, prebilling, flexible-billing]
---

## Summary

Prebilling uses `billing_schedules` on a subscription to invoice licensed-price items for future service periods when creating or updating the subscription. The 2026-11-07 capture requires `billing_mode=flexible` and API version `2026-05-27.dahlia` or later. The 2026-05-13 capture called the feature a public preview and required `2025-09-30.preview` or later. The newer page omits the preview label; that omission alone does not establish general availability or account eligibility. Invoice creation or finalization is not payment success.

> [!warning] Contradiction
> The May 2026 public-preview capture stated a `2025-09-30.preview` API prerequisite, while the November 2026 guide states `2026-05-27.dahlia` or later. Use the dated version statement for its capture; do not treat the old preview version as the newer guide's prerequisite.

## Concept and use cases

Prebilling changes when future service periods are invoiced, not when a service period starts. The November guide illustrates multiple months at signup, an early renewal invoice, an annual upfront invoice for a monthly price, item-level prebilling, and an early cancellation fee for a committed contract. For an upcoming renewal billed a set number of days early, trigger the subscription update on the desired date; prebilling does not schedule that update by itself. The May capture also gave a 45-day first-period example and a two-month renewal example.

## Requirements and item scope

- Flexible billing mode is required; an existing subscription must already be flexible before adding prebilling.
- The November guide states API version `2026-05-27.dahlia` or later.
- `billing_schedules[]` defines which items are prebilled and through what end date. `applies_to[]` targets specific price IDs. Omit it to cover applicable licensed-price items that cycle before the end date. Metered usage items are excluded and cannot be selected by `applies_to[price]`.
- The November API examples distinguish Accounts v2 `customer_account` from Customers v1 `customer`; both use flexible billing. Dashboard creation selects all items, while the API can target selected items.

## `bill_until` and end date

`bill_until.type` accepts `duration` with `interval` and `interval_count`, or a `timestamp` Unix end date. The November capture describes the duration as measured from the **current date** (for example, two months); it does not give complete arithmetic for an already-running off-anchor or mixed-interval subscription.

- **Minimum:** November says at least one full billing period from the start; its example is a monthly subscription with at least one month from the period start. It does not specify which item controls this minimum for mixed intervals.
- **Maximum:** Total prebilled cycles **across all items** cannot exceed 50; this is not a 50-cycle allowance for each item.
- **Five years:** The guide advises against setting the end date more than five years in the future; it does not state an API rejection rule for that advice.
- If the end date splits a billing period, the part before the end date is prebilled and the rest follows the subscription's configuration.

> [!warning] Contradiction
> The May public-preview capture set its minimum at one cycle of the shortest billing period and its maximum at 12 cycles of that shortest period. November gives the one-full-period wording without a mixed-interval shortest-item rule and caps total cycles across items at 50. May also said a `duration` was from the billing-cycle start, although May's later paragraph mixed “current time” with a cycle-start example; November consistently describes the anchor as the current date. Do not project the May shortest-period rule or exact off-anchor date arithmetic onto the newer guide.

## Invoice timing and payment outcome

`proration_behavior=always_invoice` generates **and finalizes** the prebilling invoice immediately when the subscription is created or updated. `create_prorations` generates it at the next natural billing cycle date. These specific timing rules qualify the guide's broad “when configured” wording. A preview invoice using `subscription_details.billing_schedules` estimates the invoice before changing the subscription.

For the November early-renewal example, update on the desired early billing date with `bill_until` at the upcoming period end and `always_invoice`. Its early-cancellation-fee example updates through the committed term with `always_invoice`, then cancels after a successful update using `prorate=false`; it illustrates invoice generation/finalization, not legal fee entitlement or successful collection. `invoice.created` and `invoice.finalized` differ from `invoice.payment_succeeded` and `invoice.payment_failed`; the example grants access to prepaid periods on payment success.

## Limitations and dated uncertainty

- Subscription schedules and schedule-backed subscriptions are incompatible with prebilling. Expired `billing_schedules` entries remain; clear them with an empty value before later creating a subscription schedule.
- Only `percent_off` coupons with `duration=once` or `forever` are compatible. The November page says `amount_off` and repeating coupons return an error when `billing_schedules` is configured.
- A scheduled cancellation automatically caps a requested prebilling end date at the cancellation date.
- November bars `payment_behavior=pending_if_incomplete` **when updating a subscription with an active billing schedule**.
- The May public-preview limitations also barred subscriptions migrated from classic to flexible billing mode and `proration_behavior=none`, and stated a broader `pending_if_incomplete` ban. November omits the first two and narrows the latter. Omission does not demonstrate that previously barred cases are supported. May's “applied immediately” wording must be read with its own `create_prorations` next-cycle invoice instruction and November's specific invoice-timing rules.

## Related pages

- [[stripe-subscriptions-prebilling]] — concept page
- [[stripe-subscriptions]] — subscriptions concept
- [[source-stripe-subscriptions-billing-mode]] — flexible billing mode prerequisite
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-billing-subscriptions-prebilling-2026-11-07|2026-11-07 prebilling guide]]
- [[raw/stripe-subscriptions-prebilling-2026|2026-05-13 public-preview prebilling guide]]
