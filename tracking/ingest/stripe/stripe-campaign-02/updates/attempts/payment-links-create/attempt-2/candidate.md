---
title: "Stripe Payment Links Overview"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payment-links/create"
raw_files:
  - "stripe-payment-links-create-2026-11-07.md"
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
- **Adaptive Pricing** — the create guide says it is always enabled for Payment Links, subject to the API-only automatic-surcharge private-preview incompatibility described below
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

The 2026-11-07 create guide adds [[raw/stripe-payment-links-create-2026-11-07|Checkout studio]] as a Dashboard hub for creating and managing Payment Links. This is a route described by the create guide; the studio page's detailed behavior was not captured for this source update.

For standard fixed products, the guide allows a Price ID in `line_items` or inline fixed `price_data`. For customer-chosen pricing, create a Price with `custom_unit_amount[enabled]=true`, then pass that Price ID as the sole line item with `quantity=1`. The older guide's inline `price_data` example with `unit_amount=1000` is a fixed-price example and should not be followed as the variable-price sequence. This example correction does not establish a new universal API restriction.

- **`stripe.paymentLinks.create({ line_items: [{ price, quantity }] })`**
- Up to **20 line items** for flat rate; for customer-defined prices, exactly **1 line item** with **quantity 1**
- Use `price_data` to create product + price inline
- Subscriptions: `subscription_data.trial_period_days` supported
- Customer-defined price: `custom_unit_amount: { enabled: true }` on Price object
- Override dynamic payment methods: `payment_method_types: ['card', 'klarna']`
- Async methods (bank debits, vouchers): 2–14 days to confirm; use webhooks for fulfillment
- **Adaptive Pricing** — both create captures describe it as always enabled for ordinary Payment Links and local-currency display in 150+ countries; this general wording does not establish compatibility with the separately documented automatic-surcharge private preview
- **Mobile**: Stripe iOS Dashboard app supports creating links (products/subscriptions only)
- **Customer-chosen-price Dashboard maximum wording**: the 2026-04-20 create capture says 10,000.00 SGD; the 2026-11-07 same-URL capture says 10,000.00 USD. Both direct readers to Stripe Support for an increase. Neither capture establishes the applicable maximum for a particular merchant or explains the currency difference.

> [!warning] Contradiction
> The create guide's broad “Adaptive Pricing is always enabled” wording does not cover every specialized Payment Link. The separately captured customize guide says API-only automatic surcharge in a US private preview requires a preview API version and a surcharge-provider app/onboarding; it supports one-off or customer-chosen pricing, excludes subscription links, limits applicable methods to cards and Apple Pay, and is incompatible with Adaptive Pricing. Do not infer a universal runtime outcome from the two dated statements.

## Related Pages

- [[stripe-payment-links]] — Stripe Payment Links concept page
- [[paypal-payment-links]] — PayPal's equivalent product
- [[stripe]] — Stripe company page
- [[raw/stripe-payment-links-customize-2026-11-07|2026-11-07 customize capture]] — dated automatic-surcharge preview exception to broad Adaptive Pricing wording

## Raw Sources

- [[raw/stripe-payment-links-create-2026-11-07|2026-11-07 create guide]] — Checkout studio route, variable Price ID with one item and quantity 1, dated USD maximum wording
- [[raw/stripe-payment-links-overview-2025|2026-04-20 capture]] — Payment Links features table, no-code capabilities, Invoicing vs Payment Links comparison
- [[raw/stripe-payment-links-create-2025|2026-04-20 capture]] — Create a payment link: 2 pricing models, API (line_items, price_data, subscription_data), custom_unit_amount, payment_method_types, Adaptive Pricing, mobile iOS app, async methods
- [[raw/stripe-payment-links-share-2025|2026-04-20 capture]] — Share a payment link: share channels, QR code (never expires), buy button embed, deactivate/reactivate (active: false); can't delete
- [[raw/stripe-payment-links-track-2025|2026-04-20 capture]] — Track a payment link: 5 UTM params (150 char max), client_reference_id (200 char max, no secrets), after_completion redirect, checkout.session.completed webhook
- [[raw/stripe-payment-links-buy-button-2025|2026-04-20 capture]] — Buy button: stripe-buy-button web component, 2 layouts, 3 attributes (client-reference-id/customer-email/customer-session-client-secret), CustomerSession (30min expiry, never cache), CSP requirements
- [[raw/stripe-payment-links-customize-2025|2026-04-20 capture]] — Customize checkout: payment limits (restrictions.completed_sessions.limit), custom deactivation message, address/phone/name/tax ID collection, Stripe Tax, ToS consent, custom fields (3 types), URL params, free trials without PM, adjustable quantities, custom domain
- [[raw/stripe-payment-links-shipping-2025|2026-04-20 capture]] — Shipping rates: shippingRates.create (fixed_amount + delivery_estimate), shipping_options on payment link; one-time prices only (not subscriptions)
- [[raw/stripe-payment-links-promotions-2025|2026-04-20 capture]] — Promotions, upsells, optional items: allow_promotion_codes, guest customer caveat, subscription upsells (Dashboard only), optional_items (up to 10), cross-sells (product-level, overridden by optional_items)
