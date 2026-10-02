---
title: "Braintree Credit Cards: Server-Side Implementation (Node.js)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/credit-cards/server-side/node"
raw_files:
  - "braintree/docs/guides/credit-cards/server-side/node-2026-09-16.md"
tags: [braintree, node-js, credit-cards, transactions, card-verification, vault]
---

## Overview

This [[braintree]] website-guide snapshot, collected 2026-09-16 and routed to Node.js, documents server-side credit-card transaction creation and card verification. The server receives a payment-method nonce from the client, supplies the transaction amount and can request immediate settlement submission; the page separately covers verification before storing or updating a card in the Vault. The captured body does not identify an exact Node SDK package version.

## Key takeaways

- The page calls `Transaction:Sale` the simplest credit-card transaction route. Its example combines a server-supplied amount with a client-relayed payment-method nonce and sets `submitForSettlement: true`; it also directs the integration to collect device data on the client and include it in the transaction. These are documented callback and Promise examples, not proof of authorization, settlement or funding.
- The successful-transaction Vault option can create a new customer when no `customer_id` is included. Use the exact request reference linked from the raw page for field behavior rather than generalizing the example.
- Card verification checks whether credit- or debit-card data matches a valid, open account before Vault storage or update. Braintree strongly recommends verification before cards are stored; the documented gateway check uses a $0 or $1 authorization and automatically voids it, unless a different verification amount is specified. An authorization and automatic void can still be consequential and are distinct from a purchase.
- When Premium Fraud Management Tools are used, the page strongly recommends sending device data for every verification. Successful verification is returned within the payment-method response, while the page routes unsuccessful `processor_declined` or `gateway_rejected` verification results and their reason fields separately.
- The collected guide says Braintree Marketplace verifications cannot use sub-merchant accounts. This is a scope limitation in the snapshot, not evidence of current Marketplace availability or merchant eligibility.

## Evidence limitations

> [!warning] Snapshot, version and execution boundaries
> This retained webpage is Node.js-routed but does not state an exact SDK package version. Its examples do not establish current SDK support, merchant configuration, card eligibility, successful authorization, settlement, funding or a completed payment. Client collection of a nonce or device data and server-side use of those values are separate responsibilities.

## Detail locators

- GraphQL alternative navigation: `# Server-Side Implementation`, lines 17-18.
- Sale purpose, amount plus client-relayed nonce, device-data direction and callback/Promise examples: `## Creating transactions`, lines 21-64.
- Successful-transaction Vault option and new-customer side effect when no customer ID is included: `## Creating transactions`, line 65.
- Verification purpose, default enablement guidance, one-time request routes, $0/$1 authorization with automatic void and custom amount: `## Card verification`, lines 66-86.
- Callback and Promise verification examples: `## Card verification`, lines 87-113.
- Premium Fraud Management Tools device-data recommendation: `## Card verification`, lines 115-116.
- Successful and unsuccessful result placement, decline/rejection statuses and reason-field routes: `### Verification results`, lines 119-185.
- Marketplace sub-merchant-account restriction: `### Verifications on sub-merchant accounts`, lines 187-189.
- Transaction, customer, payment-method, verification and Hosted Fields navigation: `## See Also`, lines 190-197.

## Related

- Company: [[braintree]]
- Concepts: [[braintree-server-sdk]], [[braintree-payment-methods]]
- Client-side responsibility route: [[source-braintree-credit-cards-overview]]
- Transaction lifecycle context: [[source-braintree-transaction-lifecycle]]

## Related raw API references

- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Transaction Sale request for Node.js]] - unread navigation-only request reference
- [[raw/braintree/docs/reference/request/payment-method/create/node-2026-09-16|Payment Method Create request for Node.js]] - unread navigation-only verification and Vault reference
- [[raw/braintree/docs/reference/response/credit-card-verification/node-2026-09-16|Credit Card Verification response for Node.js]] - unread navigation-only status and reason-field reference
- [[raw/braintree/docs/guides/premium-fraud-management-tools/server-side/node-2026-09-16|Premium Fraud Management Tools server-side guide for Node.js]] - unread navigation-only device-data reference
- [[raw/braintree/docs/guides/braintree-marketplace/create/node-2026-09-16|Braintree Marketplace create guide for Node.js]] - unread navigation-only Marketplace verification reference

## Raw Sources

- [[raw/braintree/docs/guides/credit-cards/server-side/node-2026-09-16|Braintree Node.js server-side credit-card implementation]] - fully read pinned website snapshot covering transaction creation, Vault storage and card verification
