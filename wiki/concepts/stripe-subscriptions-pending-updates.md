---
title: "Stripe Subscription Pending Updates"
type: concept
category: framework
tags: [stripe, billing, subscriptions, pending-updates, payment-failure, webhooks]
---

## Overview

Pending updates is a Stripe feature that makes subscription changes conditional on successful payment. Without it, Stripe applies changes regardless of whether the new invoice pays — rollback on failure is a manual process. With pending updates, changes are held in a `pending_update` hash until the invoice succeeds or expires.

## When to use

Use pending updates for any invoice-generating subscription change where you want the update to only apply if payment succeeds. Typical cases:
- Upgrading a plan mid-period with `proration_behavior=always_invoice`
- Changing billing period
- Ending a trial that requires payment

## Prerequisites

- `collection_method=charge_automatically`
- Supported payment method (27 types): Card, Link, Alipay, Amazon Pay, Afterpay/Clearpay, Apple Pay, Cash App Pay, EPS, GoPay, Google Pay, Kakao Pay, Klarna, KR Card, Naver Pay, NG Card, PayPal, PayTo, Pix, PromptPay, Revolut Pay, Satispay, Stablecoins/crypto, Swish, TWINT, UPI, WeChat Pay

## How it works

```js
stripe.subscriptions.update(subId, {
  payment_behavior: 'pending_if_incomplete',
  proration_behavior: 'always_invoice',
  items: [{ id: subItemId, price: newPriceId }]
})
```

- **Payment succeeds**: subscription updated immediately, invoice marked `paid`
- **Payment fails**: `pending_update` hash on subscription holds changes; subscription unchanged

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

On repeated failure: `pending_update` remains with the original expiry; no changes applied.

## Canceling / changing pending updates

- **Cancel**: void the invoice (`subscription.latest_invoice` → `invoices.void`)
- **Change**: update subscription with new values — old invoice voided, new invoice created, new expiry set

## Supported attributes

Only attributes that control proration or generate invoices: `items` (price, quantity), `trial_end`, `trial_from_plan`, `billing_cycle_anchor`, `proration_behavior`, `proration_date`, `add_invoice_items`. Config and metadata attributes are NOT supported.

## Expiration

Expires at the earlier of:
- `trial_end` or earliest `items.current_period_end` if within 23h of the update request
- 23h from the update request (otherwise)

Auto-voided (update discarded) if: billing threshold hit, or subscription schedule phase transition.

## Webhooks

| Event | Purpose |
|---|---|
| `customer.subscription.updated` | Check `pending_update` hash; handle payment failures |
| `customer.subscription.pending_update_applied` | Provision/deprovision services after successful payment |
| `customer.subscription.pending_update_expired` | Retry update if needed |

## Metered items

- Outstanding usage billed on pending update invoice
- If expired before payment: usage is **discarded and unbillable** on any future invoice
- Exception: `billing_mode=flexible` bills usage when removing a metered price regardless

## Interaction with subscription schedules

A schedule phase change **discards** a pending update and voids the associated invoice. Retry the update after the phase transition if needed.

## Sources

- [[source-stripe-subscriptions-pending-updates]] — Stripe docs: full pending updates guide (prerequisites, lifecycle, supported attrs, expiry, metered items)
