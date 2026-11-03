---
title: "GET balance webhook setting by ID | Adyen Balance Platform API"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/(settingId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/(settingId)/2026-11-02.md"
tags: [adyen, balance-platform, balance-webhooks, webhook-settings, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `GET /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId}` to read a specific setting configured to trigger Balance webhooks. Its captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; `latest` in the documentation URL does not itself establish a live version. See [[adyen-platforms]] for the platform context.

## Key takeaways

- All three path parameters are required and identify distinct resources: balance platform, Balance webhook, and webhook setting. This GET has no request body or query parameters in the captured page. [Raw: lines 5–19]
- A 200 response requires `currency`, setting `id`, `status`, `target` and `type`. The target requires its own `id` and `type`; target types are `balancePlatform`, `accountHolder`, and `balanceAccount`, which select the scope of balance-change notifications. `active` means a balance webhook is received if any condition in the setting is met; `inactive` means none is received even if conditions are met. This describes configured behavior, not proof of actual webhook delivery for a particular event. [Raw: lines 23–35]
> [!warning] Contradiction
> This GET's status row says an active setting triggers a Balance webhook if **any** condition is met (pinned raw line 31). The related [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook|configuration guide]] says a balance change must meet **all** configured conditions (its raw line 90). The captured sources do not resolve how multiple conditions are combined. Do not infer a reliable compound-alert rule or actual delivery from this read.

- The success example includes `conditions` with available-balance, less-than and numeric value fields, but these are absent from the listed 200 response table. Treat the example as illustrative rather than a complete required schema or a guarantee of an emitted alert. [Raw: lines 26–35, 151–173]
- The page lists 400, 401, 403, 404, 422 and 500 errors. Its 404 description says “The payment was not found,” although this endpoint reads a webhook setting; that text does not establish a payment lookup or payment outcome. [Raw: lines 38–149]

## Detail locators

- Purpose, TEST v2 server and required path identifiers: pinned raw lines 5–19.
- Success response fields and status/target semantics: lines 21–35.
- Error headings and bodies: lines 38–149; illustrative 200 payload: lines 151–173.

## Related

- [[adyen-platforms]] — platform and Balance webhook context.
- [[source-adyen-docs-platforms-balance-updates-manage-balance-webhook]] — separate guide for managing settings.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/(settingId)/2026-11-02|Captured API Explorer page (2026-11-02)]]
