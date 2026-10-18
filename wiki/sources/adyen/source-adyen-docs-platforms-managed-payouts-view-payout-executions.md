---
title: "View managed payout executions | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/managed-payouts/view-payout-executions"
raw_files:
  - "adyen/docs/platforms/managed-payouts/view-payout-executions/2026-09-15.md"
tags: [adyen, platforms, managed-payouts, payout-executions, webhooks]
---

## Overview

This 2026-09-15 [[adyen]] for Platforms guide explains how to inspect **executions**: payout attempts initiated by a managed payout schedule applied to a user's balance account. Customer Area or a Configuration API GET exposes the execution timeline and result. A successful schedule execution creates and sends a payout transfer; its result and transfer ID are not proof that the user's bank received the funds. Transfer webhooks own the later transfer lifecycle, including a possible return. [[adyen-platforms]]

## Access and execution results

- Configuration API reads require a credential with **Bank Scheduled Payouts Merchant Role**. Customer Area viewing requires **Balance platform base role** and **Configure scheduled payouts**. The page calls for Configuration and Transfer webhook subscriptions to track execution and ensuing movement. In Customer Area, the operator follows account holder → balance account → **Scheduled transfers** → managed schedule → **Events**. The page contrasts a managed schedule's estimated arrival time with a custom schedule's transfer schedule. See raw lines 21–48.
- The Events table labels **Sent** as payout created and sent, **Not sent** as not triggered when conditions such as insufficient available balance are unmet, and **Failed** as a schedule execution error. The table says no action is required for its low-balance Not-sent example, but other skipped reason codes include disabled configuration or Adyen block. A Failed example can involve a closed/suspended external bank account or disabled `sendToTransferInstrument` capability after missing KYC checks; the guide warns that payouts continue to fail until the root cause is resolved. Do not treat Sent as bank credit or Not sent as one universal recovery instruction. See raw lines 49–57.
- GET `/balanceAccounts/{balanceAccountId}/payoutSchedules/{id}/executions` scopes by balance-account and managed-schedule IDs and returns `payoutScheduleExecutions`. The illustrative API results are `succeeded`, `skipped` and `failed`; a successful execution webhook includes the execution ID, schedule ID and `resultDetails.transferId` for the resulting transfer. Skipped/failed execution webhooks carry `reasonCode` and `reason`, with the enumerated examples at raw lines 145–168 covering no balance/minimum threshold/disabled or blocked schedules, reserve insufficiency, routing/counterparty/transfer-instrument problems, missing capabilities, route amount limits and invalid amount/address. These are schedule-execution results, not final transfer or bank-arrival results. See raw lines 59–168.
- After a successful execution, monitor Transfer webhooks for the payout transfer from the user's balance account to their bank transfer instrument. The guide names authorized, captured and eventual bank-return updates. A captured transfer or execution result still needs its own evidence boundary before claiming beneficiary bank receipt; the page provides no actual bank statement or final confirmation. See raw lines 230–234.

## Pinned-example cautions

- The sample labeled **Payout execution skipped** has webhook type `.skipped` and `reasonCode: noBalanceToPayOut`, yet its `data.result` is `failed` (raw lines 172–199). The failed sample uses `reasonCode: counterpartyBlocked` (220–221), while the table lists `counterpartyAccountBlocked` (159). Both are test payloads, so do not normalize either sample into a definitive result/reason mapping without the current API contract and actual events. The API example also repeats one execution ID across different illustrative outcomes (73, 81, 89, 99); use real IDs when joining records.
- The page's bank-detail table is explicitly **TEST only** (254–282), not a live country/currency availability list. Its `IR` row contains an `IE` IBAN (274), and its Hungary row labels an `hkLocal` identification type (272); verify a fixture before use rather than relying on those rows as normative routing data. The testing section calls for checking Sent/Not Sent/Failed in Customer Area with corresponding success/skipped/failed webhooks, but these are test expectations, not proof of a production bank outcome. See raw lines 236–282.

## Detail locators

- **Purpose, roles, webhook subscriptions and Customer Area navigation:** raw lines 15–48.
- **Customer Area statuses and low-balance versus failure causes:** raw lines 49–57.
- **Scoped GET, response array, success webhook and transfer ID:** raw lines 59–143.
- **Skip/fail reasons and inconsistent test examples:** raw lines 145–228.
- **Transfer lifecycle, test scenarios and TEST-only bank details:** raw lines 230–282.

## Related

- [[adyen-platforms]]
- [[source-adyen-docs-platforms-managed-payouts]] — schedule purpose and estimated timing
- [[source-adyen-docs-platforms-managed-payouts-use-managed-payouts]] — applying and managing schedules

## Raw Sources

- [[raw/adyen/docs/platforms/managed-payouts/view-payout-executions/2026-09-15|Adyen Platforms payout-execution guide — collected 2026-09-15]]
