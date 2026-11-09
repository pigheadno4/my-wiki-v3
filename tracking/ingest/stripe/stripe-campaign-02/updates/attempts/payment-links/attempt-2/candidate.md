---
title: "Stripe Payment Links Overview"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: https://docs.stripe.com/payment-links
raw_files:
  - "stripe-payment-links-2026-11-07.md"
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

Stripe Payment Links are shareable URLs for a Stripe-hosted payment page. The 2026-11-07 overview retains the no-code positioning, local-language and Adaptive Pricing descriptions, buy-button route, reuse with an optional purchase limit, and comparison with Invoicing from the 2026-04-20 overview. This update concerns the overview URL only. The seven other historical Payment Links raw captures below support their own API, customization, sharing, tracking, shipping, and promotion details and were not revalidated by this overview comparison.

## Key Takeaways

- **No-code hosted page** — share a link or embed a buy button; the overview rates integration effort complexity 1/5.
- **Payment-method catalog and dynamic display** — the overview describes 40+ methods managed in Dashboard. Its November footnote says dynamic display filters for eligibility and availability varies by product. The 40+ figure is a catalog description, not a promise that 40 or more methods appear for every buyer, link, currency, or account.
- **Adaptive Pricing** — the overview describes local-currency presentation; eligibility and runtime display still depend on the relevant path.
- **Language** — the comparison describes 30+ languages and browser-language matching for Payment Links.
- **Reusable** — links can be used multiple times with multiple customers, or their purchase count can be limited; neither overview promises an unlimited volume.
- **Subscription support** — links can sell subscriptions, and the comparison limits Smart Retries and reminder-email recovery to subscription Payment Links.
- **Checkout Studio** — the November overview adds a route explicitly labeled **Private preview** for configuring, monitoring, and experimenting across Payment Links and other Checkout integrations. The overview link does not establish access, account eligibility, or a demonstrated experiment result.

## Invoicing vs Payment Links

| | Payment Links | Invoicing |
| --- | --- | --- |
| Customer | Anyone with the link | Specific customer |
| Partial payments or plans | No | Yes |
| Edit quantities | Yes | No |
| Choose price | Yes | No |
| Upsells or optional items | Yes | No |
| Quote to invoice | No | Yes |
| Smart Retries and reminders | Subscription links only | Available for automatic collection |
| Reconciliation | URL parameters | Automatic bank-payment reconciliation |

The November comparison also retains Stripe Tax support, receipt/refund support, and a Stripe-hosted page, while expanding explanatory links and footnotes. Product-specific availability and eligibility still govern which methods a customer sees.

## API Creation Details — separate historical create capture

The following details come from the separate 2026-04-20 create guide in this source's historical bundle, not from this overview pair:

- **`stripe.paymentLinks.create({ line_items: [{ price, quantity }] })`**
- Up to **20 line items** for flat rate; **1 line item** for customer-defined prices
- Use `price_data` to create product and price inline
- Subscriptions: `subscription_data.trial_period_days` supported
- Customer-defined price: `custom_unit_amount: { enabled: true }` on Price object
- Override dynamic payment methods: `payment_method_types: ['card', 'klarna']`
- Async methods (bank debits, vouchers): 2–14 days to confirm; use webhooks for fulfillment
- The older create guide broadly describes Adaptive Pricing as enabled for Payment Links, 150+ countries, and ML-based currency selection. This assigned overview pair does not independently test that broad claim or its compatibility with other features.
- **Mobile**: Stripe iOS Dashboard app supports creating links for products/subscriptions in the older create guide
- **Customer-chooses max**: 10,000 SGD default in the older create guide; contact Stripe support to increase

## Related Pages

- [[stripe-payment-links]] — Stripe Payment Links concept page
- [[paypal-payment-links]] — PayPal's equivalent product
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payment-links-2026-11-07|Payment Links overview, captured 2026-11-07]] — hosted page, expanded Invoicing comparison, eligibility footnote, and Checkout Studio private-preview navigation
- [[raw/stripe-payment-links-overview-2025|Payment Links overview, captured 2026-04-20]] — earlier hosted-page features and Invoicing comparison
- [[raw/stripe-payment-links-create-2025|Create guide, captured 2026-04-20]] — pricing models, API parameters, Adaptive Pricing, mobile iOS app, and async methods
- [[raw/stripe-payment-links-share-2025|Share guide, captured 2026-04-20]] — share channels, QR code, buy button, and deactivation
- [[raw/stripe-payment-links-track-2025|Track guide, captured 2026-04-20]] — UTM and client reference parameters, redirect, and webhook tracking
- [[raw/stripe-payment-links-buy-button-2025|Buy-button guide, captured 2026-04-20]] — web component, layouts, CustomerSession, and CSP
- [[raw/stripe-payment-links-customize-2025|Customize guide, captured 2026-04-20]] — limits, collection fields, tax, consent, custom fields, URL parameters, trials, quantities, and domain
- [[raw/stripe-payment-links-shipping-2025|Shipping guide, captured 2026-04-20]] — rates and one-time-price scope
- [[raw/stripe-payment-links-promotions-2025|Promotions guide, captured 2026-04-20]] — promotion codes, upsells, optional items, and cross-sells
