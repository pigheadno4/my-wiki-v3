---
title: "Stripe Docs — Dynamic payment methods"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-dynamic-payment-methods-2025.md"
tags: [stripe, dynamic-payment-methods, payment-element, checkout, ai-models, optimized-checkout, automatic-payment-methods]
---

## Summary

Covers the dynamic payment methods system: Dashboard-driven PM management, migration from manual `payment_method_types`, per-transaction exclusion, 6 eligibility criteria, AI ordering models, and Dashboard customization features.

## Key Facts

- **Migration**: remove `payment_method_types`; API < 2023-08-16 needs `automatic_payment_methods[enabled]=true`
- **Exclusion**: `excluded_payment_method_types` on PaymentIntent/SetupIntent/Checkout/Payment Element — but Apple Pay, Google Pay, Link use `wallets` hash instead (error if using `excluded_payment_method_types` for these)
- **6 eligibility criteria**: Dashboard settings, product support, presentment currency, charge amount (final incl. tax), API support (`setup_future_usage`/`capture_method`), customer country
- **AI models**: 100+ signals, exploration-exploitation framework (Optimized Checkout Suite)
- **Customization**: payment method rules, A/B testing, PM configurations, embed PM settings (Connect)
- **Connect**: direct charges or `on_behalf_of` → connected account's settings determine available PMs

## Related Pages

- [[stripe-dynamic-payment-methods]] — concept page
- [[stripe-payment-methods]] — payment methods overview
- [[source-stripe-automatic-payment-methods]] — Aug 2023 API change context
- [[source-stripe-payment-method-support]] — product + API support matrices
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-dynamic-payment-methods-2025]] — verbatim webpage content (156 lines)
