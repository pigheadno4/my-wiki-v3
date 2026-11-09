---
title: "Stripe Payment Links Overview"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payment-links"
raw_files:
  - "stripe-payment-links-2026-11-07.md"
  - "stripe-payment-links-create-2026-11-07.md"
  - "stripe-payment-links-share-2026-11-07.md"
  - "stripe-payment-links-buy-button-2026-11-07.md"
  - "stripe-payment-links-customize-2026-11-07.md"
  - "stripe-payment-links-promotions-2026-11-07.md"
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

Payment Links provide shareable URLs for Stripe-hosted checkout pages. The six 2026-11-07 captures cover the overview, creation, sharing, buy button, checkout customization, and promotions; eight 2026-04-20 raw files retain the earlier overview and separate create, share, track, buy-button, customize, shipping, and promotions guidance. Each dated capture describes its own URL. The newer URL-parameter comparison made no substantive update, so tracking guidance below remains attributed to the older track raw. These documents describe product behavior, not a verified merchant configuration or completed transaction. See [[stripe-payment-links]] and [[stripe]].

## Product choice and availability

- **Hosted link:** Create and share a Stripe-hosted page through the Dashboard without website code. A buy button instead requires website embed code; using an existing customer through that button also requires server authentication and a CustomerSession.
- **Payment methods:** The overview describes a 40+ method catalog managed in Dashboard. Dynamic display filters for eligibility and method availability varies by product; the figure is not a per-buyer or per-link display guarantee.
- **Language, currency, reuse:** The overview describes browser-language matching across 30+ languages, local-currency presentation through Adaptive Pricing, and repeated sharing with an optional purchase limit. It does not promise unlimited volume or every currency for every customer.
- **Subscription links:** The overview comparison limits Smart Retries and reminder-email recovery to subscription Payment Links. The customer-chooses-what-to-pay model is not a recurring-payment or recurring-donation path.
- **Checkout Studio:** The November overview links a Payment Links management route labeled **Private preview**. The create and customize guides also link Studio for management or branding. These links do not establish account access or an experiment result.

| Capability | Payment Links | Invoicing |
| --- | --- | --- |
| Customer | Anyone with the link | A specific customer |
| Partial payments or plans | No | Yes |
| Editable quantity and chosen price | Yes, where configured | No in the overview comparison |
| Upsells or optional items | Yes | No in the overview comparison |
| Quote to invoice | No | Yes |
| Smart Retries and reminders | Subscription links only | Available for automatic collection |
| Reconciliation | URL parameters | Automatic bank-payment reconciliation |

This table reflects the dated overview comparison, not an account-specific feature test. See the new overview at [[raw/stripe-payment-links-2026-11-07]] (lines 73–107) and older overview at [[raw/stripe-payment-links-overview-2025]] (lines 41–64).

## Creation, pricing, and payment state

