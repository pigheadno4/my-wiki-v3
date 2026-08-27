---
title: "Metronome API: Get the Rate Schedule for a Contract"
type: source
date_ingested: 2026-08-27
canonical_url: "https://docs.metronome.com/api-reference/contracts/get-the-rate-schedule-for-a-contract.md"
original_format: webpage
raw_files:
  - "metronome/api-reference/contracts/get-the-rate-schedule-for-a-contract-2026-07-13.md"
tags: [metronome, api, contracts, rate-cards, pricing]
---

## Overview

Bearer-authenticated `POST /v1/contracts/getContractRateSchedule` retrieves the rate schedule for one customer contract at a selected point in time. It resolves the contract's rate card, scheduled changes, and contract overrides for customer-facing price inspection, while returning only entitled rates.

## Query-critical facts

- The JSON payload schema requires UUID `customer_id` and `contract_id` properties. The enclosing OpenAPI `requestBody` is not marked required, so omitted-body behavior is not established.
- Optional date-time `at` selects schedule segments overlapping that time; when omitted, Metronome uses the current timestamp.
- `selectors` uses OR semantics across selector objects, and no selectors returns all rates. Individual selectors can narrow by product ID, product tags, subscription billing frequency, exact pricing-group values, or partial pricing-group values.
- Optional query parameters paginate the result: `limit` accepts 1 through 100 and `next_page` supplies a cursor. HTTP `200` requires a `data` array and can return nullable `next_page`.
- Each schedule entry requires rate-card and product identity, product name, tags and custom fields, `starting_at`, `entitled`, and `list_rate`. It can additionally expose `ending_before`, pricing-group values, an override rate, a commit rate, and subscription billing frequency.
- The returned rate schemas distinguish list, override, and commit-rate surfaces and include flat, percentage, subscription, custom, tiered, and tiered-percentage representations; the full conditional fields and enums remain in raw.

## Material boundaries

- The page documents no result ordering, default page size, cursor lifetime, cross-page snapshot consistency, rate-change freshness, read-after-edit behavior, or non-`200` error contract.
- The payload and principal response objects do not declare `additionalProperties: false`; do not infer rejection of unknown fields. Some rate representations carry client- or feature-gating metadata, so schema presence does not prove universal availability.
- "Entitled" defines which rates this endpoint returns for a contract. The page does not establish application access control, invoice-line creation, final billed amounts, taxes, credits, payment state, or override precedence. Because this is a POST read, the API-wide [[source-metronome-api-reference-idempotency|idempotency authority]] also matters: same-key replay can return the original result and therefore does not prove a fresh schedule read.

## Raw detail coverage

The exact pagination and payload schemas, selector field catalog and matching rules, complete schedule-entry requiredness and nullability, list/override/commit rate variants, billing-frequency and rate-type enums, feature-gating annotations, tier and minimum structures, credit-type fields, custom-field and pricing-group maps, examples, security declaration, and response schema remain in the complete raw reference linked below.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-api-idempotency]]
- Related concepts: [[metronome-credits-and-commits]]
- Related source: [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/contracts/get-the-rate-schedule-for-a-contract-2026-07-13|2026-07-13 snapshot - complete endpoint, selectors, rate schedules, schemas, and examples]]
