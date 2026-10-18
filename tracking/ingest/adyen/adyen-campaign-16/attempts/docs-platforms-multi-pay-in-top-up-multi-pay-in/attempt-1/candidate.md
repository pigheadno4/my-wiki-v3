---
title: "Adyen Platforms top up a multi pay-in account"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/multi-pay-in/top-up-multi-pay-in"
raw_files:
  - "adyen/docs/platforms/multi-pay-in/top-up-multi-pay-in/2026-09-15.md"
tags: [adyen, platforms, multi-pay-in, internal-transfers, balance-accounts]
---

## Overview

Adyen documents an **internal balance-platform transfer** from the platform's liable balance account to its multi pay-in balance account. It can cover a shortfall when a third-party pay-in partner withholds part of a user's payment or offsets bank payout costs, leaving less settled in the multi pay-in account than the platform intends to allocate. This is neither a bank deposit into the platform nor the subsequent allocation to user balance accounts. See [[adyen]] and [[adyen-platforms]]. The pinned guide describes the operation; it does not prove a particular transfer was authorised, booked, or available to allocate.

## Key takeaways

- The prerequisite is Transfers API credentials and subscription to any of the named Transfer or Transaction webhooks. For the top-up, POST `/transfers` with required `amount` (currency and value), `balanceAccountId` as the **source liable balance account**, `counterparty.balanceAccountId` as the **destination multi pay-in account**, and `category=internal`. `description` and `reference` are optional identifiers for webhooks/reports. See raw lines 21–46.
- The USD 2.40 test request shows `value: 240`, source suffix `LIABLE`, destination suffix `00005`, and `internal` category; it is illustrative, not a permitted-currency list or minimum/maximum transfer limit. The page states no country list, transfer ceiling, or bank receipt condition. See raw lines 46–70.
- The response section calls `status=authorised` a successful top-up request and says a non-authorised response should be investigated; `refused` with `notEnoughBalance` is an example. Authorised is distinct from the later booked debit and credit events. The sample response amount is `10000` although its preceding USD 2.40 request is `240`, so do not carry the response amount into reconciliation. See raw lines 352–392.
- The two account perspectives use `category=internal` and `type=internalTransfer`: the liable source reports `direction=outgoing`, the multi pay-in destination `direction=incoming`. Each has received, authorised, and booked transfer stages, with transaction webhooks for booked account changes. Match account ID, counterparty, transfer ID, transaction ID, currency, amount, status, and direction per leg. See raw lines 394–427, 431–711, and 713–1001.
- The source debit and destination credit are separate account records. A received or authorised webhook alone does not show both booked changes. The liable-side sample's booked transaction has a positive `240` value despite the surrounding debit narrative and `-240` balance mutation, and several updated-stage sample payloads retain a `balancePlatform.transfer.created` type despite prose saying updated; treat those samples as illustrative and reconcile actual events. See raw lines 579–709, 791–864, 870–1001.

## Detail locators

- **Need and prerequisites:** raw lines 15–29; partner withholding creates the possible shortfall, while this guide's operation spends from platform liable balance.
- **Request fields and pinned SDK/test examples:** raw lines 31–350. The curl sample uses Transfers API v4 test endpoint; language-library versions vary and are only dated examples.
- **Response and refusal:** raw lines 352–392. A response status is not booked balance evidence.
- **Liable debit:** raw lines 418–711. Outgoing received → authorised/reserved → booked with transaction ID; then booked transaction notification.
- **Multi pay-in credit:** raw lines 713–1001. Incoming received → authorised/reserved → booked with transaction ID; then booked transaction notification.
- **Next step:** raw lines 1003–1015 routes to allocating third-party payments and refunding them; only the allocation page [[source-adyen-docs-platforms-multi-pay-in-payments]] is separately captured here. Top-up does not itself allocate to the user.

## Related

- [[adyen-platforms]] — platform account context.
- [[source-adyen-docs-platforms-multi-pay-in-payments]] — separate per-payment third-party allocation after the multi pay-in account has funds.
- [[source-adyen-docs-platforms-manage-liable-accounts]] — platform liable-account context.

## Raw Sources

- [[raw/adyen/docs/platforms/multi-pay-in/top-up-multi-pay-in/2026-09-15|Adyen Top up multi pay-in account, fetched 2026-09-15]]
