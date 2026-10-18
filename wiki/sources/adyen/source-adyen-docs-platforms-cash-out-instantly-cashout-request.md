---
title: "Make a cashout request for Adyen for Platforms | Adyen Docs"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/cash-out-instantly/cashout-request"
raw_files:
  - "adyen/docs/platforms/cash-out-instantly/cashout-request/2026-09-15.md"
tags: [adyen, platforms, cashout, transfers-api, payouts]
---

## Overview

This Adyen for Platforms guide describes requesting a cashout that makes a user's pending funds available in the user's balance account. A request may additionally specify the user's transfer instrument to pay out the funds; without that ID, the funds remain in the balance account. The guide uses Transfers API `/cashouts` and says processing is asynchronous, with transfer and transaction webhooks for outcomes. The webpage was fetched 2026-09-15 but reports `last_modified` 2020-09-11. It does not prove current cashout eligibility, an executed cashout, or receipt at a beneficiary bank. [[adyen]] [[adyen-platforms]]

## Key takeaways

- **Enablement and capability gates:** The page requires an Adyen for Platforms integration, API credential roles for Transfers API and Configuration API, Support enablement of cashout for the platform, sales-day settlement enabled on the user's balance account, and Transfer-webhook handling. User accounts need `receiveFromBalanceAccount` and `sendToBalanceAccount`; `sendToTransferInstrument` is additionally required for a cashout with `transferInstrumentId`. From LEM API v3, the latter capability is verified at transfer-instrument level. These are documented prerequisites, not proof that a specific user or bank account passes them.
- **Recommended checks:** Before POST `/cashouts`, the guide recommends calculating an instant bank route for a transfer instrument via Configuration API `/transferRoutes/calculate` and checking for `transferRoutes.priority: instant`, plus reading `balances.pendingAvailable` on the user's balance account. A negative pending-available amount should be shown as zero available for cashout. Route calculation and balance checks reduce failure risk; neither reserves funds or guarantees bank credit.
- **Request shape and destination:** POST `/cashouts` requires `instructingBalanceAccountId`, amount value and currency. `counterparty.transferInstrumentId` is conditional: supply it for payout to the user's transfer instrument; omit it to keep cashout funds in the user's balance account. Optional platform fee amount is in minor units, must not exceed the cashout amount, and the cashout-plus-fee sum must fit the pending available balance; fee currency must equal cashout currency. Description and beneficiary reference are allowed/returned only with a transfer-instrument ID. The response has a cashout `id` and a `transfers` array, including `cashoutRepayment` and, if charged, `cashoutFee` legs; creation is not final outcome.
- **Outcome and failure:** Adyen says cashout processing is asynchronous. The page points to created/updated Transfer webhooks and transaction-created webhooks, with Transfer and Transaction subscriptions, to track related legs and success or failure. If the request succeeds but the payout to the transfer instrument fails, the cashout is reversed: amount and user fee return to pending available balance and the platform is not charged for the failed cashout. After a confirmed failure, a retry is a new POST `/cashouts` request; the guide does not authorize retrying a pending operation blindly. Error examples distinguish invalid or wrong-entity instrument ID, no instant route, unsupported currency, mismatched fee currency, below-minimum amount and exceeded pending balance. The snapshot lists EUR, USD, GBP and AUD with a one-unit minimum; verify current account/region eligibility.
- **Example conflict:** The test request shows EUR 1,000 cashout (`amount.value: 100000`) and EUR 10 fee (`fee.amount.value: 1000`). Its purported successful response instead echoes fee amount `100000`, while the `cashoutFee` transfer is `1000` and `cashoutRepayment` is `101000`. Do not treat that response as a consistent fee calculation or executed money movement; use the API contract and observed asynchronous events.

## Detail locators

- Purpose, platform/role/capability, webhooks and Support/sales-day prerequisites: pinned raw lines 15–35.
- Recommended route and pending-available checks, including instant priority and negative-balance display: pinned raw lines 37–104.
- `/cashouts` required/conditional fields, optional fee constraints and test request: pinned raw lines 106–151.
- Response IDs/transfer types, conflicting fee example and asynchronous processing: pinned raw lines 153–206.
- Three webhook types, subscription and separate transfer-details route: pinned raw lines 208–223.
- Reversal on failed instrument payout, new-request retry and dated error/currency/minimum examples: pinned raw lines 225–326.

## Related

- [[adyen-platforms]] — platform/user balance-account context and main concept route.
- [[source-adyen-docs-platforms-cash-out-instantly-cashout-webhooks]] — separate multi-leg webhook evidence guide.
- [[adyen-payouts]] — broader payout context; this Platforms Transfers API cashout is distinct from the legacy Payout API described there.

## Raw Sources

- [[raw/adyen/docs/platforms/cash-out-instantly/cashout-request/2026-09-15|Make a cashout request — 2026-09-15 snapshot]]
