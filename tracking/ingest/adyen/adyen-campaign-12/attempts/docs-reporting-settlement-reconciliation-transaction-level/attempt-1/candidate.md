---
title: "Adyen transaction-level settlement reconciliation"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level"
raw_files:
  - "adyen/docs/reporting/settlement-reconciliation/transaction-level/2026-09-15.md"
tags: [adyen, reporting, settlement, reconciliation, payout-batch]
---

## Overview

Adyen's transaction-level reconciliation guide explains how to compare transaction costs and the payout amount **within a single payout batch**. The primary input is the merchant-account Settlement details report; an External settlement detail report is conditional on an external-acquirer arrangement. This dated guide provides a report-matching method, not proof that a bank received the payout.

## Key takeaways

- Adyen recommends reconciling at merchant-account level because Settlement details reports are generated there. With external acquirers, the External settlement detail report is company-account generated; select entries for the matching merchant account and merge them, or reconcile an external-acquirer report separately if using that instead. Brazilian card installments need the separate installment-reconciliation instructions.
- Each report line is an **entry**, and one transaction may have multiple entries. Use Adyen's Psp Reference and the merchant's Merchant Reference to find and match transaction records; do not count entries as unique payments.
- For credits, the guide uses Gross Credit for customer-paid gross amount, Commission/Markup/Scheme Fees/Interchange Fees for costs, and Net Credit after costs. For debits such as refunds, chargebacks and fees, inspect Gross Debit and Net Debit with Type and Modification Reference. Keep Gross Currency and Net Currency distinct; sample EUR values illustrate the method, not a guarantee that every report row uses one currency.
- Add net credits and subtract net debits to compare with the batch payout. A `MerchantPayout` entry has the payout amount in **Net Debit**; its Modification Reference includes a reference, batch number and merchant account, and the example says the reference can be used in the merchant's accounting system. This report row and accounting reference do not establish bank-statement arrival or final bank reconciliation.
- Investigate differences caused by weekend sales entering the following week's batch, payments not yet settled, capture failure or an uncancelled payment/partial payment. The guide routes to open balances in monthly/daily finance reporting, aggregate settled amounts versus sales, received-payment and interactive-accounting reports, and Customer Area status/logs. A payment missing from `Settled` requires investigation rather than an assumed payout.
- **Source wording conflict:** the debit prose calls Net Debit gross debit *minus* additional costs, but its chargeback example adds EUR 7.50 markup to EUR 120 gross debit and shows EUR 127.50 Net Debit. Preserve the report's Type, fee fields and signed columns when reconciling rather than applying the prose as a universal formula.

## Detail locators

- Opening through `## Step 1 (Optional)` — single-batch scope, Settlement details and conditional external-acquirer inputs, merchant/company report scope and Brazil installment exception.
- `## Step 2: Find transactions` — entry versus transaction grain and PSP/merchant references.
- `## Step 3` / `## Step 4` — gross/net credit and debit fields, fee columns, Gross/Net Currency examples, and the debit prose/example conflict.
- `## Step 5` — `MerchantPayout`, Net Debit batch amount, Modification Reference and example batch number; these are report fields rather than a bank-statement match.
- `## Step 6 (Optional)` — weekend-batch timing, unsettled-payment causes and four investigation routes.

## Related

- Company: [[adyen]]
- Reporting concept: [[adyen-reporting]]

## Raw Sources

- [[raw/adyen/docs/reporting/settlement-reconciliation/transaction-level/2026-09-15|2026-09-15 transaction-level reconciliation guide]]
