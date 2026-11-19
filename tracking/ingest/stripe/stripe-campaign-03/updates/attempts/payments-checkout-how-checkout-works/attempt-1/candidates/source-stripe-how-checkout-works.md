---
title: "Stripe: How Checkout Works"
type: source
date_ingested: 2026-04-20
date_updated: 2026-11-15
canonical_url: https://docs.stripe.com/payments/checkout/how-checkout-works
original_format: webpage
raw_files:
  - "stripe-how-checkout-works-2025.md"
  - "stripe-checkout-customization-2025.md"
  - "stripe-checkout-collect-addresses-2025.md"
  - "stripe-checkout-phone-numbers-2025.md"
  - "stripe-checkout-name-collection-2025.md"
  - "stripe-checkout-promotional-emails-2025.md"
  - "stripe-checkout-compliant-promotional-emails-2025.md"
  - "stripe-checkout-limited-inventory-2025.md"
  - "stripe-checkout-adjustable-quantity-2025.md"
  - "stripe-checkout-pay-what-you-want-2025.md"
  - "stripe-checkout-payment-methods-2025.md"
  - "stripe-checkout-guest-customers-2025.md"
tags: [stripe, checkout, checkout-sessions, hosted, embedded, elements, features, mixed-cart, adaptive-pricing, billing-address, shipping-address, phone-number, name-collection, promotional-emails, consent, compliance, gdpr, inventory, session-expiry, adjustable-quantity, pay-what-you-want, donations, tips]
---

## Summary

The April 20, 2026 full guide captured hosted page, embedded page, and Checkout Elements bodies: their Checkout Session lifecycles, 26-row Hosted feature table, mixed carts, saving, expiration, webhooks, and agentic checkout. The November 7, 2026 canonical capture is only a four-link variant index. It does not establish the behavior of the linked bodies or remove the earlier guidance.

## Key Takeaways

- **11 built-in Hosted-table rows (April 2026)**: digital wallets + Link, responsive mobile, SCA, CAPTCHA, PCI, card validation, error messaging, adjustable quantities, auto tax, international language, Adaptive Pricing
- **15 customizable Hosted-table rows (April 2026)**: taxes, branding, optional items, payment methods, upsells, custom domains (hosted only, **paid**), receipts, discounts, success page, abandoned carts, Link autofill, Tax IDs, shipping, phone, billing cycle date
- **Custom domains**: paid feature; hosted page only
- **Session expiry (April 2026)**: 24h default; configurable 30min–24h via `expires_at`; can also be manually expired via `stripe.checkout.sessions.expire(id)`. The application can process `checkout.session.expired` to return reserved items to inventory or send an abandonment message; the event does not itself release stock.
- **Mixed cart**: `mode: 'subscription'` + mix of recurring + one-time Price IDs in `line_items`
- **Checkout for agents**: structured controls + programmatic guidance for AI agents navigating checkout pages
- **Save payment methods**: `payment_intent_data.setup_future_usage` (payment mode) or automatic (subscription mode)
- **Guest customers**: Sessions without an existing/new Customer use guest customers

## Feature Table (Built-in vs Customizable)

| Feature | Type |
| --- | --- |
| Digital wallets + Link | Built-in |
| Responsive mobile design | Built-in |
| SCA-ready | Built-in |
| CAPTCHAs | Built-in |
| PCI compliance | Built-in |
| Card validation | Built-in |
| Error messaging | Built-in |
| Adjustable quantities | Built-in |
| Automatic tax collection | Built-in |
| International language support | Built-in |
| Adaptive Pricing | Built-in |
| Collect taxes | Customizable |
| Custom branding (colors/buttons/font) | Customizable |
| Optional items | Customizable |
| Global payment methods | Customizable |
| Subscription upsells | Customizable |
| Custom domains (hosted only, paid) | Customizable |
| Email receipts | Customizable |
| Apply discounts | Customizable |
| Custom success page | Customizable |
| Recover abandoned carts | Customizable |
| Autofill with Link | Customizable |
| Collect Tax IDs | Customizable |
| Collect shipping information | Customizable |
| Collect phone numbers | Customizable |
| Set subscription billing cycle date | Customizable |

## Lifecycle per Mode (April 2026 full bodies)

| Captured body | Lifecycle and state boundary |
| --- | --- |
| Hosted page | Server creates Checkout Session with trusted line items and mode; customer follows `session.url` to the hosted page; `success_url` is a return route. Handle Session events on the server and verify payment status before paid-order fulfillment. |
| Embedded page | Server creates Checkout Session with `ui_mode: 'embedded_page'` and `return_url`; client mounts the embedded form. A return URL and `checkout.session.completed` are not alone proof of paid funds. |
| Checkout Elements | Server creates Checkout Session; client renders Elements on site. Handle completion through a server event destination and the payment-status boundary. |

