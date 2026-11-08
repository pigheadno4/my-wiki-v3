---
title: "Stripe Subscription Coupons and Promotion Codes"
type: concept
category: technology
tags: [stripe, subscriptions, coupons, promotion-codes, discounts, stackable]
---

## Overview

Coupons define percentage or fixed-amount discounts, and customer-facing promotion codes map to coupons. The 2026-11-07 guide states up to 20 coupon- or code-derived discounts on a subscription, subscription item, **or invoice**; it does not establish one combined budget across those objects. See [[source-stripe-subscriptions-coupons]].

## Coupons

```js
stripe.coupons.create({ duration: 'once'|'forever'|'repeating', percent_off|amount_off, ... })
```

- Only `name` editable after creation
- `applies_to`: restrict to specific product IDs
- `max_redemptions`: coupon limit across all customers; direct coupon applications and promotion-code redemptions both consume that coupon's counter. `redeem_by`: expiration. See [[source-stripe-subscriptions-coupons]] (2026-11-07 lines 209–215).
- Deleting prevents future use but doesn't remove existing discounts

**Duration behaviors**:
- `once` — applies to first invoice; **removed from `subscription.discounts` after invoice finalizes** (sub may appear to have no discount)
- `repeating` — `duration_in_months` months
- `forever` — all invoices indefinitely
- Backdating: duration counts from backdate start date, not API call time

## Promotion Codes

Customer-facing codes (`FALLPROMO` → 25% off coupon). Multiple codes per coupon.

- Case-insensitive. Distinct customer-restricted active codes may reuse a string; an active code redeemable by any customer cannot share that string with another active code. An inactivated string can be reused. See [[source-stripe-subscriptions-coupons]] (2026-05-13 lines 265–281; 2026-11-07 lines 245–261).
- Restrictions: `first_time_transaction`, `minimum_amount` (checked at redemption — first payment only), `expires_at`, `max_redemptions`, specific `customer`
- Deactivate via `active: false`; permanently inactive once expired or max reached
- **Cannot apply with amount restrictions** to: Subscription Items, Invoice Items, subscription updates, future schedule phases

## Stackable Discounts

Apply discounts at subscription and subscription-item levels. The 2026-11-07 guide also states a limit of up to 20 on an invoice; coupon- and promotion-code-derived discounts share each stated target limit. The 2026-05-13 stacking section says up to 20 entries per `discounts` parameter. See [[source-stripe-subscriptions-coupons]].

- Order matters: `percent_off` before `amount_off` = different total than reverse
- Must include all desired discounts when updating (pass old + new)
- `discounts: ""` clears all
- Updating discounts alone creates neither prorations nor an invoice. A separate billable current-cycle change, such as a quantity or price change, can trigger proration; if combined in the same call, the proration uses the updated discount state. See [[source-stripe-subscriptions-coupons]] (2026-05-13 lines 583–587; 2026-11-07 lines 499–503).

## Apply via Checkout

```js
stripe.checkout.sessions.create({ allow_promotion_codes: true }) // shows promo code box
// OR:
stripe.checkout.sessions.create({ discounts: [{ coupon: 'id' }] }) // pre-applied
```

## Alternative Discount Methods

Negative customer balance, negative invoice items, cheaper price object.

## Sources

- [[source-stripe-subscriptions-coupons]] — full guide: coupon creation, promotion code restrictions, stackable discounts, alternative methods
