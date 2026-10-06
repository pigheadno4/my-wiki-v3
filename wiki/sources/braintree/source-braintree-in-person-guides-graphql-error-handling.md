---
title: "Braintree In-Person GraphQL Error Handling"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/graphql-error-handling"
raw_files:
  - "braintree/in-person/guides/graphql-error-handling-2026-09-16.md"
tags: [braintree, in-person, graphql, error-handling, point-of-sale]
---

## Overview

This collected [[braintree|Braintree]] website guide explains how a point-of-sale application should interpret error information returned by the In-Person GraphQL API. It separates HTTP transport status from the JSON operation outcome, describes partial-success response layers, routes operational failure conditions to legacy codes, and recommends diagnostic logging. It is an unversioned website snapshot, not exact GraphQL schema or SDK authority, current reader or merchant support evidence, or proof that a payment or transaction succeeded.

## Key takeaways

- The page says the GraphQL API returns HTTP 200 even when an error occurred. Callers must inspect the JSON body: `data`, `errors`, and `extensions` may coexist, and a request containing multiple queries or mutations can contain both data and error messages. HTTP success therefore does not establish operation or payment success, and partial success must not be treated as all-or-nothing completion.
- A successful query has a `data` object whose keys match requested fields. When an error occurs, the body includes a top-level `errors` array. Its human-readable `message` is explicitly unstable and should not be parsed; the page instead identifies `extensions.legacyCode` as the error-catalog lookup key. Exact response-field and catalog details remain at the raw locators below rather than serving as commit-qualified schema evidence.
- The response `extensions` object includes a request-specific `requestId`. The guide recommends that the POS application store `requestId`, `transactionId`, and the API request and response for troubleshooting. This is diagnostic guidance: presence or logging of those identifiers does not establish reader readiness, transaction success, settlement, or funding.
- Reader identity and availability, context lifecycle, and transaction diagnosis remain distinct. The catalog separately covers an offline reader, a reader not found under the supplied ID/account credentials, a reader already processing another `PENDING` or `PROCESSING` context, a missing context, and a context that cannot be cancelled while `PROCESSING` or `COMPLETE`. It does not make a reader error a transaction-state result or define unlisted retry behavior.
- Routine request, location, pagination, configuration, printing, and other validation or operational failures are catalogued by legacy code in the raw. Processor response codes are a separate response layer that the page suggests consuming for cashier or accounting detail; the amount-based note is a simulation instruction, not proof of production processor behavior or a successful payment.

> [!warning] Inspect every returned layer
> A 200 status is only the documented transport behavior. Check `data`, `errors`, and `extensions`, preserve mixed data/error outcomes, and do not infer rollback, payment success, or transaction state from the HTTP status alone.

## Detail locators

- Response transport and partial-success model: `# GraphQL Error Handling`, raw line 16.
- Successful-query `data` object: `#### Data`, raw lines 19-21.
- Error-body requirement, invalid-reader example, unstable `message`, and `legacyCode` lookup role: `#### Errors`, raw lines 24-39.
- Request identifier and POS logging recommendation: `#### Extensions` and `#### Point of Sale Logging`, raw lines 46-53.
- Operation-specific legacy codes, including authorization, reader, context, location, owner, user-code, amount, invalid-field, pagination, configuration, and printing conditions: `## Table 1 - Error Code Explanations`, raw lines 56-87.
- Reader/context distinctions: codes `96703`, `96704`, `96706`, `96708`, and `96716`, raw lines 60-63 and 70.
- Raw processor-response-code route and amount-based simulation note: `## Processor Response Codes`, raw lines 90-96.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- [[source-braintree-graphql-guides-making-api-calls]] — general GraphQL request-construction and timeout route; this source is scoped to In-Person error interpretation.

## Raw Sources

- [[raw/braintree/in-person/guides/graphql-error-handling-2026-09-16|Braintree In-Person GraphQL Error Handling (fetched 2026-09-16)]]
