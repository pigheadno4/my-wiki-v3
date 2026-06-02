---
title: "Stripe Payment Links Overview"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-payment-links-overview-2025.md"
  - "stripe-payment-links-create-2025.md"
  - "stripe-payment-links-share-2025.md"
  - "stripe-payment-links-track-2025.md"
  - "stripe-payment-links-buy-button-2025.md"
  - "stripe-payment-links-customize-2025.md"
  - "stripe-payment-links-shipping-2025.md"
  - "stripe-payment-links-promotions-2025.md"
tags: [stripe, payment-links, no-code, invoicing, adaptive-pricing, buy-button]
---

## Summary

Stripe Payment Links product overview — features, availability, no-code capabilities, and a detailed comparison against Stripe Invoicing.

## Key Takeaways

- **No code** — Stripe-hosted page; share link or embed buy button; no integration required
- **40+ payment methods** managed in Dashboard; dynamic presentment
- **Adaptive Pricing** — automatically displays local currency
- **Browser language** auto-detection (30+ languages)
- **Reusable** — share multiple times; optionally limit purchase count
- **Subscription support** — create subscription payment links (Smart Retries + reminders apply)

## Invoicing vs Payment Links

| | Payment Links | Invoicing |
| --- | --- | --- |
| Customer | Anyone with link | Specific customer |
| Partial payments | ✗ | ✓ |
| Edit quantities | ✓ | ✗ |
| Choose price | ✓ | ✗ |
| Upsells | ✓ | ✗ |
| Quote→Invoice | ✗ | ✓ |
| Smart Retries | Subscription links only | ✓ all |
| Reconciliation | URL parameters | Auto |

## API Creation Details

- **`stripe.paymentLinks.create({ line_items: [{ price, quantity }] })`**
- Up to **20 line items** for flat rate; **1 line item** for customer-defined prices
- Use `price_data` to create product + price inline
- Subscriptions: `subscription_data.trial_period_days` supported
- Customer-defined price: `custom_unit_amount: { enabled: true }` on Price object
- Override dynamic payment methods: `payment_method_types: ['card', 'klarna']`
- Async methods (bank debits, vouchers): 2–14 days to confirm; use webhooks for fulfillment
- **Adaptive Pricing always enabled** for Payment Links; 150+ countries; ML-based currency selection
- **Mobile**: Stripe iOS Dashboard app supports creating links (products/subscriptions only)
- **Customer-chooses max**: 10,000 SGD default; contact Stripe support to increase

## Related Pages

- [[stripe-payment-links]] — Stripe Payment Links concept page
- [[paypal-payment-links]] — PayPal's equivalent product
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-payment-links-overview-2025]] — Payment Links features table, no-code capabilities, Invoicing vs Payment Links comparison
- [[stripe-payment-links-create-2025]] — Create a payment link: 2 pricing models, API (line_items, price_data, subscription_data), custom_unit_amount, payment_method_types, Adaptive Pricing, mobile iOS app, async methods
- [[stripe-payment-links-share-2025]] — Share a payment link: share channels, QR code (never expires), buy button embed, deactivate/reactivate (active: false); can't delete
- [[stripe-payment-links-track-2025]] — Track a payment link: 5 UTM params (150 char max), client_reference_id (200 char max, no secrets), after_completion redirect, checkout.session.completed webhook
- [[stripe-payment-links-buy-button-2025]] — Buy button: stripe-buy-button web component, 2 layouts, 3 attributes (client-reference-id/customer-email/customer-session-client-secret), CustomerSession (30min expiry, never cache), CSP requirements
- [[stripe-payment-links-customize-2025]] — Customize checkout: payment limits (restrictions.completed_sessions.limit), custom deactivation message, address/phone/name/tax ID collection, Stripe Tax, ToS consent, custom fields (3 types), URL params, free trials without PM, adjustable quantities, custom domain
- [[stripe-payment-links-shipping-2025]] — Shipping rates: shippingRates.create (fixed_amount + delivery_estimate), shipping_options on payment link; one-time prices only (not subscriptions)
- [[stripe-payment-links-promotions-2025]] — Promotions, upsells, optional items: allow_promotion_codes, guest customer caveat, subscription upsells (Dashboard only), optional_items (up to 10), cross-sells (product-level, overridden by optional_items)
