---
title: "Braintree Orchestration: FlexFactor Integration Guide"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/orchestration/flexfactor"
raw_files:
  - "braintree/docs/guides/orchestration/flexfactor-2026-09-16.md"
tags: [braintree, orchestration, flexfactor, card-payments, revenue-recovery]
---

## Overview

This Braintree-hosted guide describes integrating FlexFactor with Braintree through the PayPal Orchestration Platform. It says FlexFactor's real-time decision engine evaluates a transaction after failure on PayPal Enterprise and can recover revenue from false declines. The documented integration supports Visa and Mastercard credit or debit cards. This is Braintree authority for this orchestration route, not independent FlexFactor provider authority, and the snapshot does not prove merchant enablement, transaction execution, recovery, settlement, dispute outcome, or funding.

## Key takeaways

- Each merchant needs a FlexFactor account, FlexFactor credentials shared securely with Braintree through an AM or TAM, and currency-specific merchant accounts. Merchants without a dedicated AM or TAM are directed to Braintree client onboarding.
- The guide describes a direct Braintree connection that routes transactions to FlexFactor. The merchant makes the initial transaction attempt and decides when to trigger a retry to FlexFactor; this merchant-driven rule is distinct from Braintree's automatic retries for the specific capture, dual-step charge, and refund HTTP-error states documented in the status table. This orchestration route is not automatically the Braintree Forward API, and Forward API-only limitations must not be imported into it.
- The supported core path is dual-step authorization and capture; single-step charge is marked unsupported. A standalone authorization must be captured within seven days, while the status mapping says the FlexFactor-configured authorization window can range from five minutes to seven days. Full capture is supported, but partial capture, capture above the authorized amount, and authorization adjustment are not.
- For capture or dual-step charge HTTP 4xx/5xx outcomes after successful authorization, the Braintree status remains `SETTLING` while Braintree automatically retries FlexFactor until a final `SETTLED` or `SETTLEMENT_DECLINED` status. Do not ship goods or treat the transaction as successful before `SETTLED`. Refund HTTP 4xx/5xx follows the same automatic-retry and final-status pattern.
- Full and partial refunds are supported, but refunds cannot exceed the settled amount and partial refunds are limited to 60% of the original order price. Full voids before settlement are supported; settled transactions require a refund. FlexFactor handles disputes and chargebacks for this integration.

## Detail locators

- **Supported lifecycle and methods:** `Features` → `Core transaction lifecycle`, `Voids and refunds`, and `Payment instruments and methods`.
- **Data, fraud, and verification support:** `Features` → `Data, descriptors, and fraud signals` and `Verifications`.
- **Account, credentials, and merchant-account prerequisites:** `Before you begin`.
- **Connection and merchant-triggered retry:** `FlexFactor integration`.
- **Status ownership, conditional automatic retries, and fulfillment warnings:** `Transaction status mapping`.
- **Required transaction fields:** `Required fields`.
- **Captured sandbox card behavior:** `Testing`; these examples do not establish production eligibility or successful execution.
- **Dispute ownership:** `Disputes`.

## Related

- [[braintree]]
- [[braintree-orchestration]]

## Related raw API references

The guide links to Braintree SDK and GraphQL transaction-processing references and to FlexFactor credential documentation. Those linked targets were not read for this entry and are navigation only.

## Raw Sources

- [[raw/braintree/docs/guides/orchestration/flexfactor-2026-09-16|FlexFactor Integration Guide (2026-09-16 snapshot)]]
