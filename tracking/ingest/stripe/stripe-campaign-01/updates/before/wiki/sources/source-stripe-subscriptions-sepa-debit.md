---
title: "Stripe Subscriptions — Set Up SEPA Direct Debit Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-sepa-debit-2026.md"
tags: [stripe, billing, subscriptions, sepa-debit, eur, europe, checkout, payment-element, delayed-notification]
---

## Summary

Integration guide for SEPA Direct Debit subscriptions. Two paths: Checkout (recommended) and Payment Element. Key: delayed notification payment method — do NOT fulfill on `checkout.session.completed`. Extensive IBAN test data for 20+ European countries (8 scenarios each).

## Two integration paths

### Path 1: Checkout (hosted)

```js
stripe.checkout.sessions.create({
  payment_method_types: ['sepa_debit'],
  line_items: [{ price: priceId, quantity: 1 }],
  mode: 'subscription',
  success_url: '...'
})
```

### Path 2: Payment Element (advanced)

Create subscription: `default_incomplete` + `save_default_payment_method='on_subscription'` → mount Payment Element → `stripe.confirmPayment({ return_url })` → SEPA redirects to Stripe-hosted confirmation → on return check PaymentIntent status.

## Delayed notification — key events

Do NOT fulfill on `checkout.session.completed` alone:

| Event | Action |
|---|---|
| `checkout.session.completed` | Customer authorized — wait |
| `checkout.session.async_payment_succeeded` | Funds confirmed → fulfill |
| `checkout.session.async_payment_failed` | Email customer |
| `invoice.paid` | Subscription renewal succeeded → fulfill |
| `invoice.payment_failed` | Contact customer |

## Optional Checkout features

- Setup fee: one-time + recurring `line_items`
- Inline pricing: `price_data` + `product_data`
- Existing customer: `customer` or `customer_account`
- Trials: `subscription_data.trial_period_days`
- Fixed tax rates: `subscription_data.default_tax_rates`
- Dynamic tax rates: `line_items.dynamic_tax_rates` (cannot mix with fixed)
- Coupons: `discounts[{coupon}]`
- Promo codes: `allow_promotion_codes: true`

## Test IBANs

8 scenarios per country: success, successDelayed (3 min), failed, failedDelayed, disputed, exceedsWeeklyVolumeLimit, exceedsWeeklyTransactionLimit, insufficientFunds.

Token format: `pm_{scenario}_{country_code}` (e.g. `pm_success_de`, `pm_disputed_fr`).

20+ countries covered: AT, BE, HR, EE, FI, FR, DE, GI, IE, LI, LT, LU, NL, NO, PT, SK, SI, ES, SE, CH, GB. Full IBAN tables in raw file.

## Related pages

- [[stripe-sepa-debit]] — concept page (updated with subscription facts)
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-sepa-debit-2026]] — verbatim Stripe docs webpage (1761 lines, 1 image reused)
