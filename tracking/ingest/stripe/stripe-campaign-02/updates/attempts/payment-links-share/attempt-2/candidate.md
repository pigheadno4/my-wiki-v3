---
title: "Stripe Payment Links Overview"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: https://docs.stripe.com/payment-links/share
raw_files:
  - "stripe-payment-links-share-2026-11-07.md"
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

## Sharing and Link State (November 7 Share Capture)

A Payment Link URL can be copied from the Dashboard or read from the API's `url` field and shared by email, text, social media, website, or app. The Dashboard can create a QR code for an existing or new link and offer a PNG download; it can also produce buy-button embed code. The QR code itself has no intrinsic expiration, but a scan redirects to an expiration page after its underlying link is deactivated, and customers cannot make new purchases through that link. A created Payment Link cannot be deleted; `active: false` deactivates it, and `active: true` reactivates it. These operations change link availability for future purchases, not the state of a completed payment. The November diff changes API documentation URL paths without establishing a runtime API change.

## Raw Sources

- [[raw/stripe-payment-links-share-2026-11-07|November 7 share capture]] — sharing channels, QR and buy-button routes, and link-state behavior

- [[raw/stripe-payment-links-overview-2025|stripe-payment-links-overview-2025]] — Payment Links features table, no-code capabilities, Invoicing vs Payment Links comparison
- [[raw/stripe-payment-links-create-2025|stripe-payment-links-create-2025]] — Create a payment link: 2 pricing models, API (line_items, price_data, subscription_data), custom_unit_amount, payment_method_types, Adaptive Pricing, mobile iOS app, async methods
- [[raw/stripe-payment-links-share-2025|April 20 share capture]] — share channels, persistent QR image (deactivated underlying link redirects scans to an expiration page and blocks new purchases), buy button embed, deactivate/reactivate (`active: false`/`true`); created links cannot be deleted
- [[raw/stripe-payment-links-track-2025|stripe-payment-links-track-2025]] — Track a payment link: 5 UTM params (150 char max), client_reference_id (200 char max, no secrets), after_completion redirect, checkout.session.completed webhook
- [[raw/stripe-payment-links-buy-button-2025|stripe-payment-links-buy-button-2025]] — Buy button: stripe-buy-button web component, 2 layouts, 3 attributes (client-reference-id/customer-email/customer-session-client-secret), CustomerSession (30min expiry, never cache), CSP requirements
- [[raw/stripe-payment-links-customize-2025|stripe-payment-links-customize-2025]] — Customize checkout: payment limits (restrictions.completed_sessions.limit), custom deactivation message, address/phone/name/tax ID collection, Stripe Tax, ToS consent, custom fields (3 types), URL params, free trials without PM, adjustable quantities, custom domain
- [[raw/stripe-payment-links-shipping-2025|stripe-payment-links-shipping-2025]] — Shipping rates: shippingRates.create (fixed_amount + delivery_estimate), shipping_options on payment link; one-time prices only (not subscriptions)
- [[raw/stripe-payment-links-promotions-2025|stripe-payment-links-promotions-2025]] — Promotions, upsells, optional items: allow_promotion_codes, guest customer caveat, subscription upsells (Dashboard only), optional_items (up to 10), cross-sells (product-level, overridden by optional_items)
