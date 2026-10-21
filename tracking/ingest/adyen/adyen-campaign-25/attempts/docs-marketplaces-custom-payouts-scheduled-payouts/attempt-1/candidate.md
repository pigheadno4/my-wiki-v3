---
title: "Adyen Marketplaces custom scheduled payouts"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/custom-payouts/scheduled-payouts"
raw_files:
  - "adyen/docs/marketplaces/custom-payouts/scheduled-payouts/2026-09-15.md"
tags: [adyen, marketplaces, platforms, custom-payouts, scheduled-payouts, sweeps]
---

## Overview

This 2022-modified, 2026-09-15-captured [[adyen]] Marketplace guide describes a custom payout schedule on a user's balance account in [[adyen-platforms]]. The schedule evaluates time and balance conditions, then initiates a transfer request to a verified bank account represented by a transfer instrument. Schedule creation, sweep execution, transfer status, balance-account debit and beneficiary-bank receipt are separate evidence stages; this guide does not prove any specific payout arrived.

## Key takeaways

- Prerequisites include an Adyen for Platforms integration, a Transfers API credential with **TransferService Webservice Initiate role**, Customer Area **Balance platform base role** and **Configure scheduled payouts**, the user's **sendToTransferInstrument** capability, and an account holder and transfer instrument linked to the same legal entity. The guide recommends checking available transfer routes and regional bank-method cutoffs; optional default platform transfer description setup uses Support. These are stated setup gates, not proof of a particular account's roles, capability or bank-route availability. See raw lines 19–38.
- Create a schedule in Customer Area or with Configuration API POST `/balanceAccounts/{balanceAccountId}/sweeps`. The API table specifies destination `counterparty.transferInstrumentId`, payout currency, `schedule.type=cron`, a `cronExpression` evaluated in the balance account's time zone, and `type=push`; optional bank `priorities` require `category=bank`. A created schedule has an ID and default **active** status, changeable by PATCH. A sweep-created or sweep-updated webhook confirms configuration, not payout or bank credit. See raw lines 53–99, 120–140, 425–458 and 1102–1128.
- By default, the API sweep targets all available balance at evaluation. Optional `triggerAmount` requires available balance at least that amount; `targetAmount` preserves a balance and requires `triggerAmount` higher than `targetAmount`; `sweepAmount` fixes the payout amount and requires `triggerAmount` at least `sweepAmount`. Customer Area offers corresponding all-available, maintained-balance and fixed-amount controls. When all schedule conditions hold, a transfer request is triggered, not a guaranteed final transfer. See raw lines 40–51, 71–99 and 460–503.
- Priorities can affect speed and fees. The page recommends an ordered list; it says all supplied priorities must have valid routes when configuring, then execution uses the first priority yielding a valid route for the actual amount. Unspecified priority defaults differ by region, and some routes have amount limits. The priority-update curl and some SDK examples show different fields; the creation curl uses USD while several SDK examples use EUR. Treat each test example as illustrative, and verify the intended currency/fields before implementation. See raw lines 144–422 and 839–1100.
- For observation, the page separates `balanceAccountSweepExecution` success/failure events from transfer-created/updated status changes and `balancePlatform.transaction.created` debit events. Transfer updates include event history and sequence number. Customer Area shows schedule and payout details. None of these labels alone establishes beneficiary-bank receipt; follow the transfer/return lifecycle for an actual case. See raw lines 1130–1171.

## Detail locators

- Scope, cutoff warning, roles/capability/legal-entity gates: raw lines 19–38.
- Conditions and Customer Area schedule controls: raw lines 40–118.
- Configuration API POST fields, balance-account time zone and TEST examples: raw lines 120–458.
- Optional trigger/target/fixed amount relationships and example: raw lines 460–503.
- Dynamic descriptions, short transfer reference, bank-priority route rules and discrepant update examples: raw lines 507–1102.
- Sweep-created webhook and execution/transfer/transaction tracking: raw lines 1104–1153.
- Schedule detail view: raw lines 1155–1171.

## Related

- [[adyen]] — provider profile.
- [[adyen-platforms]] — modern Marketplace balance-platform payout route.
- [[source-adyen-docs-platforms-custom-payouts-scheduled-payouts]] — separate Platforms URL with closely related guide; preserve provenance.
- [[source-adyen-docs-marketplaces-managed-payouts]] — Adyen-contact managed schedule, distinct from custom sweep configuration.
- [[adyen-payouts]] — separate legacy Payout API concept, not this balance-account sweep.

## Raw Sources

- [[raw/adyen/docs/marketplaces/custom-payouts/scheduled-payouts/2026-09-15|Configure custom payout schedules — pinned 2026-09-15 raw snapshot]]
