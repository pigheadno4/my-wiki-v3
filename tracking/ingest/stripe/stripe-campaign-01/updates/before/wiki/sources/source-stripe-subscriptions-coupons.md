---
title: "Stripe — Coupons and Promotion Codes for Subscriptions"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-coupons-2026.md"
tags: [stripe, subscriptions, coupons, promotion-codes, discounts, stackable]
---

## Summary

Comprehensive guide to subscription discounts via coupons and promotion codes. Covers creation, duration behavior, stackable discounts, promotion code restrictions, and alternative discount methods.

## Coupon Duration Behavior

- `once` — applies to first invoice; removed from `subscription.discounts` after invoice finalizes (sub may appear to have no discount)
- `repeating` — applies for `duration_in_months` months
- `forever` — applies indefinitely
- **Backdating**: duration counts from backdate start date (not API call time)

## Key Coupon Facts

- Only `name` is editable after creation
- `applies_to` restricts to specific product IDs
- `max_redemptions` = limit across all customers; `redeem_by` = expiration date
- Deleting prevents future use but doesn't remove existing discounts

## Promotion Codes

Customer-facing codes mapped to coupons. Multiple codes can map to one coupon.

- Case-insensitive; unique across active codes
- Restrictions: `first_time_transaction`, `minimum_amount`, `expires_at`, `max_redemptions`, specific `customer`
- Deactivate: `active: false`; cannot reactivate once expired or max redeemed
- **Cannot apply with amount restrictions** to Subscription Items, Invoice Items, subscription updates, or future schedule phases

## Stackable Discounts

Up to 20 discounts per `discounts[]` array; applies at subscription + item level.

- Order matters: `percent_off` + `amount_off` sequence affects total
- Updating discounts: must include all desired discounts (old + new); `discounts: ""` clears all
- Updating discounts alone doesn't create prorations; only when combined with proration-triggering changes

## Alternative Discount Methods

Negative customer balance, negative invoice items, cheaper price object.

## Related Pages

- [[stripe-subscriptions-coupons]] — concept page
- [[stripe-subscriptions]] — subscriptions context

## Raw Sources

- [[stripe-subscriptions-coupons-2026]] — verbatim coupons guide (605 lines, 1 image)
