---
title: "Stripe Subscription Coupons and Promotion Codes"
type: concept
category: technology
tags: [stripe, subscriptions, coupons, promotion-codes, discounts, stackable]
---

## Overview

Coupons define discounts (percentage or fixed amount) applied to subscriptions. Promotion codes are customer-facing codes that map to coupons. Both can be stacked (up to 20 per subscription/item).

## Coupons

```js
stripe.coupons.create({ duration: 'once'|'forever'|'repeating', percent_off|amount_off, ... })
```

- Only `name` editable after creation
- `applies_to`: restrict to specific product IDs
- `max_redemptions`: limit across all customers; `redeem_by`: expiration
- Deleting prevents future use but doesn't remove existing discounts

**Duration behaviors**:
- `once` — applies to first invoice; **removed from `subscription.discounts` after invoice finalizes** (sub may appear to have no discount)
- `repeating` — `duration_in_months` months
- `forever` — all invoices indefinitely
- Backdating: duration counts from backdate start date, not API call time

## Promotion Codes

Customer-facing codes (`FALLPROMO` → 25% off coupon). Multiple codes per coupon.

- Case-insensitive; unique across active codes
- Restrictions: `first_time_transaction`, `minimum_amount` (checked at redemption — first payment only), `expires_at`, `max_redemptions`, specific `customer`
- Deactivate via `active: false`; permanently inactive once expired or max reached
- **Cannot apply with amount restrictions** to: Subscription Items, Invoice Items, subscription updates, future schedule phases

## Stackable Discounts

Apply discounts at both subscription level and subscription item level. Up to 20 per `discounts[]`.

- Order matters: `percent_off` before `amount_off` = different total than reverse
- Must include all desired discounts when updating (pass old + new)
- `discounts: ""` clears all
- Updating discounts alone doesn't trigger prorations — only when combined with proration-triggering changes (quantity change, price change, etc.)

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
