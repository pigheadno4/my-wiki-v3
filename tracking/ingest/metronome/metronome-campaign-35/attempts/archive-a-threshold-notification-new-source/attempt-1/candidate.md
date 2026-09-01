---
title: "Metronome Archive a Threshold Notification API"
type: source
date_ingested: 2026-09-01
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/alerts/archive-a-threshold-notification"
raw_files:
  - "metronome/api-reference/alerts/archive-a-threshold-notification-2026-07-13.md"
tags: [metronome, api, alerts, threshold-notifications, monitoring, archival, idempotency]
---

## Overview

This OpenAPI page documents bearer-authenticated `POST /v1/alerts/archive`, which permanently disables one threshold-notification configuration identified by UUID and removes it from active evaluation across all customers. The operation can also release that configuration's resource `uniqueness_key`, but notification archival, uniqueness-key reuse, API-request replay, and webhook or history behavior are separate surfaces.

## Query-critical facts

- In a supplied JSON payload, UUID `id` is required and identifies the threshold notification to archive. The enclosing OpenAPI `requestBody` is not marked `required: true`, so omitted-body behavior is not established; the object schema also does not declare `additionalProperties: false`, so unknown-field behavior is undocumented.
- Archival is irreversible for evaluation: the configuration cannot be re-enabled, and Metronome directs callers to create a new threshold notification to resume monitoring. The page says evaluation stops immediately across all customers, but it does not define an acknowledgement-versus-completion boundary, treatment of an evaluation already in progress, or read and export propagation timing.
- Optional boolean `release_uniqueness_key` resets the archived notification's resource key for reuse when set to `true`. The page does not specify omitted or explicit-false semantics, release visibility, atomic ordering between archival and release, concurrent reuse, rollback, or interaction with an in-flight creation attempt. This resource-key lifecycle is distinct from the API-wide `Idempotency-Key` request-result cache.
- The page asserts that archival preserves threshold-notification history and configuration for compliance and auditing. It does not identify the retained records, access surface, retention period, completeness, immutability, export behavior, or any compliance standard. Current Get authority separately says an archived notification can still return its configuration with nullable `customer_status`, while current List authority requires explicitly including archived configurations; neither authority turns the archive response into history or proves webhook-event retention.
- HTTP `200` requires top-level `data`, whose generic `Id` object requires UUID `id`; the narrative labels it the archived threshold notification's ID, and the example repeats the request UUID. The response exposes no archived representation, per-customer states, released key, affected-evaluation count, history locator, completion timestamp, or propagation status. Generic HTTP `404` means the specified resource was not found.

## Material boundaries

The dedicated archive page's immediate stop and preservation statements are authority for this threshold-configuration mutation only. They do not establish cancellation of notifications already emitted, queued, or in flight; webhook delivery or retry suppression; retraction of merchant actions; preservation of webhook or event-log history; read-after-archive freshness; or propagation to exports, dashboards, and reports. The separate shared Plan-and-Contract overview identifies `/alerts/archive` only as an unversioned route that archives a configuration so it no longer triggers; it does not replace this page's POST method, versioned path, payload, authentication, response, or all-customer scope, and neither source defines entity-specific parameter differences here.

The endpoint declares only HTTP `200` and generic `404`. It does not map a missing body, missing or malformed UUID, unknown versus inaccessible notification, already archived state, conflict, authorization failure, throttling, timeout, or server failure to specific outcomes; nor does it define atomicity, partial success, rollback, concurrent archive/create behavior, recovery after an ambiguous result, or whether a failed archive releases a uniqueness key.

Because this mutation uses POST, the separate API-wide [[metronome-api-idempotency|`Idempotency-Key` authority]] applies only after execution admission: Metronome persists a result once the request begins executing, meaning validation passed and no pre-execution concurrent-request conflict prevented execution. For an admitted request, identical same-key parameters replay the original persisted result, changed parameters return HTTP `409`, retention is at least 24 hours, and a persisted result can be HTTP `500`. Validation failures and pre-execution concurrency conflicts are not established as cached results. This endpoint adds no archive-specific behavior for no key, a different or expired key, repeated archival, release visibility, cached or ambiguous failure state, or recovery. Same-key replay is not fresh proof of current evaluation cessation, configuration visibility, webhook state, historical retention, or uniqueness-key availability. [[source-metronome-api-reference-idempotency]]

## Raw-detail coverage map

- **Operation and admission:** production server, global bearer authentication, POST `/v1/alerts/archive`, operation ID, request media type, request example, unmarked request-body wrapper, and required UUID `id` inside a supplied payload are in raw. API-wide execution-admission and replay semantics remain in the dedicated idempotency source.
- **Archive lifecycle and monitoring:** permanent disablement, removal from active monitoring across all customers, immediate evaluation stop, inability to re-enable, and create-new-to-resume guidance are in raw; in-progress work, acknowledgement versus completion, per-customer state transitions, read freshness, and cross-surface propagation are undocumented.
- **Uniqueness-key lifecycle:** optional `release_uniqueness_key`, its documented true-to-reset behavior, and intended future reuse are in raw; omitted or false behavior, release timing and visibility, concurrency, failed-archive treatment, and interaction with API request replay are not defined.
- **Response and failures:** required `data`, nested required UUID `data.id`, repeated-ID example, generic `404` error with required string `message`, and absence of an archived representation, key-release result, affected-customer count, history locator, or propagation marker are in raw.
- **History, delivery, and schema limits:** the page's historical-configuration preservation assertion and compliance/auditing rationale are in raw, but retention duration, record completeness, access path, webhook-event preservation, already-generated delivery handling, export behavior, and compliance guarantees are not. Request and response objects do not declare closed-schema behavior.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-alerts-and-notifications]], [[metronome-api-idempotency]], [[metronome-webhooks]]
- Related sources: [[source-metronome-api-reference-alerts-create-a-threshold-notification]], [[source-metronome-api-reference-alerts-get-a-threshold-notification]], [[source-metronome-api-reference-alerts-get-all-threshold-notifications]], [[source-metronome-plans-shared-endpoints-notifications]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/alerts/archive-a-threshold-notification-2026-07-13|2026-07-13 snapshot - complete threshold-notification archive lifecycle, uniqueness-key release, request and response schemas, errors, and OpenAPI metadata]]
