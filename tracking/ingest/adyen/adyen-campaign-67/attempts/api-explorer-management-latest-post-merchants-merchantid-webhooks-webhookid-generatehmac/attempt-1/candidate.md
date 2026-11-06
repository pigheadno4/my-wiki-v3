---
title: "Adyen Management API: Generate an HMAC key for a merchant webhook"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/webhooks/(webhookId)/generateHmac"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/webhooks/(webhookId)/generateHmac/2026-11-05.md"
tags: [adyen, management-api, webhooks, hmac]
---

## Overview

This [[adyen]] Management API `latest` reference, captured 2026-11-05, documents `POST /merchants/{merchantId}/webhooks/{webhookId}/generateHmac`. It generates an HMAC key for the identified merchant-account webhook so received notifications can be checked for integrity and origin. The page says creating the key starts HMAC-signed notifications. Its only listed server is `https://management-test.adyen.com/v3`; no Live server is listed here.

## Key takeaways

- The caller's API credential must have the **Management API—Webhooks read and write** role. Both path parameters are required: `merchantId` is the merchant-account identifier and `webhookId` identifies the target webhook. The captured reference lists no request body, query parameters, idempotency header, rate/size limit, or default.
- A `200` means the request succeeded and has a response body with required `hmacKey`. A `204` also means successful processing but has no additional content; do not assume a key is returned for that response. The example key is illustrative and is not a usable credential to copy.
- Generating a key and starting signed notifications do not prove that a notification was delivered or that a receiver verified its signature. The separate [[source-adyen-docs-development-resources-webhooks-secure-webhooks-verify-hmac-signatures|HMAC verification guide]] documents endpoint-specific and Test-versus-Live key scope plus replacement-key propagation, but those operational details are separate from this API reference.
- The page documents 400, 401, 403, 422 and 500 error responses. It does not specify retry, reversal or key-rotation timing for this endpoint. No payment, settlement, account eligibility or compliance outcome follows from key generation.

## Detail locators

- Purpose, signed-notification statement, role and captured Test server: opening text and `## Servers`, lines 5-14.
- Required merchant and webhook path identities; no other input section appears: `## Parameters`, lines 16-22.
- Success response alternatives and required `hmacKey` only for the 200 body: `### 200 Success` and `### 204 Success`, lines 24-36.
- Error meanings and shared problem-body schema: `### 400 Client Error` (lines 39-56), `### 401 Client Error` (59-76), `### 403 Client Error` (79-96), `### 422 Client Error` (99-116), and `### 500 Server Error` (119-136).
- Illustrative returned-key value: `## Response examples`, lines 138-147.

## Related

- Company: [[adyen]]
- Concept: [[adyen-webhooks]]
- Separate HMAC verification and replacement-key guidance: [[source-adyen-docs-development-resources-webhooks-secure-webhooks-verify-hmac-signatures]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/webhooks/(webhookId)/generateHmac/2026-11-05|Adyen Management API — Generate merchant webhook HMAC key (2026-11-05)]]
