---
title: "Metronome API Pagination"
type: source
date_ingested: 2026-07-29
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/pagination"
raw_files:
  - "metronome/api-reference/pagination-2026-07-13.md"
tags: [metronome, api, pagination]
---

## Overview

This reference documents Metronome's cursor-based pagination convention for list methods that return multiple results. It applies the same `limit` and `next_page` URL parameters across list endpoints; `/customers` is the example endpoint in the source.

## Key takeaways

- `limit` controls the number of results returned per page, while `next_page` carries the cursor for the following page.
- A response containing a `next_page` value indicates that additional records remain; clients include that value in the subsequent query.
- Pagination finishes when `next_page` is `null`.
- The source recommends `limit=1` for inspecting a response, `limit=50` when loading many results with fewer calls, and caps `limit` at `100`.

## Details

A client begins with a list request, optionally setting `limit`. When the response includes `next_page`, the client sends another request with that cursor as the `next_page` query parameter. The source's `/v1/customers` example shows `limit=10` on the initial request and then adds the returned cursor to retrieve the next page.

## Scope and unknowns

This source defines the request parameters, continuation signal, completion condition, and stated limit guidance. It does not specify a default limit, result ordering, cursor lifetime, retry behavior, or endpoint-specific variations.

The separate SDK guide says Metronome SDKs support pagination and configurable automatic retries, but this page does not describe how an SDK exposes cursors or whether retries affect page traversal.

## Related

- Company: [[metronome]]
- Related sources: [[source-metronome-guides-get-started-developer-sdks]]
- Concept audit: no standalone concept page was warranted for this thin API-wide convention.

## Raw Sources

- [[raw/metronome/api-reference/pagination-2026-07-13|2026-07-13 snapshot — Metronome API pagination]]
