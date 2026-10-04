---
title: "Braintree Boleto Bancário"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/boleto-bancario"
raw_files:
  - "braintree/docs/guides/local-payment-methods/boleto-bancario-2026-09-16.md"
  - "braintree/graphql/integration_guides/non_instant_local_payments-2026-09-16.md"
  - "braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16.md"
tags: [braintree, local-payment-methods, boleto-bancario, brazil, non-instant-payments, webhooks]
---

## Overview

This collected Braintree developer guide describes Boleto Bancário as a cash-based Brazilian payment scheme that is created online and paid at a bank branch or an authorized processor. It is a non-instant method: the page gives the buyer up to three days to pay the voucher. The 2026-09-16 snapshot says Boleto Bancário is in limited release only for pilot merchants in Brazil, so it does not establish current availability, merchant approval, buyer eligibility or successful payment execution.

## Key takeaways

- The method-specific prerequisite is a valid PayPal business account that has been created, verified and linked in the Braintree Control Panel. The primary Boleto page directs merchants to the server-side GraphQL non-instant Local Payments guide to create a local payment transaction; it does not itself document a client SDK, client token, nonce or single-use-token flow. The supporting GraphQL guide describes payment-context creation, but its Boleto support statements conflict as preserved below.
- Boleto Bancário is non-instant. The guide says there is no capture call; Braintree associates a transaction for the merchant after receiving confirmation that the voucher was paid. Creating the local payment transaction or presenting an approval URL therefore is not evidence that the buyer paid, that a transaction was associated, or that settlement or merchant funding completed.
- A webhook integration is required. The page assigns webhooks the roles of confirming a successful payment and notifying the merchant that a voucher expired. The funded and expired payloads are examples; the example transaction's `settled` status does not prove that a particular payment settled or that funds reached the merchant's bank account.
- In Sandbox, the approval URL opens a modal that can simulate successful, expired and unapproved outcomes. The page says successful and expired simulations send a webhook in two to three minutes, while the payment context becomes settled-associated or expired as described. These simulator outcomes are Sandbox behavior, not Production timing or real-payment evidence.

## Evidence boundaries

> [!warning] Availability, GraphQL support and environment
> Preserve the primary page's exact pilot-only Brazil qualification. It directs Boleto transaction creation to GraphQL, and the supporting GraphQL guide names Boleto Bancário with BRL under Requirements; however, that guide's `currently supports` list contains Multibanco, OXXO and Trustly but omits Boleto. The same GraphQL page says every merchant may test the API in Sandbox while Production use requires account enablement. These same-date snapshots do not resolve Boleto's current Production support, account enablement or eligibility. The primary page's approval-URL modal and stated two-to-three-minute webhook behavior are explicitly Sandbox simulation.

> [!warning] Currency conflict
> The umbrella Local Payment Methods article says transactions are automatically presented in EUR, while the GraphQL guide requires the PayPal account currency to match the funding source and names BRL for Boleto. The primary Boleto page's funded-webhook example also carries BRL, but an example is not a universal runtime guarantee. Preserve the conflict; do not harmonize it into a single presentment rule without current method-specific authority.

> [!warning] Non-instant lifecycle
> Keep GraphQL payment-context creation, voucher presentation, buyer payment, Braintree's receipt of payment confirmation, transaction association, webhook delivery, example `settled` state, settlement and merchant funding as distinct evidence points. This page names funded and expired webhook events but does not establish bank funding for an individual payment.

## Detail locators

- Limited-release status and pilot-merchant Brazil scope: primary Boleto guide, `### Configuration > **AVAILABILITY**`, raw lines 20-21.
- Cash-based method identity, in-person payment locations and up-to-three-day non-instant timing: primary Boleto guide, `### Configuration`, raw line 23.
- Linked, verified PayPal business-account prerequisite: primary Boleto guide, `### Configuration`, raw line 26.
- Primary page's server-side GraphQL transaction-creation route: primary Boleto guide, `### Server Side requests with GraphQL`, raw lines 29-33.
- No-capture behavior and confirmation-dependent transaction association: primary Boleto guide, `### Capturing Non-Instant Transaction`, raw lines 36-38.
- Sandbox approval-URL modal, simulated outcomes, webhook timing and payment-context results: primary Boleto guide, `### Capturing Non-Instant Transaction > **NOTE**`, raw lines 39-43.
- Required webhook roles: primary Boleto guide, `### Configure webhooks`, raw lines 48-50.
- Example funded and expired payload fields, including example BRL currency and `settled` status: primary Boleto guide, `### Configure webhooks`, raw lines 52-79.
- Boleto/BRL currency requirement, Sandbox testing and Production-enablement qualification: GraphQL non-instant guide, `## Requirements`, raw lines 20-23.
- Payment-context creation description and current-support list that omits Boleto: GraphQL non-instant guide, `## Creating Non-Instant Local Payment Contexts`, raw lines 26-35.
- Umbrella statement that Local Payment Method transactions are automatically presented in EUR: Local Payment Methods article, `## Availability`, raw line 21.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Article-level Local Payment Methods owner: [[source-braintree-payment-methods-local-payment-methods]]

## Related raw API references

The following collected pages were not used as factual authority for this source entry; they are exact-file navigation for follow-on implementation work:

- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Braintree webhooks overview]]
- [[raw/braintree/docs/reference/general/webhooks/local-payment-methods/node-2026-09-16|Node.js Local Payment Method webhook reference]]

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/boleto-bancario-2026-09-16|Braintree Boleto Bancário guide]] - fully read primary pinned snapshot covering method identity, pilot applicability, PayPal setup, GraphQL routing, non-instant transaction association, Sandbox simulation and webhook outcomes
- [[raw/braintree/graphql/integration_guides/non_instant_local_payments-2026-09-16|Braintree GraphQL non-instant Local Payment Methods guide]] - fully read supporting snapshot covering requirements, environment qualification, payment-context creation, the captured current-support list and non-instant lifecycle
- [[raw/braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16|Braintree Local Payment Methods article]] - fully read supporting snapshot for the umbrella EUR presentment statement and article-level method context
