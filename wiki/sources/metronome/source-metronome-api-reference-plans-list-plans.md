---
title: "Metronome API Reference: List Plans"
type: source
date_ingested: 2026-08-21
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/plans/list-plans.md"
raw_files:
  - "metronome/api-reference/plans/list-plans-2026-07-13.md"
tags: [metronome, api-reference, plans, contracts, pagination]
---

## Overview

This API reference documents `GET /v1/plans`, which lists available plans on Metronome's deprecated Plans surface. Metronome directs new clients to implement with Contracts, but this page does not identify a replacement Contracts route, schema mapping, migration procedure, or removal date.

## Key takeaways

- The operation is `GET /v1/plans` on `https://api.metronome.com/v1` and uses bearer authentication.
- Both query parameters are optional: `limit` accepts an integer from 1 through 100, and `next_page` supplies the cursor at which the next result page should begin.
- A successful JSON response requires `data` and `next_page`; `data` is an array of plans and `next_page` is a nullable string.
- Each plan requires a UUID `id`, string `name`, and string `description`; optional `custom_fields` is a string-valued map associated with the plan entity.
- The page labels Plans deprecated and tells new clients to use Contracts, without defining how the legacy list response maps to Contracts.

## Request

The OpenAPI operation is `GET /plans` under the `/v1` production server, yielding `GET /v1/plans`. The document applies the global HTTP bearer security scheme. It defines no request body and only two optional query parameters: `limit`, whose inclusive schema bounds are 1 and 100, and `next_page`, a string cursor indicating where the next page should start. It does not document default or stable ordering, cursor lifetime, invalid-cursor behavior, or a total count.

## Response

HTTP 200 is the only response documented. Its JSON object requires `data` and `next_page`. `data` contains `Plan` objects; every object requires UUID-formatted `id`, `name`, and `description`, while `custom_fields` is optional and permits arbitrary string-valued properties. `next_page` is nullable, and the example uses `null`; the page does not explicitly state the termination rule beyond that schema and example.

## Deprecation and migration boundary

This is explicitly a deprecated Plans endpoint, and the documentation says new clients should implement using Contracts. The page does not name an equivalent Contract operation, state that a Contract response has the same fields, define Plan-to-Contract identity or custom-field migration, give a shutdown date, or say that the deprecated endpoint is unavailable. No non-200 error schemas, authorization scopes beyond bearer authentication, rate limits, retry guidance, or compatibility guarantees are supplied.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]]

## Raw Sources

- [[raw/metronome/api-reference/plans/list-plans-2026-07-13|2026-07-13 snapshot - deprecated List plans API reference]]
