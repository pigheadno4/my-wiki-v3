---
title: "Braintree Server-Side Tokenization (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/server-side-tokenization/node"
raw_files:
  - "braintree/docs/guides/server-side-tokenization/node-2026-09-16.md"
tags: [braintree, nodejs, server-sdk, graphql, tokenization, credit-cards, payment-method-nonce]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide is a Node-routed walkthrough for creating a non-vaulted single-use payment method (nonce) from raw credit-card details through the GraphQL client exposed on a configured Braintree Gateway instance. It describes a tokenization request and result-access pattern, not a package-qualified SDK implementation or exact GraphQL schema baseline, and tokenization does not establish authorization, verification, Vault storage, payment success, settlement or funding.

## Key takeaways

- The documented sequence is to create a Braintree gateway instance, execute a GraphQL query with a query definition and input variables, and retrieve the resulting single-use payment method. The page names the operation as `TokenizeCreditCard` and the input as `TokenizeCreditCardInput`; the collected query-definition code block contains only `undefined`, so this snapshot does not preserve an executable mutation or its exact field selection.
- The input example nests raw card details under `input.creditCard`, with `number`, `expirationYear`, `expirationMonth` and `cardholderName`. These are illustrative values and fields, not evidence of the complete schema, requiredness, production-valid data, or a successful request. The guide routes schema discovery to the GraphQL API Explorer, introspection and the GraphQL schema rather than enumerating the full input contract.
- A configured gateway issues the operation through `gateway.graphQLClient.query(query, variables)`; the page shows both callback and Promise forms. It does not identify a Node package version, and the website example is not proof that any particular installed SDK version exposes identical behavior.
- The result examples access `result.data.tokenizeCreditCard.paymentMethod.id` as a typical nonce. The sample JSON also displays `usage: "SINGLE_USE"` and selected card-detail fields, but the page states that response fields correspond to those requested, so the example is not a guarantee that all displayed fields are returned.
- The final section uses a Braintree Sandbox and the GraphQL API Explorer for interactive field discovery and autocomplete. That sandbox workflow does not establish Production availability, merchant enablement, PCI scope, credential suitability, or execution of a real payment.

> [!warning] Captured query and scope boundaries
> The central GraphQL query-definition block is rendered as `undefined` in the collected page. Do not reconstruct the mutation text, exact selection set, required fields or runtime contract from the surrounding variable and response examples. The page accepts raw card details but states no PCI qualification or handling requirements in the captured text; use separate applicable authority before treating this walkthrough as security or compliance guidance.

## Detail locators

- Purpose, non-vaulted raw-card scope, built-in Server SDK GraphQL-client statement and three-step outline: `## Using Braintree Server SDK to create single-use payment methods (nonces) without vaulting`, raw lines 17-25.
- Named mutation, configurable response fields, schema-discovery routes and missing `undefined` Node query block: `## Execute a GraphQL query`, raw lines 28-37.
- `TokenizeCreditCardInput` variable explanation plus illustrative Node and JSON raw-card shapes: raw lines 38-69.
- Configured-gateway invocation in callback and Promise forms: raw lines 70-85.
- Result ID access as a typical nonce, callback/Promise forms and illustrative response shape with `SINGLE_USE`: `## Retrieve the single-use payment method (nonce)`, raw lines 87-133.
- Sandbox API Explorer iteration, billing-address example and autocomplete/documentation navigation: `## Going further`, raw lines 135-161.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Shared nonce and single-use-payment-method terminology/lifecycle: [[source-braintree-payment-method-nonces]]

## Related raw API references

The page links to gateway setup, the Braintree GraphQL API Explorer, introspection guidance and the GraphQL schema. Those targets were not read for this entry and are navigation only; they do not fill the missing query definition or establish exact schema, package behavior, current availability, compliance scope or execution outcomes.

## Raw Sources

- [[raw/braintree/docs/guides/server-side-tokenization/node-2026-09-16|Braintree Server-Side Tokenization Node guide]] - complete collected page covering the non-vaulted raw-card input, Server SDK GraphQL-client invocation and single-use payment-method result pattern
