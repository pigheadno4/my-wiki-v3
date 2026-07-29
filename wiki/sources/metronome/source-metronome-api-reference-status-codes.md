---
title: "Metronome API status codes"
type: source
date_ingested: 2026-07-30
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/status-codes"
raw_files:
  - "metronome/api-reference/status-codes-2026-07-13.md"
tags: [metronome, api, http-status-codes, rate-limiting]
---

## Overview

This API reference defines Metronome's HTTP status-code conventions for API success and failure. It classifies success, client errors, and Metronome server errors, gives common response codes and remediation guidance, and identifies a rate-limit header for distinguishing client-wide and per-customer limits.

## Key takeaways

- Metronome uses `2xx` for successful requests, `4xx` for client errors, and `5xx` for Metronome server errors.
- Every `4XX` error uses an `application/json` object containing a descriptive `message`.
- The documented common client responses cover malformed requests (`400`), invalid or unauthorized tokens (`401`), forbidden resource access (`403`), missing resources (`404`), and conflicts (`409`).
- A `429` response directs clients to inspect `X-Metronome-Rate-Limit-Type`, determine whether the exceeded limit is `client` or `customer`, then back off and retry later.
- For server errors, the source recommends retrying. When an `Idempotency-Key` was used, it first directs the client to verify that the resource was not partially created, then retry with a different key.

## Details

The reference's status-code table describes `200` as a successful request. For `400`, it recommends correcting malformed request syntax or parameters. For `401` and `403`, it directs the caller to validate the API token; for `404`, it directs the caller to validate the requested resource ID. A `409` can arise when a request conflicts with the current state of an existing resource, including a duplicate object or a non-unique idempotency key.

For a rate-limited `429`, the response header value `client` means the organization's overall limit for that endpoint was exceeded; `customer` means the targeted customer's per-customer limit was exceeded. The source does not state either limit's numeric value.

## Scope and unknowns

This source documents broad HTTP response categories, common status codes, a single-field `4XX` error envelope, and the two rate-limit scopes. It does not specify a response-body schema for successful or `5XX` responses, a machine-readable error-code taxonomy, numeric rate limits, reset or retry-after headers, the backoff schedule, or exact idempotency-conflict and partial-creation recovery semantics.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/status-codes-2026-07-13|2026-07-13 snapshot — Metronome API status codes]]
