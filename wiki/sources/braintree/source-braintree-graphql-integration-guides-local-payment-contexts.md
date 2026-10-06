---
title: "Braintree GraphQL Local Payment Contexts Integration Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/integration_guides/local_payment_contexts"
raw_files:
  - "braintree/graphql/integration_guides/local_payment_contexts-2026-09-16.md"
tags: [braintree, graphql, local-payment-methods, payment-contexts, identifiers]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide describes how to retrieve a Local Payment Context with a GraphQL global ID and how to convert a legacy UUID-format context ID to a GraphQL ID. It is a lookup and identifier-conversion guide, not a client-SDK implementation, exact GraphQL schema baseline, context-creation procedure or payment-execution record. The snapshot does not establish current API availability, merchant enablement, account access or a completed payment.

## Key takeaways

- The page states that use of this API requires creating and linking a PayPal account to the Braintree Control Panel with login credentials. This is an account prerequisite in the captured guide; it does not itself prove that an account is linked, eligible or authorized for a particular Local Payment Method.
- Retrieving a Local Payment Context requires its GraphQL global ID. The example uses the root `node(id: $id)` query with an inline fragment on `LocalPaymentContext` and selects identity, type, amount/currency, approval URL, merchant-account, timestamp, payment-ID and order-ID fields. These are fields in the displayed selection set, not an exhaustive or version-pinned schema.
- The displayed response is an example for a `MULTIBANCO` context with a `1.00 EUR` amount and several null timestamps. Those values and nulls do not establish universal method behavior, required field population, a transition order or payment finality. The separate not-found JSON is likewise an example, not independently verified runtime behavior.
- If the caller has a legacy UUID-format ID, the guide says to call `idFromLegacyId(legacyId: $legacyId, type: $type)` with `LegacyIdType` set to `PAYMENT_CONTEXT`. The shown variables and returned ID are examples.

> [!warning] Context lookup is not a charge or finality signal
> This page documents retrieval and ID conversion only. It does not create a Local Payment Context, approve it, charge a payment method, authorize or capture funds, process a webhook, settle a transaction or prove merchant funding. Selecting `approvalUrl`, `approvedAt`, `transactedAt` or `expiredAt` does not by itself define the meaning, ordering or finality of those states.

> [!warning] Website-example and credential boundary
> The page does not identify an SDK, package version, exact GraphQL schema version, credential type beyond the linked-account statement, or Sandbox-versus-Production environment. Treat its queries, variables, response objects and error payload as website examples, and use the linked setup, schema and ID-migration authorities for exact current behavior. Never expose account credentials in evidence.

## Detail locators

- PayPal-account linking and Control Panel login-credential prerequisite: `## Requirements`, raw line 20.
- Global-ID requirement and legacy-ID conversion route: `## Fetching Local Payment Contexts`, raw line 25.
- `node` query, `LocalPaymentContext` type condition and selected fields: `### Query`, raw lines 28-54.
- Example `MULTIBANCO` object and request ID: `### Response`, raw lines 55-82.
- Example not-found error with `node: null`: `### JSON`, raw lines 83-114.
- Legacy UUID conversion with `idFromLegacyId` and `PAYMENT_CONTEXT`: `## Convert Legacy Id Query`, raw lines 116-145.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Local Payment Methods family overview and lifecycle boundaries: [[source-braintree-local-payment-methods-overview]]
- Linked PayPal-account setup route: [[source-braintree-payment-methods-paypal-setup-guide]]

## Related raw API references

The page links to the GraphQL `LegacyIdType` reference and the legacy-versus-GraphQL-ID migration guide. Those targets were not read for this entry and are navigation only; they do not establish exact current enum membership, schema compatibility, credential scope or runtime behavior.

## Raw Sources

- [[raw/braintree/graphql/integration_guides/local_payment_contexts-2026-09-16|Braintree GraphQL Local Payment Contexts integration guide]] - fully read pinned snapshot covering the linked-account prerequisite, global-ID lookup, displayed context fields, example not-found payload and legacy-ID conversion
