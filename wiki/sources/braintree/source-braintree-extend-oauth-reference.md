---
title: "Braintree Extend OAuth Reference"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/oauth/reference"
raw_files:
  - "braintree/docs/guides/extend/oauth/reference-2026-09-16.md"
tags: [braintree, braintree-extend, oauth, scopes, connected-merchants]
---

## Overview

This collected Braintree Extend reference is the scope catalog for OAuth applications acting on behalf of connected merchants. It separates resource-oriented OAuth scopes from additional scopes and preserves the page's production closed-beta and sandbox open-beta availability statement. It is a scope reference, not proof that a platform or merchant is eligible, connected, authorized, or able to complete a payment operation.

## Key takeaways

- The resource-oriented table maps OAuth scope names to Braintree operation routes across addresses, Apple Pay web domains, client tokens, credit-card verification, customers, disputes, document upload, merchant accounts, payment methods and nonces, settlement summaries, subscriptions, and transactions. Use the raw table for the exact inventory rather than treating this summary as a replacement schema.
- Several dispute scopes have `/facilitated` variants restricted by the page to disputes for which the connected OAuth application was a facilitator. The transaction-search-related additional scope is likewise limited to facilitated transactions; these qualifications must not be generalized to the unqualified scopes.
- The additional-scope table separately routes facilitated-transaction metrics, Grant API use, facilitated-transaction search, and Shared Vault. A scope's presence in this catalog does not prove that the corresponding product, API, merchant account, or operation is enabled or available.
- The page states that OAuth was in closed beta in production and open beta in sandbox in the collected snapshot. The linked production-interest route uses a Braintree Auth contact URL, but that link does not make this Extend OAuth scope catalog a Braintree Auth source; keep [[braintree-extend-oauth]] and [[braintree-auth]] distinct.

## Detail locators

- Snapshot availability and production-interest route: `# Reference`, lines 14-17.
- Complete resource-oriented scope inventory: `## Resource-oriented OAuth scopes`, lines 20-79.
- Facilitator-qualified dispute variants: `## Resource-oriented OAuth scopes`, lines 43-49.
- Transaction scopes, including escrow, clone, find, refund, sale, search, settlement and void routes: `## Resource-oriented OAuth scopes`, lines 71-79.
- Additional scope inventory for facilitated metrics, Grant API, facilitated search and Shared Vault: `## Additional OAuth scopes`, lines 82-89.

## Evidence boundary

> [!warning] OAuth scope, permission and execution are separate
> This page catalogs OAuth scope names and linked operation routes. It does not define Control Panel role assignment, demonstrate merchant consent, issue credentials, verify an API call, or prove authorization, payment acceptance or settlement. Control Panel role-permission questions remain owned by the separate permission source.

> [!warning] Collected rendering limitations
> The collected Markdown concatenates adjacent links in some multi-operation rows, and the `dispute:search` row retains an empty link label. Treat the verified line ranges and link targets as locators, not reconstructed API prose or proof that every linked operation was read.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-extend-oauth]]
- Product distinction: [[braintree-auth]]
- Control Panel permission navigation: [[source-braintree-control-panel-users-roles-role-permissions]]

## Related raw API references

The operation, facilitator, Grant API and Shared Vault links inside the assigned raw are navigation only unless separately collected and read.

## Raw Sources

- [[raw/braintree/docs/guides/extend/oauth/reference-2026-09-16|Braintree Extend OAuth Reference]] - complete collected scope catalog, availability statement, facilitator qualifications and linked operation routes
