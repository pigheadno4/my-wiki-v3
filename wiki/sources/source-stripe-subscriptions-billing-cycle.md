---
title: "Stripe — Set the Subscription Billing Renewal Date"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/billing-cycle"
raw_files:
  - "stripe-billing-subscriptions-billing-cycle-2026-11-07.md"
  - "stripe-subscriptions-billing-cycle-2026.md"
tags: [stripe, subscriptions, billing-cycle, billing-cycle-anchor, proration, trial]
---

## Summary

Stripe's billing-cycle guide explains how recurring price intervals and billing-cycle anchors align future renewal dates. It documents anchor configuration and direct timestamps when creating a subscription, changing an existing cycle with a now reset or trial, and a 2026-11-07 **private preview** for a specific-timestamp update of flexible-mode subscriptions. The May and November API examples use different shapes and must be read with their capture and version context.

## New subscriptions: anchor configuration

`billing_cycle_anchor_config` calculates an anchor for monthly or yearly subscriptions, including short months and leap years; `day_of_month=31` gives an end-of-month cycle, and `month` can align multi-month or yearly cycles. Hour, minute, and second can be specified; omitted values come from the subscription creation time, with the anchor expressed in UTC. Config does not support anchoring on a backdated start date (old lines 29–40, 60–87; new lines 30–68).

A config-derived `billing_cycle_anchor` can be more than one billing period after creation. The **first full invoice** still occurs within one billing period of creation or trial end, and can precede that anchor. The guide's two-month February example has an August 31 anchor but a first full invoice in February after an initial prorated period (old lines 112–114; new lines 83–85). The anchor aligns future cycle dates; it need not equal the first full invoice date.

## New subscriptions: direct timestamp

On **creation**, `billing_cycle_anchor` accepts a Unix timestamp directly through the Subscriptions API or Checkout. This option covers daily or weekly intervals as well as timestamp preference for other intervals. The page shows separate customer-configured Accounts v2 and Customers v1 creation examples (old lines 116–158; new lines 87–113). A direct arbitrary timestamp on an ordinary **update** is not established by these creation examples; see the qualified existing-subscription options below.

The 2026-05-12 capture renders creation examples in Node.js, and the 2026-11-07 capture renders them in curl. This presentation change does not establish Node SDK deprecation.

## Initial proration and Checkout boundary

By default, the creation-to-first-full-invoice period gets a prorated invoice. Setting `proration_behavior=none` makes that initial interval free, with no invoice until the first full billing period. In the **Subscriptions API**, `trial_end` can be combined with an anchor; a prorated invoice can follow the trial depending on the dates (old lines 160–167; new lines 115–122).

In **Checkout subscription mode**, `subscription_data.billing_cycle_anchor` sets the anchor, but Checkout does **not** support combining a trial with it. Checkout's `proration_behavior=none` makes the initial interval free and does not generate an invoice until the first billing period; one-time prices cannot be used in that case (old lines 169–207; new lines 124–149). The Checkout trial restriction is specific to Checkout, not the Subscriptions API.

## Existing subscriptions: reset to now

The 2026-11-07 guide uses `billing_cycle_anchor.type=now` for an update. Its curl example pins `Stripe-Version: 2026-09-30.endive` and sets `billing_cycle_anchor[type]=now` with `proration_behavior=create_prorations` (new lines 165–183). Proration can credit days already paid; disabling it can overcharge. Do not generalize this example's parameter shape to other API versions.

**Flexible-mode invoice exception:** resetting the anchor to now on `billing_mode[type]=flexible` does not automatically create an invoice. To trigger an invoice for that reset, set `proration_behavior=always_invoice`. If subscription items also change and their prorations do not fully cancel, Stripe immediately invoices regardless of `proration_behavior` (new lines 169–171). This qualifies the guide's general immediate-invoice wording at line 167.

The 2026-05-12 variant instead shows a Node.js update with scalar `billing_cycle_anchor: "now"` and `proration_behavior: "create_prorations"` (old lines 222–239). The two captures do not establish interchangeability of scalar and typed forms across API versions.

The May Dashboard path said **Bill today instead** under Billing and payment collection (old lines 241–246); November says **Reset the billing cycle** under Advanced options with a Prorate changes toggle (new lines 185–190). These are dated UI descriptions, not evidence that the old option was removed everywhere.

## Existing subscriptions: specific timestamp private preview (2026-11-07)

A specific-timestamp **update** is in **private preview** and requires API version `2026-09-30.preview` and a subscription using **flexible billing mode**. The request sets `billing_cycle_anchor.type=timestamp` and `billing_cycle_anchor.timestamp`. Stripe describes credits or debits for prior/new period days through proration, with proration behavior controlling immediate invoicing or disabling prorations (new lines 192–224).

The requested timestamp must be within one price interval of the current time; for mixed intervals, the smallest price interval governs, and with a free trial it must be after the current `trial_end` (new lines 226–235). The page also mentions specific timestamps for preview-invoice creation and resuming a paused subscription (new line 237). The capture does not prove preview enrollment, account eligibility, or that any particular update succeeded.

## Existing subscriptions: trial and automatic changes

Adding a free trial to an existing subscription can set its anchor to `trial_end`; the guide's example shifts the next full cycle from July 23 to August 1. `proration_behavior=none` can prevent prorations for the change (old lines 248–262; new lines 239–253).

Automatic anchor changes described in the guide include adding a paid price after all prices were zero, setting or changing `cancel_at` before renewal under the stated future-anchor condition, and switching to a price with a different recurring interval (old lines 216–220; new lines 159–163). The flexible-mode statement that the anchor remains unchanged on certain create/update changes is about **automatic** changes; it does not prohibit an explicit reset-to-now or qualified preview timestamp request (new lines 159, 169–171, 210–213).

The May Dashboard trial path listed **Continue subscription and send invoice**, **Cancel subscription**, and **Pause subscription** when a trial ends without a payment method (old lines 275–288). The November path is shorter (new lines 262–268). Its omission does not establish removal of those older UI choices.

## Usage-based billing and thresholds

If a changed cycle ends a usage-based service period early, the guide says usage accrued during the shortened period is charged. A subscription can also bill when an amount threshold is reached and optionally reset the service period at that threshold (old lines 290–298; new lines 270–278).

## Related pages

- [[stripe-subscriptions]] — subscription concept
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-billing-subscriptions-billing-cycle-2026-11-07|2026-11-07 billing-cycle guide capture]]
- [[raw/stripe-subscriptions-billing-cycle-2026|2026-05-12 billing-cycle guide capture]]
