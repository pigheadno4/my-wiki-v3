---
title: "Braintree PINless Debit Optimized Routing Ruby SDK Code Samples"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/pinless-debit/optimized-debit-routing/code-samples/sdk/ruby"
raw_files:
  - "braintree/docs/guides/pinless-debit/optimized-debit-routing/code-samples/sdk/ruby-2026-09-16.md"
tags: [braintree, pinless-debit, optimized-debit-routing, ruby, transaction-search]
---

## Overview

This captured, unversioned [[braintree|Braintree]] Ruby SDK code-sample page shows how the routed debit network is read from a transaction response and how transactions are searched by debit network. Its prose also says transactions can be retrieved by transaction ID, but the displayed search demonstrates only a debit-network filter. [[braintree-payment-methods]]

The page is illustrative website documentation, not a package-qualified or runnable guarantee. It does not identify a Ruby SDK version, credentials, environment, merchant eligibility or enablement, client/server ownership, card or network-token behavior, current support, or GitHub implementation/history, and it does not prove a matching result, authorization, payment, settlement or funding outcome.

## Key takeaways

- For transactions routed on debit networks, the page says the transaction response's `debit_network` field is populated during authorization and remains available for subsequent actions. The captured prose runs the named `submit_for_settlement` and `void` actions together, so use the raw locator rather than inferring exact method spelling or invocation from that sentence.
- The Ruby response snippet reads `result.transaction.debit_network` alongside transaction ID and status. It is a field-access example, not proof that the field is populated for transactions outside the stated debit-network-routing condition or for every merchant, card, network or environment.
- The transaction-search prose names retrieval by transaction ID or by the network used for optimized debit routing. The displayed Ruby search shows only `search.debit_network.is "STAR"`; `STAR` is an example filter value, not a routing, availability or result guarantee.
- The snapshot does not provide response/error handling, pagination or result-count behavior. The loop prints each returned transaction's amount but does not establish that the example search returns any records.

## Detail locators

- Routed-network response-field condition and subsequent-action statement: `## Fetch the routed debit network of a transaction`, raw lines 14-17.
- Ruby transaction-response field-access snippet: raw lines 18-24.
- Transaction-ID-or-debit-network search statement: `## Transaction search with debit network`, raw lines 26-29.
- Ruby `STAR` search filter and amount-printing loop: raw lines 30-38.

## Related

- [[braintree]]
- [[braintree-payment-methods]]
- [[braintree-server-sdk]] - package-qualified Ruby SDK implementation and version history are separate from this unversioned website example
- [[source-braintree-docs-guides-pinless-debit-optimized-debit-routing-integration]] - separate enablement, SDK-version and Network Transaction Identifier route
- [[source-braintree-docs-guides-pinless-debit-optimized-debit-routing-code-samples-graphql]] - separate GraphQL transaction-search example

## Raw Sources

- [[raw/braintree/docs/guides/pinless-debit/optimized-debit-routing/code-samples/sdk/ruby-2026-09-16|Braintree PINless Debit optimized-routing Ruby SDK code samples (2026-09-16 snapshot)]]
