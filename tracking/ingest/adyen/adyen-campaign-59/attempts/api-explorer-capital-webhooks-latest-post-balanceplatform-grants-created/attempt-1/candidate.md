---
title: "Adyen Capital grant created webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital-webhooks/latest/post/balancePlatform.grants.created"
raw_files:
  - "adyen/api-explorer/capital-webhooks/latest/post/balancePlatform.grants.created/2026-09-15.md"
tags: [adyen, capital, grant-webhooks, financing]
---

## Overview

This 2026-09-15-captured API Explorer `latest` POST reference describes Adyen's incoming `balancePlatform.grants.created` webhook after a Capital grant is created. The page gives grant data and status fields, not evidence that principal was disbursed, received in a bank, or repaid. [[adyen]] [[adyen-capital]] [[adyen-webhooks]]

## Key takeaways

- The displayed body requires `balances`, `grantAccountId`, `grantOfferId`, grant `id`, and `status`. Within `balances`, currency, fee, principal and total are required; total is described as fee plus principal. These are grant amounts, not a confirmation of money movement. See raw lines 11–26.
- Optional `counterparty` can identify the receiving account holder, balance account or transfer instrument, with ownership qualifications in the field descriptions. The page does not mark any of its nested IDs required. See raw lines 19–22.
- `status.code` is required and lists Pending, Active, Repaid, WrittenOff, Failed, Revoked, Requested, Reviewing, Approved, Rejected and Cancelled. Optional `status.actions` entries have required `actionCode` and `resolved` fields. The created-event name does not select one status code or prove completion of actions. See raw lines 26–30.
- The response table says any HTTP 2xx accepts the webhook and marks `notificationResponse` optional. This reference supplies no request example, delivery/order/retry/deduplication/signature rule, disbursement transition or bank-receipt proof. See raw lines 32–40.

## Detail locators

- Purpose and grant data schema: raw lines 5–30.
- Acknowledgment response: raw lines 32–40.

## Related

- [[adyen-capital]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/api-explorer/capital-webhooks/latest/post/balancePlatform.grants.created/2026-09-15|Capital grant created webhook reference, captured 2026-09-15]]
