---
title: "Adyen Management API v3: test a merchant webhook"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/webhooks/(webhookId)/test"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/webhooks/(webhookId)/test/2026-11-05.md"
tags: [adyen, management-api, webhooks, testing]
---

## Overview

This 2026-11-05-captured Adyen Management API reference describes `POST /merchants/{merchantId}/webhooks/{webhookId}/test`. It sends sample notifications to test a merchant webhook configuration and returns test results, including the receiver's HTTP response. The listed server is `https://management-test.adyen.com/v3`; the API credential needs the **Management API—Webhooks read and write** role. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- Required string path IDs are `merchantId` for the merchant account and `webhookId` for the webhook configuration. The body schema marks `types` optional and lists supported event codes by webhook type; `notification` is an optional custom test notification object but is **required when `types` contains `CUSTOM`**. Within an included `notification.amount`, `currency` and minor-unit integer `value` are required. The page gives no default for an omitted `types` list.
- For each chosen event code, the reference says Adyen sends four test notifications spanning success/failure scenarios in hard-coded EUR and GBP, regardless of merchant configured currencies. For `CUSTOM`, it says only the specified custom notification is sent.
- HTTP `200` has an optional `data` array of per-test results; each element's `status` is required and is `success` when the receiver returns `2xx`, otherwise `failed`. Optional fields include `merchantId`, `output`, sent notification body, receiver `responseCode`, and `responseTime` in milliseconds. HTTP `204` is separately documented as processed without additional content.
- A successful test reports the sample webhook receiver's response. Neither a sample notification's `success` field nor the test `status` proves a real payment, production delivery, later webhook reliability, or financial finality. The captured page does not specify idempotency or a live server.

> [!warning] Contradiction
> The custom request example sets HUF `notification.amount.value` to `1000` (raw lines 57–71), but its `200` response example embeds a `requestSent` notification with HUF `value` `100` (raw lines 213–223). The examples do not establish that the sent amount echoes the submitted custom amount exactly.

## Detail locators

- Purpose, number/currencies of samples, credential role, TEST server, and path IDs: raw lines 5–26.
- Optional and conditional body fields, supported `types` by webhook type, and custom notification subfields: raw lines 29–42.
- Standard and custom request examples: raw lines 44–72. The custom example is an illustration, not a payment result.
- `200`/per-test result schema and `204` no-content response: raw lines 73–91; response examples: raw lines 193–226.
- `400`, `401`, `403`, `422`, and `500` problem responses: raw lines 94–191. `401` requires authentication; `403` means insufficient permission.

## Related

- [[adyen-webhooks]] — webhook configuration, receipt, and testing context.
- [[adyen-api-access]] — API credential context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/webhooks/(webhookId)/test/2026-11-05|Adyen Management API merchant webhook test, captured 2026-11-05]]
