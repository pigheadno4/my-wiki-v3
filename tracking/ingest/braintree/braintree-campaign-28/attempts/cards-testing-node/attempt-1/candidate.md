---
title: "Braintree Credit Cards Testing and Go Live (Node.js)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/credit-cards/testing-go-live/node"
raw_files:
  - "braintree/docs/guides/credit-cards/testing-go-live/node-2026-09-16.md"
tags: [braintree, credit-cards, node-js, sandbox, production, testing]
---

## Overview

This collected Braintree Node.js guide documents Sandbox credit-card test values and the responsibilities for moving a card integration to Production. Its retrieval value is the distinction between transaction and verification test controls, the isolated Production account and credentials, the server-side environment change, and the limited real-payment checks recommended after go-live preparation.

## Key takeaways

- The Sandbox accepts specific test card numbers. In this guide, transaction success is controlled by the test amount, while verification success is controlled by the test card number. A listed valid card number does not guarantee transaction success because transaction amount and, when enabled, AVS/CVV information can also affect the result.
- Separate tables cover card numbers that simulate unsuccessful verification, card-type indicators, and issuer or bank information. These values and examples remain at the raw locators below; they are Sandbox fixtures, not evidence of Production acceptance or current payment-method support.
- Sandbox and Production accounts are not linked. Created objects, processing options, and recurring-billing settings do not transfer, while login information, merchant ID, and API keys differ. Production settings therefore must be recreated to match the tested configuration, including applicable recurring-billing plans or settings.
- The guide recommends a dedicated API user rather than an individual user's credentials because deleting or suspending that individual could break the gateway connection. It calls for a non-employee-specific email and Account Admin permissions, then places the API user's Production merchant ID, public key, and private key in server-side code; public and private keys are environment- and user-specific.
- The Node.js server configuration switches to `braintree.Environment.Production` and Production credentials. The page says no client-side configuration update is needed for this switch because the client receives its client token from the server.
- The Production check uses a small number of low-value sale transactions for each intended payment-method type, submitted for settlement and followed through to bank deposit. Real payment methods are required; settled tests debit the associated method and incur fees, so the guide says to use reasonable amounts and limit the number of transactions.

> [!warning] Snapshot guidance is not live-payment proof
> This collected page does not establish current card or payment-method support, merchant eligibility, Production acceptance, successful settlement, or bank deposit. Sandbox values do not work in Production, and the Production-check procedure involves real payment methods, debits, and assessed fees. Damaged or concatenated rendered link labels in the snapshot are navigation limitations, not negative evidence about product behavior.

## Detail locators

- Transaction-success versus verification-success controls: `# Testing and Go Live > NOTE`, lines 16-22.
- Valid card-number table and amount/AVS/CVV qualification: `### Valid card numbers`, lines 25-57.
- Unsuccessful-verification card table and transaction-versus-verification warning: `### Card numbers for unsuccessful verification`, lines 58-73.
- Card-type indicator values: `### Card numbers with type indicators`, lines 74-86.
- Country-of-issuance and issuing-bank examples: `### Card numbers with other information`, lines 89-102.
- Sandbox/Production isolation and non-transfer warning: `## Go live > IMPORTANT`, lines 104-108.
- Dedicated API-user recommendation and Production credentials: `### Create an API user` through `### Get production credentials`, lines 111-127.
- Production account recreation, Node.js server environment change, and client-token boundary: `### Update production account settings` through `### Update live server configuration`, lines 128-145.
- Low-value Production sales, settlement/deposit check, and real-payment debit/fee warning: `## Test transactions in production`, lines 146-150.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Supporting integration concept: [[braintree-server-sdk]]
- Related environment comparison: [[source-braintree-get-started-try-it-out]]

## Related raw API references

- [[raw/braintree/docs/reference/general/testing/node-2026-09-16|Braintree Node.js general testing reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/control-panel/important-gateway-credentials-2026-09-16|Braintree gateway-credentials article]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/control-panel/users-roles/managing-users-roles-2026-09-16|Braintree users-and-roles article]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Braintree Node.js transaction-sale reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/payment-method-types-overview-2026-09-16|Braintree payment-method types overview]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/credit-cards/testing-go-live/node-2026-09-16|Braintree Credit Cards Testing and Go Live for Node.js]] - complete collected guide covering Sandbox card-test controls and tables, isolated Production credentials and settings, the Node.js server environment change, and limited real-payment Production checks
