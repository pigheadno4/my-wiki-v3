---
title: "Stripe — Crypto Onramp: Embedded Setup Guide"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/crypto/onramp/embedded"
raw_files:
  - "stripe-crypto-onramp-embedded-2026-11-07.md"
  - "stripe-crypto-onramp-embedded-setup-2026.md"
tags: [stripe, crypto, onramp, embedded, fiat-to-crypto, session-states, quotes-api, mobile, webhook]
---

## Overview

The May 11 and November 7, 2026 captures are an extended embedded onramp setup guide for [[stripe]]'s fiat-to-crypto widget, distinct from the simpler quickstart and from the private-preview headless Embedded Components flow in [[stripe-crypto-onramp]]. Both captures describe SDK loading, server-minted sessions, state changes, optional pre-population and appearance, mobile web views, estimated quotes, webhooks, validation and persistence. The guide's regional and preview descriptions do not prove access or a completed payment/delivery for an individual platform.

## Access and integration setup

- Both captures describe embedded onramp as available in the EU and US except Hawaii, with the Onramp API in **public preview** and an application required before development. The May capture says "testing environment"; November says **sandbox**. After access, use Dashboard keys; this is an access prerequisite, not proof of approval.
- Load the onramp scripts directly from Stripe's `js.stripe.com` and `crypto-js.stripe.com` domains; the guide warns against bundling or self-hosting. Its May script example uses `https://js.stripe.com/dahlia/stripe.js`; November's example uses `https://js.stripe.com/endive/stripe.js`. The sample path change alone does not establish a mandatory new API version or runtime compatibility for an account. The package-manager alternative uses `@stripe/stripe-js` and `@stripe/crypto`. Both captures say official server libraries lack built-in support for these public-preview endpoints and show curl examples.
- The server calls `POST /v1/crypto/onramp_sessions` and mints one session per customer. Render the onramp only after successful session creation and provide a fallback for creation errors. The client uses a publishable key and the returned client secret to initialize and mount JavaScript or React UI. See the full raw examples for exact setup code.

## Session and UI behavior

The five documented states are `initialized` (new session), `rejected` (customer rejected), `requires_payment` (onboarding or sign-in complete and payment page reached; a failed payment can leave it there), `fulfillment_processing` (**payment completed but crypto not yet delivered**), and `fulfillment_complete` (**payment succeeded and delivery confirmed**). The mobile flow may return a customer to the app at `fulfillment_processing` while the backend continues to poll; that redirect is not evidence of delivery.

Optional transaction pre-population includes `wallet_addresses`, `lock_wallet_address`, `source_currency` (`usd`/`eur` in the captures), `source_amount` **or** `destination_amount` (mutually exclusive), destination currency/network and allowed arrays. Customer pre-population can include email, name, date of birth and address. SSN cannot be pre-populated; if supplying date of birth, provide year, month and day together. Appearance supports dark mode at creation and updates after render. Sandbox examples use OTP `000000`, SSN `000000000`, address line 1 `address_full_match`, and card `4242424242424242`; the guide says sandbox transaction amounts are overridden by preset limits.

## Quotes, events and errors

`GET /v1/crypto/onramp/quotes` supplies **estimated** conversions by destination currency/network. A fixed source or destination amount can be requested, with currency/network filters; source and destination amounts are mutually exclusive, and a fixed destination amount requires one destination currency and one network. Quotes can change before the customer opens the widget. The November guide explicitly says **by default**, transaction and network fees are added on top of `source_amount`; `source_total_amount` represents the fiat total paid **including fees**. May example responses show fee and total fields but do not state this default rule. Example numbers are not guaranteed pricing.

`crypto.onramp_session.updated` fires on post-creation status changes, **not** initial session creation. Front-end events include `onramp_ui_loaded`, `onramp_session_updated`, and modal-only opened/closed events; `'*'` subscribes to all. Session-creation validation can return customer supportability, unsupported geography, incident/fraud shutdown, invalid source/destination combinations, wallet/network mismatch or merchant setup errors. For example, passing `customer_ip_address` can produce HTTP 400 `crypto_onramp_unsupportable_customer`; an incident can produce `crypto_onramp_disabled`. See the full error table in each raw. Stripe describes itself as merchant of record and says it may restrict session creation during fraud attacks. These examples do not establish whether a particular customer is supportable.

## Mobile and persistence

Both captures discuss hosting the widget in a mobile web view/browser and returning via universal link, with backend status checks. Both also contain this unresolved credential-handling conflict:

> [!warning] Contradiction
> The May and November mobile examples place `client_secret` in a front-end URL path and read it from the URL (May lines 477, 499–520; November lines 510, 529–550). Their own persistence sections say the secret exposes private wallet-address information and must **not** be logged, embedded in URLs, or exposed to anyone other than the customer; any page containing it must use TLS (May line 959; November line 995). This source does not reconcile those instructions or validate an alternative transport. Do not treat its URL-path sample as safe implementation guidance.

OnrampSession is a stateful server-side resource; reusing a previously issued client secret can resume a customer. The captures suggest linking the session to an authenticated Web2 customer or privacy-preserving local storage for an account-less Web3 experience. Either route remains subject to the secret-disclosure and TLS restrictions above.

## Use-case and raw detail locators

- Wallet funding, transaction top-ups, Dapp/NFT checkout and DEX configurations, including wallet and destination restrictions: both raws, final "Configure the onramp by use case" sections. These are examples, not evidence of completed exchanges.
- Access, script channels, server/client scope and one-session-per-customer rule: both raws, "Before you begin", "Install the SDK and client library", and "Create a crypto onramp session".
- State meanings, pre-population and sandbox test values: both raws, "States", "Pre-populate parameters", and "Sandbox values".
- Quote parameter defaults, response fields, sample amounts and fee statement: both raws, "Configure conversion quotes"; default fee statement is in November only.
- Status webhook and front-end event payload examples: both raws, "Listen to webhook events".
- Supportability/fraud conditions and full 16-row additional-validation table: both raws, "Handle customer supportability and fraud".
- Mobile sample versus sensitive-secret prohibition: both raws, "Configure the onramp for mobile use" and "Use session persistence".

## Related

- [[stripe-crypto-onramp]] — onramp modes and reciprocal source route
- [[source-stripe-crypto-onramp-embedded-quickstart]] — simpler widget setup
- [[stripe]] — provider context

## Raw Sources

- [[raw/stripe-crypto-onramp-embedded-2026-11-07|Stripe embedded-onramp extended guide, fetched 2026-11-07]]
- [[raw/stripe-crypto-onramp-embedded-setup-2026|Stripe embedded-onramp extended guide, fetched 2026-05-11]]
