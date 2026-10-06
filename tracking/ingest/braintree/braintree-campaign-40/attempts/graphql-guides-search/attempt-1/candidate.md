---
title: "Braintree GraphQL Search Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/guides/search"
raw_files:
  - "braintree/graphql/guides/search-2026-09-16.md"
tags: [braintree, graphql, search, pagination]
---

## Overview

This 2026-09-16 snapshot of Braintree's unversioned website GraphQL search guide explains how to retrieve multiple objects of one searchable type: select the object type and requested node fields, pass criteria in variables, POST the query, and traverse the returned connection with cursors. It is a website guide, not a language-SDK contract or the exact-commit GraphQL schema. Its sandbox transaction requests and returned payloads are examples, not proof of current type availability, merchant eligibility, production behavior, or a successful payment operation.

## Key takeaways

- The guide contrasts a node query for one known object ID with a search query for multiple objects of the same type. It routes the actual searchable object types and fields to the GraphQL reference rather than defining the complete schema in this page.
- Multiple supplied criteria are combined with logical AND, so an object must satisfy every supplied criterion. An empty string, null value, or empty list is treated like an omitted search field; the guide separately warns that empty or null `isNot` does not mean "all nonempty results."
- The documented criteria patterns are ranges, timestamps, multiple-value fields, and free text. Their operators and transaction/customer inputs are examples and locators, not global guarantees for every searchable object or field.
- Results use Relay cursor connections. The snapshot says the default maximum page size is 50; clients request fields under `edges.node`, inspect `pageInfo`, and pass a returned cursor with `after` to fetch logically later results.
- When no object matches, the documented response has an empty `edges` array, `hasNextPage: false`, and null start/end cursors. This is a query-result state, not evidence about payment execution or settlement.
- The two cURL examples POST to the sandbox endpoint using placeholder Basic-auth public/private keys and a `Braintree-Version: 2019-01-01` header. Those values demonstrate the examples' environment, credential form, and version context; they do not establish a universal or current credential/version requirement.

## Detail locators

- Search purpose and four-step workflow: raw lines 14-24 under `# Searching for Objects`.
- Sandbox transaction-search cURL example, selected fields, credentials, version header, endpoint, and variables: raw lines 26-71 under `### CURL`.
- Criteria combination and empty-value semantics: raw lines 75-81 under `## Constructing Searches`.
- Range operators and bounded amount example: raw lines 84-106 under `### Ranges`.
- Timestamp operators and UTC interval example: raw lines 110-130 under `### Timestamps`.
- Multiple-value `in` operator and transaction-status example: raw lines 134-155 under `### Multiple Value Fields`.
- Free-text operators, `startsWith` example, and the `isNot` empty/null warning: raw lines 159-180 under `### Free Text Searches`.
- Combined February 2019 transaction-search example: raw lines 183-239 under `### Putting it all together`.
- Relay connection behavior, page-size statement, and first-page query/response: raw lines 243-311 under `## Understanding Your Results`.
- Subsequent-page `after` cursor example: raw lines 311-372.
- Empty-result response shape: raw lines 376-400 under `### Empty Results`.

## Related

- [[braintree]]
- [[braintree-payment-platform]]
- [[source-braintree-graphql-guides-making-api-calls]]
- [[source-github-graphql-api]]

## Raw Sources

- [[raw/braintree/graphql/guides/search-2026-09-16|Braintree GraphQL Search guide (2026-09-16 snapshot)]]
