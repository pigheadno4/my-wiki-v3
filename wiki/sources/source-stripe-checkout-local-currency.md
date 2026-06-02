---
title: "Let Customers Pay in Their Local Currency"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-checkout-local-currency-2025.md"
tags: [stripe, checkout-sessions, currency, adaptive-pricing, fx-quotes, manual-currency-prices, localization]
---

## Summary

Navigation/hub page for Stripe's three approaches to multi-currency pricing. All three use Elements + Checkout Sessions API.

## The Three Approaches

| Approach | Description | Status in wiki |
| --- | --- | --- |
| **Adaptive Pricing** | Auto-converts to customer's local currency; 0% merchant / 2–4% customer fee; 150+ countries | ✓ Documented — [[stripe-adaptive-pricing]] |
| **FX Quotes API** | Determine which currencies to localize; control fee pass-through; establish exchange rates | ✓ Documented — [[stripe-fx-quotes-api]] |
| **Manual currency prices** | Statically set prices per currency; same price regardless of FX changes | ✓ Documented — [[source-stripe-manual-currency-prices]] |

## FX Quotes API

Now documented — see [[stripe-fx-quotes-api]]. It allows merchants to:

- Determine which currencies to display
- Choose whether to pass FX fees to customers
- Establish fixed exchange rates

## Manual Currency Prices

Now documented — see [[source-stripe-manual-currency-prices]]. A static alternative to Adaptive Pricing: merchants set prices per currency explicitly. No dynamic conversion.

## Related Pages

- [[stripe-adaptive-pricing]] — Adaptive Pricing concept page
- [[source-stripe-adaptive-pricing]] — Adaptive Pricing source
- [[stripe-currency-selector-element]] — UI component for currency selection

## Raw Sources

- [[stripe-checkout-local-currency-2025]] — verbatim hub page (12 lines)
