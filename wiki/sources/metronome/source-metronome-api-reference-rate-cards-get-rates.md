---
title: "Metronome API: Get Rates"
type: source
date_ingested: 2026-09-08
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/rate-cards/get-rates"
raw_files:
  - "metronome/api-reference/rate-cards/get-rates-2026-07-13.md"
tags: [metronome, api-reference, rate-cards, pricing-catalog, rate-schedules]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/contract-pricing/rate-cards/getRates`, which retrieves a rate card's rate schedule at a supplied timestamp. It is the rate-card pricing read for product experiences and other catalog lookups, with optional selectors and cursor pagination.

## Retrieval scope

The supplied JSON payload schema requires UUID `rate_card_id` and date-time `at`; `at` is described as the inclusive starting point for the schedule. The enclosing OpenAPI `requestBody` is not marked required, so omitted-body behavior is not established. Optional `selectors` use OR semantics across selector objects, while supplying no selectors returns all rates. Selector fields can narrow by product ID, product tags, billing frequency, exact pricing-group values, or partial pricing-group values; use the raw schemas for each field's matching rule and enum.

Optional query `limit` accepts 1 through 100 results, and `next_page` supplies a cursor. HTTP `200` requires top-level `data`, an array of `RateSchedule` entries, and may include nullable `next_page`. Each schedule entry requires product identity and metadata, `starting_at`, `entitled`, and `rate`; optional fields include `ending_before`, pricing-group values, `commit_rate`, and billing frequency.

> [!warning] Rate-card rates are not customer-contract rates
> This operation reads the rate schedule on a rate card. For a specific customer's contract, including contract-level overrides, the page directs callers to `getContractRateSchedule`. This source does not establish contract-override precedence, final invoice amounts, result ordering, cursor lifetime, cross-page snapshot consistency, or rate-change freshness.

## Raw detail locators

- Method, path, operation ID, bearer authentication, and request media type: OpenAPI fence and `paths./v1/contract-pricing/rate-cards/getRates.post`, plus top-level `security`.
- Payload-property requiredness, timestamp meaning, request example, and selector presence: `paths./v1/contract-pricing/rate-cards/getRates.post.requestBody` and `components.schemas.GetRatesPayload`.
- Selector filters, matching semantics, string-map shapes, and billing-frequency variants: `components.schemas.RateSelectorWithProductTags`.
- Query pagination controls: `components.parameters.PageLimit` and `components.parameters.NextPage`.
- Success envelope and immediate placement of `data` and `next_page`: `paths./v1/contract-pricing/rate-cards/getRates.post.responses.200`.
- Schedule-entry fields and requiredness, list and commit rate forms, rate-type enums, tiers, minimum configuration, pricing-group maps, and credit-type identity: `components.schemas.RateSchedule`, `Rate`, `CommitRate`, `Tier`, `MinimumConfig`, and `CreditType`.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-products-and-rate-cards]]
- Supporting concept: [[metronome-customers-and-contracts]]
- Contract-specific route: [[source-metronome-api-reference-contracts-get-the-rate-schedule-for-a-contract]]

## Raw Sources

- [[raw/metronome/api-reference/rate-cards/get-rates-2026-07-13|2026-07-13 snapshot - rate-card rate-schedule retrieval, selector matching, pagination, and response schemas]]

## Related raw API references

- [[raw/metronome/api-reference/contracts/get-the-rate-schedule-for-a-contract-2026-07-13|Contract rate-schedule reference]] - navigation only for customer-contract rates and overrides; not used as factual evidence for this source.
