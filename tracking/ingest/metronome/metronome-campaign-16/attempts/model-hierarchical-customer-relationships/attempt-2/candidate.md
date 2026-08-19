---
title: "Model hierarchical customer relationships"
type: source
date_ingested: 2026-08-19
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/model-hierarchical-customer-relationships.md"
original_format: webpage
raw_files:
  - "metronome/guides/pricing-packaging/billing-model-guides/model-hierarchical-customer-relationships-2026-07-13.md"
tags: [metronome, account-hierarchies, customers, contracts, commits, consolidated-invoicing]
---

## Overview

This guide models one-level parent-child account relationships across distinct Metronome customers and contracts. It combines shared or selectively accessible commitments, independent child pricing, parent-versus-self payment routing, and optional parent-level invoice consolidation for enterprise organizations.

The examples use Disney and its subsidiaries to illustrate the configuration rather than define a complete contract API. Dedicated API references remain authoritative for request validation, enum handling, mutation behavior, and monetary denomination.

## Key takeaways

- A hierarchy contains distinct customer objects and contracts, supports only one parent-child level, and has a maximum of 10 active nodes. Relationships are configured during contract creation; each customer still requires its own contract.
- Parent commits can expose balance to all children, no children, or selected child contract IDs. Parent and child contracts must be active during the same period for child access. The guide states that hierarchies can also share credits, but its worked access configurations are commit examples.
- A child can pay itself and receive a separate usage statement, or name the parent as payer and consolidate its usage statement into the parent invoice. Consolidation requires `payer: "PARENT"`; self-paying children must use `usage_statement_behavior: "SEPARATE"`.
- Consolidated invoice inclusion additionally depends on the parent using `invoice_consolidation_type: "CONCATENATE"`, the child service period being bounded by the parent service period, and parent and child issue dates aligning on the same day.
- Each child's usage is rated under its own contract and can use a distinct rate card or override. Parent tiered pricing applies only to direct parent usage, not aggregated child usage.
- Consolidated invoice and breakdown examples retain origin invoice, contract, and customer identifiers so consumers can analyze subsidiary spend and contract performance.
- Hierarchy billing currently supports Stripe only. Parent commit alerts may be delayed when only children send usage, and invoice and commit embeddable dashboards do not work for customers whose contract participates in a hierarchy.

## Relationship and contract model

Create separate parent and child customers and configure billing for each. The child contract's `hierarchy_configuration.parent` identifies both the parent contract and parent customer. The same child configuration chooses `payer` and `usage_statement_behavior`; the examples pair `SELF` with `SEPARATE` and `PARENT` with `CONSOLIDATE`. The guide does not document reparenting, detachment, deletion, concurrent edits, lifecycle transitions, or whether these pairs exhaust every accepted combination.

The hierarchy is limited to one parent-child level, with no grandchildren or deeper nesting, and no more than 10 active nodes. One contract cannot automatically apply to every child: each customer needs its own contract. Hierarchy relationships are established as part of contract creation rather than through a separate relationship endpoint in this guide.

## Shared and selective commitments

A parent commit's `hierarchy_configuration.child_access` controls which child contracts can draw down the balance. The examples use `all` for organization-wide access, `none` for parent-only access, and `contract_ids` with selected child contract IDs for selective access. Children configured as self-payers pay their own overages after a shared parent commit is exhausted. Parent and child contracts must both be active during the same period for the child to access the parent commit.

Selective access can coexist with contract-specific pricing. In the worked example, subsidiaries use different rate cards, one child receives a multiplier override, and parent commits target different product IDs. This establishes per-contract rating and balance eligibility in the example, but not general precedence among overlapping commits, balance priorities, rate overrides, or simultaneous drawdown. The page also does not define validation or enforcement for cycles, duplicate parents, node-limit violations, reparenting, detachment, deletion, or concurrent hierarchy changes.

## Parent payment and consolidated invoicing

The consolidation example gives the parent `invoice_consolidation_type: "CONCATENATE"` and configures the child with `payer: "PARENT"` and `usage_statement_behavior: "CONSOLIDATE"`. The resulting consolidated usage statement is paid through the parent's billing provider and contains line items that identify their originating customer and contract. A self-paying child cannot use consolidation according to the troubleshooting section.

Metronome still generates standalone usage statements for the parent and every child and exposes them through its UI, API, and data export. When consolidation is enabled, those standalone statements are not sent to downstream billing providers. The guide warns merchant UIs to avoid counting both the standalone parent statement and the consolidated invoice as parent spend.

A child invoice consolidates only when its usage service period is bounded by the parent's service period and the issue dates align on the same day. The page illustrates those conditions but does not define timezone handling, partial-period proration, late usage, regeneration, correction, finalization ordering, or failure recovery. When a child invoice fails the bounded-service-period or same-issue-day checks, the page does not say whether it is routed separately, withheld from the provider, retried, surfaced as an error, or later consolidated.

## Inspecting hierarchy and invoice origin

The guide retrieves a contract with `POST /v2/contracts/get`; a parent response shows its child contract and customer IDs. It retrieves a consolidated invoice with `POST /v1/invoices/get`; the illustrated response has type `USAGE_CONSOLIDATED`, lists constituent invoices, and places origin identifiers on usage line items. `POST /v1/invoices/breakdown` similarly returns origin customer and contract IDs, which can be grouped for subsidiary-spend and contract-performance analysis.

These are worked response fragments, not complete endpoint contracts. The page does not define authentication beyond the curl bearer header, required and optional response fields, pagination, error responses, consistency, finalization state, or whether every consolidated line-item type carries the same origin object.

## Limitations and documentation cautions

- Only Stripe billing is supported for hierarchies; marketplace billing is described as coming soon without a date or supported-provider contract.
- Parent commit-balance alerts do not automatically trigger merely because a child consumes the commit. The guide says evaluation occurs when the parent receives usage and may be delayed when only children receive usage; it gives no latency, replay, or eventual-evaluation guarantee.
- The final spend-alert bullet ends with the incomplete phrase `parent spend alerts only include parent's`. No scope conclusion should be inferred from that truncated sentence.
- Invoice and commit embeddable dashboards do not work for customers with a contract in a hierarchy. The page does not state whether this applies to other dashboards, reports, API views, or data export.

> [!warning] Dollar-amount contradiction
> The guide calls its shared parent commitment $10M, while both the access and invoice schedule payloads use `amount: 10000000`. Existing Metronome currency evidence states that USD API values use cents, under which `10000000` is $100,000, not $10M. The same scaling tension recurs where the guide labels a parent commit $200K while using `amount: 200000`, and a child commit $500K while using `amount: 500000`. The payloads do not identify another currency or pricing unit that resolves these pairs; do not assume an undocumented custom unit. Verify the intended denomination and amount before adapting any payload; see [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]].

No direct contradiction was found with the existing create-contract or edit-commit summaries when this guide is treated as worked configuration. Those sources already describe hierarchy payer and statement behavior and accept all, none, or contract-ID child access. They do not resolve the guide's monetary examples, complete nested validation, relationship lifecycle, consolidation failure handling, or truncated alert statement.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-credits-and-commits]], [[metronome-invoicing]], [[metronome-alerts-and-notifications]], [[metronome-reporting-and-analytics]], [[metronome-currencies-and-custom-pricing-units]]
- Related sources: [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-api-reference-credits-and-commits-edit-a-commit]], [[source-metronome-integrations-invoice-integrations-stripe]], [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/billing-model-guides/model-hierarchical-customer-relationships-2026-07-13|2026-07-13 snapshot — hierarchy contracts, shared commits, consolidated invoicing, origin analysis, and limitations]]
