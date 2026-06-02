---
title: "Stripe: Accept an Afterpay or Clearpay Payment"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-afterpay-clearpay-accept-payment-2025.md"
tags: [stripe, bnpl, afterpay, clearpay, buy-now-pay-later, checkout, payment-intents, elements]
---

## Summary

Integration guide for Afterpay/Clearpay payments across three paths: Checkout (hosted/embedded), Checkout Sessions API (Elements), and PaymentIntents API (Elements + manual). Mirrors Affirm integration structure but with Afterpay-specific differences.

## Key Details

**API enum**: `afterpay_clearpay`

**Three integration paths**: Checkout, Checkout Sessions API (Elements), PaymentIntents API.

**Checkout Session constraints**: payment mode only; domestic currency; one-time line items only. Shipping address via `payment_intent_data[shipping]` improves loan acceptance.

**3-hour expiry**: PaymentIntents in `requires_action` auto-expire after **3 hours** (not 12 hours like Affirm).

**Billing details required** for manual PaymentIntent path — `payment_method_data.billing_details` is required; shipping is optional but recommended for better authentication rates.

**Manual capture test mode**: uncaptured PaymentIntents auto-expire 10 minutes after authorization.

**Always offer fallback payment methods** — Afterpay has higher decline rates than cards.

## Raw Sources

- [[stripe-afterpay-clearpay-accept-payment-2025]] — verbatim webpage content (2871 lines); fixed 20+ `_italic_` → `*italic*` across 7 term types
