---
title: "Stripe Subscription Schedules"
type: source
date_ingested: 2026-11-08
canonical_url: https://docs.stripe.com/billing/subscriptions/subscription-schedules
original_format: webpage
raw_files:
  - "stripe-billing-subscriptions-subscription-schedules-2026-11-07.md"
  - "stripe-subscriptions-schedules-2026.md"
tags: [stripe, billing, subscriptions, subscription-schedules, phases, proration, installments]
---

## Summary

Stripe's subscription schedules create a subscription or attach to an existing one, then apply sequential phases to automate changes over time. Only one phase is active at a time; a schedule can have up to 10 current and future phases. The November 2026 guide describes Dashboard and API workflows for creating, editing, previewing, and canceling schedules; it documents release through the API. The May 2026 capture said the Dashboard feature required the classic Subscription editor and that the editor choice persisted for 30 days. Treat that as dated UI guidance, not a current universal availability rule.

## Core concepts

- A phase supplies its configuration when it starts. After the final phase, `end_behavior` can release or cancel the schedule; consequences depend on whether a subscription exists.
- API release accepts a schedule ID in `not_started` or `active` state, removes the schedule and remaining phases, preserves an existing subscription, and creates none if the schedule has not started. API cancellation also accepts those states; with an active subscription, it cancels the associated subscription immediately. Dashboard deletion before the start cancels the schedule before a subscription is created.
- The first invoice for a schedule-created subscription with `collection_method=charge_automatically` behaves like a recurring invoice rather than immediately finalizing as in the guide's direct-creation comparison. In the `start_date=now` example, it begins as `draft`, remains editable for about an hour, then advances to `open` or `paid` depending on asynchronous payment outcome. The capture does not verify an actual payment or settlement.

## Phase attributes

- `duration.interval` plus `duration.interval_count` is recommended over manually setting `start_date` and `end_date`.
- `iterations` counts billing periods, including for installment examples.
- `trial_end` can end before the phase end or at the phase end.
- A phase can configure items, discounts, quantities, billing cycle anchor, taxes, and metadata, subject to the particular API or Dashboard path.

## Two proration behavior settings

| Setting | Scope | Values |
|---|---|---|
| Top-level `proration_behavior` | A schedule update affecting the current phase | `create_prorations` (default), `none`, `always_invoice` |
| Per-phase `proration_behavior` | Proration when entering that phase | Same three values |

## Phase attribute inheritance and tax

Five attributes can be set at both `default_settings` and phase level: `automatic_tax`, `billing_thresholds`, `collection_method`, `default_payment_method`, and `invoice_settings`. A phase value overrides the schedule default; absent both, customer or account defaults apply.

To use manual `default_tax_rates` for a phase, set its `automatic_tax.enabled=false`, including when the schedule default might later enable automatic tax. Manual tax rates and enabled automatic tax cannot apply to the same phase; remove manual rates to enable automatic tax. Enabling automatic tax directly on a subscription with an attached schedule updates its current phase and the schedule default. Future phases with no explicit setting inherit that changed default. Retained manual rates on such a phase do not become a fallback if automatic tax calculation fails.

## Phase metadata rules

- A non-empty phase metadata value adds or updates the key on the subscription when that phase begins.
- An empty value unsets that key on the subscription.
- Direct edits to subscription metadata do not update the current phase metadata.

## Updating schedules

Pass all current and future phases on an update; past phases are response-only. Re-send previously configured parameters that must remain: omitted values are unset for the existing phase. An active-phase update also updates the underlying subscription. The 10-phase limit counts current and future phases, not past phases.

## Direct subscription updates on schedule-attached subscriptions

A direct subscription edit can be overwritten when a later schedule phase begins. Stripe recommends the Subscription Schedule API for scheduled changes and keeping schedule IDs with subscription IDs; a released schedule ID can be discarded after the `subscription_schedule.released` event. Dashboard edits, where available, update the attached schedule.

Direct edits to `items`, `discounts`, `tax_rates`, `trial_end`, `trial_settings`, `trial_start`, `application_fee_percent`, `add_invoice_items`, or `automatic_tax` **might** automatically create a new phase. The guide's concrete item-deletion example splits the active phase into an ended two-item phase and a new one-item phase. Subscription metadata edits do not propagate to the schedule.

## Creation and use cases

1. **Future start** — `start_date` in the future creates the subscription when that date arrives.
2. **Backdate** — a past `start_date` creates the subscription immediately and bills elapsed time; the application controls access to digital content. Backdating alone is not an access grant.
3. **Attach to an existing subscription** — `from_subscription` creates one phase based on the current billing period and configuration, without proration invoice items from the migration.
4. **Upgrade, downgrade, change price or quantity** — configure successive phases; the guide's single-item downgrade is an example, not a general template.
5. **Coupons and tax changes** — configure phase-specific discounts or tax settings while observing automatic/manual tax exclusions.
6. **Reset billing cycle anchor** — use `billing_cycle_anchor: phase_start` in the illustrated transition.
7. **Installments** — use `iterations` and a suitable `end_behavior`; the May and November guides illustrate one-off `price_data` amounts.
8. **Keep billing after a final phase** — the Dashboard examples set the last phase to **Forever**. A finite Dashboard final end date cancels the subscription at that date. For fixed-duration release without canceling the subscription, the November guide uses the API with `end_behavior=release`.

## Preview and Dashboard boundaries

The API can preview an existing schedule with an invoice preview using its schedule ID, or preview proposed phases through `schedule_details.phases`. Preview is prospective and does not establish invoice finalization or payment. Dashboard paths in the November capture include create, edit, preview, and cancel; release is shown through the API. Dashboard availability for every account or editor variant is not established by this capture.

The May capture's Node.js snippets remain dated examples; the November capture mainly uses curl and includes a Ruby downgrade example. The sample-language change does not establish SDK deprecation.

## Related pages

- [[stripe-subscriptions-schedules]] — concept page
- [[stripe-subscriptions]] — concept page
- [[stripe-subscriptions-prorations]] — proration behavior
- [[stripe]] — company page

## Raw Sources

- [[stripe-billing-subscriptions-subscription-schedules-2026-11-07]] — Stripe guide captured 2026-11-07 (989 lines)
- [[stripe-subscriptions-schedules-2026]] — Stripe guide captured 2026-05-13 (1170 lines)
