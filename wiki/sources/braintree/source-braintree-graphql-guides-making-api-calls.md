---
title: "Braintree GraphQL: Making API Calls"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/guides/making_api_calls"
raw_files:
  - "braintree/graphql/guides/making_api_calls-2026-09-16.md"
tags: [braintree, graphql, api, authentication, error-handling]
---

## Overview

This collected [[braintree|Braintree]] guide describes direct HTTP request construction for the Braintree GraphQL API: environment-specific endpoints, operation-dependent authorization credentials, required request headers and JSON body shape, response and error interpretation, timeout ambiguity, and the separate GraphiQL sandbox route. It is a request guide, not evidence that a particular SDK or deployment is compatible, that an account is enabled for an operation, or that a payment succeeded.

## Key takeaways

- Queries and mutations use one endpoint per environment; the page says requests should use POST. A registered Braintree account and an `Authorization` header are required. Tokenization keys and client-token authorization fingerprints are limited to certain generally non-money-movement operations, while vaulting and charging require API-key authentication; the page also lists closed-beta Braintree Auth access tokens.
- HTTP requests require a date-formatted `Braintree-Version` header, `Content-Type: application/json`, and a JSON object containing a `query` key plus an optional `variables` object. The version date is part of this GraphQL request contract, not an SDK-version or deployment-equivalence claim.
- The collected page says the API returns HTTP 200 even when errors occur and can return partial data together with errors. Callers must inspect the JSON `data`, `errors`, and `extensions` fields; the human-readable error message may change, and `errorType` is deprecated in favor of `errorClass`.
- Braintree says returned data is not input-validated, output-encoded, or sanitized, so the application must validate and apply context-appropriate encoding before use or display.
- The guide recommends a 60-second timeout for requests such as transaction creation. A shorter client timeout can occur before a charge later succeeds, so the timeout alone does not establish failure; the page directs the merchant to search for the transaction and verify its status.

## Detail locators

- `Endpoints` and `Important Security Requirement` — sandbox/live endpoint split, POST guidance, and application-layer validation and encoding responsibility.
- `Request Requirements` — credential types and operation limits, API-key encoding, authorization fingerprints, closed-beta Braintree Auth, required version/content headers, and JSON query/variables shape.
- `Your First Request` and `A More Interesting Request` — ping and `chargePaymentMethod` request examples, including a multiple-mutation alias example; examples do not prove account eligibility or execution.
- `Understanding Responses` — HTTP-200 behavior, partial success, top-level response objects, error fields and classes, deprecated `errorType`, and request IDs.
- `Timeouts` — recommended timeout and the later-success-after-client-timeout hazard.
- `Using GraphiQL` — browser API Explorer with sandbox login credentials and its plain-GraphQL-plus-separate-variables input format versus JSON-formatted HTTP requests.

## Related

- [[braintree-payment-platform]]
- [[braintree-auth]] — only for the separately collected Braintree Auth product and OAuth route; this page's Braintree Auth credential option is marked closed beta.

## Raw Sources

- [[raw/braintree/graphql/guides/making_api_calls-2026-09-16|Braintree GraphQL Making API Calls (fetched 2026-09-16)]]
