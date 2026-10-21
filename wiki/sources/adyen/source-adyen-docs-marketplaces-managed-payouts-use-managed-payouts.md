---
title: "Use managed payouts for marketplaces"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/managed-payouts/use-managed-payouts"
raw_files:
  - "adyen/docs/marketplaces/managed-payouts/use-managed-payouts/2026-09-15.md"
tags: [adyen, marketplaces, platforms, managed-payouts]
---

## Overview

This pinned Adyen Marketplace guide explains how a platform uses managed payout schedules configured with its Adyen contact and applies them to users' balance accounts. It covers viewing, applying, updating, deactivating, deleting, and testing schedules through Customer Area or the Configuration API. It is schedule configuration guidance, not evidence of a transfer, payout execution, or bank receipt. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The Configuration API credential needs the **Bank Scheduled Payouts Merchant Role**; Customer Area users need the **Balance platform base role** and **Configure scheduled payouts** role. Subscribe to Configuration and Scheduled payout webhooks; the user needs the `sendToTransferInstrument` capability. A balance account can have only one schedule per currency, and each schedule supports one location and currency (raw lines 27–47).
- Managed payout schedules do not override pass-through or sales-day settlement delays of T+7 or more. Funds are paid out only once settled (raw line 47).
- A platform can view its platform-level schedules, then apply one to a user's balance account by automatic application, Configuration API, or Customer Area. The API application supplies `balancePlatformPayoutScheduleId` and `transferInstrumentId`; optional account-level fields can override defaults. A successful application returns an account-level schedule and a created webhook; it does not establish payout or bank-receipt success (raw lines 49–74, 193–205, 333–406).
- Automatic application requires enablement through an Adyen contact and applies to **new** balance accounts with matching currency and location. It cannot automatically apply to accounts associated with existing legal entities; use Customer Area or Configuration API for those. Eligibility also depends on the active account, default currency, non-liable sole account holder, one eligible verified transfer instrument, and country match, with the documented Eurozone exception for euro schedules. If those conditions are unmet, application stays pending and retries after account or instrument updates. Closing-time and rail validation can instead produce fallback or failure (raw lines 207–257).
- Customer Area and API let a platform view and modify an account-level schedule. Managed schedules display estimated payout arrival, while custom schedules display transfer initiation time. The API PATCH leaves omitted fields unchanged. Platform-level deactivation and deletion require an Adyen contact (raw lines 434–446, 499–560, 585–649).
- **Deactivation instruction conflict:** the guide calls account-level deactivation temporary and says to make a PATCH request, but its concrete deactivation curl uses `-X DELETE` and HTTP 204, matching the following deletion section. Do not treat that DELETE example as a verified safe way to temporarily deactivate; resolve the operation before use (raw lines 585–649).
- In TEST, a created-schedule webhook or API HTTP 200 checks application, not a completed payout. An active schedule blocks balance-account `timeZone` changes with HTTP 422 / 30_021 until deletion; a US schedule with a CA transfer instrument fails country matching. The listed bank details are for TEST (raw lines 651–691).

## Detail locators

- Platform schedule listing and identifiers: raw lines 49–191.
- Automatic application, conditions, retries, closing-time and reachability behavior: raw lines 207–257.
- Customer Area application fields and Configuration API request/response: raw lines 258–406.
- View, update, deactivate and delete account-level schedules: raw lines 407–649.
- TEST scenarios and test bank details: raw lines 651–691.

## Related

- [[adyen]]
- [[adyen-platforms]]
- [[adyen-index]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/managed-payouts/use-managed-payouts/2026-09-15|Pinned managed payouts guide]]