The April body calls its embedded variant `payment-ui=embedded-form` while its Session example uses `ui_mode: 'embedded_page'`. The November index separately links `payment-ui=embedded-page` and `payment-ui=checkout-form`. Their linked bodies were not captured; the labels do not establish behavioral equivalence or Checkout Form SDK availability.

## Key Webhooks

| Event | Use |
| --- | --- |
| `checkout.session.completed` | Session completed. For paid orders, check `payment_status === 'paid'`; delayed methods may require later `checkout.session.async_payment_succeeded` or failed-event handling. |
| `checkout.session.expired` | Merchant handler can return reserved items to inventory or send an abandonment email. |

## Address Collection

- **Billing address**: `billing_address_collection: 'required'` — forces collection on every session (default: only when needed, e.g. for tax calculation)
- **Shipping address**: `shipping_address_collection.allowed_countries` — array of ISO two-letter country codes (e.g. `["US", "CA"]`)
- Shipping details saved to `shipping_details` property on the Checkout Session object, included in `checkout.session.completed` webhook payload
- Works for both **hosted** (`success_url`) and **embedded** (`ui_mode: 'embedded_page'` + `return_url`) modes — same params, same behavior

## Phone Number Collection

- `phone_number_collection: { enabled: true }` — adds a **required** phone number field
- Supported in `payment` and `subscription` modes only — **not** `setup` mode
- Field placement: under shipping address fields (if collecting address), otherwise below email input
- One phone number per session
- **E.164 format guaranteed** except for wallet payments (Apple Pay/Google Pay) — wallets provide their own format
- **3 retrieval locations**: `Account.contact_phone`, `Customer.phone`, `CheckoutSession.customer_details.phone`
- Existing customer phone prefills the field; customer-updated phone overwrites the saved value
- Customer portal supports self-service phone number updates

## Name Collection

- **`name_collection` param**: collect `business` and/or `individual` names as **first-class** top-level fields (separate from billing/shipping names)
- Each field: `enabled: true`, optionally `optional: true` (default is required)
- **Express checkout impact**: when business name is required, Apple Pay and one-click buttons move to bottom of form or are disabled
- **Retrieval**: `Customer.business_name` / `Customer.individual_name`; `CheckoutSession.collected_information.business_name` / `.individual_name`; also in `customer_details` hash
- `Customer.name` auto-set to `business_name` or `individual_name` (business takes priority)

## Pay-What-You-Want / Tips / Donations

- **Mechanism**: `custom_unit_amount: { enabled: true }` on Price object — customer sets amount at checkout
- **Optional bounds**: `preset` (suggested initial amount), `minimum`, `maximum` on the price
- **Limitations**: single line item only (quantity = 1); no promo codes/discounts; no recurring payments; no optional items
- **Use cases**: tips, donations, pay-what-you-want products/services
- **Inline pricing alternative**: `price_data` on Checkout Session also supports one-off donations but isn't reusable (API only)
- Works for both hosted and embedded modes — same Price ID, same session create pattern

## Adjustable Quantities

- `adjustable_quantity: { enabled: true }` on `line_items` — customers can change quantities during checkout
- **Defaults**: min `0`, max `99`; absolute max `999,999`
- If initial `line_items[].quantity > 99`, set `adjustable_quantity.maximum ≥ quantity`
- **Inventory reservation pattern**: reserve `adjustable_quantity.maximum` units (not `line_items.quantity`) at session create to avoid overselling
- Checkout prevents removing the last remaining item
- **Post-payment**: `stripe.checkout.sessions.listLineItems(session.id, { limit: 100 })` → finalized quantities; removed items absent from response

## Promotional Email Consent

- `consent_collection: { promotions: 'auto' }` — adds a **dynamic checkbox** to Checkout for collecting customer consent to promotional emails
- Checkbox display is jurisdiction-aware: automatically hidden or disabled where local data privacy laws prohibit it; default checked state also varies by country pair (merchant + customer)
- Consent stored in `CheckoutSession.consent.promotions`; retrieve via `checkout.session.completed` webhook
- Works for both **hosted** (`success_url`) and **embedded** (`ui_mode: 'embedded_page'` + `return_url`) modes — same param
- Common pattern: store consenting customers' emails for cart abandonment recovery or newsletter campaigns

