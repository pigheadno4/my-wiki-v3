---
title: "Braintree Extend OAuth Connect URLs (Node.js)"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/oauth/connect-urls/node"
raw_files:
  - "braintree/docs/guides/extend/oauth/connect-urls/node-2026-09-16.md"
tags: [braintree, braintree-extend, oauth, node-js, connect-urls]
---

## Overview

This collected Node.js guide documents the first Connect URL stage of [[braintree-extend-oauth]]. After a platform has configured its OAuth application, it uses its OAuth application credentials to generate a Braintree URL where a merchant logs in and is asked to agree to the requested scopes. The guide covers URL inputs and redirect and state controls; it does not prove that a merchant consented, credentials were issued, API access succeeded or a payment was accepted. This is an Extend route, not the separate [[braintree-auth]] product.

## Key takeaways

- The 2026-09-16 snapshot labels OAuth closed beta in production and open beta in sandbox. This is page-scoped availability wording, not evidence of current access, production-beta admission or account enablement.
- The platform-side Node.js gateway example initializes `BraintreeGateway` with OAuth application `clientId` and `clientSecret` values and calls `gateway.oauth.connectUrl()`. The resulting URL sends the merchant to Braintree to log in and agree to the requested scopes. The placeholders and generated URL demonstrate request construction only; they do not establish secure secret storage, successful consent or a completed connection.
- Connect URL generation requires `redirect_uri` and `scope`; `state` is also supported. The redirect URI is where Braintree sends the merchant after authorization, must already be allowlisted in the OAuth application configuration and must be a full URI. HTTPS is required in production. Exact parameter spelling in the Node example, its sample values and the Control Panel steps for revealing credentials remain in the raw locators.
- `scope` identifies requested permissions for the merchant account. Multiple scopes use a comma-delimited string. The example's `shared_vault_transactions` value is illustrative and does not prove that scope was granted, enabled or used successfully; the full scope inventory belongs to the linked OAuth reference.
- The guide describes `state` as an OAuth 2.0 CSRF control: submit a non-guessable value, verify that the value returned to the redirect URI matches it and escape its contents, typically with base64 or URL encoding, so the browser redirect does not alter it. The page says Braintree returns the submitted value verbatim; it does not replace the platform's matching check.
- For a user consenting to their own OAuth application, Braintree automatically intersects requested scopes with that user's current API privileges. If the intersection changes, the access token is automatically revoked and the user must request a new token to use the existing intersection. This special case is not a general statement about every connected merchant or every token change.

## Evidence boundaries

> [!warning] Environment and transport qualification
> Production is labeled closed beta and sandbox open beta in this collected page. Credentials must come from the Control Panel for the environment being used, and the redirect URI must be allowlisted there; production redirect URIs require HTTPS. None of those configuration facts proves current eligibility or successful authorization.

> [!warning] Credential and state security boundary
> The Node gateway example contains placeholder OAuth application credentials, not deployable values or a complete secret-management design. The documented CSRF protection depends on the platform generating a non-guessable, properly escaped `state` and comparing the returned value; merely including a fixed or unchecked value does not satisfy the described check.

> [!warning] Extend and Auth remain distinct
> This guide is collected under Braintree Extend. Its OAuth and connected-merchant vocabulary must not be used to transfer availability, configuration, scope or lifecycle claims to [[braintree-auth]].

## Detail locators

- Availability and Connect URL's place in the OAuth sequence: `# Connect URLs`, lines 14-19.
- Required credentials, required and optional parameters, and the Node `gateway.oauth.connectUrl()` example: `# Connect URLs`, lines 21-44.
- Production-versus-sandbox Control Panel credential-access steps: `## Access your OAuth application credentials`, lines 47-57.
- Redirect destination, allowlisting, full-URI requirement and production HTTPS rule: `## Specify connect URL parameters > ### Redirect URI`, lines 60-67.
- Requested-permission meaning, comma-delimited multiple scopes and the example scope route: `## Specify connect URL parameters > ### Scope`, lines 70-74.
- Own-application consent intersection and automatic revocation consequence: `## Specify connect URL parameters > ### Scope`, line 76.
- Non-guessable state, returned-value comparison and escaping guidance: `## Specify connect URL parameters > ### State`, lines 81-85.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-extend-oauth]]
- Product orientation: [[braintree-payment-platform]]
- Node gateway boundary: [[braintree-server-sdk]]
- Separate product route: [[braintree-auth]]

## Related raw API references

- [[raw/braintree/docs/guides/extend/oauth/configuration-2026-09-16|Braintree Extend OAuth configuration]] - unread navigation-only route for OAuth application configuration and redirect allowlisting details
- [[raw/braintree/docs/guides/extend/oauth/overview-2026-09-16|Braintree Extend OAuth overview]] - unread navigation-only route for the wider OAuth sequence
- [[raw/braintree/docs/guides/extend/oauth/reference-2026-09-16|Braintree Extend OAuth reference]] - unread navigation-only route for the complete scope inventory
- [[raw/braintree/docs/guides/extend/oauth/shared-vault/node-2026-09-16|Braintree Extend Shared Vault (Node.js)]] - unread navigation-only route for the example scope's Shared Vault use case
- [[raw/braintree/docs/guides/extend/oauth/access-tokens/node-2026-09-16|Braintree Extend OAuth Access Tokens (Node.js)]] - unread navigation-only route for the post-consent authorization-code exchange and token lifecycle

## Raw Sources

- [[raw/braintree/docs/guides/extend/oauth/connect-urls/node-2026-09-16|Braintree Extend OAuth Connect URLs (Node.js)]] - complete collected guide for merchant login and requested-scope consent URL generation, environment-specific application credentials, redirect allowlisting, scope selection, CSRF state handling and the own-application privilege-intersection consequence
