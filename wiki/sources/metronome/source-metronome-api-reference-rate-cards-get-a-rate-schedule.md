---
title: "Metronome API: Get a Rate Schedule"
type: source
date_ingested: 2026-09-11
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/rate-cards/get-a-rate-schedule"
raw_files:
  - "metronome/api-reference/rate-cards/get-a-rate-schedule-2026-07-13.md"
tags: [metronome, api-reference, rate-cards, rate-schedules]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/contract-pricing/rate-cards/getRateSchedule`, which retrieves scheduled rate-card pricing from a chosen starting date. It is intended for catalog and product-experience views of upcoming pricing changes, not for customer-contract pricing that includes contract-level overrides.

## Retrieval scope

The payload schema requires a rate-card UUID and `starting_at`, defined as an inclusive schedule boundary. Optional `ending_before` is exclusive; when it is omitted, the response includes all future schedule segments. Optional selectors can filter by product ID, billing frequency, or exact or partial pricing-group values; selector objects use ANY matching, while no selectors returns all rates. The enclosing OpenAPI `requestBody` is not marked required, so omitted-body behavior is not established.

Optional query parameters provide a result limit and a next-page cursor. A successful response places the scheduled-rate entries in top-level `data` and can include `next_page`; use the raw schemas for the complete request, selector, schedule-entry, rate, commit-rate, tier, minimum, and credit-type shapes.

> [!warning] Rate-card schedules are not contract-specific schedules
> For a specific customer's contract, including contract-level overrides, this page directs callers to `getContractRateSchedule`. This endpoint does not establish contract-override precedence or a customer's final invoiced price.

## Raw detail locators

- Method, path, operation ID, bearer authentication, request example, and response envelope: OpenAPI fence; top-level `security`; and `paths./v1/contract-pricing/rate-cards/getRateSchedule.post`.
- Required payload properties and date/filter scope: `components.schemas.GetRateSchedulePayload`.
- Selector matching: `components.schemas.RateSelector`.
- Scheduled-rate response fields and nested pricing schemas: `components.schemas.RateSchedule`, `Rate`, `CommitRate`, `Tier`, `MinimumConfig`, and `CreditType`.
- Query pagination: `components.parameters.PageLimit` and `components.parameters.NextPage`.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-products-and-rate-cards]]
- Contract-specific schedule: [[source-metronome-api-reference-contracts-get-the-rate-schedule-for-a-contract]]

## Raw Sources

- [[raw/metronome/api-reference/rate-cards/get-a-rate-schedule-2026-07-13|2026-07-13 snapshot - rate-card schedule retrieval, date and selector filters, and scheduled-rate schemas]]
