---
title: "Stripe — Crypto Onramp: Stripe-Hosted Integration"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/crypto/onramp/stripe-hosted"
raw_files:
  - "stripe-crypto-onramp-stripe-hosted-2026-11-07.md"
  - "stripe-crypto-onramp-stripe-hosted-2026.md"
tags: [stripe, crypto, onramp, fiat-to-crypto, redirect, session-api, pci]
---

## Overview

The May 11 and November 7, 2026 captures describe the Stripe-hosted standalone crypto onramp at `crypto.link.com`: platforms redirect users there through either a frontend-generated URL or a backend-created onramp session with a redirect URL. The November example changes the Stripe.js script path from Dahlia to Endive. That example change does not establish a mandatory SDK upgrade, removal of the older script path, account access, or a completed crypto purchase. See [[stripe-crypto-onramp]].

## Access before integration

Both dated guides say accessing the onramp, including a sandbox, requires creating or signing in to a Stripe account, setting it up, submitting an onramp application, and waiting for approval before development in a sandbox. Stripe says it reviews **most** applications within 48 hours; this is not a guaranteed review time. The frontend URL-generation option below is described as needing no Stripe account for that code path. It does not waive the separate onramp application and approval gate or demonstrate that an unapproved URL can complete a transaction. The captures do not establish any particular account's approval.

## Two customization paths

| Path | Where and scope | Use in the captured guide |
| --- | --- | --- |
| Generate redirect URL | Frontend; no Stripe account needed to generate the URL | Lightweight prefill of suggested source or destination amount, destination currency, and network; no branding |
| Mint session with redirect URL | Backend with Stripe account | Full customization including destination wallet address and branding; create a new onramp session for every user visit |

**Frontend script loading:** Both captures instruct direct script tags from `js.stripe.com` and `crypto-js.stripe.com` for compatibility and PCI compliance; do not bundle or self-host them because the integration might break without warning. The May HTML example uses `https://js.stripe.com/dahlia/stripe.js`; the November HTML example uses `https://js.stripe.com/endive/stripe.js`. Both examples retain `https://crypto-js.stripe.com/crypto-onramp-outer.js`. These are dated example paths, not a tested compatibility matrix.

**Frontend API example:** `window.StripeOnramp.Standalone({...}).getUrl()` generates the redirect URL. The guide's prefill fields include `source_currency` (shown as `usd` or `eur`), one `amount.source_amount` **or** `amount.destination_amount`, destination currencies/networks restrictions, and default destination currency/network. Only one amount may be specified. A generated URL is not evidence of an approved onramp account or successful payment.

**Backend API:** The guide instructs creating a new `POST /v1/crypto/onramp_sessions` request per user visit and redirecting to the returned `redirect_url`. Its sample response also shows `client_secret`, `transaction_details`, and `status: initialized`. That sample shows a newly initialized session, not checkout completion, crypto delivery, or settlement.

## Captured currencies and geography

Both guides list ETH (Ethereum/Base), SOL, POL, MATIC, BTC, AVAX, XLM and USDC (Ethereum, Solana, Polygon, Avalanche, Base and Stellar) for the US/EU context, expressly saying available currencies are **subject to change**. They say XLM and USDC on Stellar, Avalanche or Polygon are unavailable in New York; ETH on Base, MATIC, AVAX, and USDC on Solana, Polygon, Avalanche or Base are unsupported in the EU. These are dated documentation snapshots and do not prove current regional, asset, or account eligibility.

## Detail locators

- [[raw/stripe-crypto-onramp-stripe-hosted-2026-11-07|November 7, 2026 capture]]: application and sandbox access lines 11–18; currencies and exclusions lines 26–45; path comparison lines 47–54; script loading/examples lines 56–80; prefill fields lines 82–89; backend session/sample response lines 93–142.
- [[raw/stripe-crypto-onramp-stripe-hosted-2026|May 11, 2026 capture]]: corresponding access lines 10–17, currency/geography lines 25–44, frontend/backend paths and Dahlia example lines 46–94, sample response lines 103–135.

## Related

- [[stripe]]; [[stripe-crypto-onramp]]; [[source-stripe-crypto-onramp]]

## Raw Sources

- [[raw/stripe-crypto-onramp-stripe-hosted-2026-11-07|November 7, 2026 Stripe-hosted guide]]
- [[raw/stripe-crypto-onramp-stripe-hosted-2026|May 11, 2026 Stripe-hosted guide]]
