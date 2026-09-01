---
title: "Metronome API Reference: List Contracts Associated with a Package"
type: source
date_ingested: 2026-09-01
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/contracts/list-contracts-associated-with-a-package"
raw_files:
  - "metronome/api-reference/contracts/list-contracts-associated-with-a-package-2026-07-13.md"
tags: [metronome, api, packages, contracts, customers, pagination]
---

## Overview

This reference documents bearer-authenticated `POST /v1/packages/listContractsOnPackage`, which discovers customer and contract identities associated with one package for cohort management and migration planning. It is an association-list authority, not a contract-detail read or authority for ending contracts, provisioning replacements, or proving migration completion.

## Query-critical facts

- The operation runs against `https://api.metronome.com` with bearer authentication. Within a supplied JSON object, UUID `package_id` is required; the enclosing `requestBody` is not marked required and the object does not declare `additionalProperties: false`, so omitted-body and unknown-field runtime behavior are undocumented.
- Optional RFC 3339 `starting_at` includes contracts that started on or after that timestamp, while optional RFC 3339 `covering_date` includes contracts active on that date; the two filters cannot be combined. Optional `include_archived` defaults to `false`. The page does not define an exclusive period-end filter, behavior when both time filters are omitted, exact active-at boundary treatment, or how archived inclusion intersects either time filter.
- HTTP `200` requires top-level `data`; nullable `next_page` is an optional sibling property. Every projection item requires UUID `customer_id`, UUID `contract_id`, and `starting_at`, and may carry `ending_before` and `archived_at`. The item does not expose package identity, alias or version, contract terms, rate card, current status, mutation state, invoice state, or migration outcome.
- Pagination uses optional query `limit` from 1 through 100 and query `next_page`. The separate pagination authority supplies repeat-until-null traversal when a cursor is returned, but this endpoint does not require `next_page` in the response and defines no default page size, result ordering, total count, cursor lifetime, snapshot consistency, duplicate-or-skip behavior during concurrent changes, as-of marker, freshness guarantee, or read-after-mutation visibility.
- The only endpoint-specific error documented is HTTP `400` with required `code` and `message`, where `code` is `PackageNotFound`. The page does not document authentication errors, invalid-filter errors, cursor errors, partial results, or recovery behavior.

## Material boundaries

- The prose describes associations over a specific time period, but the request exposes either a lower bound on contract start or one covering instant, not a closed interval. Do not infer interval-overlap semantics, historical completeness, or a stable point-in-time cohort beyond the selected filter.
- The migration example says to list active customers, end contracts, and provision customers on a new package. This endpoint establishes only the discovery step; dedicated contract and package authorities govern the separate mutations, and this page does not establish atomicity, ordering, idempotency of those mutations, rollback, propagation, or reconciliation.
- The separate API-wide `Idempotency-Key` authority applies to all POST endpoints. A provided-key result is persisted only after execution admission, meaning validation passed and no pre-execution concurrent-request conflict prevented execution; identical same-key parameters then replay the original result, while changed parameters return HTTP `409`. Advancing `next_page` or changing package, time, or archive filters changes parameters. Replay is not proof of a fresh association list or stable pagination snapshot, and this endpoint adds no local key, retry, cache, concurrency, or recovery contract.

## Raw-detail coverage map

Use the exact raw snapshot for the production server and bearer declaration; `POST /v1/packages/listContractsOnPackage` identity and operation ID; cohort-management and migration-planning narrative; package UUID and complete time and archive filter schema; request example; query cursor and 1-100 limit definitions; required response `data`, optional nullable sibling `next_page`, complete `ContractProjectionSummary` required and optional fields, and response example; `PackageNotFound` error shape; and the absent request-body-required marker, closed-object declaration, closed-interval filter, default page size, ordering, totals, snapshot, freshness, mutation, and reconciliation guarantees. Use the dedicated pagination source for cursor traversal, the idempotency source for API-wide POST replay, and dedicated package and contract authorities for package configuration, contract details, ending, replacement provisioning, and migration outcomes.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-packages-and-aliases]], [[metronome-customers-and-contracts]], [[metronome-reporting-and-analytics]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-pagination]], [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/contracts/list-contracts-associated-with-a-package-2026-07-13|2026-07-13 snapshot - package association scope, contract and customer identity, time filters, pagination, response placement, and authority boundaries]]