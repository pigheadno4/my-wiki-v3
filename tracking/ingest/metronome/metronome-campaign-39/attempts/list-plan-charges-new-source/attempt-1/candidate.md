---
title: "Metronome API: List Plan Charges"
type: source
date_ingested: 2026-09-08
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/plans/list-plan-charges"
raw_files:
  - "metronome/api-reference/plans/list-plan-charges-2026-07-13.md"
tags: [metronome, api-reference, plans, charges, pagination, deprecated]
---

## Overview

This API reference documents bearer-authenticated `GET /v1/planDetails/{plan_id}/charges`, which lists charge configurations for one legacy Plan. The page is useful for locating the deprecated Plan-charge response shape; Metronome directs new clients to Contracts but does not identify a replacement Contract operation or mapping here.

## Retrieval boundary

> [!warning] Deprecated Plans surface
> This endpoint belongs to the deprecated Plans API. New implementations should use Contracts; this page does not establish that a Contract response has the same charge model or fields.

The required path parameter `plan_id` is UUID-formatted. Optional query parameters provide a `limit` from 1 through 100 and a `next_page` cursor. A documented `200` JSON response requires a `data` array of `PlanCharge` objects and a nullable sibling `next_page`.

## Raw detail locators

- Method, path, operation ID, bearer authentication, and deprecation notice: OpenAPI `security` and `paths./planDetails/{plan_id}/charges.get`.
- Required Plan identifier and query pagination controls: `components.parameters.PlanId`, `PageLimit`, and `NextPage`.
- Success envelope and worked example: `paths./planDetails/{plan_id}/charges.get.responses.200`.
- Required and optional charge fields, charge-type values, credit-type identity, price tiers, ramp timing, tier-reset behavior, quantity conversion and rounding, and custom fields: `components.schemas.PlanCharge`, `ChargeType`, `CreditType`, and `CustomField`.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-products-and-rate-cards]]
- Migration context: [[metronome-customers-and-contracts]]

## Raw Sources

- [[raw/metronome/api-reference/plans/list-plan-charges-2026-07-13|2026-07-13 snapshot - deprecated Plan charge listing, pagination, response envelope, and schemas]]
