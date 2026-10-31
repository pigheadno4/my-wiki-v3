---
title: "Adyen Balance webhook v1 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balance-webhooks/latest/overview"
raw_files:
  - "adyen/api-explorer/balance-webhooks/latest/overview/2026-09-15.md"
tags: [adyen, webhooks, balance-platform, balances]
---

## Overview

This 2026-09-15-captured API Explorer overview labels the family **Balance webhook v1**. Adyen says these webhooks inform recipients of balance changes in a balance platform. It lists event routes for blocked-funds release and balance update; this overview is a catalog and does not give either event's payload schema. The `latest` route is not independent proof of a newer or current version. See [[adyen]], [[adyen-webhooks]] and [[adyen-platforms]].

## Key takeaways

- The page says the Configuration API can set conditions for sending balance-change webhooks across the entire balance platform, balance accounts of specified account holders, or one balance account. The linked settings route is navigation to a separate contract; this overview does not specify condition semantics, subscription state or current eligibility.
- The two listed incoming POST event types are `balancePlatform.balanceAccount.balance.block.released` and `balancePlatform.balanceAccount.balance.updated`. The listing gives only their names and summaries. A notification of balance change does not by itself prove a transfer, payout, settlement or bank receipt.

## Detail locators

- Family label and purpose: pinned raw title/introduction, lines 5–7.
- Configuration API condition scopes: raw lines 9–15.
- Listed incoming event routes: `## Endpoints > ### General`, lines 17–23.

## Related raw API references

- [[raw/adyen/api-explorer/balance-webhooks/latest/post/balancePlatform.balanceAccount.balance.block.released/2026-09-15|Blocked-funds release event reference]] — navigation only; separate event schema.
- [[raw/adyen/api-explorer/balance-webhooks/latest/post/balancePlatform.balanceAccount.balance.updated/2026-09-15|Balance update event reference]] — navigation only; separate event schema.

## Raw Sources

- [[raw/adyen/api-explorer/balance-webhooks/latest/overview/2026-09-15|Balance webhook v1 overview snapshot]]
