---
title: "Adyen Payout Service: return an internal push transfer"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/internal-fund-transfers/return-transfers"
raw_files:
  - "adyen/docs/payouts/payout-service/internal-fund-transfers/return-transfers/2026-09-15.md"
tags: [adyen, payout-service, internal-transfers, returns, balance-accounts]
---

## Overview

This Payout Service-path guide (last modified 2020-09-11; captured 2026-09-15) describes returning funds from a destination balance account to the source balance account of an **original internal push transfer**. The return uses that incoming transfer's ID and is handled as a modification of the same transfer, rather than a newly initiated internal transfer. It does not describe an external bank payout or a general reversal for pull transfers. See [[adyen]] and [[adyen-platform-internal-transfers]].

## Key takeaways

- **Prerequisites and direction:** The guide requires an accepting server with the Transfer webhook added, Support enablement of transfers for the balance account from which funds are returned, and a Transfers API credential with **TransferService Webservice Initiate**. If the two balance accounts belong to different account holders, the holder of the account returning funds needs `sendToBalanceAccount`; the original sender's holder needs `receiveFromBalanceAccount`. These are directional gates, not interchangeable capabilities.
- **Return request:** POST `/transfers/{transferId}/returns` uses the original **incoming** transfer ID from the webhook. The request's `amount` supplies currency and value matching the original transfer; `reference` is an optional unique return reference in the source table. The EUR 100 test example and language-library samples illustrate the request rather than proving a live movement; consult raw lines 43-290 for exact request shape and versions.
- **Response and tracking:** The response has its own return-request `id`, a `transferId` pointing back to the original incoming transfer, and a status. The guide shows `authorised` and notes that `Declined` can indicate a wrong transfer ID in the URL. It directs operators to Transfer webhooks for subsequent return status **and failure** and to Customer Area for viewing the return. An authorised response alone is not booked-return or recipient-balance evidence.

## Detail locators

- Scope, push-only restriction and role/capability/webhook prerequisites: pinned raw lines 15-38.
- Endpoint, matching amount, optional reference and TEST examples with SDK versions: pinned raw lines 39-290.
- Return-request versus original-transfer IDs, decline clue and webhook follow-up: pinned raw lines 293-314.

## Related

- [[adyen-platform-internal-transfers]] — main internal balance-account movement concept and reciprocal source route.
- [[source-adyen-docs-payouts-payout-service-internal-fund-transfers-internal-transfer-webhooks]] — Payout Service-path event detail for internal legs and nested returns.
- [[source-adyen-docs-platforms-internal-fund-transfers-return-transfers]] — separately captured Platforms-path return guide.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/internal-fund-transfers/return-transfers/2026-09-15|Payout Service internal push-transfer return guide, captured 2026-09-15]]
