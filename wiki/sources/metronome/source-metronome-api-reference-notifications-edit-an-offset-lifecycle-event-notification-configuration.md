---
title: "Metronome API Reference: Edit an Offset Lifecycle Event Notification Configuration"
type: source
date_ingested: 2026-09-09
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/notifications/edit-an-offset-lifecycle-event-notification-configuration"
raw_files:
  - "metronome/api-reference/notifications/edit-an-offset-lifecycle-event-notification-configuration-2026-07-13.md"
tags: [metronome, api, notifications, offset-notifications, lifecycle-events]
---

## Overview

This reference documents bearer-authenticated `POST /v2/notifications/edit` for editing an existing offset lifecycle event notification configuration. It is configuration-mutation authority, not evidence that a lifecycle event occurred or that a notification was generated or delivered.

## Key facts

- An offset configuration edit identifies the stored configuration and supplies an updated policy. The updated `policy.type` must match the configuration's existing lifecycle event type, so this operation does not document changing the configuration to a different lifecycle-event basis.
- The offset policy retains a lifecycle-event type and a signed ISO 8601 duration: positive offsets schedule after the base event and negative offsets schedule before it. Use `components.schemas.LifecycleEventOffsetPolicy` in the raw snapshot for the exact fields and examples.
- The shared edit payload also covers system lifecycle event configurations. Its `is_enabled` field is supported only for system lifecycle events, so this page does not establish an enable-or-disable control for offset configurations.

## Material boundaries

The OpenAPI request-body wrapper is not marked `required: true`; inside a supplied payload, only `policy` appears in the required-property list. The optional `id` description says it is not provided for system-event configuration updates, but the page does not explicitly state offset-edit omitted-ID behavior. Use `components.schemas.EditNotificationConfigPayload` for that requiredness boundary rather than inferring runtime acceptance.

A successful response requires top-level `data` and permits either a system or offset lifecycle-event notification configuration. The full response inventory and documented `400` error codes remain in `paths./v2/notifications/edit.post`. A successful configuration response does not prove that an underlying lifecycle event occurred, that an offset notification was emitted, or that webhook delivery succeeded.

## Raw-detail coverage map

Use `paths./v2/notifications/edit.post` for the operation identity, production server, bearer security declaration, request example, response envelope, and error response. Use `components.schemas.EditNotificationConfigPayload` for configuration identity, policy-update scope, payload requiredness, and the system-only enablement boundary; use `components.schemas.LifecycleEventOffsetPolicy` for lifecycle-event type and signed offset semantics; and use the two notification-configuration schemas for the complete response fields.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-alerts-and-notifications]]
- Related sources: [[source-metronome-api-reference-notifications-get-an-offset-lifecycle-event-notification-configuration]], [[source-metronome-api-reference-notifications-list-offset-lifecycle-event-notification-configurations]], [[source-metronome-guides-customers-billing-set-up-notifications-offset-notifications]]

## Raw Sources

- [[raw/metronome/api-reference/notifications/edit-an-offset-lifecycle-event-notification-configuration-2026-07-13|2026-07-13 snapshot - offset notification configuration edit, fixed lifecycle-event type, signed offset semantics, system-only enablement, and response schema]]
