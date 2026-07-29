---
title: "Apply credits and commits to contracts"
type: source
date_ingested: 2026-07-29
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/create-a-pre-paid-commit"
original_format: webpage
raw_files:
  - "metronome/guides/pricing-packaging/apply-credits-and-commits/create-a-pre-paid-commit-2026-07-13.md"
tags: [metronome, credits-and-commits, prepaid-commits, contracts]
---

## Overview

This guide explains how Metronome models free credits, prepaid commits, postpaid commits, and recurring grants on customer contracts. It distinguishes when balance becomes accessible from when a prepaid amount is invoiced, then follows the balances through product and contract targeting, consumption priority, renewal rollover or period expiration, contract transitions, and line-item invoice application.

## Key takeaways

- An `access_schedule` controls the amount and hour-aligned date range in which a credit or commit can fund usage. Product IDs, product tags, or specifiers can narrow eligible usage, and customer-level grants can also be limited to selected contracts.
- Every credit or commit is associated with a fixed product because that product identifies the prepaid charge, postpaid true-up, or credit on invoices and provides metadata for reporting.
- A prepaid commit is paid in advance, but its access and invoice schedules are independent: one balance can be invoiced once or in multiple installments, and the invoice amount can differ from the accessible amount.
- Lower numeric priorities draw down first. Credits and prepaid commits are applied before postpaid commits; a usage amount can be covered by only one balance at a time, with uncovered usage remaining as overage.
- Recurring credits and commits create a new grant and ledger each period. `commit_duration`, recurrence, proration, rollover, and contract-transition settings determine whether unused value expires or survives into later periods or a renewed contract.

## Access, scope, and prerequisites

API monetary amounts are expressed in cents for USD; other supported currencies use whole units. Before granting value, provision the customer and the relevant contract where applicable, and create or select the fixed product used for invoice attribution.

An access schedule contains one or more amount-and-date segments. Only usage inside a segment's date range can consume its balance. Applicability can be broad or restricted by products, product tags, pricing or presentation-group specifiers, and, for customer-level grants, contract IDs or names. Product tags allow future products in an existing family to consume the same balance without enumerating each ID.

The Metronome app path for a free customer credit is **Customers** > select the customer > **Contract commits and credits** > **Add credit**. The corresponding example calls `POST /v1/contracts/customerCredits/create`. Contract commits are added with **Add commit** during contract creation, and the examples call `POST /v1/contracts/create`. Commits can also exist at customer level for use across all or a subset of that customer's contracts.

## Prepaid and postpaid commits

### Prepaid commits

A prepaid commit represents spend paid in advance. Its access schedule governs when committed value can be used, while its optional invoice schedule governs when and how much is billed. The guide permits any number of invoice installments and documents **Do not invoice** for recording an invoiced amount without generating an invoice for a downstream billing provider.

The worked scenario describes a $10,000 commitment available from October 1, 2024 through October 1, 2025 and billed in $4,000 and $6,000 installments. A priority controls drawdown order when multiple balances apply, and an optional rollover percentage controls how much of the initial balance moves to a new contract during renewal.

### Postpaid commits

A postpaid commit represents spend paid in arrears. Usage during its access schedule is billed normally; if cumulative spend is below the committed amount, Metronome issues a final true-up on the configured invoice date. That date defaults to the contract end and can be moved to a later date. Prepaid commits and credits burn down before postpaid commits, while lower-priority-number postpaid balances consume first among themselves.

## Recurring grants and contract transitions

Recurring credits model free periodic usage, while recurring commits model paid periodic usage. Each period receives a distinct balance and ledger. `commit_duration` determines how many periods unused value remains available, and the recurrence schedule defaults to the contract's usage schedule. When `recurrence_frequency` is set on the contract, the recurring grant anchors to its own `starting_at`; if the contract and grant start dates differ, the first period is not prorated. Otherwise null proration defaults to `FIRST_AND_LAST`, and rounding behavior can be configured for prorated access and invoice amounts.

Upgrades and downgrades use contract renewal transitions: the old contract ends, future recurring charges are removed, and a new related contract carries the new terms. A transition rollover can preserve eligible remaining balances. At a period boundary, the new contract produces a finalized scheduled invoice and a new draft usage invoice. A mid-period renewal prorates the first grant and finalizes usage on the former contract through the transition date. A backdated renewal moves open-period usage to the replacement contract and uses a one-time first-period adjustment before the forward recurring schedule begins.

## Invoice application and drawdown

Credits and commits apply to usage at invoice line-item level rather than only to the aggregate invoice. Covered usage, the negative commit-application offset, and uncovered overage appear as separate invoice lines, preserving product-level attribution for precommitted and overage spend. In the illustrated $10 usage case, a prepaid commit covers $4 and creates a -$4 application line, while the remaining $6 appears as overage. Scheduled commit charges can be consolidated onto the contract's usage statement when that contract setting is enabled.

## Documentation cautions

> [!warning] Contradiction
> The prepaid prose describes $10,000 of accessible value, but its USD-cent API sample sets the access amount to `100000` ($1,000) while the invoice items total `1000000` ($10,000). Both recurring example payloads omit commas and are not valid JSON as printed. Their timelines also conflict with the prose: the first contract starts on January 1 while its recurring credit starts December 1, and the stated January 21 mid-period upgrade request instead starts the replacement contract on January 1 with its recurring commit starting December 1. Finally, these examples encode `rollover_fraction` as `100`, while the dedicated create-contract API source documents the field as a fraction from 0 to 1. Verify the current schema and intended dates and amounts before implementing the examples.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-invoicing]], [[metronome-usage-based-billing]]
- API boundaries: [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-api-reference-credits-and-commits-create-a-commit]]
- Enterprise lifecycle: [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/apply-credits-and-commits/create-a-pre-paid-commit-2026-07-13|2026-07-13 snapshot — credit and commit schedules, lifecycle, and invoice application]]
