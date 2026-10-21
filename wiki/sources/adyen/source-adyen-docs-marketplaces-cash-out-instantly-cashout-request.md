---
title: "Adyen Marketplace cashout request"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/cash-out-instantly/cashout-request"
raw_files:
  - "adyen/docs/marketplaces/cash-out-instantly/cashout-request/2026-09-15.md"
tags: [adyen, marketplaces, platforms, cashout, payouts]
---

## Overview

This 2020-modified Marketplace guide, captured 2026-09-15, describes POST `/cashouts` to make a user's pending funds instantly available in that user's balance account. A request may also direct those funds to the user's transfer instrument as a separate payout leg; omitting the instrument leaves them in the balance account. The endpoint's created cashout and related transfer IDs begin asynchronous processing, not proof of payout or bank receipt. [[adyen]] [[adyen-platforms]]

## Key takeaways

- Prerequisites are an Adyen for Platforms integration, API credentials with Transfers and Configuration API roles, accepted Transfer webhooks, Support enablement for the marketplace, and sales-day settlement on the user's balance account. The user's accounts need `receiveFromBalanceAccount` and `sendToBalanceAccount`; `sendToTransferInstrument` is conditional on a transfer-instrument payout. From LEM API v3, that payout capability is verified at the individual transfer-instrument level, not all instruments for the legal entity (raw lines 21–35).
- For the optional instant bank payout, the guide **recommends** calculating a bank route with `priorities: [instant]` and verifying an `instant` response, then checking `balances.pendingAvailable` with GET `/balanceAccounts/{id}`. Show zero cashout availability when that balance is negative. A route calculation is a precheck, not a guarantee that a later payout succeeds (raw lines 39–104).
- POST `/cashouts` requires `instructingBalanceAccountId`, `amount.value` and `amount.currency`. `counterparty.transferInstrumentId` is required only to pay out to the user's transfer instrument; absent it, the funds remain in the user's balance account. `description` and `referenceForBeneficiary` are allowed only with that instrument. The platform may charge a fee in minor units, no more than the cashout amount, in the same currency; cashout plus fee must fit the pending balance (raw lines 106–122).
- The created response exposes a cashout ID and related transfer objects such as `cashoutRepayment` (deduction after settlement) and `cashoutFee`. Track the asynchronous result through Transfer `created`/`updated` and Transaction `created` webhooks; subscribe to both Transfer and Transaction webhooks for that flow. A created response, balance-account availability, or booked debit does not establish bank receipt (raw lines 149–219).
- If a request succeeds but its instrument payout fails, the guide says the cashout is reversed: cashout amount and user fee return to the user's balance account as pending available, and the marketplace is not charged for the failed cashout. Retrying requires a **new** POST `/cashouts`. Invalid instrument ownership, no instant route, currency/fee mismatch and insufficient pending balance are error routes; this snapshot lists EUR, USD, GBP and AUD and a unit-one minimum, subject to the page's dated scope (raw lines 221–322).
- **Example conflict:** the request table names `counterparty.transferInstrumentId`, but the curl example places `transferInstrumentId` at the top level. Its prose says EUR 1000 with EUR 10 fee, and request uses fee value 1000, but the example response shows `fee.amount.value: 100000` while its `cashoutFee` transfer is 1000. Do not infer canonical request placement or fee math from those conflicting examples; verify against the API schema (raw lines 117–124, 128–146, 162–199).

## Detail locators

- Purpose, conditional capabilities, setup, optional checks and balance limit: raw lines 17–104. Request fields, TEST /btl/v4 curl example, created response and example conflicts: lines 106–202.
- Async webhook subscriptions, failure reversal/new-request retry, error causes and dated currencies/minimum: lines 204–322.

## Related

- [[adyen]] — provider.
- [[adyen-platforms]] — modern platform/Marketplace context.
- [[source-adyen-docs-marketplaces-cash-out-instantly-cashout-webhooks]] — Marketplace cashout transfer legs and statuses.
- [[source-adyen-docs-platforms-cash-out-instantly-cashout-request]] — separate Platforms-path request guide.
- [[adyen-classic-platforms]] — distinct legacy integration.

## Raw Sources

- [[raw/adyen/docs/marketplaces/cash-out-instantly/cashout-request/2026-09-15|Marketplace cashout request — 2026-09-15 snapshot]]
