---
title: "Braintree Auth Reference (Node.js)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-auth/reference/node"
raw_files:
  - "braintree/docs/guides/braintree-auth/reference/node-2026-09-16.md"
tags: [braintree, braintree-auth, oauth, merchant-onboarding, nodejs]
---

## Overview

This collected Node.js-route reference is a retrieval entry for Braintree Auth signup and login controls, OAuth scopes, merchant identity, and the special connection pattern for downloadable software. It documents a closed-beta Braintree Auth snapshot and is not authority for generic transaction authorization, current access, or the complete behavior of the linked Connect, OAuth, merchant-account, webhook, or multi-currency guides.

## Key takeaways

- Braintree Auth is described as closed beta. The page presents Braintree Auth and Connect with Braintree as one merchant experience in which a merchant can create an account or sign in through a Connect URL within an OAuth scope.
- Platforms can pre-populate documented user and business fields during new-account signup, while `login_only` changes the landing page to accept only existing Braintree merchants. The exact field inventory and formats remain in the raw reference.
- The reference makes standard OAuth scopes available alongside Braintree Auth-specific scope entries for dispute management, dispute webhooks, read-only access, and read-write control. Its prose says there are three additional scopes while the rendered table contains four entries, so use the table and dedicated OAuth guidance without inferring a reconciled count.
- After a merchant completes Connect, the OAuth redirect returns `merchantId`; the page characterizes it as the account's unique Braintree identifier for support and for constructing Control Panel deep links.
- For downloadable software, the page routes platform OAuth through an intermediary server so `client_id` and `client_secret` are not shipped inside the software. Its worked `state` example is explicitly insecure and must be replaced by the safe handling described in the server-side implementation guide.

## Evidence boundaries and detail locators

- Signup pre-population field categories and exact names: `## Signup form fields`, `### User`, lines 23-40, and `### Business`, lines 43-61.
- Existing-merchant-only landing-page option: `## Login-only flow`, lines 64-67.
- Scope names and meanings, including the prose/table count mismatch: `## OAuth scopes`, lines 70-77.
- OAuth redirect merchant identifier and Control Panel deep-link use: `## Merchant ID`, lines 80-85.
- Intermediary-server sequence and the insecure example-state warning: `## Downloadable software flow`, lines 86-101.
- Braintree Auth merchant-account validation error catalog: `## Merchant account validation errors`, lines 104-188. The catalog is a raw-detail route, not a complete account-creation or recovery specification.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-auth]]
- Broader product orientation: [[braintree-payment-platform]]
- Related notification route: [[source-braintree-webhooks-braintree-auth-node]]
- Related currency-account route: [[source-braintree-merchant-account-create-for-currency-node]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-auth/connect-2026-09-16|Braintree Auth Connect guide]] - unread navigation-only route for the merchant connection experience
- [[raw/braintree/docs/guides/braintree-auth/oauth-flow/node-2026-09-16|Braintree Auth Node.js OAuth-flow guide]] - unread navigation-only route for the authorization sequence and redirect handling
- [[raw/braintree/docs/guides/braintree-auth/server-side/node-2026-09-16|Braintree Auth Node.js server-side guide]] - unread navigation-only route for Connect URL generation and safe `state` handling
- [[raw/braintree/docs/guides/braintree-auth/multi-currency/node-2026-09-16|Braintree Auth Node.js multi-currency guide]] - unread navigation-only route for merchant-account currency behavior
- [[raw/braintree/docs/guides/braintree-auth/webhooks/node-2026-09-16|Braintree Auth Node.js webhooks guide]] - unread navigation-only route for Braintree Auth notification behavior

## Raw Sources

- [[raw/braintree/docs/guides/braintree-auth/reference/node-2026-09-16|Braintree Auth Node.js reference]] - complete collected reference covering signup and login controls, OAuth scopes, merchant identity, downloadable-software connection guidance, and Braintree Auth validation-error routes
