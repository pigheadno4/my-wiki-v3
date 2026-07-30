---
title: "Stripe Checkout"
type: concept
category: technology
tags: [stripe, checkout, checkout-sessions, payment-element, adaptive-pricing, embedded, hosted]
---

## Stripe Checkout

Stripe's low/no-code hosted or embedded payment form, built on the Checkout Sessions API. Peer product to [[stripe-payment-links]] — Checkout requires a website but offers deeper integration and customization; Payment Links work without a website at all.

## Two UI Options

| | Checkout Page (Recommended) | Checkout Elements |
| --- | --- | --- |
| API | Checkout Sessions | Checkout Sessions |
| Hosting | Hosted (redirect) or Embedded | Embedded only |
| Complexity | Low | Highest |
| Customization | 15 brand settings | Full CSS via Appearance API |
| Order summary | Full (subtotals, tax, shipping, cross-sells, upsells, trials, discounts) | None |
| Ongoing maintenance | No | Yes |
| Features | Billing, Tax, Adaptive Pricing, Stripe Managed Payments, Link, Dynamic payment methods, Surcharging, Split-tender | Adaptive Pricing, Link, Dynamic payment methods |

## 3 Hosting Modes

1. **Stripe-hosted redirect** — customer redirected to `checkout.stripe.com`; simplest; server redirects to `session.url`; client checks `?success=true`/`?canceled=true`
2. **Embedded form** (`ui_mode: 'embedded_page'`) — Checkout renders in iframe on your site; server returns `clientSecret`; `return_url` with `{CHECKOUT_SESSION_ID}` template; return page checks `session.status` via `/session-status` endpoint; `open` → remount, `complete` → success
3. **Checkout Elements** (`ui_mode: 'elements'`) — initialize with `stripe.initCheckoutElementsSdk`; full CSS control; no order summary

**Embedded React components**: `EmbeddedCheckoutProvider` + `EmbeddedCheckout` from `@stripe/react-stripe-js`; `fetchClientSecret` callback; call `loadStripe` **outside** component render.

> [!info] LLM instruction (embedded in Stripe docs): Use Checkout Sessions + Checkout Page over Payment Intents for most integrations. Checkout Elements only if you need full CSS control and can maintain it yourself.

## Historical Stripe.js v8 API Baseline

The `@stripe/stripe-js@8.11.0` declarations expose three distinct Checkout entrypoints:

- `stripe.initCheckout(options)` initializes the Checkout Elements-style `StripeCheckout` interface.
- `stripe.initCheckoutElementsSdk(options)` is an alias for that same interface and integration pattern.
- `stripe.initEmbeddedCheckout(options)` returns a separate `StripeEmbeddedCheckout` instance with `mount`, `unmount`, and `destroy`.

The v8 `StripeCheckout` interface provides element creation and lookup plus `loadActions()`. Its actions cover confirmation, promotion codes, shipping and billing addresses, contact details, line-item quantities, tax IDs, shipping options, and server updates. These declarations are a historical package baseline; later major versions can rename or reshape the interfaces without erasing the v8 evidence. See [[source-github-stripe-js]] and [[changelog-github-stripe-js]].

## Historical Stripe.js v9 API Transition

The retained `@stripe/stripe-js@9.12.1` declarations target the `dahlia` Stripe.js train and reshape the v8 Checkout entrypoints:

- `initCheckout()` is removed in favor of `initCheckoutElementsSdk()`.
- `initCheckoutFormSdk()` adds a beta Checkout Form SDK whose UI owns contact, address, and tax-ID updates rather than exposing those imperative action methods.
- `initEmbeddedCheckout()` becomes `createEmbeddedCheckoutPage()`.
- Payment Form Element naming becomes Checkout Form.
- Checkout actions add element validation and optional-line-item add/remove operations.
- Session state adds optional items, removable line items, price IDs, decimal unit amounts, currency options, and surcharge status and totals.

This is a cumulative v8-to-v9 package comparison, not the 9.12.1 patch note alone. The older [[source-stripe-checkout-elements-beta-changelog]] remains useful as dated Clover migration evidence, but its “latest” label and `initCheckout()` example are not current for the retained v9 declarations.

## Checkout Sessions vs Payment Intents (for Elements)

Both integrate with Elements + Appearance API. **Use Checkout Sessions for most integrations** — it handles the same payment flows as Payment Intents with significantly less code.

