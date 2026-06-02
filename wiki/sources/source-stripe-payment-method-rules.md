---
title: "Stripe Docs — Payment method rules"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-payment-method-rules-2025.md"
tags: [stripe, payment-method-rules, dynamic-payment-methods, checkout, payment-element, klarna, bnpl]
---

## Summary

Guide for setting Dashboard-based rules to control when payment methods appear — no code required. Rules filter by order amount or buyer country/currency. Part of the dynamic payment methods customization suite.

## Key Facts

- **Rule types**: amount-based (hide/show if order above/below threshold) or location-based (country/currency)
- **Subscriptions caveat**: rules do NOT apply when creating subscriptions
- **Currency auto-conversion**: limits set in one currency are auto-converted at current exchange rate for other-currency transactions
- **A/B testing**: rules can serve as targeting criteria in A/B experiments
- **Setup**: Dashboard → Payment methods settings → PM overflow menu → Customize availability → Apply Overrides

## Testing Location-Based Rules

| Integration | How to test |
| --- | --- |
| Checkout | Pass `customer_email: 'test+location_FR@example.com'` (ISO country code suffix) when creating session |
| Payment Links | Pass `prefilled_email` or `locked_prefilled_email` URL parameter with location-formatted email |

## CDN Assets

- `raw/assets/stripe-pm-rules-klarna-present.png` — Klarna visible in checkout (73 KB)
- `raw/assets/stripe-pm-rules-klarna-hidden.png` — Klarna hidden in checkout (115 KB)

## Related Pages

- [[stripe-payment-method-rules]] — concept page
- [[stripe-dynamic-payment-methods]] — dynamic payment methods (prerequisite)
- [[stripe-ab-testing-payment-methods]] — A/B testing (compatible with PM rules)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-payment-method-rules-2025]] — verbatim webpage content (78 lines)
