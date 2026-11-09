---
title: "Stripe: Accept Stablecoin Payments"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: https://docs.stripe.com/payments/accept-stablecoin-payments
raw_files:
  - "stripe-accept-stablecoin-payments-2025.md"
tags: [stripe, stablecoin, crypto, usdc, checkout, elements, payment-intents, direct-api, ios, android, metamask, testnet]
---

## Summary

The May 1, 2026 capture is a detailed, bundled guide for enabling Pay with Crypto and integrating through **six variant routes**: Checkout, Elements with Checkout Sessions API, Elements with Payment Intents API, Direct API, iOS, and Android. It also describes Payment Links, testnet setup, redirect handling, and payment events. The November 7, 2026 base capture is a **20-line index** pointing to those six variants; its lack of detailed instructions does not establish that an option ended. This job did not capture the November variant contents, so the detailed integration facts below remain **dated May evidence**, not verified current variant behavior or proof of successful execution.

## Access, Eligibility, and Payment Flow (May 2026 Capture)

The older guide says customers can pay with stablecoins globally while **only US businesses** can accept them, subject to payment-method access. A business first requests **Stablecoins and Crypto** in Dashboard Payment Methods; Stripe reviews the request, shows it as **Pending** during review, and marks it active **after approval**. This dated page does not verify approval or geographic eligibility for any live account.

For an approved, active method, the guide recommends Stripe's **default dynamic payment methods** with Payment Links, Hosted Checkout, Embedded Checkout Forms, or Elements. Under those named conditions, Stripe says no further integration update is needed and it displays stablecoin payment options to **eligible customers**. That is separate from merchant approval and is not an unconditional promise that every customer sees Crypto. A custom integration can list `crypto` manually.

For the stablecoin payment flow described there, the customer is redirected to `crypto.stripe.com` to connect a wallet and complete payment; funds settle in the merchant's **Stripe balance in USD**. The payer's stablecoin, a Checkout line-item currency, a PaymentIntent or Direct API payment currency, and USD balance settlement are distinct concepts.

## Route Inventory and Dated Integration Details

| Route | May 2026 bundled guide | November 2026 base index |
| --- | --- | --- |
| Checkout | Create a Checkout Session with `payment_method_types` including `crypto`; this path says **all line items use USD** and shows a USD curl example. | Lists Checkout variant. |
| Elements + Checkout Sessions API | Server creates a Session with `ui_mode: 'elements'` and returns its client secret. The front end initializes Checkout Elements, mounts Payment Element, collects a valid email, and calls `confirm()`; dynamic or manual method listing is shown. | Lists Elements / Checkout Sessions API variant. |
| Elements + Payment Intents API | Payment Element and server-created PaymentIntent; examples use USD and can select `payment_method_types: ['crypto']`. Accounts v2 `customer_account` and Customers v1 `customer` examples are separate. The client calls `elements.submit()` then `stripe.confirmPayment` with `return_url`; after a server-side intent update, `elements.fetchUpdates()` refreshes the UI. | Lists Elements / Payment Intents API variant. |
| Direct API | Create a PaymentIntent server-side with a **supported currency**, amount, and `crypto` method; pass its client secret to the client, then use `stripe.confirmPayment` and a return URL or handle a `requires_action` / `redirect_to_url` next action. The old guide says crypto payment currencies map to merchant country, with USD the default local currency. | Lists Direct API variant. |
| iOS | Server-created PaymentIntent plus iOS SDK flow; the dated example uses `STPPaymentHandler.confirmPayment`, crypto payment method params, and a return URL handled by an app URL scheme or universal link. | Lists Mobile / iOS variant. |
| Android | Server-created PaymentIntent plus Android SDK flow; the dated example uses `PaymentLauncher.confirm` and crypto payment method creation, redirecting to `crypto.stripe.com/pay`. | Lists Mobile / Android variant. |

The Checkout requirement that `line_items` use `usd` belongs to **that Checkout path** in the May guide. The USD PaymentIntent values in other route examples are examples, not a universal payment-currency rule. The Direct API section explicitly allows supported currencies mapping to the merchant country, with USD as default. USD **Stripe-balance settlement** is a separate May guide statement. No supported-currency list, current route contract, or current account eligibility can be inferred from the November base index alone.

The old bundled examples include HTML + JavaScript and React variants, client-secret handling, manual and dynamic method selection, and mobile setup. They include placeholder keys and incomplete or dated sample code; their presence does not prove a current SDK version, successful payment, or PCI compliance for an application.

## Payment Completion and Testing (May 2026 Capture)

For Payment Intents routes, the guide describes confirming the payment and using the redirect return URL to inspect the PaymentIntent status. For fulfillment actions, it advises listening for `payment_intent.succeeded` through Dashboard, webhook, or partner integration **instead of relying on a client callback**, because the client may close or manipulate its response. A redirect or client callback alone is not proof of a completed charge, blockchain finality, or USD settlement.

The historical sandbox instructions use test API keys, a wallet, and testnet assets. Stripe recommends MetaMask, Polygon **Amoy** (chain ID `80002`, `POL` gas), a Polygon Amoy USDC token at `0x41E94Eb019C0762f9Bfcf9Fb1E58725BfB0e7582`, the Circle USDC faucet, and a POL faucet. Some faucets may require mainnet tokens. The guide also lists Paxos USDP, Devnet SOL, Sepolia ETH, and Amoy POL faucets. These are **test examples**; faucet availability, token contracts, and mainnet support are not independently verified by the November index. The May guide notes that a test refund can arrive as a token contract different from the payment token, and suggests checking the refund transaction hash.

## Provenance Boundary

The May capture provides detailed route, access, currency, and testnet statements. The November capture supplies **navigation links only** to variant pages that were not fetched in this job. Keep the May raw as the factual source; use the new raw index only to locate routes. The index does not refresh the older guide's merchant access, supported payment currencies, API parameters, SDK examples, or payment outcomes. See [[source-stripe-stablecoin-payments]] for the separate payment-method overview and its own capture date.

## Related Pages

- [[stripe-stablecoin-payments]] — stablecoin concept and product overview
- [[source-stripe-stablecoin-payments]] — separate stablecoin method overview
- [[stripe]] — provider overview

## Related raw API references

- [[raw/stripe-payments-accept-stablecoin-payments-2026-11-07|2026-11-07 stablecoin variant index]] — links to Checkout, both Elements API variants, Direct API, iOS, and Android; detailed variant content was not captured

## Raw Sources

- [[raw/stripe-accept-stablecoin-payments-2025|2026-05-01 bundled Stripe stablecoin integration guide]] — dated detailed guide, including six variant routes, examples, and testnet instructions
