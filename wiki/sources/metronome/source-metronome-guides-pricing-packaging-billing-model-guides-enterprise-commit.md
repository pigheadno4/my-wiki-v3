---
title: "Launch an enterprise commit model"
type: source
date_ingested: 2026-07-28
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/enterprise-commit"
original_format: webpage
raw_files:
  - "metronome/guides/pricing-packaging/billing-model-guides/enterprise-commit-2026-07-13.md"
tags: [metronome, enterprise-commit, contracts, usage-based-billing]
---

## Overview

This guide describes an enterprise commitment lifecycle from product and rate-card design through customer provisioning, contract creation, mid-contract changes, renewal, and finance workflows. Its example combines a three-year prepaid commitment, scheduled access, installment invoicing, tag-scoped discounts, rollover, and a separately scheduled support charge.

## Key takeaways

- Enterprise terms can combine prepaid or postpaid commitments, negotiated discounts, one-time charges, and renewals.
- A prepaid commitment can use separate access and invoice schedules; the example makes $500,000 available over three years while invoicing two $250,000 installments.
- Product tags let rate overrides target groups of products, and fixed products represent one-time charges and upfront commitment payments.
- Contract edits add terms to an existing contract; transitions start a new contract and retain the relationship needed for renewal logic such as rollover.
- Custom fields can connect Metronome customers, contracts, products, and invoice lines to CRM and ERP records.

## Details

### Reusable billing building blocks

Products and rate cards remain common building blocks even when enterprise contracts are customized. The guide recommends organizing products with tags so negotiated overrides can target groups of similarly priced, discounted, or packaged products. Every invoice charge maps to a product, including one-time charges and upfront payments for prepaid commitments; those charges use fixed products.

Custom fields can preserve external identifiers such as CRM account and opportunity IDs or ERP SKU IDs. These mappings support reconciliation, audit trails, and revenue-recognition routing.

### Example contract

The InfraX example defines a $500,000 prepaid commitment with annual access allocations of $50,000, $200,000, and $250,000. Its invoice schedule charges $250,000 at the start of year 1 and another $250,000 at the start of year 3. A `rollover_fraction` of `0.25` permits limited renewal rollover, while tag-scoped multipliers discount `storage` products by 10% in year 1 and 20% afterward. A separate scheduled charge bills $5,000 for professional support in month 3.

### Customer and contract lifecycle

The guide recommends customer-facing cost exploration and spend controls, and describes using Salesforce-connected usage and balance data to support negotiations. For commercial changes, edits add terms without replacing the contract. Transitions start a new contract, preserve the relationship to the original, and can apply renewal transition logic such as rolling over unused commitments or credits.

> [!warning] Documentation inconsistencies
> The create-contract example uses `product` inside a commit, while the dedicated create-contract API reference documents `product_id`. The upsell prose also describes a new $300,000 commitment, but its example request uses `add_scheduled_charges` rather than adding a commit. Verify the current API schema and intended accounting treatment before implementing either example.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-usage-based-billing]]
- API boundary: [[source-metronome-api-reference-contracts-create-a-contract]]
- Targeted commit mutation: [[source-metronome-api-reference-credits-and-commits-edit-a-commit]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/billing-model-guides/enterprise-commit-2026-07-13|2026-07-13 snapshot — enterprise commitment lifecycle and examples]]
