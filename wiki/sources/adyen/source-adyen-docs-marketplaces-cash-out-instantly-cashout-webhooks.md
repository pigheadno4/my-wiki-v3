---
title: "Adyen Marketplace cashout webhooks"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/cash-out-instantly/cashout-webhooks"
raw_files:
  - "adyen/docs/marketplaces/cash-out-instantly/cashout-webhooks/2026-09-15.md"
tags: [adyen, marketplaces, platforms, cashout, transfers, webhooks]
---

## Overview

This 2026-09-15 Marketplace snapshot describes balance-platform Transfer and Transaction webhooks for a cashout requested on behalf of a marketplace user. It separates the user's balance-account funding, optional fee debit, optional transfer-instrument payout, and later cashout repayment. The example is a TEST Balance Platform API v4 request advancing EUR 1,000 of sales funds before their scheduled settlement, with an optional EUR 10 fee. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Four distinct legs:** `cashoutFunding` is an incoming internal transfer into the user's balance account; `cashoutFee` is an outgoing internal debit only if a fee is specified; `bankTransfer` is an outgoing bank-category transfer to the user's transfer instrument only if one is specified; and `cashoutRepayment` is an outgoing internal debit of the advanced funds when the original sales funds settle. Identify them by transfer `category`, `direction`, and `type` (raw lines 19–24, 39–74).
- **Subscription and status evidence:** The server must receive and accept webhooks, and the marketplace must subscribe to Transfer and Transaction webhooks in Customer Area. The guide names `balancePlatform.transfer.created`, `balancePlatform.transfer.updated`, and `balancePlatform.transaction.created`. Its separate-leg examples progress through received, authorised, and booked accounting events; a booked transaction records a balance-account debit or credit. For the optional instant-priority bank payout, a later transfer update with `tracking.status: credited` is distinct from the booked debit. These illustrative TEST events are not independent proof of a particular beneficiary bank receipt (raw lines 26–37, 117–1121).
- **Repayment timing and sample conflict:** The opening says the repayment transfer is triggered on the originally scheduled settlement date, while the detailed section says its transfer request is created on cashout day and the amount is deducted when sales funds settle. Treat creation versus debit timing as unresolved by this snapshot. The repayment narrative calls for `transfer.updated` authorised/booked notices, but both adjacent sample envelopes retain `balancePlatform.transfer.created` and top-level `status: received` while nested events advance. Do not construct a universal top-level state machine from those payloads (raw lines 24, 1124–1416).
- **Other sample limits:** The fee prose says its value date is when the fee is sent to the platform's liable balance account, while its booked payload uses `counterparty.balanceAccountId: CashOutFunding`; this is not an unambiguous liable-account destination. The Marketplace request example places `transferInstrumentId` directly in the body, whereas the otherwise closely parallel Platforms cashout-webhook example nests it in `counterparty`; neither illustrative webhook page settles the accepted request schema. The source gives no failure, return, retry or bank-receipt sequence (raw lines 78–115, 553–664, 1122–1416).

## Detail locators

- Transfer legs, webhook types, subscription requirements, and category/direction/type mapping: pinned raw lines 19–74.
- TEST EUR 1,000 cashout, EUR 10 fee, scheduled settlement example and v4 request: pinned raw lines 78–115.
- Funding transfer and transaction event examples: pinned raw lines 117–408.
- Fee debit, liable-account wording and booked payload: pinned raw lines 409–700.
- Optional instant bank transfer, booked debit and later credited tracking: pinned raw lines 701–1121.
- Repayment timing and inconsistent sample envelopes: pinned raw lines 1124–1416.

## Related

- [[adyen-platforms]] — main platform and marketplace money-movement context.
- [[adyen-webhooks]] — general webhook handling.
- [[source-adyen-docs-platforms-cash-out-instantly-cashout-webhooks]] — closely parallel Platforms-path snapshot; request-body examples differ.
- [[source-adyen-docs-platforms-payout-webhooks]] — separate payout status, failure, return and bank-tracking route.

## Raw Sources

- [[raw/adyen/docs/marketplaces/cash-out-instantly/cashout-webhooks/2026-09-15|Marketplace webhooks for cashouts, captured 2026-09-15]]
