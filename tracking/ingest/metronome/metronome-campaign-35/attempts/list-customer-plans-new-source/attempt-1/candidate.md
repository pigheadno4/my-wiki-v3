---
title: "Metronome API: List Customer Plans"
type: source
date_ingested: 2026-09-01
canonical_url: "https://docs.metronome.com/api-reference/plans/list-customer-plans"
original_format: webpage
raw_files:
  - "metronome/api-reference/plans/list-customer-plans-2026-07-13.md"
tags: [metronome, api, customers, plans, contracts, pagination]
---

## Overview

Bearer-authenticated `GET /v1/customers/{customer_id}/plans` lists one customer's legacy Plan assignments in reverse-chronological order. The operation belongs to the deprecated Plans surface; Metronome directs new clients to Contracts, but this page does not identify a replacement Contract route or define how customer-plan identity and state migrate.

## Query-critical facts

- The required path locator is UUID-formatted `customer_id`. The returned `CustomerPlan` keeps customer-assignment identity distinct from catalog identity: required UUID `id` is the customer-plan ID, while required UUID `plan_id` identifies the Plan.
- The page promises reverse-chronological ordering, but does not name the ordering timestamp, tie-breaker, or treatment of assignments with the same start time. Each returned item requires `starting_on`; optional `ending_before` can expose an end boundary, but the endpoint does not define whether the collection contains active, ended, archived, scheduled, or otherwise filtered assignments.
- Optional query `limit` accepts 1 through 100, and optional `next_page` supplies the cursor at which the next page begins. HTTP `200` requires top-level `data`, an array of customer plans, and nullable sibling `next_page`; the separate [[source-metronome-api-reference-pagination|pagination authority]] supplies repeat-with-cursor-until-null traversal.
- Every customer-plan item also requires `plan_name`, `plan_description`, and `custom_fields`. Optional `net_payment_terms_days` and `trial_info` are ordinary response detail; when `trial_info` is present, its schema requires `ending_before` and `spending_caps`, and every spending-cap item requires `amount`, `amount_remaining`, and `credit_type`. These returned fields do not establish current Contract pricing, an available balance, invoice state, payment collection, or accounting outcome.
- `custom_fields` is an explicitly open map with string values and is annotated for the `customer_plan` entity. The enclosing customer-plan, trial-info, and spending-cap objects do not declare `additionalProperties: false`; unknown-property behavior must not be inferred as closed from the documented property catalogs.

## Material boundaries

- This is a deprecated Plans read. The page tells new clients to use Contracts but names no equivalent Contracts endpoint, Plan-to-Contract or customer-plan-to-contract identity mapping, field mapping, migration procedure, compatibility period, historical-continuity rule, or removal date. The current contract read is a separate authority and must not be treated as a shape-compatible replacement merely because both surfaces describe customer pricing state.
- Reverse-chronological order and cursor traversal do not establish a stable snapshot. The page defines no default page size, total count, cursor lifetime, cursor filter binding, cross-page duplicate-or-skip behavior under change, as-of selector, cache behavior, freshness, or read-after-write visibility. A completed traversal therefore does not prove an immutable or newly current customer-plan history.
- This GET page documents no endpoint-specific retry, timeout-recovery, rate-limit, or non-`200` error contract. It has no request body and establishes no state transition; do not import the separate API-wide POST `Idempotency-Key` execution-admission and replay rules into this operation.

## Raw-detail coverage map

| Raw detail category | Exact raw coverage |
| --- | --- |
| Operation and authority | OpenAPI version, production `/v1` server, document-level bearer security, `GET /customers/{customer_id}/plans`, operation ID, Plans tag, and full provider tag catalog |
| Customer scope and ordering | Required UUID customer path parameter, customer-plan versus Plan identifiers, reverse-chronological statement, required `starting_on`, optional `ending_before`, and unspecified ordering key, tie-breaker, and active-versus-ended filter |
| Pagination and completeness | Optional `limit` bounds of 1 through 100, optional `next_page` request cursor, required top-level `data` and nullable sibling `next_page`, success example, and endpoint-local snapshot, freshness, cursor-lifetime, and retry unknowns |
| Customer-plan representation | Complete requiredness and types for assignment ID, Plan ID, name, description, start and end times, net payment terms, trial information, and customer-plan custom fields |
| Trial and spending-cap detail | Nested trial end, spending-cap array, amount and remaining-amount fields, credit-type identity schema, exact example values, and the absence of denomination, calculation, balance-authority, and lifecycle guarantees |
| Deprecation and migration | Legacy Plans status, direction to Contracts for new clients, and the absence of replacement-route, identity-mapping, field-mapping, migration, continuity, compatibility-period, and removal-date guarantees |
| Schema and error boundary | Explicit open string-valued custom-field map; no closed-object declaration on the other response objects; only documented HTTP `200`; and no endpoint-specific non-success, cache, retry, timeout-recovery, or read-after-write contract |

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-reporting-and-analytics]]
- Secondary concepts: [[metronome-credits-and-commits]], [[metronome-custom-fields]]
- Related sources: [[source-metronome-api-reference-pagination]], [[source-metronome-api-reference-plans-list-plans]], [[source-metronome-api-reference-plans-get-plan-details]], [[source-metronome-api-reference-contracts-get-a-contract-v2]]

## Raw Sources

- [[raw/metronome/api-reference/plans/list-customer-plans-2026-07-13|2026-07-13 snapshot - complete deprecated customer-plan listing, pagination, assignment schema, and Contracts migration boundary]]
