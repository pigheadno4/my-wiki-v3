---
title: "Metronome Edit a Commit API"
type: source
date_ingested: 2026-07-29
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/edit-a-commit"
original_format: webpage
raw_files:
  - "metronome/api-reference/credits-and-commits/edit-a-commit-2026-07-13.md"
tags: [metronome, credits-and-commits, commit-editing, api-reference]
---

## Overview

This API reference documents Metronome's bearer-authenticated `POST /v2/contracts/commits/edit` endpoint for changing one existing contract-level or customer-level commit. The request identifies the customer and commit, then selectively supplies editable commit fields, schedule operations, product targeting, invoicing routing, rate behavior, or hierarchy access. This is a targeted commit mutation, not the customer-commit creation endpoint and not a general contract edit.

## Key takeaways

- `customer_id` and `commit_id` are the only schema-required request fields; both are UUIDs identifying the customer and the existing commit.
- Editable fields include `name`, `description`, access and invoice schedules, `invoice_contract_id`, product targeting, `product_id`, `priority`, `rate_type`, and `hierarchy_configuration`.
- Access and invoice schedules use separate add, update, and remove arrays. Added access items require `amount`, `starting_at`, and `ending_before`; added invoice items require `timestamp`. Updated and removed items are addressed by item UUID.
- Draft invoices reflect an edit immediately. Finalized invoices remain unchanged unless voided and regenerated, and invoice or access schedule items already tied to finalized invoices have additional update or removal restrictions.
- Product targeting can use product IDs, product tags, or specifiers. If none of those three selector fields is provided, the commit applies to all products; `specifiers` cannot be combined with either direct selector field.
- A successful response contains `data.id`. The documented `400` error has `code` and `message`, but the only enumerated code is `CustomerNotFound`.

## Endpoint and identity

Send a bearer-authenticated `POST` request to `/v2/contracts/commits/edit` with an `application/json` body. The required UUID `customer_id` is described as the customer whose commit is being edited, while `commit_id` identifies the commit itself. No `contract_id` is required, even though the description says the existing commit may be contract-level or customer-level.

This endpoint edits a specific existing commit. It does not create a new customer-level commit like `POST /v1/contracts/customerCommits/create`, and it is narrower than a general contract edit: the editable surface here is the selected commit and its directly related schedules, product applicability, invoicing contract, rate type, priority, and hierarchy configuration.

## Editable request surface

The optional top-level update fields are:

| Field | Documented role |
| --- | --- |
| `name`, `description` | Updated commit display text. |
| `access_schedule` | Add, update, or remove access-schedule items. |
| `invoice_schedule` | Add, update, or remove invoice-schedule items. |
| `invoice_contract_id` | Contract UUID to use for invoicing. |
| `applicable_product_ids`, `applicable_product_tags`, `specifiers` | Alternative ways to determine which usage can draw down the commit. |
| `product_id` | UUID field exposed by the schema without a description. |
| `priority` | Consumption ordering; lower numeric priority applies first when multiple commits are applicable. |
| `rate_type` | Switch current and future invoices between list-rate and commit-rate behavior. |
| `hierarchy_configuration` | Set child access to all children, no children, or a non-empty list of contract UUIDs. |

`rate_type` accepts upper- or lowercase forms of `LIST_RATE` and `COMMIT_RATE`. A rate-type update applies to current and future invoices; previously finalized invoices must be voided and regenerated before they reflect the change.

## Schedule operations and invoice-state constraints

### Access schedule

`access_schedule.add_schedule_items` accepts items that each require a numeric `amount` and date-time `starting_at` and `ending_before` values. An update item requires its UUID `id` and may supply `amount`, `starting_at`, or `ending_before`; a removal item requires only its UUID.

An access-schedule segment that has been applied to a finalized invoice cannot be removed. The page says the invoice can first be voided and the access segment then removed.

### Invoice schedule

