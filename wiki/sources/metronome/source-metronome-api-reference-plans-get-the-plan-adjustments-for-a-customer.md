---
title: "Metronome API: Get the Plan Adjustments for a Customer"
type: source
date_ingested: 2026-09-10
canonical_url: "https://docs.metronome.com/api-reference/plans/get-the-plan-adjustments-for-a-customer"
original_format: webpage
raw_files:
  - "metronome/api-reference/plans/get-the-plan-adjustments-for-a-customer-2026-07-13.md"
tags: [metronome, api, plans, price-adjustments, customers, contracts]
---

## Overview

Bearer-authenticated `GET /v1/customers/{customer_id}/plans/{customer_plan_id}/priceAdjustments` lists price adjustments for one selected legacy customer-Plan relationship. Metronome marks this Plans endpoint as deprecated and directs new clients to Contracts, without identifying a replacement Contracts operation or mapping the legacy relationship or adjustments to Contract objects.

## Query-critical facts

- The route requires both a UUID `customer_id` and a UUID `customer_plan_id`; the latter is explicitly the ID of a customer-Plan relationship, not the catalog Plan ID. Use a customer-plan assignment identity when selecting this operation.
- HTTP `200` places the adjustment collection in top-level `data` and the nullable continuation cursor in sibling `next_page`. Optional `limit` and `next_page` query parameters control traversal; exact bounds and cursor schema remain at the raw OpenAPI locators below.
- Each `data` item is a `PriceAdjustment`; consult the exact schema for its required fields, adjustment and charge categories, values, quantity, and tier detail rather than treating this summary as a complete response contract.

## Material boundaries

- This is a read on the deprecated Plans surface; it does not create, apply, update, or remove an adjustment.
- "New clients should implement using Contracts" is migration direction, not evidence that a particular Contract endpoint is a drop-in replacement. This page provides no Plan-to-Contract or customer-plan-to-contract identity mapping, field mapping, migration procedure, compatibility period, or removal date.

## Raw-detail coverage map

| Raw detail category | Exact raw coverage |
| --- | --- |
| Operation and authority | `## OpenAPI` → `/customers/{customer_id}/plans/{customer_plan_id}/priceAdjustments` → `get`; production `/v1` server and document-level bearer security |
| Customer-plan selection | `components.parameters.CustomerId` and `components.parameters.CustomerPlanId`, including UUID formats and the customer-plan relationship description |
| Response and traversal | Operation `responses.200.content.application/json.schema`; `components.parameters.PageLimit`; `components.parameters.NextPage` |
| Adjustment detail | `components.schemas.PriceAdjustment` and `components.schemas.ChargeType`, including required properties and category-specific value, quantity, and tier fields |
| Deprecation boundary | Operation `description` under the GET path and the page introduction |

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-customers-and-contracts]]
- Supporting concept: [[metronome-products-and-rate-cards]]
- Related source for discovering legacy customer-plan assignment identity: [[source-metronome-api-reference-plans-list-customer-plans]]

## Raw Sources

- [[raw/metronome/api-reference/plans/get-the-plan-adjustments-for-a-customer-2026-07-13|2026-07-13 snapshot - complete deprecated customer-Plan adjustment GET operation and schema]]
