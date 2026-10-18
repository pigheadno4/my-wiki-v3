---
title: "Adyen Platforms scheduled internal fund transfers"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/internal-fund-transfers/scheduled-fund-transfers"
raw_files:
  - "adyen/docs/platforms/internal-fund-transfers/scheduled-fund-transfers/2026-09-15.md"
tags: [adyen, platforms, internal-transfers, sweeps, balance-accounts]
---

## Overview

This Adyen for Platforms guide (page last modified 2020-09-11; captured 2026-09-15) explains schedules for internal fund transfers between balance accounts within a platform. A sweep evaluates a push or pull on a schedule, using a configured amount and source or destination. The guide covers Customer Area and Balance Platform API setup, then separates schedule creation from the transfer requests and booking events that result. See [[adyen]], [[adyen-platforms]] and [[adyen-platform-internal-transfers]].

## Key takeaways

- **Prerequisites:** The page calls for an Adyen for Platforms integration; a Transfers API credential with TransferService Webservice Initiate role; Customer Area Initiate internal transfers and Balance platform base roles; a server accepting transfer webhooks; and Support enablement for transfers on the source balance account. When the two balance accounts belong to different account holders, the sending account holder needs sendToBalanceAccount and the receiving account holder needs receiveFromBalanceAccount capability. These are documented setup conditions, not proof of current permission or enablement.
- **Schedule and amount:** Configure a sweep in Customer Area or POST /balanceAccounts/{balanceAccountId}/sweeps. In the API instructions, counterparty balance-account ID, currency and cron schedule define the route and evaluation time; cron uses the balance account's time zone, and push is the default type. The API walkthrough defaults to transferring all available balance. Optional triggerAmount gates evaluation, targetAmount keeps a minimum, and sweepAmount sets a fixed amount; the raw states triggerAmount must exceed targetAmount or be at least sweepAmount for those options. The source currency must match a balance currency. See the raw's Create a sweep and Optional sweep configuration sections for fields, examples and exact conditions.
- **Creation versus execution:** The response shows a schedule ID and active status by default; the balancePlatform.balanceAccountSweep.created webhook is the guide's confirmation route for schedule creation. A resulting transfer request has outgoing and incoming webhook series, with received, authorised, booked or failure status. The Customer Area represents one between-account movement as debit and credit transfer entries. A schedule or an Events-tab Success entry (described here as transfer created) does not itself prove that a transfer booked.
- **Failure and UI cautions:** For a failed internal transfer, the guide directs checking the source available balance, then topping up or making a separate liable-to-user internal transfer when insufficient; it directs contacting Support if sufficient funds still fail. Its Customer Area schedule details require Balance platform base role. The captured page also reuses payout and bank-recipient wording and includes a transfer-instrument counterparty in a later description example; those passages should not be used to redefine this guide's balance-account-to-balance-account scope. The Events status table repeats Success and only states that a transfer was created.

## Detail locators

- Purpose, push/pull examples, and Requirements matrix: pinned raw lines 15-42.
- Customer Area setup, balance threshold, frequency and timing example: pinned raw lines 44-110.
- API POST fields, account time zone and example: pinned raw lines 112-131; response/default active status and creation webhook: lines 415-448.
- Optional trigger, target and fixed amount behavior: pinned raw lines 452-460; update example: lines 462-487.
- Dynamic description section and mixed transfer-instrument/payout example: pinned raw lines 490-817.
- Resulting transfer webhooks, troubleshooting, schedule details and Events status table: pinned raw lines 819-877.

## Related

- [[adyen-platform-internal-transfers]] — internal balance-account transfer concept and reciprocal source route.
- [[adyen-platforms]] — parent platform context.

## Related raw API references

- [[raw/adyen/docs/platforms/internal-fund-transfers/internal-transfer-webhooks/2026-09-15|Internal-transfer webhooks]] — separate event detail; navigation only.
- [[raw/adyen/docs/platforms/custom-payouts/scheduled-payouts/2026-09-15|Scheduled payouts]] — external payout sweep guide; navigation only.

## Raw Sources

- [[raw/adyen/docs/platforms/internal-fund-transfers/scheduled-fund-transfers/2026-09-15|Adyen Schedule internal funds transfers, captured 2026-09-15]]
