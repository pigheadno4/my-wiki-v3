---
title: "Braintree SEPA Direct Debit Vaulting (Node.js Route)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/sepa-direct-debit/vaulting/node"
raw_files:
  - "braintree/docs/guides/sepa-direct-debit/vaulting/node-2026-09-16.md"
tags: [braintree, sepa, direct-debit, vault, node-js, payment-methods]
---

## Overview

This 2026-09-16 Braintree website snapshot is a Node.js-routed server guide to storing a customer's SEPA Direct Debit authorization as a Vault payment method, retrieving that method, using its token in a later sale, and deleting it. The page does not name an exact server SDK package or version or distinguish Sandbox from Production, so its gateway examples are historical webpage evidence rather than current environment, merchant-enablement, or successful-payment evidence.

## Key takeaways

- A Vault payment method belongs to a customer and represents transactable information such as authorization to charge a SEPA Direct Debit account. The page says its token can be stored by the merchant server with reduced PCI compliance burden and later supplied to create transactions.
- For an existing customer, the documented create action accepts that customer's ID and a payment-method nonce received from the client. The page also routes an alternative that creates a new customer and payment method together from a nonce.
- After successful creation, the documented next action is a Transaction Sale using the payment-method token. Creation and token storage do not by themselves establish that a later transaction succeeds.
- The find action looks up a payment method by token, returns a PaymentMethod response object, and also returns a link to the associated mandate. A missing method produces the page's linked not-found error route.
- Deleting a payment method by token also revokes its associated mandate. This is a consequential server-side lifecycle action; the page does not document restoration or a replacement mandate in this snapshot.

## Material warning

> [!warning] Deletion also revokes the mandate
> The page explicitly couples payment-method deletion to revocation of the customer's associated mandate. Treat the operation as more than removal of a stored token.

## Detail locators

- Vault payment-method identity, customer ownership, token storage and later transaction use: `# Vaulting`, raw line 16.
- Existing-customer creation from a client nonce, callback and Promise examples, and the new-customer alternative: `## Create`, raw lines 17-45.
- Post-create Transaction Sale route using the payment-method token: `## Create`, raw lines 47-50.
- Token lookup, callback and Promise examples, missing-method behavior, response-object route and associated-mandate link: `## Find`, raw lines 51-82.
- Token deletion, callback and Promise examples, missing-method behavior and mandate revocation: `## Delete`, raw lines 85-118.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Server integration concept: [[braintree-server-sdk]]
- SEPA mandate and lifecycle overview: [[source-braintree-docs-guides-sepa-direct-debit-overview]]
- Client nonce route: [[source-braintree-docs-guides-sepa-direct-debit-client-side-javascript-v3]]
- Testing and environment transition route: [[source-braintree-docs-guides-sepa-direct-debit-testing-go-live-node]]

## Raw Sources

- [[raw/braintree/docs/guides/sepa-direct-debit/vaulting/node-2026-09-16|Braintree SEPA Direct Debit vaulting guide (Node.js route)]] - complete collected page covering Vault payment-method creation, token-based transaction use, lookup and mandate-coupled deletion
