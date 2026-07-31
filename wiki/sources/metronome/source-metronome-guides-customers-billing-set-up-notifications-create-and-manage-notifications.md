---
title: "Manage your customer lifecycle with Metronome notifications"
type: source
date_ingested: 2026-07-31
canonical_url: "https://docs.metronome.com/guides/customers-billing/set-up-notifications/create-and-manage-notifications"
original_format: webpage
raw_files:
  - "metronome/guides/customers-billing/set-up-notifications/create-and-manage-notifications-2026-07-13.md"
tags: [metronome, notifications, webhooks, customer-lifecycle, thresholds]
---

## Overview

This guide explains how Metronome notifications turn customer activity, contract events, and billing conditions into webhook-delivered signals. It distinguishes threshold, system, and offset notifications, then documents their delivery model, evaluation timing, state behavior, and operational uses.

## Key takeaways

- Threshold notifications fire when monitored conditions are met, system notifications follow object events or configured timestamps, and offset notifications follow a user-defined schedule relative to an event.
- Notifications are delivered asynchronously as JSON webhook payloads to configured endpoints; all notification types use HTTPS POST.
- Failed deliveries are retried with exponential backoff and jitter for up to 48 hours. Delivery is at least once, so endpoints must safely handle duplicates.
- Threshold conditions are evaluated at least every three minutes, and a notification is documented to fire within five minutes after usage that breaches the threshold is ingested.
- System and offset notifications are stateless. Threshold notifications are stateful and move between `OK` and `IN_ALARM`, with `EVALUATING` representing the pre-evaluation condition and an optional resolved event when an alarm returns to `OK`.
- Metronome currently sends every notification to every configured webhook; this page does not describe per-webhook notification filtering.

## Notification families and uses

Threshold notifications monitor conditions such as spend exceeding an amount or available credit falling below a percentage. System notifications cover object creation, updates, and scheduled lifecycle moments such as contract starts or ends. Offset notifications use a merchant-defined relative policy, such as several days before a commit expires or after a contract starts.

The guide positions these signals as inputs to merchant-owned workflows: onboarding and trial reminders, usage-based access management, sales notifications about expiring contracts or exhausted commits, and proactive customer communication before credits expire or contracts renew. The notification itself is an action signal; the merchant remains responsible for the downstream product, communication, or operational response.

## Delivery model

Metronome sends notifications asynchronously as JSON-formatted webhooks. Payloads follow a consistent schema and can include `customer_id`, `timestamp`, and fields for the relevant object. Payloads also include a signature header for origin verification, while the dedicated [[source-metronome-guides-platform-configuration-setup-webhooks]] page remains the authority for the exact verification procedure.

If an endpoint is unavailable, Metronome retries with exponential backoff and jitter for up to 48 hours or until delivery succeeds. Because delivery is at least once, duplicates are possible and receivers should be idempotent. The guide also recommends retaining delivery logs for audit and downstream debugging.

## Evaluation, scheduling, and state

Threshold evaluation occurs at least once every three minutes. The page says a threshold notification fires within five minutes after the triggering usage is ingested. System notifications are generated from an object's configured timestamp or an action such as an edit, while offset notifications are generated from a user-defined policy relative to an event; both are described as near-real-time delivery at the applicable moment.

System and offset notifications are stateless because they do not track an ongoing condition after their scheduled trigger. Threshold notifications are continuously evaluated. The page describes `OK` and `IN_ALARM` as their two ongoing states, while separately listing `EVALUATING` before the first evaluation. A threshold can return from `IN_ALARM` to `OK`, and an additional `*_resolved` notification may be emitted when that behavior is enabled.

The initial state depends on underlying data. For example, a customer with no active commits remains `OK` for commit-balance notifications until a commit exists and is consumed.

## Operating guidance and boundaries

The guide recommends system notifications for time-based lifecycle automation, threshold notifications for continuous spend, usage, and credit monitoring, and offset notifications for proactive relative-date workflows. Custom fields can narrow notification policies to customer groups such as an enterprise segment or product tier. Receivers should make endpoints idempotent and retain delivery records.

> [!info] Evolving
> Metronome says it is expanding the available system and threshold notification types. This page documents no fixed completeness guarantee for the catalog.

Metronome currently supports webhook delivery only, and all notifications are sent to all configured webhooks. The page does not document endpoint configuration steps, a complete payload schema, event-ordering guarantees, or per-destination filtering; use [[source-metronome-guides-platform-configuration-setup-webhooks]] for the broader delivery and verification contract.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-alerts-and-notifications]], [[metronome-webhooks]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-guides-platform-configuration-setup-webhooks]], [[source-metronome-guides-pricing-packaging-billing-model-guides-create-a-trial]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/set-up-notifications/create-and-manage-notifications-2026-07-13|2026-07-13 snapshot — notification types, delivery, scheduling, and states]]
