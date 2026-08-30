---
title: "ASC 606 Revenue Recognition Guide for Usage Companies"
type: source
date_ingested: 2026-08-30
canonical_url: "https://docs.metronome.com/guides/reporting-insights/financial-reporting/asc-606-revenue-recognition"
original_format: webpage
raw_files:
  - "metronome/guides/reporting-insights/financial-reporting/asc-606-revenue-recognition-2026-07-13.md"
tags: [metronome, asc-606, revenue-recognition, financial-reporting, contracts, data-export]
---

## Overview

This guide explains the five-step ASC 606 model and illustrates how Metronome contracts, products, pricing, usage, invoices, balances, ledgers, exports, and integration identifiers can supply data for a merchant-owned revenue-recognition process. It is a product and data-model guide, not accounting authority: Metronome says it is not a revenue-recognition platform, does not create journal entries or make accounting determinations, and leaves contract-specific policy and compliance to the customer and qualified accounting professionals.

## Query-critical facts

- The page organizes ASC 606 into contract identification, performance-obligation identification, transaction-price determination, allocation based on standalone selling price, and recognition when or as obligations are satisfied. For each step it separates the accounting idea, customer challenges, Metronome support, and common issues.
- For contract identification, the guide routes usage, charges, and credits through a persistent contract identity and describes contract dates, amendments, version history, hierarchy or linkage, and CRM/ERP identifiers as reconciliation inputs. Metronome can capture changes, but the customer decides whether agreements combine, how modifications are accounted for, what period is enforceable, and how free periods affect the contract.
- Products, rate cards, tags, custom fields, and charge-level exports provide SKU and obligation granularity. The customer remains responsible for deciding which promises are distinct and mapping them correctly; a Metronome SKU is not automatically an ASC 606 performance obligation.
- Fixed and variable fees, discounts, credits, usage, pricing changes, and original-currency data can support transaction-price analysis. Metronome does not determine variable-consideration constraints or foreign-exchange policy, and its granular historical data supports downstream standalone-selling-price analysis and allocation rather than performing allocation or reallocation.
- Timestamped usage, service-period fields, invoice and line-item identifiers, commit links, and balance-ledger entries can support period-specific billed-versus-earned reporting, true-up attribution, breakage analysis, and external recognition schedules. The guide's examples cover on-demand usage, prepaid purchase and drawdown, expiration, postpaid drawdown and true-up, overage, and free credits; their amounts and accounting treatments remain illustrative rather than policy.
- The page describes APIs and Data Export as inputs to revenue subledgers, ERPs, warehouses, CSV reports, and reconciliation with systems such as Salesforce and Stripe. Claims such as full history, immutable audit trail, real-time processing, schema-stable exports, long-term retention, and audit-ready reporting are source-scoped product statements, not defined completeness, freshness, retention, exactly-once delivery, close-control, or auditor-approval guarantees. Dedicated export, API, contract-history, and reconciliation sources remain authoritative for those operational details.

## Material boundaries and tensions

- The disclaimer controls every accounting example: contract combination, modification treatment, performance obligations, transaction price, variable consideration, SSP allocation, recognition timing, breakage, foreign exchange, and material rights depend on the customer's contracts and policies. Metronome supplies data and workflow support but does not make those determinations or generate revenue journal entries.
- The guide says revenue is recognized when or as performance obligations are satisfied and explicitly warns that invoice timing and recognition often differ. Its appendix nevertheless labels on-demand and overage revenue as recognized upon invoicing and postpaid true-up as recognized when the invoice is finalized. Preserve these as illustrative, source-specific reporting treatments; invoice issuance, finalization, usage, drawdown, expiration, or true-up is not by itself proof of the merchant's ASC 606 conclusion.
- This page links to the existing revenue-data-model and CloudNet example guides but does not resolve their documented postpaid-ledger ambiguity, reused identifiers, schema-label conflicts, arithmetic conflicts, or category conflicts. Do not use this higher-level guide to silently repair those examples or to override current Data Export table grain, freshness, duplication, snapshot, or reconciliation boundaries.

## Raw-detail coverage map

Use the raw page for the complete data-model principles; all five ASC 606 sections; contract-combination, modification, opt-out, free-period, obligation, setup-fee, support-tier, variable-consideration, FX, SSP, commit-attribution, material-right, timing, cutoff, breakage, and upfront-invoice examples; every linked Metronome documentation route; the seven appendix scenarios and example amounts; invoice, line-item, balance, and ledger field mappings; revenue-category and status mappings; and the complete product, pricing, contract, reporting, reconciliation, and account-hierarchy capability lists. Consult dedicated accounting authority for ASC 606 conclusions and dedicated Metronome API, Data Export, contract-history, invoice, credit/commit, integration, and reconciliation sources for operational schemas and guarantees.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-reporting-and-analytics]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]]
- Supporting concepts: [[metronome-invoicing]], [[metronome-credits-and-commits]], [[payment-reconciliation-reporting]]
- Related sources: [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition]], [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition-examples]], [[source-metronome-guides-reporting-insights-financial-reporting-reconcile-data]], [[source-metronome-guides-reporting-insights-data-export-overview]], [[source-metronome-guides-reporting-insights-data-export-database-reference]]

## Raw Sources

- [[raw/metronome/guides/reporting-insights/financial-reporting/asc-606-revenue-recognition-2026-07-13|2026-07-13 snapshot - ASC 606 five-step mapping, Metronome data and reporting support, worked examples, accounting disclaimer, and reconciliation boundaries]]
