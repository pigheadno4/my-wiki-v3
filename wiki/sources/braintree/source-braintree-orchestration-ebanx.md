---
title: "Braintree EBANX Orchestration Integration Guide"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/orchestration/ebanx"
raw_files:
  - "braintree/docs/guides/orchestration/ebanx-2026-09-16.md"
tags: [braintree, orchestration, ebanx, card-processing, transactions]
---

## Overview

This 2026-09-16 snapshot is a Braintree-hosted integration guide for processing card transactions through EBANX with the PayPal Payment Orchestration platform while merchants continue to create and manage the transactions through Braintree. It is not independent EBANX API authority and does not establish current market availability, merchant eligibility, successful processing, settlement or funding.

The guide's central boundary is operational: use the Braintree SDK or GraphQL API for transaction operations. It warns that operating directly with EBANX can create discrepancies and synchronization errors. This is an orchestration route, not documentation of Braintree Forward API request construction.

## Key takeaways

- Setup is required on both sides. The Braintree side needs currency-specific merchant accounts; the EBANX side needs an account and separate sandbox and production integration keys. The guide directs the merchant to share the applicable EBANX key securely with Braintree through its AM or TAM/onboarding route. A collected page or configured sandbox key does not establish production enablement.
- Customer creation is mandatory for this integration. Full name and email are required for EBANX transactions even where Braintree does not generally require them; missing email or full name is documented to produce `PROCESSOR_DECLINED`. Country, payment-method and merchant-configuration conditions—including tax identifiers, address data, debit enablement, 3DS, dual-step processing and partial capture—remain qualified by the raw sections below.
- The snapshot contains an unresolved Nigeria partial-capture conflict: the feature matrix at raw line 39 lists Nigeria among markets with conditional partial-capture support, while the country table at raw line 457 says partial capture is not supported there. The snapshot does not reconcile these statements; do not represent Nigeria partial capture as available without separate current provider/account confirmation.
- The guide supports Braintree SDK or GraphQL transaction creation and management rather than a separate EBANX-direct operation path. Routine request fields, EBANX mappings, supported transaction operations, response codes and diagnostic fields are retained in the raw locators instead of reproduced exhaustively here.
- Lifecycle statuses require status-aware fulfillment and retry handling. Authorizations must be captured within five days. A capture or refund API error can remain `SETTLING` while Braintree reconciles with EBANX; the guide says not to ship or provide service until `SETTLED` and not to build duplicate capture/refund retry loops when `success: true` accompanies `SETTLING`. A charge that is `FAILED` after no inline response can later reconcile to `SETTLED` and trigger an automatic refund, so the initial failure is not, under that stated condition, proof that no processing occurred.

> [!warning] Keep all transaction operations on Braintree
> For this integration, the guide explicitly directs merchants to use Braintree for transaction operations. Do not reinterpret the linked EBANX setup material as authority to bypass Braintree for the orchestrated lifecycle.

> [!warning] Fulfill only on the documented final status
> Do not treat `success: true` with `SETTLING`, an API error, or the initial no-inline-response `FAILED` state as final settlement evidence. Follow the Braintree status and reconciliation path and confirm `SETTLED` before fulfillment. None of these status examples establish bank funding.

## Detail locators

- Integration identity, supported-market list and Braintree-only transaction-operation warning: introduction, raw lines 14-20.
- Capability matrix for charge, authorization/capture, void/refund, payment instruments, fraud signals and verification: `## Features`, raw lines 21-108. For the unresolved Nigeria partial-capture conflict, compare the conditional-support statement at raw line 39 with the not-supported statement at raw line 457.
- Braintree merchant-account setup, EBANX account and environment-specific keys, secure key handoff, and refund/CVV/debit/dual-step prerequisites: `## Before you begin`, raw lines 111-129.
- Braintree SDK/GraphQL operation route and required transaction fields: `## Transactions` through `### Fields that Braintree passes to EBANX`, raw lines 132-190.
- Mandatory customer creation, vaulted-method orientation, tax-identifier handling and supported transaction operations: raw lines 193-255.
- EBANX-to-Braintree status mapping, reconciliation behavior, fulfillment warning and retry guidance: `## Transaction status mapping` through `## Retries`, raw lines 258-305.
- Network-token options and enablement boundaries: `## Network tokens`, raw lines 307-314.
- Response-code mappings and conditionally present NRC/MAC diagnostics: `## Response codes`, raw lines 316-393.
- Sandbox-only card mappings and outcomes: `## Test cards`, raw lines 396-432.
- Country-specific requirements and limitations: raw lines 435-471.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Transaction API boundary: [[braintree-server-sdk]]
- Currency-specific merchant-account context: [[braintree-currencies]]

## Related raw API references

- [[raw/braintree/docs/guides/orchestration/overview-2026-09-16|Braintree Payment Orchestration overview]] - linked navigation-only overview; not read as factual evidence for this source
- [[raw/braintree/docs/guides/transactions/node-2026-09-16|Braintree transactions guide (Node.js)]] - linked navigation-only SDK transaction route; not read as factual evidence for this source
- [[raw/braintree/graphql/guides/transactions-2026-09-16|Braintree GraphQL transactions guide]] - linked navigation-only GraphQL transaction route; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/orchestration/ebanx-2026-09-16|Braintree EBANX Integration Guide]] - fully read primary snapshot covering setup, Braintree-routed operations, fields, supported capabilities, lifecycle mapping, reconciliation, retries, diagnostics, testing and country qualifications
