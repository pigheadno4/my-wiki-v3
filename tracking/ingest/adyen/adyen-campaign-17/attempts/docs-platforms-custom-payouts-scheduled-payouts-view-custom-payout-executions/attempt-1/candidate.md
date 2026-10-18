---
title: "View Adyen Platforms custom payout schedule executions"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/custom-payouts/scheduled-payouts/view-custom-payout-executions"
raw_files:
  - "adyen/docs/platforms/custom-payouts/scheduled-payouts/view-custom-payout-executions/2026-09-15.md"
tags: [adyen, platforms, custom-payouts, scheduled-payouts, sweep-executions]
---

## Overview

This 2026-09-15 Adyen for Platforms guide explains how to inspect each *execution* of a custom payout schedule on a balance account. An execution is a payout initiated by that schedule. Customer Area Events and a Configuration API executions endpoint show whether that attempt was sent, skipped, or failed; a successful execution supplies the resulting transfer ID. The execution result identifies schedule initiation, while the resulting bank-transfer lifecycle and eventual beneficiary bank receipt require separate evidence.

## Key takeaways

- For API viewing, the Configuration API credential needs `Bank Scheduled Payouts Merchant Role`. Customer Area viewing needs `Balance platform base role` and `Configure scheduled payouts`. To track execution and resulting fund movement, the page asks for Configuration and Transfer webhooks. The Customer Area route is account holder → balance account → **Scheduled transfers** → custom schedule → **Events**, which shows next payout and past execution dates/statuses. The UI distinguishes a managed schedule's estimated arrival time from a custom schedule's transfer schedule.
- Customer Area execution statuses are **Sent** (payout created and sent), **Not sent** (conditions did not trigger payout, such as low balance), and **Failed** (error, including bank-account or capability issues). The page says failed schedules will continue failing until the root cause is resolved. These labels describe scheduled attempt status, not beneficiary-bank receipt.
- The Configuration API `GET /balanceAccounts/{balanceAccountId}/sweeps/{id}/executions` returns a `sweepExecutions` array with execution IDs, `triggeredAt`, `result`, and details. The sample shows `succeeded` with `transferId`, `skipped` with `noBalanceToPayOut` or `disabledConfiguration`, and `failed` with a blocked-counterparty reason. Use the resulting transfer ID to follow the separate transfer lifecycle; a successful sweep execution does not establish booked or bank-received payout.
- Configuration webhooks describe `balancePlatform.balanceAccountSweepExecution.succeeded`, `.skipped`, and `.failed`. Success includes the sweep and execution IDs plus `resultDetails.transferId`; skip/failure includes reason and reason code. The reason table includes low balance/threshold or disabled/manual skip, and failures such as insufficient reserve collateral, routing, counterparty, capability, account hierarchy, amount, or address problems. A failure may be flagged final, disabling the schedule; the failed webhook's `sweepConfigurationDisabled` boolean reports that condition. The API example instead shows `sweepDisabled` as a string, and the blocked-counterparty reason code differs between its table/API example and failed webhook sample; treat these as example inconsistencies and verify actual payload schema.
- After a successful execution triggers a funds transfer, Transfer webhooks provide its later status, including authorization, capture, or a possible bank return. A `Sent` UI state, `succeeded` execution, or downstream balance booking is not evidence of beneficiary bank receipt. The illustrated webhook payloads use the TEST environment.

## Detail locators

- `## Requirements` and `## View payout schedule executions in Customer Area`: access roles, webhook subscriptions, UI path and managed/custom schedule display distinction.
- `### Execution event statuses and reasons`: Sent, Not sent, Failed meanings and root-cause warning.
- `## View payout schedule executions through API`: Configuration API endpoint and `sweepExecutions` response example.
- `## Execution results and reasons`: webhook event types, reason-code table, `sweepConfigurationDisabled` final-failure behavior and example inconsistencies.
- `### Track fund movements`: follow the resulting transfer with Transfer webhooks, including possible return.

## Related

- [[adyen-platforms]] — main Platforms concept and source route.
- [[source-adyen-docs-platforms-custom-payouts-scheduled-payouts]] — custom payout schedule configuration.
- [[source-adyen-docs-platforms-custom-payouts]] — custom payout overview and bank-transfer scope.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/custom-payouts/scheduled-payouts/view-custom-payout-executions/2026-09-15|Adyen view custom payout executions (fetched 2026-09-15)]]
