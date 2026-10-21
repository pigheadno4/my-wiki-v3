---
title: "View Adyen Marketplace custom payout schedule executions"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/custom-payouts/scheduled-payouts/view-custom-payout-executions"
raw_files:
  - "adyen/docs/marketplaces/custom-payouts/scheduled-payouts/view-custom-payout-executions/2026-09-15.md"
tags: [adyen, marketplaces, platforms, custom-payouts, scheduled-payouts, sweep-executions]
---

## Overview

This 2026-09-15-captured [[adyen]] Marketplace guide shows how to inspect each execution of a custom payout schedule on a user's balance account in [[adyen-platforms]]. Customer Area and Configuration API expose whether a scheduled attempt was sent, skipped or failed; a successful execution gives a resulting transfer ID. Execution success starts a separate funds-transfer lifecycle from the balance account to the user's bank-account transfer instrument and does not itself prove bank receipt.

## Key takeaways

- Viewing executions through the Configuration API requires **Bank Scheduled Payouts Merchant Role**. Customer Area viewing requires **Balance platform base role** and **Configure scheduled payouts**. The page calls for Configuration and Transfer webhooks to track both execution and subsequent funds movement. In Customer Area, navigate account holder → balance account → **Scheduled transfers** → custom schedule → **Events** for next payout and past execution dates/statuses. A managed schedule shows estimated arrival; a custom schedule shows transfer schedule. See raw lines 19–47.
- Customer Area labels are **Sent** (payout created and sent), **Not sent** (conditions unmet, such as insufficient balance), and **Failed** (error). The page mentions closed/suspended external bank account and disabled send-to-transfer-instrument capability due to missing KYC checks as possible failure causes, and says failures continue until the root cause is resolved. These are schedule attempt labels, not a beneficiary-bank credit confirmation. See raw lines 49–57.
- Configuration API GET `/balanceAccounts/{balanceAccountId}/sweeps/{id}/executions` returns a `sweepExecutions` array. Its TEST sample has `succeeded` plus `resultDetails.transferId`, `skipped` plus reason codes, and `failed` plus a reason; the successful transfer ID routes to later Transfer webhooks. Configuration webhook types `balancePlatform.balanceAccountSweepExecution.succeeded`, `.skipped` and `.failed` report execution result, sweep and execution IDs, and transfer ID or reason. See raw lines 59–149 and 174–213.
- Skip reasons include no balance, minimum threshold, disabled configuration and manual Adyen block. Failure reasons in the table include insufficient reserve collateral, no route, blocked/invalid counterparty, inactive hierarchy, missing instrument or capability, amount/route limits and invalid address. A failure may be marked final; for example a permanently closed counterparty can disable the custom schedule, and the failed webhook's boolean `sweepConfigurationDisabled` reports this. Do not treat every failed execution as automatically disabling the schedule. See raw lines 147–213.
- The samples have schema/value tensions: API response example uses `sweepDisabled: "true"`, while webhook prose/payload uses boolean `sweepConfigurationDisabled: true`; the table/API example gives `counterpartyAccountBlocked`, but failed webhook example gives `counterpartyBlocked`. Sample webhook `timestamp` also precedes its `triggeredAt`; do not infer a real event order or canonical enum/field name from those illustrative payloads. Verify the applicable API/webhook schema and actual message. See raw lines 70–110, 128–143, 153–170 and 217–235.
- After `succeeded`, use Transfer webhooks to observe authorization, capture and possible bank return for the separate payout transfer. A `Sent` UI label, sweep success, or transfer initiation alone is not bank receipt. See raw lines 238–242 and [[source-adyen-docs-marketplaces-payout-webhooks]].

## Detail locators

- Purpose, access roles, webhook subscriptions and Customer Area Events path: raw lines 17–47.
- UI Sent/Not sent/Failed definitions and failure examples: raw lines 49–57.
- Configuration API path and `sweepExecutions` TEST example: raw lines 59–110.
- Succeeded/skip/failure webhook structure and reason table: raw lines 112–213.
- Failed webhook disable flag, contradictory example code and fund movement route: raw lines 215–247.

## Related

- [[adyen]] — provider profile.
- [[adyen-platforms]] — canonical platform payout concept.
- [[source-adyen-docs-marketplaces-custom-payouts-scheduled-payouts]] — schedule configuration and conditions.
- [[source-adyen-docs-platforms-custom-payouts-scheduled-payouts-view-custom-payout-executions]] — separate Platforms URL for the analogous guide.
- [[source-adyen-docs-marketplaces-payout-webhooks]] — later transfer and bank-status evidence.

## Raw Sources

- [[raw/adyen/docs/marketplaces/custom-payouts/scheduled-payouts/view-custom-payout-executions/2026-09-15|Marketplace custom payout executions — pinned 2026-09-15 raw snapshot]]
