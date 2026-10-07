---
title: "Braintree Elo Server-Side Implementation (Node.js Route)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/elo/server-side/node"
raw_files:
  - "braintree/docs/guides/elo/server-side/node-2026-09-16.md"
tags: [braintree, elo, nodejs, server-side, transactions]
---

## Overview

This 2026-09-16 snapshot is an unversioned [[braintree|Braintree]] Elo server-side guide on the Node.js route. It describes sending a client-tokenized payment method nonce to the merchant server, then creating a transaction with client-collected device data. At capture, the page described Elo as a limited release for select merchants using what it calls the latest JavaScript v3 and server SDKs and directed merchants to request access.

## Key takeaways

- The documented handoff begins after the client successfully tokenizes the customer's payment information: the client-provided nonce is passed to the server for transaction creation, with client-collected device data included in the request.
- The callback and Promise examples both call `gateway.transaction.sale`, pass an illustrative `10.00` amount, nonce and device data, and set `submitForSettlement: true`; see the raw locators for the exact examples and result branches.

> [!warning] Snapshot and implementation boundary
> The page-relative word "latest" does not identify an exact Node.js server SDK package or version. This website snapshot does not establish current Elo support, merchant or environment enablement, exact GitHub SDK implementation or history, or a successful transaction or settlement outcome.

## Detail locators

- Limited-release merchant, JavaScript v3/server-SDK and access-request conditions — `AVAILABILITY`, raw line 18.
- Nonce-to-server transaction handoff and client device-data instruction — `Creating transactions`, raw line 23.
- Callback-form `gateway.transaction.sale` example — `Callbacks`, raw lines 24–40.
- Promise-form `gateway.transaction.sale` example — `Promises`, raw lines 42–58.

## Related

- [[braintree]] — provider context and website-versus-versioned-repository evidence boundary
- [[braintree-payment-methods]] — provider payment-method eligibility and Elo retrieval route
- [[source-braintree-docs-guides-elo-client-side-javascript-v3]] — captured Elo JavaScript v3 client-side route
- [[source-braintree-docs-guides-elo-testing]] — captured Elo Sandbox fixture route

## Raw Sources

- [[raw/braintree/docs/guides/elo/server-side/node-2026-09-16|Braintree Elo server-side Node.js route (2026-09-16 snapshot)]]
