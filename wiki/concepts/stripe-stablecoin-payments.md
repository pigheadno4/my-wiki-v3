---
title: "Stripe Stablecoin Payments"
type: concept
category: technology
tags: [stripe, stablecoins, crypto, usdc, usdp, usdg, connect, billing]
---

## Definition

The May 2026 direct Stripe Crypto overview describes US businesses accepting stablecoins from customers worldwide, subject to applicable restrictions, with USD settlement in their Stripe balance. See Product Support for the November direct Crypto wording and the separate Link path.

## Supported Stablecoins and Networks

| Stablecoin | Networks in the May 2026 direct overview |
| --- | --- |
| USDC | Ethereum, Solana, Polygon, Base |
| USDP | Ethereum, Solana |
| USDG | Ethereum |

## Key Properties

- **Transaction limit**: 10,000 USD per transaction
- **No disputes/chargebacks**: customer must authenticate — low fraud risk
- **Refunds**: always returned as stablecoins to original wallet (not USD)
- **Capture and payout**. The direct product overview lists manual capture as unsupported and payout timing as network-dependent. The dedicated stablecoin API rows mark manual capture supported, and the Wallets API rows mark it unsupported.
- **Billing**. The direct overview lists invoices and subscriptions. The dedicated and Wallets matrices apply separate private-preview, invite-only and product labels. See [[source-stripe-stablecoin-payments]] for the dated rows and their unresolved account and workflow scope.

## Payment Flow

1. Customer selects **Crypto** at checkout
2. Redirected to crypto.stripe.com
3. Connects crypto wallet, selects currency and network
4. Payment confirmed
5. (Optional) Redirected back to merchant site

## Product Support

The direct Stripe Crypto overview covers Checkout, Elements, Invoicing, Payment Links, Billing and Connect, subject to product and account eligibility. November lists USD presentment and other currencies in private preview, and describes settlement to the merchant’s local-currency Stripe balance. Its named business previews and detailed country list, including GI, LI and NO, differ from the May and November cross-method rows that say USD and US businesses. The direct November token table adds USDC on Tempo and qualifies USDP and USDG as US only. See [[source-stripe-stablecoin-payments]] for the dated geographic, currency and product-matrix boundaries.

Stablecoins on Link is a separate funding path for eligible US businesses serving customers in supported countries. It covers one-time, on-session USD payments of 1–10,000 USD via Payment Links, Stripe Checkout or Elements, with USD settlement in the merchant’s Stripe balance on completion. The Link glossary names OUSD and USDC for balances and USDC.e for Tempo transfers. The Link guide supplies no comprehensive checkout token/network list. See [[source-stripe-stablecoins-on-link]].

## Connect

Both direct overviews make each connected account’s enabled method a prerequisite. Accounts with full Stripe Dashboard access, including Standard accounts, can enable the method there. For accounts without full Dashboard access, request `crypto_payments` in the platform Dashboard or through the API.

Check status: `account.capabilities.crypto_payments = 'active'`.

## Sources

- [[source-stripe-stablecoin-payments]] — May and November 2026 direct Crypto overviews with dated eligibility, presentment and settlement, checkout token networks, product-matrix differences, refunds and Connect activation.
- [[source-stripe-stablecoins-on-link]] — separate Link funding path and dated eligibility, wallet selection and USD Stripe-balance settlement
- [[source-stripe-accept-stablecoin-payments]] — dated May 2026 bundled integration guide: Dashboard request/review/approval, default dynamic methods for eligible customers, Checkout, Elements with Checkout Sessions API, Elements with Payment Intents API, Direct API, iOS, Android, and MetaMask + Polygon Amoy test examples. The November 2026 base page indexes those six variants but their current detailed content was not captured; its index alone does not refresh route behavior or account access.
- [[source-stripe-crypto-deposit-mode]] — deposit mode: API-only, direct on-chain deposit addresses, USDC only (Tempo/Base/Solana), exact amount required, access required
- [[source-stripe-subscriptions-stablecoins]] — May 2026 full three-path subscription guide and November 2026 variant-index navigation; USDC is a price example in the Payment Intents path, while Checkout and Setup Intents examples use USD; sandbox instructions do not prove production token/network support
