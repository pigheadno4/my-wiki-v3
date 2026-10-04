---
title: "Braintree PayPal Orchestration Adyen Integration Guide"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/orchestration/adyen"
raw_files:
  - "braintree/docs/guides/orchestration/adyen-2026-09-16.md"
tags: [braintree, paypal-orchestration, adyen, authorization, capture, transaction-lifecycle]
---

## Overview

This collected Braintree guide documents an Adyen processor connection under the PayPal Orchestration platform. It says merchants can keep their existing Braintree integration and perform transaction operations through Braintree, while settlement, chargebacks, reporting and reconciliation are handled through the merchant's Adyen portal. This is an orchestration transaction-processing guide, not a Forward API destination example.

The page was collected on 2026-09-16. It is Braintree-hosted integration documentation, not independent Adyen API authority and not proof of current country or account eligibility, processor-connection enablement, transaction success, settlement or funding.

## Key takeaways

- The documented central path is Braintree transaction operations through an Adyen processor connection. The page warns that performing operations directly with Adyen can cause synchronization issues and data inconsistencies.
- The core flow uses authorization followed by capture: the capability table marks single-step or orchestrated charge unsupported, standalone authorization supported subject to the processor-defined expiry window, and full and partial capture supported. The exact capability, void, refund, payment-method and verification matrices remain in the raw page.
- Setup requires currency-specific Braintree merchant accounts, an Adyen account for each merchant, Braintree AM/TAM help configuring the processor connection, and an Adyen API user with the `API PCI Payments` role. The guide supports only currencies with zero or two decimal places; three-decimal currencies are stated to return an error.
- The page lists cards as supported, with Apple Pay and Google Pay limited to authorization, and lists Venmo and PayPal as unsupported for this integration. These are snapshot-scoped integration statements, not current Adyen-wide capability claims.
- Capture and refund begin in `SETTLING` and await Adyen webhook outcomes. Fulfillment must wait for `SETTLED`; `success: true` with `SETTLING` must not trigger duplicate capture or refund retries. After a timeout or uncertain creation result, the guide says to use Braintree Find or Search with the internal transaction reference before attempting another create.
- Country scope is internally inconsistent: the introduction says the connection supports transactions in **most** countries Adyen supports, while `## Supported countries` says it supports **all** countries Adyen supports. Do not resolve that conflict from this snapshot; confirm current merchant, country and currency eligibility.

> [!warning] Keep transaction control on Braintree
> For this documented connection, perform transaction operations through Braintree. Direct Adyen operations can desynchronize the systems. The assignment of post-processing to the Adyen portal does not establish that settlement completed or that funds arrived.

> [!warning] Treat `SETTLING` as pending
> A successful capture or refund call can still be awaiting an Adyen webhook and can later become `SETTLEMENT_DECLINED`. Do not fulfill before `SETTLED`, and do not create a duplicate capture, refund or transaction solely because the first result is pending or timed out.

> [!warning] Orchestration is not automatically Forward API
> This page documents Braintree transaction operations and status synchronization for an Adyen processor connection. Do not transfer Forward API production-eligibility, transformation, forwarding or destination-example limits into these operations unless separate evidence explicitly connects them.

## Detail locators

- Integration identity, existing-Braintree route, Adyen-portal post-processing and country wording: introduction below `# Adyen Integration Guide`, raw lines 14-18.
- Core authorization/capture support and limitations: `### Core transaction lifecycle`, raw lines 24-37.
- Void and refund support matrix: `### Voids and refunds`, raw lines 41-55.
- Cards, wallet authorization-only limits and unsupported Venmo/PayPal: `### Payment instruments and methods`, raw lines 59-72.
- AVS/CVV, descriptors, network tokens, L2/L3 data and 3DS qualifications: `### Data, descriptors, and fraud signals`, raw lines 75-87.
- Verification support: `### Verifications`, raw lines 90-100.
- Braintree merchant-account, Adyen account, processor-connection and `API PCI Payments` role prerequisites; CVV, address, webhook and decimal-currency conditions: `## Before you begin`, raw lines 103-117.
- Transaction creation fields and currency qualification: `### Transaction creation`, raw lines 132-143.
- Operation-specific Braintree-to-Adyen field mappings: `### Fields that Braintree passes to Adyen`, raw lines 144-198.
- Customer, tokenization and Vault navigation: `### Customer creation` through `### Vaulted payment methods`, raw lines 201-213.
- Supported Braintree transaction operations and GraphQL reverse behavior: `#### Supported transaction operations`, raw lines 221-242.
- L2/L3 inclusion conditions and excluded operations: `## L2/L3 enhanced data support`, raw lines 248-252.
- Adyen-response to Braintree-status mapping, asynchronous `SETTLING` behavior and fulfillment warning: `## Transaction statuses`, raw lines 255-287.
- Pending-result and timeout retry controls: `## Retries`, raw lines 290-294.
- Network-token choices and enablement route: `## Network token support`, raw lines 297-305.
- Limited response-code display, pass-through fields and exact error/refusal mappings: `## Response codes`, raw lines 308-434.
- Sandbox card remapping and success/failure fixtures: `## Test cards`, raw lines 437-463.
- Conflicting all-country wording and repeated decimal-currency limit: `## Supported countries`, raw lines 466-470.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-orchestration]]
- General gateway-operation context: [[braintree-server-sdk]]
- Distinct outbound request-construction route: [[braintree-forward-api]]

## Related raw API references

- [[raw/braintree/docs/guides/orchestration/overview-2026-09-16|Braintree Orchestration overview]] - navigation-only sibling overview; not read as factual evidence for this source
- [[raw/braintree/docs/guides/transactions/node-2026-09-16|Braintree Node.js transactions guide]] - navigation-only general transaction route; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/orchestration/adyen-2026-09-16|Braintree PayPal Orchestration Adyen integration guide]] - complete collected page covering identity, processor setup, operation support, field mappings, status synchronization, retries, response mappings and sandbox testing
