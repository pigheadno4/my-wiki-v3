---
title: "Payout Service path: track balance updates"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/balance-updates"
raw_files:
  - "adyen/docs/payouts/payout-service/balance-updates/2026-09-15.md"
tags: [adyen, payout-service, platforms, balance-accounts, balance-webhooks]
---

## Overview

This 2026-09-15 [[adyen]] page appears under the **Payout Service** path but describes a **balance-platform Balance webhook** pilot for balance-change notifications. A setting may cover every balance account in a platform, all accounts of a specific account holder, or one balance account. The page explains subscription, settings scope and inheritance; it is not evidence that the pilot is enabled for an account, that an event arrived, or that a payment, payout, refund or top-up completed. [[adyen-platforms]]

## Key takeaways

- Balance changes can occur within payment lifecycles or financial products; the page gives payments, payouts, refunds and chargebacks as examples affecting Available. These are illustrative causes, not a universal timing or amount rule. Balance webhooks are explicitly **limited availability / pilot**, with processes and documentation subject to change. See raw lines 19–32.
- Subscribe to the Balance webhook in Customer Area and retain its ID, then POST settings to `/balancePlatforms/{id}/webhooks/{id}/settings` with the webhook ID and triggering criteria. The target may be `balancePlatform`, `accountHolder`, or `balanceAccount`; when conditions match, Adyen describes a webhook to the configured server. Detailed roles, limits and security setup belong to the child configuration guide. See raw lines 34–47 and 59–67.
- Platform-level settings are described as inherited by connected accounts; account-holder and balance-account settings are described as overriding broader settings. The table also says granular levels inherit higher-level settings, without spelling out exactly how inherited and overriding criteria combine. Do not assume a particular merge rule from this overview. See raw lines 49–57.
- This overview says **all** conditions must match, but the linked configuration guide's `status=active` row says **any** condition may trigger while its own `conditions` row says all. Compound-condition behavior remains unresolved across the captured pages; confirm current API semantics before relying on it for automatic controls. See raw line 47 and [[source-adyen-docs-payouts-payout-service-balance-updates-configure-balance-webhook]] raw lines 88–90.

## Detail locators

- **Pilot, example causes and target scopes:** raw lines 15–32.
- **Subscribe, settings POST, target types and condition wording:** raw lines 34–47.
- **Inheritance/override text and table:** raw lines 49–57.
- **Child configuration and management routes:** raw lines 59–67.

## Related

- [[adyen-platforms]]
- [[adyen-payouts]] — Payout Service documentation path, distinct from legacy Payout API
- [[source-adyen-docs-payouts-payout-service-balance-updates-configure-balance-webhook|Detailed configuration guide]]
- [[source-adyen-docs-platforms-balance-updates|Parallel Platforms-path overview]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/balance-updates/2026-09-15|Adyen Payout Service path balance updates — collected 2026-09-15]]
