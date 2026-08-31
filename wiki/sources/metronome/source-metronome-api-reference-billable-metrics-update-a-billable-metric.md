---
title: "Metronome API Reference: Update a Billable Metric"
type: source
date_ingested: 2026-08-31
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/billable-metrics/update-a-billable-metric"
raw_files:
  - "metronome/api-reference/billable-metrics/update-a-billable-metric-2026-07-13.md"
tags: [metronome, api, billable-metrics, metric-lifecycle, products]
---

## Overview

Bearer-authenticated `PUT /v1/billable-metrics/{billable_metric_id}` changes only an existing billable metric's display name. Its OpenAPI success envelope places a required UUID `id` under required top-level `data`; calculation configuration must instead be replaced through a new metric and an effective-dated Product reference change. The page does not establish repeated-PUT safety, propagation timing, configuration-history treatment, or historical reporting behavior.

## Query-critical facts

- The required path parameter `billable_metric_id` is a UUID and identifies the existing metric. Inside a supplied JSON object, `name` is the only property and is required; it is the new metric name. The enclosing OpenAPI `requestBody` is not marked `required: true`, and the object does not declare `additionalProperties: false`, so omitted-body and unknown-field runtime behavior are not documented.
- The endpoint changes only the display name. Filters, aggregation, grouping, SQL, and other calculation configuration are not mutable through this operation; the page says configurations cannot be changed after creation. It does not document name length, emptiness, uniqueness, normalization, authorization beyond bearer authentication, or an endpoint error catalog.
- For a streaming-metric configuration change, the documented example workflow is to duplicate the metric, make and save the changes, navigate to the Product associated with the incorrect metric, and schedule that Product to reference the new metric on the appropriate date. This is a replacement workflow, not an in-place configuration edit.
- HTTP `200` requires top-level `data`; `data` references a generic `Id` object that requires UUID `id`. The prose calls this the billable metric ID returned to confirm the update, but the response example's UUID differs from the path-parameter example and the generic schema does not encode equality. Treat `data.id` as the documented response identity placement without asserting from this page alone that it equals the requested metric UUID or represents a separate operation resource.
- The separate [[source-metronome-api-reference-idempotency|Metronome API-wide idempotency authority]] documents `Idempotency-Key` only for all **POST** endpoints. This operation is `PUT`, exposes no resource `uniqueness_key`, and provides no endpoint-specific retry, repeated-call, concurrent-rename, lost-update, timeout, cached-error, or ambiguous-failure recovery contract. A desired final name must not be treated as proof of request-result replay or concurrency safety.

## Replacement, propagation, and history boundaries

The five-step replacement workflow is introduced as an example for a streaming billable metric and names one associated Product. It does not establish that every associated Product is discovered or migrated, that the original metric is archived, that Product scheduling and metric creation are atomic, or that failed and concurrent changes roll back. It also does not define effective-date inclusivity, timezone, accepted or late-event matching, cross-transition aggregation, read-after-write visibility, or when the new reference reaches rating, invoice, report, export, alert, or downstream-integration surfaces. Dedicated Product and metric authorities remain necessary for those mechanics.

For a name-only update, the page returns no updated name, configuration snapshot, version, audit record, timestamp, or propagation status. It does not say when Get or List results, Product views, invoices, reports, or exports show the new display name; whether earlier records retain the old name; or whether any historical calculation or financial result is recomputed. The sparse identifier response confirms neither propagation nor historical convergence.

> [!warning] Response-identity evidence boundary
> The narrative says the response returns the billable metric ID, while the generic `Id` schema only requires `data.id` and the response and path examples use different UUIDs. Preserve the immediate-parent placement and narrative meaning, but do not infer equality, operation-resource identity, or fresh metric state from the examples.

## Raw-detail coverage map

Use the exact raw page for the production server and bearer-security declaration; exact route and operation ID; required path UUID; request-body nesting, required `name` property, and example; complete HTTP `200` envelope and generic `Id` schema; response example; duplicated endpoint description; and the numbered streaming-metric replacement workflow. The raw page contains no non-200 response map, endpoint-specific idempotency or retry rule, concurrency/version field, propagation status, audit history, or historical-reporting contract.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-billable-metrics]], [[metronome-products-and-rate-cards]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-billable-metrics-create-a-billable-metric]], [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]], [[source-metronome-guides-implement-metronome-core-concepts-billable-metrics-sql-editor]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/billable-metrics/update-a-billable-metric-2026-07-13|2026-07-13 snapshot — name-only metric update, immutable-configuration replacement workflow, request and response identity placement, and lifecycle unknowns]]