---
title: "View Marketplace managed-payout executions"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/managed-payouts/view-payout-executions"
raw_files:
  - "adyen/docs/marketplaces/managed-payouts/view-payout-executions/2026-09-15.md"
tags: [adyen, marketplaces, platforms, managed-payouts, payout-executions, webhooks]
---

## Overview

This 2026-09-15 Marketplace-path guide explains how to view each execution of a managed payout schedule on a balance account in Customer Area or through the Configuration API. An execution is a payout initiated by a schedule. The guide distinguishes creation, skip and initiation failure, then routes a successful execution's `transferId` to separate transfer-webhook tracking. See [[adyen]] and [[adyen-platforms]] for provider and modern balance-platform context. `Sent` or `succeeded` execution is not proof of bank credit.

## Key takeaways

- API viewing requires a Configuration API credential with **Bank Scheduled Payouts Merchant Role**. Customer Area viewing requires **Balance platform base role** and **Configure scheduled payouts**. The guide calls for Configuration and Transfer webhook subscriptions to track executions and ensuing fund movements. These are access/tracking gates, not payout-result evidence.
- In Customer Area, find the account holder, balance account and managed schedule, then its **Events** tab. A managed schedule specifies estimated payout arrival; a custom schedule specifies the transfer schedule. The UI labels are **Sent** for a successfully created/sent payout, **Not sent** when payout conditions are unmet, and **Failed** when an error prevented schedule send. A low balance can cause a non-actionable skip, while a closed/suspended external account or disabled transfer capability can cause repeated failures until the cause is fixed.
- The scoped GET `/balanceAccounts/{balanceAccountId}/payoutSchedules/{id}/executions` returns `payoutScheduleExecutions`. A `succeeded` result has `resultDetails.transferId`; `skipped` and `failed` have reason codes. The published table includes skips for no balance, threshold, disabled configuration or Adyen block, and failures for reserve collateral, route, counterparty, account hierarchy, transfer instrument, capability, route-limit, amount and address conditions. Use the exact reason for a given execution rather than equating every missed payout with insufficient balance.
- Configuration webhooks use `balancePlatform.balanceAccountPayoutScheduleExecution.succeeded`, `.skipped` or `.failed`. The skipped TEST example's webhook type and `noBalanceToPayOut` reason indicate a skip, but its `data.result` says `failed`; this snapshot does not resolve that mismatch. The failed example gives `counterpartyBlocked`, whereas the preceding reason-code table lists `counterpartyAccountBlocked`; do not normalize either code without observed payload or current schema.
- A successful execution creates a funds transfer. Follow Transfer webhooks for later authorized, captured and possible bank-return states on the user balance-account-to-bank route. The TEST fixture table is for testing managed schedules only; it does not establish live payout eligibility or bank receipt. The testing matrix includes apparent locale/type anomalies (for example `HU` with `hkLocal` and `IR` paired with an Irish IBAN), so do not treat fixture labels as current bank-format authority.

## Detail locators

- Purpose, role/webhook prerequisites and Customer Area path/statuses: raw lines 15–57. Scoped Configuration API read and example execution results: lines 59–109.
- Success webhook and transfer ID: lines 111–143. Skipped/failed reason table: lines 145–168. Skipped sample result/type mismatch: lines 172–199; failed reason-code mismatch: lines 201–228. Separate Transfer webhook lifecycle and bank-return route: lines 230–234. TEST scenarios and bank details: lines 236–282.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — modern platform balance-account and payout context.
- [[source-adyen-docs-marketplaces-managed-payouts]] — managed-payout model and schedule scope.
- [[source-adyen-docs-platforms-managed-payouts-view-payout-executions]] — separately pinned Platforms-path guide.
- [[source-adyen-docs-platforms-payout-webhooks]] — separate transfer status and bank-return evidence route.

## Related raw API references

- The raw page links to Configuration API executions and webhook schemas plus payout Transfer webhooks; those linked references own current endpoint contracts and later bank status.

## Raw Sources

- [[raw/adyen/docs/marketplaces/managed-payouts/view-payout-executions/2026-09-15|Adyen Docs: View payout executions (2026-09-15 snapshot)]]
