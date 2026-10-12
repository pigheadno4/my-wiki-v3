---
title: "Adyen API Idempotency"
type: concept
category: technology
tags: [adyen, api, idempotency, retries, error-handling]
---

## Adyen API idempotency

Adyen documents an `idempotency-key` request header for POST calls. Reusing the same key after an uncertain response can return the first attempt's response without duplicating the operation when Adyen already processed it. The key identifies one message, has a maximum length of 64 characters, and is recommended to be a UUID; the response header can be used to verify idempotent processing. This is a request-replay boundary, not proof of payment authorization, capture, settlement, or current account eligibility. [[source-adyen-docs-development-resources-api-idempotency]]

## Scope and lifetime

Keys are stored and checked for uniqueness at company-account level and are valid for 7 to 14 days after first submission. Duplicate-key checking does not cross regional endpoints when they are targeted simultaneously, so a key alone is not a global cross-region duplicate guard. Adyen recommends a unique random UUID v4 per request to keep API credentials under one account from accessing one another's responses. Reducing a credential's access does not prevent retrieval of earlier responses while previously used keys remain available. [[source-adyen-docs-development-resources-api-idempotency]]

## Retry and concurrency boundary

When no response arrives, for example after a timeout, the request can be retried with the same idempotency key. When an API response is received, retry later with the same key only if its `transient-error` header is `true`; do not retry that response if the header is absent or `false`. A race between two same-key payment requests can process one while returning a transient error for the other. A duplicate submitted before the first completes can return HTTP 422 or HTTP 409 with error code 704, `request already processed or in progress`. Retries should use exponential backoff. [[source-adyen-docs-development-resources-api-idempotency]]

If the stateful idempotency store is unavailable, the API documents HTTP 503 with error code 703 and marks the request transient. The page lists pausing and retrying later, or omitting the header to fall back to non-idempotent processing. Omitting the header removes this idempotency mechanism and must not be presented as a duplicate-safe retry. [[source-adyen-docs-development-resources-api-idempotency]]

## Related

- [[adyen]]
- [[source-adyen-docs-development-resources-api-idempotency]]
