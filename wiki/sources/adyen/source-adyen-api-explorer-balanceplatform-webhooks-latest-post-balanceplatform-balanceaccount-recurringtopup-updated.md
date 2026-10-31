---
title: "Adyen Balance Platform recurring top-up updated webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.recurringTopUp.updated"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.recurringTopUp.updated/2026-09-15.md"
tags: [adyen, balance-platform, webhooks, recurring-top-ups]
---

## Overview

This 2026-09-15-captured API Explorer `latest` POST reference defines the incoming `balancePlatform.balanceAccount.recurringTopUp.updated` webhook Adyen sends when a recurring top-up configuration is successfully updated for a balance account. It is an event contract, not a merchant update operation or proof of a direct debit or booked credit. [[adyen]] [[adyen-webhooks]] [[adyen-issuing]]

## Key takeaways

- The request body requires `data`, `environment`, and `type`. Within `data`, `accountId` identifies the balance account and `webhookTopUpConfiguration` is required; the configuration requires `id`, `counterparty`, `description`, `status`, `topUpAmount`, and `trigger`. See raw lines 11–32.
- Configuration status is `active` (enabled for funds to be pulled in) or `inactive` (disabled and cannot be triggered). `disabledReason` and `reasonDetail` are optional fields populated only when inactive. `topUpAmount` can be fixed or target, and `trigger` can be a schedule or minimum-balance threshold; this page gives no nested required-field table for those objects. See raw lines 19–29.
- `balancePlatform`, `creationDate`, outer `data.id`, `timestamp`, `mandate`, and `referenceForBeneficiary` are optional in this table. `creationDate` is event-trigger time, whereas `timestamp` is queue time. The configuration `id` is required and distinct from optional outer `data.id`. See raw lines 15–32.
- The test example shows an inactive configuration, EUR fixed amount and threshold, a counterparty transfer instrument, mandate and disabled reason. Those are example values, not universal payload requirements or evidence that a funding transfer occurred. The response section says any HTTP 2xx accepts the webhook and shows an optional `notificationResponse` example. See raw lines 34–96.

## Detail locators

- Envelope, account and configuration fields: raw lines 9–32.
- Example JSON, including event type and test environment: raw lines 34–76.
- Acknowledgment response: raw lines 77–96.

## Related

- [[adyen-webhooks]]
- [[adyen-issuing]]
- [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.recurringTopUp.updated/2026-09-15|Recurring top-up updated webhook reference, captured 2026-09-15]]
