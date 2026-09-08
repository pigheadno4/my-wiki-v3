---
title: "Metronome API: Archive a Commit"
type: source
date_ingested: 2026-09-08
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/archive-a-commit"
raw_files:
  - "metronome/api-reference/credits-and-commits/archive-a-commit-2026-07-13.md"
tags: [metronome, credits, commits, archival]
---

## Overview

Metronome exposes a bearer-secured `POST /v2/contracts/commits/archive` operation for deactivating a contract-level or customer-level commit while preserving historical records. Before archival, every finalized usage invoice to which the commit was applied and every finalized commit-payment invoice must be voided.

## Key takeaways

- The documented correction sequence is to void the affected finalized usage and commit-payment invoices, archive the commit, and regenerate the voided usage invoice without the archived commit's application.
- Archived commits no longer appear by default in `listCustomerCommits` or `listCustomerBalances`; callers can use `include_archived` to request their details.
- An archived commit has a null ledger and zero remaining balance.

> [!warning] Full deactivation
> Archival deactivates the commit's entire access schedule. To reduce rather than fully deactivate a grant, the page instead routes operators to `editCommit` or `addManualBalanceLedgerEntry`.

## API and detail locators

- Authentication and operation: `OpenAPI > security` and `OpenAPI > paths > /v2/contracts/commits/archive > post`.
- Request schema: `OpenAPI > paths > /v2/contracts/commits/archive > post > requestBody` references `components > schemas > ArchiveCommitPayload`. The enclosing request body is not marked required, while the referenced payload requires UUID `customer_id` and `commit_id`; unknown-field behavior is not specified.
- Response schema: `OpenAPI > paths > /v2/contracts/commits/archive > post > responses`. HTTP `200` requires `data`, whose referenced `Id` schema requires UUID `id`; the `400` schema and `CustomerNotFound` code are recorded at the same locator.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-invoicing]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/archive-a-commit-2026-07-13|Archive a commit]] — complete collected documentation and embedded OpenAPI operation
