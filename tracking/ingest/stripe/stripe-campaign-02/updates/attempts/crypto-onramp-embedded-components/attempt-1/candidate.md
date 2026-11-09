---
title: "Stripe — Crypto Onramp: Embedded Components Hub and Historical Headless Quickstart"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/crypto/onramp/embedded-components"
raw_files:
  - "stripe-crypto-onramp-embedded-components-2026.md"
tags: [stripe, crypto, onramp, embedded-components, headless, link-auth, oauth, mobile, react-native, private-preview]
---

## Overview

This exact URL was a full Embedded Components headless onramp quickstart in the May 11, 2026 capture. The November 7, 2026 capture is instead a navigation hub for an onramp flow native to an app or website, with a distinct [quickstart](https://docs.stripe.com/crypto/onramp/embedded-components-quickstart.md) URL and separate overview, platform integration, KYC, EU KYC, and error-handling routes. A reader seeking the current quickstart should follow that separate route and verify its current contents. The November hub does not restate the May walkthrough or establish that its API calls were removed, that preview status changed, or that any country or account is eligible.

## May 2026 headless quickstart

The retained May guide describes a Link OAuth and custom UI flow, with web `@stripe/crypto`, React Native `@stripe/stripe-react-native`, and linked iOS/Android sample apps. Its code is an illustrative Node server and React client, not an executed onramp transaction or a current SDK contract. The separate May [[source-stripe-crypto-onramp-embedded-components-integration|integration guide]] described Embedded Components as private preview, US only excluding New York, and requiring completed onboarding even in sandbox; those are historical qualifications, not November-verified access rules.

### Server flow in the May guide

1. The May guide requires backend Stripe API requests to carry `Stripe-Version: 2026-03-25.dahlia;crypto_onramp_beta=v2`. Its server creates a `LinkAuthIntent` and, after client consent, exchanges it for an OAuth access token. Store that token on the backend and send it in `Stripe-OAuth-Token` on subsequent crypto API calls; do not expose it to the client. Refresh expired access tokens with the Link token endpoint and client credentials.
2. Retrieve the CryptoCustomer to inspect KYC and verification status; list ConsumerWallets and PaymentTokens to decide whether wallet registration or payment-method collection is needed. These checks and setup steps are gates in the dated guide, not proof that a particular customer passes them.
3. Create a `CryptoOnrampSession` with `ui_mode: headless`, the authorized `crypto_customer_id`, a `payment_token`, amount, currencies, network, and wallet address. Refresh an executable quote before expiry: the guide warns checkout with an expired quote returns HTTP 400.
4. The backend calls the checkout API and returns `client_secret` for the client SDK to handle any required step such as 3DS. A created session, returned secret, or UI completion step does not by itself prove authorization, crypto delivery, or settlement.

### Client flow in the May guide

The narrated client sequence is Link authentication, conditional KYC and identity verification, wallet registration, payment-method collection, then checkout. It calls `authenticate()` with a server-created auth intent and keeps the resulting `crypto_customer_id` on the backend. It rechecks customer status after `submitKycInfo()` or `verifyDocuments()`, registers a wallet with `registerWalletAddress()`, and uses `collectPaymentMethod()` if no stored payment token is available. The example calls `performCheckout(sessionId, fetchClientSecret)` and refreshes an expired quote. The React sample's final “Transaction complete” UI text is sample state, not independently verified payment or delivery.

## Detail locators

- [[raw/stripe-crypto-onramp-embedded-components-2026|May 11, 2026 full quickstart]]: overview and version header lines 6–28; server OAuth, setup, session, quote and checkout narration lines 30–64; client sequence lines 76–96; Node/React examples lines 103–526.
- The May [[source-stripe-crypto-onramp-embedded-components-integration|integration source]] and its May raw lines 14–24 provide the dated private-preview and US-excluding-New-York context. The November hub does not update those claims.

## Related

- [[stripe]]; [[stripe-crypto-onramp]]; [[source-stripe-crypto-onramp-embedded-setup]]

## Related raw API references

The [[raw/stripe-crypto-onramp-embedded-components-2026-11-07|November 7, 2026 same-URL hub]] is navigation only. The linked pages below were not reviewed as factual evidence in this update:

- [Embedded Components overview](https://docs.stripe.com/crypto/onramp/embedded-components-overview.md)
- [Embedded Components quickstart](https://docs.stripe.com/crypto/onramp/embedded-components-quickstart.md)
- [Platform integration guide: Web, React Native, Android, iOS](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md)
- [KYC integration guide](https://docs.stripe.com/crypto/onramp/kyc-integration-guide.md)
- [EU KYC integration guide](https://docs.stripe.com/crypto/onramp/eu-kyc-integration-guide.md) — a content route, not evidence of EU eligibility
- [Error handling guide](https://docs.stripe.com/crypto/onramp/embedded-components-error-handling-guide.md)

## Raw Sources

- [[raw/stripe-crypto-onramp-embedded-components-2026|May 11, 2026 headless quickstart]]
