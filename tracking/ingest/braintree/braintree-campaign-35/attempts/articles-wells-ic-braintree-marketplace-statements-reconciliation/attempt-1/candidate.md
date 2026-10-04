---
title: "IC+ Braintree Marketplace Statements and Reconciliation"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-ic/braintree-marketplace-statements-reconciliation"
raw_files:
  - "braintree/articles/wells-ic/braintree-marketplace-statements-reconciliation-2026-09-16.md"
tags: [braintree, marketplace, ic-plus, statements, reconciliation]
---

## Overview

This collected Braintree article documents statement interpretation and reconciliation specifically for Braintree Marketplace under the IC+ pricing model. It distinguishes master-merchant statement reconciliation from the tools used to help individual sub-merchants reconcile; merchants outside Braintree Marketplace are directed to a different statement route.

The snapshot is Braintree-hosted Marketplace documentation, not independent Wells Fargo bank-policy authority. It does not establish current regional, account or pricing eligibility, and its IC+ fee treatment should not be transferred to a flat-pricing statement route.

## Key takeaways

- Statements are accessed in the Control Panel under **Reports** → **Statements**. A user who cannot see **Reports** needs the **View Statements** role permission.
- Under the documented IC+ model, the summary separates card-association interchange or pass-through fees from Braintree fees. Interchange fees are billed by settlement timing, Braintree fees by disbursement timing, and the article says both are debited on the second Tuesday of the following month as two withdrawals.
- For master merchants, the statement's Master Merchant Disbursement Details combines gross service fees with refunds, chargebacks, fee credits and Braintree fees to determine **Total Disbursed**. The article says that total should match the bank-statement deposit and that funds should appear within 1–2 business days of the disbursement date; these are reconciliation expectations, not proof that a deposit arrived.
- The Dashboard is expressly excluded as a reconciliation tool. For sub-merchants, the statement aggregates all sub-merchants, so the article instead routes multiple-sub-merchant work to a disbursed-date transaction export and a specific sub-merchant to the Disbursement Summary. The latter requires **Create, Run, and Download Reports** permission.
- The article says sub-merchants do not pay Braintree transaction fees and receive gross sales less designated service fees. Its transaction-export and Disbursement Summary calculations therefore account for service fees when matching a sub-merchant's reported deposit.

> [!warning] Marketplace and pricing scope
> These instructions are for the captured IC+ Braintree Marketplace statement route. The page says non-Marketplace statements look different; do not generalize its fee structure, statement layout or reconciliation procedure to ordinary merchant or flat-pricing accounts.

> [!warning] Report and deposit boundary
> A statement total, expected 1–2-business-day bank appearance or calculated sub-merchant amount supports reconciliation but does not independently prove that funds reached a bank account. The snapshot also does not establish current regional or account eligibility.

## Detail locators

- Marketplace-only scope and route to different non-Marketplace statements: opening note, raw lines 17–18.
- Control Panel access and **View Statements** permission: `## Statements`, raw lines 23–34.
- Statement-section inventory, including master-merchant and sub-merchant disbursements, escrow, refunds and chargebacks: `## Statements`, raw lines 38–50.
- Master Merchant Summary purpose: `### Summary page > #### Master Merchant Summary`, raw lines 53–60.
- IC+ interchange-versus-Braintree fee categories, billing events and debit timing: `#### Fee Details`, raw lines 63–67.
- Braintree-fee rows, pass-through report access and pricing-schedule fields: `##### Braintree Fee Details` through `#### Pricing Schedule`, raw lines 70–95.
- Master-merchant reconciliation, Dashboard exclusion, disbursement calculation and bank timing: `## Reconciliation` through `### Master merchant reconciliation`, raw lines 98–112.
- Sub-merchant fee treatment and disbursed-date transaction-export procedure: `### Sub-merchant reconciliation` through `#### For multiple sub-merchants`, raw lines 115–139.
- Disbursement Summary permission, run procedure and service-fee adjustment: `#### For a specific sub-merchant`, raw lines 142–156.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-marketplace]]

## Raw Sources

- [[raw/braintree/articles/wells-ic/braintree-marketplace-statements-reconciliation-2026-09-16|IC+ Braintree Marketplace statements and reconciliation]] - complete collected snapshot for Marketplace statement access, IC+ fee presentation, and master/sub-merchant reconciliation routes
