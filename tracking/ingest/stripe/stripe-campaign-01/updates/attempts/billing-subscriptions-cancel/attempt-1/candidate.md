---
title: "Stripe Subscriptions — Cancel Subscriptions"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/cancel"
raw_files:
  - "stripe-billing-subscriptions-cancel-2026-11-07.md"
  - "stripe-subscriptions-cancel-2026.md"
tags: [stripe, billing, subscriptions, cancellation, prorations, webhooks]
---

## Overview

Stripe's [[stripe-subscriptions-cancel]] guide covers manual immediate and period-end cancellation, custom cancel dates, subscription schedules, and configured dispute-triggered cancellation. It also explains prorations, pending invoice items, invoices, events and billing-cycle anchors. The 2026-11-07 capture clarifies when custom-date prorations can be disabled and adds an optional Workflows template for pending invoice items; the 2026-05-13 capture remains historical evidence. See [[stripe]] and [[stripe-subscriptions]].

## Cancellation paths

- By default, an API or Dashboard cancellation takes effect immediately and stops future invoices for that subscription. Once canceled, the subscription can be updated only for `metadata` and `cancellation_details`; it cannot be reactivated. The May capture's Node.js `stripe.subscriptions.cancel` snippet and November curl DELETE example are dated renderings of this path.
- Setting `cancel_at_period_end=true` keeps the subscription through its already paid period. Setting it back to `false` can stop the pending cancellation before that period ends. A subscription schedule with `end_behavior=cancel` manages `cancel_at` at its final phase; adding a phase to that final phase removes the cancel date and can affect period end and anchor. The older Node.js and newer curl update examples are locators, not evidence of execution.
- The Dashboard can be configured to cancel after a dispute, but only for full-amount credit or debit card disputes. Test clocks are excluded; changes take approximately one hour. A scheduled subscription is released from its schedule before cancellation, so later schedule phases do not apply. This does not show any merchant enabled the setting.
- The guide also describes automatic cancellation after up to eight failed billing attempts, with the attempt count configurable in Dashboard settings. Pausing payment collection is distinct from canceling and does not itself change subscription status.

## Custom cancel date and prorations

A future `cancel_at` can shorten `items.current_period_end`, which creates prorations unless the update disables them where allowed. The guide says a custom cancel date does not offer a refund. Its November text permits prevention of the credit proration only when `cancel_at` is within the **current billing period**; being within that period alone does not suppress it. The May capture explicitly names `proration_behavior=none` as the within-period suppression path. For a cancel date outside the current period, November says prorations cannot be disabled. When `cancel_at` shortens the current period, disabling prorations can affect invoice lines differently by billing mode; this capture does not define the complete per-mode effects.

> [!warning] Contradiction
> The May 2026 capture says a credit proration is “always generated” for a custom cancellation date and, in the same passage, gives a `proration_behavior=none` prevention path within the current period. The prior source repeated the absolute claim. The November 2026 wording resolves the overstatement with the within-period condition and the outside-current-period prohibition. Do not treat all custom dates as automatically credited or all within-period dates as automatically suppressed.

For `billing_mode` subscriptions, `min_period_end` and `max_period_end` helpers resolve the earliest or latest item period-end timestamp immediately. A date more than one period away leaves the current cycle unaffected until renewal into the period containing the date. For flexible billing subscriptions in `trialing` status, changing `cancel_at` does not alter `trial_end`. The post-June-2024 billing-cycle-anchor reset guarantee is limited to subscriptions created after June 2024; older ones can retain legacy behavior.

## Invoice items and existing invoices

Pending invoice items can still be billed if cancellation includes a final invoice or the customer has another active subscription. The guide's manual route deletes the pending items to avoid that billing. The November capture adds an optional **Workflows** template that runs **when the subscription ends** and deletes **only its pending invoice items**. The template's presence does not establish that it was installed or run, that earlier items were retroactively deleted, or that existing invoices were erased. Metered usage can bill at period end unless `clear_usage` is used on an update; `invoice_now` can create a final invoice.

For period-end cancellation, pending prorations remain to be collected at period end. For an early cancellation, invoice items remain unprocessed unless specifically invoiced. Cancellation sets `auto_advance=false` on open and draft invoices for that subscription, pausing automatic collection and reminder emails; manual collection and emails remain possible. This does not void those invoices or discharge amounts owed.

## Cancellation events and historical qualifications

`customer.subscription.updated` includes scheduling `cancel_at_period_end=true`; `customer.subscription.deleted` marks actual cancellation by direct delete or when the scheduled period end arrives. The update event is not the deletion event or evidence of a paid final invoice.

The warning about update parameters before API version 2018-02-28 remains in both captures: historically, any parameter on Update Subscription stopped a pending cancellation. The anchor-reset qualification above applies only to subscriptions created after June 2024.

## Detail locators

- November: manual and period-end cancellation (raw lines 17–64); schedule and full-amount card dispute limits (66–88); invoice items and Workflows (90–107); events and stopping a pending cancel (109–139); custom date, proration and billing-mode/anchor qualifications (141–176).
- May: Node.js cancel/update examples (raw lines 35–41, 60–68, 135–159); internally mixed custom-date statement and suppression path (20); invoice and event boundaries (96–118); 2018-02-28 and post-June-2024 qualifications (145, 182).
- The November page uses curl examples where May used Node.js. Neither captured example proves an executed cancellation, refund, final invoice payment or workflow run.

## Related

- [[stripe-subscriptions-cancel]] — cancellation concept
- [[stripe-subscriptions-prorations]] — proration behavior
- [[stripe-subscriptions]] — subscription lifecycle
- [[stripe]] — company

## Raw Sources

- [[raw/stripe-billing-subscriptions-cancel-2026-11-07|Cancellation guide — captured 2026-11-07]]
- [[raw/stripe-subscriptions-cancel-2026|Cancellation guide — captured 2026-05-13]]
