---
title: "Metronome API Reference: Get an Offset Lifecycle Event Notification Configuration"
type: source
date_ingested: 2026-09-08
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/notifications/get-an-offset-lifecycle-event-notification-configuration"
raw_files:
  - "metronome/api-reference/notifications/get-an-offset-lifecycle-event-notification-configuration-2026-07-13.md"
tags: [metronome, api, notifications, offset-notifications, lifecycle-events]
---

## Overview

This reference documents `POST /v2/notifications/get`, which retrieves one offset lifecycle event notification configuration by ID. It is the targeted configuration-lookup authority for finding the stored lifecycle-event policy and offset, not evidence that a notification was generated or delivered.

## Key facts

- Within the supplied JSON payload schema, required UUID property `id` selects the notification configuration. The enclosing `requestBody` is not itself marked `required: true`, so this snapshot does not define omitted-body behavior.
- A successful response requires top-level `data`, which contains the offset-notification configuration. Its required `policy` contains required `type` and `offset`: `type` identifies the lifecycle event on which the offset is based, while `offset` is an ISO 8601 duration whose positive values mean after the base event and negative values mean before it.
- The configuration's own `type` field is separate from `policy.type`; the former identifies an offset lifecycle event notification configuration, while the latter identifies its base lifecycle event.

## Material boundary

The documented response exposes configuration metadata, including identity, name, environment, creator, timestamps, archive state, and policy. It does not expose a calculated fire time, generated-event state, webhook delivery state, retry state, or notification history; use the dedicated offset-notification and webhook sources for those behaviors.

## Raw-detail coverage map

Use the exact raw snapshot at `paths./v2/notifications/get.post` for the operation identity, production server, top-level bearer security declaration, request example, response envelope, and documented `400` and `404` errors. Use `components.schemas.GetNotificationConfigPayload` for request-ID type and requiredness; `components.schemas.LifecycleEventOffsetNotificationConfig` for configuration identity, environment, creation, and archive fields; and `components.schemas.LifecycleEventOffsetPolicy` for lifecycle-event type, signed ISO 8601 offset meaning, and examples.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-alerts-and-notifications]]
- Related sources: [[source-metronome-api-reference-notifications-list-offset-lifecycle-event-notification-configurations]], [[source-metronome-api-reference-notifications-list-system-notification-event-types]], [[source-metronome-guides-customers-billing-set-up-notifications-offset-notifications]]

## Raw Sources

- [[raw/metronome/api-reference/notifications/get-an-offset-lifecycle-event-notification-configuration-2026-07-13|2026-07-13 snapshot - targeted configuration lookup, request identity, response placement, lifecycle-event type, signed offset, and error schemas]]
