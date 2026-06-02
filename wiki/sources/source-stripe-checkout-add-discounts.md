---
title: "Add Discounts (Checkout Sessions)"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-checkout-add-discounts-2025.md"
tags: [stripe, checkout-sessions, discounts, coupons, promotion-codes, applyPromotionCode, elements]
---

## Summary

Comprehensive reference for Coupons and Promotion Codes in Checkout Sessions with the Elements UI. Adds client-side API for applying/removing promotion codes. Supplementary to [[source-stripe-checkout-discounts]].

## Client-Side Promotion Code API

This is the key new content vs the existing discounts source:

```js
// HTML+JS — apply
actions.applyPromotionCode(input.value).then((result) => {
  if (result.error) { /* show error */ }
  else { input.value = ''; }
});

// HTML+JS — remove ALL applied codes
actions.removePromotionCode();

// React equivalents from checkoutState.checkout:
// applyPromotionCode(code) / removePromotionCode()
```

> `removePromotionCode()` removes **all** applied promotion codes, not just one.

## Session Setup for Promotion Codes

```js
// Allow customer-entered codes
stripe.checkout.sessions.create({ allow_promotion_codes: true, ... });

// Server-apply a coupon directly
stripe.checkout.sessions.create({ discounts: [{ coupon: 'COUPON_ID' }], ... });
// Max 1 coupon or promotion code per session
```

## Key Coupon Facts

- Multiple promo codes can map to one coupon (e.g. `FALLPROMO` + `SPRINGPROMO` → same 25% off coupon)
- `applies_to`: limits eligible product IDs; any promo codes on that coupon also inherit the restriction
- `code` is case-insensitive; unique across active codes for any customer

## Permanent Inactivation

Promotion codes become **permanently inactive** (cannot reactivate) when:
- The underlying coupon becomes invalid
- `max_redemptions` is reached
- `expires_at` is passed

## Related Pages

- [[source-stripe-checkout-discounts]] — existing discounts source (more detail on Coupon API + restrictions)
- [[stripe-checkout]] — Checkout concept page

## Raw Sources

- [[stripe-checkout-add-discounts-2025]] — verbatim discounts guide for Elements integration
