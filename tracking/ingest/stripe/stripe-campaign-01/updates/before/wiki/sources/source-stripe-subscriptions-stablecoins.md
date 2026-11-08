---
title: "Stripe Subscriptions — Set Up Stablecoin Payment Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-stablecoins-2026.md"
tags: [stripe, billing, subscriptions, stablecoins, crypto, usdc, web3, checkout, setup-intents, payment-intents]
---

## Summary

Integration guide for stablecoin subscriptions. Three integration paths: Checkout (simplest), Payment Intents API, SetupIntents API. PM type: `crypto`. Supports USDC and other stablecoins. Testnet testing with MetaMask + Polygon Amoy.

## Three integration paths

### Path 1: Checkout

```js
stripe.checkout.sessions.create({
  payment_method_types: ['crypto'],
  line_items: [{ price: priceId, quantity: 1 }],
  mode: 'subscription',
  success_url: '...'
})
```

Key events: `checkout.session.completed` → wait; `invoice.paid` → fulfill; `invoice.payment_failed` → retry.

### Path 2: Payment Intents API

1. Create subscription: `default_incomplete` + `payment_method_types=['crypto']` + `save_default_payment_method='on_subscription'`
2. Confirm PaymentIntent: `payment_method_data.type='crypto'` + `mandate_data` + `return_url`
3. Response `requires_action` → redirect to `next_action.redirect_to_url.url` → customer connects wallet and pays
4. Listen for `payment_intent.succeeded`

Note: Supports USDC as native price currency (not just USD fiat).

### Path 3: SetupIntents API

1. SetupIntent: `payment_method_types=['crypto']`, `confirm=true`, `usage=off_session`, `mandate_data`, `return_url`
2. Redirect to `next_action.redirect_to_url.url` → customer connects wallet
3. After auth: create subscription with `payment_method` from SetupIntent + `off_session=true`

## Testnet testing

- Wallet: MetaMask
- Network: Polygon Amoy (Chain ID: 80002)
- USDC contract: `0x41E94Eb019C0762f9Bfcf9Fb1E58725BfB0e7582`
- USDC faucet: faucet.circle.com → Polygon PoS Amoy
- POL (gas) faucet: faucet.polygon.technology

Additional faucets: Paxos USDP, Devnet SOL, Sepolia ETH, Amoy POL.

## Related pages

- [[stripe-stablecoin-payments]] — concept page (updated with subscription facts)
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-stablecoins-2026]] — verbatim Stripe docs webpage (640 lines, 1 image reused)
