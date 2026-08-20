---
title: "Edit a contract"
type: source
date_ingested: 2026-08-19
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/make-pricing-changes/edit-contract.md"
original_format: webpage
raw_files:
  - "metronome/guides/pricing-packaging/make-pricing-changes/edit-contract-2026-07-13.md"
tags: [metronome, contracts, contract-editing, commits, credits, invoicing]
---

## Overview

This guide explains how Metronome contract edits support mid-term commercial changes and corrections through the UI or the `editContract` endpoint. It illustrates schedule and product-applicability changes, explains edit-history and historical-state retrieval, enumerates the supported edit surface, and documents invoice-state, rollover, and archival guardrails.

## Key takeaways

- Contract edits immediately recalculate draft invoices. Finalized invoices remain unchanged, but a finalized invoice that is voided and regenerated reflects the contract's current edited state.
- One worked upsell increases a prepaid commit's access amount, extends its access end, and adds an invoice-schedule item for the incremental charge. A second edit broadens a commit from one eligible product to two for the whole open billing period.
- `getEditHistory` returns edits made through `editContract`, `updateEndDate`, `setUsageFilters`, and the Metronome UI. `getContract` with `as_of_date` returns full contract state at a historical point, and Metronome also records edits in audit logs.
- Supported operations span commits, recurring commits, credits, recurring credits, overrides, scheduled charges, spend-threshold configuration, and contract name and end date changes.
- Finalized and voided invoice associations constrain schedule edits and archiving. Rollover commits cannot themselves be edited, and the originating commit has separate access- and invoice-schedule cutoffs.

## Worked edit flows

### Commit access and invoice schedules

The first BigData example starts with a two-year contract and a $100,000 prepaid commit usable only in year one. Six months later, the customer has $10,000 remaining and negotiates a $200,000 commitment usable through the full contract term. The displayed `/v2/contracts/edit` request identifies `customer_id`, `contract_id`, and `commit_id`; it updates the existing access item to `20000000` and extends `ending_before` to 2027-01-01, then adds a `10000000` invoice item dated 2025-07-01 for the incremental charge. These identifiers, dates, and amounts are illustrative, and the guide does not define the numeric unit in this example.

### Commit product applicability

The second example begins with Commit A applying only to Data Reads. On March 5, the request replaces the shown `applicable_product_ids` value with IDs for Data Reads and Data Writes. The open March draft immediately applies Commit A to both products for the whole billing period, reducing its illustrated total from $10 to $0. The finalized February invoice remains unchanged. If February were voided and regenerated, the guide says the current two-product applicability would apply there as well; the edit timestamp is therefore not presented as a historical eligibility cutoff for regeneration.

## History and historical state

`getEditHistory` returns all recorded edits to a contract, including edits made through `editContract`, `updateEndDate`, `setUsageFilters`, and the UI. The example contains two edit records: an added multiplier override followed by an added prepaid commit, each with its own edit ID and timestamp. To reconstruct the full contract between those edits, the guide passes the first edit's creation time as `as_of_date` to `getContract`; the returned state contains the override but not the later commit. All edits are also recorded in Metronome audit logs available through the UI and API.

## Supported edit surface

The guide enumerates these supported operations:

- Commits: add a commit; edit access and invoice schedules; edit name and description; edit applicable product IDs and tags; edit rollover fraction; or archive the commit.
- Recurring commits: add one, or edit its `ending_before`, invoice amount, and access amount.
- Credits: add a credit; edit its access schedule, name, description, and applicable product IDs or tags; add a recurring credit; or archive a credit.
- Recurring credits: edit `ending_before` and access amount.
- Overrides: add or remove an override.
- Scheduled charges: add one, edit its invoice schedule, or archive it.
- Spend thresholds: add or update spend-threshold configuration.
- Contract identity and lifecycle: update the contract end date or name.

This is a capability list, not a complete request schema. Apart from the two commit examples, the page does not specify required fields, omitted-versus-null behavior, validation and error responses, idempotency, authorization, concurrency, atomicity across multiple updates, or proration and general backdating behavior.

## Limitations and lifecycle guardrails

### Commit and scheduled-charge invoice schedules

An invoice-schedule item associated with a finalized invoice cannot be removed or updated. If the associated invoice is voided, the item still cannot be removed; the page does not state whether updating it after voiding is allowed.

### Commit and credit access schedules

An access-schedule segment applied to a finalized invoice cannot be removed until that invoice is voided. Removing the segment also removes its manual ledger entry. Any access-schedule change immediately affects drafts; finalized invoices remain unchanged unless voided and regenerated, after which they reflect the new schedule. The page does not separately define downstream-provider, payment, refund, tax, or revenue-ledger effects.

### Rollover commits

Rollover commits cannot be edited. The originating commit's access schedule remains editable only until the contract receiving the transition has a finalized invoice, while its invoice schedule remains editable only until the original contract ends. The guide does not define whether either cutoff is inclusive, how concurrent finalization is ordered, or the failure returned after a cutoff.

### Finalized scheduled invoices

If an added invoice item or an edited invoice-item timestamp targets date X and a finalized scheduled invoice already exists at X, that invoice remains untouched and Metronome creates a new finalized scheduled invoice for the edited items. The guide does not describe collection, delivery, duplication protection, or consolidation behavior for the new invoice.

### Archiving terms

Before archiving a commit, all finalized usage invoices to which it applied and all finalized invoices for its payment must be voided. Before archiving a credit, all finalized usage invoices to which it applied must be voided. Before archiving a scheduled charge, all finalized invoices created by it must be voided. The page does not define whether these checks include downstream invoice state or only Metronome invoice state.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-credits-and-commits]], [[metronome-invoicing]]
- Related sources: [[source-metronome-api-reference-contracts-get-contract-edit-history]], [[source-metronome-api-reference-credits-and-commits-edit-a-commit]], [[source-metronome-api-reference-contracts-amend-a-contract]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/make-pricing-changes/edit-contract-2026-07-13|2026-07-13 snapshot — contract edit examples, history, supported operations, and lifecycle guardrails]]
