---
title: "Metronome API: List Customers on a Plan"
type: source
date_ingested: 2026-09-08
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/plans/list-customers-on-a-plan"
raw_files:
  - "metronome/api-reference/plans/list-customers-on-a-plan-2026-07-13.md"
tags: [metronome, api-reference, plans, customers, contracts, pagination, deprecated]
---

## Overview

This API reference documents bearer-authenticated `GET /v1/planDetails/{plan_id}/customers`, which lists customers associated with one legacy Plan. Its optional `status` filter defaults to `active`, meaning current customers of the Plan; the page is primarily a retrieval route for the deprecated Plans surface and its customer-and-plan response shape.

## Retrieval boundary

> [!warning] Deprecated Plans surface
> Metronome marks this endpoint as deprecated and directs new clients to Contracts. This page does not identify a replacement Contracts operation, establish Plan-to-Contract identity or field mapping, provide a migration procedure, or state a removal date.

The required `plan_id` path parameter is UUID-formatted. Optional query parameters include `limit` from 1 through 100, a `next_page` cursor, and `status`. Status accepts `all`, `active`, `ended`, or `upcoming`; comma-separated values are ORed, but the page says `ended,upcoming` is not yet supported.

A documented `200` JSON response requires a `data` array and nullable sibling `next_page`. Each array item requires both `customer_details` and `plan_details`; use the component schemas for field-level requiredness and configuration-dependent fields.

## Raw detail locators

- Production server, bearer authentication, method, path, operation ID, and deprecation wording: OpenAPI `servers`, top-level `security`, and `paths./planDetails/{plan_id}/customers.get`.
- Required Plan identifier and optional pagination controls: `components.parameters.PlanId`, `PageLimit`, and `NextPage`.
- Status default, values, comma-OR behavior, and unsupported combination: `components.parameters.CustomerPlanStatus`.
- Success envelope, immediate-parent placement, and worked example: `paths./planDetails/{plan_id}/customers.get.responses.200`.
- Customer/Plan pairing and detailed identity, aliases, timestamps, configuration-dependent billable status, Plan assignment dates, custom fields, and Salesforce configuration: `components.schemas.CustomerAndPlanDetail`, `CustomerDetail`, `CustomerPlanDetail`, `CustomerConfig`, `CustomField`, and `BillableStatus`.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-customers-and-contracts]]

## Raw Sources

- [[raw/metronome/api-reference/plans/list-customers-on-a-plan-2026-07-13|2026-07-13 snapshot - deprecated Plan customer listing, active-status default, pagination, response envelope, and schemas]]
