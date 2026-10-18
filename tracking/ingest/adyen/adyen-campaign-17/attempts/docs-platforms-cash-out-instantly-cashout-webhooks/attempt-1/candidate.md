---
title: "Adyen Platforms cashout webhooks"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/cash-out-instantly/cashout-webhooks"
raw_files:
  - "adyen/docs/platforms/cash-out-instantly/cashout-webhooks/2026-09-15.md"
tags: [adyen, platforms, cashout, transfers, webhooks]
---

## Overview

This 2026-09-15 capture of Adyen's Platforms cashout webhook guide explains the transfer and transaction events produced by a cashout request for a platform user. The source uses a test example of advancing a user's EUR 1,000 sales funds before scheduled settlement, with an optional EUR 10 fee and optional payout to that user's transfer instrument. It describes balance-platform events, not the legacy Online Payouts Payout API or POS cashout. See [[adyen]], [[adyen-platforms]], and [[adyen-webhooks]].

## Key takeaways

- **Four separate transfer legs:** Cashout funding is an incoming internal transfer crediting the user's balance account (`cashoutFunding`). A specified fee creates an outgoing internal debit (`cashoutFee`). A specified transfer instrument creates an outgoing bank-category payout from the user's balance account (`bankTransfer`, with `categoryData.priority: instant` in the example). Cashout repayment is an outgoing internal debit (`cashoutRepayment`): the request is created on the cashout date, while the amount is deducted when the originally scheduled sales funds settle. These are distinct transfer objects, not four states of one payout.
- **Webhook setup and identification:** The server must receive and accept webhooks, and the platform must subscribe to Transfer and Transaction webhooks in Customer Area. The guide uses `balancePlatform.transfer.created`, `balancePlatform.transfer.updated`, and `balancePlatform.transaction.created`. Identify the four legs using `category`, `direction`, and `type`; the transfer's `data.id`, `sequenceNumber`, `reference`, balance-account/account-holder fields, and a booked event's `transactionId` are shown in sample payloads. The user's balance account is the source or destination of each described leg; the optional payout counterparty is the user's transfer instrument.
- **Status and money movement:** The examples show received, authorised, and booked transfer stages. A transaction.created event describes the corresponding balance-account debit or credit after booking. For the optional bank payout, a later transfer.updated sample has `tracking.status: credited` for the transfer instrument; the earlier booked balance-account debit alone does not show this later tracking event. Even the provider's credited tracking in this test example is not independent evidence that a particular beneficiary bank received funds. This page gives no failed/returned payout or retry sequence; use the separate payout-webhook documentation and actual operation evidence for those outcomes.
- **Sample qualification and conflicts:** The EUR 1,000/10 fee, January 1–3 timeline, IDs, priority, and dates are illustrative test data, not universal timing, availability, or destination guarantees. The cashout-repayment narrative calls its authorised/booked notifications `transfer.updated`, but the adjacent sample payloads retain outer `type: balancePlatform.transfer.created` and `status: received` even as nested accounting events progress. Read actual envelope and event fields for a real webhook rather than treating those examples as a consistent top-level state machine. The fee narrative says its value date represents transfer to the platform's liable balance account, while the booked sample's counterparty is `CashOutFunding`; this sample does not establish a universal liable-account ID or ownership conclusion.

## Detail locators

- Four legs, event types, subscription prerequisites, and `category`/`direction`/`type` identifiers: pinned raw lines 19–74.
- Test request and January sales/settlement scenario: pinned raw lines 78–115.
- Funding transfer and transaction examples: pinned raw lines 117–408.
- Fee debit narrative, value date, and transaction examples: pinned raw lines 409–700.
- Optional bank payout's received/authorised/booked, transaction, and later credited tracking examples: pinned raw lines 701–1127.
- Repayment timing and contradictory outer envelope/status in the authorised and booked samples: pinned raw lines 1128–1420.

## Related

- [[adyen-platforms]] — current Platforms integration and balance-account context.
- [[adyen-webhooks]] — general webhook handling and event scope.

## Raw Sources

- [[raw/adyen/docs/platforms/cash-out-instantly/cashout-webhooks/2026-09-15|Adyen Webhooks for cashouts, captured 2026-09-15]]
