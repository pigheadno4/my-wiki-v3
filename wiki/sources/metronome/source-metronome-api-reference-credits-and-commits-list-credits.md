---
title: "List credits"
type: source
date_ingested: 2026-09-07
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/list-credits"
raw_files:
  - "metronome/api-reference/credits-and-commits/list-credits-2026-08-28.md"
tags: [metronome, api-reference, credits-and-commits, customer-credits]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/contracts/customerCredits/list`, which retrieves customer credits, including promotional and contract-specific credits. It is the evidence route for finding credit access schedules, applicability, optional ledgers, and calculated balances; exact request fields and response schemas remain in the immutable raw snapshot.

HTTP `200` returns an object whose required `data` array contains `Credit` objects and whose required, nullable `next_page` supports continuation.

## Query-critical routes

- Within a supplied JSON object, `customer_id` is the only required property. The enclosing OpenAPI `requestBody` is not marked required, and the request object does not declare `additionalProperties`, so omitted-body and unknown-field behavior are undocumented.
- The raw request schema is the authority for the optional credit, date-window, contract/archive scope, ledger, balance, page-token, and limit controls. `limit` ranges from 1 to 25 and defaults to 25; the page does not define ordering, cursor lifetime, invalid-cursor behavior, or cross-page snapshot consistency.
- `include_ledgers` requests ordered balance-impacting events and `include_balance` requests the current accessible balance; both are documented as potentially slower. The balance schema excludes expired and upcoming segments from current balance, floors the calculated value at zero when excessive negative manual entries would exceed remaining positive value, and includes future-dated manual entries on active segments. Use the raw `CreditLedger` union and ledger-entry component keys for exact event shapes.
- Use `components.schemas.Credit` for credit identity, contract association, priority, attribution product, access schedule, applicability, subscription configuration, ledger, balance, metadata, and hierarchy fields. Ordinary property requiredness, enums, annotations, and nested shapes are intentionally retained in raw rather than reconstructed here.

## Documentation cautions

> [!warning] Credit-versus-commit wording
> The operation is named **List credits**, its success `data` items reference the `Credit` schema, and the path is `/customerCredits/list`. However, the pagination description says it returns up to 25 "commits" and the `credit_id` guideline says it retrieves a specific "commit". Do not infer that this endpoint lists commits from those two phrases; verify runtime behavior if that distinction matters.

> [!warning] Product field naming and purpose
> The narrative calls the attribution field `product_id` and explicitly says it is for external quote-to-cash mapping, not the product to which the credit applies. The response schema instead exposes a required `product` object with `id` and `name`, while applicability is represented separately through `applicable_product_ids`, `applicable_product_tags`, and `specifiers`. Use the exact raw schema and live API contract before mapping these fields.

## Raw-detail locators

- Operation, bearer security, and request controls: OpenAPI `paths./v1/contracts/customerCredits/list.post` and `requestBody.content.application/json.schema`.
- Success envelope and cursor placement: `responses.200.content.application/json.schema`.
- Credit fields and applicability: `components.schemas.Credit`, `ScheduleDuration`, `CommitSpecifier`, and `ExcludeSpecifier`.
- Optional ledger and balance expansion: `components.schemas.CreditLedger`, its referenced ledger-entry schemas, and `BalanceForCommitsAndCredits`.
- Nested subscription, custom-field, hierarchy, and rollover shapes: their exact keys under `components.schemas`.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-credits-and-commits]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/list-credits-2026-08-28|2026-08-28 snapshot - customer-credit list purpose, request controls, response envelope, credit schemas, ledger events, and calculated balance]]
