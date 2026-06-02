---
title: "Stripe: Manage Default Payment Methods in the Dashboard"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-automatic-payment-methods-2025.md"
tags: [stripe, payment-methods, dynamic-payment-methods, payment-intents, automatic-payment-methods]
---

## Summary

As of August 16, 2023, omitting `payment_method_types` on a PaymentIntent/SetupIntent defaults to Dashboard-managed payment methods (not just `card`). `automatic_payment_methods.enabled` defaults to `true`.

## Key Details

**Prior behavior**: omitting `payment_method_types` → only `card`.

**New behavior**: Stripe applies all eligible Dashboard-managed payment methods automatically.

**Apple Pay**: enabled by default. **Google Pay**: disabled by default; also filtered if automatic tax enabled without shipping address.

**Server-side/API confirmation options**:
1. Provide `return_url` (required for redirect-based methods)
2. Set `automatic_payment_methods: { allow_redirects: 'never' }` — no redirect methods, no `return_url` required
3. Specify explicit `payment_method_types` — no Dashboard management, no `return_url` required

**Elements**: migrate Card Element/individual payment method Elements to the Payment Element (25+ payment methods in one integration).

**Checkout/Payment Links**: upgrade API version without code changes.

**`off_session: true`**: no changes needed.

## Raw Sources

- [[stripe-automatic-payment-methods-2025]] — verbatim webpage content (upgrade paths with Node.js/JS/React code examples)
