---
title: "Stripe Payment Links Overview"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payment-links/buy-button"
raw_files:
  - "stripe-payment-links-buy-button-2026-11-07.md"
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

Stripe Payment Links product overview — features, availability, no-code hosted-link capabilities, and a detailed comparison against Stripe Invoicing. This update adds the same-URL 2026-11-07 buy-button capture; the other listed Payment Links URLs retain their 2026-04-20 descriptions pending their separately scoped comparisons.

## Key Takeaways

- **Hosted link** — Stripe-hosted payment page can be shared without website integration. Embedding a buy button requires pasting a script and `<stripe-buy-button>` web component into the website; reusing an existing customer requires server authentication and CustomerSession creation.
- **40+ payment methods** managed in Dashboard; dynamic presentment
- **Adaptive Pricing** — automatically displays local currency
- **Browser language** auto-detection (30+ languages)
- **Reusable** — share multiple times; optionally limit purchase count
- **Subscription support** — create subscription payment links (Smart Retries + reminders apply)

## Invoicing vs Payment Links

||Payment Links|Invoicing|
|---|---|---|
|Customer|Anyone with link|Specific customer|
|Partial payments|✗|✓|
|Edit quantities|✓|✗|
|Choose price|✓|✗|
|Upsells|✓|✗|
|Quote→Invoice|✗|✓|
|Smart Retries|Subscription links only|✓ all|
|Reconciliation|URL parameters|Auto|

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

## Buy Button (2026-11-07 Capture)

Choose an existing Payment Link or create a new one, select **Buy button**, customize its simple-button or card-widget design, then copy embed code into the website. Branding and call to action initially follow the Payment Link; colors, shape, font, language, and call to action can be changed. The embed consists of a `<script>` tag loading `https://js.stripe.com/v3/buy-button.js` and a `<stripe-buy-button>` web component with buy-button ID and publishable key. If that publishable key is revoked, update the embed code. The 2026-11-07 capture uses an HTML example; its prose still says React can mount the component with the script in `index.html`. The 2026-04-20 capture retains a React example, whose omission from the newer example is not a deprecation statement.

| Component attribute | Documented behavior and limit |
| --- | --- |
| `client-reference-id` | Reconciliation string attached to the Checkout Session and sent in `checkout.session.completed` on payment completion. Alphanumeric characters, dashes, underscores; at most 200 characters. Invalid values are silently discarded while the payment page continues. Do not infer the identifier was retained merely because checkout opened. |
| `customer-email` | Prefills `customer_email` and prevents customer editing on the payment page. Invalid email values are silently discarded while the payment page continues. |
| `customer-session-client-secret` | Client secret from a server-created CustomerSession for an authenticated existing customer; it is not a client-supplied trusted customer identifier. |

For an existing customer, authenticate on the server and create a CustomerSession for the correct identity: `customer_account` for a customer-configured Account through Accounts v2, or `customer` for Customer v1. Enable the `buy_button` component and send that session's `client_secret` to the client for `customer-session-client-secret`. Supply the secret within 30 minutes; after supply, the CustomerSession expires after another 30 minutes, and the button then cannot create Checkout Sessions. Generate a fresh secret for each render rather than caching one. This timing does not guarantee checkout completion.

The 2026-11-07 page says Accounts v2 is generally available to Connect users and in public preview for other Stripe users; preview participants specify a preview version. It describes Dashboard **Account previews and features → Reusable payment methods for Global Payouts** as the preview enrollment path. This snapshot does not establish a specific account's eligibility or current live availability. The older 2026-04-20 capture contains Node CustomerSession examples; the newer capture switches to curl examples, without evidence that Node support ended.

If a Content Security Policy is deployed, allow `https://js.stripe.com` in both `frame-src` and `script-src`. Rendering requires a website domain; local testing requires an HTTP server on localhost. Without a specified existing customer, a subscription or saved-payment-method Checkout Session creates a Customer, while a one-time payment uses a guest customer. Payment tracking in the Dashboard follows a completed payment; the embedded button alone does not establish one.

## Related Pages

- [[stripe-payment-links]] — Stripe Payment Links concept page
- [[paypal-payment-links]] — PayPal's equivalent product
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payment-links-buy-button-2026-11-07|2026-11-07 buy-button capture]] — embed, attributes, CustomerSession identity and timing, CSP and domain limits
- [[raw/stripe-payment-links-overview-2025|2026-04-20 Payment Links overview]] — features table, hosted sharing, Invoicing comparison
- [[raw/stripe-payment-links-create-2025|2026-04-20 create guide]] — pricing models, API creation, Adaptive Pricing, mobile and asynchronous methods
- [[raw/stripe-payment-links-share-2025|2026-04-20 share guide]] — share channels, QR code, buy button and link lifecycle
- [[raw/stripe-payment-links-track-2025|2026-04-20 track guide]] — UTM and client reference parameters, redirect and webhook
- [[raw/stripe-payment-links-buy-button-2025|2026-04-20 buy-button capture]] — React and Node examples, attributes, CustomerSession timing, CSP
- [[raw/stripe-payment-links-customize-2025|2026-04-20 customize guide]] — checkout fields, limits, trials, URL parameters and domain
- [[raw/stripe-payment-links-shipping-2025|2026-04-20 shipping guide]] — shipping rates and one-time price constraint
- [[raw/stripe-payment-links-promotions-2025|2026-04-20 promotions guide]] — promotions, upsells, optional items and cross-sells
