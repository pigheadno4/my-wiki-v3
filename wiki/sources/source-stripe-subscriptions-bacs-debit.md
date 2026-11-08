---
title: "Stripe Subscriptions — Set Up Bacs Direct Debit Subscription"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/bacs-debit"
raw_files:
  - "stripe-billing-subscriptions-bacs-debit-2026-11-07.md"
  - "stripe-subscriptions-bacs-debit-2026.md"
tags: [stripe, billing, subscriptions, bacs, uk, direct-debit, checkout]
---

## Summary

Stripe's Bacs Direct Debit subscription guide uses Checkout: a client checkout button calls a server endpoint that creates a subscription-mode Checkout Session with at least one recurring Price. This page does not establish that other Bacs subscription integration paths are unavailable. It covers delayed-payment webhooks, test accounts, optional pricing, trials, taxes, coupons, and one-time setup fees. The 2026-11-07 capture adds an explicit payment-success plus active-subscription fulfillment check, allows repeat sandbox-to-live product copies, and deprecates `line_items.dynamic_tax_rates`.

## Integration: Checkout path in this guide

The 2026-05-13 Node.js example below explicitly selects `bacs_debit`. The 2026-11-07 curl examples omit `payment_method_types` while the prose directs enabling desired payment methods in the Dashboard; the omission alone does not establish automatic Bacs selection, parameter removal, or eligibility for a particular account.

```js
stripe.checkout.sessions.create({
  payment_method_types: ['bacs_debit'],
  line_items: [{ price: priceId, quantity: 1 }],
  mode: 'subscription',
  success_url: '...'
})
```

## Delayed notification — key webhook events

Bacs is a delayed-notification method. `checkout.session.completed` records debit authorization, not payment success. In the 2026-11-07 guide, a subscription can be `active` while its first payment is processing. Before fulfilling goods or services, verify the related subscription is `active` and wait for `invoice.paid` or confirm that the underlying PaymentIntent is `succeeded`. Payment success does not itself prove funds are already available or a bank receipt.

| Event | Action |
|---|---|
| `checkout.session.completed` | Customer authorized debit — wait |
| `checkout.session.async_payment_succeeded` | Delayed payment succeeded; verify related subscription is `active` before fulfillment |
| `checkout.session.async_payment_failed` | Email customer to retry |
| `invoice.paid` | Payment succeeded; verify related subscription is `active` before fulfillment |
| `invoice.payment_failed` | Contact customer |

## Optional features via Checkout

- **Setup fee**: add a one-time price alongside recurring price in `line_items` — appears on initial invoice only
- **Inline pricing**: use `price_data` + `product_data` to create products/prices inline without pre-registering them
- **Trial**: `subscription_data.trial_period_days` or `trial_end`
- **Fixed tax rates**: `subscription_data.default_tax_rates` or `line_items.tax_rates`
- **Dynamic tax rates (deprecated)**: the 2026-11-07 guide labels `line_items.dynamic_tax_rates` deprecated; use Stripe Tax or `line_items.tax_rates` instead. For legacy use, it cannot be combined with `subscription_data.default_tax_rates` or `line_items.tax_rates`.
- **Coupons**: `discounts: [{coupon: id}]` on session
- **Promo codes**: `allow_promotion_codes: true`
- **Existing customer**: pass `customer` or `customer_account` to pre-fill email

## Sandbox behavior

- Bacs debit notification emails are **NOT sent** in sandboxes
- Sandbox test outcomes vary: some payment-success and failure cases take about three minutes, and one success case immediately creates a dispute. Do not read a test payment outcome as proof of live settlement.
- Use **delayed test accounts** (3-min processing) to better simulate live behavior

## Test accounts (sort code `10-88-00`)

| Account | Token | Behavior |
|---|---|---|
| `00012345` | `pm_bacsDebit_success` | Instant success |
| `90012345` | `pm_bacsDebit_successDelayed` | Success after 3 min |
| `33333335` | `pm_bacsDebit_debitNotAuthorized` | Fails; mandate → inactive |
| `93333335` | `pm_bacsDebit_debitNotAuthorizedDelayed` | Fails after 3 min; mandate → inactive |
| `22222227` | `pm_bacsDebit_insufficientFunds` | Fails; mandate stays active |
| `92222227` | `pm_bacsDebit_insufficientFundsDelayed` | Fails after 3 min; mandate stays active |
| `55555559` | `pm_bacsDebit_dispute` | Success after 3 min then dispute |
| `00033333` | `pm_bacsDebit_mandateRefused` | PM created but mandate → inactive immediately |
| `00044444` | — | Fails immediately; customer prompted to update |

## Product sandbox→live note

The 2026-11-07 guide allows copying the same sandbox product to live mode more than once. Each copy is a separate live product; later sandbox changes do not update existing live copies.

> [!warning] Contradiction
> The 2026-05-13 capture said a sandbox product could be copied to live only once. The 2026-11-07 capture explicitly permits repeat copies. Preserve the old limit as dated historical wording, not a current restriction.

## Related pages

- [[stripe-bacs-direct-debit]] — concept page (updated with subscription facts)
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-billing-subscriptions-bacs-debit-2026-11-07|2026-11-07 Bacs subscription guide]] — Checkout path, payment confirmation, sandbox-copy and tax updates
- [[raw/stripe-subscriptions-bacs-debit-2026|2026-05-13 Bacs subscription guide]] — historical Node.js rendering and once-only copy statement
