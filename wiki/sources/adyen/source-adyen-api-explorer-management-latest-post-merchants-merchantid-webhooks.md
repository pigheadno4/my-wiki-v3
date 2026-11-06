---
title: "Set up a merchant webhook | Adyen Management API v3"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/webhooks"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/webhooks/2026-11-05.md"
tags: [adyen, management-api, merchant-webhooks, configuration]
---

## Overview

This 2026-11-05-captured Management API reference describes `POST /merchants/{merchantId}/webhooks`, which configures a subscription to webhook notifications for merchant-account events. The listed server is TEST `https://management-test.adyen.com/v3`; the path's required `merchantId` identifies the merchant account. The caller's API credential requires **Management API—Webhooks read and write**. Optional username/password fields can add basic authentication for the recipient URL. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The request-body property table marks `active`, `communicationFormat`, `type` and the public recipient `url` required. `active` must be `true` for Adyen to send account-event webhooks; this is a necessary configuration state, not a delivery guarantee. The listed formats are `soap`, `http` and `json`. The table does not separately declare whole-body requiredness or an idempotency rule. Its detailed type list and standard-webhook `additionalSettings` fields are in raw lines 31–42.
- Expired, self-signed and untrusted-root certificate acceptance flags each default to `false`. Optional `encryptionProtocol` permits `TLSv1.3`, `TLSv1.2` or TEST-only `HTTP`; absent a value, the table says `sslVersion: TLSv1.2`. Optional `networkType` defaults to `public`; `populateSoapActionHeader` defaults to `false` and applies only to SOAP. The sample's `true` self-signed and untrusted-root flags are example values, not a security recommendation.
- A `200` marks the request succeeded and can return the webhook's `id`, `active`, `type`, `url`, communication and certificate settings, `hasError`, `hasPassword`, `hmacKeyCheckValue` and optional resource links. The `generateHmac` and `testWebhook` links are available operations, not proof that an HMAC key was generated or that a webhook test or delivery passed. A `204` says processing succeeded without additional content. The response schema's company-level filter fields do not make this merchant-path call a company-level configuration.
- The page lists `400`, `401`, `403`, `422` and `500` errors. It gives no delivery, propagation, retry, deletion/reversal or asynchronous approval guarantee. A configured webhook is separate from an emitted event, receiver acknowledgement and any payment or financial result.

> [!warning] Contradiction
> The listed TEST server is `/v3`, while the `200` example's self, HMAC, merchant and test links use `/v1`. The example does not resolve the versioned route or a Live URL.

> [!warning] Contradiction
> The request `type` list includes `rreq-notification` but does not list `terminal-api-notification`; the `200` response `type` list does the reverse. The captured tables do not reconcile allowed request values with returned values.

## Detail locators

- Raw lines 5–42: purpose, role, TEST server, merchant path and request schema, including defaults and conditional fields.
- Raw lines 44–60: illustrative request; lines 63–107: `200` response schema and `204` no-content response.
- Raw lines 110–207: error classes and generic error schemas; lines 209–311: illustrative `200` response and `/v1` links.

## Related

- [[adyen-webhooks]] — webhook concept and event-delivery context.
- [[source-adyen-api-explorer-managementnotification-latest-overview]] — separate Management event catalog.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/webhooks/2026-11-05|2026-11-05 merchant webhook setup reference]]