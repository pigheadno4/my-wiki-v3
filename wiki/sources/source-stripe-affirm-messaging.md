---
title: "Stripe: Display Affirm Messaging (Legacy)"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-affirm-messaging-2025.md"
tags: [stripe, bnpl, affirm, messaging, legacy, payment-method-messaging]
---

## Summary

**Legacy** guide for the `affirmMessage` Element — no longer available in the latest Stripe.js. Stripe recommends the Payment Method Messaging Element instead. Includes the legacy API, minimum amount note, and CSS customization options.

## Key Details

> [!warning] **Deprecated** — `affirmMessage` Element is no longer available in the latest Stripe.js. Use the [Payment Method Messaging Element](https://docs.stripe.com/elements/payment-method-messaging.md) instead.

**Legacy API**: `elements.create('affirmMessage', { amount: 5000, currency: 'USD' })` → mount to DOM element. Minimum $50 USD/CAD — no render below threshold.

**Customization**: `logoColor`, `fontColor`, `fontSize`, `textAlign`.

**Recommended replacement**: Payment Method Messaging Element — covers all BNPL methods dynamically.

## Raw Sources

- [[stripe-affirm-messaging-2025]] — verbatim webpage content (94 lines); fixed `_Legacy_` → `*Legacy*`
