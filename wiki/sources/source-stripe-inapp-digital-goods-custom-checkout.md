---
title: "Accept iOS Digital Goods Payments with Custom Checkout (Elements)"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/mobile/digital-goods/custom-checkout"
raw_files:
  - "stripe-mobile-digital-goods-custom-checkout-2026-11-07.md"
  - "stripe-inapp-digital-goods-custom-checkout-2025.md"
tags: [stripe, mobile, ios, digital-goods, payment-element, elements, subscriptions, accounts-v2, customers-v1, universal-links, webhooks]
---

## Summary

The April and November 2026 captures describe an **iOS app-to-web subscription checkout**: the app opens the merchant's own Elements/Payment Element checkout page in Safari, then uses a universal link to return to the app. This is distinct from the Stripe-hosted Checkout and Payment Links paths; the guide does not describe a native in-app Elements payment form. The guide is for in-app digital goods, content, and subscriptions; it routes physical goods, goods/services consumed outside the app, and real-time person-to-person services to the native iOS payment guide. It documents a server-side subscription and webhook integration. See [[stripe-inapp-payments]] and [[stripe-subscriptions]]. [April capture](../../raw/stripe-inapp-digital-goods-custom-checkout-2025.md#L4-L16), [April scope](../../raw/stripe-inapp-digital-goods-custom-checkout-2025.md#L24-L38), [November capture](../../raw/stripe-mobile-digital-goods-custom-checkout-2026-11-07.md#L5-L17), [November scope](../../raw/stripe-mobile-digital-goods-custom-checkout-2026-11-07.md#L21-L45).

## Path and dated Apple Pay scope

