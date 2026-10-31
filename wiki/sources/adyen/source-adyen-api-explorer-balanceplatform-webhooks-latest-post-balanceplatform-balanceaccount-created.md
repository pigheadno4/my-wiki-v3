---
title: "Adyen Balance Platform webhook: balance account created"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.created"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.created/2026-09-15.md"
tags: [adyen, balance-platform, webhooks, balance-accounts]
---

## Overview

This captured Balance Platform Webhooks API Explorer POST reference describes an incoming `balancePlatform.balanceAccount.created` event that Adyen sends when a balance account is successfully created. It is a webhook event contract, not an instruction to create an account. The page's `latest` path is a captured label; the raw does not identify a numbered webhook API version. See [[adyen-webhooks]], [[adyen-platforms]], and [[adyen]].

## Key takeaways

- The request body requires `data`, `environment` (`test` or `live`), and `type`. `timestamp` is optional and describes when the event was queued. The `data.balanceAccount` object and `data.balancePlatform` identifier are marked optional in the table; if `balanceAccount` is supplied, its `accountHolderId` and balance-account `id` are marked required within that object. The example uses `type: balancePlatform.balanceAccount.created`.
- The balance account schema lists optional `balances`, `defaultCurrencyCode`, `description`, `metadata`, `migratedAccountCode`, `platformPaymentConfiguration`, `reference`, `status`, and `timeZone`. Default currency is EUR and cannot change after creation; status defaults to active. The metadata deletion warning concerns an update that omits existing key-value pairs, not this creation event.
- The example is a test-environment payload with account holder ID, balance-account ID, EUR and active status. It illustrates the event shape; it does not prove a specific account's funding, verification, eligibility, payout, or bank receipt. The response section says any HTTP `2xx` accepts the webhook and labels `notificationResponse` optional. It does not establish delivery ordering, deduplication, retry, signature verification, or final financial state for this event.

## Detail locators

- Trigger and event title: pinned raw lines 5–7.
- Envelope, conditional nested fields, default currency, status and metadata qualifications: pinned raw lines 11–30.
- Example payload and event type: pinned raw lines 32–50.
- Acknowledgment response: pinned raw lines 51–59.

## Related

- [[adyen-webhooks]] — webhook family and processing context.
- [[adyen-platforms]] — balance-platform resource context.
- [[source-adyen-api-explorer-balanceplatform-latest-post-balanceaccounts]] — separate balance-account creation API reference.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.created/2026-09-15|Balance account created webhook reference, captured 2026-09-15]]
