---
title: "Configure a Marketplace balance-account settlement delay"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/custom-payouts/configure-settlement-delay"
raw_files:
  - "adyen/docs/marketplaces/custom-payouts/configure-settlement-delay/2026-09-15.md"
tags: [adyen, marketplaces, balance-accounts, settlement-delay]
---

## Overview

This pinned Marketplace guide explains how a platform overrides its merchant-account transaction settlement-delay default for a **specific user's balance account** through the Configuration API. The setting governs after how many **business days** funds in a settlement batch become available; configuring it is distinct from scheduling a payout or proving a transfer or bank receipt. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The Configuration API credential needs the **Balance Platform BCL role**. Subscribe to `balancePlatform.balanceAccount.created` and `.updated` Configuration webhooks. An Account Manager must enable custom sales-day settlement delay for the marketplace (raw lines 21–31).
- Custom settlement delay is unavailable on a balance account with a **managed payout schedule**. A value of **1 day** requires previous Adyen approval (raw line 30).
- When creating an account, POST `/balanceAccounts`; when changing an existing account, PATCH `/balanceAccounts/{id}`. Include `platformPaymentConfiguration.settlementDelayDays`, whose documented values are integers **1–20** or `null` for default. The guide's TEST example sets **3** business days (raw lines 33–64).
- `platformPaymentConfiguration.salesDayClosingTime` is conditionally required. It uses `HH:MM` with hours **00–07** and minutes **00**, default **00:00**. If a specific closing time was previously configured, include it on balance-account updates or it resets to default (raw lines 40–46). This makes a delay-only PATCH potentially change the sales-day cutoff.
- The API response reflects the requested `platformPaymentConfiguration` on the account; a created or updated Configuration webhook follows application. These confirm configuration state, not actual settlement completion, payout initiation, booked transfer or bank receipt (raw lines 268–321).

## Detail locators

- Scope, roles, webhook setup, approval and managed-schedule limit: raw lines 15–31.
- POST/PATCH fields, settlement-day range and closing-time reset: raw lines 33–48.
- TEST PATCH example and account response: raw lines 50–292.
- Created/updated account webhook examples: raw lines 294–321.

## Related

- [[adyen]]
- [[adyen-platforms]]
- [[adyen-index]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/custom-payouts/configure-settlement-delay/2026-09-15|Pinned settlement-delay guide]]