The April and November captures say an iOS app selling these digital goods in the **US or EEA** can accept Apple Pay using Elements, while saying the app cannot accept Apple Pay for these goods in other regions. This is the guide's dated, region-specific statement, not an independent current platform-policy or merchant-eligibility determination. The guide says Apple Pay appears in the Payment Element when the device is supported and a card is saved in Wallet. The April guide says to use `payment_method_types` for additional methods; the November guide's two model branches instead direct merchants to enable additional methods in the Dashboard. That documentation change alone does not prove every API-level option was removed. [April geography](../../raw/stripe-inapp-digital-goods-custom-checkout-2025.md#L8-L14), [April methods](../../raw/stripe-inapp-digital-goods-custom-checkout-2025.md#L153); [November geography](../../raw/stripe-mobile-digital-goods-custom-checkout-2026-11-07.md#L9-L15), [November methods](../../raw/stripe-mobile-digital-goods-custom-checkout-2026-11-07.md#L220), [second branch](../../raw/stripe-mobile-digital-goods-custom-checkout-2026-11-07.md#L272).

| Dated guide path | Own server | Customer identity | Checkout surface |
| --- | --- | --- | --- |
| Payment Links | Not required by this guide's comparison | Path-dependent | Hosted link; for limited products/prices |
| Stripe-hosted Checkout | Server path in linked guide | Path-dependent | Stripe-hosted page |
| Elements (this guide) | Yes | Customer-configured Account **or** Customer | Merchant-owned web checkout opened in Safari |

The table distinguishes documented routes, not universal platform capabilities. The Payment Links and hosted Checkout rows are navigation to separate guides, not a claim that this capture fully specifies their server and identity details. [April path comparison](../../raw/stripe-inapp-digital-goods-custom-checkout-2025.md#L8-L16); [November path comparison](../../raw/stripe-mobile-digital-goods-custom-checkout-2026-11-07.md#L9-L17).

## Customer identity and incomplete subscription

The April example used a `Customer` and only gave a general instruction to substitute Accounts v2 references. The November guide gives **separate** customer-configured Accounts v2 and Customers v1 branches. It says Accounts v2 is generally available for Connect users and in public preview for other Stripe users; preview participants must specify a preview version. Its preference for customer-configured Accounts is stated for **most use cases**, not a universal migration requirement or proof that an account is eligible. Store a mapping from the app user to the appropriate Stripe identity so purchases can be recovered. [April note and mapping](../../raw/stripe-inapp-digital-goods-custom-checkout-2025.md#L22-L28), [April Customer example](../../raw/stripe-inapp-digital-goods-custom-checkout-2025.md#L66-L100); [November Accounts scope](../../raw/stripe-mobile-digital-goods-custom-checkout-2026-11-07.md#L39-L45), [November Account example](../../raw/stripe-mobile-digital-goods-custom-checkout-2026-11-07.md#L93-L129), [November Customer example](../../raw/stripe-mobile-digital-goods-custom-checkout-2026-11-07.md#L131-L167).

For an initial Payment Element subscription payment, both November examples pass `payment_behavior: 'default_incomplete'` and expand `latest_invoice.payment_intent`; the server returns that PaymentIntent's client secret and stores the Subscription ID for later lifecycle changes. **The identity key differs:** Accounts v2 uses `customer_account: customerAccountId`; Customers v1 uses `customer: customerId`. The April Customer example used `customer` and the same incomplete-payment pattern. These are guide examples, not proof that the request succeeded or that access should be granted when the Subscription is first created. [April Subscription](../../raw/stripe-inapp-digital-goods-custom-checkout-2025.md#L102-L141); [November Account Subscription](../../raw/stripe-mobile-digital-goods-custom-checkout-2026-11-07.md#L169-L220), [November Customer Subscription](../../raw/stripe-mobile-digital-goods-custom-checkout-2026-11-07.md#L222-L272).

```js
// Accounts v2 branch in the November guide:
customer_account: customerAccountId

// Customers v1 branch:
customer: customerId

// Both illustrated branches:
payment_behavior: 'default_incomplete'
expand: ['latest_invoice.payment_intent']
```

## Safari return, confirmation, and fulfillment

Configure the merchant domain's `/.well-known/apple-app-site-association` with `application/json`, an Associated Domains entitlement, and success/cancel fallback pages. The app opens its own checkout URL in Safari; the web Payment Element calls `stripe.confirmPayment` with a universal-link `return_url`. The Swift sample checks whether payments are disabled by parental controls and sets a local `paymentComplete` flag when a URL contains `success`. That sample flag and a returned URL are navigation/UI examples, not authoritative payment or entitlement state. [April links](../../raw/stripe-inapp-digital-goods-custom-checkout-2025.md#L155-L207), [April app and confirm](../../raw/stripe-inapp-digital-goods-custom-checkout-2025.md#L209-L268); [November links](../../raw/stripe-mobile-digital-goods-custom-checkout-2026-11-07.md#L274-L326), [November app and confirm](../../raw/stripe-mobile-digital-goods-custom-checkout-2026-11-07.md#L328-L385).

The server example verifies the Stripe webhook signature and handles `invoice.payment_succeeded`, `invoice.payment_failed`, and `customer.subscription.updated` to update its own subscription state. The November guide explicitly says `customer.subscription.updated` still applies with customer-configured Accounts; the April general suggestion to replace event references should not be followed for that named event. Tie grant/renewal of digital access to verified payment/subscription state for the relevant user, including recurring events; a browser return, UI flag, or mere Subscription creation does not establish a paid state. The snippets show event branches and comments, not a complete working entitlement system. [April event guidance](../../raw/stripe-inapp-digital-goods-custom-checkout-2025.md#L270-L326); [November events](../../raw/stripe-mobile-digital-goods-custom-checkout-2026-11-07.md#L388-L439).

## Testing and related pages

The guide lists sandbox cards for immediate processing, 3DS2, and insufficient-funds decline, plus steps for debugging universal links using Associated Domains development mode and `SharedWebCredentials` logs. These are test instructions, not evidence of a live purchase or functioning integration. [April tests](../../raw/stripe-inapp-digital-goods-custom-checkout-2025.md#L328-L393); [November tests](../../raw/stripe-mobile-digital-goods-custom-checkout-2026-11-07.md#L441-L508).

- [[stripe-inapp-payments]] — iOS and Android payment paths
- [[stripe-subscriptions]] — subscription state and access
- [[source-stripe-inapp-digital-goods-checkout]] — separate Stripe-hosted Checkout path
- [[source-stripe-inapp-digital-goods-payment-links]] — separate Payment Links path
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-mobile-digital-goods-custom-checkout-2026-11-07|November 7, 2026 custom checkout guide]] — full webpage content (516 lines)
- [[raw/stripe-inapp-digital-goods-custom-checkout-2025|April 22, 2026 custom checkout guide]] — historical webpage content (401 lines)
