---
title: "Metronome Shared Plan and Contract Alert Endpoints"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/plans-shared-endpoints/notifications"
raw_files:
  - "metronome/plans-shared-endpoints/notifications-2026-07-13.md"
tags: [metronome, alerts, notifications, plans, contracts, api]
---

## Overview

This Metronome documentation overview identifies a shared alert endpoint surface for Plans and Contracts. It inventories creation, customer retrieval and listing, reset, and archival routes, then lists the alert types supported when targeting plans.

## Key takeaways

- The documented alert endpoints are shared by Plans and Contracts, although their input and response parameters can differ by targeted entity.
- The overview lists five unversioned route labels: `/alerts/create`, `/customer-alerts/get`, `/customer-alerts/list`, `/customer-alerts/reset`, and `/alerts/archive`.
- For plans, `alert_type` can identify low credit balance, low remaining plan days, low remaining credit percentage, or a usage-threshold condition.
- This page does not supply HTTP methods, version prefixes, request or response schemas, authentication, errors, state-transition rules, or the parameter differences between Plans and Contracts.

## Shared endpoint inventory

| Route label | Documented purpose |
| --- | --- |
| `/alerts/create` | Create an alert configuration for a plan or contract. |
| `/customer-alerts/get` | Retrieve one customer alert configuration. |
| `/customer-alerts/list` | List a customer's active alerts. |
| `/customer-alerts/reset` | Clear an alert's triggered state. |
| `/alerts/archive` | Archive a configuration so it no longer triggers. |

The source presents these as shared endpoints but does not identify which request or response fields vary by entity. It also does not state whether every operation uses the same customer scope or whether archived configurations remain retrievable.

## Plan alert types

The plan-targeted `alert_type` values listed by the page are:

- `low_credit_balance_reached`
- `low_remaining_days_in_plan_reached`
- `low_remaining_credit_percentage_reached`
- `usage_threshold_reached`

The page does not define each condition's threshold unit, evaluation cadence, state model, payload, supported filters, or whether this list is exhaustive across other alert surfaces. It points to the Contracts version of the creation documentation but does not enumerate the Contract-specific parameter differences.

## Documentation boundary

The route labels here omit HTTP methods and API version prefixes. The dedicated reset reference documents `POST /v1/customer-alerts/reset`; this overview's `/customer-alerts/reset` label should therefore be treated as navigation-level endpoint identification rather than a replacement for the versioned API contract in [[source-metronome-api-reference-alerts-reset-a-threshold-notification]].

No direct contradiction with the existing Metronome alert and notification material was found. This page adds the shared Plan-and-Contract endpoint inventory and the four plan-targeted alert types, while the existing lifecycle and API sources remain authoritative for evaluation, webhook delivery, and operation-specific schemas.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-alerts-and-notifications]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]], [[source-metronome-api-reference-alerts-reset-a-threshold-notification]]

## Raw Sources

- [[raw/metronome/plans-shared-endpoints/notifications-2026-07-13|2026-07-13 snapshot - shared Plan and Contract alert endpoints and plan alert types]]
