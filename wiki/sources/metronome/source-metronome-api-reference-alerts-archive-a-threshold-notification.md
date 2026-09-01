---
title: "Metronome Archive a Threshold Notification API"
type: source
date_ingested: 2026-09-01
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/alerts/archive-a-threshold-notification"
raw_files:
  - "metronome/api-reference/alerts/archive-a-threshold-notification-2026-07-13.md"
tags: [metronome, api, alerts, threshold-notifications, monitoring, archival, idempotency, data-export]
---

## Overview

This OpenAPI page documents bearer-authenticated `POST /v1/alerts/archive`, which permanently disables one threshold-notification configuration identified by UUID and removes it from active evaluation across all customers. It may also release that configuration's resource `uniqueness_key`; archive state, resource-key reuse, API-request replay, webhook delivery, and exported history remain distinct surfaces.

## Query-critical facts

- In a supplied JSON payload, UUID `id` is required and identifies the threshold notification to archive. The enclosing OpenAPI `requestBody` is not marked `required: true`, so omitted-body behavior is not established; the object schema also does not declare `additionalProperties: false`, so unknown-field behavior is undocumented.
- Archival is irreversible for evaluation: the configuration cannot be re-enabled, and Metronome directs callers to create a new threshold notification to resume monitoring. The page says evaluation stops immediately across all customers, but it does not define an acknowledgement-versus-completion boundary, treatment of an evaluation already in progress, or read and export propagation timing.
- Optional boolean `release_uniqueness_key` resets the archived notification's resource key for reuse when set to `true`. Current create authority describes that key as 1-128 characters and organization-unique, says every threshold notification must have one although the payload required array omits it, and says reuse blocks creation with HTTP `409`; the API-wide lifetime table says the resource key lasts until released. The archive and creation authorities do not define omitted or explicit-false behavior, normalization, release timing or visibility, atomic ordering, failed-attempt key consumption, concurrent reuse or replacement, or interaction with request-result replay.
- The page asserts that archival preserves threshold-notification history and configuration for compliance and auditing. Current Data Export authority separately exposes `alert.archived_at` and `alert.disabled_at`, plus alert-linked `customer_alert_history` status-change rows whose `created_at` records when evaluation changed status. The cookbook nevertheless labels an alert query active while filtering `webhooks_enabled` and `disabled_at` but not `archived_at`; no current authority says archive also sets `disabled_at`. These export surfaces do not establish immediate propagation, history completeness or immutability, retention duration, webhook-delivery history, or a compliance guarantee.
- HTTP `200` requires top-level `data`, whose generic `Id` object requires UUID `id`; the narrative labels it the archived threshold notification's ID, and the example repeats the request UUID. The response exposes no archived representation, per-customer states, released key, affected-evaluation count, history locator, completion timestamp, or propagation status. Generic HTTP `404` means the specified resource was not found.

## Material boundaries

The dedicated archive page's immediate stop and preservation statements govern this threshold-configuration mutation only. They do not establish cancellation of notifications already emitted, queued, retrying, or in flight; webhook delivery suppression; retraction of merchant actions; preservation of webhook-event history; or immediate propagation to reads, exports, dashboards, and reports. Current Get authority separately returns archived configuration with nullable `customer_status`, while List requires explicit inclusion of archived configurations. Data Export provides archive and status-change evidence routes, but neither those routes nor the archive response prove complete or immutable history.

The endpoint declares only HTTP `200` and generic `404`. It does not map a missing body, missing or malformed UUID, unknown versus inaccessible notification, already archived state, conflict, authorization failure, throttling, timeout, or server failure to specific outcomes; nor does it define atomicity, partial success, rollback, concurrent archive/create behavior, or whether a failed archive releases a resource key.

Because this mutation uses POST, the separate API-wide [[metronome-api-idempotency|`Idempotency-Key` authority]] applies only after execution admission: Metronome persists a result once the request begins executing, meaning validation passed and no pre-execution concurrent-request conflict prevented execution. For an admitted request, identical same-key parameters replay the persisted original result, changed parameters return HTTP `409`, retention is at least 24 hours, and a persisted result can be HTTP `500`; the same key then replays that cached error. The idempotency authority directs callers to investigate resulting system state and decide whether to resolve manually or retry rather than assume that another key is safe. The separate status-code authority instead recommends verifying partial creation after `5XX` and then retrying with a different key. Neither authority defines one universally safe archive-and-release recovery sequence. Validation failures and pre-execution concurrency conflicts are not established cached results, while archive state, key-release visibility, another or expired key, concurrency, propagation, and final recovery remain endpoint-specific unknowns. [[source-metronome-api-reference-idempotency]] [[source-metronome-api-reference-status-codes]]

## Raw-detail coverage map

- **Operation and admission:** production server, global bearer authentication, POST `/v1/alerts/archive`, operation ID, request media type, example, unmarked request-body wrapper, and required UUID `id` inside a supplied payload are in raw. API-wide execution admission, persisted-result replay, cached HTTP `500`, and recovery guidance remain in the dedicated idempotency and status-code sources.
- **Archive lifecycle and monitoring:** permanent disablement, removal from active monitoring across all customers, immediate evaluation stop, inability to re-enable, and create-new-to-resume guidance are in raw; in-progress work, acknowledgement versus completion, per-customer transitions, read freshness, and cross-surface propagation are undocumented.
- **Resource uniqueness lifecycle:** the assigned raw documents `release_uniqueness_key: true` as resetting the archived notification's key for future reuse. Current create and idempotency authorities define its 1-128-character organization scope, duplicate-creation HTTP `409`, creation requiredness conflict, and until-release lifetime; omitted or false behavior, normalization, release ordering and visibility, failed-attempt consumption, concurrency, replacement, and interaction with API-request replay remain undefined.
- **Response and failures:** required `data`, nested required UUID `data.id`, repeated-ID example, generic `404` error with required string `message`, and absence of an archived representation, release result, affected-customer count, history locator, or propagation marker are in raw. API-wide cached-error replay and conflicting recovery guidance do not resolve endpoint state after an ambiguous failure.
- **History, exports, delivery, and schema limits:** the raw asserts preservation of threshold-notification history and configuration. Data Export routes archive visibility through distinct `alert.archived_at` and `disabled_at` fields and alert-linked status changes through `customer_alert_history`, while the cookbook's active query omits `archived_at`; access timing, completeness, immutability, retention, webhook history, and the relationship between archive and disable timestamps are not defined. Request and response objects do not declare closed-schema behavior.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-alerts-and-notifications]], [[metronome-api-idempotency]], [[metronome-webhooks]], [[metronome-reporting-and-analytics]]
- Related sources: [[source-metronome-api-reference-alerts-create-a-threshold-notification]], [[source-metronome-api-reference-alerts-get-a-threshold-notification]], [[source-metronome-api-reference-alerts-get-all-threshold-notifications]], [[source-metronome-guides-reporting-insights-data-export-database-reference]], [[source-metronome-guides-reporting-insights-data-export-cookbook]], [[source-metronome-plans-shared-endpoints-notifications]], [[source-metronome-api-reference-idempotency]], [[source-metronome-api-reference-status-codes]]

## Raw Sources

- [[raw/metronome/api-reference/alerts/archive-a-threshold-notification-2026-07-13|2026-07-13 snapshot - complete threshold-notification archive lifecycle, uniqueness-key release, request and response schemas, errors, and OpenAPI metadata]]
