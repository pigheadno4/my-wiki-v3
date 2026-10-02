---
title: "Braintree Tokenization Keys (iOS v7)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/authorization/tokenization-key/ios/v7"
raw_files:
  - "braintree/docs/guides/authorization/tokenization-key/ios/v7-2026-09-16.md"
tags: [braintree, ios-sdk, client-authorization, tokenization-key, payment-method-tokenization]
---

## Overview

This Braintree iOS v7 guide documents tokenization keys as static, reduced-privilege credentials that authorize client-side payment-information tokenization. This is Braintree client-SDK authorization, not Braintree Auth merchant OAuth, transaction authorization, or evidence of payment success.

## Key takeaways

- A tokenization key may be reused indefinitely across client apps. Multiple active keys can be labeled for separate purposes, and revoking a key deauthorizes every client using that key. The page also says an Account Admin role permission may be needed if key use produces an insufficient-privileges error.
- The page lists credit cards, PayPal, Venmo, Apple Pay, and Google Pay as tokenizable with a tokenization key, but the credential authorizes only a subset of client API capabilities. Clients can only tokenize payment information: they cannot supply a customer ID, choose a merchant account ID, provide other configuration, retrieve a customer's saved methods in Drop-in, or create a 3D Secure transaction.
- A tokenization key cannot save a payment method directly from the client into a customer's Vault. The page routes the resulting payment-method nonce to the merchant server for saving, or points to a customer-scoped client token as the alternative.
- Reduced authorization makes tokenization keys publishable in client apps, but each key is bound to one environment. The page warns that a production key always communicates with Braintree's live environment regardless of environment variables or debug modes.
- The initialization section says tokenization keys work with any Android or iOS SDK version, while the same captured page warns that older mobile SDK certificates would fail after March 30, 2026 and directs iOS integrations to version 6.17.0 or later. Preserve that snapshot tension; it does not establish current iOS v7 support or GitHub implementation parity.

## Detail locators

- Client-token comparison, Account Admin qualification, tokenizable methods, indefinite reuse, labeling, and revocation: `# Tokenization Keys`, lines 20-24; `### Static`, lines 27-33.
- Reduced-privilege limits, Vault handoff alternatives, saved-method behavior, and 3D Secure restriction: `### Reduced privilege`, lines 36-45.
- Control Panel retrieval and key generation: `## Obtaining a tokenization key`, lines 48-58.
- Publishability, environment prefixes, and live-environment warning: `## Adding a tokenization key to your app`, lines 61-71.
- SDK compatibility statement and Swift initialization example: `## Initializing the SDK`, lines 74-84.
- Historical mobile-certificate notice and stated traffic-failure consequence: `# Tokenization Keys`, lines 17-18.

## Related

- Company: [[braintree]]
- Concept: [[braintree-ios-sdk]]
- Related source: [[source-braintree-authorization-overview]]

## Raw Sources

- [[raw/braintree/docs/guides/authorization/tokenization-key/ios/v7-2026-09-16|Braintree tokenization-key guide for iOS v7]] - complete captured guide covering credential purpose, reduced privileges, lifecycle, environment binding, setup, certificate warning, and Swift initialization
