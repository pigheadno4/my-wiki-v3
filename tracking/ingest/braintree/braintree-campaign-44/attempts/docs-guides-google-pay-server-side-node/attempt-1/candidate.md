---
title: "Braintree Google Pay Server-Side Implementation (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/google-pay/server-side/node"
raw_files:
  - "braintree/docs/guides/google-pay/server-side/node-2026-09-16.md"
tags: [braintree, google-pay, server-side, node-js, digital-wallets]
---

## Overview

This Braintree Google Pay server-side guide is a Node.js-routed webpage for turning a client-produced Google Pay card nonce into a server transaction request. It also records the gateway's legacy `AndroidPayCard` representation and separates conditionally supported Google Pay card storage from unsupported vaulting of PayPal accounts returned through Google Pay.

## Key takeaways

- The page says Google Pay is available with Braintree's latest Android and JavaScript SDKs, then instructs the merchant to send the Google Pay card nonce and collected device data from the client to the server.
- Callback and Promise examples call `gateway.transaction.sale()` with an amount, `paymentMethodNonce`, `deviceData`, a billing postal code and `submitForSettlement: true`.
- Braintree says Google Pay cards remain represented as Android Pay cards in its API to avoid breaking changes; the example consequence is an `AndroidPayCard` response object from Payment Method Create.
- Google Pay cards may be saved in the Vault only for specific use cases. The page separately says PayPal accounts from Google Pay cannot be vaulted, so transaction options `store_in_vault` and `store_in_vault_on_success` are unsupported for that case.
- The page links to a separate GraphQL implementation, while this entry retains the Node.js-routed server SDK family path.

## Detail locators

- GraphQL alternative and SDK-family availability statement: `# Server-Side Implementation`, lines 17-22.
- Client nonce/device-data handoff instruction: `## Creating transactions > ### Using card nonces`, line 30.
- Callback and Promise `gateway.transaction.sale()` examples: lines 31-67.
- Legacy `AndroidPayCard` API representation note: lines 69-70.
- Google Pay card and PayPal-account Vault conditions, plus listed card-storage routes: `## Vaulting Google Pay`, lines 73-84.

## Scope and evidence boundary

This is a 2026-09-16 snapshot of an unversioned Braintree website route selected for Node.js server-side documentation. It covers Braintree Google Pay client-to-server handoff and illustrative sale/Vault paths, not a direct PayPal Orders or Google API integration; the opening nonce instruction is rendering-damaged, no exact Node package or runtime is identified, and the page does not establish current merchant enablement, environment behavior, or a transaction, settlement, funding or Vault outcome.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]

## Raw Sources

- [[raw/braintree/docs/guides/google-pay/server-side/node-2026-09-16|Braintree Google Pay Server-Side Implementation - Node.js]] - complete collected webpage for nonce-based sale examples, legacy response naming and Vault qualifications
