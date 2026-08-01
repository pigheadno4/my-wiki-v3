---
title: "Metronome Reset a Threshold Notification API"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/alerts/reset-a-threshold-notification"
raw_files:
  - "metronome/api-reference/alerts/reset-a-threshold-notification-2026-07-13.md"
tags: [metronome, alerts, threshold-notifications, api, asynchronous-processing, webhooks]
---

## Overview

This API reference documents `POST /v1/customer-alerts/reset`, an exceptional-operation endpoint that clears prior evaluation state for one customer threshold notification and starts a fresh assessment against current thresholds. It is intended for correction, configuration-change, testing, debugging, and stuck-state cases rather than routine evaluation.

## Key takeaways

- The request identifies one customer and one threshold notification with required UUID-formatted `customer_id` and `alert_id` properties.
- Reset initiation is immediate, but re-evaluation occurs asynchronously in the background. A `200` confirms that reset and re-evaluation were initiated; the endpoint returns no response body and does not report the resulting threshold state.
- Clearing cached evaluation state may cause a new webhook notification when the current threshold is breached. The page does not guarantee that a webhook is emitted, delivered once, or delivered before any particular subsequent operation.
- The reference documents only the `200` response. It supplies no endpoint-specific error responses, idempotency mechanism, retry rule, rate limit, concurrency rule, or ordering guarantee.

## Eligibility and identifier boundaries

The endpoint is scoped to a specific threshold notification for a specific Metronome customer. The JSON schema requires `customer_id` and `alert_id`; both are strings with UUID format. `customer_id` is described as the Metronome customer ID, and `alert_id` as the Metronome ID of the threshold notification. The page does not document use of ingest aliases, external customer identifiers, notification names, or notification types in place of these IDs.

The source does not define whether archived, deleted, disabled, never-evaluated, already-evaluating, `OK`, or `IN_ALARM` notifications are eligible. It also does not state how the API validates that the alert belongs to the supplied customer, whether the customer and alert must be active, or whether system and offset notifications are rejected. The title and field description limit the documented contract to threshold notifications; they do not establish a general notification-reset API.

The introductory use cases include re-evaluation after threshold modifications, customer-balance or credit adjustments, data corrections, and false-positive or stuck states. Those examples do not establish an in-place alert-update API, define which configuration changes qualify, or say that reset repairs the underlying data or configuration.

## Reset and evaluation state

The operation clears previous or cached evaluation state and starts a fresh assessment against current thresholds. Clearing evaluation state is not documented as archiving the notification, changing its threshold, deleting alert history, retracting an earlier webhook, restoring merchant-controlled access, or changing a customer balance or credit. The page does not name the state immediately after reset, so it does not establish that the alert enters `EVALUATING`, `OK`, `IN_ALARM`, or any other status before the background assessment finishes.

The prose describes both an immediate trigger and background re-evaluation. The safest response boundary is therefore initiation rather than completed evaluation: the reset operation returns immediately, while the new threshold result is produced asynchronously. The source does not define an evaluation completion signal, polling sequence, status transition, data snapshot time, cache-clear atomicity, or interaction with the ordinary continuous-evaluation cadence. It also does not say what “current thresholds” means when configuration or billing data changes concurrently.

## Response and webhook effects

The only documented response is HTTP `200` with description `Success`. The prose says this confirms that the threshold notification was reset and re-evaluation initiated, and explicitly says no response body is returned. A caller therefore cannot learn the post-evaluation state, breached dimension, evaluated amount, evaluation timestamp, or webhook outcome from this response.

A fresh assessment may produce new webhook notifications if thresholds are breached. “May” does not guarantee emission for every reset, and the page does not specify event type, payload, deduplication key, delivery timing, ordering relative to the `200`, retry behavior, or whether a reset of an already-breached notification produces another alarm event. Those delivery mechanics must not be inferred from the reset response; use the dedicated notification and webhook sources for the broader lifecycle and delivery model.

## API contract

- **Method and path:** `POST /v1/customer-alerts/reset`
- **Production server:** `https://api.metronome.com`
- **Authentication declaration:** global HTTP bearer authentication; no endpoint-specific scopes or permissions are listed
- **Operation ID:** `resetCustomerAlerts-v1`
- **Request media type:** `application/json`
- **Required payload properties:** `customer_id`, `alert_id`
- **Property types:** UUID-formatted strings
- **Documented success:** `200 Success`, without response content

The example sends UUID values for both properties. The source does not define additional-property handling, case normalization, nullable values, UUID-version restrictions, maximum lengths, or whether either identifier can be supplied in a header or query parameter.

## Errors, retries, idempotency, and concurrency

No error responses are declared. The page does not say how missing bodies, missing properties, malformed UUIDs, unknown IDs, a customer-alert mismatch, an ineligible notification type or state, insufficient authorization, conflicts, throttling, or server failures are represented. It also does not document which failures occur before versus after evaluation-state clearing.

The request has no documented idempotency key, uniqueness key, conditional header, or replay token, and the source makes no idempotency guarantee. Repeating the request could initiate another fresh assessment and could possibly lead to another webhook; the page does not define duplicate suppression. Clients therefore cannot treat a timeout or ambiguous transport failure as safely retryable on evidence from this page alone.

Concurrent resets and concurrent alert or billing-data changes are also unspecified. There is no documented serialization, last-write rule, version precondition, atomic boundary between state clearing and evaluation, or guarantee about which threshold and data versions win.

## Schema defects and documentation unknowns

> [!warning] Optional request-body ambiguity
> The component schema marks both identifier properties as required, but the OpenAPI operation's `requestBody` object does not set `required: true`. This page does not resolve whether an entirely absent body is rejected.

The response definition has no `content`, which is consistent with the prose saying no response body is returned, but the phrase “confirmation” refers only to the `200` status rather than a response object. The reference does not document response headers, a job or evaluation identifier, or a later completion resource.

The immediate-versus-asynchronous wording distinguishes immediate reset initiation from background assessment, but it does not provide a completion-time guarantee. “Use sparingly” is operating advice, not a rate limit, quota, or concurrency contract. The listed debugging and correction uses do not establish production authorization policy, audit logging, rollback, historical-state retention, or automatic correction of the condition that caused the prior alarm.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-alerts-and-notifications]], [[metronome-webhooks]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]], [[source-metronome-guides-customers-billing-optimize-customer-experience-customer-controls]], [[source-metronome-guides-platform-configuration-setup-webhooks]]

## Raw Sources

- [[raw/metronome/api-reference/alerts/reset-a-threshold-notification-2026-07-13|2026-07-13 snapshot — threshold-notification reset endpoint, asynchronous evaluation, identifiers, and response boundary]]
