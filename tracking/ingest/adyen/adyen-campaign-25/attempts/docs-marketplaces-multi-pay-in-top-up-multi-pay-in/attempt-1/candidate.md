---
title: "Top up a Marketplace multi pay-in account"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/multi-pay-in/top-up-multi-pay-in"
raw_files:
  - "adyen/docs/marketplaces/multi-pay-in/top-up-multi-pay-in/2026-09-15.md"
tags: [adyen, marketplaces, multi-pay-in, internal-transfers]
---

## Overview

This pinned Marketplace guide describes an **internal** top-up from the platform's liable balance account to its multi pay-in account. A pay-in partner may withhold funds from payments or offset bank payout costs, leaving less in multi pay-in than the platform intends to allocate to users; the platform can fill that difference from its liable account. This is balance-account funding, not a new partner bank deposit, user allocation, external payout, or bank receipt. See [[adyen]] and [[adyen-multi-pay-in]].

## Key takeaways

- The operation requires Transfers API credentials and transfer or transaction webhook subscriptions. POST `/transfers` with `amount`, source `balanceAccountId` set to the **liable balance account**, `counterparty.balanceAccountId` set to the **multi pay-in account**, and `category: internal`. Optional `description` and `reference` help identify webhook/report entries (raw lines 21–46).
- The TEST request illustrates **USD 2.40** (`value: 240`) moving from liable to multi pay-in. Its example response unexpectedly shows `amount.value: 10000`, not 240; do not use that response as arithmetic proof of the requested top-up (raw lines 46–70, 352–388).
- The API response uses `status: authorised` for the guide's successful authorization example; a non-authorised result may be `refused` with `reason: notEnoughBalance`. Authorization alone does not prove booked movement. Follow the transfer and transaction webhooks (raw lines 352–402).
- The outgoing liable-account leg and incoming multi-pay-in leg have separate `internalTransfer` webhook records. The source account is `outgoing`; the destination account is `incoming`. Both pass through `received`, `authorised`, and `booked`. The liable-account booked transfer and transaction evidence shows debit; the multi-pay-in booked transfer and transaction evidence shows credit (raw lines 406–427, 431–711, 713–1001).
- `balancePlatform.transfer.created` identifies each leg, `balancePlatform.transfer.updated` reports status changes, and `balancePlatform.transaction.created` reports booked debit and credit. The examples are TEST illustrations, not proof that a particular live top-up completed (raw lines 394–416, 579–711, 870–1001).

## Detail locators

- Funding reason, prerequisites, request fields and TEST request: raw lines 15–70.
- API response and refusal example: raw lines 352–392.
- Webhook types and outgoing liable leg: raw lines 394–711.
- Incoming multi pay-in leg and booked credit: raw lines 713–1001.

## Related

- [[adyen]]
- [[adyen-multi-pay-in]]
- [[adyen-platform-internal-transfers]]
- [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/multi-pay-in/top-up-multi-pay-in/2026-09-15|Pinned multi pay-in top-up guide]]
