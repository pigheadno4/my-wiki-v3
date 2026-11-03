---
title: "Use managed payout schedules | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/managed-payouts/use-managed-payouts"
raw_files:
  - "adyen/docs/platforms/managed-payouts/use-managed-payouts/2026-09-15.md"
tags: [adyen, platforms, managed-payouts, payout-schedules, balance-accounts, configuration-api]
---

## Overview

This [[adyen]] for Platforms guide explains how to view, apply, inspect, update, deactivate and delete **managed payout schedules** after configuring them with an Adyen contact. Schedules are configured on a balance platform and applied to users' balance accounts through Customer Area or the Configuration API; automatic application to qualifying new accounts is a separate path. A configured schedule or successful configuration response is not proof that a payout ran or that a beneficiary bank received funds. See [[adyen-platforms]] and [[source-adyen-docs-platforms-managed-payouts]] for the product overview.

## Key takeaways

- **Access, eligibility and settlement boundary.** Configuration API credentials require the **Bank Scheduled Payouts Merchant Role**; Customer Area users need Balance platform base and Configure scheduled payouts roles. The page calls for Configuration and Scheduled payout webhooks, and the user needs `sendToTransferInstrument`. A balance account can have only **one payout schedule per currency**, and each schedule covers one location and currency. Managed payouts do not change settlement timing for pass-through payments or sales-day payouts with a **T+7-or-longer** settlement delay; those payments settle on their indicated timing and pay out once settled. These conditions do not prove current regional/currency/account availability. [Raw: Requirements, lines 27–47]
- **Apply and verify a schedule.** GET `/balancePlatforms/{balancePlatformId}/payoutSchedules` lists configured schedules and IDs. Applying one to a user balance account can use Customer Area, POST `/balanceAccounts/{balanceAccountId}/payoutSchedules`, or Adyen-contact-enabled automatic application for qualifying **new** balance accounts. The API request requires `balancePlatformPayoutScheduleId` and `transferInstrumentId`; omitted optional fields inherit schedule defaults. Automatic application cannot be used for balance accounts associated with **existing legal entities**. Under **automatic application**, the account, schedule, transfer instrument, country, currency and verification prerequisite checks can leave application **pending**; Adyen retries that automatic application after balance-account or transfer-instrument updates. Manual Customer Area and Configuration API cutoff or rail validation instead follows the fallback-or-error behavior below. A created-schedule webhook or HTTP 200 indicates configuration, not payout initiation or bank credit. [Raw: lines 49–74, 193–243, 333–406]
- **Cutoff and bank-rail outcomes are conditional.** Application is checked against the user's sales-day closing time and transfer-instrument reachability. Where another daily window or banking rail is available, Adyen describes a fallback that retains the same settlement delay; where no viable schedule meets it, configuration fails validation. Customer Area can also redirect a supported currency/country combination to a custom schedule. The US T+1 9:00-to-13:30 and Australia NPP examples are regional illustrations, not universal arrival guarantees. Automatic-application failure has a dedicated webhook. [Raw: lines 245–257, 318–331, 394–406]
- **Update and effects.** PATCH `/balanceAccounts/{balanceAccountId}/payoutSchedules/{id}` changes only supplied settings; allowed frequency values are constrained by the applied schedule. For a monthly date on a weekend, the page says initiation moves to the next business day; for a missing 29th–31st it moves to the month's last day. `minPayoutAmount`, `maxPayoutAmount` and `retainedAmount` constrain available payout behavior; higher transfer priority incurs higher fees in the Customer Area flow. The testing table says an active managed schedule blocks a balance-account `timeZone` change until the schedule is deleted, with an expected HTTP 422/error `30_021`. The page does not define refund, payout-return or retry outcome handling. [Raw: lines 290–316, 499–560, 651–661]
- **Deactivate/delete ambiguity.** The balance-account deactivation section says to make a **PATCH** request but its example uses **DELETE** on the same path shown under deletion; both examples say HTTP 204. Platform-level deactivation or deletion requires contacting Adyen. Because the raw does not resolve the balance-account endpoint/action distinction, verify the current Configuration API contract before using these examples. [Raw: lines 585–649]

## Detail locators

- Raw `Requirements` (lines 27–47): roles, webhook/capability conditions, schedule count/location/currency and settlement timing exception.
- Raw `View managed payout schedules for your balance platform` (lines 49–191): GET IDs, filter fields and test-only examples; sample ETAs/defaults are not guarantees.
- Raw `Apply a payout schedule to a balance account` (lines 193–432): automatic, Customer Area and Configuration API routes, pending/retry conditions, fallback/validation behavior and configuration webhooks.
- Raw `View` and `Update` (lines 434–583): applied-schedule inspection, patchable fields, business-day rules and HTTP 200 response.
- Raw `Deactivate`, `Delete` and `Testing` (lines 585–691): action ambiguity, platform-contact route, timezone-change restriction and test-only bank data. The test-bank table is not a live availability list.

## Related

- [[adyen-platforms]] — platform/user balance-account context
- [[source-adyen-docs-platforms-managed-payouts]] — managed-payout product schedule overview
- [[source-adyen-docs-platforms-manage-transfer-instruments]] — transfer-instrument context

## Raw Sources

- [[raw/adyen/docs/platforms/managed-payouts/use-managed-payouts/2026-09-15|Adyen use managed payouts — collected 2026-09-15]]
