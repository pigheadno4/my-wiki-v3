---
title: "Return transferred funds | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/internal-fund-transfers/return-transfers"
raw_files:
  - "adyen/docs/platforms/internal-fund-transfers/return-transfers/2026-09-15.md"
tags: [adyen, platforms, internal-transfers, returns, balance-accounts]
---

## Overview

This 2020-last-modified [[adyen]] for Platforms guide, captured 2026-09-15, explains how to return funds mistakenly sent between balance accounts **to the sender of the original internal push transfer**. The return is a modification of that original transfer, not a fresh internal transfer or an external bank payout. The request uses the original incoming transfer ID; the return request has its own ID. A response marked `authorised` is not proof that the return was booked to the source balance account. [[adyen-platform-internal-transfers]]

## Conditions and request

- The return path works only when the original internal transfer was a **push** transfer. The server must receive and accept webhooks and have Transfer webhooks configured; Support must enable transfers for the balance account **where the funds are returned from**. When the two balance accounts belong to different account holders, the holder of the returning account needs `sendToBalanceAccount` and the holder of the original source/return destination needs `receiveFromBalanceAccount`. The API credential needs Transfers API access and **TransferService Webservice Initiate** role. Do not generalize those conditional cross-holder capability checks to every same-holder return. See raw lines 17–37.
- POST `/transfers/{transferId}/returns` uses the ID of the **original incoming transfer** from webhook evidence, not a new outbound transfer ID. The request table marks `amount` required and says its currency and value must match the original transfer; `reference` is an optional unique return reference. The EUR 100 example uses the test balance-platform v4 endpoint and versioned client snippets, so it does not prove current live access or completed movement. The page does not describe a partial-return route. See raw lines 39–52 and 58–291.

## Response and outcome evidence

- The response's `id` identifies the **return request**, while `transferId` refers back to the original incoming transfer supplied in the URL. The page describes `status: authorised`; a `Declined` status **can** indicate a wrong URL transfer ID, not necessarily that it is the only possible cause. The sample JSON uses lowercase `authorised`. These fields identify an accepted request state, not the final two-sided balance movement. See raw lines 293–308.
- Track the return through Adyen's internal-transfer webhooks, which provide request status and failure updates, or view it in Customer Area. Use the actual outgoing and incoming booked legs when claiming funds returned to the source balance account. This guide provides no booked-event payload, bank statement, payout, retry rule or legal-fund ownership proof. See raw lines 310–314 and the linked internal-transfer webhook route.

## Detail locators

- **Original push-only return and same-transfer modification:** raw lines 15–21.
- **Webhook, Support, cross-holder capability and API-role prerequisites:** raw lines 23–37.
- **Original incoming ID, equal amount/currency and test request examples:** raw lines 39–291.
- **Return-request ID, original transfer ID, Authorised/Declined qualification and tracking route:** raw lines 293–314.

## Related

- [[adyen-platform-internal-transfers]]
- [[adyen-platforms]]
- [[source-adyen-docs-platforms-internal-fund-transfers-internal-transfer-webhooks]] — separate outcome-event detail

## Raw Sources

- [[raw/adyen/docs/platforms/internal-fund-transfers/return-transfers/2026-09-15|Adyen Platforms internal-transfer return guide — collected 2026-09-15]]
