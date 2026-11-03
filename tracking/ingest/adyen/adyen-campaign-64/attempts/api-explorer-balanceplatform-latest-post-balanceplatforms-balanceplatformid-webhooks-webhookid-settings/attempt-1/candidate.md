---
title: "Adyen Balance Platform API v2: Create a balance webhook setting"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/2026-11-02.md"
tags: [adyen, platforms, balance-platform, webhooks, api-reference]
---

## Overview

Captured Balance Platform API v2 TEST-server `POST /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings` reference. It creates criteria for balance-change webhook notifications, scoped to a balance platform, account holder, or balance account. This configuration resource is part of [[adyen]] and [[adyen-platforms]]; its creation is separate from any balance-change event or money movement.

## Key takeaways

- Both path IDs are required: `balancePlatformId` identifies the balance platform and `webhookId` identifies the balance webhook being configured. The listed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`. The body requires `currency`, `status`, `target`, and `type: balance`; `target` requires a resource `id` and a `type` of `balancePlatform`, `accountHolder`, or `balanceAccount`.
- `conditions` is an optional array, but its listed members `balanceType`, `conditionType`, and integer `value` are marked required within each condition. `value` is in minor units. The documented balance types are available, balance, pending, and reserved; comparisons are greaterThan, greaterThanOrEqual, lessThan, and lessThanOrEqual. The raw does not specify a default or number limit for conditions.
- Settings at a higher level apply to lower resources, and the most granular setting overrides higher settings: balance account over account holder over balance platform. `active` means a balance webhook is received if any configured condition is met; `inactive` means it is not received even if conditions are met. The reference does not specify the delivery timing or prove any notification was sent.
- The 200 response says the request succeeded and returns a webhook-setting `id`, `currency`, `status`, `target`, and `type`. Its example also shows conditions, although the response field table does not list conditions. This response establishes configuration creation, not a balance threshold crossing or settlement, payout, or bank receipt.

## Detail locators

- Purpose, hierarchy and TEST server: pinned raw lines 5–18. Path/body schema and minor-unit condition values: lines 20–41. Request example: lines 43–63.
- 200 response table and example: lines 64–78 and 194–216. The listed error classes are 400, 401, 403, 404, 422, and 500 (lines 81–192). The 404 prose says `The payment was not found` despite this being a webhook-setting route; do not infer a payment lookup from that generic error description.

## Related

- [[adyen-platforms]] — platform resource and webhook context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/2026-11-02|Pinned 2026-11-02 API reference]]
