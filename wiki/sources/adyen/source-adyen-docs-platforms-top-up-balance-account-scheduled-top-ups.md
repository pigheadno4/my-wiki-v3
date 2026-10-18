---
title: "Scheduled balance-account top-ups | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/top-up-balance-account/scheduled-top-ups"
raw_files:
  - "adyen/docs/platforms/top-up-balance-account/scheduled-top-ups/2026-09-15.md"
tags: [adyen, platforms, top-ups, sweeps, direct-debit, balance-accounts]
---

## Overview

This [[adyen]] for Platforms guide describes a **pull sweep** configured on a user's balance account to trigger an incoming top-up request from a verified transfer instrument when sweep conditions are met. Its worked Configuration API example uses a **balance threshold**, although the introduction also mentions fixed timing as a possible condition. Sweep creation is a configuration event; later Transfer and Transaction webhooks track whether a triggered request adds funds. It is distinct from an on-demand Checkout top-up or an internal balance-account transfer. [[adyen-platforms]]

## Key takeaways

- **Eligibility and setup.** The guide requires Adyen for Platforms, Configuration API credentials, Configuration/Transfer/Transaction webhook subscriptions, and the user's `receiveFromTransferInstrument` capability. It says scheduled top-ups are supported only for account holders with **verified bank accounts in the EU, UK or US**, over corresponding **SEPA, BACS or ACH** standard debit rails. Support must enable scheduled top-ups for the platform. These snapshot requirements do not prove a specific account, bank, region, rail, currency or mandate is currently eligible; this page does not detail direct-debit mandates or return rights. [Raw: Requirements, lines 26–37]
- **Pull sweep identity and conditions.** A sweep is a configuration on the **user's balance account**. For a scheduled top-up, `type: pull` draws from the specified source transfer instrument into that balance account when its condition is evaluated. The page describes pre-defined timing and/or available-balance thresholds conceptually; the worked request sets `schedule.type: balance` and a `triggerAmount`, not a cron schedule. Its EUR 5,000 threshold and EUR 1,000 sweep amount are illustrative. A trigger starts an incoming transfer request; it is not itself booked credit. [Raw: Sweeps and How it works, lines 39–59; Create a pull sweep, lines 63–107]
- **Configuration request.** POST `/balanceAccounts/{balanceAccountId}/sweeps` names the destination balance account in the path. The field table marks source `counterparty.transferInstrumentId`, `counterparty.merchantAccount`, currency, `schedule.type`, `type`, `triggerAmount` and `sweepAmount` required for this illustrated route. The transfer instrument must link to the account holder's legal entity. The table describes the merchant account as another source-of-funds identifier; do not infer exact external debit mechanics from those two field labels alone. The test snippets use versioned client libraries and are example payloads, not a validated live operation. [Raw: lines 61–74, 76–461]
- **Creation versus transfer.** The response returns a sweep ID and says new sweeps default to **active**; status can be updated with PATCH `/balanceAccounts/{balanceAccountId}/sweeps/{sweepId}`. The `balancePlatform.balanceAccountSweep.created` webhook reports successful sweep creation. Only when conditions are later met does Adyen initiate an incoming top-up transfer; the linked top-up-webhook route tracks received, authorized, funds-added and failure states. Neither an active sweep nor a creation webhook establishes a successful direct debit, booked user balance, payout or bank receipt. [Raw: lines 463–500]

## Detail locators

- Raw `Requirements` (lines 26–37): API, webhook, capability, verified-bank geography/rails and Support-enable gates.
- Raw `Sweeps` and `How it works` (lines 39–59): pull direction, timing/amount concepts and distinction between configuration and triggered transfer.
- Raw `Create a pull sweep` (lines 61–461): required fields and threshold-based test request; library versions are pinned in examples.
- Raw response and webhook route (lines 463–505): default active status, PATCH status, creation webhook and later top-up event navigation.

## Related

- [[adyen-platforms]] — platform/user balance-account context
- [[source-adyen-docs-platforms-top-up-balance-account-top-up-webhooks]] — later scheduled top-up transfer and transaction states
- [[source-adyen-docs-platforms-top-up-balance-account-on-demand-top-ups]] — separate one-off Checkout funding route

## Raw Sources

- [[raw/adyen/docs/platforms/top-up-balance-account/scheduled-top-ups/2026-09-15|Adyen Platforms scheduled top-ups — collected 2026-09-15]]
