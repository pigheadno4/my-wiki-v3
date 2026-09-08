---
title: "Metronome Manage Contract Lifecycle Transitions"
type: source
date_ingested: 2026-09-08
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/customers-billing/manage-customers/manage-customer-lifecycle"
raw_files:
  - "metronome/guides/customers-billing/manage-customers/manage-customer-lifecycle-2026-07-13.md"
tags: [metronome, contracts, contract-lifecycle, renewals, entitlements]
---

## Overview

This Metronome guide uses worked enterprise-contract scenarios to show how customer contracts are created, changed during their term, renewed into a linked successor, and ended early. It is a retrieval entry point for contract lifecycle and product-access workflow questions; the dated examples and request payloads remain in the raw snapshot.

## Query-critical facts

- A mid-term add-on is modeled as an edit to the existing contract. In the worked example, the edit schedules a new-product entitlement, adds a product-scoped prepaid commitment, and applies a discounted rate from October 1, 2025.
- A renewal is modeled as a new contract linked to the previous contract with transition type `renewal`. The January 1, 2026 example illustrates how an eligible remaining commitment rolls into the successor contract; its amounts, dates, scope, and drawdown order are example-specific.
- To conclude a contract early, the guide schedules a new contract end date through the update-end-date API. Its example treats financial obligations and product access as separate concerns at the end of the relationship.

## Material boundary

Ending the contract does not by itself document automatic access revocation inside the merchant's product. The guide tells the merchant to configure an alert that emits a webhook and to make its entitlement system listen for that webhook and gate access.

The monetary amounts, discounts, dates, rollover result, priorities, product IDs, and request bodies are worked examples, not stated platform defaults. Verify implementation details against the exact raw sections and the linked dedicated API references.

## Raw-detail coverage map

- `# Manage contract lifecycle transitions` states the guide's purpose and lifecycle capabilities.
- `## Create an enterprise contract motion` contains the provisioning sequence, illustrative terms, `/v1/contracts/create` request, and contract-read entitlement check.
- `## Mid-term add-ons and renewals motion` contains the dated Product B beta-launch scenario, `/v2/contracts/edit` example, successor-contract renewal transition, and illustrative rollover calculation.
- `## End a contract motion` contains the early-end workflow, alert/webhook and entitlement-system responsibilities, example-specific prepaid outcome, and `/v1/contracts/updateEndDate` request.

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-customers-and-contracts]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/manage-customers/manage-customer-lifecycle-2026-07-13|2026-07-13 snapshot - contract creation, mid-term edit, renewal, and early-end examples]]
