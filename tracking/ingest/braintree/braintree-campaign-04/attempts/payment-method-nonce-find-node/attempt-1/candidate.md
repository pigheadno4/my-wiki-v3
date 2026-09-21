---
title: "Braintree Payment Method Nonce Find (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/payment-method-nonce/find/node"
raw_files:
  - "braintree/docs/reference/request/payment-method-nonce/find/node-2026-09-16.md"
tags: [braintree, node-js, payment-method-nonce, 3d-secure, risk-checking]
---

## Overview

This Braintree Node.js reference documents `gateway.paymentMethodNonce.find()` for retrieving information about an existing payment-method nonce. Unlike an operation that uses the nonce for a transaction or Vault action, this lookup does not consume it; the returned nonce and available 3D Secure information can support server-side risk checking before transaction creation.

## Key takeaways

- The page provides callback and Promise forms of `gateway.paymentMethodNonce.find("nonce_string")`.
- A find call does not consume the payment-method nonce. It returns the nonce string with available 3D Secure information, including liability-shift indicators, for server-side risk checking before a transaction is created. This lookup is not documented as creating, authorizing, or guaranteeing a successful payment.
- `threeDSecureInfo` may be absent when 3D Secure information was not captured with the nonce.
- When the nonce cannot be found, the page routes the failure to Braintree's Node.js `notFoundError` reference.

## Detail locators

- Lookup purpose: `# Payment Method Nonce: Find`, lines 15-17.
- Non-consuming behavior, returned 3D Secure fields, and server-side risk-check scope: `# Payment Method Nonce: Find`, line 19.
- Callback and Promise examples, including the absent-3D-Secure-information branch: `### Callback`, lines 20-32, and `### Promise`, lines 35-47.
- Missing-nonce failure route: immediately after the Promise example, line 49.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Related concept: [[braintree-web-sdk]]
- Related source: [[source-braintree-payment-method-nonces]]

## Raw Sources

- [[raw/braintree/docs/reference/request/payment-method-nonce/find/node-2026-09-16|Braintree Node.js payment-method nonce find reference]] - complete page covering lookup, non-consumption, returned 3D Secure information, and the missing-nonce route
