---
title: "Metronome System Notifications"
type: source
date_ingested: 2026-08-27
canonical_url: "https://docs.metronome.com/guides/customers-billing/set-up-notifications/system-notifications.md"
original_format: webpage
raw_files:
  - "metronome/guides/customers-billing/set-up-notifications/system-notifications-2026-07-13.md"
tags: [metronome, notifications, webhooks, contracts, commits, credits, lifecycle-events]
---

## Overview

This guide defines Metronome system notifications for time-based automation around customer contract, commit, and credit lifecycle events. It identifies the available event policies, their example webhook payload families, and the account-wide UI and API controls for enabling prospective publication.

## Query-critical facts

- A system notification is tied either to an object's configured timestamp, such as contract start, or to the time an action occurs, such as contract creation. The documented use case is automation around a customer's key lifecycle events.
- The catalog contains five contract policies for create, start, edit, end, and archive; five commit policies for create, edit, archive, segment start, and segment end; and the same five lifecycle policies for credits. Segment start and end payloads expose the triggering segment's index, count, and identifier in addition to the associated object, contract, and customer context.
- System-notification payloads differ from threshold-notification payloads: system payloads do not include `properties`. The examples otherwise show notification identity, policy `type`, timestamp, environment, customer identity and custom fields, plus object-specific contract, commit, credit, recurring-parent, and segment fields. Receivers therefore cannot assume one payload shape for both notification families.
- System notifications can be enabled in the Notifications UI or with `POST /v2/notifications/edit` by passing the selected policy and `is_enabled: true`; a successful API call returns HTTP `200`. The UI says every system notification is disabled by default for an account and that enabling one publishes that event for all customers to all configured webhooks.
- Enablement is prospective: Metronome starts generating events only from the point of enablement and does not create notifications for past data. The policy itself cannot be edited.

## Material boundaries

- This page provides payload examples rather than a normative closed schema. It does not define field requiredness, nullability, forward-compatible additions, payload-version negotiation, or whether every shown custom-field and recurring-parent field is always present. Use the raw examples for implementation inspection without converting example presence into a universal guarantee.
- The page says enabled events are sent to every configured webhook, but it does not define HTTP delivery, signing, latency, ordering, retry duration, duplicate delivery, deduplication, endpoint failure handling, or replay behavior. Those mechanics belong to the dedicated [[metronome-webhooks]] authority.
- The API walkthrough names the mutation and a `200` result but supplies no complete request or response schema, authentication declaration, error catalog, authorization scope, disablement behavior, propagation timing, concurrent-edit semantics, or treatment of already generated or in-flight notifications. The separate [[source-metronome-api-reference-idempotency|API-wide POST idempotency authority]] applies `Idempotency-Key`, but this guide adds no endpoint-specific guarantee for no-key or expired-key retries, cached-error recovery, or the final state after an ambiguous failure.
- Prospective generation and immutable policy selection mean enablement cannot be used to reconstruct missed historical lifecycle events, while this page does not identify an API reconciliation procedure for that gap.

## Raw-detail coverage map

Use the raw page for the complete 15-policy event catalog; every contract, commit, credit, recurring-parent, and segment payload example; notification, object, customer, environment, custom-field, and segment fields; the UI navigation and confirmation walkthrough; the `POST /v2/notifications/edit` enablement outline; default-disabled account behavior; all-customers and all-configured-webhooks scope; and the prospective-only and immutable-policy limitations. Dedicated webhook and API references remain authoritative for delivery, verification, retries, complete mutation schemas, errors, and recovery.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-alerts-and-notifications]], [[metronome-webhooks]], [[metronome-customers-and-contracts]], [[metronome-credits-and-commits]]
- Related source: [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/set-up-notifications/system-notifications-2026-07-13|2026-07-13 snapshot - lifecycle-event catalog, webhook payload examples, enablement routes, scope, and historical-data limitation]]
