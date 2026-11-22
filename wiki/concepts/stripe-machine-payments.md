---
title: "Stripe Machine Payments"
type: concept
category: technology
tags: [stripe, machine-payments, mpp, x402, agentic-commerce, usdc, stablecoin, frontier, base, solana]
---

## Overview

Stripe Machine Payments ("Frontier") enables **machine-to-machine payments** — AI agents pay for API calls and services programmatically using crypto (USDC) or Stripe card networks. Payments settle in fiat directly into the seller's Stripe balance.

## Two Roles

**Sellers**: charge for API resources or services. The November MPP guide lists minimums by rail.

**Agents**: the stablecoin rail uses a wallet, while the SPT rail uses a Shared Payment Token credential. The November MPP guide's manual SPT test uses a Link account and Link CLI for a one-time test token. See [[source-stripe-machine-payments-mpp-quickstart]].

## Supported Networks and Protocols

| Network | Protocol | Currency |
| --- | --- | --- |
| Base | x402 | USDC |
| Solana | MPP | USDC |
| Tempo | MPP | USDC.e in the November 2026 guide |
| Stripe card networks | MPP | Stripe currencies |

**MPP** (Machine Payments Protocol): multi-network; covers Solana, Tempo, and Stripe card networks.

**x402**: The November 2026 guide uses Base mainnet (`eip155:8453`), USDC, an authenticated CDP facilitator and an upfront Stripe address resource as static `payTo`. It records the settled transaction on a `transaction_verification` PaymentIntent. Its separate sandbox uses Base Sepolia (`eip155:84532`) and the public x402 facilitator. Live `purl` testing moves real funds. The May Hono quickstart used a dynamic deposit-mode Intent and cache-validated retry addresses. See [[source-stripe-machine-payments-x402-quickstart]].

**USDC contract addresses for November 2026 crypto PaymentIntent `transaction_verification`:** The May same-URL historical guide lists the same addresses for `deposit` mode. The November Machine Payments protocol table labels Tempo MPP as USDC.e and routes Base USDC to x402. A separate `2026-10-28.endive` Tempo deposit-address creation example shows `livemode: false` and `token_currency: usdc` with contract `0x20c0000000000000000000009e8d7eb59b783726`. These scoped examples leave interoperability and migration unverified. See [[source-stripe-machine-payments-x402-quickstart]].

| Network | Contract |
| --- | --- |
| Tempo | `0x20c000000000000000000000b9537d11c60e8b50` |
| Base | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` |
| Solana | `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |

## Key Features

- **Minimums in the November MPP guide**: 0.50 USD for card SPTs and 0.01 USDC for stablecoins.
- **Fiat settlement**: Stripe describes off-ramping supported stablecoin payments into Stripe balance. The May overview describes standard reporting and multicurrency payouts.
- **Deposit addresses and privacy**: The May overview describes a unique address per payment and reduced on-chain visibility for its deposit flow. The May MPP example creates a Tempo address with a deposit-mode PaymentIntent. The November MPP handler uses a separately provisioned or fetched account-level Tempo address, and the November x402 walkthrough uses a precreated static Base recipient. See [[source-stripe-machine-payments-mpp-quickstart]] and [[source-stripe-machine-payments-x402-quickstart]].
- **Refunds**: The May overview describes returning stablecoin refunds to the sender wallet.
- **Eligibility**: The May overview describes nationwide SPT card and wallet acceptance for developers with a US legal entity and excludes New York and Texas for stablecoins. The May x402 webpage describes US-only stablecoin acceptance. The November overview routes non-US SPT businesses to supported-country guidance. The November x402 guide and Machine Payments overview describe US stablecoin availability except New York and an access-request route covering 30+ countries outside the US. Access is subject to eligibility and Stripe approval.

## MPP Implementation (`mppx` library)

HTTP 402 middleware pattern: `Mppx.create({ methods, secretKey })` → `mppx.charge({ amount, currency })(request)` → return `result.challenge` (402) or `result.withReceipt(content)`.

**May 2026 examples**: The Hono quickstart derives and caches a Tempo recipient from a crypto deposit-mode PaymentIntent and uses the dated `2026-03-04.preview` client. It has a separate SPT handler. The separate May integration guide uses `simulate_crypto_deposit` for its sandbox deposit-mode PaymentIntents and uses `profile_test_` or `profile_` for sandbox or live SPT examples.

**November 2026 example**: `stripe.create` takes the merchant's Stripe profile ID as `networkId` and its default handler supports SPT. `defaultMethods()` adds Tempo when supplied with a separately managed deposit address. Use a sandbox key and profile for test validation, with a sandbox Tempo address for the Tempo path. Hosted Tempo fee sponsorship is live-only, uses `mppx` 0.9.2 or later and a deposit address from the API key's account, and excludes Connect. The November product overview's general Connect support has broader scope.

**Agent-side testing**: The November guide's manual examples use Link CLI for a one-time test SPT and a Tempo wallet for the stablecoin rail. At `@stripe/link-cli@0.13.0`, `link-cli mpp pay` can run the Stripe HTTP `402` flow from challenge parsing through approval, SPT retrieval, credential signing, and request retry. Live validation can use real funds. See [[source-stripe-machine-payments-mpp-quickstart]] for setup and testing scope.

## Relationship to Other Products

- [[stripe-agentic-commerce]] — broader agent commerce context (ACS, RequestedSession, OCA)
- [[stripe-stablecoin-payments]] — stablecoin payment acceptance on Stripe

## Sources

- [[source-stripe-machine-payments]] — overview: seller/agent use cases, networks, protocols, geo restrictions
- [[source-stripe-machine-payments-mpp]] — MPP implementation: mppx library, crypto + SPT payment flows, PaymentIntent, testing with link-cli
- [[source-stripe-machine-payments-mpp-quickstart]] — May 2026 structured Hono quickstart and November 2026 MPP guide with a Stripe profile, default SPTs, configured Tempo addresses, fee sponsorship limits and sandbox/live testing.
- [[source-stripe-machine-payments-x402-quickstart]] — November x402 full guide for static Base USDC receipt, transaction-verification recording and live/sandbox testing, alongside the May dynamic deposit-mode quickstart. Distinguishes Tempo verification-table and non-live deposit-address examples.
- [[source-stripe-machine-payments-x402]] — May 2026 x402 webpage on deposit-mode capture, simulator testing, token contracts and CDP mainnet. For the separate November Base Sepolia public-facilitator test and transaction verification, see [[source-stripe-machine-payments-x402-quickstart]].
- [[source-github-link-cli]] — Link CLI `0.13.0` implementation of the Stripe MPP agent payment flow
