---
title: "Stripe — Free Trial Periods on Subscriptions (Legacy trial_end)"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: https://docs.stripe.com/billing/subscriptions/trials/free-trials
raw_files:
  - "stripe-billing-subscriptions-trials-free-trials-2026-11-07.md"
  - "stripe-subscriptions-free-trials-2026.md"
tags: [stripe, subscriptions, free-trials, legacy, trial-end, trial-period-days, pause, resume]
---

## Summary

Both the May 12 and November 7, 2026 captures call `trial_end` free-trial periods a **legacy** integration path and recommend Trial Offers for new integrations. The November page adds a comparison link. Trial Offers are a separate preview path with their own constraints; the legacy Checkout trial example remains documented here.

## Trial period and first invoice

- Supply `trial_end` as a timestamp, or `trial_period_days` as an integer. The trial period cannot exceed 730 days. `trial_end=now` can end a trial early.
- Accounts v2 customer-configured Account examples use `customer_account`; Customers v1 examples use `customer`. The November capture says Accounts v2 was generally available for Connect users and in public preview for other Stripe users, with a preview version required for participants.
- A trial may start without a payment method. Stripe still creates an immediate zero-amount invoice whose line description includes “Free trial.”
- When the trial ends and the subscription is not `paused`, Stripe creates an invoice and emits `invoice.created`, then attempts to charge about an hour later. These steps do not establish that payment succeeds or that a specific subscription becomes active.
- Usage recorded during a trial is not billed then, but can be viewed in the meter event summary. For a `paused` subscription, meter events may be sent but are not invoiced; future invoices include only events after resume. Legacy usage records cannot be created while paused.

## No-payment-method end behavior

Set `trial_settings.end_behavior.missing_payment_method` on the subscription:

| Value | Documented result at trial end without a payment method |
|---|---|
| `cancel` | The subscription cancels. A later paid service requires a new subscription. |
| `pause` | The subscription enters `paused`, stops cycling and invoicing, and can remain paused indefinitely until resumed. |
| `create_invoice` | Stripe invoices; if there is still no method when the invoice finalizes, the subscription moves to `past_due`. |

A truly `paused` subscription stops generating invoices. `pause_collection` instead stops collection while invoicing and billing periods continue.

For a no-method **Checkout Session**, the examples set `subscription_data.trial_settings.end_behavior.missing_payment_method` to `cancel` or `pause` and `payment_method_collection=if_required`, making payment-information collection optional in that Checkout Session. That Checkout setting is not a global rule for all subscription flows. The API create examples also include `payment_settings.save_default_payment_method=on_subscription`; the guide does not say that setting is required for the missing-method behavior.

## Dashboard controls (November 2026)

The November Dashboard guide offers **Pause or cancel if free trial ends without a payment method**. For cancel, select **Cancel immediately** and expect `customer.subscription.deleted`. For pause, select **Pause** and expect `customer.subscription.paused`. The option is hidden if a payment method was provided or **Email invoice to customer with link to payment page** was selected. This visibility statement describes this Dashboard flow, not every API configuration.

The May pause instructions inconsistently said to select **Cancel subscription** while expecting `customer.subscription.paused`. Use the November **Pause** instruction for the newer captured UI.

## Resume a paused subscription

Use the Dashboard, API `resume` endpoint, customer portal, or hosted invoice page to resume. Adding a payment method alone is not the documented reactivation gate. The API can start resume without a method attached, for example to view the invoice, but **the resumption invoice must be paid before the subscription is reactivated**. The guide says the invoice automatically voids after 23 hours **if its associated PaymentIntent has no payment method attached and is unconfirmed**. This is a conditional void rule, not an unconditional 23-hour payment deadline.

The endpoint can optionally change `billing_cycle_anchor` or create prorations. With `billing_cycle_anchor=unchanged`, a debit proration may cover the partial period unless `proration_behavior=none`; `always_invoice` also creates a current-period invoice. With `billing_cycle_anchor=now`, the new cycle starts now. The guide does **not** specify the default anchor value on resume. November Dashboard controls explicitly offer **Reset billing cycle anchor to now** and an optional prorated bill.

The customer portal example lets a customer select **Start subscription** and add a method; the hosted invoice page offers **Authorize and pay**. Both are payment/resumption actions, not evidence that attachment alone reactivates the subscription.

## Other trial behavior and version scope

For most subscriptions given a later trial, `trial_start` continues to show the first trial's start. As of API version `2025-04-30`, a subscription using `billing_mode=flexible` instead reports the most recent trial's start. Adding items during a trial can create zero-amount invoices; a one-time price added through `add_invoice_items` can still be charged during the trial. The guide also illustrates a free trial followed by a prorated period before a fixed billing-cycle anchor. Its fixed historical timestamps are examples, not valid current request values.

The May capture used Node examples and the November capture uses curl for corresponding operations. That presentation change does not establish removal of the Node SDK path.

## Related Pages

- [[stripe-subscriptions]] — subscription concepts and Checkout trial use
- [[stripe-subscriptions-trial-offers]] — separate Trial Offers preview path
- [[stripe]] — company page

## Raw Sources

- [[stripe-billing-subscriptions-trials-free-trials-2026-11-07]] — November 7, 2026 Stripe guide
- [[stripe-subscriptions-free-trials-2026]] — May 12, 2026 Stripe guide
