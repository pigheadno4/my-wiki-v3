---
title: "iOS Subscription Management with Customer Portal"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: https://docs.stripe.com/mobile/digital-goods/customer-portal
raw_files:
  - "stripe-mobile-digital-goods-customer-portal-2026-11-07.md"
  - "stripe-inapp-digital-goods-customer-portal-2025.md"
tags: [stripe, mobile, ios, digital-goods, customer-portal, subscriptions, universal-links, webhooks, billing-portal]
---

## Summary

Guide for **managing** iOS digital-goods subscriptions through a Stripe-hosted customer portal opened from the app in Safari. Both the 2026-04-22 and 2026-11-07 captures describe this management flow. They explicitly leave subscription purchasing, user authentication, and native StoreKit purchases to other guides. The US/EEA Apple Pay external-page statement is context for a separate purchase path, not an implementation or permission rule established by this portal guide. See [[source-stripe-inapp-digital-goods-checkout]] for the separate Checkout purchase guide.

## Portal configuration

Configure the portal independently in sandbox and live mode for the actions customers may take. In the stated Connect flow, configure the portal **for the platform, not as a connected account**. The adjacent API option lets the Connect platform manage different portal configurations for its connected accounts or customer groups; it does not say connected accounts configure their own portal here.

A product catalog is required when customers can upgrade, downgrade, or change subscription quantities; invoicing-only portal use does not require one. Product names and descriptions are editable in Dashboard and API, while quantity restrictions are editable in Dashboard. Price amount, currency, and billing interval are fixed when the price is created. In the Stripe Tax context, letting customers add or update tax IDs in the portal is optional. Portal preview and testing are limited to a sandbox and require Dashboard edit permission.

## Portal session and return

When a customer wants to manage a subscription, the server creates a `stripe.billingPortal.sessions.create` session using that customer's Stripe customer ID and a `return_url`, then returns the session URL to the app. The app calls its server and opens that URL in Safari. Configure universal links with an `apple-app-site-association` file and Associated Domains entitlement, and serve a fallback page at the return URL in case the link does not open the app. The sample's `cus_...` placeholder and comment to replace customer lookup logic do not implement or prove user authentication or authorization.

## Subscription webhooks and access

For production, configure a webhook endpoint subscribed to appropriate event types. `customer.subscription.created`, `customer.subscription.updated`, and `customer.subscription.deleted` are examples; handle all events needed to monitor the statuses of the subscriptions configured for the portal. The Node example only branches on created and deleted and maps them to true/false; it does not inspect subscription status or implement an updated branch. A created event alone does not prove an active subscription or entitlement. Determine access from the subscription's actual governing status or active entitlements, including after updates, rather than treating an event name as an access decision.

## Optional: Deep links

Customer portal deep links can open a specified portal action and customize the return behavior after that action.

## Documentation change boundary

The 2026-11-07 page changes example setup language, Ruby/Node installation presentation, CLI steps, and iOS package instructions, including omitting the earlier CocoaPods steps. The assigned captures do not establish that CocoaPods or the older Node setup is deprecated. The linked subscription lifecycle and webhook guides were not fetched for this unit; this page does not enumerate every status transition or prove a customer's entitlement state.

## Related Pages

- [[stripe-inapp-payments]] — in-app payments concept page
- [[stripe-subscriptions]] — Stripe subscriptions concept page
- [[source-stripe-inapp-digital-goods-checkout]] — subscription purchase, Checkout path
- [[source-stripe-inapp-digital-goods-custom-checkout]] — subscription purchase, Elements path

## Raw Sources

- [[raw/stripe-mobile-digital-goods-customer-portal-2026-11-07|2026-11-07 iOS customer portal guide]] — updated full guide and examples.
- [[raw/stripe-inapp-digital-goods-customer-portal-2025|2026-04-22 iOS customer portal guide]] — historical full guide and local image reference.
