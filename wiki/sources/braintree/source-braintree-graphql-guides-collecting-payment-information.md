---
title: "Braintree GraphQL Collecting Payment Information Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/guides/collecting_payment_information"
raw_files:
  - "braintree/graphql/guides/collecting_payment_information-2026-09-16.md"
tags: [braintree, graphql, payment-methods, tokenization, client-token]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide describes a client/server route for collecting payment information without the merchant storing or passing through the sensitive payment data: a Braintree client SDK sends the data to Braintree, which temporarily stores it and returns a string identifier. Client SDK documentation calls that string a nonce; for the GraphQL API, the guide identifies it as the ID of a single-use `PaymentMethod`. The page is orientation and example evidence, not an exact GraphQL schema, a package-qualified SDK implementation, server-credential guidance, proof of current payment-method eligibility, or evidence that tokenization, charging, vaulting or payment execution succeeded.

## Key takeaways

- The guide's collection boundary assigns sensitive-data submission to a Braintree client SDK: the SDK sends payment data directly from the client to Braintree's servers, where it is temporarily stored, and returns an identifier to the client. This statement describes Braintree's offered SDK integration path; it does not establish the behavior or compliance scope of arbitrary merchant-built collection forms.
- The same identifier is called a nonce in the SDK documentation and the ID of a single-use `PaymentMethod` in GraphQL. The guide directs the client-side flow to submit it to the merchant server, where a GraphQL integration can use it to charge or vault the payment method. The single-use label does not prove that a displayed example request succeeded or that a particular merchant or buyer is eligible.
- Configuring the client-side integration requires a form of authorization. The page presents a GraphQL `createClientToken` mutation as one option, then shows a separate mutation/variables example with an optional merchant-account ID. The page does not document the server credentials used to call GraphQL, make `merchantAccountId` universally required, or establish that the displayed mutation shape is the complete current schema.
- The checkout snippet is specifically introduced as an example for a website. It initializes Braintree Drop-in with the client token, requests a payment method and comments that `payload.nonce` should be submitted to the merchant server. Treat it as illustrative website code, not proof of a named Drop-in or JavaScript package version, a successful client-token request, or runtime payment behavior.

> [!warning] Single-use and evidence boundaries
> The returned GraphQL payment-method ID is described as single-use and is passed to the merchant server for charging or vaulting. The page presents GraphQL client-token creation separately from using the returned token in the client-side integration, but does not document the server credentials used for that API call. Do not treat its client-token and Drop-in examples as execution, eligibility, schema-completeness or security-compliance proof. The raw does not specify a nonce lifetime beyond calling it single-use.

## Detail locators

- Supported payment-method examples and links to method-specific guides: `## The Client-Side Integration`, line 19.
- Sensitive-data route, temporary Braintree storage, nonce terminology, GraphQL single-use `PaymentMethod` ID and charge-or-vault handoff: `## The Client-Side Integration`, line 21.
- JavaScript, iOS and Android client-SDK guide navigation: line 23; these links are navigation, not retained package-version evidence.
- Client authorization prerequisite and GraphQL client-token option: `## Requesting a Client Token`, lines 26-28.
- Basic `createClientToken` mutation example: lines 30-38.
- Optional merchant-account-ID mutation and variables examples: lines 42-64.
- Website Drop-in illustration and `payload.nonce` server handoff: `## Use the Client Token to Get a Payment Method`, lines 68-73.
- Server-side charge-or-Vault instruction: `## Use the Payment Method`, lines 76-78.
- Tokenization terminology and non-sensitive GraphQL ID description: `#### Terminology Note`, lines 81-87.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- GraphQL payment lifecycle orientation: [[source-braintree-graphql-guides-concepts]]
- GraphQL payment-method lifecycle operations: [[source-braintree-graphql-guides-payment-methods]]
- Browser SDK boundary: [[braintree-web-sdk]]
- Server integration boundary: [[braintree-server-sdk]]
- Exact commit-qualified GraphQL schema: [[source-github-graphql-api]]

## Raw Sources

- [[raw/braintree/graphql/guides/collecting_payment_information-2026-09-16|Braintree GraphQL collecting payment information guide (2026-09-16)]]
