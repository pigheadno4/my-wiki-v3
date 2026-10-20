---
title: "Adyen Issuing recurring top-up webhooks"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/add-manage-funds/top-ups/top-up-webhooks"
raw_files:
  - "adyen/docs/issuing/add-manage-funds/top-ups/top-up-webhooks/2026-09-15.md"
tags: [adyen, issuing, top-ups, direct-debits, webhooks, balance-accounts]
---

## Overview

This Issuing-path page, captured 2026-09-15 and marked modified 2020-09-11, maps **recurring Top-up API configuration changes** and their triggered **direct-debit top-ups** to Configuration, Transfer, and Transaction webhooks. A successful Top-up API response does not itself confirm that a recurring top-up was created, updated, or deleted. [[adyen-issuing]]

## Key takeaways

- The guide requires an Adyen Issuing integration and a server able to receive and accept webhooks. Subscribe to Configuration webhooks for successful recurring top-up creation, update, and deletion; their payload identifies the balance account (`data.accountId`), configuration (`data.webhookTopUpConfiguration`), and event `type` (raw lines 19–49).
- For a triggered direct debit, `balancePlatform.transfer.created` reports initiation and `balancePlatform.transfer.updated` reports status changes. The page labels the relevant transfer `category=bank` and `type=bankDirectDebit`; Transaction webhooks track the resulting movement of funds. `balancePlatform.transaction.created` is sent when funds are credited to the balance account, whereas Transfer webhooks cover status changes (raw lines 23, 30–32, 164–178, 706–712).
- An accepted initial request can still fail during processing. The guide supplies `rejected` (internal validation or transaction-rule failure) and `returned` (funds sent back after reaching a destination bank) examples. Inspect the actual status and accounting events rather than treating `created`, `received`, `authorised`, or an example `booked` event as irrevocable funding (raw lines 184–433, 435–439, 573–704).
- **Direction/example conflict:** prose calls `transfer.created` an *outgoing* direct-debit request from a balance account (raw line 168). The initiated/authorised examples show `direction: outgoing` (raw lines 216, 291), while the booked example shows `direction: incoming` (line 380); failure examples also show incoming direction and include a payment-instrument field (lines 492, 553–565, 625, 686–698). The identification heading calls these payout-related events even though this is a top-up guide (line 173). Do not derive a stable money-flow direction or Issuing-card relationship from these samples alone.

## Detail locators

- Configuration event names, payload fields, and three test-environment example notifications: raw lines 35–162. Example IDs, statuses, timestamps and amounts are illustrative.
- Transfer identification fields and received/authorised/booked test examples, including balance mutations and direct-debit metadata: raw lines 164–433.
- Rejected and returned transfer samples, including later reversal-style accounting rows: raw lines 435–704.
- Credited-balance-account Transaction webhook and sample `booked` transaction: raw lines 706–750.

## Related

- [[adyen]] — provider context.

- [[adyen-issuing]] — Issuing model and sources.
- [[source-adyen-docs-issuing-add-manage-funds]] — funding-route overview.
- [[source-adyen-docs-platforms-top-up-balance-account-top-up-webhooks]] — separate Platforms scheduled/on-demand top-up webhook guide with different transfer categories and flows.

## Raw Sources

- [[raw/adyen/docs/issuing/add-manage-funds/top-ups/top-up-webhooks/2026-09-15|Issuing recurring top-up webhooks guide, captured 2026-09-15]]