## Promotional Email Compliance

- **Checkbox label**: "Keep me updated with news and personalized offers"
- **US**: opt-out model — can send unless customer opts out; **ROW**: affirmative consent required (unchecked default)
- **Checkbox default logic**: Stripe considers both merchant account jurisdiction + customer IP address; unchecked default when either is in an affirmative-consent jurisdiction
- **Recovery emails**: only for customers who entered email + checkbox was checked at session expiry; recommend limiting broader campaigns to completed-purchase + consented customers
- **Unsubscribe**: every promotional email must include sender info + unsubscribe mechanism; honor promptly; withdrawal must be as easy as consent; Stripe redirects data subject requests back to merchant
- **Limited use**: consent data may only be used for promotional emails — no other purposes without separately obtained rights
- **Privacy policy**: must disclose collection/use of data for promotional emails; also covers prospective customers (non-completers)

## Related Pages

- [[stripe]] — Stripe company route.
- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-checkout-sessions]] — Checkout Sessions API deep dive
- [[source-stripe-checkout-quickstart]] — Hosted + embedded quickstart code

## Raw Sources

- [[raw/stripe-how-checkout-works-2025|stripe-how-checkout-works-2025]] — Full How Checkout Works: 3 modes, 24-feature table, mixed cart, session expiry, save payment details, guest customers, Checkout for agents (371 lines, 2 MP4 + 1 PNG)
- [[raw/stripe-checkout-customization-2025|stripe-checkout-customization-2025]] — Customize Checkout: 4 sub-pages (Appearance, Card brands, Custom domain, Product images); custom domain applies to Checkout + Payment Links + customer portal
- [[raw/stripe-checkout-collect-addresses-2025|stripe-checkout-collect-addresses-2025]] — Collect physical addresses: billing_address_collection, shipping_address_collection with allowed_countries, shipping_details in webhook
- [[raw/stripe-checkout-phone-numbers-2025|stripe-checkout-phone-numbers-2025]] — Collect phone numbers: phone_number_collection, E.164 format, 3 retrieval locations, wallet limitations, customer portal updates
- [[raw/stripe-checkout-name-collection-2025|stripe-checkout-name-collection-2025]] — Collect customer names: name_collection (business/individual), first-class fields, express checkout impact, retrieval from Customer + Checkout Session (1 CDN image)
- [[raw/stripe-checkout-promotional-emails-2025|stripe-checkout-promotional-emails-2025]] — Collect promotional email consent: consent_collection.promotions='auto', jurisdiction-aware checkbox, consent.promotions on Checkout Session, webhook pattern (1 CDN image)
- [[raw/stripe-checkout-compliant-promotional-emails-2025|stripe-checkout-compliant-promotional-emails-2025]] — Compliance best practices: US opt-out vs ROW affirmative consent, checkbox default logic, unsubscribe requirements, limited use restriction, privacy policy disclosure
- [[raw/stripe-checkout-limited-inventory-2025|stripe-checkout-limited-inventory-2025]] — Limited inventory: manual expire endpoint (sessions.expire), expires_at param (30min–24h), checkout.session.expired webhook for inventory release
- [[raw/stripe-checkout-adjustable-quantity-2025|stripe-checkout-adjustable-quantity-2025]] — Adjustable quantities: adjustable_quantity param (min/max/enabled), defaults (0–99), max up to 999999, inventory reservation pattern, listLineItems post-payment fulfillment
- [[raw/stripe-checkout-pay-what-you-want-2025|stripe-checkout-pay-what-you-want-2025]] — Pay-what-you-want: custom_unit_amount on Price, preset/min/max bounds, limitations (1 item, no discounts/recurring), tips/donations use cases (1 CDN image)
- [[raw/stripe-checkout-payment-methods-2025|stripe-checkout-payment-methods-2025]] — Payment methods: dynamic (Dashboard settings + eligibility) by default; override with payment_method_types; multiple PMs still reordered by location
- [[raw/stripe-checkout-guest-customers-2025|stripe-checkout-guest-customers-2025]] — Guest customers: sessions without Customer object; grouped by card/email/phone; read-only, no new charges; customer_creation param; Customers tab export only

## Related raw API references

- [[raw/stripe-payments-checkout-how-checkout-works-2026-11-07|2026-11-07 Checkout variant index]] — navigation-only capture linking Full hosted page (`payment-ui=stripe-hosted`), Full embedded page (`embedded-page`), Embedded form (`checkout-form`), and Elements (`checkout-elements`); no linked body or runtime behavior was captured.
