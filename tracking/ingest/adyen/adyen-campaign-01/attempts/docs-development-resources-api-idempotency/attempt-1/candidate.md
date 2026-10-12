---
title: "Adyen Docs: API idempotency"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/api-idempotency"
raw_files:
  - "adyen/docs/development-resources/api-idempotency/2026-09-15.md"
tags: [adyen, api, idempotency, retries, error-handling]
---

## Overview

This Adyen development-resources page documents request-level idempotency for POST calls: a merchant sends an `idempotency-key` header so an uncertain request can be retried with the same key and, when the first request was already processed, receive the first attempt's response without duplicating that operation. The page characterizes GET, DELETE, and PUT as idempotent by definition; its header-based mechanism is for POST requests.

The behavior is bounded by company-account and regional scope, a 7-to-14-day key-validity period, and specific transient-error signals. It does not establish global cross-region duplicate detection or make every retry condition safe.

## Key takeaways

- Submit `idempotency-key:<key>` in the request header. The key is a message identifier with a maximum length of 64 characters; Adyen recommends a UUID. If no response arrives, reuse the same header. The response's `idempotency-key` header can be checked to verify idempotent processing, and integrations must treat HTTP headers case-insensitively.
- Keys are stored and checked for uniqueness at company-account level and remain valid for 7 to 14 days after first submission. Simultaneous calls to different regional endpoints are not checked for duplicate keys across regions.
- Adyen recommends a unique version-4 random UUID per request so two API credentials under the same account cannot access each other's responses. Lowering a credential's access level does not prevent retrieval of earlier responses when previously used keys remain available.
- A transient error is described as having no side effects. Retry later with the same key only when the response header `transient-error` is `true`; when the header is absent or `false`, the page says not to retry. Sending duplicate same-key requests before the first completes can yield HTTP 422 or 409 with error code 704, while one request is processed.
- Use exponential backoff for retries. If the idempotency data store is unavailable, Adyen documents HTTP 503 with error code 703 and marks the request transient. The page also lists omitting the header as a possible fallback when many such responses occur, but that is explicitly non-idempotent processing and therefore removes this duplicate-suppression mechanism; it is not an unconditional safe-retry path.

## Detail locators

- POST scope and asynchronous-webhook context: lines 26-30.
- Header submission, 64-character key limit, same-key replay, response-header check, and case-insensitive header handling: lines 31-39.
- `/payments` examples for curl, Java, PHP, C#, Node.js, and Ruby: lines 41-248.
- Company-account scope, 7-to-14-day validity, and regional duplication boundary: lines 250-254.
- Credential-response security considerations: lines 256-260.
- Transient-error, concurrent duplicate, retry-signal, and HTTP 422/409 error-704 behavior: lines 262-268.
- Exponential backoff: lines 270-272.
- Idempotency-store unavailability, HTTP 503/error 703, and non-idempotent fallback warning: lines 274-281.

## Related

- [[adyen-api-idempotency]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/development-resources/api-idempotency/2026-09-15|Adyen API idempotency (2026-09-15 snapshot)]]
