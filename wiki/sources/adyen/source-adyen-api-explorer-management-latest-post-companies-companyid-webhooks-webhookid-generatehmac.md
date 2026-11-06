---
title: "Adyen Management API v3: generate a company webhook HMAC key"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/webhooks/(webhookId)/generateHmac"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/webhooks/(webhookId)/generateHmac/2026-11-05.md"
tags: [adyen, management-api, webhooks, hmac]
---

## Overview

This 2026-11-05-captured Management API v3 TEST reference describes `POST /companies/{companyId}/webhooks/{webhookId}/generateHmac`. It returns an HMAC key for the webhook configuration identified by `webhookId` under the company account identified by `companyId`. Adyen says creating the key starts HMAC-signed notifications; the key is for checking notification integrity and origin. See [[adyen-webhooks]] and [[adyen-api-access]].

## Key takeaways

- Both path IDs are required strings. The caller's API credential needs the `Management API—Webhooks read and write` role. The captured server is `https://management-test.adyen.com/v3`; this source does not document a request body, defaults, limits, or a live server.
- A 200 response requires an `hmacKey` string generated for this webhook. This establishes success of the key-generation request, not verification of a received notification, successful delivery, or a payment outcome.
- The page lists 400 request problem, 401 authentication required, 403 insufficient permissions, 422 validation error, and 500 server processing failure. It states no idempotency, key-rotation/expiry, propagation timing, deletion, or rollback contract. Do not infer those from the success example.

## Detail locators

- Purpose, effect and role: raw lines 5–11.
- Captured server and path identities: raw lines 13–22.
- Success response and error schemas: raw lines 24–132.
- Illustrative 200 response: raw lines 134–143.

## Related

- [[adyen-webhooks]] — webhook delivery and signature context.
- [[adyen-api-access]] — API credential and role context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/webhooks/(webhookId)/generateHmac/2026-11-05|POST company webhook generateHmac, captured 2026-11-05]]