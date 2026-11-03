---
title: "Adyen Balance Platform API v2: Get all balance webhook settings"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/2026-11-02.md"
tags: [adyen, balance-platform, webhooks, configuration, api]
---

## Overview

This 2026-11-02 [[adyen]] Balance Platform API Explorer capture documents `GET /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings` on the listed TEST `/bcl/v2` server. It reads the balance webhook settings configured under one balance platform and balance webhook. It does not create a setting, send a webhook, change a balance, or report a payment or payout outcome. The `latest` URL segment and TEST server do not prove current version, LIVE availability, subscription or account access.

## Key takeaways

- Both path parameters are required strings: `balancePlatformId` identifies the balance platform and `webhookId` the balance webhook. This page lists no query or body parameters, defaults, pagination or result-count limits.
- The 200 schema marks the `webhookSettings` array optional. For each setting object, it marks `currency` (three-character ISO balance currency), setting `id`, `status`, `target` and `type` required. `target.id` and `target.type` are required within `target`; the target type may identify the whole `balancePlatform`, an `accountHolder` or one `balanceAccount`. The setting ID is distinct from both path IDs and from the target resource ID.
- The status row describes `active` as receiving a balance webhook if any setting condition is met, and `inactive` as suppressing it even if conditions are met. The two setting objects in the single named 200 response example contain `conditions` and threshold values, but the 200 schema table does not list a `conditions` field or define its requiredness. A listed active status or threshold is configuration readback, not evidence of webhook delivery or a balance change.

> [!warning] Contradiction
> This endpoint's status row says **any** condition can trigger an active setting (raw line 31). The separately captured [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook|Balance webhook configuration guide]] says **all** configured conditions must match (its raw lines 88–90), while its own status row also says any. Multi-condition Boolean behavior remains unresolved in these captures; do not treat either wording as a tested delivery guarantee.

> [!warning] Contradiction
> The 404 row says “The payment was not found” (raw lines 95–96), although the title, path and 200 schema concern webhook settings. Do not reinterpret this GET as a payment lookup or infer which webhook-setting absence yields 404 from that row.

- The page lists 400 request, 401 authentication, 403 permission, 404, 422 validation and 500 server errors. Error bodies have optional detail, error code, request ID, status and other problem fields; `invalidFields` is optional, with required `message`, `name` and `value` inside each returned item. The page specifies no idempotency header, mutation, deletion, propagation timing, delivery/retry contract or reversal for this GET.

## Detail locators

- Raw lines 5–18: purpose, TEST v2 server and required path IDs.
- Raw lines 20–35: 200 response schema, optional list and required fields within returned setting objects.
- Raw lines 38–149: 400, 401, 403, 404, 422 and 500 errors; the anomalous 404 text is at lines 95–96.
- Raw lines 151–195: one named 200 response example containing two setting objects with balance-platform/balance-account targets and conditions.
- Related configuration guide raw lines 88–90: all-versus-any condition-language conflict; this guide is separate authority, not the assigned raw.

## Related

- [[adyen]]
- [[adyen-webhooks]]
- [[adyen-platforms]]
- [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]]
- [[source-adyen-docs-platforms-balance-updates-manage-balance-webhook]]

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/2026-11-02|Adyen Balance Platform API Explorer GET all balance webhook settings (captured 2026-11-02)]]
