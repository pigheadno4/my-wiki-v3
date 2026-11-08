---
title: "Stripe Subscriptions — Pending Updates"
type: source
date_ingested: 2026-11-08
canonical_url: https://docs.stripe.com/billing/subscriptions/pending-updates
original_format: webpage
raw_files:
  - "stripe-billing-subscriptions-pending-updates-2026-11-07.md"
  - "stripe-subscriptions-pending-updates-2026.md"
tags: [stripe, billing, subscriptions, pending-updates, payment-failure, webhooks]
---

## Summary

Stripe's pending updates normally defer an invoice-generating subscription change until payment succeeds. The November 7, 2026 capture states an exception: when a resumption attempt moves a paused subscription to `active` or `past_due`, Stripe applies a matching pending update even if payment fails. A populated `pending_update` means changes have not applied yet; it does not alone establish payment failure. This is documentation behavior, not proof of an individual account's eligibility or payment outcome.

> [!warning] Contradiction
> The May 13 capture describes payment success as an unconditional gate and a populated `pending_update` as failed payment. The November 7 capture qualifies both claims with the paused-subscription resumption exception and possible Billing with Payment Records processing. Use the invoice outcome and the applied event for dependent actions.

## When an update generates an invoice

The November guide lists first payment (for example trial end), a changed billing period, and a proration with `proration_behavior=always_invoice` as invoice triggers. Many other changes apply immediately without a `pending_update`; if no invoice is created, Stripe makes no payment attempt. Examples include payment-method, tax, and retry configuration, billing threshold adjustments, and setting `cancel_at_period_end=true`.

`add_invoice_items` alone, when no other part of the update independently creates an invoice, is in that non-invoicing group. In classic billing mode, `proration_behavior=always_invoice` creates an invoice, so that combination is excluded from the non-invoicing example. In flexible mode, the one-time charges remain pending even with `always_invoice`. Pending invoice items and the subscription's `pending_update` are distinct.

The May capture also names metadata changes and coupons or promotion codes for future invoices as examples of changes without a new invoice. Its November successor omits those examples from this section but lists metadata and discount fields among supported pending-update attributes. The list alone does not establish that a standalone change to one of these fields generates an invoice or pending update.

## Default behavior, prerequisites, and request

By default, Stripe applies subscription updates regardless of payment outcome on the new invoice; rollback after failure is manual. With `payment_behavior=pending_if_incomplete`, the payment gate normally applies, subject to the paused-resumption exception above. The guide requires `collection_method=charge_automatically` and a payment method on its supported list. That documentation list is not evidence every method is enabled for a particular account or customer.

Set `payment_behavior=pending_if_incomplete` on update subscription, create subscription item, or update subscription item calls. The May capture shows a Node.js update example; the November capture renders a cURL example. Both use `proration_behavior=always_invoice` for an invoice-generating price change. The change of example format does not establish removal of Node.js support.

```js
// May 13, 2026 documentation example, abbreviated
stripe.subscriptions.update(subId, {
  payment_behavior: 'pending_if_incomplete',
  proration_behavior: 'always_invoice',
  items: [{ id: subItemId, price: newPriceId }]
})
```

## Observe and resolve a pending update

The returned Subscription object might not yet reflect an applied update. A failed card payment is one example in which it contains `pending_update`, including `expires_at`. More generally, a populated hash means the update has not applied yet, not necessarily that payment failed. Billing with Payment Records might still be processing a reported payment, so inspect payment outcome on the invoice before handling it as failure.

For a card decline, attach a new payment method and pay the generated invoice with the invoice pay endpoint. For required customer authentication, follow the `requires_action` flow. A successful payment marks the invoice `paid` and causes Stripe to apply the change. With Billing and Payment Records, those steps might finish in different API requests. Wait for `customer.subscription.pending_update_applied` before provisioning or other dependent actions. On repeated payment failure, the pending update retains its original expiry.

Stripe suspends invoices scheduled by `pending_invoice_item_interval` while `pending_update` is populated. Interval invoicing resumes after application, cancellation, or expiry.

## Cancel or replace

Void the invoice identified by `subscription.latest_invoice` to cancel a pending update. Updating a subscription with replacement values voids the previous invoice and creates a new invoice. Successful payment applies the most recent values; failure produces a new pending update and expiration.

## Supported attributes

The November guide lists these for the update-subscription endpoint: `expand`, `payment_behavior`, `proration_behavior`, `proration_date`, `billing_cycle_anchor`, `items` (`price`, `quantity`, `discounts`), `trial_end`, `trial_from_plan`, `metadata`, `discounts`, `cancel_at_period_end`, `coupon`, `promotion_code`, and `add_invoice_items`. Create/update subscription item supports `expand`, `payment_behavior`, `proration_behavior`, `proration_date`, `price`, `quantity`, and `discounts`. These are endpoint-specific lists in the pending-updates guide, not a claim that every standalone field change invoices or is held pending. Configuration changes are non-invoicing examples above.

## Expiration and automatic removal

The `expires_at` time is the first trial end or earliest subscription-item current-period end if one falls within 23 hours of the update request; otherwise it is 23 hours after the request. The May prose spells this `expired_at`, while its JSON example and the November prose use `expires_at`.

Stripe also voids the invoice and removes the pending update if a billing threshold is reached or a linked subscription schedule enters a new phase. A later update with `billing_cycle_anchor`, a nonempty `items` list, `trial_end`, or `trial_from_plan=true` removes it even when values match. Conflicting discount or cancellation updates can also remove it: `discounts`, legacy `coupon` or `promotion_code`, `cancel_at_period_end`, or `cancel_at`. For discount conflicts, Stripe compares discount IDs and order; resubmitting even the same coupon or promotion code creates a new discount, while reusing the same discount IDs in the same order does not conflict.

## Events and schedules

The same event names apply to Customer objects and customer-configured Account objects: `customer.subscription.updated` to inspect changes, `customer.subscription.pending_update_applied` to confirm application before dependent actions, and `customer.subscription.pending_update_expired` for expiry or automatic void. A schedule phase change discards the pending update and voids its invoice; retry after that transition if needed.

## Metered usage and existing invoice items

The pending-update invoice bills outstanding metered usage. If the pending update expires unpaid, that usage is discarded and is not billed on later invoices. Usage reported between creation of a pending update that removes a metered price and payment of its invoice is also disregarded; the November guide qualifies that flexible billing charges usage when removing the metered price.

Existing pending invoice items have separate inclusion rules. In flexible mode, update invoices normally include eligible pending items, but `payment_behavior=pending_if_incomplete` excludes pre-existing pending items, even on billing-cycle-anchor reset, leaving them pending. In classic mode, anchor-reset invoices include eligible pending items; other `always_invoice` update invoices exclude them when the update itself produces invoice items such as prorations.

## Related pages

- [[stripe-subscriptions-pending-updates]] — concept page
- [[stripe-subscriptions-prorations]] — proration behavior options
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-billing-subscriptions-pending-updates-2026-11-07]] — Stripe guide captured November 7, 2026
- [[stripe-subscriptions-pending-updates-2026]] — Stripe guide captured May 13, 2026
