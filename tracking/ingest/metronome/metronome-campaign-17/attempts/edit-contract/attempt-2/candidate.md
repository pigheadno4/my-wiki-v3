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
- `getEditHistory` lists recorded edits, `getContract` with `as_of_date` is the guide's full historical-state route, and Metronome audit logs are a third surface. The guide's `updateEndDate` name conflicts with the dedicated history source's `updateContractEndDate`, and its described edit `created_at` is not shown in the history records.
- Supported operations span commits, recurring commits, credits, recurring credits, overrides, scheduled charges, spend-threshold configuration, and contract name and end date changes.
- Finalized and voided invoice associations constrain schedule edits and archiving. Rollover commits cannot themselves be edited, and the originating commit has separate access- and invoice-schedule cutoffs.

## Worked edit flows

### Commit access and invoice schedules

The first BigData example starts with a two-year contract and a $100,000 prepaid commit usable only in year one. Six months later, the customer has $10,000 remaining and negotiates a $200,000 commitment usable through the full contract term. The displayed `/v2/contracts/edit` request identifies `customer_id`, `contract_id`, and `commit_id`; it updates the existing access item to `20000000` and extends `ending_before` to 2027-01-01, then adds a `10000000` invoice item dated 2025-07-01 for the incremental charge. These identifiers, dates, and amounts are illustrative, and the guide does not define the numeric unit in this example. Both displayed edit calls send `Authorization: Bearer $TOKEN` and `Content-Type: application/json`; the guide does not define token issuance, required permissions, or scope requirements.

### Commit product applicability

The second example begins with Commit A applying only to Data Reads. On March 5, the request submits `applicable_product_ids` containing IDs for both Data Reads and Data Writes. The open March draft immediately applies Commit A to both products for the whole billing period, reducing its illustrated total from $10 to $0. The finalized February invoice remains unchanged. If February were voided and regenerated, the guide says the current two-product applicability would apply there as well; the edit timestamp is therefore not presented as a historical eligibility cutoff for regeneration. This example does not establish whether arrays generally replace, merge, or append, or how omitted and null values behave.

## History and historical state

`getEditHistory` returns all recorded edits to a contract, including edits made through `editContract`, the guide's named end-date endpoint, `setUsageFilters`, and the UI. Its example contains two edit records: an added multiplier override followed by an added prepaid commit, each with its own edit ID and `timestamp`.

> [!warning] Documentation inconsistency — endpoint name
> This guide names the end-date endpoint `updateEndDate`, while the dedicated Get Contract Edit History source names it `updateContractEndDate`. The sources do not reconcile the names, so neither should be treated as current runtime truth without a current endpoint authority.

The guide identifies `getContract` with `as_of_date` as the route for retrieving full contract state at a historical point. Its displayed state after the first edit but before the second contains the override and an empty `commits` array.

> [!warning] Documentation inconsistency — historical timestamp source
> The prose says the first edit's `created_at` is passed as `as_of_date`, but the shown edit records expose `timestamp`, not `created_at`. The displayed historical contract state's `created_at` is `2025-02-26T23:06:32.574000+00:00`, before the first edit's `timestamp` of `2025-02-26T23:07:00.727000+00:00`, and the actual `getContract` request is not shown. The exact timestamp source and request value therefore remain unresolved.

Metronome separately says all contract edits are recorded in audit logs available through the UI and API. Edit-history records, historical full-state retrieval, and audit logs are distinct documented surfaces; the guide does not define their consistency, ordering, or retention relationship.

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

This is a capability list, not a complete request schema. Apart from the two commit examples, the page does not specify required fields, general array replacement-versus-merge behavior, omitted-versus-null behavior, validation and error responses, idempotency, token issuance or required permission and scope rules, concurrency, atomicity across multiple updates, or proration and general backdating behavior.

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
