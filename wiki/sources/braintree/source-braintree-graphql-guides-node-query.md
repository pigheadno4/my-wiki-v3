---
title: "Braintree GraphQL Node Query Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/guides/node_query"
raw_files:
  - "braintree/graphql/guides/node_query-2026-09-16.md"
tags: [braintree, graphql, node-query, global-id, object-retrieval]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide describes the GraphQL `node` query for retrieving one object from a known global ID without supplying the object's type as a separate query argument. It is a GraphQL operation guide, not documentation for the legacy Braintree Node.js server SDK, a complete or exact schema, proof of current type availability, or evidence that any request or payment operation succeeded. Use the separate [[source-braintree-graphql-guides-search]] route when the retrieval question concerns multiple objects of one type rather than one known ID.

## Key takeaways

- A type is fetchable through this query only when it implements the `Node` interface and uses global IDs. The guide defines such an ID as identifying one type instance uniquely across all objects of all types that implement `Node`.
- The page's captured interface list contains `Transaction`, `PaymentMethod`, `Refund`, `Customer` and `Verification`, and it shows a `__type(name: "Node") { possibleTypes { ... } }` introspection query. Treat that list as snapshot evidence; use the retained exact-commit schema or current introspection for an exact schema question.
- The query takes an ID while inline fragments select fields for possible runtime types. The transaction and refund examples each request `status`; when the ID may identify either, the guide directs the caller to include both type fragments. The page does not document missing, invalid or unauthorized ID response behavior.
- The transaction example saves a created transaction's ID for later lookup and requests its status plus nested payment-method details. Its displayed `SUBMITTED_FOR_SETTLEMENT` payload and request ID are example output, not a guaranteed state, payment-method shape, or successful execution result.

## Detail locators

- Node-query identity, known-ID purpose and distinction from a type-specific REST endpoint: raw lines 14-18 under `# Finding Objects with Node Query`.
- `Node` interface/global-ID eligibility, introspection query and captured implementing-type list: raw lines 18-38.
- Transaction and refund fragment examples, including the two-fragment case for an ID with either possible type: raw lines 40-75.
- Saved-transaction-ID lookup query and displayed example response: raw lines 77-112 under `## Fetching Transactions`.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Multi-object search: [[source-braintree-graphql-guides-search]]
- Transaction operations: [[source-braintree-graphql-guides-transactions]]
- Exact commit-qualified schema: [[source-github-graphql-api]]

## Raw Sources

- [[raw/braintree/graphql/guides/node_query-2026-09-16|Braintree GraphQL Node Query guide]] - complete collected website page for known-global-ID object retrieval, interface eligibility, type fragments and the transaction example
