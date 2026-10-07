---
title: "Braintree In-Person Configure Sandbox"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/get-started-1/configure-sandbox"
raw_files:
  - "braintree/in-person/get-started-1/configure-sandbox-2026-09-16.md"
tags: [braintree, in-person, sandbox, dev-kit, graphql]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide is a preparation sequence for a Braintree Sandbox account before connecting a Dev Kit Verifone P400 reader and before the kit arrives. It covers Sandbox account creation, merchant-authentication selection, a first Braintree GraphQL connectivity request, optional In-Store custom fields, and test transaction, reversal/refund and search exercises. The sequence is setup guidance, not proof of current product availability, account eligibility, reader pairing or connectivity, production enablement, or any successful payment, refund or search result.

## Key takeaways

- The page recommends preparing a Braintree Sandbox account before the reader arrives. Its Dev Kit Verifone P400 is designed for only one Braintree Sandbox account: after pairing, the page says it cannot be used with another Braintree Sandbox account. The Dev Kit is limited by this snapshot to a United States Sandbox account, so sign-up must select United States.
- A merchant or third-party integrator working for a merchant must choose and implement an authentication method suited to the use case. The page describes static first-party API keys as the fastest route, not the only route: it identifies the Public Key and Private Key as values generated in the Sandbox merchant account and says to save them safely.
- For the connectivity exercise, the guide recommends Postman with its linked Braintree GraphQL In-Store collection and Sandbox environment. After import, it instructs the user to configure the collection for Basic Auth with the Sandbox Public API Key as username and Private Key as password, save the settings, and make a first Braintree GraphQL request. This is a credentialed connectivity check, not reader pairing, transaction success or production proof.
- In-Store custom fields are optional and account-dependent. The page says they can retain additional In-Person transaction data for Control Panel visibility and reporting, with Cashier ID or the employee creating the transaction as examples; those examples do not require those fields for every merchant.
- The remaining exercises route to linked authorities for creating a card-not-present GraphQL transaction with testing nonces, reversing or refunding a test transaction, and searching transaction records for back-office or reporting needs. This page supplies the sequence and navigation, while the linked guides hold the operation details.

## Material warnings

> [!warning] Dev Kit account binding and country scope
> The snapshot says the Dev Kit Verifone P400 is designed for only one Braintree Sandbox account and cannot be used with another Braintree Sandbox account after pairing. It also limits the Dev Kit to United States Sandbox accounts. Account creation or possession of keys does not establish reader pairing or eligibility beyond those stated conditions.

> [!warning] Sandbox preparation is not production or outcome proof
> Authentication setup, a GraphQL connectivity request, optional field configuration and test exercises are Sandbox preparation. They do not prove production enablement, current availability, reader-online state, or successful authorization, charge, reversal, refund, settlement, funding or search results.

## Detail locators

- Preparation purpose before the Dev Kit arrives: introduction, lines 14-16.
- Sandbox account creation, one-account reader binding and United States-only Dev Kit condition: `### 1. Create a Braintree Sandbox Account`, lines 19-26.
- Authentication choice, merchant/integrator scope and static first-party Public/Private API key route: `### 2. Review Authentication Options`, lines 29-33.
- Postman collection/environment imports, Basic Auth field mapping and first GraphQL connectivity request: `### 3. Make a Braintree GraphQL Request`, lines 36-45.
- Optional In-Store custom-field purpose and examples: `### 4. Configure Custom Fields in Sandbox (Optional)`, lines 48-50.
- Card-not-present transaction exercise and testing-nonce navigation: `### 5. Test a "card not present" transaction`, lines 53-55.
- Cancellation/refund exercise and authorization-reversal example navigation: `### 6. Implement reversals`, lines 58-60.
- Transaction-search purpose and query-example navigation: `### 7. Search for transactions`, lines 63-65.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Related raw API references

- [[raw/braintree/in-person/guides/api-authentication-2026-09-16|API Authentication Options]] - unread authentication-method navigation
- [[raw/braintree/articles/control-panel/important-gateway-credentials-2026-09-16|Important Gateway Credentials]] - unread Sandbox API-key navigation
- [[raw/braintree/graphql/guides/making_api_calls-2026-09-16|Making Braintree GraphQL API Calls]] - unread first-request navigation
- [[raw/braintree/articles/control-panel/custom-fields-2026-09-16|Custom Fields]] - unread configuration navigation
- [[raw/braintree/graphql/guides/transactions-2026-09-16|GraphQL Transactions]] - unread card-not-present and reversal/refund navigation
- [[raw/braintree/in-person/guides/making-a-transaction-2026-09-16|In-Person Transaction Examples]] - unread authorization-reversal example navigation
- [[raw/braintree/graphql/guides/search-2026-09-16|GraphQL Search]] - unread transaction-search navigation
- [[raw/braintree/in-person/guides/additional-api-calls-2026-09-16|In-Person Additional API Calls]] - unread transaction-query example navigation

## Raw Sources

- [[raw/braintree/in-person/get-started-1/configure-sandbox-2026-09-16|Braintree In-Person Configure Sandbox]] - complete collected preparation guide for the Dev Kit Sandbox account, authentication, GraphQL connectivity and test-operation sequence