The create guide distinguishes fixed-price products or subscriptions from customer-chosen amounts for tips, donations, or pay-what-you-want sales. Its Dashboard flow supports an optional suggested amount and minimum/maximum for the latter. For fixed products, the API can use a Price ID in `line_items` or inline fixed `price_data`; a subscription can use a recurring Price and `subscription_data.trial_period_days`. The older fixed inline `price_data.unit_amount` sample is not the variable-price handoff. For customer-chosen pricing, first create a Price with `custom_unit_amount[enabled]=true`, then use that Price ID as the sole Payment Link line item with `quantity=1`. The guide allows up to 20 flat-rate line items, while the customer-chosen path has one item with quantity one. These example paths do not establish a new universal ban on fixed inline prices. [Create capture](../../raw/stripe-payment-links-create-2026-11-07.md#L39-L113).

The 2026-04-20 create guide states a default Dashboard maximum of **10,000.00 SGD** for customer-chosen amounts; the 2026-11-07 same-URL capture says **10,000.00 USD**. Both give a Stripe Support route for an increase. The captures do not explain the currency difference or verify the effective maximum for a particular merchant. The iOS Dashboard app example creates product or subscription links, not customer-chosen links. `payment_method_types` can specify a method set instead of the Dashboard-managed dynamic set. Bank debits and vouchers may take **2–14 days** to confirm; use payment-clearance webhooks before fulfillment. Link creation, a browser return, or `checkout.session.completed` for a delayed method is not itself settlement. [Old maximum](../../raw/stripe-payment-links-create-2025.md#L29-L33), [new maximum and mobile](../../raw/stripe-payment-links-create-2026-11-07.md#L29-L36), [methods and delayed confirmation](../../raw/stripe-payment-links-create-2026-11-07.md#L120-L139).

> [!warning] Contradiction
> The dated create guides broadly say Adaptive Pricing is always enabled for Payment Links. The 2026-11-07 customize guide explicitly says its API-only automatic-surcharge private preview is incompatible with Adaptive Pricing. Keep that specialized exception and its access conditions; neither statement establishes a universal runtime resolution for every link or account. [Create wording](../../raw/stripe-payment-links-create-2026-11-07.md#L143-L145), [customize exception](../../raw/stripe-payment-links-customize-2026-11-07.md#L364-L423).

## Sharing, QR codes, and link state

Copy a URL in Dashboard or read the Payment Link API's `url` field to share it by email, text, social media, website, or app. Dashboard can create or download a PNG QR code and provide buy-button embed code. The QR image itself does not expire; after the underlying link is deactivated, a scan redirects to an expiration page and no new purchase can be finalized through that link. A created Payment Link cannot be deleted. Dashboard deactivation or API `active=false` blocks future purchases; `active=true` reactivates it. None of these link-state actions reverses a completed payment. The November share diff's API-reference URL edits do not establish a runtime API change. [New share guide](../../raw/stripe-payment-links-share-2026-11-07.md#L15-L43), [old share guide](../../raw/stripe-payment-links-share-2025.md#L14-L42).

A configured use limit counts **completed Checkout Sessions**, with `restrictions[completed_sessions][limit]` tied to `checkout.session.completed`. The link deactivates at the configured count; creating or opening a Session is not a consumed use. The deactivation message can be customized with the Dashboard or `inactive_message`. Counting Session completion is distinct from final success for asynchronous payment methods. [Customize capture](../../raw/stripe-payment-links-customize-2026-11-07.md#L13-L62).

## Embedded buy button

The buy-button flow starts with an existing or new Payment Link and copies a `<script>` loading `https://js.stripe.com/v3/buy-button.js` plus the `<stripe-buy-button>` web component into a website. Simple-button and card-widget designs are described. React mounting remains in the November prose and the older React example; a newer HTML sample does not deprecate React. A revoked publishable key requires updated embed code. Rendering requires a website domain; local testing uses an HTTP server, and a deployed Content Security Policy must allow `https://js.stripe.com` in both `frame-src` and `script-src`. [Buy-button capture](../../raw/stripe-payment-links-buy-button-2026-11-07.md#L7-L47), [older React example](../../raw/stripe-payment-links-buy-button-2025.md#L24-L28).

- `client-reference-id` is a reconciliation string of at most 200 alphanumeric, dash, or underscore characters. A valid value is attached to the Checkout Session and sent in `checkout.session.completed`; an invalid value is silently discarded although the payment page still works.
- `customer-email` prefills an uneditable email; an invalid value is also silently discarded.
- `customer-session-client-secret` comes from a **server-created CustomerSession** after authenticating the existing customer. Use `customer_account` for a customer-configured Account or `customer` for Customer v1, and enable the buy-button component. Accounts v2 is described as generally available for Connect users and public preview for other users, with a preview version for participants; that does not prove a given account's access. Supply the secret within 30 minutes, then the Session expires another 30 minutes after supply. Generate a fresh secret for each render rather than caching it. Expiry prevents the button from creating new Checkout Sessions; it is not a payment-completion timer.

Without an existing customer specified, the guide describes Customer creation for subscription or saved-method Sessions and a guest customer for a one-time payment. An embedded button or an open page proves neither retained attributes nor successful payment. [Attribute table and identities](../../raw/stripe-payment-links-buy-button-2026-11-07.md#L49-L93).

## Checkout customization and tax products

The customize guide retains billing and shipping address, phone, name and tax-ID collection, terms consent, custom fields, branding, domains, adjustable quantities and subscription trials. Dashboard address choices can make fields required, while API billing-address collection can be `required` or `auto`; shipping collection needs `allowed_countries`. Name fields may be optional. Custom fields allow text (255 characters), numbers (255 digits), or a dropdown with up to 10 options on Dashboard-created links and up to 200 after API creation. A free trial without payment-method collection is a **subscription-product** path with trial-end handling, not a one-time-link option. [Customize details](../../raw/stripe-payment-links-customize-2026-11-07.md#L64-L141), [fields and trials](../../raw/stripe-payment-links-customize-2026-11-07.md#L182-L248), [trials](../../raw/stripe-payment-links-customize-2026-11-07.md#L321-L340).

For URL personalization, `prefilled_email` is editable, `locked_prefilled_email` is uneditable and takes precedence, `prefilled_promo_code` needs promotions enabled, and `locale` selects a supported language. New `prefilled_amount` supplies an **editable starting amount only for pay-what-you-want links**; fixed-price links ignore it. Use a positive integer in the custom price's default currency smallest unit and within its configured minimum and maximum. Invalid values fall back to the stored preset or empty state. The preset amount prevents automatic customer-local-currency use for that amount, and a non-default `currency` at link creation raises an error. This is the customize capture's parameter, separate from the unchanged tracking-URL comparison. [Customize parameter table](../../raw/stripe-payment-links-customize-2026-11-07.md#L285-L315).

Stripe Tax is a paid calculation-and-collection product after setup. The newer customize guide separately points digital-product sellers to **Managed Payments**, a merchant-of-record route in which Stripe handles tax registration, collection, filing and remittance along with fraud, disputes and support. That paragraph does not make ordinary Stripe Tax a merchant-of-record service or prove Managed Payments eligibility. See [[source-stripe-managed-payments-payment-links]]. [Customize tax sections](../../raw/stripe-payment-links-customize-2026-11-07.md#L147-L180).

**Automatic surcharge is a 2026-11-07 private preview**, not general Payment Links availability. The guide requires a surcharge-provider Stripe App and onboarding, a preview `Stripe-Version` header for API creation (the example uses `2026-10-28.preview`), and `automatic_surcharge[enabled]=true` with a calculation basis of `total_before_tax` or `total_after_tax`. It describes Stripe Tax interaction through `automatic_surcharge[tax_behavior]`. The path is **API-only**, supports one-off or customer-chosen pricing, excludes subscription links and Adaptive Pricing, and in this preview is US-only for cards and Apple Pay. Unsupported methods receive no applicable surcharge. The merchant must verify provider calculation against applicable law and network rules. The captured page proves neither preview access, legal compliance nor a live payment outcome. [Surcharge conditions](../../raw/stripe-payment-links-customize-2026-11-07.md#L364-L423).

## Promotions, upsells, and optional items

Enable customer-entered promotion codes with `allow_promotion_codes=true`; `prefilled_promo_code` can prefill a shared URL. One-time Payment Links create guest customers by default, so first-time-order-only codes **may not work as expected**; the guide does not say every such code fails. The November guide documents subscription upsell setup on the Dashboard **Price detail** page: selecting an eligible upsell price immediately applies it to eligible links using that price. It does not establish Dashboard exclusivity. A link can offer up to **10 optional items** with initial or adjustable quantities. Product-associated cross-sells appear across eligible links containing that product, but do not appear when the link specifies additional optional items directly. The Node-to-curl promotion-code example and other presentation edits do not establish changed runtime behavior. [New promotion guide](../../raw/stripe-payment-links-promotions-2026-11-07.md#L15-L91), [old promotion guide](../../raw/stripe-payment-links-promotions-2025.md#L16-L99).

## Retained tracking and shipping guidance

The 2026-04-20 track raw identifies `utm_source`, `utm_content`, `utm_medium`, `utm_term` and `utm_campaign`, with a 150-character UTM limit and `redirect` confirmation behavior for carrying them to the redirect URL. `client_reference_id` is a 200-character reconciliation string on a Checkout Session, not authenticated customer identity. Invalid values can be dropped while checkout still works; shareable URLs must not contain secrets. `checkout.session.completed` supports reconciliation, and delayed bank-debit or voucher methods need additional payment-outcome webhooks. The separately reviewed 2026-11-07 URL-parameter page made editorial and example changes, so this source retains the older track raw as its factual provenance rather than adding a new raw identity. [Historical track guide](../../raw/stripe-payment-links-track-2025.md#L10-L48).

The retained 2026-04-20 shipping guide describes billing and shipping address collection, shipping-country selection, Dashboard rates, and an API-created fixed-amount ShippingRate with a delivery estimate and `shipping_options` on a Payment Link. That guide says shipping rates on Payment Links work only with **one-time prices**, not subscription prices. This is dated guidance from the old shipping raw; no newer shipping capture was merged. [Historical shipping guide](../../raw/stripe-payment-links-shipping-2025.md#L14-L52).

## Related Pages

- [[stripe-payment-links]] — Payment Links concept and reciprocal source route
- [[source-stripe-managed-payments-payment-links]] — separate Managed Payments merchant-of-record integration
- [[stripe]] — Stripe company
- [[paypal-payment-links]] — PayPal counterpart

## Raw Sources

- [[raw/stripe-payment-links-2026-11-07|Payment Links overview, 2026-11-07]] — product table, dynamic eligibility footnote, Checkout Studio private-preview route
- [[raw/stripe-payment-links-create-2026-11-07|Create guide, 2026-11-07]] — Dashboard pricing models, variable Price handoff, dated USD maximum, delayed methods
- [[raw/stripe-payment-links-share-2026-11-07|Share guide, 2026-11-07]] — distribution, persistent QR image and inactive-link redirect, deactivation/reactivation
- [[raw/stripe-payment-links-buy-button-2026-11-07|Buy button guide, 2026-11-07]] — embed, attributes, CustomerSession identities and timing
- [[raw/stripe-payment-links-customize-2026-11-07|Customize guide, 2026-11-07]] — completed-Session limits, checkout fields, amount preset, Managed Payments route, surcharge preview
- [[raw/stripe-payment-links-promotions-2026-11-07|Promotions guide, 2026-11-07]] — codes, qualified guest-customer caveat, upsells, optional items and cross-sells
- [[raw/stripe-payment-links-overview-2025|Payment Links overview, 2026-04-20]] — historical hosted-page features and Invoicing comparison
- [[raw/stripe-payment-links-create-2025|Create guide, 2026-04-20]] — historical pricing, API samples, SGD maximum wording, mobile and delayed methods
- [[raw/stripe-payment-links-share-2025|Share guide, 2026-04-20]] — historical channels, QR and link-state behavior
- [[raw/stripe-payment-links-track-2025|Track guide, 2026-04-20]] — historical UTM limits, client reference, redirect and delayed-method webhooks
- [[raw/stripe-payment-links-buy-button-2025|Buy button guide, 2026-04-20]] — historical React/Node examples, attributes, CustomerSession and CSP
- [[raw/stripe-payment-links-customize-2025|Customize guide, 2026-04-20]] — historical limits, fields, tax, consent, URL parameters, trials and quantities
- [[raw/stripe-payment-links-shipping-2025|Shipping guide, 2026-04-20]] — historical rates and one-time-price constraint
- [[raw/stripe-payment-links-promotions-2025|Promotions guide, 2026-04-20]] — historical codes, upsells, optional items and cross-sells
