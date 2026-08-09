---
title: "Metronome ASC 606 Guide for Usage Companies"
type: source
date_ingested: 2026-08-05
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/reporting-insights/financial-reporting/asc-606-revenue-recognition.md"
raw_files:
  - "metronome/guides/reporting-insights/financial-reporting/asc-606-revenue-recognition-2026-07-13.md"
tags: [metronome, asc-606, revenue-recognition, usage-based-billing, financial-reporting, accounting-data]
---

## Overview

This guide explains ASC 606's five-step model and describes how Metronome's billing data, contract model, product tagging, usage records, ledgers, and exports can support a merchant's revenue-recognition workflow. It is informational product guidance rather than authoritative accounting advice: Metronome says it is not a revenue-recognition platform, does not make accounting determinations, and does not generate revenue journal entries.

## Key takeaways

- The guide organizes ASC 606 into identifying the customer contract, identifying performance obligations, determining the transaction price, allocating that price to the obligations, and recognizing revenue as obligations are satisfied.
- Metronome describes transaction and ledger histories with daily usage and service-delivery granularity, broken down by product, customer, commitment, and revenue category.
- Contract IDs, effective dates, version history, product and obligation tags, usage-to-charge relationships, and consistent identifiers are presented as inputs for downstream accounting and audit workflows.
- Metronome supplies charge-level and historical data that downstream ERP or revenue tools can use for standalone-selling-price analysis and allocation, but the guide says Metronome does not perform reallocations.
- Timestamped usage, billed-versus-earned export views, true-up links, and retained billing history can support recognition schedules, while the merchant remains responsible for contract interpretation, accounting policy, allocation, recognition timing, breakage, foreign-exchange treatment, and professional review.

## ASC 606 support model

### Contract identification

The guide maps contract identification to persistent contract IDs, contract start and end dates, amendment effective dates, total contract value, retained version history, contract hierarchy, and CRM or ERP integration hooks. These fields can support reconciliation and amendment tracking, but the merchant must decide whether related agreements should be combined, how modifications are accounted for, and how termination rights affect the enforceable contract period.

### Performance obligations

Products, rate cards, usage metrics, and obligation tags can map charges or usage events to obligation categories while retaining product-level detail for bundled offerings. The guide cautions that a Metronome SKU is not necessarily a distinct performance obligation and that the merchant must evaluate implementation services, support tiers, hybrid offerings, and other promises under its accounting policy.

### Transaction price

Metronome can retain fixed and variable pricing components, discounts, credits, raw usage, adjustments, currencies, and contract pricing structures. The source presents these as data inputs; it leaves estimates and constraints for variable consideration, the definition of total contract value, and functional-currency policy to the merchant.

### Allocation

Charge-level reporting, usage-to-obligation mapping, historical raw amounts, and stable identifiers can supply downstream allocation inputs. Metronome does not determine standalone selling prices, allocate the transaction price among performance obligations, or perform reallocations. Bundled discounts, commit attribution, rollovers, and possible material rights therefore require merchant-owned accounting analysis.

### Recognition timing

The guide describes timestamped usage events, billed-versus-earned export views, true-up linkage, and long-term data retention as inputs for recognition schedules. It discusses point-in-time and over-time recognition, cutoff, breakage, and differences between invoicing and revenue timing, but those treatments remain illustrative and contract-dependent rather than platform-generated accounting conclusions.

## Illustrative data mappings

The appendix maps on-demand usage, prepaid commitment drawdown and expiration, postpaid commitment drawdown and true-ups, overage, and free credits to invoice, line-item, balance, and ledger fields. Examples include `CONTRACT_USAGE`, `CONTRACT_SCHEDULED`, and `CONTRACT_TRUEUP` invoices; populated or null `line_items.commit_id`; prepaid and postpaid balance types; and expiration or true-up ledger entries.

These mappings are examples of report construction, not a complete accounting policy. The guide itself allows policy-dependent alternatives—for example, prepaid expiration may be recognized earlier under a breakage model—and says free credits may offset recognized revenue as contra-revenue. Invoice or ledger classification alone therefore does not establish the correct journal entry or recognition outcome.

## Documentation boundaries

Metronome characterizes its data as supporting ASC 606 workflows and audit-ready analysis, but the page expressly disclaims prescriptive guidance and assigns policy decisions to the merchant. Product-capability statements, example accounting treatments, and field mappings should be validated against current contracts, API and export schemas, downstream controls, and qualified accounting advice. The page does not establish auditor approval, complete journal-entry logic, close procedures, correction or restatement handling, or compliance merely from using Metronome data.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-reporting-and-analytics]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-invoicing]], [[metronome-credits-and-commits]], [[metronome-usage-based-billing]]
- Related source: [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition]]

## Raw Sources

- [[raw/metronome/guides/reporting-insights/financial-reporting/asc-606-revenue-recognition-2026-07-13|2026-07-13 snapshot - ASC 606 support model, illustrative accounting scenarios, data mappings, and responsibility boundaries]]
