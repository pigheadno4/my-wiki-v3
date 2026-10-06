---
title: "Braintree GraphQL Request Batching Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/guides/request_batching"
raw_files:
  - "braintree/graphql/guides/request_batching-2026-09-16.md"
tags: [braintree, graphql, request-batching, transport, variable-export]
---

## Overview

This collected Braintree website guide describes a work-in-progress GraphQL transport extension for sending an ordered series of ordinary GraphQL request payloads in one HTTP request and optionally passing resolved scalar values to later operations. The page says the extension is intended to maintain full compliance with the GraphQL specification because the specification leaves request/response transport intentionally vague. That is a stated design intent, not proof of achieved or current standards compliance; its `v0` media type and future-looking language make this a 2026-09-16 snapshot, not proof of deployment availability, account eligibility, SDK support or successful execution.

## Key takeaways

- A batch opts in with the custom `application/vnd+braintree.graphql.batch.v0+json` media type and sends a JSON array whose members are regular GraphQL payloads. Authentication applies to the whole batch; per-operation authentication is not supported in this snapshot.
- `@export(as: "name")` makes a resolved scalar field available as `$name` to later operations that declare the variable. An explicitly passed variable overrides an exported variable with the same name; exporting beneath a list retains only the last encountered value.
- Operations execute sequentially. Responses are regular GraphQL response payloads returned as a list in request order, with one shared `requestId`; each `exportedVariables` entry is the snapshot accumulated through that operation.
- Errors do not stop later operations. If an errored field does not resolve, its export is omitted, so a dependent later operation behaves as though that variable was never supplied and may produce its own GraphQL error.
- At the time of the snapshot, a batch is limited to five operations and operations beyond the limit return an error. Only scalar values can be exported, and the implementation returns one combined response rather than streaming individual results.
- Braintree recommends batching only when mixing queries and mutations and/or passing values between them. Independent fields should use standard GraphQL where possible: query fields run in parallel, while top-level mutation fields run sequentially.

> [!warning] No stop-on-error guarantee
> Do not treat an earlier GraphQL error as rollback or short-circuit behavior. Every operation is attempted, so independent later mutations may still have effects even when an earlier dependency fails.

> [!warning] Keep website transport evidence separate
> The code sample uses a generic Ruby HTTP gem; it does not establish Braintree Ruby, other server-SDK or client-SDK support. The separately retained `braintree/graphql-api` source is a commit-qualified field/schema contract and must not inherit this website snapshot's batching transport behavior without exact repository evidence.

## Detail locators

- Ruby HTTP example, whole-request basic authentication, required custom media type, JSON-array body and exported-variable dependency: raw lines 18-33.
- Ordered response list, shared request ID, accumulated `exportedVariables` snapshots and dependency-failure example: `## Responses`, raw lines 36-52.
- Intended use versus standard GraphQL query/mutation execution and preference for standard GraphQL: `## When to use Request Batching`, raw lines 55-94.
- Single combined response rather than streaming: `## Prior Art`, raw lines 97-99.
- Non-short-circuit execution, sequential timing, five-operation limit, scalar-only export, passed-variable precedence, list-node last-value behavior and batch-wide authentication: `## More Considerations and Limitations`, raw lines 102-134.
- Composable-operation motivation and single-response handling goal: `## Motivation`, raw lines 137-143.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Separate commit-qualified schema authority: [[source-github-graphql-api]]

## Raw Sources

- [[raw/braintree/graphql/guides/request_batching-2026-09-16|Braintree GraphQL Request Batching]] - fully read 2026-09-16 website snapshot of the batching transport, operation ordering, variable dependency, error behavior and limits
