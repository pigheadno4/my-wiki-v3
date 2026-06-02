---
title: "GitHub: stripe/stripe-postman — Stripe API Postman Collection"
type: source
date_ingested: 2026-05-13
original_format: github-repo
raw_files:
  - "github-stripe-postman.md"
tags: [stripe, postman, api, developer-tools, testing, rest-api]
---

## Summary

Official Stripe Postman collection (`stripe/stripe-postman`). A single JSON collection (`StripeAPICollection.json`, 84k lines) covering the full Stripe API — 107 endpoint groups, ~400+ endpoints total. Hosted publicly at the [Stripe Developers Postman workspace](https://www.postman.com/stripedev/stripe-developers/overview).

The workspace currently has 4 versioned collections:
- ⭐️ **Stripe API [2024-04-10]** — current/starred version
- Stripe API [2023-10-16]
- Stripe API [06-30-2023]
- Stripe API Demos

## Setup

Two ways to use:
1. **Fork from workspace**: Fork directly from the [Stripe Developers workspace](https://www.postman.com/stripedev/stripe-developers/overview) into your own Postman workspace.
2. **Import JSON**: Copy `StripeAPICollection.json` from GitHub and import via Postman's "Paste Raw Text" dialog.

**Authentication**: Create a Postman environment, add `secret_key` variable with your [test mode secret key](https://dashboard.stripe.com/test/apikeys). Set as active environment and assign to the collection.

## Scope: 107 API endpoint groups

Full coverage of Stripe API objects including: Accounts, Balance, Billing Meters, Charges, Checkout, Coupons, Credit Notes, Customers, Disputes, Entitlement Features, Events, Financial Connections, Forwarding Requests, Identity, Invoices (15 endpoints), Issuing (Authorizations/Cardholders/Cards/Disputes/Tokens/Transactions), Mandates, Payment Intents (11 endpoints), Payment Links, Payment Methods, Prices, Products, Promotion Codes, Quotes, Radar, Refunds, Reporting, Setup Intents, Subscriptions, Tax (Calculations/IDs/Rates/Registrations/Transactions), Terminal (11 reader endpoints), Test Clocks, Tokens, Transfers, Treasury (CreditReversals/DebitReversals/FinancialAccounts/InboundTransfers/OutboundPayments/OutboundTransfers/ReceivedCredits/ReceivedDebits/Transactions), Webhook Endpoints.

Full endpoint group table in stub file: [[github-stripe-postman]].

## Recent changelog (as of 2024-04-15)

- Added `balances` and `payouts_list` on `AccountSession#create.components`
- Added `entitlements.active_entitlement_summary.updated` webhook event
- Added `amazon_pay` support across PaymentIntent, SetupIntent, PaymentMethod, Checkout, ConfirmationToken
- Added `swish` on `PaymentMethodConfiguration`
- `Billing.MeterEvent#create.timestamp` made optional
- Removed `config` on `Forwarding.Request#create`

## Related pages

- [[stripe]] — company page
- [[source-github-stripe-node]] — Node.js SDK (server-side)
- [[source-github-stripe-react-native]] — React Native SDK
- [[source-github-stripe-ios]] — iOS SDK
- [[source-github-stripe-android]] — Android SDK

## Raw Sources

- [[github-stripe-postman]] — stub file with endpoint group index table
