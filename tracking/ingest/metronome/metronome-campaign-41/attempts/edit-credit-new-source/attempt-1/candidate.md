---
title: "Metronome Edit a Credit API"
type: source
date_ingested: 2026-09-09
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/edit-a-credit"
original_format: webpage
raw_files:
  - "metronome/api-reference/credits-and-commits/edit-a-credit-2026-08-28.md"
tags: [metronome, credits-and-commits, credit-editing, api-reference]
---

## Overview

This API reference documents bearer-authenticated `POST /v2/contracts/credits/edit`, which edits an existing contract-level or customer-level credit. It supports extending a free credit's duration or amount and changing access schedules, applicable products, priority, and other documented credit fields; it edits a credit, not a commit.

## Central behavior

- The operation selects an existing credit with customer and credit identifiers. Its supported metadata, targeting, rate, priority, hierarchy, and access-schedule properties are inventoried under `components.schemas.EditCreditPayload` in the raw OpenAPI.
- Draft invoices reflect an edit immediately. Finalized invoices remain unchanged unless they are voided and regenerated.
- Changing `rate_type` affects current and future invoices; previously finalized invoices must be voided and regenerated for that change to appear.

> [!warning] Finalized-invoice schedule restriction
> An access-schedule segment that was applied to a finalized invoice cannot be removed. The documented sequence is to void that invoice first and then remove the segment.

> [!warning] Omitted-field ambiguity
> The applicability field descriptions say that when both product IDs and product tags are not provided, the credit applies to all products, but this edit page gives no general rule for omitted optional fields. Do not assume ordinary patch or clear-to-all behavior beyond the documented field-specific wording.

## Raw detail routes

| Detail | Verified raw locator |
| --- | --- |
| Operation, authentication, and request example | OpenAPI fence `post /v2/contracts/credits/edit`, then `paths./v2/contracts/credits/edit.post` |
| Editable fields and selectors | `components.schemas.EditCreditPayload` |
| Access-schedule add, update, and removal shapes | `components.schemas.UpdateAccessScheduleInput` |
| Usage targeting and hierarchy variants | `components.schemas.CommitSpecifierInput` and `components.schemas.CommitHierarchyConfiguration` |
| Success and error envelopes | `paths./v2/contracts/credits/edit.post.responses`, with `components.schemas.Id` |

## Related

- Company: [[metronome]]
- Main concept: [[metronome-credits-and-commits]]
- Supporting concept: [[metronome-invoicing]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/edit-a-credit-2026-08-28|2026-08-28 snapshot - credit-edit purpose, invoice effects, access-schedule restriction, and complete OpenAPI schemas]]