| Feature | Checkout Sessions | Payment Intents |
| --- | --- | --- |
| Tax calculation | Built-in (`automatic_tax.enabled`) | Manual Tax API integration |
| Subscriptions | Built-in | Manual Subscriptions API |
| Coupons & discounts | Built-in | Manual calculation |
| Shipping costs | Built-in | Manual calculation |
| UI flexibility | Hosted page + embedded + custom | Custom Elements only |
| Address collection | Built-in (billing, shipping, customer) | Manual |
| Order tracking & receipts | Built-in | Custom implementation |
| Amount updates | Dynamic line item updates | Manual |
| Session expiration | Automatic after 24 hours | None |
| Webhook events | Full checkout lifecycle | Payment status only |
| **Adaptive Pricing** | ✓ Exclusive to Checkout Sessions | ✗ Not available |

**IC+ only** (both APIs): Multicapture, Overcapture, Extended authorization, Incremental authorization. See [[source-stripe-elements-advanced-payments]] for full comparison matrix.

## Key Capabilities

- **100+ payment methods** — dynamic presentment based on location, currency, transaction
- **Adaptive Pricing** — auto local currency in 150+ countries (always enabled for Payment Links; available for Checkout); merchant pays 0%, customer pays 2–4% fee; unlocks 20 local PMs; `presentment_details` in webhook; see [[stripe-adaptive-pricing]]
- **Subscriptions**: recurring prices → subscription mode
- **Save payment methods**: `payment_intent_data.setup_future_usage` or `saved_payment_method_options.payment_method_save`
- **Auth + capture**: `payment_intent_data.capture_method: 'manual'`
- **Mobile**: iOS (PaymentSheet), Android (PaymentSheet), React Native (`useStripe`)

## Notable Details

