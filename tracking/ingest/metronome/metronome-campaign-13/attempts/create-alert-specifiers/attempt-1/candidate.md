---
title: "Create alert specifiers"
type: source
review_level: mechanical
date_ingested: 2026-08-04
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/customers-billing/set-up-notifications/create-alert-specifiers.md"
raw_files:
  - "metronome/guides/customers-billing/set-up-notifications/create-alert-specifiers-2026-07-13.md"
tags: [metronome, alerts, alert-specifiers, custom-fields, credits, commits, webhooks]
---

## Overview

This guide explains alert specifiers for the `low_remaining_contract_credit_and_commit_balance_reached` alert. Specifiers let a merchant include or exclude commits and credits by custom-field conditions, or group balance evaluation by one custom-field key. The guide demonstrates exact-match filters, per-key grouping and webhook payloads, exclusions, status retrieval through `POST /v1/customer-alerts/get`, and a resolved-webhook event.

## Key takeaways

- Without specifiers, the alert evaluates the combined balance of all active commits and credits for a customer and sends one notification when that total falls below the configured threshold.
- A `custom_field_filters` entry with a key and value selects matching commits and credits. Multiple specifiers are OR conditions, while multiple conditions in one specifier are AND conditions.
- Omitting a filter value groups evaluation separately for each unique value of one key. Per-key grouping requires one specifier with one key; the guide says a customer can have up to three per-key balance alerts, with up to 1K unique key-value pairs per group key.
- `exclude` entries are OR conditions. An excluded entity must also be within the inclusion scope of the same specifier.
- Setting or updating a custom-field value on a credit or commit triggers re-evaluation of applicable balance alerts that use `alert_specifiers`. A grouped alert's webhook identifies the triggering key and value; the first group to cross the threshold also produces an overall-alert webhook without a value.
- `POST /v1/customer-alerts/get` can return status for a specified key-value pair. The guide also documents a `low_remaining_contract_credit_and_commit_balance_resolved` webhook when an alert returns from `IN_ALARM` to `OK`, with enablement handled through a Metronome representative.

## Details

### Filter evaluation

Alert specifiers are defined in the `alert_specifiers` array of a `low_remaining_contract_credit_and_commit_balance_reached` alert. An omitted `custom_field_filters` includes all commits and credits. A key/value filter counts only matching entities; multiple filters in one specifier require all conditions, while multiple specifiers are evaluated as OR. The `exclude` array removes matching commits or credits even when they satisfy inclusion conditions.

Custom fields can be set on a commit or credit at creation. The guide says that setting or updating a field on either object triggers re-evaluation of any applicable balance alert using `alert_specifiers`.

### Per-key grouping and webhook payloads

A `custom_field_filters` entry with a key but no value evaluates the balance separately for each unique value. Per-key grouping uses a single specifier with a single key, and the guide says up to three such balance alerts can be configured for one customer with support for up to 1K unique key-value pairs per group key; for keys above 1000 values, it directs readers to contact a Metronome representative.

When a grouped balance reaches its threshold, the webhook's `alert_specifiers` payload identifies the triggering key and value. If that is the first key-value pair to cross the threshold, an additional overall-alert webhook omits the `value` field. The source's examples do not describe webhook delivery timing or retry behavior.

### Exclusion and status retrieval

Exclusion entries are evaluated as OR: a commit or credit is removed when it matches any exclusion condition. The excluded entity type must be within the inclusion scope of that same specifier; the example excludes `is_product_specific: true` credits from a general balance alert.

To retrieve status, send `POST /v1/customer-alerts/get` with `alert_id`, `customer_id`, and either `custom_field_filters` or `alert_specifiers` for the desired key-value pair. The example response includes `customer_status: in_alarm`, an active alert, its threshold, and the matching specifier.

### Documentation boundaries

The examples use different entity labels, including `ContractCredit`, `ContractCreditorCommit`, and `ContractCreditOrCommit`; the guide does not reconcile those labels, so they should be checked against the current API schema. The page supplies worked request and payload examples but does not specify general validation, idempotency, delivery, retry, ordering, or signature semantics. A resolved webhook is described only as an `OK` transition from `IN_ALARM`, and the page says to contact a Metronome representative if that feature must be enabled.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-alerts-and-notifications]], [[metronome-custom-fields]], [[metronome-credits-and-commits]], [[metronome-webhooks]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/set-up-notifications/create-alert-specifiers-2026-07-13|2026-07-13 snapshot — alert specifier inclusion, grouping, exclusion, status retrieval, and resolved webhooks]]
