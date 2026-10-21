---
title: "Adyen Payout Service scheduled internal transfers"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/internal-fund-transfers/scheduled-fund-transfers"
raw_files:
  - "adyen/docs/payouts/payout-service/internal-fund-transfers/scheduled-fund-transfers/2026-09-15.md"
tags: [adyen, payout-service, platforms, internal-transfers, sweeps]
---

## Overview

This 2020-modified, 2026-09-15-captured [[adyen]] Payout Service guide describes balance-account **sweeps** that schedule internal transfers between balance accounts. It routes through [[adyen-platform-internal-transfers]] because the configured balance account pushes funds to another balance account or pulls from one based on schedule and amount conditions (raw lines 15–35). Despite the Payout Service path and some “payout” language, the core operation here is internal account-to-account movement, separate from a transfer instrument or external bank payout.

## Key takeaways

- **Prerequisites and ownership:** The source calls for an Adyen for Platforms integration; a Transfers API credential with **TransferService Webservice Initiate** role; Customer Area **Initiate internal transfers** and **Balance platform base** roles; accepted/subscribed Transfer webhooks; and Support enablement for the source balance account (raw lines 37–54). Only when the involved balance accounts belong to *different* account holders does the sender need `sendToBalanceAccount` and the receiver `receiveFromBalanceAccount` capability (lines 51–53). The described create call itself is a Balance Platform Configuration API `/balanceAccounts/{balanceAccountId}/sweeps` endpoint (lines 124–150); the guide does not reconcile that with its Transfers API credential-role wording.
- **Direction, schedule and amounts:** `push` moves funds out of the configured balance account to a specified destination; `pull` brings them in from a specified source. The API example defaults to push, uses `counterparty.balanceAccountId`, a currency matching the balances, and a `cron` expression evaluated in the configured balance account's timezone (raw lines 25–35, 124–150). Customer Area offers full available, maintain-balance and fixed-amount options (lines 60–123). Without optional amount objects, the schedule transfers all available balance when evaluated; `triggerAmount` gates execution, `targetAmount` retains a minimum and requires trigger strictly greater than target, while fixed `sweepAmount` requires trigger at least sweep amount (lines 464–477). The USD/EUR figures and TEST endpoint are examples, not actual transfer evidence.
- **Configuration versus execution:** The response provides a sweep ID and default `active` status, which may be patched; `balancePlatform.balanceAccountSweep.created` or `.updated` webhooks concern schedule configuration (raw lines 425–460, 480–499). A condition being met triggers a transfer **request**, not immediate booked movement (line 35). For a resulting internal transfer, separate outgoing and incoming webhook series progress through `received`, `authorised`, `booked` or failure. Customer Area shows two entries, one debited and one credited (lines 831–837).
- **Material example conflicts:** The dynamic-description section switches from internal `counterparty.balanceAccountId` to `transferInstrumentId` in its sample and discusses beneficiary-bank statements and a Payout Report, which are external-payout cues (raw lines 134–140, 501–540, 824–829). It also names `remittanceForBeneficiary` where the earlier parameter table uses `referenceForBeneficiary` (lines 136–137, 507). The Customer Area balance-account field is described as a transfer-instrument ID (lines 83–86). Keep the core internal-transfer route and do not infer the destination type or field equivalence from those mixed examples.

## Detail locators

- Internal sweep purpose, direction and conditional role/capability/source setup: raw lines 15–54.
- Customer Area setup and USD maintenance illustration: raw lines 56–123. API account-to-account fields and versioned TEST samples: lines 124–424.
- Created/active response and schedule webhook: raw lines 425–460; amount controls and EUR illustration: lines 464–499.
- Description placeholders, destination/field mismatch and bank-statement language: raw lines 501–829; resulting two-sided internal transfer statuses: lines 831–837.

## Evidence boundary

A created or active sweep is configuration, not proof that its condition was met or a transfer booked. Even a booked internal debit/credit pair remains inside balance-platform accounts and is not a beneficiary-bank receipt. The mixed transfer-instrument and bank-description examples conflict with the page's stated balance-account destination; this source does not establish an external bank payout, a particular destination's validity or live eligibility.

## Related

- [[adyen-platform-internal-transfers]] — internal movement concept.
- [[adyen-platforms]] — required current platform integration.
- [[source-adyen-docs-marketplaces-internal-fund-transfers-scheduled-fund-transfers]] — separate Marketplace-path sweep guide.
- [[adyen-payouts]] — distinct generic payout route.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/internal-fund-transfers/scheduled-fund-transfers/2026-09-15|Pinned Payout Service scheduled internal-transfer guide, captured 2026-09-15]]
