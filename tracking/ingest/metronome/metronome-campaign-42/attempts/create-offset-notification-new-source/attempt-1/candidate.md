---
title: "Metronome API Reference: Create an Offset Lifecycle Event Notification Configuration"
type: source
date_ingested: 2026-09-09
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/notifications/create-an-offset-lifecycle-event-notification-configuration"
raw_files:
  - "metronome/api-reference/notifications/create-an-offset-lifecycle-event-notification-configuration-2026-07-13.md"
tags: [metronome, api, notifications, offset-notifications, lifecycle-events]
---

## Overview

This reference documents bearer-authenticated `POST /v2/notifications/create` for creating and storing an offset lifecycle event notification configuration. The lifecycle event type is inferred from `policy.type`; successful configuration creation is not evidence that the lifecycle event occurred, an offset notification was emitted, or webhook delivery succeeded.

## Key facts

- The operation creates an offset lifecycle event notification configuration, and the configuration's lifecycle event type comes from `policy.type`.
- The offset policy uses a signed ISO 8601 duration relative to the selected lifecycle event: positive values indicate a time after the event and negative values indicate a time before it.
- A successful `200` response places the stored configuration under top-level `data`. Use the raw response schema for its complete property inventory rather than treating the response as an emitted event or delivery record.

## Raw-detail coverage map

- **Operation and authentication:** `## OpenAPI` -> document-level `servers` and `security`, then `paths./v2/notifications/create.post`.
- **Creation payload:** `components.schemas.CreateNotificationConfigPayload`; use `components.schemas.LifecycleEventOffsetPolicy` for the lifecycle-event type and signed offset semantics.
- **Stored configuration response:** `paths./v2/notifications/create.post.responses.200.content.application/json`, with the stored configuration schema at `components.schemas.LifecycleEventOffsetNotificationConfig`.
- **Other schema and failure detail:** keep the complete definitions and documented response details in `## OpenAPI`.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-alerts-and-notifications]]

## Raw Sources

- [[raw/metronome/api-reference/notifications/create-an-offset-lifecycle-event-notification-configuration-2026-07-13|2026-07-13 snapshot - offset lifecycle event notification configuration creation]]
