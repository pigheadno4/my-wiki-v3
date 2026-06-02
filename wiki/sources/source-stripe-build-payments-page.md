---
title: "Stripe: Build a Payments Page"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-build-payments-page-2025.md"
tags: [stripe, checkout, checkout-sessions, payment-element, checkout-elements, adaptive-pricing]
---

## Summary

Overview of Stripe's two Checkout UI options built on the Checkout Sessions API: Checkout Page (recommended, low complexity, full feature set) vs Checkout Elements (highest complexity, full CSS control, no order summary).

## Key Takeaways

- **Both UIs use the Checkout Sessions API** — same underlying API, different front-end experience
- **Checkout Page** (recommended): Billing, Tax, Adaptive Pricing, Stripe Managed Payments, Link, Dynamic payment methods, Surcharging, Split-tender; full order summary; hosted or embedded; low complexity; 15 brand settings; no ongoing maintenance
- **Checkout Elements**: Adaptive Pricing, Link, Dynamic payment methods only; no order summary; embedded only; highest complexity; full CSS via Appearance API; requires ongoing maintenance
- **100+ local payment methods** supported

## Checkout Page vs Elements

| | PAGE (Recommended) | ELEMENTS |
| --- | --- | --- |
| Hosting | Hosted or Embedded | Embedded only |
| Complexity | Low | Highest |
| Customization | 15 brand settings | Full CSS (Appearance API) |
| Order summary | Full (subtotals, tax, shipping, cross-sells, upsells, trials, discounts) | None |
| Ongoing maintenance | No | Yes |
| Extra features | Billing, Tax, Surcharging, Split-tender, Stripe Managed Payments | — |

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page
- [[stripe-payment-links]] — no-code peer product
- [[source-stripe-checkout-sessions]] — Checkout Sessions API deep dive
- [[source-stripe-accept-a-payment]] — full integration guide

## Raw Sources

- [[stripe-build-payments-page-2025]] — Checkout Page vs Elements comparison: feature matrix, hosting modes, maintenance tradeoffs, customization options, 3 PNG illustrations
