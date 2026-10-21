---
title: "Webhook structure and types for payouts | Adyen Docs"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/webhook-types"
raw_files:
  - "adyen/docs/payouts/payout-service/webhook-types/2026-09-15.md"
tags: [adyen, payouts, payout-service, webhooks, transfers]
---

## Overview

This Payout Service guide, captured 2026-09-15, describes the general webhook envelope and the configuration and Transfer event types shown for account holders, balance accounts, sweeps, internal transfers, and third-party bank payouts. It is a type and routing reference, not evidence that a particular webhook was subscribed to or delivered, or that a transfer settled or reached a bank. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The general body has `data`, `environment` (`test` or `live`), and `type`. The `data` shape varies by type; some types also have `data.status`. The account-holder creation JSON is a test example, not evidence of a real account or delivered notification (raw lines 26–38, 42–78).
- Configuration types listed here report successful creation/update of account holders and balance accounts, and creation/deletion/update of balance-account sweeps. The section's introductory sentence also mentions payment instruments, but this captured table does not enumerate payment-instrument types (raw lines 80–92).
- `balancePlatform.transfer.created` represents creation of a request to credit or deduct funds from a platform balance account, with the triggering event in its content; `balancePlatform.transfer.updated` marks a request status change. These event labels alone do not establish funds movement or beneficiary-bank receipt (raw lines 70–78, 94–101).
- For the Transfer webhooks in this guide, identify internal transfer with `category=internal`, `type=internalTransfer`, and counterparty `balanceAccountId`; a third-party payout to a bank account uses `category=bank`, `type=bankTransfer`, and counterparty `bankAccount`. The table does not specify further status values or a settlement timeline (raw lines 103–109).

## Detail locators

- Webhook envelope and test example: raw lines 26–68.
- General event distinctions and `data.status` qualifier: raw lines 70–78.
- Configuration type table: raw lines 80–92.
- Transfer types and internal-versus-bank classification: raw lines 94–109.

## Related

- [[adyen-webhooks]]
- [[adyen-platform-internal-transfers]]
- [[source-adyen-docs-payouts-payout-service-internal-fund-transfers-internal-transfer-webhooks]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/webhook-types/2026-09-15|Pinned Payout Service webhook types guide]]
