---
title: "Stripe Subscriptions — Prorations"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/prorations"
raw_files:
  - "stripe-billing-subscriptions-prorations-2026-11-07.md"
  - "stripe-subscriptions-prorations-2026.md"
tags: [stripe, billing, subscriptions, prorations, credit-prorations, billing-mode]
---

## Summary

Stripe's same-URL May and November 2026 guides explain proration invoice items for subscription changes, discount treatment, credit calculation in classic versus flexible billing mode, preview, and `proration_behavior`. The November guide adds an operation-based classification matrix, conditional credit-to-debit attribution, optional time granularity customization, and clearer limits on disabling prorations. Its examples are documentation illustrations, not observed payment outcomes.

## Identify proration items

Use Invoice item `proration` or Invoice line item `parent.subscription_item_details.proration` to identify Stripe's classification. Stripe bases it on the **operation that creates the item**, not just whether its service period is partial. A scheduled phase transition behaves like a subscription update for classification. A single operation may create both proration and non-proration items; a manually created negative invoice item is not automatically a proration.

The November matrix calls subscription billing credits, backdated-period items, some anchor-created debits even for a full period, trial-offer updates without a trial-status change, and renewals shortened by `cancel_at` prorations. It calls ordinary full-period creation/update debits, trial-start/end debits, certain free-trial updates, and some renewal debits non-prorations. See new raw lines 24–48 for exact scenario boundaries.

> [!warning] Contradiction
> The May source summary described mid-period changes as though each always creates both an unused-time credit and a remaining-time debit. The November classification explicitly includes credit-only or debit-only scenarios and mixed proration/non-proration operations. The paired credit/debit calculation below is one price-upgrade example, not a universal item shape.

## How prorations work

In the guide's illustrative halfway upgrade from a 10 USD monthly plan to 20 USD, a -5 USD unused-time credit and +10 USD remaining-time debit yield a net +5 USD invoice amount. Negative prorations are not automatically refunded; positive prorations are not immediately billed by default. Neither this arithmetic nor an invoice total proves payment.

Stripe calculates prorations to the second by default. The November page links optional Stripe-authored and custom proration scripts for different granularity or calculations; the capture does not establish availability for any particular account. Prorations apply to charges ahead of the billing period, not usage-based billing.

## Discounts and common update triggers

Proration items have `discountable=false`; existing subscription discounts affect their calculated amount, but invoice discounts do not apply again to those items. Non-proration lines can show `discount_amounts`. A discount-only change does not generate proration items; when a discount change and a proration trigger share a request, Stripe uses the modified discount state for proration calculation.

The guide's common default triggers are adding/removing subscription items, changing price or quantity, adding a trial to an active subscription, moving the billing cycle anchor, and setting `cancel_at` mid-period. Its non-trigger table includes configuration and metadata changes and future billing settings such as discounts, billing thresholds, `cancel_at_period_end`, and `add_invoice_items` (new raw 83–125; May raw 41–83). This table describes **proration items**, not all invoice or billing activity. Manually adding a negative `unit_amount` with `add_invoice_items` is a separate path and does not by itself make that item a Stripe-classified proration.

## Unpaid invoices

Stripe computes prorations assuming prior subscription invoices will eventually be paid. A change while the current-period invoice is unpaid can credit unused time the customer never paid for. The guide suggests `proration_behavior=none` on that update, then either a one-off invoice while retaining the billing period or `billing_cycle_anchor=now` to reset it. It warns that the old invoice can later cause double payment and says to void that unpaid invoice. See new raw lines 142–151 and May raw lines 100–109.

## Proration behavior

| Value | Documented effect |
|---|---|
| `create_prorations` (default) | Creates applicable proration items. Immediate invoicing occurs only under certain conditions; period-end invoicing is not guaranteed by this setting alone. |
| `always_invoice` | Calculates prorations and immediately **generates an invoice** for the change; this does not establish successful collection. |
| `none` | Disables prorations for that request; it does not stop non-proration items such as regular renewal or full-period subscription items. Repeat on each relevant request to suppress future prorations. |

When canceling, the November page says proration can be disabled only if `cancel_at` is within the current billing period; a date outside the current period does not permit it (new raw 721–749). The guide also says that when prorations are disabled, customers are billed the full new price when the next invoice is generated; this is conditional on that invoice.

## Credit prorations: classic versus flexible

In the documented example, an upgrade from 10 to 20 USD used `proration_behavior=none`, so no upgrade debit was billed. A later downgrade produces a classic-mode credit based on the current 20 USD price (-6.67 USD) plus a 3.33 USD debit, for a -3.34 USD example invoice total. Flexible mode uses the **last billed** 10 USD price, so the 3.33 USD credit and debit cancel to a zero example invoice total (new raw 172–251; May raw 119–223). “Last billed” does not mean the invoice was paid.

For an `amount_off` coupon across items, the guide's example allocates a 5 USD coupon differently: classic shows a -2.50 USD credit; flexible uses proportional original invoice `discount_amounts` and shows -4.17 USD (new raw 253–337; May raw 225–332). These are sample invoice totals, not refunds or payment receipts.

> [!warning] Contradiction
> The former source summary said flexible mode was more accurate to what the customer “actually paid.” The raw example establishes the last **price billed** and example invoice totals. It does not establish whether the customer paid either invoice; the guide separately warns about unpaid invoices.

### Credit attribution metadata

When Stripe can attribute a credit proration Invoice item to its original debit, `proration_details.credited_items` identifies it. Type `invoice_item` points to a pending debit item; type `invoice_line_items` points to one or more debit lines on an existing invoice, including tiered cases. In classic mode `proration_details` can be absent when Stripe cannot identify the original debit. This is reconciliation metadata, not proof of payment or a guarantee every credit has a link (new raw 161–170).

## Preview a proration

A preview invoice uses the proposed subscription change without modifying the subscription. Because default calculation is second-level, pass the same `subscription_details.proration_date` in the preview and `proration_date` in the actual update to hold the calculation time steady. The May source showed this with Node.js; the November selected examples use Ruby. Both retain separate Accounts v2 `customer_account` and Customers v1 `customer` identity paths (new raw 339–405; May raw 334–400).

The sample preview response has `amount_paid=0`, `attempted=false`, `paid=false`, and `status=draft`. It is not a finalized or paid invoice (new raw 418–425, 665–680). The old Node.js form was:

```js
stripe.invoices.createPreview({
  customer: customerId,
  subscription: subId,
  subscription_details: { items, proration_date }
})
```

## Related pages

- [[stripe-subscriptions-prorations]] — concept page
- [[stripe-subscriptions]] — concept page
- [[source-stripe-subscriptions-change-price]] — price change guide
- [[source-stripe-subscriptions-modify]] — subscription update overview
- [[source-stripe-subscriptions-billing-mode-compare]] — classic versus flexible comparison
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-billing-subscriptions-prorations-2026-11-07|Stripe prorations guide, November 7 2026]] — updated same-URL capture
- [[raw/stripe-subscriptions-prorations-2026|Stripe prorations guide, May 13 2026]] — historical capture
