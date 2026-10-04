---
title: "Braintree Premium Fraud Management Tools Testing and Go Live (Node.js)"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/premium-fraud-management-tools/testing-go-live/node"
raw_files:
  - "braintree/docs/guides/premium-fraud-management-tools/testing-go-live/node-2026-09-16.md"
tags: [braintree, premium-fraud-management-tools, fraud-protection-advanced, node-js, sandbox, production]
---

## Overview

This 2026-09-16 Braintree Node.js guide snapshot covers sandbox simulations for Premium Fraud Management Tools and risk-threshold rejections, then the separate move to production credentials, settings and limited live transaction checks. Its central retrieval value is the environment boundary: sandbox results and configuration do not transfer to production, and the page does not by itself establish current product eligibility, account enablement, processor approval, settlement or funding.

## Key takeaways

- In sandbox, one documented test card simulates a transaction flagged for pending review; the page says this simulation is available only for the named Fraud Protection Advanced product. Separate card values simulate fraud or risk-threshold gateway rejection. These are test controls, not evidence that a merchant is enabled for the product or that the same behavior occurs with production payment methods.
- For the risk-threshold gateway rejection reason, the page requires at least Node server SDK `2.24.0`; otherwise the returned gateway-rejection status is `Unrecognized`. The exact card values, statuses, decisions, reasons and test nonces remain in the raw locators below.
- The sandbox Fraud Protection and Fraud Protection Advanced Dashboard is illustrative: settings cannot be changed there to reject transactions, so the page directs sandbox rejection tests to its defined card value. Its Kount and risk-threshold nonces work only under the stated tool or rule enablement conditions, and `fake-gateway-rejected-fraud-nonce` is deprecated.
- Sandbox and production accounts are not linked. Created objects, processing options and recurring-billing settings do not transfer; production has different login information, merchant ID and API keys. The guide recommends a dedicated API user rather than an individual user's credentials, with a non-employee-specific email and Account Admin permissions.
- Production merchant ID, public key and private key are placed in server-side Node.js configuration with `braintree.Environment.Production`; public and private keys are environment- and user-specific. The page says no client-side configuration update is needed because the client obtains its client token from the server. Production settings, including applicable recurring-billing plans or settings, must be recreated to mirror the tested sandbox configuration.
- Production checks use a small number of low-value sales for each intended payment-method type, submitted for settlement and followed through to bank deposit. Real payment methods are required: settled tests debit the associated payment method and incur fees. The page also warns that too many tests in a short period can trigger Premium Fraud Management Tools gateway rejection and says not to use more than two different card numbers from the same IP address.

> [!warning] Sandbox simulation is not production proof
> Sandbox settings and objects do not transfer, sandbox test values do not work in production, and this collected snapshot does not prove current product availability, merchant eligibility, successful production processing, settlement or deposit.

> [!warning] Production tests move real money and can affect fraud decisions
> The guide requires real production payment methods; settled tests debit the method and incur fees. Keep amounts reasonable and transaction count limited, and preserve the page's same-IP card-count warning.

## Detail locators

- Fraud Protection Advanced pending-review simulation and exact test card: `# Testing and Go Live`, lines 16-23.
- Fraud and risk-threshold rejection simulations, Node SDK minimum and fallback status: `# Testing and Go Live`, lines 24-42.
- Illustrative-only sandbox Dashboard and card-value testing direction: `NOTE`, lines 46-47.
- Conditional Kount and risk-threshold nonces plus deprecated fraud nonce: payment-method nonce table and `NOTIFICATION`, lines 49-60.
- Sandbox/production isolation and non-transfer warning: `## Go live > IMPORTANT`, lines 63-68.
- Dedicated API-user recommendation, permission qualification and production credential list: `### Create an API user` through `### Get production credentials`, lines 70-88.
- Production setting recreation, Node server environment switch and client-token boundary: `### Update production account settings` through `### Update live server configuration`, lines 91-112.
- Low-value production sales, settlement/deposit checks, real-payment debit and fee warning, and same-IP fraud-testing limit: `## Test transactions in production`, lines 117-125.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-fraud-protection-advanced]]
- Supporting basic fraud-tool route: [[braintree-fraud-tools]]
- Supporting server integration route: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/articles/guides/fraud-tools/premium/overview-2026-09-16|Braintree Premium Fraud Management Tools overview]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/guides/fraud-tools/premium/fraud-protection-advanced-2026-09-16|Braintree Fraud Protection Advanced article]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/guides/fraud-tools/basic/risk-threshold-rules-2026-09-16|Braintree risk-threshold rules article]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/control-panel/transactions/gateway-rejections-2026-09-16|Braintree gateway-rejections article]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/control-panel/important-gateway-credentials-2026-09-16|Braintree gateway-credentials article]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/control-panel/users-roles/managing-users-roles-2026-09-16|Braintree users-and-roles article]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/general/exceptions/node-2026-09-16|Braintree Node.js general exceptions reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Braintree Node.js transaction-sale reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/transactions/node-2026-09-16|Braintree Node.js transactions guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/payment-method-types-overview-2026-09-16|Braintree payment-method types overview]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/get-started/try-it-out-2026-09-16|Braintree sandbox-versus-production article]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/premium-fraud-management-tools/testing-go-live/node-2026-09-16|Braintree Premium Fraud Management Tools Testing and Go Live for Node.js]] - complete collected page covering conditional sandbox fraud simulations, production isolation and credentials, the Node server environment transition, client-token continuity and limited real-payment production checks
