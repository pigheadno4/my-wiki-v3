---
title: "Payout Service recurring balance-account top-up management"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/top-up-balance-accounts/manage-recurring-top-ups"
raw_files:
  - "adyen/docs/payouts/payout-service/top-up-balance-accounts/manage-recurring-top-ups/2026-09-15.md"
tags: [adyen, payouts, payout-service, balance-accounts, recurring-top-ups]
---

## Overview

This Payout Service guide, last modified 2020-09-11 and captured 2026-09-15, describes viewing, updating, deactivating and deleting **recurring top-up schedules** for a balance account through the Configuration API or Customer Area. A schedule can automatically trigger future top-up attempts; schedule state or API sample responses do not prove a direct debit, booked balance credit or future-debit revocation. See [[adyen]] and [[adyen-payouts]] (raw lines 5–21, 303–445).

## Key takeaways

- The stated scope is an **enterprise payouts** integration. API schedule configuration requires a Configuration API credential with **BankAPI Advanced Webservice** role; the Customer Area route instead lists **Balance platform base** and **Configure scheduled payouts** human roles. It lists Configuration, Transfer and Transaction webhooks. Transfer-instrument funding requires an active **receiveFromTransferInstrument** capability with valid verification status, and the top-up source needs enough funds. This feature does **not** support on-demand top-ups (raw lines 23–36).
- GET `/balanceAccounts/{balanceAccountId}/recurringTopUps` lists schedules for one balance account in creation order, with optional `limit` and cursor pagination. The response data includes source transfer instrument when applicable, fixed versus target amount, schedule/threshold, status and direct-debit beneficiary reference. The page describes weekday, weekly, monthly and continuous balance checks; a returned schedule is not a posted top-up (raw lines 40–112, 183–222).
- PATCH `/balanceAccounts/{balanceAccountId}/recurringTopUps/{topUpId}` changes specified settings and leaves omitted parameters unchanged. It can adjust fixed/target amount, schedule, threshold, status and reference. The source `transferInstrumentId` is **immutable**: changing the funding source requires deactivating the existing schedule and creating a new one. The page's example changes amount and sets `status: inactive`; deactivation is a schedule lifecycle action, not evidence that any previously initiated debit was reversed (raw lines 303–411).
- DELETE on that specific balance-account/top-up-ID route removes a recurring top-up; the guide illustrates success as **204 No Content** and a separate Customer Area Remove action. It does not specify that deactivation or deletion cancels already triggered transfers, revokes a funding mandate or prevents every future debit outside that schedule. Do not infer those effects from the response (raw lines 413–453).
- The example pagination `link.next.href` and `link.previous.href` use singular `recurringTopUp` while the documented GET/PATCH/DELETE endpoints use plural `recurringTopUps`; treat the example links as internally inconsistent rather than changing the documented route or asserting live API behavior (raw lines 63, 178, 185, 288–291, 309, 419).

## Detail locators

- Integration, roles, webhooks, capability, no on-demand path and funding-source balance: raw lines 23–36.
- GET list, schedule data and pagination examples: raw lines 40–301.
- PATCH mutable fields, immutable source and inactive example: raw lines 303–411.
- DELETE route, 204 example and Customer Area removal: raw lines 413–453.

## Related

- [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-create-recurring-top-ups]]
- [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-top-up-webhooks]]
- [[adyen-api-access]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/top-up-balance-accounts/manage-recurring-top-ups/2026-09-15|Pinned recurring top-up management guide]]
