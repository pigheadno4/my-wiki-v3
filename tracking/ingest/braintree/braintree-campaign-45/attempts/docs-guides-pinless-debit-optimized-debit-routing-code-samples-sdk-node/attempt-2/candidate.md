---
title: "Braintree PINless Debit Optimized Routing Node SDK Code Sample"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/pinless-debit/optimized-debit-routing/code-samples/sdk/node"
raw_files:
  - "braintree/docs/guides/pinless-debit/optimized-debit-routing/code-samples/sdk/node-2026-09-16.md"
tags: [braintree, pinless-debit, optimized-debit-routing, node, transaction-search]
---

## Overview

This captured, unversioned [[braintree|Braintree]] website Node SDK-route code-sample page labels two snippets as Node examples. It illustrates reading routed debit-network metadata from a transaction response and searching optimized-routing transactions by transaction ID or the debit network used during the transaction. The visible search snippet demonstrates only the debit-network path, using `STAR` as an example filter. [[braintree-payment-methods]]

The page does not identify an exact Braintree Node SDK package or version, establish client/server ownership, or provide credentials, gateway configuration, environment, error handling, merchant eligibility or enablement. Treat it as illustrative website evidence rather than GitHub implementation/history or a guarantee of current SDK/API support, network availability, matching results, authorization success, settlement or funding. Its `debit_network` field concerns the routed debit network; the snapshot provides no network-token behavior.

> [!warning] Node property-name conflict
> The captured website response snippet literally uses `result.transaction.debit_network`, but retained exact-version `braintree@3.40.0` server-SDK evidence parses XML gateway responses through `Util.convertNodeToObject`, which camel-cases keys, and defines the transaction-search field as `debitNetwork`; its cumulative changelog also records `debitNetwork` for `Transaction.sale` and `Transaction.search`. Do not treat the website's snake_case response accessor as verified runnable or current Node SDK syntax. Keep the unversioned website statement separate from the versioned implementation evidence in [[source-github-braintree-node]]; exact code locators are `lib/braintree/http.js:151-171`, `lib/braintree/util.js:67-121`, `lib/braintree/transaction_search.js:71-74` and `CHANGELOG.md:166-173` in the retained 2026-10-06 `deb5227` snapshot.

## Key takeaways

- The page says the debit-network field is populated for transactions routed on debit networks during authorization and remains available for later actions named on the page. This is conditional on debit-network routing; it is not a promise that every transaction receives a value. The raw prose has damaged spacing around the later action names, so use the raw locator for exact captured wording.
- The first Node snippet reads `result.transaction.debit_network` alongside transaction ID and status. It shows result access only, not the request that created or authorized the transaction.
- The prose says transactions can be retrieved by transaction ID or by the network used for optimized debit routing. The displayed Node search demonstrates only `gateway.transaction.search` with `search.debitNetwork().is("STAR")`; `STAR` is an example value, not a guarantee of merchant, account or environment availability.
- The callback iterates returned transactions and logs `transaction.amount`. The example does not establish that a search will match, define pagination/completeness, or provide production-ready error handling.

## Detail locators

- Routed-debit-network population and later-action availability: `## Fetch the routed debit network of a transaction`, raw lines 14-17.
- Node transaction-result field access, including `result.transaction.debit_network`: raw lines 18-24.
- Transaction-ID-or-routed-network retrieval statement: `## Transaction search with debit network`, raw lines 26-29.
- Node `gateway.transaction.search` example, `STAR` filter, callback iteration and amount logging: raw lines 30-38.

## Related

- [[braintree]]
- [[braintree-payment-methods]]
- [[source-braintree-docs-guides-pinless-debit-optimized-debit-routing-code-samples-graphql]] - separate GraphQL transaction-search example
- [[source-braintree-docs-guides-pinless-debit-optimized-debit-routing-integration]] - separate optimized-routing integration and enablement route
- [[source-github-braintree-node]] - separate exact-version Node server-SDK implementation and history route

## Raw Sources

- [[raw/braintree/docs/guides/pinless-debit/optimized-debit-routing/code-samples/sdk/node-2026-09-16|Braintree PINless Debit optimized-routing Node code sample (2026-09-16 snapshot)]]
