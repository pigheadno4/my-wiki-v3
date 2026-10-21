---
title: "Adyen Marketplace internal push-transfer returns"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/internal-fund-transfers/return-transfers"
raw_files:
  - "adyen/docs/marketplaces/internal-fund-transfers/return-transfers/2026-09-15.md"
tags: [adyen, marketplaces, platforms, internal-transfers, returns, balance-accounts]
---

## Overview

This 2020-modified, 2026-09-15-captured [[adyen]] Marketplace guide explains returning funds mistakenly moved between balance accounts to the sender of the original **internal push transfer**. The return is a modification of that original transfer in [[adyen-platform-internal-transfers]], not a fresh internal transfer or an external bank payout. It uses the original incoming transfer ID; an authorised return request is not evidence that both balance-account legs have booked.

## Key takeaways

- This return path works only when the original internal transfer was a **push**. The server must receive and accept webhooks with Transfer webhook added in Customer Area; Support must enable transfers for the balance account **where funds are returned from**. The API credential needs Transfers API access and **TransferService Webservice Initiate** role. If the two balance accounts belong to different account holders, the returning-account holder needs `sendToBalanceAccount`, and the original source/return-recipient holder needs `receiveFromBalanceAccount`. Those capability checks are stated conditionally for different holders, not as universal same-holder requirements. See raw lines 17–37.
- POST `/transfers/{transferId}/returns` uses the ID of the **original incoming transfer** from the webhooks. The request table marks `amount` required and says currency and value must be the same as the original transfer; `reference` is an optional unique return reference. Thus the page describes an equal-amount return, not a partial-return procedure. The EUR 100 example targets the TEST Balance Platform Transfers API v4 endpoint, and the SDK snippets are versioned examples rather than live-operation proof. See raw lines 39–291.
- The response `id` is the return-request ID, whereas `transferId` is the original incoming transfer ID provided in the URL. The prose describes `Authorised`, and the sample JSON uses lowercase `authorised`; `Declined` **can** indicate a wrong URL ID, not necessarily the only cause. These are request states, not confirmation of booked return movement. See raw lines 293–308.
- Track the return and possible failure with the linked internal-transfer webhooks, or view it in Customer Area. The separate webhook guide describes nested return-modification states and the two account views at booking. This page itself supplies no booked webhook payload, bank receipt, retry rule or proof of a specific transfer. See raw lines 310–314 and [[source-adyen-docs-marketplaces-internal-fund-transfers-internal-transfer-webhooks]].

## Detail locators

- Push-only original transfer and same-transfer modification: raw lines 17–21.
- Webhook, Support, conditional cross-holder capability and credential gates: raw lines 23–37.
- Original incoming ID, matching amount/currency and TEST request examples: raw lines 39–291.
- Return-request versus original-transfer IDs, Authorised/Declined qualification and tracking: raw lines 293–314.

## Related

- [[adyen]] — provider profile.
- [[adyen-platform-internal-transfers]] — canonical internal balance-account movement concept.
- [[adyen-platforms]] — modern platform context.
- [[source-adyen-docs-marketplaces-internal-fund-transfers-internal-transfer-webhooks]] — return modification and booked account-leg evidence.
- [[source-adyen-docs-platforms-internal-fund-transfers-return-transfers]] — separate Platforms URL for the related guide.

## Raw Sources

- [[raw/adyen/docs/marketplaces/internal-fund-transfers/return-transfers/2026-09-15|Marketplace internal push-transfer return — pinned 2026-09-15 raw snapshot]]
