---
title: "Stripe Docs — Payment method configurations"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-payment-method-configurations-2025.md"
tags: [stripe, payment-method-configurations, dynamic-payment-methods, payment-element, checkout, connect, pmc]
---

## Summary

Guide for creating and using named payment method configurations (PMCs) to display different PM sets for different checkout scenarios. Covers Dashboard + API creation, integration across platforms, and the decision rule between configs and per-transaction exclusion.

## Key Facts

- **Default**: one "Default Config" per account; additional configs created via Dashboard or API
- **Config ID**: `pmc_...`; IDs for the config passed at PaymentIntent/Checkout/Payment Element creation
- **Apple Pay**: enabled by default; Google Pay: disabled by default; Google Pay also filtered with automatic tax + no shipping address
- **API**: `stripe.paymentMethodConfigurations.create({ name, pm: { display_preference: { preference: 'on' } } })`
- **Integration**: `payment_method_configuration: 'pmc_234'` on PaymentIntent or Checkout; `paymentMethodConfiguration: 'pmc_234'` on Payment Element (Web); `paymentMethodConfigurationId` on iOS/Android

## Config vs `excluded_payment_method_types` Decision Rule

- **Use configs** for broad category differences (one-time vs subscriptions, consistent offerings)
- **Use `excluded_payment_method_types`** for per-transaction fine-grained control
- Both can be combined; Apple Pay / Google Pay / Link must use `wallets` hash instead of exclusion

## CDN Assets

- `raw/assets/stripe-payment-method-configurations.png` — configurations Dashboard UI (168 KB)

## Related Pages

- [[stripe-payment-method-configurations]] — concept page
- [[stripe-dynamic-payment-methods]] — dynamic payment methods (prerequisite)
- [[stripe-payment-method-rules]] — PM rules (complementary customization feature)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-payment-method-configurations-2025]] — verbatim webpage content (194 lines)
