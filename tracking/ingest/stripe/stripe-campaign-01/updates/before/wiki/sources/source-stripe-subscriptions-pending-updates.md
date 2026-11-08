---
title: "Stripe Subscriptions — Pending Updates"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-pending-updates-2026.md"
tags: [stripe, billing, subscriptions, pending-updates, payment-failure, webhooks]
---

## Summary

Guide to pending updates — a feature that gates subscription changes on successful payment, preventing manual rollback if the new invoice fails.

## When a subscription update generates a new invoice

- Subscription requires payment for the first time (e.g. trial end)
- Billing period changes
- Proration with `proration_behavior=always_invoice`

Does NOT generate an invoice (and therefore doesn't trigger pending updates): config changes, metadata, discount-only, billing thresholds, `cancel_at_period_end`, `add_invoice_items`.

## Default vs pending updates behavior

- **Default**: Stripe applies updates regardless of payment outcome — rollback on failure is manual
- **With pending updates** (`payment_behavior=pending_if_incomplete`): changes are held back until the new invoice is successfully paid

## Prerequisites

- `collection_method=charge_automatically`
- Payment method must be one of 27 supported types: Card, Link, Alipay, Amazon Pay, Afterpay/Clearpay, Apple Pay, Cash App Pay, EPS, GoPay, Google Pay, Kakao Pay, Klarna, KR Card, Naver Pay, NG Card, PayPal, PayTo, Pix, PromptPay, Revolut Pay, Satispay, Stablecoins/crypto, Swish, TWINT, UPI, WeChat Pay

## Usage

Set `payment_behavior=pending_if_incomplete` on the update:

```js
stripe.subscriptions.update(subId, {
  payment_behavior: 'pending_if_incomplete',
  proration_behavior: 'always_invoice',
  items: [{ id: subItemId, price: newPriceId }]
})
```

On payment failure, the returned subscription has a `pending_update` hash containing the held-back changes and an `expires_at` timestamp. The subscription is NOT updated yet.

## Handling failed payments

- **Card decline**: attach new payment method, then call `invoices.pay` on the invoice the update generated
- **3DS/auth required**: follow the `requires_action` flow
- On success: changes in `pending_update` are applied immediately; invoice marked `paid`
- On repeated failure: `pending_update` remains with the original expiry; no changes applied

## Canceling or changing pending updates

- **Cancel**: void the invoice (`latest_invoice` on subscription → `invoices.void`)
- **Change**: update the subscription with new values — voids old invoice, creates new one, new expiry

## Supported attributes

Limited to proration/invoice-generating attributes: `items` (price, quantity), `trial_end`, `trial_from_plan`, `billing_cycle_anchor`, `proration_behavior`, `proration_date`, `proration_date`, `add_invoice_items`, `expand`, `payment_behavior`. Does NOT support metadata, config, or discount attributes.

## Expiration

Pending update expires at whichever comes first:
- `trial_end` or earliest `items.current_period_end` — if within 23h of the update request
- 23h from the update request (otherwise)

Also auto-voided (and update discarded) if: billing threshold hit, or subscription schedule transitions to a new phase.

## Webhooks

| Event | Purpose |
|---|---|
| `customer.subscription.updated` | Check `pending_update` hash; handle payment failures |
| `customer.subscription.pending_update_applied` | Provision/deprovision after successful payment |
| `customer.subscription.pending_update_expired` | Retry update if needed |

## Metered items edge cases

- Outstanding usage billed on pending update invoice
- If update expires before payment: usage is discarded and cannot be billed on any subsequent invoice
- Exception: `billing_mode=flexible` — Stripe bills for usage even when removing a metered price

## Related pages

- [[stripe-subscriptions-pending-updates]] — concept page
- [[stripe-subscriptions-prorations]] — proration behavior options
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-pending-updates-2026]] — verbatim Stripe docs webpage
