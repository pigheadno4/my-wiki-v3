---
title: "DELETE /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId} — Delete a balance webhook setting | Adyen"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/(settingId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/delete/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/(settingId)/2026-11-02.md"
tags: [adyen, balance-platform, balance-webhooks, settings, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents deletion of one balance webhook setting containing conditions that trigger balance webhooks. The required path identifies the balance platform, balance webhook and setting separately; this operation concerns notification configuration, not a payment or balance transfer. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; `latest` appears in the reference URL while `/bcl/v2` identifies the captured API path. See [[adyen-platforms]] for platform context.

## Key takeaways

- `balancePlatformId`, `webhookId` and `settingId` are all required string path parameters, identifying the platform, webhook and setting respectively. The page lists no request body, query parameter, default or limit for this DELETE. [Raw: lines 5–19]
- A 204 is described as successful processing with no additional content. The endpoint says it deletes the setting that contains trigger conditions; the response contains no resulting resource or event-delivery state. The separate, older [[source-adyen-docs-platforms-balance-updates-manage-balance-webhook|2026-09-15 pilot management guide]] describes deleting a setting as permanently stopping webhooks for its specified conditions, while distinguishing temporary deactivation and removal of conditions. That guide's qualification and date should remain attached to its broader notification-effect claim. [Raw: lines 7, 21–24; companion guide raw: lines 224–253]
- The page lists 400 request-reading/understanding, 401 authentication, 403 insufficient permissions, 404, 422 validation and 500 server-processing errors. Its error-body fields are optional at the top level, including `detail`, `errorCode`, HTTP `status`, `title` and `type`; the `invalidFields` array is optional, with required child fields only within an included validation item. [Raw: lines 27–138]

> [!warning] Contradiction
> The 404 heading is followed by “The payment was not found” even though this endpoint deletes a balance webhook setting and the required IDs are platform, webhook and setting IDs. The captured page does not resolve whether that 404 wording is generic or what missing-resource condition it represents; do not treat it as evidence of a payment lookup or payment deletion. [Raw: lines 5–19, 84–100]

## Detail locators

- Purpose, TEST v2 server and required path identities: pinned raw lines 5–19.
- 204 success and no-content contract: lines 21–24.
- Error headings and body schemas, including the mismatched 404 wording: lines 27–138.

## Related

- [[adyen-platforms]] — platform and balance-account notification context.
- [[source-adyen-docs-platforms-balance-updates-manage-balance-webhook]] — separately captured pilot guide for viewing, deactivating and deleting settings; its lifecycle explanation is dated and distinct from this endpoint's 204 schema.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/delete/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/(settingId)/2026-11-02|DELETE balance webhook setting — captured 2026-11-02]]