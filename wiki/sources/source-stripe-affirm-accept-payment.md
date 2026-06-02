---
title: "Stripe: Accept an Affirm Payment"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-affirm-accept-payment-2025.md"
tags: [stripe, bnpl, affirm, buy-now-pay-later, checkout, payment-intents, elements]
---

## Summary

Integration guide for accepting Affirm payments across three paths: Checkout (hosted/embedded), Checkout Sessions API (Elements), and PaymentIntents API (Elements + manual redirect). Covers compatibility constraints, error codes, expiry behavior, and manual capture notes.

## Key Details

**Three integration paths**: Checkout (hosted/embedded page), Checkout Sessions API (Elements), PaymentIntents API (Elements or manual `confirmAffirmPayment`).

**Checkout Session constraints**: payment mode only; domestic currency; one-time line items only.

**Shipping address**: passing via `payment_intent_data[shipping]` helps loan acceptance rates even if not collecting via Checkout.

**12-hour expiry**: PaymentIntents in `requires_action` auto-expire 12 hours after creation if customer takes no action → transitions to `requires_payment_method`.

**Manual capture test mode**: uncaptured PaymentIntents auto-expire 10 minutes after authorization in test mode.

**Key error codes**:

| Code | Meaning |
| --- | --- |
| `payment_method_provider_decline` | Affirm declined — customer should contact Affirm |
| `payment_intent_payment_attempt_expired` | 12-hour session expired |
| `affirm_checkout_canceled` | User canceled OR Affirm rejected loan — indistinguishable |
| `amount_too_small` / `amount_too_large` | Outside Affirm transaction limits |
| `payment_method_not_available` | Affirm service error — retry later |

**Always offer fallback payment methods** (e.g., card) — Affirm has higher decline rates than cards.

## Raw Sources

- [[stripe-affirm-accept-payment-2025]] — verbatim webpage content (1723 lines); fixed 13× `_italic_` → `*italic*` across 8 term types
