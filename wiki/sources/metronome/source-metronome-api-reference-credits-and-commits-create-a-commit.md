---
title: "Create a commit"
type: source
date_ingested: 2026-07-28
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/create-a-commit"
original_format: webpage
raw_files:
  - "metronome/api-reference/credits-and-commits/create-a-commit-2026-07-13.md"
tags: [metronome, credits-and-commits, customer-commits, api]
---

## Overview

This API reference documents Metronome's customer-level commit creation endpoint. It creates prepaid or postpaid spending commitments that can apply across a customer's contracts or be limited to specified contracts. The page recommends adding commitments directly to contracts through create or edit APIs for most standard use cases.

## Key takeaways

- Send `POST /v1/contracts/customerCommits/create` with `customer_id`, `type`, `priority`, `product_id`, and `access_schedule`; success returns the created ID.
- Postpaid commits require an invoice schedule, matching access and invoice totals, and one item in each schedule. Prepaid commits can omit the invoice schedule to create a complimentary, uninvoiced commit.
- `invoice_contract_id` is required for postpaid commits and invoiced prepaid commits, except when `do_not_invoice=true`.
- Product targeting can use product IDs, product tags, or specifiers. Specifiers cannot be combined with either of the first two targeting fields.
- Lower numeric priority is consumed first; at equal priority, contract-level commits and credits precede customer-level ones.
- The response map lists `200`, `400`, and `404`, while the `uniqueness_key` description separately documents a `409` duplicate failure.

## Request contract

The endpoint uses bearer authentication. Its five schema-required fields are:

| Field | Role |
| --- | --- |
| `customer_id` | Customer that owns the commit. |
| `type` | Prepaid or postpaid commitment. |
| `priority` | Consumption order; lower values apply first. |
| `product_id` | Fixed product used to invoice the commitment amount. |
| `access_schedule` | Balance-distribution periods and amounts. |

Each access-schedule item requires `amount`, inclusive `starting_at`, and exclusive `ending_before`. Its `credit_type_id` defaults to USD cents when omitted.

## Type and invoicing rules

For a postpaid commit, `invoice_schedule` and `invoice_contract_id` are required, the access and invoice totals must match, and the prose permits one schedule item in each schedule. For prepaid commits, omitting the invoice schedule creates a complimentary commit without an invoice. An invoiced prepaid commit also requires `invoice_contract_id`, unless its invoice schedule sets `do_not_invoice=true`.

Point-in-time invoice items can provide either `amount` or the pair `unit_price` and `quantity`. The reusable invoice-schedule schema also exposes a recurring schedule with monthly, quarterly, semiannual, or annual frequency and divided, divided-rounded, or per-occurrence distribution.

## Scope, targeting, and ordering

`applicable_contract_ids` restricts the balance to named contracts; if omitted, it applies across all customer contracts. Product scope can be expressed with product IDs, product tags, or specifiers. With none of these fields, the commit applies to all products.

A usage item needs to satisfy at least one specifier. Within a specifier, product tags require all listed tags, and pricing-group or presentation-group values can further constrain matching. Specifier `exclude` is feature-gated, as are the NetSuite sales-order and Salesforce opportunity fields.

`uniqueness_key` is 1–128 characters and prevents duplicate credit or commit creation. Reusing a key fails instead of creating a new record.

> [!warning] Documentation inconsistencies and boundaries
> The schema accepts uppercase and lowercase commit-type enum values, while the prose names lowercase values. The generic invoice-schedule schema exposes `recurring_schedule`, but the postpaid-specific prose requires one schedule item; verify support before combining postpaid commits with a recurring invoice schedule. The uniqueness-key description documents HTTP `409`, although the operation response map lists only `200`, `400`, and `404`. One schema description also misspells `access_schedule` as `accesss_schedule`.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]]
- Preferred contract-level path: [[source-metronome-api-reference-contracts-create-a-contract]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/create-a-commit-2026-07-13|2026-07-13 snapshot — customer-level commit creation API]]
