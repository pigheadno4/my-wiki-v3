---
title: "Stripe Payment Links"
type: concept
category: technology
tags: [stripe, payment-links, no-code, buy-button, adaptive-pricing, invoicing]
---

## Stripe Payment Links

Stripe's no-code shareable payment URL product. Customers pay on a Stripe-hosted page without coding required. The 2026-11-07 [[source-stripe-payment-links]] overview describes a 40+ payment-method catalog, 30+ languages, and Adaptive Pricing for local-currency display; dynamic methods are filtered for eligibility and availability varies by product, so the catalog count is not a per-checkout display guarantee.

## Key Features

| Feature | Detail |
| --- | --- |
| UI | Stripe-hosted page |
| UI customization | Limited — 20 preset fonts, 3 border radius, custom logo/background/button color |
| Integration effort | Hosted shareable link: no website code. Embedded buy button: paste a script and web component; existing-customer reuse also requires server authentication and CustomerSession creation. See [[source-stripe-payment-links]]. |
| Language | Auto-matches browser language (30+ languages) |
| Currency | Adaptive Pricing (always enabled) — displays local currency automatically; see [[stripe-adaptive-pricing]] |
| Payment methods | 40+ catalog; dynamically displayed methods filter for eligibility and vary by product, with Dashboard management (2026-11-07 overview) |
| Automatic receipts | Yes |
| No-code refunds | Yes |
| Reusability | Reuse unlimited times, or limit number of purchases |

## What You Can Do

- Share link over email, SMS, social media
- Embed a **buy button** on your website
- Track with URL parameters and UTM codes
- Collect addresses and phone numbers
- Charge for shipping (multiple rates)
- Add promotion codes, upsells, and optional items
- Let customers edit quantities
- Let customers choose what to pay (tips/donations)
- Create subscription payment links
- Manage payment methods from Dashboard without code

**Checkout Studio route (2026-11-07 overview):** The [[source-stripe-payment-links]] overview links a Payment Links management route labeled **Private preview** for configuration, performance monitoring, and experiments across Checkout integrations. The overview link does not establish account access, eligibility, or experiment results.

## Payment Links vs Invoicing

| | Payment Links | Invoicing |
| --- | --- | --- |
| Customer | Anyone with the link | Specific individual or business |
| Reusability | Reuse many times | Can't reuse; duplicate and edit |
| Partial payments / plans | ✗ | ✓ |
| Customers edit quantities | ✓ | ✗ |
| Customers choose price | ✓ | ✗ |
| Upsells and optional items | ✓ | ✗ |
| Quote → Invoice flow | ✗ | ✓ |
| Smart Retries | Subscription links only | ✓ |
| Reconciliation | URL parameters | Auto-reconciliation |
| Stripe Tax | ✓ | ✓ |

## API Key Details

- **Create**: `stripe.paymentLinks.create({ line_items: [{ price, quantity }] })`
- **Line items**: up to 20 for flat-rate prices; customer-defined pricing uses a `custom_unit_amount` Price ID as the sole line item with quantity `1` (2026-11-07 create guide). Inline fixed `price_data.unit_amount` is a separate fixed-product example. See [[source-stripe-payment-links]].
- **Inline price**: use `price_data` to create product + price in one call
- **Subscriptions**: add `subscription_data: { trial_period_days: N }`
- **Customer-defined price**: set `custom_unit_amount: { enabled: true }` on Price object
- **Override payment methods**: `payment_method_types: ['card', 'klarna']`
- **Supported pricing models**: flat rate, tiered, package pricing (recurring + one-off)

## PHP 21.3.0 Update Surface

The PHP SDK's Payment Link update parameters add `application_fee_amount`, `application_fee_percent`, `on_behalf_of` and `transfer_data` (destination plus optional amount). This is version-qualified Connect request-contract evidence, not a statement that every merchant or payment flow is eligible. Source: [[source-github-stripe-php]].

## PHP 22.0.0 Scope Boundary

