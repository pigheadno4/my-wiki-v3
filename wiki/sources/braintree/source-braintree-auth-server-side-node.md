---
title: "Braintree Auth Server-side Connect Flow (Node.js)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-auth/server-side/node"
raw_files:
  - "braintree/docs/guides/braintree-auth/server-side/node-2026-09-16.md"
tags: [braintree, braintree-auth, oauth, nodejs, connected-merchants]
---

## Overview

This collected Node.js guide is a retrieval entry for the server-side start of a Braintree Auth Connect flow: building the merchant Connect URL and configuring its return, OAuth scope and state controls. It documents a closed-beta Braintree Auth snapshot, not generic payment-transaction authorization, current availability, or the complete behavior of the linked Connect, OAuth-flow, configuration, reference or multi-currency guides.

## Key takeaways

- Braintree Auth is described as closed beta. For both signup-capable and login-only integrations, the guide says the first Connect step is a `connect_url` built by the Braintree server SDK; clicking **Connect with Braintree** sends the merchant to that URL and starts OAuth.
- The redirect URI is where the merchant returns when OAuth completes or when the merchant chooses to finish later, and every redirect URI must be allowlisted in OAuth configuration.
- The example's `transaction:sale` and `customer:create` scopes allow the integration to create transactions and customers for the connected merchant. The guide says to request only scopes needed by the integration's API operations and routes read-only and complete scope selection to corresponding resource scopes and the OAuth Reference.
- The guide treats `state` as a CSRF control: submit a non-guessable value, verify that the returned value matches, and escape its contents, typically with base64 or URL encoding, before the browser redirect. It says Braintree returns the submitted value with the access code.

## Evidence boundaries and detail locators

- Server-built Connect URL and Node.js construction example: `# Server-side Connect Flow`, lines 20-46.
- Redirect URI return behavior and allowlisting: `## Redirect URI`, lines 49-51.
- OAuth scope selection and multiple-scope format: `## Scope`, lines 52-56.
- CSRF purpose, return matching and escaping conditions for `state`: `## State`, lines 59-61.
- Optional landing-page behavior and existing-merchant-only login: `## Landing page` and `## Supporting login-only`, lines 62-67.
- Signup country/currency effects, payment-method defaults and restrictions, and form pre-population route: `## Supporting signups`, lines 68-79. Exact parameter values and field inventories remain in the raw guide.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-auth]]
- Related reference route: [[source-braintree-auth-reference-node]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-auth/configuration-2026-09-16|Braintree Auth configuration guide]] - unread navigation-only route for OAuth application setup and redirect allowlisting
- [[raw/braintree/docs/guides/braintree-auth/connect-2026-09-16|Braintree Auth Connect guide]] - unread navigation-only route for the merchant connection experience
- [[raw/braintree/docs/guides/braintree-auth/oauth-flow/node-2026-09-16|Braintree Auth Node.js OAuth-flow guide]] - unread navigation-only route for authorization, grant exchange and redirect handling
- [[raw/braintree/docs/guides/braintree-auth/reference/node-2026-09-16|Braintree Auth Node.js reference]] - unread navigation-only route for downloadable-software handling and exact Connect options
- [[raw/braintree/docs/guides/braintree-auth/multi-currency/node-2026-09-16|Braintree Auth Node.js multi-currency guide]] - unread navigation-only route for adding merchant presentment currencies

## Raw Sources

- [[raw/braintree/docs/guides/braintree-auth/server-side/node-2026-09-16|Braintree Auth Node.js server-side Connect flow]] - complete collected guide for Connect URL generation, redirects, OAuth scopes, state security and signup/login options
