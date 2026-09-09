---
title: "Metronome API Reference: Update the Credit End Date"
type: source
date_ingested: 2026-09-09
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/update-the-credit-end-date"
raw_files:
  - "metronome/api-reference/credits-and-commits/update-the-credit-end-date-2026-07-13.md"
tags: [metronome, api-reference, customer-credits, credit-lifecycle]
---

## Overview

This reference documents bearer-authenticated `POST /v1/contracts/customerCredits/updateEndDate` for shortening an existing customer credit's end date so access terminates earlier than originally scheduled. It is a customer-credit operation, not the separate commit end-date operation, and it cannot extend a credit.

## Key facts

- The operation only moves a customer credit's end date earlier. To extend the end date or make broader edits, use the separate edit-credit endpoint.
- `access_ending_before` is an exclusive RFC 3339 cutoff: at that timestamp, access ends and the credit can no longer be drawn down.
- A successful `200` response returns an ID-shaped object under top-level `data`; use the raw response section for the exact envelope.

> [!warning] Credit-versus-commit wording conflict
> The endpoint path, title, operation description, and `customer_id` description identify a customer credit, but the `credit_id` property description says "ID of the commit to update." Treat that sentence as an internal documentation inconsistency, not authority that this endpoint updates a commit, and verify the identifier is the intended customer credit before mutation.

## Raw-detail coverage map

- **Operation and authentication:** `## OpenAPI` -> document-level `servers` and `security`, then `paths./v1/contracts/customerCredits/updateEndDate.post`.
- **Cutoff input:** `components.schemas.UpdateCreditEndDatePayload.properties.access_ending_before` contains the timestamp format and exclusive drawdown cutoff; the same payload schema contains the customer and credit identifiers.
- **Success and errors:** `paths./v1/contracts/customerCredits/updateEndDate.post.responses` contains the `200` `data.id` envelope and documented error routes.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-credits-and-commits]]
- Broader credit edits: [[source-metronome-api-reference-credits-and-commits-edit-a-credit]]
- Distinct commit operation: [[source-metronome-api-reference-credits-and-commits-update-the-commit-end-date]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/update-the-credit-end-date-2026-07-13|2026-07-13 snapshot - customer-credit end-date shortening operation, cutoff schema, response, and errors]]
