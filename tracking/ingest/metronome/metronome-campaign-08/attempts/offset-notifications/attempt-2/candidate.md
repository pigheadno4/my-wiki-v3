---
title: "Metronome Offset Notifications"
type: source
date_ingested: 2026-07-31
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/customers-billing/set-up-notifications/offset-notifications"
raw_files:
  - "metronome/guides/customers-billing/set-up-notifications/offset-notifications-2026-07-13.md"
tags: [metronome, offset-notifications, webhooks, customer-lifecycle, recurring-commits]
---

## Overview

This guide documents Metronome offset notifications: webhook signals scheduled before or after a known date associated with a system-notification event. It covers relative-time units, payload differences, UI and API creation, prospective-only firing behavior, and an edge case for offsets on future recurring-commit segments.

## Key takeaways

- An offset policy schedules a notification relative to a known date such as a commit end date or contract creation date; amounts can use hours, days, weeks, months, or years.
- Offset policies can be configured around system-notification types. The UI supports relative examples such as three days after contract start or sixty days before a commit segment ends, while the API accepts an ISO 8601 offset amount through `POST /v2/notifications/create`.
- Offset payloads differ from threshold payloads: the page says they omit `properties`. The payload `timestamp` is the source event's time, not the calculated offset fire time.
- Enabling an offset is prospective. Metronome starts generating events from that point forward and does not create events for past data; a past fire time is not replayed, and the notification does not fire if the offset is archived before its fire time.
- Offsets cannot be scheduled before `.create`, `.edit`, or `.archive` events. A long before-start offset on a recurring commit can be delayed because subsequent child commits are generated at most one future billing period ahead.
- The UI instructions say the configured offset applies to all customers and sends its events to all configured webhooks.

## Scheduling and payload semantics

Offset amounts are relative to a source-event date, with before/after policies illustrated across hours through years. The sample `contract.start` payload includes notification and environment identifiers, contract and customer identifiers and custom fields, an `offset_id`, and `offset_duration: "-P3DT12H"`. It is an example rather than a complete or universally required payload schema.

The page explicitly distinguishes the source-event timestamp from the scheduled fire time. For an offset that fires three days after a contract starts, `timestamp` remains the contract start time; consumers must not interpret that field as the time the offset notification was generated or delivered. Unlike threshold-notification payloads, offset payloads do not include a `properties` field. Receivers therefore need type-aware parsing rather than assuming the threshold shape.

## Creation and management

In the UI, a user selects a system-notification type, configures the relative offset, and saves it. The instructions say events then apply to all customers and are delivered to every configured webhook. The API path is `POST /v2/notifications/create`; the request supplies a name and policy containing the system-event type and an ISO 8601 offset amount, and a successful response returns the created configuration with a unique ID.

This page does not provide the complete request or response schema, requiredness, allowed event-type catalog, ISO 8601 validation and sign rules, authentication, authorization, idempotency, update or archive endpoints, error responses, or per-customer and per-webhook filtering controls.

## Prospective lifecycle behavior

Offset generation is not retroactive. The page documents no notification when an existing entity's fire time is already past at offset creation, when a newly created entity's calculated fire time is already past, or when an edit moves the fire time into the past. It also documents no firing after the offset configuration is archived before the scheduled time. A newly created entity can produce a notification when its fire time remains in the future.

The page documents archiving a configuration before its fire time, but it does not define a delete operation, delete endpoint, or deletion semantics.

These examples do not define behavior for every combination of existing entities, edits, archival, simultaneous changes, clock boundaries, or delivery failures. In particular, the page does not promise replay, catch-up, event ordering, exactly-once delivery, or that editing an entity after a prior offset firing will produce a second event.

## Recurring-commit edge case

Metronome says subsequent child commits for a recurring commit are generated at most one future billing period ahead. If a before-`commit.segment.start` offset is longer than that horizon, the future child does not yet exist at the intended scheduled time. The notification instead fires when the next child commit is created. In the monthly/90-day example, it fires approximately 30 days before the segment rather than 90 days before.

This is a documented notification-timing limitation, not a complete recurring-commit generation contract. The page does not define the exact child-creation instant, behavior for variable-length periods, retries after creation, edits to recurrence, or whether the one-period horizon applies outside this offset-notification scenario.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-alerts-and-notifications]], [[metronome-webhooks]], [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-guides-platform-configuration-setup-webhooks]], [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/set-up-notifications/offset-notifications-2026-07-13|2026-07-13 snapshot — offset scheduling, payload, lifecycle, and recurring-commit caveat]]
