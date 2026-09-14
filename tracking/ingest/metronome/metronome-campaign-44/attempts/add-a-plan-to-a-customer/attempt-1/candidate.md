---
title: "Metronome API: Add a Plan to a Customer"
type: source
date_ingested: 2026-09-11
canonical_url: "https://docs.metronome.com/api-reference/plans/add-a-plan-to-a-customer"
original_format: webpage
raw_files:
  - "metronome/api-reference/plans/add-a-plan-to-a-customer-2026-07-13.md"
tags: [metronome, api, plans, customers, contracts, price-adjustments]
---

## Overview

Bearer-authenticated `POST /v1/customers/{customer_id}/plans/add` associates an existing customer with an existing Plan for a specified date range. This belongs to the deprecated Plans surface; Metronome directs new clients to Contracts without identifying a drop-in replacement or a Plan-to-Contract migration mapping.

## Query-critical facts

- The required UUID path selector is `customer_id`. In the supplied JSON payload, `plan_id` and `starting_on` are required properties; `starting_on` must be an RFC 3339 timestamp at midnight UTC. Optional `ending_before` is an exclusive RFC 3339 end timestamp and must also be at midnight UTC.
- The OpenAPI operation does not mark the enclosing `requestBody` as required, even though `AddPlanToCustomerPayload` marks `plan_id` and `starting_on` as required. Do not infer omitted-body runtime behavior from the payload property's requiredness.
- The payload can apply price adjustments on top of Plan pricing. Use the exact `price_adjustments` schema locator below for its adjustment selectors and configuration rather than treating this summary as a complete request contract; the raw also locates optional trial and overage-adjustment structures.
- HTTP `200` returns required top-level `data` referencing the `Id` schema. The page does not define what the returned `data.id` identifies, so it should not be treated as the customer ID, Plan ID, customer-Plan relationship ID, or Contract ID without separate authority.

## Material boundaries

- This endpoint adds a legacy Plan assignment; it does not create a Contract. The instruction for new clients to use Contracts supplies no replacement endpoint, identity or field mapping, migration procedure, compatibility period, or removal date.
- `ending_before` is exclusive, while both date boundaries must be midnight UTC. Preserve those qualifications when constructing or interpreting an assignment interval.

## Raw-detail coverage map

| Raw detail category | Exact raw coverage |
| --- | --- |
| Operation and authority | `## OpenAPI` -> `/customers/{customer_id}/plans/add` -> `post`; production `/v1` server and document-level bearer security |
| Customer and Plan selection | Operation `parameters` -> `CustomerId`; `components.schemas.AddPlanToCustomerPayload` -> `required` and `properties.plan_id` |
| Date range | `components.schemas.AddPlanToCustomerPayload` -> `properties.starting_on` and `properties.ending_before` |
| Price adjustments | `components.schemas.AddPlanToCustomerPayload` -> `properties.price_adjustments`, including item requiredness, adjustment categories, values, quantity, tier, and ramp start |
| Other optional configuration | `components.schemas.AddPlanToCustomerPayload` -> `properties.net_payment_terms_days`, `trial_spec`, and `overage_rate_adjustments` |
| Success response | Operation `responses.200.content.application/json.schema` and `components.schemas.Id` |
| Deprecation boundary | Page introduction and operation `description` |

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-customers-and-contracts]]

## Raw Sources

- [[raw/metronome/api-reference/plans/add-a-plan-to-a-customer-2026-07-13|2026-07-13 snapshot - complete deprecated customer-Plan association POST operation and schema]]
