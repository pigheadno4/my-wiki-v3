---
title: "Braintree Boleto Bancário"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/boleto-bancario"
raw_files:
  - "braintree/docs/guides/local-payment-methods/boleto-bancario-2026-09-16.md"
tags: [braintree, local-payment-methods, boleto-bancario, brazil, non-instant-payments, webhooks]
---

## Overview

This collected Braintree developer guide describes Boleto Bancário as a cash-based Brazilian payment scheme that is created online and paid at a bank branch or an authorized processor. It is a non-instant method: the page gives the buyer up to three days to pay the voucher. The 2026-09-16 snapshot says Boleto Bancário is in limited release only for pilot merchants in Brazil, so it does not establish current availability, merchant approval, buyer eligibility or successful payment execution.

## Key takeaways

- The method-specific prerequisite is a valid PayPal business account that has been created, verified and linked in the Braintree Control Panel. The page routes transaction creation to a server-side GraphQL integration; it does not document a client SDK, client token, nonce or single-use-token flow.
- Boleto Bancário is non-instant. The guide says there is no capture call; Braintree associates a transaction for the merchant after receiving confirmation that the voucher was paid. Creating the local payment transaction or presenting an approval URL therefore is not evidence that the buyer paid, that a transaction was associated, or that settlement or merchant funding completed.
- A webhook integration is required. The page assigns webhooks the roles of confirming a successful payment and notifying the merchant that a voucher expired. The funded and expired payloads are examples; the example transaction's `settled` status does not prove that a particular payment settled or that funds reached the merchant's bank account.
- In Sandbox, the approval URL opens a modal that can simulate successful, expired and unapproved outcomes. The page says successful and expired simulations send a webhook in two to three minutes, while the payment context becomes settled-associated or expired as described. These simulator outcomes are Sandbox behavior, not Production timing or real-payment evidence.

## Evidence boundaries

> [!warning] Availability and environment
> Preserve the page's exact pilot-only Brazil qualification. This collected snapshot does not prove present release status, account enablement or Production acceptance. The approval-URL modal and stated two-to-three-minute webhook behavior are explicitly Sandbox simulation.

> [!warning] Non-instant lifecycle
> Keep GraphQL transaction creation, voucher presentation, buyer payment, Braintree's receipt of payment confirmation, transaction association, webhook delivery, example `settled` state, settlement and merchant funding as distinct evidence points. This page names funded and expired webhook events but does not establish bank funding for an individual payment.

## Detail locators

- Limited-release status and pilot-merchant Brazil scope: `### Configuration > **AVAILABILITY**`, raw lines 20-21.
- Cash-based method identity, in-person payment locations and up-to-three-day non-instant timing: `### Configuration`, raw line 23.
- Linked, verified PayPal business-account prerequisite: `### Configuration`, raw line 26.
- Server-side GraphQL transaction-creation route: `### Server Side requests with GraphQL`, raw lines 29-33.
- No-capture behavior and confirmation-dependent transaction association: `### Capturing Non-Instant Transaction`, raw lines 36-38.
- Sandbox approval-URL modal, simulated outcomes, webhook timing and payment-context results: `### Capturing Non-Instant Transaction > **NOTE**`, raw lines 39-43.
- Required webhook roles: `### Configure webhooks`, raw lines 48-50.
- Example funded and expired payload fields: `### Configure webhooks`, raw lines 52-79.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Article-level Local Payment Methods owner: [[source-braintree-payment-methods-local-payment-methods]]

## Related raw API references

The following collected pages were not used as factual authority for this source entry; they are exact-file navigation for follow-on implementation work:

- [[raw/braintree/graphql/integration_guides/non_instant_local_payments-2026-09-16|Braintree GraphQL non-instant Local Payment Methods integration guide]]
- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Braintree webhooks overview]]
- [[raw/braintree/docs/reference/general/webhooks/local-payment-methods/node-2026-09-16|Node.js Local Payment Method webhook reference]]

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/boleto-bancario-2026-09-16|Braintree Boleto Bancário guide]] - fully read pinned website snapshot covering method identity, pilot applicability, PayPal setup, GraphQL routing, non-instant transaction association, Sandbox simulation and webhook outcomes
