---
title: "Metronome List System Notification Event Types"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/notifications/list-system-notification-event-types"
raw_files:
  - "metronome/api-reference/notifications/list-system-notification-event-types-2026-07-13.md"
tags: [metronome, api-reference, notifications, lifecycle-events, offset-notifications]
---

## Overview

This API reference documents `POST /v2/notifications/system/list`, which lists available read-only system lifecycle event-type configurations that can be used when creating offset notifications. It defines bearer authentication and the successful response shape, including the lifecycle policy and optional webhook-publication status, but does not enumerate the complete event-type catalog.

## Key takeaways

- The endpoint lists system lifecycle event types for notifications; the documentation describes them as read-only and usable when creating offset notifications.
- The operation is `POST /v2/notifications/system/list` on `https://api.metronome.com` and uses bearer authentication.
- A successful `200` response requires a `data` array and may include a nullable string `cursor`.
- Every returned configuration requires `type` and `policy`; `policy.type` is a lifecycle-event string, with `contract.create` and `contract.start` shown only as examples.
- A configuration may include `is_enabled`, described as whether webhook publishing for that lifecycle event is enabled. The example response omits this optional field.

## Endpoint contract

The OpenAPI operation is identified as `listSystemNotificationConfigs-v2` and is tagged **Notifications**. Its documented production server is `https://api.metronome.com`, with HTTP bearer authentication. The page supplies no request body, query parameters, or request-side cursor field.

The successful response is an `application/json` object whose required `data` property contains `LifecycleEventSystemNotificationConfig` items. The top-level `cursor` is optional and nullable, but the page does not define how a caller supplies it, whether another page can be requested, or what a non-null value means.

## Returned configuration

Each configuration requires:

- `type`: a string indicating a system lifecycle event notification.
- `policy`: an object whose required string `type` identifies the lifecycle event. The schema gives `contract.create` and `contract.start` as examples rather than an exhaustive allowed-value list.

The optional boolean `is_enabled` is described only as whether webhook publishing for the lifecycle event is enabled. The example contains `type: SYSTEM_LIFECYCLE_EVENT`, `policy.type: contract.create`, and `cursor: null`; it does not establish that every returned `type` has the same value or that `contract.create` is the only available policy.

## Documentation boundary

This page does not define the complete event-type catalog, request fields, pagination inputs, error responses, authorization scopes, rate limits, idempotency, ordering, filtering, or how event-type availability changes. It also does not document how `is_enabled` is set or changed, whether disabled configurations remain in the list, offset-creation validation, webhook delivery behavior, or lifecycle-event payloads. No direct contradiction with the existing notification or webhook concepts was found.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-alerts-and-notifications]], [[metronome-webhooks]]
- Related sources: [[source-metronome-guides-customers-billing-set-up-notifications-offset-notifications]], [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]], [[source-metronome-guides-platform-configuration-setup-webhooks]]

## Raw Sources

- [[raw/metronome/api-reference/notifications/list-system-notification-event-types-2026-07-13|2026-07-13 snapshot - system lifecycle event-type listing contract and response schema]]
