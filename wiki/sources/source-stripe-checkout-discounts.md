---
title: "Stripe Checkout: Add Discounts"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-discounts-upsells-2025.md"
  - "stripe-checkout-discounts-2025.md"
  - "stripe-checkout-no-cost-orders-2025.md"
tags: [stripe, checkout, discounts, coupons, promotion-codes, coupon-api, no-cost-orders, free-orders]
---

## Summary

Guide for applying discounts in Stripe Checkout via coupons and promotion codes. Covers the Coupon API, applying coupons to sessions, creating customer-facing promotion codes with restrictions, and promotion code lifecycle.

## Key Takeaways

- **Max 1 discount per session**: `discounts` array supports only one coupon or promotion code
- **Two layers**: Coupon (server-side, fixed value) → Promotion Code (customer-facing, maps to coupon)
- **Apply coupon**: `discounts: [{ coupon: 'COUPON_ID' }]` on session create
- **Enable promo code input**: `allow_promotion_codes: true` on session create
- **Coupon params**: `percent_off` or `amount_off`, `currency`, `max_redemptions`, `redeem_by`, `applies_to` (product IDs)
- **Subscription discounts**: handled separately in Billing — see Billing docs for `duration` and subscription-specific behavior

## Coupon API

```js
stripe.coupons.create({
  percent_off: 20,   // or amount_off: 500
  duration: 'once',  // 'once' | 'repeating' | 'forever' (subscriptions only)
  max_redemptions: 50,
  redeem_by: 1735689600,  // Unix timestamp
  applies_to: { products: ['prod_...'] },  // limit to specific products
})
```

Multiple promotion codes can map to one coupon: `FALLPROMO` and `SPRINGPROMO` → same 25% coupon.

## Promotion Code Restrictions

| Restriction | Param | Notes |
| --- | --- | --- |
| Specific customer | `customer` | Omit for any customer |
| First-time orders | `restrictions.first_time_transaction` | Guest customers count as first-time |
| Minimum amount | `restrictions.minimum_amount` + `minimum_amount_currency` | Checked at redemption; only initial payment for subscriptions |
| Expiration | `expires_at` | Can't exceed coupon's `redeem_by`; inherits coupon `redeem_by` if unset |
| Redemption limit | `max_redemptions` | Can't exceed coupon's `max_redemptions` |

## Code Uniqueness Rules

- Case-insensitive
- Customer-restricted codes: same `code` can be reused across different customers
- General-use codes: must be unique across all active general-use codes
- Inactivate with `active: false` → can reuse code for a new promotion code

## Promotion Code Lifecycle

- **Permanently inactive** when: underlying coupon becomes invalid, `max_redemptions` reached, or `expires_at` passed
- Cannot be reactivated once permanently inactive
- Deleting prevents future use but doesn't affect past redemptions

## No-Cost Orders

- **Requires**: API version 2023-08-16 or later
- **Path 1**: `unit_amount: 0` on price/`price_data` — Checkout skips payment method collection; guest customers not supported (auto-creates Customer)
- **Path 2**: 100% off coupon or promotion code (also works if coupon ≥ total)
- **Fulfillment**: handle `checkout.session.completed` — NOT PaymentIntent events; free sessions have no associated PaymentIntent
- **Payment Links + Pricing Tables**: default for accounts created after Aug 17, 2023; older accounts enable in Checkout Settings (3-day grace period — cannot disable after 3 days)
- **Testing sandbox**: use `+no_cost_orders` email suffix (e.g., `j.appleseed+no_cost_orders@example.com`)

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page
- [[stripe-subscriptions]] — Subscription discounts handled in Billing (see `duration` param)

## Raw Sources

- [[stripe-checkout-discounts-upsells-2025]] — Navigation index: discounts, free trials, upsells, optional items, no-cost orders
- [[stripe-checkout-discounts-2025]] — Coupon API, apply to session, promotion codes, all restriction params, uniqueness rules, lifecycle
- [[stripe-checkout-no-cost-orders-2025]] — No-cost orders: unit_amount=0 path, 100% coupon path, fulfillment via checkout.session.completed only, guest customer limitation, Payment Links/pricing tables opt-in, sandbox testing