`invoice_schedule.add_schedule_items` requires a date-time `timestamp` and may include numeric `amount`, `quantity`, or `unit_price`. An update item requires its UUID `id` and may update those same fields; a removal item requires the item UUID.

An invoice-schedule item associated with a finalized invoice cannot be removed or updated. If the associated invoice has been voided, the item still cannot be removed. The page does not state whether an update becomes available after voiding, so that behavior should not be inferred.

### Effective-time and proration boundary

Schedule timing is expressed through access-item `starting_at` and `ending_before` values and invoice-item `timestamp` values. The operation schema does not expose a separate edit-level `effective_at` field, and this page does not document proration behavior or a proration parameter. The only general timing rule is that draft invoices reflect edits immediately, while finalized invoices remain untouched unless voided and regenerated.

## Product applicability, drawdown, and hierarchy

`applicable_product_ids` targets product UUIDs and `applicable_product_tags` targets product tags. If neither field nor `specifiers` is provided, the commit applies to all products. A commit specifier can filter by one `product_id`, a set of product tags, pricing-group values, or presentation-group values; customer usage must satisfy at least one specifier to draw down the commit or credit.

`specifiers` cannot be used with `applicable_product_ids` or `applicable_product_tags`. Its feature-gated `exclude` array can reject usage that matches the inclusion criteria and an excluding value; within each exclude specifier, product tags match only products with all specified tags. The schema marks this field with `x-stainless-skip` and a Mint feature group.

For hierarchy access, `hierarchy_configuration.child_access` is required when the configuration object is supplied. The allowed variants are `ALL`, `NONE`, or `CONTRACT_IDS`, with lowercase aliases also accepted. `CONTRACT_IDS` requires `contract_ids` with at least one UUID.

## Omitted and nullable fields

Only `customer_id` and `commit_id` are required by `EditCommitPayload`; every editable field is optional in the OpenAPI schema. `applicable_product_ids`, `applicable_product_tags`, `specifiers`, and `priority` are explicitly nullable. The source does not define a general contract for whether omitting an optional field leaves it unchanged or whether passing `null` clears it, so clients should not infer those mutation semantics from this page alone.

The one explicit omission rule concerns product applicability: when `applicable_product_ids`, `applicable_product_tags`, and `specifiers` are all not provided, the commit applies to all products. The schema also exposes a separate top-level `product_id` without explaining how it interacts with those selectors.

## Invoice behavior, response, and errors

Metronome says draft invoices reflect edits immediately. Finalized invoices do not change unless voided and regenerated, including for a `rate_type` change. The schedule-specific restrictions above further limit changes to items already associated with finalized or voided invoices.

A `200` response requires `data`, which contains a UUID `id`; the generic `Id` schema does not label whether this is the commit ID or another edit-related identifier, and the response example uses a value different from the request's `commit_id`. A documented `400` response requires string `code` and `message` fields, with only `CustomerNotFound` enumerated. This page does not enumerate a commit-not-found error or any other validation error codes.

## Documentation boundaries and schema cautions

- The standalone top-level `product_id` has no description and coexists with plural product selectors and specifiers; its intended interaction with those targeting fields is not documented here.
- `rate_type` and hierarchy child-access enums expose uppercase and lowercase spellings as distinct OpenAPI values.
- The success schema returns only a generic UUID `id`, so the response identifier's precise meaning should be verified before relying on it.
- The response map names only `CustomerNotFound`, even though the request also identifies a commit and multiple schedule items; do not treat that as a complete inventory of runtime validation failures.
- The page defines no proration behavior, operation-level effective timestamp, or general omitted-versus-null update rule.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-products-and-rate-cards]]
- Related sources: [[source-metronome-api-reference-credits-and-commits-create-a-commit]], [[source-metronome-api-reference-contracts-get-contract-edit-history]], [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/edit-a-commit-2026-07-13|2026-07-13 snapshot — Edit a Commit API reference]]
