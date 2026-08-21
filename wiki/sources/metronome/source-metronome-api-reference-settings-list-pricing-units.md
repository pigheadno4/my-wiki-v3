---
title: "Metronome List Pricing Units API"
type: source
date_ingested: 2026-08-21
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/settings/list-pricing-units.md"
raw_files:
  - "metronome/api-reference/settings/list-pricing-units-2026-07-13.md"
tags: [metronome, api, pricing-units, currencies, pagination]
---

## Overview

This API reference documents the bearer-authenticated `GET /v1/credit-types/list` endpoint on `https://api.metronome.com`. It lists fiat currency pricing units and configured custom pricing units, including non-fiat units such as AI credits. The reference defines optional cursor pagination and the successful JSON response shape, but it does not document error responses or mutation behavior.

## Key takeaways

- The endpoint lists all fiat currency types and configured custom pricing units; the page gives AI credits as a non-fiat example.
- The request accepts optional `limit` and `next_page` query parameters. `limit` is an integer from 1 through 100, while `next_page` is the cursor at which the next result page starts.
- A `200` response is JSON with required top-level `data` and `next_page` fields. `data` is an array whose item schema exposes a string `name`, UUID `id`, and boolean `is_currency`; `next_page` is a nullable string. The item properties themselves are not marked required by this schema.
- The fixed pricing-unit identifier documented for `USD (cents)` is `2714e483-4ff1-48e4-9e25-ac732e8f24f2`. This page does not define scaling for other fiat currencies or precision and rounding for custom units.
- Authentication uses an HTTP bearer scheme. No `4xx` or `5xx` response, error body, rate limit, retry rule, ordering guarantee, or pagination default is documented on this page.

## Request and authorization

Call `GET /v1/credit-types/list` against the documented production server, `https://api.metronome.com`. The OpenAPI document applies `bearerAuth` globally and defines it as an HTTP bearer scheme. The operation shows no request body.

Both query parameters are optional. `limit` sets the maximum number of returned results and is constrained to the inclusive range 1–100. `next_page` is a string cursor indicating where the next page begins. The page does not document a default page size, cursor lifetime, cursor reuse, stable ordering between pages, or behavior for malformed or expired cursors.

## Success response

The only documented response is `200 Success` with `application/json`. Its object schema requires `data` and `next_page`. `data` is an array; each item may expose `name` as a string, `id` as a UUID-formatted string, and `is_currency` as a boolean. Because the item schema has no `required` list, this source does not guarantee that every returned item contains all three properties. `next_page` is a nullable string.

The example returns `USD (cents)` with `is_currency: true`, a custom `cloud consumption units` entry with `is_currency: false`, and `next_page: null`. The example illustrates these values but does not establish sorting, uniqueness, total result count, or that the two-item sample is exhaustive.

## Pricing-unit denomination and naming

The page states that all fiat currency types, including examples such as USD and GBP, appear alongside any configured custom pricing units. It also names AI credits as an example of charging for usage in a non-fiat pricing unit. The documented USD entry is specifically named `USD (cents)` and has ID `2714e483-4ff1-48e4-9e25-ac732e8f24f2`.

This source does not enumerate the complete fiat set, define the denomination of GBP or any other non-USD currency, specify whether identifiers are stable across environments, or define custom-unit precision, conversion, rounding, creation, update, or deletion. Its operation path and operation ID use `credit-types` terminology while the page calls the resources pricing units; the page does not explain whether those names are aliases or distinct API concepts.

## Failure and behavior boundaries

No error status, error response schema, authorization-failure body, retry guidance, idempotency behavior, or rate-limit behavior is included. Because the operation is a listing endpoint with no documented mutation, this page provides no creation, update, archive, or deletion semantics. It also does not define permissions beyond bearer authentication, environment-specific availability, caching, consistency after configuration changes, or propagation timing.

No contradiction was found with the existing Metronome currency concept. That concept's broader supported-currency and non-USD denomination statements come from a separate guide; this endpoint independently establishes only the listing taxonomy, the `USD (cents)` identifier, pagination, authentication, and response schema described here.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-currencies-and-custom-pricing-units]], [[metronome-products-and-rate-cards]]
- Related source: [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]]

## Raw Sources

- [[raw/metronome/api-reference/settings/list-pricing-units-2026-07-13|2026-07-13 snapshot — pricing-unit list request, response schema, pagination, and bearer authentication]]
