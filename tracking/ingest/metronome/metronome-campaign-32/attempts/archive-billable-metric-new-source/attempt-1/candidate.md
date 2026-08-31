---
title: "Metronome API Reference: Archive a Billable Metric"
type: source
date_ingested: 2026-08-31
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/billable-metrics/archive-a-billable-metric"
raw_files:
  - "metronome/api-reference/billable-metrics/archive-a-billable-metric-2026-07-13.md"
tags: [metronome, api, billable-metrics, products, archival, idempotency]
---

## Overview

Bearer-authenticated `POST /v1/billable-metrics/archive` retires one billable metric selected by UUID. Archival prevents that metric from being chosen for new Products, while the page says Products already associated with it continue to meter from its archived definition. The operation returns the metric ID, and the separate API-wide `Idempotency-Key` authority governs request-result replay rather than metric identity or archive state.

## Query-critical facts

- Within a supplied JSON object, `id` is required and UUID-formatted. The enclosing OpenAPI `requestBody` is not marked `required: true`, and the referenced `Id` object does not declare `additionalProperties: false`; omitted-body, missing-ID, null, malformed-UUID, and unknown-field runtime behavior are not established by this page.
- Archival blocks the metric from use in **new** Products. It is not documented as requiring the metric to be unused or orphaned: if a Product already references it, the page says that Product continues to function as usual and meters from the archived metric definition. The page does not define a dependency check, an association-count precondition, or effects on in-flight Product creation or Product updates that select the metric concurrently.
- The page says archived metrics remain returned by the single-metric and list endpoints with populated `archived_at`. The dedicated List authority qualifies that broad statement: archived metrics are excluded by default and require `include_archived=true`. Neither page establishes retention duration, audit-history completeness, archive propagation timing, cursor consistency during archival, or historical Product and invoice visibility.
- HTTP `200` requires `data`, which references the same `Id` schema and therefore carries required UUID `data.id`. That ID identifies the targeted metric; it is not an archive-operation resource, uniqueness key, or idempotency token. The response exposes no archive timestamp, Product impact list, version, propagation status, or reconciliation result.
- The only documented endpoint failure is HTTP `404`, using an error object with required string `message` and the description "The specified resource was not found." The page does not distinguish a nonexistent metric from an already archived, unauthorized, or otherwise invisible metric, and it does not document validation, conflict, authentication, authorization, rate-limit, server-error, or partial-effect responses.
- API-wide `Idempotency-Key` behavior applies to this POST: once execution begins, identical parameters with the same key replay the persisted original result, changed parameters conflict with HTTP `409`, retention is at least 24 hours, and a cached result can be HTTP `500`. The archive endpoint adds no repeated-call or already-archived semantics; no-key, different-key, expired-key, concurrent archive or Product-association ordering; fresh-state verification; rollback; or ambiguous-failure recovery contract.

## Material boundaries and contradiction

> [!warning] Cross-source metering conflict
> This archive page says an existing Product "will continue to function as usual, metering based on the definition of the archived billable metric." The dedicated Get-a-metric source says an archived metric stops processing new usage events. Those claims are materially in tension for an existing usage Product, and the sources do not reconcile event acceptance, matching, aggregation, rating, invoice calculation, or cutoff timing. Preserve both source-scoped claims and verify current runtime behavior before archiving a metric used by a Product.

The page does not say archival is reversible or irreversible. It exposes no restore endpoint, unarchive flag, or replacement workflow, but absence of those controls is not proof that restoration is impossible. It also does not define whether already accepted or late events finish processing, whether draft or finalized invoices recalculate, whether historical usage remains queryable, or whether reports, exports, alerts, webhooks, caches, and downstream integrations converge atomically. A `200` or same-key replay therefore proves only the documented result, not complete lifecycle propagation.

## Raw-detail coverage map

Use the exact raw page for the production server and bearer-security declaration; method, path, and `archiveBillableMetric-v1` operation ID; the complete existing-versus-new Product narrative; the Get/List `archived_at` statement; request example; absent request-body required marker; required UUID `Id` property; required `data.id` success envelope and example; generic `404` reference and required-message error shape; and the absence of endpoint-specific restoration, concurrency, propagation, and retry detail. Use the dedicated Get and List sources for their own retrieval and archive-filter contracts, the product sources for Product state and metric-reference surfaces, and the idempotency source for API-wide POST replay and cached-error behavior.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-billable-metrics]], [[metronome-products-and-rate-cards]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-billable-metrics-get-a-billable-metric]], [[source-metronome-api-reference-billable-metrics-list-all-billable-metrics]], [[source-metronome-api-reference-products-get-a-product]], [[source-metronome-api-reference-products-list-products]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/billable-metrics/archive-a-billable-metric-2026-07-13|2026-07-13 snapshot - billable-metric archive lifecycle, Product effects, request and response identity, and 404 boundary]]
