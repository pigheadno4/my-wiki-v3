---
title: "Braintree SEPA Direct Debit Testing and Go Live (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/sepa-direct-debit/testing-go-live/node"
raw_files:
  - "braintree/docs/guides/sepa-direct-debit/testing-go-live/node-2026-09-16.md"
tags: [braintree, sepa, direct-debit, node-js, sandbox, production, testing]
---

## Overview

This collected Braintree Node.js website guide distinguishes mocked and linked-PayPal-account Sandbox testing for a SEPA Direct Debit integration, then documents the separate server and account changes for Production. The page has no exact Node package version. Its Sandbox flows and configuration instructions are not proof of current SEPA availability, merchant enablement, a successful live debit, settlement, or funding.

## Key takeaways

- Mocked SEPA Direct Debit testing is the default route. It uses Braintree Sandbox test values to simulate PayPal responses and can check client- and server-side configuration and request responses, but it does not support end-to-end testing, does not send data to a PayPal Sandbox account, and does not work with the PayPal Checkout component of the JavaScript v3 SDK.
- Linked-PayPal-account testing requires additional setup, connects the Braintree Sandbox account directly to a PayPal Sandbox account, returns data to both Sandbox accounts, and supports fuller integration checks such as transaction reporting and email receipts. The page says this route has no negative-testing support; linked-Sandbox results remain Sandbox evidence rather than live-payment proof.
- Linking requires API credentials from a PayPal business Sandbox account created for the same country as the Braintree Sandbox account; the app must use the same Sandbox developer account as that test account. The page warns that some fake nonces may stop working after a successful link. It also warns not to use the PayPal business account as the PayPal customer account for linked-flow or Production test payments because doing so results in declines.
- Sandbox and Production accounts are not linked: created objects, processing options and recurring-billing settings do not transfer, and Production uses different login information, merchant ID and API keys. The guide recommends a dedicated API user instead of an individual user's credentials, with a non-employee-specific email and Account Admin permissions. Production merchant ID, public key and private key must be placed in server-side code; public and private keys are environment- and user-specific.
- The Production account should mirror the tested Sandbox settings, with recurring-billing plans or settings recreated when applicable. The Node.js example switches the gateway to `braintree.Environment.Production` and Production credentials. The page says the client needs no configuration update for this switch because it obtains its client token from the server.
- The Production check calls for a limited number of low-value sale transactions for each intended payment-method type, submitted for settlement and followed through to bank deposit. Real payment methods are required, and settled tests debit the associated payment method and incur fees.

## Material warnings

> [!warning] Sandbox testing is not Production payment proof
> Mocked responses and linked-Sandbox data do not establish current Production availability, enablement, a completed bank debit, settlement, or funding. Production uses separate credentials and settings, and its test transactions use real payment methods that can move funds and incur fees.

> [!warning] Do not pay with the linked business account
> The page says using the PayPal business account as the PayPal customer account for linked-flow or Production test transactions results in declines.

## Detail locators

- Mocked versus linked-PayPal Sandbox modes, supported checks and limits: `# Testing and Go Live`, raw lines 16–32.
- PayPal business-account-as-customer decline warning: `# Testing and Go Live > IMPORTANT`, raw lines 37–38.
- Mocked-flow credentials and no-PayPal-Sandbox-data boundary: `## Mocked SEPA Direct Debit testing`, raw lines 41–45.
- Linked-account prerequisites, same-country and same-developer-account conditions, and credential fields: `## SEPA Direct Debit testing with linked PayPal account`, raw lines 46–69.
- Fake-nonce warning and Braintree Sandbox Control Panel linking actions: `## SEPA Direct Debit testing with linked PayPal account > NOTE`, raw lines 74–84.
- Sandbox/Production isolation and non-transfer warning: `## Go live > IMPORTANT`, raw lines 87–91.
- Dedicated API-user recommendation and Production credentials: `### Create an API user` through `### Get production credentials`, raw lines 94–110.
- Production settings recreation, Node.js gateway environment switch and client-token boundary: `### Update production account settings` through `### Update live server configuration`, raw lines 111–128.
- Low-value Production sales, settlement/deposit check and real-payment debit/fee warning: `## Test transactions in production`, raw lines 129–135.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- SEPA Direct Debit lifecycle overview: [[source-braintree-docs-guides-sepa-direct-debit-overview]]
- Supporting server concept: [[braintree-server-sdk]]
- Supporting administration concept: [[braintree-control-panel]]

## Related raw API references

The page links general Sandbox test values, credential and user administration, processor-decline responses, transaction sale and settlement, payment-method types, and Sandbox-versus-Production material. Those targets were not read for this entry and are navigation only; they do not establish exact SDK behavior, current availability or enablement, or a successful payment lifecycle.

## Raw Sources

- [[raw/braintree/docs/guides/sepa-direct-debit/testing-go-live/node-2026-09-16|Braintree SEPA Direct Debit Testing and Go Live for Node.js]] - complete collected page covering mocked and linked-PayPal Sandbox routes, account-linking conditions, separate Production credentials and settings, the Node.js server transition, and limited real-payment Production checks
