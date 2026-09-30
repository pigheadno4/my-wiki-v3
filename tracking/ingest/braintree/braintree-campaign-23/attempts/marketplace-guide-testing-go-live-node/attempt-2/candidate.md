---
title: "Braintree Marketplace Testing and Go Live (Node.js)"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/testing-go-live/node"
raw_files:
  - "braintree/docs/guides/braintree-marketplace/testing-go-live/node-2026-09-16.md"
tags: [braintree, marketplace, node-js, sandbox, production, webhooks]
---

## Overview

This collected Braintree Marketplace Node.js guide documents sandbox test inputs for sub-merchant confirmation webhooks and a production-transition sequence. Its retrieval value is the separation between sandbox simulation and production credentials, settings, server configuration, and limited live transaction checks; the collected page does not by itself establish current Marketplace availability or production acceptance.

## Key takeaways

- In sandbox testing, the guide uses the sub-merchant first-name field to trigger approval or decline confirmation webhooks when creating a merchant account. The approval path uses a Braintree test constant; the decline path uses an error code and says that provided error is returned in the webhook. These are sandbox simulation instructions, not evidence of a production underwriting result.
- The page provides two bank routing numbers that pass its stated checksum requirement for sandbox use. Exact values and Node examples remain in the raw locators rather than being reproduced as a general routing-number reference.
- Sandbox and production accounts are not linked: created objects, processing options and recurring-billing settings do not transfer, and login information, merchant ID and API keys differ.
- For production, the guide recommends a dedicated API user instead of an individual user's credentials, using a non-employee-specific email and Account Admin permissions. Production merchant ID, public key and private key are placed in server-side code; the public and private keys are environment- and user-specific.
- The Node server configuration switches to `braintree.Environment.Production` and production credentials after production settings are recreated. The guide says the client needs no configuration update for this switch because it obtains its client token from the server.
- Production checks use a small number of low-value sale transactions for each intended payment-method type, submitted for settlement and followed through to bank deposit. Real payment methods are required; settled tests debit the associated method and incur fees, so the guide warns to use reasonable amounts and limit the number of transactions.

> [!warning] Sandbox simulation is not production proof
> Nothing created in sandbox transfers to production, sandbox test values do not work in production, and the collected guide does not establish current Marketplace eligibility or live acceptance. Its production-test instructions involve real payment methods, debits and assessed fees.

> [!warning] Unresolved recurring-billing conflict
> This Marketplace guide says recurring-billing settings do not transfer and tells applicable integrations to recreate recurring-billing plans or settings in production. [[source-braintree-recurring-billing-overview]] separately states that Braintree recurring billing is not compatible with Braintree Marketplace. The collected documents do not resolve this conflict; do not infer Marketplace recurring-billing support.

## Detail locators

- Sandbox sub-merchant approval trigger and Node example: `## Sandbox testing > ### Braintree Marketplace webhooks > #### Sub-merchant approval`, lines 20-39.
- Sandbox sub-merchant decline trigger, returned error and Node error-code route: `#### Sub-merchant decline`, lines 41-58.
- Sandbox routing-number checksum statement and accepted test values: `### Bank routing numbers`, lines 59-64.
- Sandbox/production isolation and non-transfer warning: `## Go live > IMPORTANT`, lines 67-71.
- Dedicated API-user recommendation, account-permission qualification and production credentials: `### Create an API user` through `### Get production credentials`, lines 74-92.
- Production account recreation, Node server environment switch and client-token boundary: `### Update production account settings` through `### Update live server configuration`, lines 93-113.
- Low-value production sales, settlement/deposit check and real-payment debit/fee warning: `## Test transactions in production`, lines 114-120.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-marketplace]]
- Supporting server integration route: [[braintree-server-sdk]]
- Related webhook route: [[braintree-webhooks]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-marketplace/confirmation/node-2026-09-16|Braintree Marketplace confirmation guide for Node.js]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/control-panel/important-gateway-credentials-2026-09-16|Braintree gateway-credentials article]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/control-panel/users-roles/managing-users-roles-2026-09-16|Braintree users-and-roles article]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Braintree transaction-sale reference for Node.js]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/payment-method-types-overview-2026-09-16|Braintree payment-method types overview]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/braintree-marketplace/testing-go-live/node-2026-09-16|Braintree Marketplace Testing and Go Live for Node.js]] - complete collected guide covering sandbox sub-merchant webhook simulations, isolated production credentials and settings, the Node server environment switch, and limited real-payment production checks
