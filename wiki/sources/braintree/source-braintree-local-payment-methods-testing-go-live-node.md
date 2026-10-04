---
title: "Braintree Local Payment Methods Testing and Go Live (Node.js)"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/testing-go-live/node"
raw_files:
  - "braintree/docs/guides/local-payment-methods/testing-go-live/node-2026-09-16.md"
tags: [braintree, local-payment-methods, node-js, sandbox, production, testing]
---

## Overview

This collected Braintree Node.js guide distinguishes two Sandbox approaches for Local Payment Methods and documents the separate work required to move server-side configuration to Production. It is a website snapshot with no exact Node package version; simulated or linked-Sandbox results are not proof of current merchant eligibility, Production acceptance, successful live payment, settlement, or funding.

## Key takeaways

- Mocked Local Payment Method testing is the default. It uses Braintree Sandbox test values to simulate PayPal responses and can check client- and server-side configuration and expected request responses, but it does not provide end-to-end testing, send data to a PayPal Sandbox account, or work with the PayPal Checkout component of the JavaScript v3 SDK.
- The linked-PayPal-account approach requires additional setup and connects a Braintree Sandbox account to a PayPal Sandbox account. The page says this returns data to both Sandbox accounts and enables fuller integration testing such as transaction reporting and email receipts. This remains Sandbox evidence, not a completed live-payment result.
- The linked flow requires PayPal Sandbox API credentials. The PayPal business Sandbox account must use the same country as the Braintree Sandbox account; the app must use the same Sandbox developer account. After linking, some fake nonces may stop working. The page warns not to use the PayPal business account as the customer account for linked-flow or Production test payments because that results in declines.
- Sandbox and Production accounts are not linked: objects, processing options, recurring-billing settings, login information, merchant ID, and API keys do not transfer. The guide recommends a dedicated API user rather than an individual user's credentials, with a non-employee-specific email and Account Admin permissions, and requires Production merchant ID, public key, and private key in server-side code. Public and private keys are environment- and user-specific.
- The Node.js server example switches the gateway to `braintree.Environment.Production` and uses Production credentials. The page says no client-side configuration update is needed for this transition because the client obtains its client token from the server; this does not remove method enablement or account-configuration prerequisites. Production account settings must mirror the tested Sandbox configuration, with recurring-billing plans or settings recreated when applicable.
- The Production check calls for a small number of low-value sale transactions for each intended payment-method type, submitted for settlement and followed through to bank deposit. Real payment methods are required; settled test transactions debit the associated method and incur fees, so the guide says to use reasonable amounts and limit the number of tests.

> [!warning] Sandbox results are not live-payment proof
> Mocked outcomes and linked-Sandbox data do not establish Production availability or a completed live payment. Production uses separate credentials and settings, requires real payment methods, and can move real funds and incur fees.

## Detail locators

- Mocked versus linked-PayPal Sandbox testing modes and their boundaries: `# Testing and Go Live`, lines 16-31.
- PayPal business-account-as-customer decline warning: `# Testing and Go Live > IMPORTANT`, lines 36-37.
- Mocked-flow credential route and no-PayPal-Sandbox-data boundary: `## Mocked Local Payment Method testing`, lines 40-44.
- Linked-account prerequisites, same-country/account setup and Sandbox credentials: `## Local Payment Method testing with linked PayPal account`, lines 45-68.
- Fake-nonce warning and Braintree Sandbox Control Panel linking steps: `## Local Payment Method testing with linked PayPal account > NOTE`, lines 73-83.
- Sandbox/Production isolation and non-transfer warning: `## Go live`, lines 86-90.
- Dedicated API-user recommendation and Production credential requirements: `## Go live > ### Create an API user` through `### Get production credentials`, lines 93-109.
- Production account recreation, Node.js server environment switch and client-token boundary: `### Update production account settings` through `### Update live server configuration`, lines 110-127.
- Low-value Production sales, settlement/deposit check and real-payment debit/fee warning: `## Test transactions in production`, lines 128-134.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Local Payment Methods article owner: [[source-braintree-payment-methods-local-payment-methods]]
- Supporting server concept: [[braintree-server-sdk]]
- Supporting administration concept: [[braintree-control-panel]]
- Local-payment event route: [[braintree-webhooks]]

## Related raw API references

- [[raw/braintree/docs/reference/general/testing/node-2026-09-16|Braintree Node.js general testing reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/control-panel/important-gateway-credentials-2026-09-16|Braintree gateway-credentials article]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/control-panel/users-roles/managing-users-roles-2026-09-16|Braintree users-and-roles article]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/local-payment-methods/server-side/node-2026-09-16|Braintree Local Payment Methods server-side Node.js guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/general/webhooks/local-payment-methods/node-2026-09-16|Braintree Local Payment Methods webhook reference for Node.js]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Braintree Node.js transaction-sale reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/payment-method-types-overview-2026-09-16|Braintree payment-method types overview]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/get-started/try-it-out-2026-09-16|Braintree Sandbox-versus-Production article]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/testing-go-live/node-2026-09-16|Braintree Local Payment Methods Testing and Go Live for Node.js]] - complete collected page covering mocked and linked-PayPal Sandbox approaches, account and credential prerequisites, isolated Production configuration, the Node.js environment switch, and limited real-payment Production checks
