---
title: "Stripe — Embeddable Pricing Table for Subscriptions"
type: source
date_ingested: 2026-05-12
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/checkout/pricing-table"
raw_files:
  - "stripe-payments-checkout-pricing-table-2026-11-07.md"
  - "stripe-pricing-table-2026.md"
tags: [stripe, subscriptions, pricing-table, checkout, no-code, customer-session, embed]
---

## Summary

The May 12 and November 7, 2026 captures describe a Dashboard-created embeddable subscription pricing table. It displays Products and Prices on the merchant site through Stripe's `<stripe-pricing-table>` web component, then sends the customer to a prebuilt Stripe Checkout flow. The table supports flat-rate, per-seat, tiered pricing, and free trials. The Dashboard generates a script tag and component code; the table uses the account's publishable key, which must be updated in the embed if revoked.

## Create, embed, and customize

Create the table under Dashboard **Product catalog → Pricing tables**, add products and prices, configure display and payment settings, review the customer portal, and copy the generated embed code. Include `https://js.stripe.com/v3/pricing-table.js`, `pricing-table-id`, and `publishable-key`. For React, the guide says to put the script in `index.html` and mount the component. May includes React/TypeScript samples; November selects HTML samples. This change in example language does not establish React removal.

The table can show Product marketing features (also settable through the Product API). One product can have a custom call-to-action instead of the normal Checkout route, with an absolute, relative, `mailto`, or `tel` URL, or a URL using `{PRODUCT_ID}` and `{CUSTOMER_EMAIL}`; the email variable needs the customer email supplied. Custom fields can collect text (255 characters), numbers (255 digits), or a dropdown (10 choices); the guide says not to collect sensitive, protected, legally restricted, or personal data in them. Their values appear in payment details and in the `checkout.session.completed` event after payment completion.

Set `customer-email` to prefill Checkout Session `customer_email`; multi-currency Prices can present local currency, and `test+location_FR@email.com` illustrates location testing. A confirmation page can show a localized message or redirect to a merchant URL containing `{CHECKOUT_SESSION_ID}`; the browser redirect remains separate from event delivery. A free-trial option can collect a payment method only when required; the guide calls for email reminders before a no-method trial ends, otherwise Stripe pauses the trial. The `client-reference-id` attribute passes up to 200 alphanumeric, dash, or underscore characters to the Session for reconciliation; invalid values are silently dropped. Do not place secrets or sensitive data in this public embed attribute.

## Pass an existing customer

For a user already authenticated on the merchant server, create a Customer Session with `components.pricing_table.enabled: true` for either `customer_account` (customer-configured Account, Accounts v2) or `customer` (Customer v1). Return its `client_secret` to the browser and pass it as `customer-session-client-secret` on the pricing table component. These are distinct object identities; the merchant server creates the Customer Session, while the browser receives only its client secret.

Both dated captures give **30 minutes to include the client secret in the pricing table**, followed by **an additional 30 minutes after rendering the pricing table to complete payment**. If the customer session is expired when a Checkout Session is created, Stripe discards the secret and creates a Checkout Session without that associated customer. If it expires after Checkout Session creation but before confirmation, payment confirmation fails. The second window is anchored to pricing-table rendering, not Checkout Session creation.

The captured Accounts v2 guidance says the API is generally available for Connect users and in public preview for other Stripe users; preview users must specify a preview API version. November adds an enrollment route in Dashboard **Account previews and features → Reusable payment methods for Global Payouts**. May's access-request sentence was incomplete. This is dated access guidance, not verification that a specific account is eligible or enrolled. Both captures separately say the pricing table is **not designed to work with Connect**; platform fee collection is one example of an unsupported Connect feature. This product limitation is broader than platform fees. The Accounts v2 statement about GA access for Connect users concerns customer-configured Account identity and does not establish Connect compatibility for the pricing-table product.

## Fulfillment and limits

The Checkout flow sends `checkout.session.completed` for completed payment in the guide's example. Set up an event destination to receive it for fulfillment and reconciliation; November links the event setup route at `/events/set-up-events`, where May linked `/event-destinations`. The guide's new summary diagram merges an event label and website return in one arrow, but its detailed instructions treat server event destination and browser confirmation/redirect separately. An embed display, Session creation, or browser return is not payment or settlement proof; evaluate the completed Checkout/payment state for fulfillment.

The table displays at most **four products**, **three Prices per product**, and **three unique pricing intervals**; a Dashboard step says up to four products per interval. Tiered quantity above the default 99 must be allowed by increasing the table's adjustable-quantity Max. It does not support usage-based pricing or an intermediate account-signup step before Checkout. Both guides say it is **not designed to work with Connect**, including features such as a platform collecting fees. The guide describes a shared limit of 50 pricing-table reads per second. An iframe sandbox needs `allow-top-navigation` for Checkout redirect. Local testing needs an HTTP server on `localhost`; with CSP, allow `https://js.stripe.com` in both `script-src` and `frame-src`. Dashboard edits to Products, Prices, and payment settings update the table UI.

## Related Pages

- [[stripe]] — company overview
- [[stripe-pricing-table]] — concept route
- [[stripe-subscriptions]] — subscription context
- [[stripe-checkout]] — Checkout Sessions and fulfillment context

## Raw Sources

- [[raw/stripe-payments-checkout-pricing-table-2026-11-07|Full pricing-table guide captured 2026-11-07]]
- [[raw/stripe-pricing-table-2026|Full pricing-table guide captured 2026-05-12]]
