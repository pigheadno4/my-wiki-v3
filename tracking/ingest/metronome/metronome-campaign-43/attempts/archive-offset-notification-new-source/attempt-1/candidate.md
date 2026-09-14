---
title: "Metronome API Reference: Archive an Offset Lifecycle Event Notification Configuration"
type: source
date_ingested: 2026-09-10
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/notifications/archive-an-offset-lifecycle-event-notification-configuration"
raw_files:
  - "metronome/api-reference/notifications/archive-an-offset-lifecycle-event-notification-configuration-2026-07-13.md"
tags: [metronome, api, notifications, offset-notifications, lifecycle-events]
---

## Overview

This reference documents bearer-authenticated `POST /v2/notifications/archive` for archiving one offset lifecycle event notification configuration. The page states that archived notifications are not processed; it does not define the timing or treatment of notification work already generated, in flight, or delivered.

## Key facts

- The operation archives the offset notification configuration selected by ID. Within a supplied JSON payload, required property `id` is the configuration UUID; the enclosing OpenAPI `requestBody` is not marked `required: true`, so omitted-body runtime behavior is not established.
- A successful `200` response requires top-level `data` and routes to the offset-notification configuration schema. This is a configuration response, not a notification-generation, webhook-delivery, or recovery record.

## Material boundary

> [!warning] Processing effect does not establish delivery cancellation or recovery behavior
> The page says archived notifications are not processed, but does not define when that effect begins or whether it covers notification work already generated, queued, in flight, retried, or delivered. It also documents no restore or unarchive operation. Do not expand configuration archival into a guarantee that prior delivery work is canceled, recalled, or recoverable.

> [!warning] Success example does not demonstrate an archive timestamp
> The archival operation's `200` example shows `archived_at: null`, and the response schema permits a nullable archive timestamp. Treat this as an unresolved documentation tension rather than proof that a successful response either has or lacks a populated archive timestamp.

## Raw-detail coverage map

- **Operation and authentication:** `## OpenAPI` -> document-level `security` -> `bearerAuth`, then `paths./v2/notifications/archive.post`.
- **Configuration selector:** `components.schemas.ArchiveNotificationConfigPayload` contains the required `id` property and its UUID format.
- **Success response:** `paths./v2/notifications/archive.post.responses.200.content.application/json` locates the required `data` envelope, example, and `LifecycleEventOffsetNotificationConfig` schema.
- **Errors and stored-configuration detail:** the operation's `400` and `404` responses and the complete configuration and policy schemas remain in `## OpenAPI`.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-alerts-and-notifications]]
- Related sources: [[source-metronome-api-reference-notifications-create-an-offset-lifecycle-event-notification-configuration]], [[source-metronome-api-reference-notifications-edit-an-offset-lifecycle-event-notification-configuration]], [[source-metronome-api-reference-notifications-get-an-offset-lifecycle-event-notification-configuration]], [[source-metronome-api-reference-notifications-list-offset-lifecycle-event-notification-configurations]]

## Raw Sources

- [[raw/metronome/api-reference/notifications/archive-an-offset-lifecycle-event-notification-configuration-2026-07-13|2026-07-13 snapshot - offset notification configuration archival operation, processing boundary, response, and errors]]