- **Custom domains**: paid feature; applies to Checkout (hosted page only), **Payment Links**, and the **customer portal**
- **Session expiry**: 24h default; configurable 30min–24h via `expires_at`; can also expire manually via API
- **Mixed cart**: set `mode: 'subscription'` + include both recurring + one-time Price IDs in `line_items`
- **Save payment methods**: `payment_intent_data.setup_future_usage` (payment mode) or automatic (subscription mode); saved PMs don't appear for return purchases in Checkout
- **Guest customers**: Sessions without a Customer use guest customers; Stripe groups by card/email/phone; read-only (can't save PMs or charge later); `customer_creation` param controls auto-creation; Dashboard → Customers → Guests tab (not in Payments exports)
- **Checkout for agents**: structured controls + programmatic guidance for AI agents navigating checkout pages (currency, limits, next steps)
- **Address collection**: `billing_address_collection: 'required'` to always collect billing address; `shipping_address_collection.allowed_countries` for shipping (ISO two-letter codes); shipping details in `shipping_details` property + `checkout.session.completed` webhook
- **Shipping rates**: `shipping_options` param with pre-created ShippingRate ID or inline `shipping_rate_data`; fixed amount only; payment mode only; first option pre-selected; delivery estimates with `hour`/`day`/`business_day` units; shipping tax via `tax_code: 'txcd_92010001'`
- **Payment method migration**: remove `payment_method_types` to use Dashboard-managed dynamic methods; non-default PMs (bank redirects) turn off on migration — re-enable in Dashboard; Apple Pay on by default, Google Pay off by default; Google Pay filtered when automatic_tax + no shipping address
- **Delayed notification PMs** (2–14 day delay): Bacs, bank transfers, Boleto, Canadian PAD, Konbini, OXXO, Pay by Bank, SEPA, ACH — must handle `checkout.session.async_payment_succeeded` + `checkout.session.async_payment_failed`; on `checkout.session.completed` check `payment_status === 'paid'` before fulfilling
- **Dynamic shipping options**: embedded mode only; `permissions.update_shipping_details: 'server_only'` disables auto client-side update; `onShippingDetailsChange` client callback triggers server endpoint to validate address + recalculate rates + update session; returns `{type: "accept"}` or `{type: "reject", errorMessage}`
- **Dynamic line items**: **not supported** in hosted or embedded Checkout; **supported** in Elements path (Checkout Sessions API) via beta `runServerUpdate` pattern (SDK `2025-03-31.basil`+) — use cases: inventory checks, cross-sells, subscription interval toggle, order-total-based shipping/tax updates; see [[source-stripe-checkout-dynamic-line-items]]
- **Manual approval** (CS only): run server-side logic (fraud, inventory, PM checks) before finalizing payment; compatible with dynamic line items; PI alternative is "finalize payments on server" — see [[source-stripe-checkout-manual-approval]]
- **Credits** (private access): pass available credit amount into session; applied after tax + shipping; Stripe doesn't track balances — merchant manages; retrieve session after completion for reconciliation; use cases: store credit, prepaid gift cards; CS API only — see [[source-stripe-checkout-redeem-credits]]
- **Mid-checkout customer attachment**: call `checkout.sessions.update(id, { customer: 'cus_...' })` to attach a Customer after session creation; saved PMs, email, and billing info auto-populate without losing previously entered data; enables guest → login flow during checkout
- **Adjustable quantities**: `adjustable_quantity: { enabled: true, minimum, maximum }` on line_items; defaults 0–99; absolute max 999,999; last item cannot be removed; client update via `actions.updateLineItemQuantity({ lineItem: id, quantity })` (React: `checkoutState.checkout.updateLineItemQuantity`); fetch finalized quantities via `sessions.listLineItems(id, { limit: 100 })` post-payment; store internal IDs in `metadata` for reconciliation; quantity changes only — cannot add new line items
- **Pay-what-you-want / tips / donations**: `custom_unit_amount: { enabled: true }` on Price; optional `preset`/`minimum`/`maximum` bounds; single line item only (qty = 1); no promo codes, discounts, or recurring
- **Discounts**: `discounts: [{ coupon: 'ID' }]` (server-applied) or `allow_promotion_codes: true` (customer input field); max 1 per session; Coupon object supports `percent_off`/`amount_off`, `applies_to`, `max_redemptions`, `redeem_by`; Promotion Codes add customer/first-time/minimum-amount restrictions on top; client API: `actions.applyPromotionCode(code)` / `actions.removePromotionCode()` (removes ALL); codes permanently inactive once expired or depleted — cannot reactivate
- **Dynamic discounts** (private preview): `permissions.update_discounts: 'server_only'` + `runServerUpdate`; inline `coupon_data` (no pre-existing Coupon needed); remove via `discounts: []`; see [[source-stripe-checkout-dynamic-discounts]]
- **No-cost orders**: `unit_amount: 0` or 100% off coupon; requires API 2023-08-16+; no payment method collected; guest customers not supported (unit_amount=0 path); fulfill via `checkout.session.completed` only (no PaymentIntent on free sessions)
- **Setup mode** (`mode: 'setup'`): saves payment method without charging; requires `currency`; uses Setup Intents API; retrieve `setup_intent` from session → `payment_method` from SetupIntent → attach to Customer → charge later with `off_session: true`
- **Save during payment**: two strategies — (1) `payment_intent_data.setup_future_usage: 'off_session'` (saves, won't prefill, `allow_redisplay: 'limited'`); (2) `saved_payment_method_options.payment_method_save: 'enabled'` (customer checkbox, prefills, `allow_redisplay: 'always'`); requires `customer_creation: 'always'` if no existing customer; consult legal team (GDPR)
- **Optional items**: `optional_items` array (same structure as `line_items`); up to 10; supports `adjustable_quantity`; customers can always remove; incompatible with upsells, custom amounts, `setup` mode, recurring in payment mode; cross-sells (product catalog-based) auto-appear but disappear when `optional_items` is explicitly set
- **Phone number collection**: `phone_number_collection: { enabled: true }` — required field; `payment`/`subscription` modes only (not `setup`); E.164 format guaranteed except wallets; retrievable from `Account.contact_phone`, `Customer.phone`, or `CheckoutSession.customer_details.phone`
- **Name collection**: `name_collection` with `business` and/or `individual` sub-objects; first-class top-level fields (separate from billing/shipping names); required business name disables express checkout buttons; `Customer.name` auto-set from business_name or individual_name
- **Promotional email consent**: `consent_collection: { promotions: 'auto' }` adds a jurisdiction-aware checkbox; consent stored in `CheckoutSession.consent.promotions`; retrieve via `checkout.session.completed` webhook
- **Custom fields**: `custom_fields` array on session create; up to 3; types: `text` (255 chars), `numeric` (255 digits), `dropdown` (200 options); not in `setup` mode; optional, default values, min/max length; retrieved via `checkout.session.completed` webhook
- **Custom text**: `custom_text` param; 4 placements (`shipping_address`, `submit`, `after_submit`, `terms_of_service_acceptance`); up to 1200 chars; Markdown supported
- **ToS consent**: `consent_collection.terms_of_service: 'required'`; verified via `consent.terms_of_service = 'accepted'` in webhook; customize checkbox text with `custom_text.terms_of_service_acceptance`
- **Submit button**: `submit_type` overrides "Pay" label for one-time payments (`'donate'`, `'book'`, `'auto'`)
- **Payment method reuse agreement**: auto-shown in setup/subscription/payment+future_use; hide with `consent_collection.payment_method_reuse_agreement.position: 'hidden'`; replace with `custom_text.after_submit`
- **Policies**: return/refund, contact info, ToS/privacy links — configured in Dashboard Checkout Settings, not per-session API

## Fulfillment Pattern

- **Dual trigger**: webhook (required) + landing page (optional, for immediate UX)
- **`fulfill_checkout` function**: idempotent; expand `line_items`; check `payment_status !== 'unpaid'`; record fulfillment status
- **Events**: `checkout.session.completed` (immediate) + `checkout.session.async_payment_succeeded` (delayed PMs like ACH)
- **Landing page URL**: `success_url` (hosted), `return_url` (embedded), `after_completion.redirect.url` (Payment Links) — all use `{CHECKOUT_SESSION_ID}` template
- Hosted Checkout waits up to 10s for webhook response before redirect; not supported for organization webhook endpoints

## Key Webhooks

| Event | Trigger | Action |
| --- | --- | --- |
| `checkout.session.completed` | Payment succeeded | Fulfill order |
| `checkout.session.async_payment_succeeded` | Async method (ACH/voucher) succeeded | Fulfill order |
| `checkout.session.async_payment_failed` | Async method failed | Notify customer |

> Always fulfill via webhook — redirect alone is unreliable.

## Checkout vs Payment Links

| | Stripe Checkout | Stripe Payment Links |
| --- | --- | --- |
| Requires website | Yes | No |
| Integration | Code (Checkout Sessions API) | No code |
| Customization | High (brand settings + Appearance API) | Limited (15 brand settings) |
| Dynamic pricing | Via API / Adaptive Pricing | Adaptive Pricing (always on) |
| Reusability | Session-based (one-time) | Reusable link |
| Subscription upsells | Via API | Dashboard-only |
| Custom fields | Via API | Up to 10 (text/number/dropdown) |

## Stripe Tax Integration

- Enable with `automatic_tax: { enabled: true }` on the session
- New customers: address auto-collected and saved; no extra config
- Existing customers: verify address validity (`tax.automatic_tax = 'supported'` for Customers v1; `automatic_indirect_tax.status = 'active'` for Accounts v2); use `customer_update.shipping/address: 'auto'` to propagate checkout-entered address
- Google Pay requires shipping address or existing customer with saved shipping; Apple Pay requires v12+ browser
- See [[stripe-tax]] for full Stripe Tax concept page

## Related Concepts

- [[stripe-payment-links]] — no-code peer product; shareable URLs, no website needed
- [[stripe-subscriptions]] — Stripe Subscriptions: full lifecycle, provisioning pattern, customer portal, flexible billing mode
- [[source-stripe-checkout-build-subscriptions]] — End-to-end subscription integration: product catalog, Checkout Session, webhooks, portal
- [[source-stripe-checkout-sessions]] — Checkout Sessions API deep dive
- [[source-stripe-accept-a-payment]] — full integration guide (4 UI modes, mobile, test cards)
- [[source-stripe-build-payments-page]] — Checkout Page vs Elements comparison table

## Sources

- [[source-stripe-checkout-sessions]] — Checkout Sessions API: 3 UI modes, 5 built-in features, Adaptive Pricing, vs Payment Intents
- [[source-stripe-how-checkout-works]] — How Checkout works: 24-feature table (built-in vs customizable), mixed cart, session expiry, save payment details, guest customers, Checkout for agents
- [[source-stripe-checkout-quickstart]] — Hosted + embedded quickstart: 3 modes, key session params, React client, EmbeddedCheckoutProvider, return_url pattern
- [[source-stripe-checkout-form]] — Checkout form (custom path): single iframe, 100+ methods, built-in returning UI, Appearance API, 2 layouts
- [[source-stripe-checkout-appearance]] — Branding: branding_settings API, logo/icon logic (hosted), Connect override, 24-font compatibility table
- [[source-stripe-checkout-card-brands]] — Card brand blocking: brands_blocked param, 4 brands (discover_global_network covers Discover/Diners/JCB/UnionPay/Elo), filters Link/Apple Pay/Google Pay/saved PMs
- [[source-stripe-checkout-product-images]] — Product images: products.create images param, inline price_data.product_data, drives conversion
- [[source-stripe-accept-a-payment]] — Full guide: webhooks, saved PMs, auth+capture, mobile PaymentSheet
- [[source-stripe-build-payments-page]] — Checkout Page vs Elements: feature matrix, maintenance tradeoffs
- [[source-stripe-checkout-shipping]] — Charge for shipping: ShippingRate API, shipping_options, delivery estimates, shipping tax
- [[source-stripe-checkout-taxes]] — Collect taxes: automatic_tax param, new/existing customer flows, Accounts v2 + Customers v1, customer_update, wallet constraints
- [[source-stripe-checkout-custom-shipping-options]] — Dynamic shipping: embedded only, permissions.update_shipping_details, onShippingDetailsChange callback, server endpoint pattern
- [[source-stripe-checkout-dashboard-payment-methods]] — Dashboard payment methods: migration guide, Apple Pay/Google Pay defaults, delayed notification PM webhook pattern, test table
- [[source-stripe-adaptive-pricing]] — Adaptive Pricing: 150+ countries, 20 local PMs, presentment_details, testing, restrictions, 0% merchant / 2–4% customer fee
- [[source-stripe-checkout-discounts]] — Discounts: Coupon API, apply to session, promotion codes, all restriction params, uniqueness rules, lifecycle
- [[source-stripe-checkout-optional-items]] — Optional items: optional_items API, adjustable_quantity, cross-sells, limitations table
- [[source-stripe-checkout-save-and-reuse]] — Setup mode: session creation, SetupIntent retrieval, off-session charging, 402 handling
- [[source-stripe-checkout-save-during-payment]] — Save during payment: setup_future_usage vs payment_method_save, allow_redisplay, customer_creation, PM removal, GDPR note
- [[source-stripe-checkout-fulfillment]] — Fulfill orders: dual-trigger pattern, fulfill_checkout function, webhook handler, delayed PMs, landing page config
- [[source-stripe-checkout-receipts]] — Receipts + paid invoices: automatic setup, branding, invoice_creation param, invoice_data hash, delayed PM behavior, localization
- [[source-stripe-checkout-custom-success-page]] — Redirect behavior: hosted success page, embedded return page + session status, redirect_on_completion (3 modes), onComplete callback
- [[source-stripe-checkout-abandoned-carts]] — Abandoned cart recovery: consent + after_expiration.recovery, checkout.session.expired, recovery URL, anti-spam, conversion tracking
- [[source-stripe-checkout-conversion-funnel]] — GA4 conversion funnel (hosted): gtag instrumentation, begin_checkout, Measurement Protocol, client ID linking
- [[source-stripe-checkout-embedded-analytics]] — Embedded analytics (private preview): onAnalyticsEvent, 6 event types, client_metadata, failureReason, TypeScript types
- [[source-stripe-elements-advanced-payments]] — Checkout Sessions vs Payment Intents for Elements: feature matrix, IC+ scenarios, integration effort comparison
- [[source-stripe-checkout-sessions-vs-payment-intents]] — Official comparison: 11-row feature matrix, session expiration, webhook lifecycle scope, Adaptive Pricing exclusivity
- [[source-stripe-checkout-elements-quickstart]] — Checkout Elements quickstart: CheckoutElementsProvider, useCheckout hook, 4 elements, return page, Adaptive Pricing, Stripe Tax
- [[source-stripe-web-elements-overview]] — Stripe Elements overview: 7 elements, API comparison diagram, features
- [[source-github-stripe-js]] — package-qualified `@stripe/stripe-js@8.11.0` baseline and `9.12.1` Checkout API transition
- [[stripe-elements]] — Stripe Elements concept page (all 7 elements, React integration patterns)
- [[source-stripe-checkout-custom-components]] — Custom fields (3 types), custom text (4 placements), ToS consent, payment method reuse agreement, localization, Dashboard policies
- [[source-stripe-inapp-digital-goods-checkout]] — iOS digital goods app-to-web flow: origin_context=mobile_app, Universal Links, SKPaymentQueue gate, checkout.session.completed fulfillment
- [[source-stripe-managed-payments-setup]] — Checkout with Managed Payments: managed_payments.enabled, API 2025-03-31.basil, all-products-eligible rule, tax behavior config
