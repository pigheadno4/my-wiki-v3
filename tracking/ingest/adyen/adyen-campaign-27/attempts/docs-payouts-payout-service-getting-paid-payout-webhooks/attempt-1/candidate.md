---
title: "Adyen Payout Service bank-payout webhooks"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/getting-paid/payout-webhooks"
raw_files:
  - "adyen/docs/payouts/payout-service/getting-paid/payout-webhooks/2026-09-15.md"
tags: [adyen, payout-service, platforms, bank-payouts, webhooks]
---

## Overview

This 2023-modified Payout Service guide, captured 2026-09-15, explains **Transfer webhooks** for a payout from a platform balance account to a user's external bank account. The source is under **Payout Service**, distinct from the legacy Payout API covered by [[adyen-payouts]] and from Marketplace/Platforms-specific guides. `balancePlatform.transfer.created` reports an outgoing request; `balancePlatform.transfer.updated` reports reservation, balance-account debit, bank-side tracking, credit, failure or return. The examples are TEST payloads, not evidence that an actual beneficiary bank received funds. [[adyen]] [[adyen-platforms]]

## Key takeaways

- Prerequisite: a Payout Service integration, a server able to receive/accept webhooks, and Customer Area subscriptions to **Transfer** and **Transaction** webhooks. Identify this payout stream with `category: bank`, `direction: outgoing` from the source balance account, and `type: bankTransfer`. The guide's detailed examples are Transfer `created`/`updated` events (raw lines 19–59).
- **Request and reservation:** `transfer.created` with `status: received` identifies initiation; `transfer.updated` `authorised` means the amount is reserved on the user's source balance account. Insufficient available funds can produce `refused` / `notEnoughBalance`, and the page instructs adding funds and sending a **new** transfer request. None of these states proves a debit or bank receipt (raw lines 60–230).
- **Booked debit:** `transfer.updated` `status: booked`, outgoing direction and an accounting `events.transactionId` show deduction from the source balance account. The guide explicitly says booked is **not final**: instant bank transfers may fail and regular/wire transfers may return. A later `tracking.status: pending` with `type: internalReview` can occur after that debit; passing review yields instant `credited` tracking or a non-instant ETA, while failed review yields `tracking.status: failed`, `type: internalReview`, `reason: refusedForRegulatoryReasons`. The failed-review TEST payload still has top-level `status: booked`/`reason: approved`, so distinguish tracking outcome from top-level accounting state and do not infer a reversal from that example (raw lines 325–334, 434–581, 583–704).
- **Bank rejection and return:** `status: failed` follows external-bank rejection when automatic retries are unsuccessful; for instant transfers with end-to-end confirmation, it is the bank rejection state. `status: returned` reports funds returned by the counterparty bank, with reason and transaction ID. The failed and returned examples show positive accounting balance mutations after earlier debit, but their sample IDs and balances are not a general retry or timing promise (raw lines 706–829, 1227–1347).
- **Tracking versus confirmation:** an `estimatedArrivalTime` is an estimate of beneficiary-bank credit and may differ from actual arrival. At this snapshot the page says ETA is available for local payouts, excluding instant and cross-border. A `tracingData` event provides rail-specific network identifiers (UK GBP FPS `fpid`, US USD ACH `traceNumber`) when funds leave Adyen, useful to investigate delayed/missing transfers; tracing is not credit confirmation. For completed **instant** priority, `tracking.status: credited`/`type: confirmation` is the guide's bank-credit signal, stronger than `booked` or ETA, though it remains provider webhook evidence rather than an independent bank statement (raw lines 830–1113, 1115–1225).
- **Returned-transfer reasons:** `networkReason` gives network `code`, `description` and `namespace`, mapped to Adyen `reason`; FPS/ACH returns occur after funds left Adyen and can follow a tracing event. Temporary reasons may allow a new route/later retry, but the guide says permanent reasons block the transfer instrument and further requests fail HTTP 422 until bank details change. The table still says “check ... and retry” for `counterpartyAccountClosed` and `counterpartyAccountBlocked`; do **not** interpret that table as permission to retry a blocked instrument without resolving the permanent issue. Consult actual reason and transfer-instrument state (raw lines 1349–1547).
- **TEST example discrepancies:** the failed-review payload has `amount.value: 1000` but its first `received` mutation is `-10000`, then later `+1000`/`-1000` (raw lines 585–704). Its top-level booked/approved state coexists with failed internal-review tracking. These sample details must not be used as a universal amount or terminal-status calculation.

## Detail locators

- Integration/webhook setup and payout identifiers: raw lines 19–59. Initiation, reservation, insufficient-balance refusal and new request: lines 60–324.
- Booked debit, internal review pending/passed/failed and sample mismatch: lines 325–705. External-bank failed state: lines 706–829.
- ETA, tracing coverage, instant credited confirmation, returned state, network reasons and blocked-instrument retry boundary: lines 830–1547.

## Related

- [[adyen]] — provider.
- [[adyen-platforms]] — balance-platform context; Payout Service is a distinct integration route.
- [[adyen-payouts]] — legacy Payout API concept, distinct from this Payout Service Transfer-webhook flow.
- [[source-adyen-docs-platforms-payout-webhooks]] — separate Platforms-path payout webhook guide.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/getting-paid/payout-webhooks/2026-09-15|Payout Service bank-payout webhooks — 2026-09-15 snapshot]]
