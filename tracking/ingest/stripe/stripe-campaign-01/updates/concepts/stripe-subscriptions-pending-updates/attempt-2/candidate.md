---
title: "Stripe Subscription Pending Updates"
type: concept
category: framework
tags: [stripe, billing, subscriptions, pending-updates, payment-failure, webhooks]
---

## Overview

Pending updates normally hold an invoice-generating subscription change until payment succeeds. Without them, Stripe applies changes regardless of whether the new invoice pays, and rollback after failure is manual. A populated `pending_update` means the change has not yet applied. The November 7, 2026 guide states an exception: a resumption attempt that moves a paused subscription to `active` or `past_due` applies a matching pending update even if payment fails. See [[source-stripe-subscriptions-pending-updates]] and https://docs.stripe.com/billing/subscriptions/pending-updates.

> [!warning] Contradiction
> The May 13 guide described payment success as an unconditional gate; the November guide adds the paused-resumption exception and clarifies that a populated `pending_update` is not itself proof of payment failure.

## When to use

Use pending updates for invoice-generating subscription changes whose application should normally wait for payment, subject to that paused-resumption exception. Typical cases:
- Upgrading a plan mid-period with `proration_behavior=always_invoice`
- Changing billing period
- Ending a trial that requires payment

## Prerequisites

- `collection_method=charge_automatically`
- The November 7, 2026 guide lists 26 supported payment methods: Card, Link, Alipay, Amazon Pay, Afterpay/Clearpay, Apple Pay, Cash App Pay, EPS, GoPay, Google Pay, Kakao Pay, Klarna, KR Card, Naver Pay, NG Card, PayPal, PayTo, Pix, PromptPay, Revolut Pay, Satispay, Stablecoins/crypto, Swish, TWINT, UPI, WeChat Pay. This documentation list does not establish that each method is enabled for a particular account or customer.

## How it works

```js
stripe.subscriptions.update(subId, {
  payment_behavior: 'pending_if_incomplete',
  proration_behavior: 'always_invoice',
  items: [{ id: subItemId, price: newPriceId }]
})
```

- **Payment succeeds**: invoice becomes `paid` and Stripe applies the changes; with Billing and Payment Records these may finish in separate API requests. Use `customer.subscription.pending_update_applied` before dependent provisioning.
- **`pending_update` populated**: changes have not applied yet. Check invoice payment outcome before treating this as a failure; a reported payment might still be processing.

```json
{
  "pending_update": {
    "expires_at": 1571194285,
    "subscription_items": [{ "id": "si_...", "price": "price_..." }]
  }
}
```

## Handling failed payments

| Failure type | Action |
|---|---|
| Card decline | Attach new payment method → call `invoices.pay` on the pending invoice |
| 3DS required | Follow `requires_action` flow on the client |

If payment fails again while retrying the pending invoice in the ordinary flow, `pending_update` remains with its original expiry and no changes apply. The paused-subscription resumption exception above can still apply a matching update despite failed payment.

## Canceling / changing pending updates

- **Cancel**: void the invoice (`subscription.latest_invoice` → `invoices.void`)
- **Change**: update the subscription with new values — the previous invoice is voided and a new invoice is created. Successful payment of the new invoice applies the latest values; payment failure generates a replacement `pending_update` with a new expiry.

## Supported attributes

The update-subscription list includes `items` (price, quantity, discounts), trial and billing-cycle fields, proration fields, `add_invoice_items`, `metadata`, `discounts`, `cancel_at_period_end`, `coupon`, and `promotion_code`; subscription-item create/update also list `discounts`. This list does not mean every standalone field change invoices or becomes a pending update. The November guide still lists configuration changes as non-invoicing examples. For `add_invoice_items`, classic `always_invoice` can create an invoice while flexible mode leaves charges pending even with that setting. See [[source-stripe-subscriptions-pending-updates]] and https://docs.stripe.com/billing/subscriptions/pending-updates.

## Expiration

Expires at the earlier of:
- `trial_end` or earliest `items.current_period_end` if within 23h of the update request
- 23h from the update request (otherwise)

Auto-voided (update discarded) on billing threshold or schedule phase transition. A later update with `billing_cycle_anchor`, nonempty `items`, `trial_end`, or `trial_from_plan=true` also removes the pending update, as can conflicting discount or cancellation changes. Stripe compares discount IDs and order for those conflicts. See [[source-stripe-subscriptions-pending-updates]].

## Webhooks

| Event | Purpose |
|---|---|
| `customer.subscription.updated` | Check `pending_update` hash; handle payment failures |
| `customer.subscription.pending_update_applied` | Confirm the pending update was applied before dependent provisioning or deprovisioning; the paused-resumption exception can apply it even if payment fails |
| `customer.subscription.pending_update_expired` | Retry update if needed |

## Metered items

- Outstanding usage billed on pending update invoice
- If expired before payment: usage is **discarded and unbillable** on any future invoice
- Exception: `billing_mode=flexible` bills usage when removing a metered price regardless

Existing pending invoice items are separate from metered-usage loss and from the subscription's `pending_update`. The November guide says flexible-mode update invoices normally include eligible pending items, but `pending_if_incomplete` excludes pre-existing items, even on anchor reset. Classic anchor-reset invoices include eligible pending items; other `always_invoice` update invoices exclude them when the update itself produces invoice items. See [[source-stripe-subscriptions-pending-updates]].

## Interaction with subscription schedules

A schedule phase change **discards** a pending update and voids the associated invoice. Retry the update after the phase transition if needed.

## Sources

- [[source-stripe-subscriptions-pending-updates]] — Stripe docs: full pending updates guide (prerequisites, lifecycle, supported attrs, expiry, metered items)
