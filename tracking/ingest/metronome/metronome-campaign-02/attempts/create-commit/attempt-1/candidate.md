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
This API reference documents Metronome's customer-level commit creation endpoint. It creates prepaid or postpaid spending commitments that can apply across a customer's contracts or be limited to specified contracts, although the page recommends creating commitments directly on customer contracts for most standard use cases.

## Key takeaways
- Send `POST /v1/contracts/customerCommits/create` with `customer_id`, `type`, `priority`, `product_id`, and `access_schedule`; the API returns a commit identifier on success.
- `type` supports prepaid and postpaid values. Postpaid commits require an invoice schedule, require matching access and invoice totals, and permit only one item in each schedule.
- `invoice_contract_id` is required for postpaid commits and prepaid commits that have billing, except when a prepaid commit is free or `do_not_invoice` is true.
- Product targeting can use product IDs, product tags, or specifiers; specifiers cannot be combined with either of the other two targeting fields.
- The documented responses are `200` success, `400` bad request, and `404` not found. A reused `uniqueness_key` is documented to fail with `409`, despite no `409` response entry in the operation's response map.

## Details
The endpoint is authenticated with bearer authentication. The required request fields are `customer_id`, `type`, `priority`, `product_id`, and `access_schedule`; `product_id` is described as required because products are used to invoice the commit amount. `access_schedule` requires schedule items whose individual items require `amount`, inclusive `starting_at`, and exclusive `ending_before`.

For `POSTPAID`, `invoice_schedule` is required, only one schedule item is allowed in each schedule, and invoice totals must match the access amount. The invoice schedule can provide `amount`, or `unit_price` together with `quantity`; its schema also permits a recurring schedule. For `PREPAID`, omitting `invoice_schedule` creates a complimentary commit with no invoice. `do_not_invoice` applies only to commit invoice schedules and suppresses invoice generation when true.

`applicable_contract_ids` scopes a commit to contracts; without it, the commit applies to all contracts. If no applicable product IDs, tags, or specifiers are supplied, it applies to all products. Lower numeric `priority` values are applied first; ties give contract-level commits and credits precedence over customer-level commits and credits. `netsuite_sales_order_id` and `salesforce_opportunity_id` are feature-gated by client configuration; `exclude` within a specifier is also feature-gated.

> [!warning] Documentation inconsistency
> The schema's `type` enum accepts both uppercase and lowercase forms, while the prose says callers must specify either `"prepaid"` or `"postpaid"`. The `invoice_schedule` description also spells `access_schedule` as `accesss_schedule`; the surrounding requirements consistently refer to `access_schedule`. The uniqueness-key description documents a `409` failure, but the operation explicitly lists only `200`, `400`, and `404` responses.

## Related
- Coordinator audit: determine whether existing Metronome company and customer-commit concept pages should be linked; this candidate deliberately adds no wiki links.

## Raw Sources
- [[raw/metronome/api-reference/credits-and-commits/create-a-commit-2026-07-13|create-a-commit-2026-07-13]] — verbatim Metronome API reference for customer-level commit creation.
