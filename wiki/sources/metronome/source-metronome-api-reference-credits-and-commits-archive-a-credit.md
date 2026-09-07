---
title: "Metronome API Reference: Archive a Credit"
type: source
date_ingested: 2026-09-07
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/archive-a-credit"
raw_files:
  - "metronome/api-reference/credits-and-commits/archive-a-credit-2026-07-13.md"
tags: [metronome, credits, archive, api]
---

## Overview

This Metronome endpoint deactivates a contract-level or customer-level credit while preserving its historical record. Use the bearer-authenticated `POST /v2/contracts/credits/archive` operation when retiring the full credit rather than reducing its grant.

## Consequential behavior

> [!warning] Archive prerequisites and full-schedule effect
> A credit cannot be archived until every finalized invoice to which it was applied has been voided. The documented correction sequence is to void the affected finalized invoice, archive the credit, and then regenerate the invoice. Archiving deactivates the credit's entire access schedule; use credit editing or a manual ledger entry when the intent is only to reduce the granted amount.

After archival, the credit is excluded by default from `listCustomerCredits` and `listCustomerBalances`; callers can request it with `include_archived`. The archived credit has a null ledger and zero remaining balance.

## Detailed evidence routes

- Operation and authentication: raw OpenAPI header and operation at lines 27-38 and 99-138.
- Request identifiers and schema: `ArchiveCreditPayload` at lines 139-147 and 181-194.
- Success and error envelopes: response definitions and `Id` schema at lines 148-178 and 195-202.

These locators route implementation queries to the immutable snapshot; this source does not restate ordinary payload or response schema detail and does not assert endpoint-specific retry or idempotency behavior.

## Related

- Company: [[metronome]]
- Concept: [[metronome-credits-and-commits]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/archive-a-credit-2026-07-13|Archive a credit raw snapshot]] — complete page and embedded OpenAPI operation
