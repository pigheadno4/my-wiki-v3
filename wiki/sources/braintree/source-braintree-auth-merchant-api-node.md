---
title: "Braintree Auth Merchant API (Node.js)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-auth/merchant-api/node"
raw_files:
  - "braintree/docs/guides/braintree-auth/merchant-api/node-2026-09-16.md"
tags: [braintree, braintree-auth, merchant-api, node-js, access-tokens]
---

## Overview

This collected Braintree Auth Node.js guide covers using an already-obtained access token to initialize a gateway and perform actions on behalf of a connected merchant. It demonstrates transaction-sale and customer-creation calls and preserves the authentication-error boundary when the merchant revokes the authorization grant. The snapshot marks Braintree Auth as closed beta; it does not establish current availability, platform eligibility, transaction approval, or successful customer creation.

## Key takeaways

- The page requires an `access_token` before merchant-scoped actions can be performed. For these actions, it says the gateway is instantiated with that access token instead of the client ID and client secret used when a merchant acts for itself.
- The guide demonstrates `gateway.transaction.sale()` and `gateway.customer.create()` with both callback and Promise forms. These are worked examples, not a complete Merchant API operation or request-field reference; their inputs and returned IDs remain at the exact raw locators below.
- A merchant may revoke the authorization grant at any time. The guide states that a subsequent attempt to act on that merchant's behalf results in `exceptions.AuthenticationError`.

> [!warning] Closed-beta and merchant-action scope
> This 2026-09-16 snapshot labels Braintree Auth closed beta. Its examples show how the guide uses an access token for connected-merchant actions; they do not prove current product access, merchant authorization, transaction approval, settlement, or successful persistence of a customer.

## Detail locators

- Closed-beta availability and interest route: `# Merchant API > AVAILABILITY`, lines 17-18.
- Access-token prerequisite and gateway-credential distinction: `# Merchant API`, lines 20-22.
- Transaction-sale callback and Promise examples, including their displayed request fields and returned transaction ID: `## Creating a transaction`, lines 23-52.
- Customer-creation callback and Promise examples, including their displayed customer fields and returned customer ID: `## Creating a customer`, lines 54-87.
- Merchant revocation and resulting authentication error: `## Authentication errors`, lines 89-91.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-auth]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-auth/oauth-flow/node-2026-09-16|Braintree Auth OAuth Flow (Node.js)]] - navigation-only route for obtaining and managing the access token; not used as factual evidence here
- [[raw/braintree/docs/guides/braintree-auth/reference/node-2026-09-16|Braintree Auth Node.js guide reference]] - navigation-only route for broader Auth objects and operations; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/guides/braintree-auth/merchant-api/node-2026-09-16|Braintree Auth Merchant API (Node.js)]] - complete collected guide covering the access-token gateway setup, transaction and customer examples, and revoked-grant authentication error
