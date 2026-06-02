---
title: "Stripe: Build an Advanced Payments Integration (Elements)"
type: source
date_ingested: 2026-04-21
original_format: notes
raw_files:
  - "stripe-elements-advanced-payments-2025.md"
tags: [stripe, elements, checkout-sessions, payment-intents, advanced-payments, appearance-api, ic-plus]
---

## Summary

Overview and feature comparison of Stripe's two integration paths for custom payment UIs using Elements: Checkout Sessions API (recommended) vs Payment Intents API (maximum control). Both use the same Elements UI and Appearance API.

## Key Takeaways

- **Checkout Sessions API + Elements** = recommended for most integrations; low coding; Stripe handles checkout features
- **Payment Intents API + Elements** = maximum control; most coding — you build all checkout features yourself
- Both paths use the same Elements UI and Appearance API (same visual customization capability)
- **Functional parity**: both support 40+ payment methods, Dashboard PM management, Link, same payment scenarios
- **IC+ only** (both APIs): Multicapture, Overcapture, Extended authorization, Incremental authorization

## Feature Comparison

| Feature | Checkout Sessions API | Payment Intents API |
| --- | --- | --- |
| UI | Elements | Elements |
| Integration effort | Low coding | Most coding (build checkout yourself) |
| Hosting | Embed on site | Embed on site |
| UI customization | Appearance API | Appearance API |
| 40+ payment methods | ✓ | ✓ |
| Dashboard PM management | ✓ | ✓ |
| Link | ✓ | ✓ |
| Custom payment methods | ✓ | ✓ |

## Payment Scenario Support (both APIs)

- Set up future payments
- Save payment details during payment
- Place a hold on a payment method (auth + capture)
- Finalize payments on server
- Multi-step payment flow

**IC+ only**: Multicapture, Overcapture, Extended authorization, Incremental authorization

## Checkout Customization (both APIs)

- Appearance API for look + feel
- Dashboard-managed payment methods
- One-click checkout options (express checkout buttons)
- Email receipts
- Collect additional info (shipping, taxes)
- Subscriptions, save future payments, save during payment

## When to Choose Each

| | Checkout Sessions API | Payment Intents API |
| --- | --- | --- |
| Best for | Most integrations | Highly custom flows |
| Effort | Low | High |
| Built-in features | Stripe handles many checkout concerns | You build everything |
| Equivalent to | Checkout Elements (embedded form) | Full DIY |

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page (Checkout Elements = Checkout Sessions + Elements UI)
- [[source-stripe-checkout-sessions]] — Checkout Sessions API deep dive

## Raw Sources

- [[stripe-elements-advanced-payments-2025]] — Feature matrix: Checkout Sessions vs Payment Intents for Elements integrations, payment scenario support, IC+ features
