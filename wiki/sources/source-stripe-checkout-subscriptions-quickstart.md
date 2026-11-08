---
title: "Stripe — Prebuilt Subscription Page with Checkout (Quickstart)"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/quickstart"
raw_files:
  - "stripe-billing-quickstart-2026-11-07.md"
  - "stripe-checkout-subscriptions-quickstart-2026.md"
tags: [stripe, subscriptions, checkout, billing, quickstart, entitlements, customer-portal, trial, automatic-tax]
---

## Overview

Stripe Billing's hosted [[stripe-checkout]] subscription quickstart demonstrates a product with a recurring Price, a Checkout Session in `subscription` mode, a customer portal, and webhook and entitlement guidance. Its event-handler snippets log events or leave fulfillment calls commented; they do not implement entitlement grants. It is a sample integration, not a separate product or proof of successful payment. The 2026-11-07 webpage capture expands the visible instructions and snippets; the 2026-05-12 structured-UI capture remains separate historical evidence. See [[stripe-subscriptions]] and [[stripe-entitlements]].

## Key takeaways

- For the November sample, create or select a Product with a recurring Price and set the Price's lookup key. The server resolves that key to a Price ID for the Checkout Session. Keep authoritative price, availability, and other sensitive inventory information on the server; the client submits a lookup key, not a trusted amount. Set `mode: 'subscription'` and redirect to the returned hosted Session URL. The success URL must be publicly accessible; the sample puts `session_id={CHECKOUT_SESSION_ID}` in its query string.
- The sample presents either a customer-configured Account or a Customer identity. Its portal flow creates a portal Session for the corresponding identity and redirects to that Session's URL. The example derives the customer from the Checkout Session ID, while recommending that production integrations store the identity with the authenticated user. The May capture called Accounts v2 “recommended in most cases”; that is dated May wording, absent from the November capture, not evidence of reversal.
- A success-page message or redirect is not an access decision. The November quickstart says that after successful payment and redirect, the sample should verify the subscription is `active` before granting subscribed products and features. For feature entitlements it directs listening to active-entitlement summary events and using the list active entitlements API for the customer. Its `/webhook` instruction calls for the signing secret in `STRIPE_WEBHOOK_SECRET`. See [[stripe-checkout]] for the broader webhook and delayed-payment fulfillment pattern.
- The May capture's detailed React client and Node.js/Express excerpt is one visible choice, while its structured-UI header also lists HTML/React frontends and Ruby, Node.js, PHP, Python, Go, .NET, and Java backends. The November flattened capture exposes more language and UI variants, but repeats `success_url`, `subscription_data`, `customer`/`customer_account`, and portal creation alternatives in adjacent code. These are not a single copy-paste runnable program. The May Node portal excerpt retrieves a Checkout Session but does not create the portal Session before redirecting to `portalSession.url`.

## Detail locators

- November setup and flow: Product, recurring Price, lookup key, features and payment methods (raw lines 23–41); preview, Checkout, success, and portal pages (43–63); server-side Price selection, subscription mode, success URL, redirects and active-status check (211–249).
- November code variants: library setup (65–209); HTML/React and multi-language snippets (427–1530); duplicated Node identity/portal branches (620–665); run variants (1531–1718). Use the interactive builder's chosen variant rather than combining the flattened alternatives.
- November optional features and tests: three test-card scenarios (387–395); trial days must be at least 1, with `pause` or `cancel` for a trial without a payment method at its end (401–409); billing-cycle anchor (411–417); activate Stripe Tax before enabling automatic tax (419–425).
- May historical capture: structured UI choices (3–4), Accounts v2 wording (12), five named webhook events and signature-verification description (68–78), test cards (80–90), optional trial/anchor/tax notes (92–96), React excerpt (98–182), Node excerpt and incomplete portal branch (184–285).

## Related

- [[stripe]] — company
- [[stripe-subscriptions]] — subscription lifecycle and provisioning
- [[stripe-checkout]] — hosted Checkout and broader fulfillment states
- [[stripe-entitlements]] — feature access and active-entitlement routes
- [[source-stripe-subscriptions-overview]] — lifecycle and status guide

## Raw Sources

- [[raw/stripe-billing-quickstart-2026-11-07|Stripe Billing hosted subscription quickstart — captured 2026-11-07]]
- [[raw/stripe-checkout-subscriptions-quickstart-2026|Structured-UI quickstart and React/Node excerpt — captured 2026-05-12]]
