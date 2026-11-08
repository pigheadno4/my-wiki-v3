---
title: "Stripe — Compare Classic and Flexible Billing Mode"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/billing-mode/compare"
raw_files:
  - "stripe-billing-subscriptions-billing-mode-compare-2026-11-07.md"
  - "stripe-subscriptions-billing-mode-compare-2026.md"
tags: [stripe, subscriptions, flexible-billing, billing-mode, prorations, usage-based, mixed-intervals]
---

## Overview

Stripe compares classic and flexible subscription billing to help an integration assess a migration. Both the 2026-05-13 and 2026-11-07 captures recommend reviewing the behavioral differences and warn that a subscription migrated to flexible mode cannot migrate back to classic. This comparison does not itself establish an account's API version, eligibility, or selected default. See [[stripe]] and [[stripe-subscriptions]].

## Key differences

| Area | Classic | Flexible |
| --- | --- | --- |
| Credit prorations | Uses current item price, tax, quantity, and last discounts | Uses original debited amount; a period billed across multiple debits yields a credit for each original debit |
| Discount prorations | Distributes discounts evenly across items | Applies discounts proportionally per item |
| Adding a usage-based item | Example creates a 0 USD line | Suppresses the 0 USD line and, if the invoice would be empty, the invoice; **cycling invoices retain 0 USD usage lines** |
| Usage price after a price change | In the page's example, bills only usage reported since changing to the current price | Bills usage at the price effective when it was reported |
| Removing a usage-based item | API removal: no unbilled-usage invoice item; schedule transition: invoice without that item | API removal can create an unbilled-usage item; mid-period schedule phase transition depends on the incoming phase's `proration_behavior` |
| Renewal schedule phase transition with usage-based items | The documented scenario generates two invoices | One consolidated invoice for usage-based and licensed items, with previous-phase discounts for usage and next-phase tax rates |
| Customer Portal scheduled cancellation | `cancel_at_period_end=true`; `cancel_at` follows the period end | `cancel_at_period_end=false`; `cancel_at` is the maximum item period end and does not move when an item's period end changes |
| Subsequent trials | `trial_start` remains the first trial start | `trial_start` is the most recent trial start |
| Changing `cancel_at` during a trial | An earlier `cancel_at` can shorten `trial_end` | The documented scheduled-cancellation change does not alter `trial_end` |
| Mixed intervals | Same interval and interval count required across items | Different recurring intervals or counts can coexist |
| Subscription item limit | Up to 20 | Up to 100 |

The comparison's detailed conditions and examples are in the November raw: credit/discount prorations at lines 15–31; usage at 33–81; schedule and Portal cases at 122–140; trials at 187–239; mixed intervals and item limits at 265–279. The May raw preserves the earlier presentation at lines 12–218.

## Billing cycle anchor and prorations

The November capture says flexible subscription updates preserve the billing cycle anchor except when `billing_cycle_anchor` is explicitly set to something other than `unchanged` **or `trial_end` is updated**, which sets the anchor to the new trial end. Its comparison says the classic automatic resets on interval change, zero-to-paid price change, and moving `cancel_at` before renewal do not reset the flexible anchor. In the documented free-to-paid case, flexible mode leaves pending invoice items for the next cycle unless `proration_behavior=always_invoice` or `billing_cycle_anchor=now` is used to invoice immediately. See November lines 83–96.

> [!warning] Contradiction
> The 2026-05-13 capture said flexible mode resets the anchor only on an explicit `billing_cycle_anchor` update and its table said the anchor is never automatically reset (May lines 84–88). The 2026-11-07 capture adds the `trial_end` exception (November lines 85–92). Keep the May statement as dated wording, not an unconditional rule.

For a reset without item changes, the November example nets equivalent credits and debits. Under `create_prorations`, flexible mode leaves a net proration item without an immediate invoice; `always_invoice` invoices it immediately; `none` creates neither item nor invoice. If item changes prevent full cancellation, the page says a full-period line and immediate invoice result regardless of `proration_behavior`. See November lines 98–120.

## Short first periods and backdating

When `cancel_at` at subscription creation shortens the first period, the November table says classic mode invoices the full amount despite `proration_behavior=none`, while flexible mode treats the shortened period as a proration; with `none`, it has no line item, no invoice, and `latest_invoice=null`. The analogous update behavior is limited to an update that creates an invoice. May described this shorter period more generally; see May lines 110–116 and November lines 142–150.

For backdating consistent with regular billing, flexible mode separates invoice lines by billing period and aligns the anchor to `backdate_start_date` unless explicitly set; backdating is unsupported if the resulting invoice exceeds 250 lines. The November addition says that when a backdated period had no debit because `proration_behavior: 'none'` suppressed invoicing, flexible mode does not later issue a credit for that period on update or cancellation, while classic mode can. See May lines 118–145 and November lines 152–185.

## Pending invoice items

The November capture distinguishes two cases. When only one-time `add_invoice_items` charges are added during a mid-period subscription update or schedule phase transition, **and no subscription item, price, or quantity change independently causes an invoice**, classic mode creates an update invoice, while flexible mode leaves the additions pending despite `proration_behavior=always_invoice` alone. A later eligible invoice can include them. A separately created invoice tied to the subscription can invoice them sooner and includes all pending items for that subscription. This difference excludes subscription creation and renewal phase transitions. See November lines 241–253.

For **update-generated invoices**, the November table says classic anchor-reset invoices include eligible pending items; other `always_invoice` update invoices exclude pre-existing pending items when the update itself produces invoice items. Flexible mode includes eligible pending items on update-generated invoices, including `always_invoice` and anchor resets, except that `payment_behavior=pending_if_incomplete` leaves pre-existing items pending. See November lines 255–263.

> [!warning] Contradiction
> The May section says flexible inclusion for anchor-reset invoices with `always_invoice`, but its table calls pending items "always included" on all subscription invoices and gives a narrower classic condition (May lines 204–210). The November capture scopes inclusion to the update-generated cases above. Do not apply either May table cell as a universal rule.

## Related

- [[stripe-subscriptions]] — subscription concept and qualified billing-mode comparison route
- [[source-stripe-subscriptions-billing-mode]] — billing mode guide and migration/version context

## Raw Sources

- [[raw/stripe-billing-subscriptions-billing-mode-compare-2026-11-07|Classic versus flexible comparison, captured 2026-11-07]]
- [[raw/stripe-subscriptions-billing-mode-compare-2026|Classic versus flexible comparison, captured 2026-05-13]]
