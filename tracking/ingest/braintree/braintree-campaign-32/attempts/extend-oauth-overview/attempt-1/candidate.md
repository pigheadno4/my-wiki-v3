---
title: "Braintree Extend OAuth Overview"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/oauth/overview"
raw_files:
  - "braintree/docs/guides/extend/oauth/overview-2026-09-16.md"
tags: [braintree, braintree-extend, oauth, connected-merchants, consent]
---

## Overview

This collected unversioned Braintree Extend overview provides the purpose and end-to-end orientation for OAuth between separate Braintree accounts. An integrator's server creates a Connect URL, a merchant agrees to the requested scopes, Braintree returns the merchant to the supplied redirect URI with an authorization code, and the server exchanges that code for an access token used for authorized API calls on the merchant's behalf. This is an orientation route for [[braintree-extend-oauth]], not authority for the separate [[braintree-auth]] product.

## Key takeaways

- The page says OAuth lets separate Braintree accounts connect securely and share information. It can be used alone or with the linked Grant API and Shared Vault routes, and the page states that Braintree's implementation follows OAuth 2.0.
- The documented sequence separates responsibilities: the server generates the Connect URL with requested scopes and a redirect URI; the merchant follows that URL, logs in and consents; Braintree returns an authorization code at the redirect; and the server creates the merchant access token used for delegated API calls. Exact Connect URL inputs, scope definitions and access-token mechanics remain in their dedicated guides.
- In this 2026-09-16 snapshot, the page labels OAuth closed beta in production and open beta in sandbox. That statement does not prove current availability, platform or merchant eligibility, completed consent, credential issuance, successful API execution or payment acceptance. The production-interest link points to a Braintree Auth URL, but it does not make this Extend-path overview authority for [[braintree-auth]].

## Detail locators

- Snapshot production and sandbox availability plus the production-interest route: `# Overview`, lines 16-17.
- Separate-account connection purpose, Grant API and Shared Vault navigation, and OAuth 2.0 statement: `# Overview`, line 19.
- Connect URL, merchant consent, redirect authorization code and server-created access-token sequence: `## OAuth sequence`, lines 22-29.
- Configuration next-page navigation: lines 33-33.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-extend-oauth]]
- Product orientation: [[braintree-payment-platform]]
- Separate product route: [[braintree-auth]]

## Related raw API references

- [[raw/braintree/docs/guides/extend/oauth/configuration-2026-09-16|Braintree Extend OAuth configuration]] - unread navigation-only route from this overview's next-page link
- [[raw/braintree/docs/guides/extend/oauth/connect-urls/node-2026-09-16|Braintree Extend OAuth Connect URLs (Node.js)]] - unread navigation-only route for Connect URL details
- [[raw/braintree/docs/guides/extend/oauth/access-tokens/node-2026-09-16|Braintree Extend OAuth Access Tokens (Node.js)]] - unread navigation-only route for authorization-code exchange and token details
- [[raw/braintree/docs/guides/extend/oauth/shared-vault/node-2026-09-16|Braintree Extend Shared Vault (Node.js)]] - unread navigation-only route for the linked Shared Vault use case

The assigned raw also links a Grant API overview; that target was not separately collected or read for this entry.

## Raw Sources

- [[raw/braintree/docs/guides/extend/oauth/overview-2026-09-16|Braintree Extend OAuth Overview]] - complete collected overview for separate-account OAuth purpose, merchant consent, redirect and server-side delegation sequence, related-product navigation and snapshot availability