Payment Link create/update still accept `payment_method_types` in this version; selected Checkout/PaymentIntent/SetupIntent request removals must not be applied here. Create line-item inline product data adds `tax_details` with optional `performance_location`/`tax_code`. Method/tax contracts do not establish merchant eligibility. Source: [[source-github-stripe-php]].

## Checkout Customization

| Feature | API param | Notes |
| --- | --- | --- |
| Payment limit | `restrictions.completed_sessions.limit` | Auto-deactivates when reached |
| Custom deactivation message | `inactive_message` | Shown when link is deactivated/limit reached |
| Billing address | `billing_address_collection` | `required` or `auto` |
| Shipping address | `shipping_address_collection.allowed_countries` | ISO 2-letter codes; saved to `shipping_details` |
| Phone number | `phone_number_collection` | Required field on checkout |
| Business/individual name | `name_collection.business` / `.individual` | Saved to `collected_information` |
| Tax IDs | Dashboard setting | Appears on invoices |
| Automatic tax | `automatic_tax.enabled: true` | Stripe Tax product; collects billing address |
| Terms of service | `consent_collection.terms_of_service: 'required'` | Requires ToS URL in Public details |
| Custom fields | `custom_fields[]` | 3 types: text/numbers/dropdown; max 255; dropdown: 10 Dashboard / 200 API |
| Adjustable quantities | `line_items[].adjustable_quantity` | `enabled: true`, `minimum`, `maximum` |
| Free trial without PM | `payment_method_collection: 'if_required'` | Subscriptions only; set `trial_settings.end_behavior.missing_payment_method` |
| Custom domain | Dashboard setting | Use your subdomain instead of `buy.stripe.com` |

**URL parameters**: `prefilled_email`, `locked_prefilled_email` (takes precedence over prefilled_email), `prefilled_promo_code`, `locale`; `prefilled_amount` sets an editable starting amount only for pay-what-you-want links, with a positive smallest-unit value within configured minimum/maximum. Invalid values fall back to the stored preset or empty state; fixed-price links ignore it and multi-currency behavior is restricted. See [[source-stripe-payment-links]] (2026-11-07 customize capture).

## Automatic surcharge preview (2026-11-07 customize guide)

The [[source-stripe-payment-links]] customize capture describes an API-only US private preview for one-off and customer-chooses-what-to-pay links, limited to cards and Apple Pay. It requires provider-app onboarding and a preview API version; it excludes subscription links and Adaptive Pricing. Stripe Tax can be used with its surcharge tax behavior setting. The merchant must verify legal and network-rule compliance; this capture does not establish access or a successful charge.

## Buy Button (Embedded)

- **Embed**: `<stripe-buy-button>` web component + `<script src="https://js.stripe.com/v3/buy-button.js">`; uses publishable key — update embed code if key revoked
- **2 layouts**: simple button or card widget; customizable colors/shapes/fonts/CTA/language
- **3 attributes**:
  - `client-reference-id` — reconciliation string, max 200 permitted characters; invalid values are silently discarded while checkout remains usable; sent in `checkout.session.completed` on payment completion
  - `customer-email` — prefills an uneditable email; invalid values are silently discarded while checkout remains usable
  - `customer-session-client-secret` — pass the secret from a server-created CustomerSession after authenticating the existing customer; use `customer_account` for a customer-configured Account or `customer` for Customer v1. See [[source-stripe-payment-links]].
- **CustomerSession**: create server-side; provide `client_secret` within 30 min; expires 30 min after providing; **never cache — generate fresh per render**
- **CSP**: `frame-src` + `script-src` must allow `https://js.stripe.com`
- **Limitation**: requires website domain; test locally via Python SimpleHTTPServer or `http-server` npm

## Tracking and Reconciliation

