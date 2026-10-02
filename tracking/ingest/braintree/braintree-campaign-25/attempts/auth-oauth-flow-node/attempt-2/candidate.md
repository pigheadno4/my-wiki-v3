---
title: "Braintree Auth OAuth Flow (Node.js)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-auth/oauth-flow/node"
raw_files:
  - "braintree/docs/guides/braintree-auth/oauth-flow/node-2026-09-16.md"
tags: [braintree, braintree-auth, oauth-2, node-js, access-tokens]
---

## Overview

This closed-beta Braintree Auth Node.js guide describes the OAuth 2.0 stage after a merchant completes the Connect flow: Braintree returns an authorization code to the platform's redirect URI, the platform exchanges that code for credentials, and the resulting access token enables actions on that connected merchant's behalf subject to the OAuth permissions granted through the separate Connect configuration. This OAuth-flow page does not select or enumerate those scopes. It also provides the page-specific access-token, refresh-token and revocation lifecycle boundaries.

## Key takeaways

- Braintree Auth is identified as a closed beta in this collected page. The guide says it follows OAuth 2.0, but it is not a general OAuth specification or evidence that a particular platform can currently use the product.
- After the Connect flow, Braintree redirects the merchant to the supplied `redirect_uri`. The query string includes an authorization `code`, the passed `state`, and a `merchantId`; the page describes `merchantId` as Braintree's unique account identifier and routes its support and Control Panel deep-link details to the separate reference.
- A Node.js `BraintreeGateway` configured with the platform's `clientId` and `clientSecret` calls `gateway.oauth.createTokenFromCode()` with the returned code. The response example exposes an access token, its expiration time and a refresh token. The access token enables actions on the connected merchant's behalf subject to the OAuth permissions granted through the separate Connect configuration; this OAuth-flow page does not select or enumerate those scopes.
- The guide states that an access token expires 24 hours after creation and an initially issued refresh token expires 180 days after creation. Using the refresh token returns both a new access token and a new refresh token. The page separately says the original access token can then be revoked; it does not say that refreshing automatically revokes that original token.
- The platform can call `gateway.oauth.revokeAccessToken()` for an access token. A connected merchant can also revoke OAuth access in the Control Panel; the guide links an OAuth-access-revoked webhook route and says using a revoked token through the Merchant API results in an authentication error.

## Evidence boundaries

> [!warning] Closed-beta and page-scoped lifecycle
> This 2026-09-16 snapshot marks Braintree Auth as closed beta. Its stated 24-hour access-token and 180-day refresh-token lifetimes, SDK calls and revocation behavior are page-scoped evidence, not proof of current platform eligibility, account enablement or broader OAuth behavior.

> [!warning] Refresh does not establish revocation
> The guide presents refresh and revocation as separate actions. Do not infer that obtaining new credentials automatically revokes the original access token; use the dedicated revocation route when that distinction matters.

## Detail locators

- Closed-beta availability and OAuth 2.0 identity: `# OAuth Flow`, lines 17-20.
- Post-Connect redirect query, authorization code, returned state and `merchantId`: `## Redirect and authorization grant`, line 23.
- Authorization-code exchange, gateway client credentials and `createTokenFromCode()` callback response: `## Getting an access token > ### Callback`, lines 26-40; Promise form at lines 43-57.
- Merchant-scoped Merchant API use: `## Using an access token`, lines 59-61.
- Access-token and refresh-token lifetimes and refreshed credential pair: `## Managing access tokens`, line 66; callback and Promise examples at lines 67-97.
- Platform revocation call, merchant Control Panel revocation, webhook route and revoked-token authentication error: `## Managing access tokens`, lines 98-125.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-auth]]
- Supporting concept: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-auth/connect-2026-09-16|Braintree Auth Connect guide]] - navigation-only route for the preceding Connect flow; not used as factual evidence here
- [[raw/braintree/docs/guides/braintree-auth/server-side/node-2026-09-16|Braintree Auth Node.js server-side guide]] - navigation-only route for Connect URL scope selection and state handling; not used as factual evidence here\n- [[raw/braintree/docs/guides/braintree-auth/reference/node-2026-09-16|Braintree Auth Node.js reference]] - navigation-only route for `merchantId` details and the scope catalog; not used as factual evidence here
- [[raw/braintree/docs/guides/braintree-auth/merchant-api/node-2026-09-16|Braintree Auth Node.js Merchant API guide]] - navigation-only route for merchant-scoped actions; not used as factual evidence here
- [[raw/braintree/docs/reference/general/webhooks/oauth/node-2026-09-16|Braintree Node.js OAuth webhook reference]] - navigation-only route for OAuth-access-revoked notifications; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/guides/braintree-auth/oauth-flow/node-2026-09-16|Braintree Auth OAuth Flow (Node.js)]] - complete collected guide covering the post-Connect authorization-code exchange, merchant-scoped access token, refresh lifecycle and revocation routes
