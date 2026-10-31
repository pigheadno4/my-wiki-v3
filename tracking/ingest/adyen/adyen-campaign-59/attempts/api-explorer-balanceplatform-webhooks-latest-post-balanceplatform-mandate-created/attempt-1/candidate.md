---
title: "Adyen Balance Platform mandate created webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.mandate.created"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.mandate.created/2026-09-15.md"
tags: [adyen, balance-platform, webhooks, mandates, direct-debit]
---

## Overview

This 2026-09-15-captured API Explorer `latest` POST reference describes the incoming `balancePlatform.mandate.created` webhook Adyen sends when a direct debit mandate is created. The linked context is UK direct debits, while this event page's `mandate.type` lists `bacs`. Creation alone does not establish mandate approval or a collected debit. [[adyen]] [[adyen-webhooks]] [[adyen-business-accounts]]

## Key takeaways

- The envelope requires `data`, `environment`, and `type`. `data.balancePlatform` and `data.mandate` are optional in the displayed table. All listed nested mandate fields are also marked optional, including `id`, linked `balanceAccountId` and `paymentInstrumentId`, `counterparty`, and creation/update dates. See raw lines 11–27.
- `mandate.status` can be `pending`, `approved`, or `cancelled`; the page does not specify that the created event implies `approved`. Its only listed mandate type is `bacs`. There is no request example or status-transition sequence in this reference. See raw lines 17–29.
- The response table says any 2xx HTTP status accepts the webhook and marks `notificationResponse` optional. It does not specify delivery order, retry/deduplication, signature verification, or debit outcome. See raw lines 29–37.

## Detail locators

- Event purpose: raw lines 5–7.
- Envelope and mandate fields: raw lines 9–27.
- Acknowledgment: raw lines 29–37.

## Related

- [[adyen-webhooks]]
- [[adyen-business-accounts]]

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.mandate.created/2026-09-15|Mandate created webhook reference, captured 2026-09-15]]
