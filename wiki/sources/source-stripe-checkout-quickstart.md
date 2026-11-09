---
title: "Stripe Checkout Quickstart — Hosted & Embedded"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/checkout/quickstart"
raw_files:
  - "stripe-checkout-quickstart-2026-11-07.md"
  - "stripe-checkout-quickstart-2025.md"
  - "stripe-checkout-embedded-quickstart-2025.md"
tags: [stripe, checkout, checkout-sessions, quickstart, payment, subscription, react, node]
---

## Overview

This entry routes two Stripe Checkout quickstarts: the **Stripe-hosted redirect** guide captured at this canonical URL on 2026-04-20 and 2026-11-07, and a separately captured **embedded page** guide from 2026-04-20. The hosted flow creates a Checkout Session on the server and redirects the customer to `session.url` for Stripe's prebuilt payment page. The November hosted capture adds explicit server-side inventory protection, an `integration_identifier` suggestion for comparing implementations, and the instruction to wait for payment success before fulfillment. It does not replace the separate embedded source.

> [!warning] Return-page boundary
> Hosted return-page URL parameters and success-page messaging are for customer display; a redirect or `?success=true` query string is not payment proof or authorization to ship. The November guide says to wait until payment succeeds before fulfilling. The older hosted Node/React URL-query example is a dated UI sample, not a verification flow; consult [[source-stripe-checkout-fulfillment]] for payment-status and delayed-method handling.

## Hosted quickstart

- **Session and server data:** Create the Checkout Session on the server. The Session controls line items, order amount and currency, and eligible payment methods. Keep sensitive inventory information such as price and availability on the server; use predefined Price IDs or server-defined `price_data`. The November guide suggests `integration_identifier` for comparing conversion between Checkout implementations or user segments, not as a required payment field (November lines 159–173).
- **Mode and redirect:** `mode='payment'` is for one-time payments, `subscription` for recurring payments, and `setup` for future payment setup. Supply a publicly accessible `success_url`; after creating the Session, redirect to its `url` (November lines 175–189; April lines 19–27, 59–66).
- **Order preview:** Let customers review or change the order before redirect. The guide says the order is then final and modifications require a new Session (November lines 191–209; April line 76).
- **Return and fulfillment:** The April React example checks `?success=true` and `?canceled=true` to choose display messages, with a local `package.json` proxy to `http://localhost:4242` (April lines 78–133). The November guide explicitly separates that return message from fulfillment until payment succeeds (November lines 215–217, 1121–1123). Its next-step event-destination guidance is not a claim that every `checkout.session.completed` event has paid funds.
- **Testing and customers:** Both captures include test-card examples for success, 3DS, and decline (April lines 135–141; November lines 239–247). Checkout creates a Customer when required, such as subscriptions, and otherwise uses guest customers unless configured with `customer_creation='always'`. An existing Customers v1 identity uses `customer`; when the merchant represents customers as customer-configured Accounts v2, the November guide says an Account ID can be passed as `customer_account` to prefill its associated email (April lines 143–148; November lines 288–298). This is conditional on that identity model, not a universal replacement for Customer IDs.
- **Options:** The hosted guide locates email prefill, submit text, address collection, automatic tax, appearance settings, payouts, refunds, customer management, and Adaptive Pricing in its customization and next-step sections (November lines 253–286, 1125–1139). Checkout studio is an optional build, preview, Dashboard configuration and monitoring route without writing code first (November lines 9–11, 1141–1143); the capture does not establish account-specific access or deployment outcomes.

## Embedded quickstart — separate 2026-04-20 capture

The embedded source is a distinct `?ui=embedded-form` page. Its dated sample uses `ui_mode='embedded_page'` and `return_url` with `{CHECKOUT_SESSION_ID}`, returns a Session `client_secret` from the server, then mounts `EmbeddedCheckoutProvider` and `EmbeddedCheckout` with `fetchClientSecret`. Its sample return page retrieves Session status and remounts an open Session. This embedded example is not evidence for the November hosted guide's implementation or current runtime behavior. See the embedded raw lines 11–19, 29–75, 80–120, 170–179.

## Detail locators

- The April hosted capture has a coherent Node/React sample and local proxy choice (lines 36–70, 78–133). The November capture flattens alternative backend/frontend examples into one text stream, with repeated headings, ports, `YOUR_DOMAIN` and `success_url` assignments, package versions, and placeholder values (lines 159–169, 219–237, 300–893). These fragments are variant-specific presentation, not one runnable program or a new universal Checkout API requirement.

## Related

- [[stripe-checkout]] — Checkout modes, payment status and fulfillment context.
- [[stripe]] — Stripe provider.
- [[source-stripe-checkout-sessions]] — Checkout Sessions API reference route.
- [[source-stripe-accept-a-payment]] — broader integration guide.

## Raw Sources

- [[raw/stripe-checkout-quickstart-2026-11-07|Stripe-hosted Checkout quickstart, 2026-11-07]] — expanded hosted guide with explicit server and fulfillment cautions.
- [[raw/stripe-checkout-quickstart-2025|Stripe-hosted Checkout quickstart, 2026-04-20]] — earlier Node/React example.
- [[raw/stripe-checkout-embedded-quickstart-2025|Embedded Checkout quickstart, 2026-04-20]] — separately captured embedded example.
