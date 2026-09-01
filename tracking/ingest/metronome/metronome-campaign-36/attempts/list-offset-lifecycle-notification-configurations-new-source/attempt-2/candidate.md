---
title: "Metronome API Reference: List Offset Lifecycle Event Notification Configurations"
type: source
date_ingested: 2026-09-01
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/notifications/list-offset-lifecycle-event-notification-configurations"
raw_files:
  - "metronome/api-reference/notifications/list-offset-lifecycle-event-notification-configurations-2026-07-13.md"
tags: [metronome, api, notifications, lifecycle-events, webhooks, pagination, idempotency]
---

## Overview

This reference documents bearer-authenticated `POST /v2/notifications/offset/list`, which inventories user-created offset-notification configurations scheduled relative to lifecycle events. It is configuration-discovery authority with a documented 400-result maximum per request, not authority for creating, editing, archiving, firing, delivering, or reconciling notifications.

## Query-critical facts

- The operation uses the production API server and bearer authentication. Its enclosing `requestBody` is explicitly optional; a supplied object has no required properties and does not declare `additionalProperties: false`, so omitted-body behavior is allowed by the contract while unknown-field runtime behavior remains undocumented.
- Optional body `limit` is numeric but has no documented integer constraint, lower bound, default, or direct schema maximum; the operation description separately says a request returns at most 400 results. Optional body `cursor` supplies pagination state, and `archive_filter` accepts `ARCHIVED`, `NOT_ARCHIVED`, or `ALL`, defaulting to `NOT_ARCHIVED`.
- HTTP `200` requires top-level `data`; optional nullable sibling `cursor` is the endpoint's only documented response pagination field. This endpoint documents optional JSON-body `limit` and `cursor` plus a separate maximum of 400 results per request, while the current generic pagination authority says all list endpoints expose URL query `limit` and `next_page`, caps `limit` at 100, and repeats until `next_page` is null. The authorities do not establish whether this endpoint accepts, rejects, or ignores those generic query parameters; whether the generic 100 cap does or does not govern the body `limit`; whether callers may request 400; or whether the generic `next_page` completion rule applies to response `cursor`. Accepted body-limit range and default, cursor terminal semantics, precedence between pagination surfaces, ordering, totals, cursor lifetime, cursor binding to the archive filter, stable-snapshot and duplicate-or-skip behavior, as-of time, freshness, and read-after-mutation visibility remain unresolved.
- Each configuration requires UUID `id`, `name`, `type`, `policy`, `environment_type`, creation time and actor, and nullable `archived_at`. Its policy requires lifecycle-event `type` plus an ISO-8601 duration `offset`; positive values mean after the base event and negative values mean before it. The page does not enumerate lifecycle-event types or constrain configuration `type` or `environment_type`, and the response does not expose a calculated fire time, generation state, enablement, delivery state, webhook identity, retry state, or event history.
- The separate API-wide `Idempotency-Key` authority applies to all POST endpoints. After execution admission, identical same-key parameters replay the persisted original result, while changing `limit`, `cursor`, or `archive_filter` changes parameters and returns HTTP `409` under that authority. Replay is not proof of a fresh configuration inventory or stable pagination snapshot, and this endpoint adds no local error, retry, concurrency, cache, propagation, or recovery contract.

## Material boundaries

- Listing a configuration does not prove that its lifecycle-event type is currently available or enabled, that a future source event will occur, that a notification will be generated at the requested offset, or that any webhook will be emitted or delivered. Dedicated system-event, offset-notification, and webhook authorities govern those separate surfaces.
- `archived_at` and the archive filter expose configuration lifecycle state, but this page does not define archival transition timing, already-generated or in-flight work, restoration, or historical completeness. Absence from the default non-archived view is not proof of deletion or of delivery suppression.

## Raw-detail coverage map

Use the exact raw snapshot for the production server and bearer declaration; `POST /v2/notifications/offset/list` identity and operation ID; user-created lifecycle-relative scope and separate 400-result request maximum; optional request body; full numeric body `limit`, body `cursor`, and three-value archive-filter schema and example; required top-level `data`, optional nullable sibling response `cursor`, and response example; every required configuration identity, environment, creation, and archive field; the required policy fields and positive and negative ISO-8601 offset examples; and the absent closed-object declaration and operation-level error catalog. Preserve the pagination-authority conflict: this endpoint documents optional JSON-body `limit` and `cursor` and nullable response `cursor`, whereas the generic authority says all list endpoints expose URL query `limit` and `next_page`, caps `limit` at 100, and repeats until `next_page` is null. Neither authority resolves whether this endpoint accepts, rejects, or ignores the generic query fields, applicability of the 100 cap to body `limit`, whether 400 is requestable, completion semantics for response `cursor`, precedence, accepted body-limit range or default, ordering, totals, lifetime, filter binding, stable snapshot, duplicate-or-skip behavior, freshness, or read-after-mutation visibility. Use the idempotency source for API-wide POST replay and dedicated notification and webhook authorities for event catalogs, configuration mutations, scheduling behavior, payloads, delivery, retry, deduplication, and verification.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-alerts-and-notifications]], [[metronome-customers-and-contracts]], [[metronome-webhooks]], [[metronome-reporting-and-analytics]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-notifications-list-system-notification-event-types]], [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]], [[source-metronome-guides-customers-billing-set-up-notifications-offset-notifications]], [[source-metronome-guides-platform-configuration-setup-webhooks]], [[source-metronome-api-reference-pagination]], [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/notifications/list-offset-lifecycle-event-notification-configurations-2026-07-13|2026-07-13 snapshot - offset-notification configuration identity, lifecycle-event policy, archive filtering, endpoint-specific cursor placement, response schema, and authority boundaries]]