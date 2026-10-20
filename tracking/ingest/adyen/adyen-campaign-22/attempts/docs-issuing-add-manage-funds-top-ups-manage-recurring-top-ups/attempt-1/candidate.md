---
title: "Adyen Issuing: Manage recurring top-ups"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/add-manage-funds/top-ups/manage-recurring-top-ups"
raw_files:
  - "adyen/docs/issuing/add-manage-funds/top-ups/manage-recurring-top-ups/2026-09-15.md"
tags: [adyen, issuing, balance-platform, top-ups]
---

## Overview

Adyen Issuing guide, captured 2026-09-15, for viewing, changing and deleting an existing recurring top-up of a balance account through the Balance Platform Configuration API or Customer Area. Once configured, Adyen triggers top-ups to the balance account according to the schedule settings; this guide explicitly says the feature does not support on-demand top-ups. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The page lists an Issuing integration, a BankAPI Advanced Webservice role for API schedule configuration, Balance platform base and Configure scheduled payouts roles for Customer Area configuration, and Configuration, Transfer and Transaction webhooks. For a transfer-instrument top-up, it requires `receiveFromTransferInstrument`; check that the capability is active with a valid `verificationStatus` before attempting a transfer. The top-up source must have enough balance. See raw **Requirements**, lines 23–36.
- GET `/balanceAccounts/{balanceAccountId}/recurringTopUps` lists schedules for that balance account in creation order. The first request omits `cursor`; subsequent requests may use the returned cursor with `limit` for pagination. The default page size stated here is 10. The Customer Area route is **Accounts & Balances → Balance Accounts → Schedule ID**. See raw **View recurring top-ups**, lines 38–62 and 162–301.
- PATCH `/balanceAccounts/{balanceAccountId}/recurringTopUps/{topUpId}` updates specified settings; omitted parameters retain their creation values. `transferInstrumentId`, the funding source, cannot be changed by PATCH. To change the source of funds, deactivate the current schedule and create a new one. See raw **Update a recurring top-up**, lines 303–334.
- The update section covers fixed versus target amounts, threshold, schedule, `active`/`inactive` status, description and beneficiary reference. Its amount-switching table calls for setting the old amount field to `null`; follow the exact direction in the raw table. The documented schedule values are weekdays, weekly, monthly, or `null` for continuous monitoring; the page does not state a timezone for its 07:00 examples. See raw **Update a recurring top-up**, lines 319–334.
- DELETE `/balanceAccounts/{balanceAccountId}/recurringTopUps/{topUpId}` removes a schedule; the guide says a successful request returns `204 No Content`. Customer Area uses the schedule action menu’s **Remove**. This is a destructive schedule action, distinct from setting `status` to `inactive` with PATCH. See raw **Delete a recurring top-up**, lines 413–451.

## Detail locators

- Response fields include schedule ID, transfer-instrument counterparty when applicable, fixed or target amount, trigger schedule/threshold, status and direct-debit beneficiary reference: raw lines 84–103.
- Pagination examples and response links: raw lines 104–295. The example payloads/URLs are illustrations; use the linked API reference for an implementation-specific request shape.
- PATCH example changes a target amount to a fixed amount and deactivates a schedule: raw lines 342–405.
- Related create and webhook guide links are in raw **See also**, lines 453–461.

## Related

- [[adyen-issuing]] — Issuing concept and source route.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/issuing/add-manage-funds/top-ups/manage-recurring-top-ups/2026-09-15|Manage recurring top-ups — 2026-09-15 capture]]
