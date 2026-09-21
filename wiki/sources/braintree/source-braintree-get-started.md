---
title: "Braintree Get Started: Direct Integration Overview"
type: source
date_ingested: 2026-09-19
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/start/overview"
raw_files:
  - "braintree/docs/start/overview-2026-09-16.md"
tags: [braintree, braintree-direct, drop-in, client-sdk, server-sdk, payment-method-nonce]
---

## Overview

This Braintree guide introduces a basic Braintree Direct integration that accepts sandbox credit-card payments through Drop-in UI. Its retrieval value is the client/server responsibility split and the client-token-to-payment-method-nonce flow, together with a dated warning to migrate away from Drop-in.

## Key takeaways

- Braintree Direct is described as a toolkit for processing cards, PayPal, Apple Pay, Google Pay, and US-only Venmo, with fraud-prevention, data-security, and operational tooling. Actual merchant, buyer, platform, and regional availability still requires the relevant product documentation.
- The client SDK collects payment information; the server SDK acts on the resulting payment information. In this guide, the server generates a client token for client-SDK initialization.
- The customer submits payment information through the client integration, Braintree returns a payment-method nonce, the front end sends that nonce to the merchant server, and the server SDK uses it to create a transaction.
- The page says Drop-in becomes deprecated on October 1, 2026, remains supported for payment processing until October 1, 2027, and becomes unsupported on that date, after which processing may be suspended at any time. It directs merchants to migrate to the Braintree Android, iOS, or JavaScript SDK.

## Integration flow

1. The front end requests a client token, and the merchant server generates it with a server SDK.
2. The client SDK sends the customer's payment information to Braintree and receives a payment-method nonce.
3. The front end sends the nonce to the merchant server, where the server SDK creates a transaction.

The raw guide's `What you will need` and `How it works` sections provide the platform/language list, authorization route, checkout-UI alternatives, and exact five-step sequence. The statement that the server creates a transaction does not by itself define amount sourcing, authorization versus settlement behavior, success criteria, errors, or fulfillment policy; use the dedicated server SDK and transaction references for those details.

> [!warning] Conflicting Drop-in lifecycle dates
> This website snapshot gives October 1 dates. The retained `braintree-web-drop-in@1.47.0` and `1.48.0` GitHub sources give September 1, 2026 and September 1, 2027 for the corresponding lifecycle milestones. The September 10 `1.48.0` release also follows its unchanged no-updates date. Treat each schedule as source-specific evidence and verify current official status before migration planning. [[source-github-braintree-web-drop-in]]

## Related

- Company: [[braintree]]
- Concepts: [[braintree-web-drop-in]], [[braintree-server-sdk]], [[braintree-web-sdk]]
- Related source: [[source-github-braintree-web-drop-in]]

## Raw Sources

- [[raw/braintree/docs/start/overview-2026-09-16|Braintree Get Started overview]] - complete guide, client/server flow, and Drop-in lifecycle notice
