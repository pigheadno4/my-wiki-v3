---
title: "Braintree GraphQL Payment API Concepts"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/guides/concepts"
raw_files:
  - "braintree/graphql/guides/concepts-2026-09-16.md"
tags: [braintree, graphql, payment-methods, vault, transactions, customers]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide gives conceptual context for the main Braintree GraphQL Payment API types and their behavior: payment methods, the Vault, transactions and customers. It also sketches a typical client-token and client-SDK flow that returns a single-use payment-method ID to the merchant server for GraphQL vaulting or charging. It is an orientation document, not a complete or exact GraphQL schema, a language-SDK implementation, proof of merchant or payment-method eligibility, or evidence that any request, transaction, settlement or funding succeeded.

## Key takeaways

- The guide's typical flow separates client and server responsibilities: the server issues a client token, the client SDK collects payment information and returns a single-use payment method, and the client passes that method's ID (called a nonce by client code) to the server. The server may then use GraphQL to vault or charge it. This is a conceptual sequence, not a guarantee that every product or integration uses the same SDK path.
- `PaymentMethod` is the guide's umbrella object for something a customer can use to pay, including cards, wallets, PayPal, Venmo and bank accounts. The listed detail-object types and fields are illustrative routes; use the API Explorer or retained exact-schema source for complete field and type definitions.
- A newly collected method is single-use and expires three hours after creation or after one use. The guide says vaulting consumes that method, stores the underlying payment information and creates a multi-use method. It characterizes multi-use methods as non-expiring and usable for unlimited future charges, but that wording does not establish present product support, account or buyer eligibility, authorization for a future charge, or successful execution.
- A `Transaction` represents an attempted movement of money. Successful transactions change status as money moves toward the merchant's bank account; an unsuccessful transaction's status describes the failure. Reversing a transaction is state-dependent: the guide says it either cancels before funds are debited or refunds after money has changed hands, while direct refund is the more granular route.
- `paymentMethodSnapshot` preserves method details from transaction time, whereas `paymentMethod` requests the current vaulted method and is null when the transaction was not created with a vaulted method. Their GraphQL return types also differ; exact union members and fields belong to the schema reference.
- Customers are optional grouping records with one-to-many payment-method and transaction relationships. The guide says a payment method cannot be transferred to another customer and a transaction cannot be reassociated after creation; a single-use method can still be charged or authorized with a `customerId` when the customer does not store it.

> [!warning] Consequential and evidence boundaries
> Vaulting consumes the original single-use payment method; reversing or refunding changes transaction or monetary state; and the documented customer associations cannot later be transferred or reassigned. Confirm current operation prerequisites and state before acting. The page's examples and object descriptions are website-documentation evidence, not exact commit-qualified GraphQL schema or runtime guarantees.

## Detail locators

- Guide purpose and API Explorer route for full object fields: opening paragraph, lines 14-16.
- Typical client-token, client-SDK, nonce handoff, vault and charge sequence: `## The Lifecycle of a Payment`, lines 19-30.
- Payment-method identity and illustrative funding-source detail objects: `## Payment Methods`, lines 35-48.
- Single-use lifespan, vault consumption and the page's multi-use-method characterization: `### The Braintree Vault`, lines 51-55.
- Transaction identity, status progression, reversal and refund distinctions: `## Transactions`, lines 58-66.
- Snapshot-versus-current payment-method semantics and return-type examples: `### Transactions and Payment Methods`, lines 69-73.
- Optional customer grouping, vault association behavior, single-use `customerId` route, transaction membership and immutable associations: `## Customers`, lines 76-96.
- Exact commit-qualified GraphQL operation shapes, nullability, unions, enums and constraints are separately retained in `raw/github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/files/schema.graphql` via [[source-github-graphql-api]]; do not infer them from this website guide.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Single-use method terminology and lifespan: [[source-braintree-payment-method-nonces]]
- Transaction operation guide: [[source-braintree-graphql-guides-transactions]]
- Exact commit-qualified schema: [[source-github-graphql-api]]

## Raw Sources

- [[raw/braintree/graphql/guides/concepts-2026-09-16|Braintree GraphQL Payment API Concepts guide]] - complete collected website page for payment lifecycle, payment methods, Vault, transaction and customer concepts
