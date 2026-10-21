---
title: "Adyen Marketplace approve or cancel transfers"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/internal-fund-transfers/approve-cancel-transfers"
raw_files:
  - "adyen/docs/marketplaces/internal-fund-transfers/approve-cancel-transfers/2026-09-15.md"
tags: [adyen, marketplaces, platforms, internal-transfers, transfer-review]
---

## Overview

This 2020-modified Marketplace guide, captured 2026-09-15, describes an optional additional-review gate for a transfer initiated with a `review` object in POST `/transfers`. A designated team member approves or cancels the pending request before Adyen processes it. Approval authorizes the request and lets processing continue; cancellation or no decision within 30 days fails the request. This guide is routed from the internal-fund-transfer section, but its detailed webhook JSON examples are outgoing `category: bank` / `type: bankTransfer`; their balances and event sequence are not evidence of a completed internal balance-account transfer. [[adyen]] [[adyen-platform-internal-transfers]]

## Key takeaways

- Prerequisites: assign the web service API key the **TransferService Approval role** and subscribe to **Transfer Webhooks**. The guide says the platform chooses permitted team reviewers by assigning the required API role in Customer Area (raw lines 19–30). Initiation includes the `review` object; the request remains pending until review (lines 38–48).
- POST `/transfers/approve` or `/transfers/cancel` with an array of one or more `transferIds`, maximum 500 per request. The examples use the TEST Balance Platform API `/btl/v4` endpoint; SDK snippets show idempotency-key options. A successful request returns HTTP 200, while status/outcome details come from transfer webhooks (raw lines 52–75, 77–259, 261–287, 289–468).
- An approval authorizes the transfer request and Adyen continues processing. Cancellation fails it and stops further processing; no reviewer action within 30 days of initiation also fails it. Do not equate approval, HTTP 200, or an `authorised` webhook with a booked internal transfer or external bank receipt (raw lines 40–48, 259, 468, 565–571).
- `balancePlatform.transfer.created` with `status: received`, `reason: pending`, and `review.numberOfApprovalsRequired: 1` identifies the illustrated pending review. `balancePlatform.transfer.updated` reports the illustrated approved `authorised` / `approved` or canceled `cancelled` / `unknown` states. The guide also says webhooks report expiry after 30 days (raw lines 470–495, 565–571, 653–660).
- **Scope warning:** the three sample webhook payloads use `category: bank`, `categoryData.type: bankTransfer`, `type: bankTransfer`, `direction: outgoing`, and TEST environment. Their EUR 10000 amounts, reserved/received mutations, account IDs and statuses illustrate review reporting for bank transfers, not the internal-transfer two-leg booking sequence; consult the separate internal-transfer webhook guide for that flow (raw lines 501–562, 577–650, 666–736).

## Detail locators

- Review rationale, roles, trigger, decisions and 30-day deadline: raw lines 17–50. Approval request, TEST/SDK examples and HTTP response: lines 52–259. Cancellation request and response: lines 261–468.
- Webhook event types and pending/approved/canceled field combinations: lines 470–495, 563–571, 653–660. Bank-scoped TEST JSON examples: lines 501–562, 577–650, 666–736.

## Related

- [[adyen]] — provider.
- [[adyen-platform-internal-transfers]] — internal balance-account transfer concept and evidence boundary.
- [[source-adyen-docs-marketplaces-internal-fund-transfers-scheduled-fund-transfers]] — scheduled internal transfers.
- [[source-adyen-docs-platforms-internal-fund-transfers-approve-cancel-transfers]] — separate Platforms-path review guide.

## Raw Sources

- [[raw/adyen/docs/marketplaces/internal-fund-transfers/approve-cancel-transfers/2026-09-15|Marketplace approve or cancel transfers — 2026-09-15 snapshot]]
