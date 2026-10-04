---
title: "Braintree Adyen Reconciliation"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/adyen/reconciliation"
raw_files:
  - "braintree/articles/adyen/reconciliation-2026-09-16.md"
tags: [braintree, adyen, reconciliation, settlement, reporting]
---

## Overview

This collected Braintree article documents the Settlement Details Report for merchants whose transactions are processed with Adyen. It presents the report as the primary reconciliation tool for aligning payout-level report data with bank-deposit records and provides transaction, fee, correction and reference fields for investigation.

The snapshot is Braintree-hosted processor documentation, not independent Adyen authority and not the C33 PayPal Orchestration Adyen integration guide. It does not prove that an individual payout or bank deposit completed, or establish current regional, account or pricing eligibility.

## Key takeaways

- Braintree says the Settlement Details Report is generated upon payout and is available only to users with the Create, Run, and Download Reports permission. The documented Control Panel path is **Reports** → **Settlement Details Report** → **Run Report**.
- The report lists the transactions included in a bank deposit and gross and net settlement amounts for captures, refunds and, when present, chargebacks. It also identifies fee totals, deposit corrections and the reported bank-transfer amount. These report fields support reconciliation; they are not independent proof that funds arrived.
- The **Merchant Payout** row reports the amount Adyen sent, an Adyen reference intended to appear on the bank statement, and a **Net Debit** amount that the article says should match the bank deposit. The **Modification Reference** can align batches with account deposits.
- Transaction details are merchant-account-specific. The report's **Merchant Account** field identifies the MID used to process a transaction, and merchants processing through more than one MID receive a separate report for each MID. **Psp Reference** is Adyen's transaction identifier, while **Merchant Reference** is the Braintree transaction ID used for Control Panel search.
- Adjustments can appear as **Deposit Correction**, **Invoice Deduction** or **Balancetransfer** lines. The article says reserve movements or outstanding fees can change the reported deposit amount, monthly invoice corrections can be debits or credits, and transfers between settlement batches can alter the payout. Its €0,10-per-transaction, 1000-transaction-minimum scenario is expressly an example conditioned on agreed pricing, not a regional or universal fee schedule.
- The transaction-detail section distinguishes settled, refunded and chargeback rows and defines gross, net, currency, exchange-rate, commission and payment-method-variant fields. Use the raw locators for the exact row-by-row treatment rather than applying one amount rule to every transaction type.

> [!warning] Report and deposit boundary
> The page documents reconciliation fields in a generated report. A reported payout amount, reference or expected bank-deposit match does not by itself establish that a particular payout settled or that funds reached the merchant's bank account.

## Detail locators

- Report purpose, payout-generation condition, required role permission and Control Panel run steps: `# Reconciliation`, raw lines 16-24.
- Included transactions, gross/net settlement amounts, fees, corrections and reported bank-transfer amount: `# Reconciliation`, raw line 25.
- Payout amount, bank-statement reference and deposit-matching fields: `## Merchant Payout`, raw lines 30-34.
- Fee period, total and currency: `## Transaction Fees`, raw lines 37-39.
- Reserve movements and the conditional monthly-minimum fee example: `## Corrections > ### Deposit Correction`, raw lines 42-49.
- Tier-pricing invoice correction and debit/credit direction: `## Corrections > ### Invoice Deduction`, raw lines 52-54.
- Transfers between settlement batches and the displayed support route: `## Corrections > ### Balance Transfer`, raw lines 57-59.
- Transaction types and field-by-field amount, currency, reference, commission and payment-method definitions: `## Transaction details`, raw lines 62-136.
- Per-MID report separation and the Adyen versus Braintree transaction-reference distinction: `## Transaction details > #### Merchant Account` through `#### Merchant Reference`, raw lines 74-86.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]
- Supporting concept: [[braintree-control-panel]]
- Distinct C33 processor-connection guide: [[source-braintree-orchestration-adyen]]

## Raw Sources

- [[raw/braintree/articles/adyen/reconciliation-2026-09-16|Braintree Adyen reconciliation article]] - complete collected page covering Settlement Details Report access, payout and adjustment rows, per-MID reporting, transaction references and detailed amount fields