- **UTM codes**: append `utm_source`, `utm_content`, `utm_medium`, `utm_term`, `utm_campaign` to URL; max 150 chars; requires `redirect` confirmation behavior; invalid values silently discarded
- **`client_reference_id`**: unique string attached to Checkout Session; sent in `checkout.session.completed` webhook; max 200 chars; **do not include secrets** — links may appear in unexpected places
- **Post-payment**: `after_completion: { type: 'redirect', redirect: { url } }` on payment link
- **Webhook fulfillment**: `checkout.session.completed`; also listen for async methods (2–14 days)

## Sharing and Lifecycle

- **Share**: copy URL from Dashboard or use `paymentLink.url` from API; share via email/SMS/social/website/app
- **QR code**: generate in Dashboard; **never expires**; if link deactivated → QR redirects to expiration page
- **Buy button**: embed on website via Dashboard → copy/paste code
- **Deactivate**: set `active: false` (API) or Dashboard overflow menu → Deactivate; **cannot delete**, only deactivate/reactivate

## Promotions, Upsells, and Optional Items

- **Promotion codes**: `allow_promotion_codes: true`; create coupon → promo code in Dashboard; use `prefilled_promo_code` URL param to prefill; **caveat**: one-time Payment Links create guest customers by default, so promotion codes restricted to first-time orders won’t work as expected. See [[source-stripe-payment-links]].
- **Subscription upsells**: the guide documents setup on the Dashboard Price detail page; selecting an upsell immediately applies it to eligible Payment Links using that price, such as a monthly-to-yearly option during checkout. The guide does not establish that Dashboard setup is the only channel. See [[source-stripe-payment-links]].
- **Optional items**: up to 10; `optional_items: [{ price, quantity, adjustable_quantity? }]`; supports min/max quantity
- **Cross-sells**: product-level config in Dashboard; auto-adds optional item across all eligible payment links for that product; **cross-sells won't appear if `optional_items` is set on the payment link directly**

## Shipping Rates

- **API**: `stripe.shippingRates.create({ display_name, type: 'fixed_amount', fixed_amount: { amount, currency }, delivery_estimate: { minimum/maximum: { unit: 'business_day', value } } })`
- **Add to link**: `shipping_options: [{ shipping_rate: id }]`
- **Constraint**: shipping rates work with **one-time prices only** — not recurring/subscription prices
- Requires collecting billing + shipping address first

## Key Constraints

- No support for partial payments or payment plans
- Smart Retries and reminder emails only available for **subscription** payment links
- Customer-chooses model: **no recurring payments**; the create guide showed a default Dashboard maximum of 10,000.00 SGD on 2026-04-20 and 10,000.00 USD on 2026-11-07, with a Stripe Support route to request an increase. These are capture-specific wordings, not a verified maximum for every merchant. See [[source-stripe-payment-links]].
- Async payment methods (bank debits, vouchers): 2–14 days to confirm; use webhooks for fulfillment
- Mobile (iOS Dashboard app): product/subscription links only — customer-chooses not supported
- PCI compliance handled by Stripe

## Related Concepts

- [[paypal-payment-links]] — PayPal's equivalent (4 options: link/buy button/cart/QR; one-time only; no subscriptions)
- [[source-stripe-checkout-sessions]] — Checkout Sessions API (code-based alternative)

## Sources

- [[source-stripe-payment-links]] — Payment Links overview, features table, Invoicing vs Payment Links comparison, API creation details
- [[source-stripe-inapp-digital-goods-payment-links]] — April/November 2026 iOS digital-goods guide: a static Dashboard Payment Link needs no application endpoint for link creation, while production fulfillment calls for a trusted webhook endpoint or receiver; US/EEA Apple Pay is a dated can-accept statement, and `client_reference_id` is reconciliation context rather than authenticated identity (https://docs.stripe.com/mobile/digital-goods/payment-links; old raw/stripe-inapp-digital-goods-payment-links-2025.md:8-14,123-129,142-146; new raw/stripe-mobile-digital-goods-payment-links-2026-11-07.md:9-15,122-128,141-145).
- [[source-stripe-managed-payments-payment-links]] — Payment Links with Managed Payments (MoR): managed_payments.enabled, immutable MoR state, variable pricing, iOS Stripe app restriction
