---
title: "Braintree In-Person API Authentication Options"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/api-authentication"
raw_files:
  - "braintree/in-person/guides/api-authentication-2026-09-16.md"
tags: [braintree, in-person, graphql, api-authentication, oauth]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide compares two authentication options for GraphQL requests that invoke Braintree In-Person mutations: first-party API keys for a custom application serving one merchant or merchant-responsible API-calling code and surrounding infrastructure, and OAuth bearer authentication for one application or codebase serving multiple merchants. It is authentication-selection and credential-lifecycle guidance; the snapshot does not establish current availability, account eligibility or successful API/payment execution.

## Key takeaways

- For the first-party Basic Authentication option, the guide frames API keys as appropriate when a custom application serves one merchant or the merchant is fully responsible for the API-calling code and surrounding infrastructure. The merchant generates public and private keys in the Braintree Control Panel, stores them securely, and uses them in the page's linked GraphQL request pattern. The page does not publish credential values or establish that any credential is valid.
- For the third-party Bearer Authentication option, the guide frames OAuth as appropriate for a single application or codebase used by multiple merchants. A web-based permission-granting flow replaces merchants copying and pasting credentials.
- The multi-merchant application must create an OAuth application, implement the merchant-facing web OAuth flow, store each merchant's access and refresh tokens, monitor token expiry, and refresh tokens before expiry as needed. The linked configuration, flow and token pages own the exact environment, permission, exchange and lifecycle details; this page does not supply token lifetimes.
- A third-party application cannot grant permissions to its own account. For testing and development, the guide requires two Braintree Sandbox accounts: one application owner and one simulated test merchant. This Sandbox arrangement does not establish Production access or eligibility.

> [!warning] Keep credentials secure and merchant-scoped
> The page requires secure storage for first-party API keys and per-merchant storage plus expiry monitoring for OAuth tokens. Do not place real keys or tokens in wiki content, and do not treat one merchant's credentials as authority for another merchant.

> [!warning] OAuth testing requires separate Sandbox roles
> The application owner cannot grant third-party permissions to its own account. The documented two-account Sandbox setup is a testing and development condition, not Production authorization.

## Detail locators

- Two authentication options for Braintree In-Person GraphQL mutations: `## Choosing an Authentication Option for your POS Solution`, line 19.
- Single-merchant or merchant-responsible API-calling code and surrounding infrastructure condition, public/private API-key generation, secure storage and linked GraphQL request route: `### 1st Party API Caller (API Keys) - Basic Authentication`, lines 22-24.
- Multi-merchant application/codebase condition and web permission-granting purpose: `### 3rd Party Application (OAuth) - Bearer Authentication`, lines 27-29.
- OAuth application, merchant-facing flow, per-merchant token custody, expiry monitoring and refresh responsibility: `### 3rd Party Application (OAuth) - Bearer Authentication`, line 31.
- Own-account permission prohibition and separate application-owner/test-merchant Sandbox accounts: `**NOTE**`, lines 33-34.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]
- Connected-merchant OAuth routes: [[braintree-auth]] and [[braintree-extend-oauth]]

## Related raw API references

- [[raw/braintree/articles/control-panel/important-gateway-credentials-2026-09-16|Important Gateway Credentials]] - unread API-key navigation
- [[raw/braintree/graphql/guides/making_api_calls-2026-09-16|Making GraphQL API Calls]] - unread GraphQL request-requirements navigation
- [[raw/braintree/docs/guides/extend/oauth/configuration-2026-09-16|Extend OAuth Configuration]] - unread OAuth-application navigation
- [[raw/braintree/docs/guides/braintree-auth/overview-2026-09-16|Braintree Auth Overview]] - unread merchant-facing OAuth-flow navigation
- [[raw/braintree/docs/guides/extend/oauth/access-tokens/node-2026-09-16|Extend OAuth Access Tokens (Node.js)]] - unread token-lifecycle navigation
- [[raw/braintree/in-person/get-started-1/account-structure-2026-09-16|In-Person Account Structure]] - unread final-page navigation
- [[raw/braintree/in-person/guides/setup-reader-2026-09-16|In-Person Setup Reader]] - unread final-page navigation

## Raw Sources

- [[raw/braintree/in-person/guides/api-authentication-2026-09-16|Braintree In-Person API Authentication]] - complete collected guide comparing first-party API-key and third-party OAuth authentication options
