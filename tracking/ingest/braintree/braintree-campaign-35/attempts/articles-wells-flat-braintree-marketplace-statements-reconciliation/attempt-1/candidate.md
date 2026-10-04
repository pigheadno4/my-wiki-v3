---
title: "Braintree Marketplace Statements and Reconciliation"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-flat/braintree-marketplace-statements-reconciliation"
raw_files:
  - "braintree/articles/wells-flat/braintree-marketplace-statements-reconciliation-2026-09-16.md"
tags: [braintree, marketplace, wells-flat, statements, reconciliation]
---

## Overview

This collected Braintree-hosted Wells Flat article documents statement access and reconciliation for Braintree Marketplace master and sub-merchants. It is expressly distinct from the standard statements guide for merchants not using Braintree Marketplace.

The snapshot is not independent bank-policy evidence and does not establish current product availability or regional, account, processor, or pricing eligibility. Its Wells Flat Marketplace fee treatment must not be transferred to IC+ pricing, other processor arrangements, or ordinary merchant statements.

## Key takeaways

- Marketplace statements are available through **Reports** → **Statements** in the Control Panel. Access requires the user's role to have **View Statements** permission.
- The statement can include a summary plus master-merchant disbursement, escrow when applicable, refund, chargeback and sub-merchant-disbursement details. Its Pricing Schedule identifies the merchant account's discount rate, per-transaction fee and chargeback fee; use the raw locators for the row inventory and pricing detail.
- For master-merchant reconciliation, the article directs merchants to compare the statement's Master Merchant Disbursement Details with bank deposits. It says the disbursement date is when Braintree sent funds to the bank, funds should appear within 1–2 business days, and **Total Disbursed** should match the bank-statement deposit. These are provider statements for reconciliation, not proof that a particular deposit arrived.
- The article says an individual sub-merchant cannot reconcile from the Marketplace statement's aggregate sub-merchant revenue alone. It instead routes multiple sub-merchants through a disbursed-date transaction search and a specific sub-merchant through the Disbursement Summary. The latter requires **Create, Run, and Download Reports** permission.
- In this documented Marketplace model, sub-merchants do not pay Braintree transaction fees and receive gross sales less master-merchant-designated service fees. For multiple sub-merchants, the article uses **Amount Submitted For Settlement** minus **Service Fee**; for one sub-merchant, it says the Disbursement Summary omits service fees, which must be added to the spreadsheet and subtracted from **Total Amount**.
- For more granular master-merchant reconciliation, the article describes calculating transaction fees from the statement's Pricing Schedule, rounding down under the linked Wells Flat pricing guidance, and subtracting calculated Braintree fees from the service fee. The documented Dashboard may help assess processing activity but must not be used for reconciliation.

> [!warning] Scope and funding boundary
> Use this page only for the captured Wells Flat Braintree Marketplace statement model. It does not describe ordinary merchant statements, establish IC+ or other processor fee treatment, provide independent current bank policy, or prove an individual bank deposit.

## Detail locators

- Marketplace-only statement distinction and standard-statement route: introductory **NOTE**, raw lines 17–18.
- Statement access path and **View Statements** permission: `## Statements`, raw lines 23–34.
- Statement section inventory: `## Statements`, raw lines 38–50.
- Master Merchant Summary, Braintree Fee Details rows and Pricing Schedule: `### Summary page`, raw lines 53–75.
- Primary Marketplace reconciliation routes and Dashboard prohibition: `## Reconciliation`, raw lines 78–85.
- Master Merchant Disbursement Details, refund/chargeback/fee-credit treatment, disbursement-date timing and bank-statement comparison: `### Master merchant reconciliation`, raw lines 88–92.
- Aggregate statement limit and Marketplace sub-merchant fee treatment: `### Sub-merchant reconciliation`, raw lines 95–100.
- Multi-sub-merchant disbursed-date search, CSV workflow and per-transaction service-fee calculation: `#### For multiple sub-merchants`, raw lines 103–119.
- Single-sub-merchant report permission, report workflow and omitted-service-fee calculation: `#### For a specific sub-merchant`, raw lines 122–136.
- Transaction-level fee workflow, Wells Flat Pricing Schedule and rounding route: `### Calculating fees on a transaction level`, raw lines 139–160.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-marketplace]]
- Supporting concept: [[payment-reconciliation-reporting]]

## Raw Sources

- [[raw/braintree/articles/wells-flat/braintree-marketplace-statements-reconciliation-2026-09-16|Braintree Marketplace Statements and Reconciliation]] - complete collected Braintree Wells Flat Marketplace article covering statement access, master- and sub-merchant reconciliation, fee calculations and the Dashboard exclusion
