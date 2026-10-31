---
title: "Balance account updated webhook | Adyen Balance Platform webhooks"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.updated"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.updated/2026-09-15.md"
tags: [adyen, platforms, balance-accounts, webhooks]
---

## Overview

This captured `POST balancePlatform.balanceAccount.updated` reference describes an incoming [[adyen-platforms|Adyen for Platforms]] Balance Platform webhook that Adyen sends when a balance account is successfully updated. It is an event contract, not a merchant operation for updating an account. The example identifies `type` as `balancePlatform.balanceAccount.updated`; the captured `latest` URL is not proof of a current version. [[adyen-webhooks]]

## Key takeaways

- The request body marks `data`, `environment` (`test` or `live`), and `type` required. It marks `data.balanceAccount` optional; within that object, `accountHolderId` and balance-account `id` are marked required. `data.balancePlatform` and queued-event `timestamp` are optional. The example is a test event with account-holder and balance-account IDs, default currency, active status and time zone; it does not make those optional fields universal.
- Optional balance-account fields include balances, default currency, description, metadata, migrated Classic account code, platform-payment configuration, reference, status and time zone. The field descriptions say the default currency cannot change after creation; omitted existing metadata key-value pairs during an update are deleted. Those descriptions should not be read as saying that an omitted field in this webhook deletes data.
- A `200 Success` response section says any `2xx` HTTP status code accepts the webhook. Acceptance is a delivery acknowledgment, not proof of a financial balance change, settlement, payout or bank receipt. This reference does not establish ordering, retries, deduplication, signature verification or event finality.

## Detail locators

- Trigger and event identity: raw lines 5–7 and 34–50.
- Request body requiredness, resource IDs, optional fields and environment: raw lines 9–30.
- Example payload: raw lines 32–51.
- Acknowledgment response: raw lines 52–60.

## Related

- [[adyen-platforms]] — balance-account resource and platform context.
- [[adyen-webhooks]] — broader webhook context; this event's exact payload remains in the pinned raw.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.updated/2026-09-15|Captured balancePlatform.balanceAccount.updated reference]]
