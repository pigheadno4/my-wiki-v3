---
title: "Stripe: Build an integration with a checkout form"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-form-integration-2025.md"
tags: [stripe, checkout, checkout-form, payment-element, appearance-api, adaptive-pricing, localization]
---

## Summary

Overview of Stripe's checkout form integration — a fully custom, single-iframe checkout UI that gives developers full control over look and feel while supporting 100+ payment methods, express wallets, and Stripe's product suite.

## Key Takeaways

- **Single iframe** — full end-to-end checkout in one embedded component
- **100+ payment methods** + one-click express checkout wallets (Apple Pay, Google Pay, etc.)
- **Built-in returning customer UI** — saved payment methods + saved address book out of the box
- **Adaptive UI** — adjusts dynamically to device type (web and mobile)
- **Full CSS customization** via the Stripe Appearance API
- **Stripe product integrations**: Adaptive Pricing, Stripe Tax, Billing
- **Localization**: content translation + localized payment methods + local currency display
- **2 layouts**: single-page and multi-step (compact)

## What You Can Collect

- Payment details (100+ methods)
- One-click express checkout wallets
- Billing address
- Shipping address + options + prices
- Tax details
- Currency choice
- Custom details via custom text fields

## Layouts

| Layout | New customer UI | Returning customer UI |
| --- | --- | --- |
| Single-page | Full form on one page | Prefilled saved payment + address |
| Multi-step (compact) | Step-by-step flow | Prefilled saved payment + address |

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page (this is the Checkout Elements / custom path)
- [[source-stripe-checkout-sessions]] — Checkout Sessions API
- [[source-stripe-build-payments-page]] — Checkout Page vs Elements comparison

## Raw Sources

- [[stripe-checkout-form-integration-2025]] — Checkout form overview: 8 collectable fields, 7 features (single iframe, returning UI, Appearance API, Adaptive Pricing, Tax, Billing, localization), 2 layouts with MP4 demos
