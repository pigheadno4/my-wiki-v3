---
title: "Remove a merchant webhook | Adyen Management API v3"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/delete/merchants/(merchantId)/webhooks/(webhookId)"
raw_files:
  - "adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/webhooks/(webhookId)/2026-11-05.md"
tags: [adyen, management-api, webhooks, merchant-accounts]
---

## Overview

This [[adyen]] Management API `latest` reference, captured 2026-11-05, describes `DELETE /merchants/{merchantId}/webhooks/{webhookId}`: remove the webhook configuration identified by the merchant-account and webhook IDs in the path. The listed server is TEST `https://management-test.adyen.com/v3`. The caller's API credential must have `Management API—Webhooks read and write`. See [[adyen-webhooks]] for webhook context and [[adyen-api-access]] for API credential scope.

## Key takeaways

- The required string `merchantId` identifies the merchant account; the required string `webhookId` identifies the webhook configuration. This capture documents no query parameters, request body, defaults or limits. [Raw: lines 16–22]
- `204` is the listed success status. The reference provides no success response fields or resource readback and says to inspect the actual response code for request status. The operation removes the named configuration; the capture does not specify propagation timing, effects on already queued or in-flight notifications, or whether another configuration covers the same events. [Raw: lines 5–7, 24–27]
- The documented failures are `400` request interpretation, `401` authentication, `403` insufficient permission, `422` validation and `500` server processing. Their response tables define problem-detail fields, including optional `requestId`; see the raw for exact nested requiredness. [Raw: lines 30–127]
- This is configuration deletion, not a test or confirmation of webhook delivery, HMAC verification, payment authorization, settlement, account eligibility or compliance. The endpoint capture states no idempotency or reversal contract, asynchronous review/approval/activation stage, or Live server. Its `latest` label and capture date do not establish present availability.

## Detail locators

- Purpose, caller role, TEST v3 server and path identities: pinned raw lines 5–22.
- Success status and absence of a success body schema: pinned raw lines 24–29.
- Error categories and response schemas: pinned raw lines 30–127.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/webhooks/(webhookId)/2026-11-05|Management API merchant webhook DELETE — captured 2026-11-05]]