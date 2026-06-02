---
title: "Stripe: Display Afterpay or Clearpay Messaging (Legacy)"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-afterpay-clearpay-messaging-2025.md"
tags: [stripe, bnpl, afterpay, clearpay, messaging, legacy, payment-method-messaging]
---

## Summary

**Legacy** guide for the `afterpayClearpayMessage` Element — no longer available in the latest Stripe.js. Use Payment Method Messaging Element instead. Includes API, locale/currency support, ineligibility handling, and CSS customization.

## Key Details

> [!warning] **Deprecated** — `afterpayClearpayMessage` Element is no longer in latest Stripe.js. Use [Payment Method Messaging Element](https://docs.stripe.com/elements/payment-method-messaging.md) instead.

**Localization**: Clearpay branding automatically shown for UK locale (`en-GB`). Supported locales: `en-US`, `en-CA`, `en-AU`, `en-NZ`, `en-GB`. Currencies: USD, CAD, AUD, NZD, GBP.

**Ineligibility**: `isEligible`/`isCartEligible` options to show ineligible messaging. Automatically shows price-range ineligibility when amount exceeds limits (`showLowerLimit`/`showUpperLimit` to customize).

**Customization**: `logoType` (badge/lockup) + `badgeTheme`/`lockupTheme`. CSS for `font-family`, `font-size`, `color`, logo `width`/`height`.

## Raw Sources

- [[stripe-afterpay-clearpay-messaging-2025]] — verbatim webpage content (135 lines); fixed `_Legacy_` → `*Legacy*`
