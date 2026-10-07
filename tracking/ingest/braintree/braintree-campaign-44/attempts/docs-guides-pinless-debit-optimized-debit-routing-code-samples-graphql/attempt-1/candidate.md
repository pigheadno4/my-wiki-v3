---
title: "Braintree PINless Debit Optimized Routing GraphQL Code Sample"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/pinless-debit/optimized-debit-routing/code-samples/graphql"
raw_files:
  - "braintree/docs/guides/pinless-debit/optimized-debit-routing/code-samples/graphql-2026-09-16.md"
tags: [braintree, pinless-debit, optimized-debit-routing, graphql, transaction-search]
---

## Overview

This captured, unversioned [[braintree|Braintree]] code-sample page shows a GraphQL transaction search for records associated with PINless debit optimized routing. Its text says transactions can be retrieved by transaction ID or by the debit network used during the transaction; the displayed query demonstrates only the debit-network path, paired with a creation-time window. [[braintree-payment-methods]]

The page is an illustrative raw GraphQL example, not a runnable guarantee: it does not supply endpoint, credentials, headers, environment, error handling, client/server ownership, platform or SDK/version context, and the snapshot does not prove current schema or enum validity, merchant enablement, matching results, payment success, settlement or funding.

## Key takeaways

- The operation declares a required `$input` variable of type `TransactionSearchInput!` and passes it to `search.transactions`. That operation-level non-null marker does not establish which nested input fields are required.
- The shown variables filter `debitNetwork.is` to `STAR` and combine it with `createdAt.greaterThanOrEqualTo` and `createdAt.lessThanOrEqualTo` timestamps. These are example values and a bounded example time window, not a statement that `STAR` is universally available or that the displayed values are valid for every account or environment.
- The selection set asks for pagination metadata and transaction nodes, including `debitNetwork`, identifiers, timestamps, status, source, amount, merchant account, order, customer, disbursement, risk, facilitator, status-history, payment-method snapshot, custom-field and processor-response data. Use the raw query for the exact field and inline-fragment projection.
- Although the prose also names transaction-ID retrieval, the captured page does not show a transaction-ID variable example.

## Detail locators

- Search purpose and transaction-ID-versus-debit-network statement: `## Transaction search with debit network`, raw lines 14-16.
- GraphQL operation, pagination and full result selection: `### Query`, raw lines 19-194.
- `debitNetwork` result projection: raw line 37.
- `STAR` debit-network filter and example creation-time bounds: `### Variables`, raw lines 196-209.

## Related

- [[braintree]]
- [[braintree-payment-methods]]
- [[source-braintree-docs-guides-pinless-debit-optimized-debit-routing-integration]] - separate PINless debit integration route
- [[source-braintree-graphql-guides-search]] - broader GraphQL search route

## Raw Sources

- [[raw/braintree/docs/guides/pinless-debit/optimized-debit-routing/code-samples/graphql-2026-09-16|Braintree PINless Debit optimized-routing GraphQL code sample (2026-09-16 snapshot)]]
