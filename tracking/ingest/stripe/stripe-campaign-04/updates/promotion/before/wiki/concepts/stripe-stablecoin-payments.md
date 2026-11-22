---
title: "Stripe Stablecoin Payments"
type: concept
category: technology
tags: [stripe, stablecoins, crypto, usdc, usdp, usdg, connect, billing]
---

## Definition

Stripe Stablecoin Payments let US businesses accept cryptocurrency stablecoins from customers worldwide, settling all payments in USD in the Stripe balance.

**US businesses only** (customers global, excluding sanctioned countries). All payments settle in **USD** regardless of stablecoin.

## Supported Stablecoins and Networks

| Stablecoin | Networks |
| --- | --- |
| USDC | Ethereum, Solana, Polygon, Base |
| USDP | Ethereum, Solana |
| USDG | Ethereum |

## Key Properties

- **Transaction limit**: 10,000 USD per transaction
- **No disputes/chargebacks**: customer must authenticate — low fraud risk
- **Refunds**: always returned as stablecoins to original wallet (not USD)
- **No manual capture**; payout timing varies by network
- **Recurring payments**: supported via Stripe Billing

## Payment Flow

1. Customer selects **Crypto** at checkout
2. Redirected to crypto.stripe.com
3. Connects crypto wallet, selects currency and network
4. Payment confirmed
5. (Optional) Redirected back to merchant site

## Product Support

Checkout, Elements, Invoicing, Payment Links, Billing (invoices + subscriptions), Connect (all charge types).

## Connect

Each connected account needs the `crypto_payments` capability:
- Standard accounts: enable via Dashboard
- Other accounts: request via platform Dashboard or API

Check status: `account.capabilities.crypto_payments = 'active'`.

## Sources

- [[source-stripe-stablecoin-payments]] — primary source: stablecoin types, payment flow, limitations, disputes, refunds, Connect
- [[source-stripe-accept-stablecoin-payments]] — dated May 2026 bundled integration guide: Dashboard request/review/approval, default dynamic methods for eligible customers, Checkout, Elements with Checkout Sessions API, Elements with Payment Intents API, Direct API, iOS, Android, and MetaMask + Polygon Amoy test examples. The November 2026 base page indexes those six variants but their current detailed content was not captured; its index alone does not refresh route behavior or account access.
- [[source-stripe-crypto-deposit-mode]] — deposit mode: API-only, direct on-chain deposit addresses, USDC only (Tempo/Base/Solana), exact amount required, access required
- [[source-stripe-subscriptions-stablecoins]] — May 2026 full three-path subscription guide and November 2026 variant-index navigation; USDC is a price example in the Payment Intents path, while Checkout and Setup Intents examples use USD; sandbox instructions do not prove production token/network support
