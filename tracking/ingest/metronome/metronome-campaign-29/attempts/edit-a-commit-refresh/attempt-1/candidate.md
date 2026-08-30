---
title: "Metronome Edit a Commit API"
type: source
date_ingested: 2026-08-30
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/edit-a-commit"
original_format: webpage
raw_files:
  - "metronome/api-reference/credits-and-commits/edit-a-commit-2026-08-28.md"
  - "metronome/api-reference/credits-and-commits/edit-a-commit-2026-07-13.md"
tags: [metronome, credits-and-commits, commit-editing, api-reference]
---

## Overview

This API reference documents bearer-authenticated `POST /v2/contracts/commits/edit`, a targeted mutation of one existing contract-level or customer-level commit. It can change commit metadata, access or invoice schedules, usage and contract applicability, invoicing routing, priority, rate behavior, or hierarchy access; it is not a commit-creation operation or a general contract edit.

## Query-critical facts

- The enclosing OpenAPI `requestBody` is not marked required. Within a supplied `EditCommitPayload`, UUID `customer_id` and `commit_id` are required; `commit_id` is the existing resource selector, while the remaining top-level update properties are optional in the schema. The payload and its schedule, specifier, exclusion, and hierarchy objects do not declare `additionalProperties: false`, so omitted-body and unknown-field behavior remain undocumented; only pricing- and presentation-group maps explicitly define arbitrary string-valued properties.
- At immediate parent `EditCommitPayload`, nullable `applicable_contract_ids` selects which contracts a customer-level commit applies to. `null` means all of that customer's contracts, and the field cannot be edited for `POSTPAID` commits or contract-level commits. The page does not define omission, an empty array, invalid or foreign contract IDs, later-created contracts, or how a failed conditional edit is reported.
- At immediate parent `EditCommitPayload`, nullable direct product-ID and product-tag selectors and nullable `specifiers` control eligible usage. If all three are not provided, the field descriptions say the commit applies to all products; separately, `specifiers` cannot be combined with either direct selector and requires usage to meet at least one specifier. Because this is an edit endpoint yet the page gives no general omitted-field patch contract, callers should not silently reinterpret the explicit all-products wording as "leave unchanged."
- At immediate parent `UpdateAccessScheduleInput`, add, update, and remove arrays contain access-item objects: add items require numeric `amount`, `starting_at`, and `ending_before`; update and remove items require UUID `id`, with update optionally accepting those three fields. At immediate parent `UpdateInvoiceScheduleInput`, add items require `timestamp` and may include numeric `amount`, `quantity`, or `unit_price`; update items require `id` and may include those same values, and remove items require `id`. The page does not define a currency, cost basis, balance unit, quantity unit, relationship among `amount`, `quantity`, and `unit_price`, or precision, rounding, sign, bounds, overlap, ordering, or atomicity.
- At immediate parent `EditCommitPayload`, lower numeric `priority` applies first when several commits are eligible. `rate_type` accepts upper- and lowercase list-rate or commit-rate spellings and affects current and future invoices; finalized invoices must be voided and regenerated to reflect a change. `hierarchy_configuration` references an object whose required `child_access` chooses all children, no children, or a non-empty contract-ID list. The separate top-level UUID `product_id` has no description or documented interaction with applicability selectors.
- HTTP `200` requires top-level `data`, whose generic `Id` object requires UUID `id`; the page does not identify that value as the request `commit_id`, and the example values differ. HTTP `400` requires `code` and `message` but enumerates only `CustomerNotFound`, leaving commit, schedule-item, applicability, conditional-edit, authorization, and other validation failures undocumented.

## Lifecycle, financial, and retry boundaries

Draft invoices reflect edits immediately, whereas finalized invoices remain unchanged unless voided and regenerated. An invoice-schedule item associated with a finalized invoice cannot be removed or updated; after its invoice is voided it still cannot be removed, while update-after-void behavior is not stated. An access-schedule segment applied to a finalized invoice can be removed only after voiding that invoice. The endpoint does not define recalculation timing, balance or ledger effects, proration, tax, payment, refund, revenue, downstream-provider propagation, webhook or history visibility, validation order, partial success, transaction boundaries, or concurrent-edit behavior.

`commit_id` identifies the existing commit being changed; it is not a resource-creation uniqueness key. The separate API-wide [[source-metronome-api-reference-idempotency|idempotency authority]] says all POST endpoints accept `Idempotency-Key`, identical same-key parameters return the original result, changed parameters return `409`, retention is at least 24 hours, and a cached result can be `500`. This endpoint does not narrow that authority or define commit-edit state after cached or ambiguous failure, another or expired key, concurrent edits, read-after-write visibility, or whether the generic response `data.id` is a commit or edit identity.

## Documentation boundary

> [!warning] Omission and applicability ambiguity
> The product-selector descriptions explicitly say that not providing IDs, tags, or specifiers makes the commit apply to all products, while the endpoint otherwise supplies no general rule for omitted optional edit fields. Preserve both source-scoped statements; do not assume either a universal clear-to-all rule or a universal leave-unchanged rule without runtime verification.

The page uses numeric schema names `amount`, `quantity`, and `unit_price` without supplying currency, cost, balance, or unit definitions. Dedicated currency and credit-type authorities may describe other surfaces, but they cannot be imported as endpoint-local denomination guarantees.

## Raw-detail coverage map

| Raw detail category | Exact raw coverage |
| --- | --- |
| Operation and envelopes | Server, bearer security, POST path, operation ID, request example, request-body wrapper, success envelope, and `CustomerNotFound` error schema |
| Payload and applicability | Complete `EditCommitPayload`, required customer and commit selectors, metadata, invoicing contract, direct product selectors, customer-contract selector, specifiers, fixed product, priority, rate type, and hierarchy reference |
| Schedule mutation schemas | Full access- and invoice-schedule add, update, and remove item schemas, nested required lists, date-time fields, and numeric financial field names |
| Specifiers and hierarchy | Product and tag matching, string-valued pricing and presentation groups, feature-gated exclusions, child-access unions, enum aliases, and non-empty selected-contract list |
| Lifecycle and errors | Draft/finalized/voided invoice guidance, schedule-item restrictions, HTTP `200` identity surface, and the sole enumerated HTTP `400` code |

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-products-and-rate-cards]], [[metronome-api-idempotency]]
- Secondary concept: [[metronome-currencies-and-custom-pricing-units]]
- Related sources: [[source-metronome-api-reference-contracts-edit-a-contract]], [[source-metronome-api-reference-contracts-get-contract-edit-history]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/edit-a-commit-2026-08-28|2026-08-28 snapshot - targeted commit edit, customer-contract applicability, schedule schemas, invoice-state constraints, response, and errors]]
- [[raw/metronome/api-reference/credits-and-commits/edit-a-commit-2026-07-13|2026-07-13 snapshot - prior targeted commit edit, schedules, product applicability, rate behavior, and hierarchy access]]
