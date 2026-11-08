---
title: "Stripe Subscriptions — Set Up Stablecoin Payment Subscription"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/stablecoins"
raw_files:
  - "stripe-subscriptions-stablecoins-2026.md"
tags: [stripe, billing, subscriptions, stablecoins, crypto, usdc, web3, checkout, setup-intents, payment-intents]
---

## Summary

The May 13, 2026 full guide covers subscription payments from a customer's crypto wallet through three paths: Stripe-hosted Checkout, Payment Intents API, and Setup Intents API. The November 7 capture at this URL is a variant index with no operational body. Its three linked variant targets were not read in this update, so the index establishes neither changed API requirements nor removed subscription support. The May flows below are dated documentation, not proof of current merchant eligibility, production token/network support, successful payment, or settlement.

The guide's three monthly price examples differ: 15 USD in Checkout and Setup Intents, and 15 USDC in Payment Intents. The USDC example is a **price currency** example, not evidence of the merchant's settlement asset or of a general subscription token support matrix. The old guide's additional USDP, SOL, and ETH faucet links concern testnet assets, not accepted production subscription methods.

## May 2026: Stripe-hosted Checkout

The May server-side example creates a Checkout Session with `mode=subscription`, `payment_method_types=["crypto"]`, a recurring price, and a success URL. It redirects the customer to the returned Session URL; the customer authorizes future use of the crypto wallet. The guide distinguishes authorization from payment success:

| Event | May guide's meaning and action |
| --- | --- |
| `checkout.session.completed` | Customer submitted Checkout and authorized payment; wait for payment outcome. |
| `invoice.paid` | Payment succeeded; fulfill the purchased service or goods. |
| `invoice.payment_failed` | Payment was declined or otherwise failed; email the customer and ask them to attempt payment again. |

A Checkout completion or redirect alone is not fulfillment proof. The May guide recommends webhooks to confirm payment, though it also discusses Dashboard confirmation. Its example webhook handles event order without assuming `checkout.session.completed` precedes `invoice.paid`.

## May 2026: Payment Intents API

The server-side example creates a subscription with `payment_behavior=default_incomplete`, `payment_settings.save_default_payment_method=on_subscription`, and crypto as the payment-method type. It retrieves the first invoice's **existing** PaymentIntent ID from `latest_invoice.payments` and confirms that PaymentIntent. The confirmation example supplies `payment_method_data.type=crypto`, online `mandate_data.customer_acceptance` fields, and a `return_url`; these are shown example fields, not independently verified universal schema requirements.

The shown `requires_action` response supplies `next_action.redirect_to_url.url` for the customer's wallet setup and payment flow. That state and redirect do not mean payment succeeded. The guide identifies `payment_intent.succeeded` as the post-payment event and says to use asynchronous events rather than a client callback. It describes Dashboard, a custom webhook, or a partner solution for receiving and acting on events; it does not require one particular custom listener for every integration.

## May 2026: Setup Intents API

The May prose specifies server-side SetupIntent creation with `payment_method_types=crypto`, a Customer ID, and `usage=off_session`. Its example also includes `confirm=true`, `payment_method_data.type=crypto`, online mandate acceptance fields, and `return_url`. The response supplies a PaymentMethod ID and `next_action.redirect_to_url.url`; the customer is redirected for setup and then back to the return URL.

The subsequent server-side subscription-create example sets that PaymentMethod as `default_payment_method` and includes `off_session=true`. The guide says creation charges the preset method, while Dashboard status becomes Active **after successful payment**. Setup or redirect alone does not establish a paid invoice.

## May 2026: testnet instructions

For sandbox tests, the guide recommends MetaMask, Polygon Amoy (chain ID `80002`), Circle's Amoy USDC faucet, and POL for gas, while permitting other preferred wallet/network/faucet services. The Amoy USDC contract shown is `0x41E94Eb019C0762f9Bfcf9Fb1E58725BfB0e7582`. It warns that a test refund token can have a different contract from the payment token, so check the refund's transaction hash and token contract. These are testnet setup details and do not establish production network or stablecoin support.

## Related pages

- [[stripe-stablecoin-payments]] — broader stablecoin payments concept, sourced separately for general eligibility and settlement claims
- [[stripe-subscriptions]] — subscription concept
- [[stripe]] — company page

## Related raw API references

- [[raw/stripe-billing-subscriptions-stablecoins-2026-11-07|November 7 variant index]] — navigation only; linked Checkout, Payment Intents, and Setup Intents variant bodies were not read here

## Raw Sources

- [[raw/stripe-subscriptions-stablecoins-2026|May 13 full subscription guide]] — dated three-path examples, event meanings, and sandbox instructions
