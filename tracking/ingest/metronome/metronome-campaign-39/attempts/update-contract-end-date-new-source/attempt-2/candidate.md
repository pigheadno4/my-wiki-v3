---
title: "Metronome API Reference: Update the Contract End Date"
type: source
date_ingested: 2026-09-08
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/contracts/update-the-contract-end-date"
raw_files:
  - "metronome/api-reference/contracts/update-the-contract-end-date-2026-07-13.md"
tags: [metronome, contracts, end-date, invoicing, api]
---

## Overview

This OpenAPI page documents the bearer-authenticated `POST /v1/contracts/updateEndDate` operation for adding, changing, or removing one contract's exclusive end timestamp. It is the targeted evidence for how moving that boundary earlier or later affects contract terms, draft usage statements, scheduled invoices, and in-advance subscriptions.

## Retained behavior

- Ending a contract early impacts draft usage statements, truncates any terms, and removes upcoming scheduled invoices.
- Moving the end date into the future extends only the contract length: it does not extend terms, scheduled invoices, or in-advance subscriptions.
- Within a supplied payload, UUID `customer_id` and `contract_id` are required. Optional RFC 3339 `ending_before` is exclusive; omitting it updates the contract to be open-ended.
- `allow_ending_before_finalized_invoice` defaults to `true` and permits an end date earlier than existing finalized-invoice end timestamps. Those finalized invoices remain unchanged; Metronome says callers can void and regenerate finalized usage invoices to incorporate the new end date.

## Material boundary

Extending the contract boundary is not a renewal of its terms, invoice schedule, or in-advance subscription. The page does not define endpoint-specific propagation, concurrency, or ambiguous-failure recovery, so the successful response alone should not be treated as proof that every downstream view or system has reconciled.

## Raw-detail coverage map

- Use `paths./v1/contracts/updateEndDate.post`, including `description` and `operationId`, for the exact operation and lifecycle wording.
- Use `components.schemas.UpdateContractEndDatePayload` for identifier formats, the exclusive `ending_before` behavior, the finalized-invoice override, and defaults.
- Use `paths./v1/contracts/updateEndDate.post.requestBody.content.application/json.example` for the request example.
- Use `paths./v1/contracts/updateEndDate.post.responses` with `components.schemas.Id`, `components.schemas.Error`, and `components.responses.NotFound` for the immediate `data.id` success placement and the documented `400` and `404` shapes.
- Use top-level `servers` and `security` for the production host and bearer-authentication declaration.

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-customers-and-contracts]]
- Purpose-fit navigation: [[metronome-invoicing]], [[metronome-subscriptions]]
- API-wide retry context: [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/contracts/update-the-contract-end-date-2026-07-13|2026-07-13 snapshot - targeted contract end-date mutation, lifecycle effects, payload schema, and responses]]