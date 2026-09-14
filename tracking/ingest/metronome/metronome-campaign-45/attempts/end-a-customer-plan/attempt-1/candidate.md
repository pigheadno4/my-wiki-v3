---
title: "End a customer plan"
type: source
date_ingested: 2026-09-13
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/plans/end-a-customer-plan"
raw_files:
  - "metronome/api-reference/plans/end-a-customer-plan-2026-07-13.md"
tags: [metronome, api-reference, plans, customers, deprecated]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/customers/{customer_id}/plans/{customer_plan_id}/end`, which changes the end date of one legacy customer-Plan relationship. The Plans endpoint is deprecated; Metronome directs new clients to Contracts without identifying a replacement operation or mapping the legacy relationship to a Contract.

## Material behavior and warnings

- `ending_before` is an exclusive RFC 3339 timestamp that must be midnight UTC. If it is omitted from a supplied payload, the page says the Plan end date is cleared.
- Setting `void_invoices` to true permits an end date before the last finalized invoice date and voids invoices generated after the Plan end date.

> [!warning] Conditional downstream Stripe action
> `void_stripe_invoices` applies only when `void_invoices` is true. When both are true, Metronome says it will attempt to void each finalized Stripe invoice, or delete it if it is still a draft. This is an attempted downstream action, not a documented guarantee of Stripe success.

> [!warning] Deprecated Plans surface
> This operation changes a legacy customer Plan, not a Contract. The page provides no Contracts replacement endpoint, identity mapping, migration procedure, compatibility period, or removal date.

## Raw-detail locators

- Operation identity and bearer authentication: OpenAPI document-level `security` and `paths./customers/{customer_id}/plans/{customer_plan_id}/end.post`; the production server supplies the `/v1` prefix.
- Customer and customer-Plan targets: `components.parameters.CustomerId` and `components.parameters.CustomerPlanId`; the latter is the ID of the customer-Plan relationship.
- End-date and invoice controls: `components.schemas.EndCustomerPlanPayload`, including `ending_before`, `void_invoices`, and `void_stripe_invoices`. The enclosing `requestBody` and payload properties are not marked required; use the explicit `ending_before` description for its omission behavior.
- Success response: `paths./customers/{customer_id}/plans/{customer_plan_id}/end.post.responses.200`, which documents an empty-object schema.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-customers-and-contracts]]

## Raw Sources

- [[raw/metronome/api-reference/plans/end-a-customer-plan-2026-07-13|2026-07-13 snapshot - deprecated customer-Plan end-date operation, timing rules, invoice controls, and response]]
