---
title: "Braintree Payment Method Nonces and Single-Use Payment Methods"
type: source
date_ingested: 2026-09-19
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/payment-method-nonces"
raw_files:
  - "braintree/docs/guides/payment-method-nonces-2026-09-16.md"
tags: [braintree, payment-method-nonce, single-use-payment-method, tokenization, vault]
---

## Overview

This Braintree guide explains the shared role of SDK payment-method nonces and GraphQL single-use payment methods. It is the retrieval entry for their naming, client/server handoff, supported uses, and one-use lifecycle; it does not establish that a transaction or Vault request succeeds.

## Key takeaways

- In Braintree SDK terminology, a payment-method nonce is a secure one-time reference to payment information; the GraphQL API calls the equivalent reference a single-use payment method. The guide uses "single-use token" for both.
- A single-use token can reference any payment method, allowing the merchant server to use a common processing pattern across payment-method types.
- Braintree can generate these tokens in response to merchant client or server requests. Generally, the client sends the token to the merchant server, which returns it to Braintree as an input to a supported action.
- Each token can be used only once. If unused, it expires three hours after creation.

## Uses and lifecycle

The guide identifies two main purposes: creating a transaction through an SDK or the GraphQL API, and creating or updating a Vault payment method for repeat use. Those statements describe where the token is used, not the success state or downstream outcome of either operation.

For exact use routes, see the raw page's **Functionality** section. For the one-use restriction and unused-token expiry, see **Lifespan**. The **Security** section explains how substituting single-use tokens for raw card data reduces exposure and can reduce PCI DSS compliance burden.

## Related

- Company: [[braintree]]
- Concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/payment-method-nonces-2026-09-16|Braintree payment method nonces guide]] - complete guide covering terminology, use, security, and lifespan
