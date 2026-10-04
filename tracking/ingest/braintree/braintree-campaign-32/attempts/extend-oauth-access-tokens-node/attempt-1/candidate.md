---
title: "Braintree Extend OAuth Access Tokens (Node.js)"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/oauth/access-tokens/node"
raw_files:
  - "braintree/docs/guides/extend/oauth/access-tokens/node-2026-09-16.md"
tags: [braintree, braintree-extend, oauth, node-js, access-tokens]
---

## Overview

This collected Node.js guide documents the access-token stage of Braintree Extend OAuth after a merchant agrees to a platform's requested scopes. The merchant returns to the configured redirect URI, and the platform server exchanges the returned authorization code for credentials used to act on that merchant's behalf. This is an Extend OAuth route, not evidence that the separate [[braintree-auth]] product owns the flow merely because both use OAuth and connected-merchant credentials.

## Key takeaways

- The snapshot labels OAuth closed beta in production and open beta in sandbox. It does not establish current availability, production-beta acceptance, account eligibility, successful merchant consent or live payment acceptance.
- After the merchant agrees to the requested OAuth scopes, Braintree sends the merchant to the configured redirect URI. Its query parameters include the authorization `code`, Braintree `merchantId` and the previously supplied `state`; the code must be exchanged for an access token before making API calls on the merchant's behalf. The page does not define scope selection or claim permission beyond the scopes the merchant agreed to.
- The page places the exchange on the platform server. Its callback and Promise examples configure a Node.js `BraintreeGateway` with placeholder client ID and client secret values, call `gateway.oauth.createTokenFromCode()`, and read the returned access token, expiration time and refresh token. These examples do not establish successful execution or a complete credential-storage, rotation or incident-response policy.
- An OAuth access token expires 24 hours after creation, while the refresh token supplied with the initial access token expires after 180 days. Using the refresh token returns a new access token and a new refresh token. The guide presents refreshing and revoking as separate actions; it does not say refresh automatically revokes the original access token.
- The platform can revoke an access token through `gateway.oauth.revokeAccessToken()`. A connected merchant can instead revoke OAuth access in the Control Panel; the page routes notification to the OAuth-access-revoked webhook and says use of a revoked access token produces an authentication error.

## Evidence boundaries

> [!warning] Environment-qualified beta snapshot
> The production closed-beta and sandbox open-beta labels belong to this 2026-09-16 collected page. They are not proof of current availability or an individual platform's enablement in either environment.

> [!warning] Server credential boundary
> The guide assigns token creation to the platform server and displays placeholder client credentials, but it does not provide a complete security design. Do not treat its examples as client-side credential instructions or as evidence for secret storage, rotation, transport or compromise recovery beyond the documented refresh and revoke routes.

> [!warning] Extend and Auth remain distinct routes
> This source is collected under Braintree Extend. Its OAuth terminology and token lifecycle overlap with collected Braintree Auth material, but that overlap does not establish that the products, eligibility rules or documentation routes are interchangeable.

## Detail locators

- Production closed-beta and sandbox open-beta availability: `# Access Tokens`, lines 14-17.
- Merchant scope agreement, redirect and server-owned final OAuth step: `# Access Tokens`, line 19.
- Redirect query values and their stated purposes: `## Values returned in the redirect URI`, lines 22-30.
- Authorization-code exchange and returned credential fields: `## Creating an access token`, lines 33-72.
- Access-token and refresh-token lifetimes, refreshed credential pair and Node callback/Promise examples: `## Managing access tokens`, lines 75-114.
- Platform revocation, merchant Control Panel revocation, webhook route and revoked-token authentication error: `## Managing access tokens`, lines 115-142.
- OAuth reference, Shared Vault and Grant API navigation: `## Next steps`, lines 145-149.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-extend-oauth]]
- Product orientation: [[braintree-payment-platform]]
- Node gateway boundary: [[braintree-server-sdk]]
- OAuth revocation notification route: [[braintree-webhooks]]
- Separate product route: [[braintree-auth]]

## Related raw API references

- [[raw/braintree/docs/guides/extend/oauth/connect-urls/node-2026-09-16|Braintree Extend OAuth Connect URLs (Node.js)]] - unread navigation-only route for Connect URL, redirect URI, scope and state configuration
- [[raw/braintree/docs/guides/extend/oauth/reference-2026-09-16|Braintree Extend OAuth reference]] - unread navigation-only route for OAuth reference details
- [[raw/braintree/docs/guides/extend/oauth/shared-vault/node-2026-09-16|Braintree Extend Shared Vault (Node.js)]] - unread navigation-only route for the Shared Vault use case
- [[raw/braintree/docs/reference/general/webhooks/oauth/node-2026-09-16|Braintree OAuth webhook reference (Node.js)]] - unread navigation-only route for OAuth access-revocation notifications

## Raw Sources

- [[raw/braintree/docs/guides/extend/oauth/access-tokens/node-2026-09-16|Braintree Extend OAuth Access Tokens (Node.js)]] - complete collected guide for merchant-consented redirect values, server-side authorization-code exchange, token lifetimes, refresh and platform or merchant revocation