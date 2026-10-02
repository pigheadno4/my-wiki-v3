---
title: "Braintree Auth Testing and Go Live (Node.js)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-auth/testing-go-live/node"
raw_files:
  - "braintree/docs/guides/braintree-auth/testing-go-live/node-2026-09-16.md"
tags: [braintree, braintree-auth, node-js, oauth, sandbox, production]
---

## Overview

This collected Braintree Auth Node.js guide covers Merchant Connect sandbox testing, test authorization codes, the separate production test path, and checkout-integration prerequisites for platforms enabling payments for connected merchants. Braintree Auth is marked closed beta in this snapshot; collection and a successful Connect flow do not establish current availability, production payment acceptance, or successful underwriting.

## Key takeaways

- Sandbox Merchant Connect testing uses the provided sandbox OAuth client ID and client secret on the server and a sandbox client-side environment. The signup form resembles production, but the guide says no external credit checking or identity verification occurs in sandbox; its dummy-data exceptions and account-reuse instructions remain in the raw detail locator.
- The guide supplies test authorization codes for exercising the OAuth redirect and predetermined sandbox responses. A token obtained with `fake-valid-auth-code` acts on behalf of the platform's own merchant rather than the merchant that would authorize the application in a full OAuth flow; the default `read_write` scope and scope-qualified test-code forms are documented in the raw.
- Production testing switches both the server OAuth credentials and client-side environment to production. Connecting the production account that created the OAuth application can complete the Connect flow, but the guide warns that test transactions may be unavailable if that account has not been underwritten for payments. A new-account Connect test requires accurate personal and business information and runs a credit check on the business owner.
- For a platform enabling payments, the guide calls for the full Braintree feature set and routes to the Client SDK. Premium Fraud Management Tools are disabled by default for Braintree Auth; when a connected merchant requires them, the platform must collect and pass device data on the merchant's behalf and keep advanced fraud checking enabled.
- For PayPal Vault transactions, the guide requires device-data collection and forwarding at checkout and on any page where a Vault token can complete a transaction. It separately provides a transaction-field checklist covering platform attribution, per-merchant order-ID uniqueness, conditionally collected billing-address data, and CVV; use the exact raw locator for those conditional details rather than treating this entry as a transaction-sale schema.

> [!warning] Sandbox and Connect are not production acceptance
> Sandbox performs no external credit check or identity verification. In production, an OAuth connection can work while test transactions remain unavailable because the account may not be underwritten; a new-account Connect test requires accurate identity and business data and a business-owner credit check.

> [!warning] Closed-beta and checkout scope
> This 2026-09-16 snapshot labels Braintree Auth closed beta. Its checkout checklist is specifically for platforms enabling payments for connected merchants and does not by itself prove present eligibility, payment-method enablement, transaction approval, settlement, or live acceptance.

## Detail locators

- Closed-beta availability and interest route: `# Testing and Go Live > AVAILABILITY`, lines 17-18.
- Sandbox OAuth/client environment, production-like signup form, missing external checks, dummy-data exceptions, and connected-account reuse: `## OAuth sandbox testing > ### Signup flow`, lines 24-41.
- Test authorization-code behavior, predetermined outcomes, own-merchant token scope, callback/Promise examples, and scope-qualified test codes: `## OAuth sandbox testing > ### Redirect and authorization grant` through `### Promise`, lines 44-91.
- Production credentials/environment, existing-account underwriting limit, new-account accurate-data requirement, and business-owner credit check: `## OAuth production testing`, lines 94-102.
- Payment-enablement scope, Client SDK route, Premium Fraud Management Tools default and device-data requirements, and PayPal Vault device-data boundary: `## Checkout integration` through `### PayPal`, lines 103-120.
- Platform attribution, order-ID uniqueness, billing-address and CVV checklist with its stated conditions: `## Checkout integration > ### Transaction fields`, lines 121-129.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-auth]]
- Product-orientation route: [[braintree-payment-platform]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-auth/reference/node-2026-09-16|Braintree Auth Node.js guide reference]] - navigation-only route for signup fields and related Auth reference details; not used as factual evidence here
- [[raw/braintree/docs/guides/premium-fraud-management-tools/server-side/node-2026-09-16|Braintree Node.js Premium Fraud Management Tools server-side guide]] - navigation-only route for passing device data and advanced-fraud-checking options; not used as factual evidence here
- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Braintree Node.js transaction-sale reference]] - navigation-only route for transaction request details; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/guides/braintree-auth/testing-go-live/node-2026-09-16|Braintree Auth Testing and Go Live for Node.js]] - complete collected guide covering sandbox and production OAuth testing boundaries, test authorization codes, underwriting and credit-check cautions, and payment-enablement checklist routes
