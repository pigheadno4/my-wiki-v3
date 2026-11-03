---
title: "Adyen Balance Platform API v2: PATCH balance webhook setting by ID"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/(settingId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/patch/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/(settingId)/2026-11-02.md"
tags: [adyen, balance-platform, webhooks, balance-accounts, configuration]
---

## Overview

This 2026-11-02 Balance Platform API reference describes PATCHing a Balance webhook setting's balance-change notification conditions. Its captured server is the TEST `https://balanceplatform-api-test.adyen.com/bcl/v2` endpoint. The `latest` URL is a documentation route, not independently verified live availability. The setting is scoped by distinct balance-platform, webhook, and setting IDs. See [[adyen]], [[adyen-webhooks]] and [[adyen-platforms]].

## Key takeaways

- All three string path IDs are required: `balancePlatformId`, `webhookId`, and `settingId`. The request-body table marks `conditions`, `currency`, `status`, `target`, and `type` optional, and does not separately state that a body is required. Within a supplied `conditions` element, `balanceType`, `conditionType`, and integer `value` are marked required. `conditions` itself is typed `array,null`; the API page does not state the effect of `null` or an empty array.
- `balanceType` distinguishes `available`, settled `balance`, `pending`, and `reserved`. `conditionType` offers greater-than, greater-than-or-equal, less-than, and less-than-or-equal thresholds; `value` is in minor units of the selected balance type and currency. The optional target can identify a balance platform, account holder, or balance account. The request `type` description says set it to `balance`. The examples show deactivation with `type: balance` and `status: inactive`, and an active balance-account threshold setting; example IDs and amounts are illustrative.
- The status descriptions say `active` can send a Balance webhook when any condition is met and `inactive` suppresses it even if conditions match. The 200 schema marks `currency`, setting `id`, `status`, `target` (with `id` and `type`), and setting `type` required; the 200 examples also include `conditions`, which that response table does not list. A 200 confirms this PATCH request succeeded and returns configuration, not delivery of a notification or evidence of a balance change or money movement.
- The documented errors are 400, 401, 403, 404, 422 and 500. The 404 heading says “The payment was not found” despite this being a webhook-setting endpoint; do not infer a payment lookup or payment outcome. The page does not specify a caller role, idempotency key, conflict/version rule, propagation timing, delivery guarantee, or reversal behavior.

> [!warning] Contradiction
> This November API reference marks request `type` optional, while the 2026-09-15 [[source-adyen-docs-platforms-balance-updates-manage-balance-webhook|Platforms management guide]] marks `type` required for PATCH (its raw line 133). Its `active` description says **any** condition can trigger, while the 2026-09-15 [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook|Platforms configuration guide]] says **all** conditions must match (its raw line 90). The captured documents do not resolve multi-condition behavior or current request validation. The management guide additionally says to send all conditions to retain when updating and that removing the last condition broadens alerts to all balance changes (its raw lines 155–157, 191–195, 243–245); this API reference alone does not define those PATCH replacement semantics.

## Detail locators

- Operation, TEST server, required path IDs and request field table: pinned raw lines 5–34.
- Deactivate and update request examples: pinned raw lines 36–69.
- 200 response fields and error schemas: pinned raw lines 70–198; note 404 wording at lines 144–145.
- 200 response examples with `conditions` absent from response field table: pinned raw lines 200–253.

## Related

- [[adyen-webhooks]] — event notification context.
- [[adyen-platforms]] — platform/account-holder/balance-account context.
- [[source-adyen-docs-platforms-balance-updates-manage-balance-webhook]] — dated pilot lifecycle guide and condition retention/deletion guidance.
- [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]] — dated pilot configuration guide with conflicting all-condition statement.
- [[source-adyen-api-explorer-balance-webhooks-latest-post-balanceplatform-balanceaccount-balance-updated]] — separate event reference; configuration is not event delivery.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/patch/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/(settingId)/2026-11-02|Balance Platform PATCH webhook setting snapshot]]