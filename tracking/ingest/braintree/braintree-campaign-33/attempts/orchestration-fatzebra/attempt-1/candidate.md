---
title: "Braintree Orchestration: Fat Zebra Integration Guide"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/orchestration/fatzebra"
raw_files:
  - "braintree/docs/guides/orchestration/fatzebra-2026-09-16.md"
tags: [braintree, orchestration, fat-zebra, australia, new-zealand, card-payments]
---

## Overview

This Braintree-hosted integration guide describes using an existing Braintree integration to process transactions through PayPal Orchestration Platform with Fat Zebra. It applies only in Australia and New Zealand. Transaction operations stay on the Braintree platform, while settlement, chargebacks, reporting, and reconciliation are handled through the Fat Zebra portal. The guide is Braintree authority for this integration route, not independent Fat Zebra API authority, and the snapshot does not prove merchant enablement, transaction execution, settlement, or funding.

## Key takeaways

- Setup requires currency-specific Braintree merchant accounts plus a Fat Zebra account and environment-specific Fat Zebra API credentials. The guide directs merchants to share the required credentials securely with their Braintree AM or TAM; merchants without one are routed to Braintree client onboarding.
- Every Fat Zebra transaction requires `cardholderName`, supplied during payment-method tokenization. Wallet processing must be enabled in the Fat Zebra merchant account for Apple Pay or Google Pay; Braintree webhooks require integration-specific configuration through an AM or TAM; EFTPOS enablement is through Fat Zebra and is supported by Braintree only for single-step charge transactions.
- Supported central operations include single-step charge, standalone authorization followed by capture, full and partial capture, void, refund, verification, and selected SDK or GraphQL transaction operations. Exact capability, payment-method, field-mapping, response-code, and sandbox-test details remain in the raw locators below.
- Status is the operational source of truth. An authorization expires after five calendar days if not captured. Capture or refund API errors can remain `SETTLING` while Braintree reconciles the result, and the guide says not to ship or provide service until the status becomes `SETTLED`. A charge with no inline response can become `FAILED`, then later be reconciled to `SETTLED` with an automatic refund initiated.
- Do not create duplicate capture or refund retry loops when `success: true` is paired with `SETTLING`. After a timeout or uncertain create outcome, use Find or Search with the internal transaction reference before attempting another create; merchant-account-level retry for `FAILED` transactions requires TAM configuration.

## Detail locators

- **Feature matrix:** `Features` covers core lifecycle support, voids and refunds, payment instruments, data and fraud signals, and card verification.
- **Prerequisites and credentials:** `Before you begin`.
- **Transaction requirements and ownership:** `Transactions`; required fields and Braintree-to-Fat-Zebra mappings are under `Transaction creation`.
- **Vaulting and CVV behavior:** `Vaulted payment methods` and `Transaction object support` → `CVV handling`.
- **Statuses and reconciliation:** `Transaction status`, including `SETTLING status with HTTP errors` and `FAILED status during charge`.
- **Duplicate protection:** `Retries`.
- **Network tokens and diagnostics:** `Network tokens` and `Response codes`.
- **Sandbox behavior:** `Test cards`, including mapped card numbers, amount-based failure triggers, and Apple Pay test cryptograms.

## Related

- [[braintree]]
- [[braintree-payment-platform]]

## Related raw API references

The guide links to Braintree SDK and GraphQL transaction guides, transaction response documentation, and Fat Zebra documentation. Those linked targets were not read for this entry and are navigation only.

## Raw Sources

- [[raw/braintree/docs/guides/orchestration/fatzebra-2026-09-16|Fat Zebra Integration Guide (2026-09-16 snapshot)]]
