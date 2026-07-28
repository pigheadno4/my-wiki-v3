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
This Metronome guide describes launching an enterprise commit model, from provisioning a customer and contract through upsells, renewals, customer transparency, and finance workflows. Its example models a three-year prepaid commitment with scheduled access, installment invoicing, tag-based discounts, rollover, and a scheduled professional-support charge.

## Key takeaways
- Metronome represents enterprise terms with commitments, contract rate overrides, scheduled charges, and custom fields that can connect CRM and ERP records.
- In the example, a prepaid commitment has separate access and invoice schedules, a 25% rollover fraction, and discount multipliers scoped to product tags.
- Contract edits add terms to an existing contract; contract transitions start a new contract and can apply renewal transition logic.

## Details
Products and rate cards remain common building blocks even when enterprise contracts are customized. The guide recommends grouping products with tags so rate overrides can discount a set of similarly priced, discounted, or packaged products rather than enumerating individual product IDs.

For the InfraX example, the contract request creates a prepaid commitment with annual access allocations of $50,000, $200,000, and $250,000, while invoicing $250,000 at the beginning of year 1 and year 3. It sets `rollover_fraction` to 0.25, applies a 0.9 multiplier to `storage` products in year 1 and a 0.8 multiplier afterward, and schedules a $5,000 charge in month 3.

The guide also describes customer-facing cost exploration and spend controls, Salesforce-connected sales insights, and finance workflows. Custom fields can retain external identifiers for reconciliation, and product custom fields can carry SKU IDs for revenue-recognition mapping.

## Related
- Coordinator audit: determine whether existing Metronome company or concept pages should be updated before adding cross-links.

## Raw Sources
- [[raw/metronome/guides/pricing-packaging/billing-model-guides/enterprise-commit-2026-07-13|enterprise-commit-2026-07-13]] — verbatim Metronome guide snapshot.
