---
title: "Adyen Marketplace scheduled internal fund transfers"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/internal-fund-transfers/scheduled-fund-transfers"
raw_files:
  - "adyen/docs/marketplaces/internal-fund-transfers/scheduled-fund-transfers/2026-09-15.md"
tags: [adyen, marketplaces, platforms, internal-transfers, sweeps]
---

## Overview

This 2020-modified Marketplace guide captured 2026-09-15 configures **sweeps** to schedule internal transfers between balance accounts. A sweep can push funds out of one balance account or pull funds in from another, based on schedule, amount and source/destination. Examples include liable-to-user bonuses and same-user balance maintenance. This is an internal balance-account movement, distinct from an external bank payout; schedule creation does not establish that a future transfer was booked. [[adyen]] [[adyen-platform-internal-transfers]]

## Key takeaways

- Prerequisites listed are an Adyen for Platforms integration; a Transfers API credential with TransferService Webservice Initiate role; Customer Area Initiate internal transfers and Balance platform base roles; accepted/subscribed Transfer webhooks; and Support enablement for the source balance account. **Only when source and destination balance accounts belong to different account holders**, the sender needs `sendToBalanceAccount` and receiver needs `receiveFromBalanceAccount` capability (raw lines 25–42). The guide's API create route is a Balance Platform Configuration API sweep endpoint, despite the prerequisite table naming a Transfers API role; keep both source statements without inferring an unstated credential substitute.
- Create via Customer Area or POST `/balanceAccounts/{balanceAccountId}/sweeps`, with source balance-account ID in the path and destination `counterparty.balanceAccountId`. API fields include matching balance currency, `schedule.type: cron`, account-time-zone `schedule.cronExpression`, and `type` defaulting to `push`; the example is weekly Wednesday 09:30 in TEST. The Customer Area flow has all-available, maintain-balance or fixed-amount choices (raw lines 44–130, 132–413).
- The returned sweep ID and default `active` status identify **schedule creation**; status can be patched and `balancePlatform.balanceAccountSweep.created`/`.updated` webhooks report configuration outcomes. They are separate from actual execution and booked fund movement (raw lines 415–451, 480–487).
- By default a sweep transfers the full available balance when evaluated. Optional `triggerAmount` checks available balance against a threshold; `targetAmount` retains a minimum with `triggerAmount` strictly higher; `sweepAmount` fixes transfer amount with `triggerAmount` at least as high. The EUR 250 trigger/EUR 200 target example says EUR 620 produces EUR 420 excess, while EUR 230 does not trigger. Those are scheduled-transfer examples, not payout-to-bank evidence (raw lines 452–480).
- For each resulting **internal** transfer, watch separate outgoing and incoming webhook series: `received`, `authorised`, then `booked`, or failure. Customer Area shows two transfer entries, one debit and one credit; its schedule Events tab labels `Success` as **transfer created**, not booked. If a transfer fails, inspect source available balance and then consider user top-up or liable-to-user internal transfer; if sufficient, contact Support (raw lines 819–877).
- **Example mismatch:** the optional dynamic-description section switches its `counterparty` to `transferInstrumentId` and discusses beneficiary bank statements and payout reports, whereas the core internal-transfer instructions require `balanceAccountId`. The parameter table names `referenceForBeneficiary`, while that section says `remittanceForBeneficiary`. Do not take this mixed external-payout example as evidence that a scheduled internal transfer goes to a bank or that either naming is interchangeable. The Customer Area table also calls its destination balance-account field a transfer-instrument ID (raw lines 65–68, 122–128, 489–521, 812–817).

## Detail locators

- Sweep purpose/direction and conditional roles/capabilities/source enablement: raw lines 17–42. Customer Area create flow and USD maintenance example: lines 44–111. API account-to-account fields, TEST examples and active response: lines 112–451.
- Amount controls, threshold/target conditions and EUR example: lines 452–487. Dynamic description/transfer-instrument versus balance-account mismatch: lines 489–817.
- Execution webhooks, two-sided entries, failure triage and schedule event meanings: lines 819–877.

## Related

- [[adyen]] — provider.
- [[adyen-platform-internal-transfers]] — internal balance-account transfer concept.
- [[adyen-platforms]] — modern platform context.
- [[source-adyen-docs-platforms-internal-fund-transfers-scheduled-fund-transfers]] — separate Platforms-path guide.
- [[adyen-classic-platforms]] — distinct legacy integration.

## Raw Sources

- [[raw/adyen/docs/marketplaces/internal-fund-transfers/scheduled-fund-transfers/2026-09-15|Marketplace scheduled internal fund transfers — 2026-09-15 snapshot]]
