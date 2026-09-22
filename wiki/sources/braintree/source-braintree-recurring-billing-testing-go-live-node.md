---
title: "Braintree Recurring Billing Testing and Go Live (Node.js)"
type: source
date_ingested: 2026-09-22
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/recurring-billing/testing-go-live/node"
raw_files:
  - "braintree/docs/guides/recurring-billing/testing-go-live/node-2026-09-16.md"
tags: [braintree, node-js, recurring-billing, sandbox, production]
---

## Overview

This Braintree Node.js guide covers testing a recurring-billing integration in the sandbox and moving that integration to production. It keeps simulated sandbox values separate from live behavior, identifies the production credentials and account configuration that must be established separately, and routes detailed test values to the pinned raw page.

## Key takeaways

- Sandbox recurring-billing testing starts by storing a payment method with test values, creating a plan, and creating a subscription. The detailed payment-method, plan, subscription, nonce, verification, CVV and 3D Secure examples remain in the raw locators below rather than forming a live-behavior specification.
- In sandbox card testing, transaction success is determined by the test amount, while verification success is determined by the test nonce. The page's test nonces and Node.js nonce objects simulate sandbox outcomes; they are not production payment methods or proof of live processing behavior.
- A sandbox account is not linked to a production account. Sandbox processing options, recurring-billing settings and other created objects do not transfer, and production uses different login information, merchant ID and API keys.
- For production, the guide recommends a dedicated API user rather than an individual user's credentials, with a non-employee-specific email and Account Admin permissions. The integration then uses that user's production merchant ID, public key and private key; the public and private keys are environment- and user-specific.
- The production account must mirror the tested sandbox settings, including recreated recurring-billing plans or settings. Server-side Node.js configuration switches to `braintree.Environment.Production` and production credentials. The page says the client side needs no configuration update for this switch because it obtains its client token from the server.
- Production verification uses a small number of low-value sale transactions for every intended payment-method type, submitted for settlement and followed through to bank deposit. Production requires real payment methods: settled tests debit the associated method and incur fees, so Braintree warns to use reasonable amounts and limit the number of transactions.

> [!warning] Sandbox simulations are not live-payment evidence
> Nothing created in sandbox transfers to production, sandbox test values do not work in production, and a successful simulated result does not establish production availability or settlement. Production tests use real payment methods and can move real funds and incur fees.

## Detail locators

- Sandbox recurring-billing setup sequence: `# Testing and Go Live`, lines 16-21.
- Card-transaction versus card-verification test-success controls: `## Test values > ### Nonces representing cards`, lines 27-35.
- Card and alternative-payment-method nonce tables: `## Test values`, lines 27-94.
- Card-verification, CVV-only and 3D Secure test scenarios: `## Test values`, lines 96-169.
- Node.js nonce objects and general testing-reference route: `## Test values > ### Nonce objects > ### Node.js`, lines 171-183.
- Sandbox/production separation warning: `## Go live`, lines 186-190.
- Dedicated API-user recommendation and production credential requirements: `## Go live > ### Create an API user` through `### Get production credentials`, lines 193-211.
- Production account, server and client configuration transition: `## Go live > ### Update production account settings` through `### Update live server configuration`, lines 214-235.
- Low-value production sale, settlement and deposit checks plus the real-payment-method, debit and fee warning: `## Test transactions in production`, lines 238-244.

## Related

- Company: [[braintree]]
- Main concept: [[recurring-payments]]
- Supporting concept: [[braintree-server-sdk]]
- Related transaction creation: [[source-braintree-transaction-sale-node]]
- Related settlement submission: [[source-braintree-transaction-submit-for-settlement-node]]

## Related raw API references

- [[raw/braintree/docs/reference/request/payment-method/create/node-2026-09-16|Braintree Node.js payment-method creation reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/recurring-billing/plans/node-2026-09-16|Braintree Node.js recurring-billing plans guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/recurring-billing/create/node-2026-09-16|Braintree Node.js recurring-billing creation guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/general/testing/node-2026-09-16|Braintree Node.js testing reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/control-panel/important-gateway-credentials-2026-09-16|Braintree gateway-credentials article]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/control-panel/users-roles/managing-users-roles-2026-09-16|Braintree users-and-roles article]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/transactions/node-2026-09-16|Braintree Node.js transactions guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/payment-method-types-overview-2026-09-16|Braintree payment-method types overview]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/get-started/try-it-out-2026-09-16|Braintree sandbox-versus-production article]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/recurring-billing/testing-go-live/node-2026-09-16|Braintree Recurring Billing Testing and Go Live for Node.js]] - complete collected page covering sandbox setup and test-value routes, isolated production credentials and settings, Node.js environment transition, and limited real-payment production tests
