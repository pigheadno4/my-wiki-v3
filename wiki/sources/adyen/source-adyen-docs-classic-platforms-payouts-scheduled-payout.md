---
title: "Classic Platforms scheduled bank payouts"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/payouts/scheduled-payout"
raw_files:
  - "adyen/docs/classic-platforms/payouts/scheduled-payout/2026-09-15.md"
tags: [adyen, classic-platforms, payouts, schedules, account-api]
---

## Overview

This Classic Adyen for Platforms page (last modified 2020-03-20; captured 2026-09-15) describes automatic payouts of available account funds to account holders, platform and per-account schedule settings, optional same-day speed, and payout descriptors. It explicitly routes new integrations elsewhere. Its Classic `accountCode` and Account API operations belong under [[adyen-classic-platforms]], with provider context at [[adyen]]; configuration alone does not establish a sent payout or bank receipt.

## Key takeaways

- The page says the platform default is `DAILY`: automatic payouts each day to account holders with a **positive balance**, using available account funds. A platform-wide default change requires Adyen Support (raw lines 21–25). For **newer Classic integrations**, optimized daily timing depends on account-holder country code; existing integrations can ask Support to enable it. Otherwise daily payouts are at **00:00 CET**. The country-time matrix is at raw lines 29–40.
- To override the platform default for a **specific account**, use Classic Account API `POST /updateAccount` with `payoutSchedule.schedule`. The table lists daily, weekly, twice-monthly and monthly options. `HOLD` means **no scheduled payout by Adyen**, requires a `reason`, and leaves payouts to be manually triggered (raw lines 42–59). The sample request includes an `action` field but does not establish the consequences of that sample value for already scheduled payouts (raw lines 61–75).
- For schedule updates, **HTTP 200** supplies response data but still requires `ACCOUNT_UPDATED` notification to confirm central-database update. **HTTP 202** acknowledges a queued request and likewise requires the notification to confirm success (raw lines 90–93). Do not read either response as a completed payout.
- Faster payout processing is an option only where the relevant express method is available, with this dated page listing **Australia, United Kingdom and United States**. It says funds can be available the same day **if processed before the bank cutoff**. Platform-wide enablement goes through Support; a specific account uses `POST /updateAccount` with `payoutSpeed=SAME_DAY`. The page again requires `ACCOUNT_UPDATED` confirmation for update responses (raw lines 95–125). This conditional schedule does not guarantee same-day bank receipt.
- The default payout descriptor is the platform name. Support can configure dynamic values from account/account-holder descriptions or codes and payout PSP reference; the submitted value has a **1–35-character** and character-set constraint (raw lines 127–142). The page does not demonstrate how a particular bank actually displays it.

## Detail locators

- Optimized timing matrix and legacy default: raw lines 29–40. Schedule enum and `HOLD` reason/manual boundary: raw lines 42–59. The value named `WEEKLY_ON_TUE_FRI_MIDNIGHT` is described as Tuesday and Friday; `BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT` is described as monthly on the 1st and 15th. Preserve table wording rather than inferring cadence from enum names (raw lines 55–58).
- Illustrative test `/updateAccount` request/response and asynchronous confirmation: raw lines 61–93.
- Same-day regions, cutoff, configuration and notification: raw lines 95–125. Descriptor values and allowed characters: raw lines 127–142.

## Related

- [[adyen-classic-platforms]] — Classic concept and source route.
- [[adyen]] — provider.
- [[source-adyen-docs-classic-platforms-payouts-track-payouts]] — separate payout status and return tracking.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/payouts/scheduled-payout/2026-09-15|Classic Platforms scheduled payouts, captured 2026-09-15]]
