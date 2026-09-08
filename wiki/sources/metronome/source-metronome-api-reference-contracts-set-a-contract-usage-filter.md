---
title: "Metronome Set a Contract Usage Filter"
type: source
date_ingested: 2026-09-08
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/contracts/set-a-contract-usage-filter"
raw_files:
  - "metronome/api-reference/contracts/set-a-contract-usage-filter-2026-07-13.md"
tags: [metronome, contracts, usage-filters, billable-metrics]
---

## Overview

This API reference documents how to route usage among one customer's contracts when their rates overlap. The bearer-authenticated `POST /v1/contracts/setUsageFilter` operation targets one customer and contract and lets the associated usage filter change over time.

## Routing behavior and prerequisite

A usage filter chooses the appropriate contract through a predefined group key and selected group values. The documented example uses `project_id` to route two projects to separate contracts.

> [!warning] Billable-metric prerequisite
> The `group_key` must already be defined on the billable metrics underlying the contracts' rate card.

Within `SetUsageFilterPayload`, `customer_id`, `contract_id`, `group_key`, `group_values`, and `starting_at` are required properties. `group_values` is an array of strings, but the schema does not state minimum or maximum cardinality, uniqueness, or unmatched and multiply matched usage behavior.

## Raw-detail navigation

See the raw OpenAPI operation `POST /v1/contracts/setUsageFilter` for bearer authentication, the request example, and response status definitions. See schema key `SetUsageFilterPayload` for exact property types and required fields; the enclosing `requestBody` is not marked required and the object does not declare `additionalProperties`.

## Related

- Company: [[metronome]]
- Concept: [[metronome-customers-and-contracts]]
- Related source: [[source-metronome-guides-implement-metronome-core-concepts-provision-contract]] — broader contract-provisioning and usage-filter navigation

## Raw Sources

- [[raw/metronome/api-reference/contracts/set-a-contract-usage-filter-2026-07-13|2026-07-13 snapshot — usage-filter purpose, prerequisite, request schema, and responses]]
