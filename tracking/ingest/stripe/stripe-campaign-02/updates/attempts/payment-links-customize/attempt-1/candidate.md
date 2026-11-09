---
title: "Stripe Payment Links Overview"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payment-links/customize"
raw_files:
  - "stripe-payment-links-customize-2026-11-07.md"
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

Stripe Payment Links overview and historical eight-page bundle, now supplemented by the 2026-11-07 customization capture. This candidate incorporates only the assigned customize raw pair; the other Payment Links raw identities and claims remain historical context for coordinator consolidation. The new capture documents a pay-what-you-want URL parameter, Managed Payments navigation, and a private-preview automatic surcharge path.

## Key Takeaways

- **No code** — Stripe-hosted page; share link or embed buy button; no integration required
- **40+ payment methods** managed in Dashboard; dynamic presentment
- **Adaptive Pricing** — generally displays local currency; the 2026-11-07 automatic surcharge private preview is explicitly incompatible with it
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
- **Adaptive Pricing**: the separately captured create guide broadly says always enabled for Payment Links and describes 150+ countries and ML-based currency selection. The 2026-11-07 customize capture explicitly excludes compatibility with its API-only automatic surcharge private preview.

> [!warning] Contradiction
> The general Payment Links create wording says Adaptive Pricing is always enabled, while the customize guide says automatic surcharge is incompatible with Adaptive Pricing. Preserve that preview-specific exception; neither statement establishes a universal runtime resolution for every account or link.
- **Mobile**: Stripe iOS Dashboard app supports creating links (products/subscriptions only)
- **Customer-chooses max**: 10,000 SGD default; contact Stripe support to increase

## Customize checkout (2026-11-07 capture)

A payment-link use limit counts **completed Checkout Sessions**: the link is considered paid when a Session completes, with the API description tying `restrictions[completed_sessions][limit]` to `checkout.session.completed`. The link deactivates after the configured count; merely creating or opening it is not a consumed use. The deactivation message can be customized through the Dashboard or `inactive_message`.

Checkout customization also includes billing and shipping address collection, phone and business/individual name collection, tax ID collection, Stripe Tax, terms-of-service consent, custom fields, branding, custom domains, adjustable quantities, and free trials. Dashboard address collection makes selected address fields required; API billing-address collection can be `required` or `auto`. Shipping collection needs `allowed_countries`. Name fields can be optional. Custom field types remain text (255 characters), numbers (255 digits), and dropdown; dropdown choices are limited to 10 for Dashboard-created links and 200 after API creation. The free-trial-without-payment-method path is for subscription-product links and needs trial-end handling; it does not apply to one-time links. The new capture adds Checkout studio as another branding route.

**URL parameters:** `prefilled_email` is editable; `locked_prefilled_email` is uneditable and takes precedence when both email parameters are supplied; `prefilled_promo_code` needs promotions enabled; `locale` chooses a supported language. The new `prefilled_amount` sets an **editable initial amount only on pay-what-you-want links**, with no effect on fixed-price links. It must be a positive integer in the custom price's default currency smallest unit and meet that price's configured minimum and maximum. Invalid values fall back to the link's stored preset amount or the default empty state. It restricts multi-currency behavior: Checkout cannot automatically use the customer's local currency for that amount, and creating the link with a non-default `currency` parameter raises an error. This URL-parameter section is grounded in this customize capture only; the separate URL-parameter source unit remains independently owned.

**Tax product boundary:** Stripe Tax can calculate/collect tax after setup. The new Managed Payments paragraph links a separate digital-products merchant-of-record route, with Stripe handling tax registration/filing/remittance plus fraud, disputes and support in that product. It is not ordinary Stripe Tax, and this section does not independently establish a merchant's Managed Payments eligibility. See [[source-stripe-managed-payments-payment-links]] for the distinct source route.

**Automatic surcharge, private preview:** The new guide describes a third-party-provider calculation based on card details. Access is by private preview; a surcharge provider Stripe App must be installed and onboarded, and a preview `Stripe-Version` header is required for API creation (the example uses `2026-10-28.preview`). The API uses `automatic_surcharge[enabled]=true` with `automatic_surcharge[calculation_basis]` set to `total_before_tax` or `total_after_tax`; it also describes Stripe Tax compatibility through `automatic_surcharge[tax_behavior]`. The path is **API-only**, supports one-off and customer-chooses-what-to-pay links, excludes subscription links and Adaptive Pricing, and during this preview is limited to the United States, cards and Apple Pay. Unsupported methods receive no applicable surcharge. The merchant remains responsible for verifying provider calculations against law and network rules; the guide is not proof of compliance, preview access or live payment outcome.

### Customize detail locators

- [[raw/stripe-payment-links-customize-2026-11-07|2026-11-07 customize guide]], completed-session limits and deactivation 13–62; address and phone 64–112; names/tax IDs/Stripe Tax 114–174; Managed Payments 176–180; ToS/custom fields 182–248.
- Same raw, Adaptive Pricing 250–254; Checkout studio/domain/policies 264–283; URL parameters and `prefilled_amount` 285–315; subscription trials and quantity 317–362; private-preview surcharge conditions 364–423.
- [[raw/stripe-payment-links-customize-2025|2026-04-20 customize guide]], prior completed-session limit 12–30; addresses/names/tax/ToS/custom fields 83–295; Adaptive Pricing and old URL parameters 297–357; trials/quantities 363–412.

## Related Pages

- [[stripe-payment-links]] — Stripe Payment Links concept page
- [[paypal-payment-links]] — PayPal's equivalent product
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payment-links-customize-2026-11-07|Customize checkout, captured 2026-11-07]] — pay-what-you-want amount preset, Managed Payments link, private-preview automatic surcharge and retained customization fields
- [[raw/stripe-payment-links-overview-2025|Payment Links overview, captured 2026-04-20]] — Payment Links features table, no-code capabilities, Invoicing vs Payment Links comparison
- [[raw/stripe-payment-links-create-2025|create guide, captured 2026-04-20]] — Create a payment link: 2 pricing models, API (line_items, price_data, subscription_data), custom_unit_amount, payment_method_types, Adaptive Pricing, mobile iOS app, async methods
- [[raw/stripe-payment-links-share-2025|share guide, captured 2026-04-20]] — Share a payment link: share channels, QR code (never expires), buy button embed, deactivate/reactivate (active: false); can't delete
- [[raw/stripe-payment-links-track-2025|track guide, captured 2026-04-20]] — Track a payment link: 5 UTM params (150 char max), client_reference_id (200 char max, no secrets), after_completion redirect, checkout.session.completed webhook
- [[raw/stripe-payment-links-buy-button-2025|buy-button guide, captured 2026-04-20]] — Buy button: stripe-buy-button web component, 2 layouts, 3 attributes (client-reference-id/customer-email/customer-session-client-secret), CustomerSession (30min expiry, never cache), CSP requirements
- [[raw/stripe-payment-links-customize-2025|Customize checkout, captured 2026-04-20]] — payment limits, deactivation message, collection fields, Stripe Tax, ToS, URL parameters, subscription trials, quantities, domain
- [[raw/stripe-payment-links-shipping-2025|shipping guide, captured 2026-04-20]] — Shipping rates: shippingRates.create (fixed_amount + delivery_estimate), shipping_options on payment link; one-time prices only (not subscriptions)
- [[raw/stripe-payment-links-promotions-2025|promotions guide, captured 2026-04-20]] — Promotions, upsells, optional items: allow_promotion_codes, guest customer caveat, subscription upsells (Dashboard only), optional_items (up to 10), cross-sells (product-level, overridden by optional_items)
