---
title: "Metronome API: Get Plan Details"
type: source
date_ingested: 2026-08-27
canonical_url: "https://docs.metronome.com/api-reference/plans/get-plan-details.md"
original_format: webpage
raw_files:
  - "metronome/api-reference/plans/get-plan-details-2026-07-13.md"
tags: [metronome, api, plans, pricing, credit-grants, deprecated]
---

## Overview

This OpenAPI page documents bearer-authenticated `GET /v1/planDetails/{plan_id}`, which retrieves high-level configuration for one legacy Plan. The Plans surface is deprecated, and Metronome directs new clients to Contracts without supplying a Plan-to-Contract identity, field, or migration mapping on this page.

## Query-critical facts

- The required path locator is UUID-formatted `plan_id`; the endpoint documents only an HTTP `200` success response whose top-level object requires `data`.
- `data` references `PlanDetail`, which requires UUID `id`, string `name`, and `custom_fields`; `description`, `minimums`, `overage_rates`, and `credit_grants` are optional. This differs from the separate legacy Plan-list representation already documented in the wiki, where `description` is required and `custom_fields` is optional, so callers must preserve operation-specific requiredness rather than merge the two response shapes.
- A returned minimum requires `name`, numeric `value`, numeric `start_period`, and a credit type. A returned overage rate requires numeric `to_fiat_conversion_factor`, numeric `start_period`, fiat credit type, and source credit type. In both structures, `start_period` is described as the number of billing periods before the charge applies.
- Returned credit-grant configuration requires name, granted and paid numeric amounts, priority, effective duration, `send_invoice`, and credit types for the granted and paid amounts; recurrence duration, recurrence interval, and reason are optional. These are Plan configuration fields, not proof of an issued customer's current balance, ledger state, invoice state, or collection outcome.
- Plan `custom_fields` is required in this detail representation and uses an arbitrary-key map whose values are strings, annotated for the `plan` entity. The endpoint does not define field ordering, configured-key completeness, permissions, redaction, or freshness.

## Material boundaries

- Deprecation is an integration and lifecycle boundary: new clients should use Contracts, but this page names no replacement endpoint, removal date, compatibility period, identity mapping, field mapping, or migration behavior.
- The response exposes financially meaningful configuration surfaces, but it does not define denomination, conversion-factor direction, precision, rounding, charge calculation, credit issuance, balance application, invoice generation, tax, delivery, collection, payment, accounting, or reconciliation behavior. Credit-type identity and the success example's `USD (cents)` label do not establish a universal unit for every Plan.
- This is a configuration read, not a customer assignment, entitlement, billing-state, or historical-state view. The page defines no archive visibility, effective as-of time, version history, result freshness, read-after-write consistency, cache behavior, not-found response, or other non-`200` error contract.
- `PlanDetail` and its nested minimum, overage-rate, and credit-grant objects do not declare `additionalProperties: false`; do not infer closed schemas or unknown-field rejection. The success example shows one possible combination and does not make optional fields universally present.

## Raw-detail coverage map

Use the complete raw snapshot for the production server and bearer-security declaration; exact path, operation ID, and UUID locator; required success envelope; full PlanDetail requiredness; minimum, overage-rate, credit-grant, credit-type, and custom-field schemas; price-ramp timing descriptions; every optional recurrence and reason field; the complete success example and example identifiers and amounts; OpenAPI tag catalog; and the absence of documented non-`200`, history, freshness, migration, and closed-schema guarantees.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-credits-and-commits]]
- Additional affected concepts: [[metronome-custom-fields]], [[metronome-currencies-and-custom-pricing-units]]

## Raw Sources

- [[raw/metronome/api-reference/plans/get-plan-details-2026-07-13|2026-07-13 snapshot - deprecated Plan lookup, financial configuration schemas, custom fields, and read boundaries]]
