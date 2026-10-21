---
title: "Configure Marketplace pull sweeps for balance-account top-ups"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/top-up-balance-account/scheduled-top-ups"
raw_files:
  - "adyen/docs/marketplaces/top-up-balance-account/scheduled-top-ups/2026-09-15.md"
tags: [adyen, marketplaces, top-ups, sweeps, balance-accounts]
---

## Overview

This pinned Marketplace guide describes a **pull sweep** that can trigger a direct-debit top-up from a user's **verified transfer instrument** into that user's balance account. Sweeps can be conditioned on timing and/or available-balance thresholds, but the page's concrete API example configures a **balance-triggered** sweep, not a fixed-time cron request. A created configuration or triggered request does not prove funds were added. See [[adyen]] and [[adyen-platforms]] (raw lines 15–24, 39–59, 61–107).

## Key takeaways

- The guide requires Adyen for Platforms, Configuration API credentials, Configuration/Transfer/Transaction webhooks, the user's **receiveFromTransferInstrument** capability, and Support enablement. Scheduled top-ups are limited to account holders with verified bank accounts in the **EU, UK and US**, using the corresponding standard **SEPA, BACS or ACH** debit rails (raw lines 26–37).
- A sweep belongs to the user's balance account. `type: pull` directs funds **from** the specified verified transfer instrument **into** that account; `schedule.type: balance` in the shown request evaluates the available-balance trigger. The source lists `counterparty.transferInstrumentId` linked to the account holder's legal entity, `counterparty.merchantAccount`, matching `currency`, `triggerAmount`, and `sweepAmount` in the POST `/balanceAccounts/{balanceAccountId}/sweeps` request (raw lines 39–74).
- The TEST example triggers below **EUR 5,000** (`triggerAmount.value: 500000`) and requests a fixed **EUR 1,000** pull (`sweepAmount.value: 100000`). These are threshold and transfer amount, not a guarantee that the balance stays above EUR 5,000 during asynchronous bank debit processing (raw lines 76–107).
- The response gives a sweep ID and defaults its status to **active**. A PATCH to `/balanceAccounts/{balanceAccountId}/sweeps/{sweepId}` can change that status; the `balancePlatform.balanceAccountSweep.created` webhook confirms sweep creation. When conditions are met, Adyen initiates an incoming top-up transfer and transfer/transaction webhooks report its authorization, added-funds outcome or failure. Distinguish configuration creation, transfer initiation, authorization and booked balance-account credit (raw lines 53–59, 463–500).
- The opening discusses pre-defined fixed schedules, but the provided parameter table and payload set `schedule.type: balance` only. Consult the relevant current API contract before deriving fixed-time schedule fields from this example (raw lines 19–24, 63–107).

## Detail locators

- Product, region, verified-bank, capability and webhook gates: raw lines 15–37.
- Sweep directions/conditions and Configuration API parameters: raw lines 39–74.
- TEST threshold/top-up payload and active response: raw lines 76–107, 463–492.
- Creation versus resulting transfer/webhook states: raw lines 494–505.

## Related

- [[adyen]]
- [[adyen-platforms]]
- [[source-adyen-docs-marketplaces-top-up-balance-account-top-up-webhooks]]
- [[adyen-index]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/top-up-balance-account/scheduled-top-ups/2026-09-15|Pinned scheduled top-up guide]]
