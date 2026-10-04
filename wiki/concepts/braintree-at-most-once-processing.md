---
title: "Braintree At-Most-Once Processing"
type: concept
category: technology
tags: [braintree, at-most-once, idempotency, api-request-key, duplicate-requests]
---

## Braintree At-Most-Once Processing

Braintree's collected limited-audience guide defines At-Most-Once Processing as logical-intent idempotency for preventing duplicate API requests from causing duplicate actions. It requires a merchant-supplied `ApiRequestKey` for the intended logical action, treats identical keys within 30 days as duplicates, and states that this feature is mutually exclusive with transaction duplicate checking. This is distinct from network-level response replay. [[source-braintree-articles-guides-at-most-once]]

## Duplicate and retry route

For matching request details, an in-progress operation can return a retryable validation error and a completed operation can return its current result state; changed request details produce a validation error. The returned state may be unsuccessful or may have advanced since the original request. Generating a new key is not uniformly safe: use the source's action-specific tables and record/state checks, because some cases require investigation and potentially Braintree intervention.

The captured page is not generally public and directs readers to the product team before sharing. It establishes neither current merchant eligibility nor enablement, SDK support or successful execution.

## Sources

- [[source-braintree-articles-aib-af-idempotency-lr]] - 2026-09-16 Braintree-hosted AIB AF/LR snapshot of logical-intent request identity, duplicate handling, and action-specific retry qualifications; the route does not establish independent current bank policy or merchant enablement

- [[source-braintree-articles-guides-at-most-once]] - 2026-09-16 limited-audience guide to logical-intent request identity, 30-day duplicate handling, action-specific outcomes and retry qualifications
