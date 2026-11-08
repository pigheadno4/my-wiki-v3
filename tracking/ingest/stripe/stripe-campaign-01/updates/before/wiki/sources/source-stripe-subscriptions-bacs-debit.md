---
title: "Stripe Subscriptions — Set Up Bacs Direct Debit Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-bacs-debit-2026.md"
tags: [stripe, billing, subscriptions, bacs, uk, direct-debit, checkout]
---

## Summary

Integration guide for Bacs Direct Debit subscriptions via Stripe Checkout. Checkout-only path — no Elements/custom UI variant. Covers test accounts, delayed notification webhooks, inline pricing, trials, tax rates, coupons, and setup fees.

## Integration: Checkout only

```js
stripe.checkout.sessions.create({
  payment_method_types: ['bacs_debit'],
  line_items: [{ price: priceId, quantity: 1 }],
  mode: 'subscription',
  success_url: '...'
})
```

## Delayed notification — key webhook events

Bacs is async. Do NOT fulfill on `checkout.session.completed` alone:

| Event | Action |
|---|---|
| `checkout.session.completed` | Customer authorized debit — wait |
| `checkout.session.async_payment_succeeded` | Funds confirmed → fulfill |
| `checkout.session.async_payment_failed` | Email customer to retry |
| `invoice.paid` | Subscription renewal succeeded → fulfill |
| `invoice.payment_failed` | Contact customer |

## Optional features via Checkout

- **Setup fee**: add a one-time price alongside recurring price in `line_items` — appears on initial invoice only
- **Inline pricing**: use `price_data` + `product_data` to create products/prices inline without pre-registering them
- **Trial**: `subscription_data.trial_period_days` or `trial_end`
- **Fixed tax rates**: `subscription_data.default_tax_rates` or `line_items.tax_rates`
- **Dynamic tax rates**: `line_items.dynamic_tax_rates` (cannot mix with fixed)
- **Coupons**: `discounts: [{coupon: id}]` on session
- **Promo codes**: `allow_promotion_codes: true`
- **Existing customer**: pass `customer` or `customer_account` to pre-fill email

## Sandbox behavior

- Bacs debit notification emails are **NOT sent** in sandboxes
- Test transactions settle instantly (live transactions take multiple days)
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

Sandbox products can be copied to live once via Dashboard ("Copy to live mode"). Subsequent updates to sandbox product do NOT sync to live.

## Related pages

- [[stripe-bacs-direct-debit]] — concept page (updated with subscription facts)
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-bacs-debit-2026]] — verbatim Stripe docs webpage (692 lines, 1 image reused)
