---
title: "Stripe Web Elements Overview"
type: source
date_ingested: 2026-04-21
original_format: notes
raw_files:
  - "stripe-web-elements-overview-2025.md"
tags: [stripe, elements, payment-element, express-checkout, link, address-element, adaptive-pricing, checkout-sessions, payment-intents]
---

## Summary

Overview of Stripe Elements — the prebuilt UI component library built on Stripe.js. Documents all 7 elements, their compatible APIs, and the key architectural difference between Checkout Sessions API (manages customer/shipping/tax/discounts/payment) and Payment Intents API (payment step only).

## Key Takeaways

- **Stripe Elements** = prebuilt UI components in Stripe.js; tokenizes payment details client-side, never touches your server
- **7 Elements** — see table below
- **Two compatible APIs**: Checkout Sessions (recommended) vs Payment Intents (lower-level)
- **Checkout Sessions API manages 5 concerns**: Customer, Shipping, Taxes, Discounts/coupons, Payment
- **Payment Intents API manages 1 concern**: Payment only — you build everything else
- **Adaptive Pricing**: only available with Checkout Sessions API
- **Currency Selector Element**: only compatible with Checkout Sessions API

## 7 Elements

| Element | Purpose | API compatibility |
| --- | --- | --- |
| Payment Element | Accept 100+ payment methods including cards | Both |
| Express Checkout Element | Apple Pay, Google Pay, PayPal one-click buttons | Both |
| Link Authentication Element | Auto-fill saved payment/shipping via Link | Both |
| Address Element | Collect billing/shipping + display Link saved addresses | Both |
| Payment Method Messaging Element | Show Buy now, Pay later plans | Both |
| Currency Selector Element | Local currency choice with Adaptive Pricing | Checkout Sessions only |
| Tax ID Element | Collect business tax IDs for invoices/VAT | Both |

## API Comparison (from diagram)

| Checkout concern | Checkout Sessions API | Payment Intents API |
| --- | --- | --- |
| Customer management | ✓ Built-in | Build yourself |
| Shipping | ✓ Built-in | Build yourself |
| Taxes | ✓ Built-in | Build yourself |
| Discounts and coupons | ✓ Built-in | Build yourself |
| Payment | ✓ Built-in | ✓ Core feature |
| Adaptive Pricing | ✓ Only here | ✗ Not available |

## Features of Elements

- 100+ global payment methods including Apple Pay
- Link: auto-fill saved payment/shipping for returning customers
- Saved payment methods: built-in save/reuse/manage
- Compliance: globally compliant; mandates and consent notices handled automatically
- Up-to-date forms: localized, built-in error handling, provider requirements maintained by Stripe
- Appearance API: full CSS-level customization to match your site
- Address collection: full or partial billing addresses
- Other: CVC recollection, card brand control

## Related Pages

- [[stripe-elements]] — Stripe Elements concept page
- [[stripe-checkout]] — Checkout Sessions + Elements integration
- [[stripe-payment-intents]] — Payment Intents + Elements integration

## Raw Sources

- [[stripe-web-elements-overview-2025]] — Elements overview: 7 elements, 2 compatible APIs, API comparison diagram (Checkout Sessions vs Payment Intents), features list
