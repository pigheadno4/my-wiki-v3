---
title: "Adyen for Platforms custom scheduled payouts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/custom-payouts/scheduled-payouts"
raw_files:
  - "adyen/docs/platforms/custom-payouts/scheduled-payouts/2026-09-15.md"
tags: [adyen, platforms, scheduled-payouts, sweeps, balance-accounts]
---

## Overview

This Adyen for Platforms guide, last modified 2022-04-20 and captured 2026-09-15, describes configuring an automatic custom payout schedule from a balance account to a user's verified bank account represented by a transfer instrument. A schedule evaluates timing and balance conditions, then triggers a transfer request when all conditions are met. Creating or updating a sweep configuration is distinct from executing a transfer and from beneficiary bank receipt. The page does not identify a merchant of record, legal owner of funds, current account eligibility, or a successful live payout.

## Key takeaways

- Prerequisites include a Platforms integration; a Transfers API credential with **TransferService Webservice Initiate role**; Customer Area **Balance platform base role** and **Configure scheduled payouts**; the user's **sendToTransferInstrument** capability; and an account holder and transfer instrument linked to the same legal entity. The guide recommends calculating available transfer routes before configuration. It does not establish that a particular user or bank route has been verified or enabled.
- Create a schedule in Customer Area or with Configuration API POST `/balanceAccounts/{balanceAccountId}/sweeps`. The API guide names the destination transfer instrument, payout currency, `schedule.type: cron`, `schedule.cronExpression` evaluated in the balance account's time zone, and `type: push`. The response includes an ID and default `active` status; PATCH can update the schedule. `balancePlatform.balanceAccountSweep.created` and `.updated` webhooks concern schedule creation and updates, not money arriving at the bank. Examples use test endpoints and differ in their illustrated currencies, so each example must be read in its own context.
- By default, the API schedule pays out the available balance at evaluation. Optional `triggerAmount` requires available balance at least that high; `targetAmount` keeps an amount on the balance account and requires `triggerAmount` higher than `targetAmount`; `sweepAmount` fixes the payout size and requires `triggerAmount` at least that amount. Customer Area also offers all-available, maintained-balance and specific-amount choices plus a minimum balance trigger. These conditions gate an initiated transfer request; they do not promise receipt at the scheduled time.
- A bank-transfer priority or ordered list affects route speed and fees. When setting priorities, specify `category: bank`; the guide says all listed priorities must have valid routes at configuration, while execution uses the first priority yielding a valid route for the transfer amount. Some routes impose amount limits. The unspecified default priority differs by region. Regional method cutoffs affect expected bank receipt time, so scheduled evaluation time is not a delivery guarantee. The source gives no general business-day, approval, cancellation, insufficient-funds retry or returned-payout rule; consult the linked route and payout-execution guidance for those outcomes.
- For movements, use Customer Area plus transfer-created/updated, `balanceAccountSweepExecution`, and transaction-created webhooks. They have different grains: scheduled sweep configuration, execution result, transfer status, and deduction from a balance account. The page says transfer updates include an event history and sequence number. None alone is beneficiary bank receipt proof.

## Detail locators

- `Requirements` and `How it works` — roles, capability, shared legal entity, route recommendation, schedule conditions and transfer-request trigger (raw lines 23–51).
- `Create a custom payout schedule` / `Customer Area` — balance account, destination instrument, currency, trigger, amount mode, frequency, timing and priority controls (lines 53–118).
- `Create a custom payout schedule` / `API` — POST sweep fields, cron time zone, push direction, default status, PATCH route and creation webhook; test curl and library examples carry different sample currencies (lines 120–458).
- `Optional configuration` / `Sweep configuration` — available-balance default, trigger/target/sweep amount relationships and illustrative EUR balances (lines 460–503).
- `Dynamic transfer statement description` and `Priorities` — placeholder descriptions, reconciliation reference, bank category, ordered priorities and amount-dependent route limit (lines 507–526, 830–847).
- `Track fund movements` and `View sweep details` — execution/transfer/transaction event distinctions and Customer Area schedule view (lines 1071–1140).

## Related

- Company: [[adyen]]
- Main concept: [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/docs/platforms/custom-payouts/scheduled-payouts/2026-09-15|2026-09-15 custom scheduled payouts guide]]
