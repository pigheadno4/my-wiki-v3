---
title: "Adyen DCC transactions and fees reporting"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/dcc-transactions-and-fees"
raw_files:
  - "adyen/docs/reporting/dcc-transactions-and-fees/2026-09-15.md"
tags: [adyen, reporting, dynamic-currency-conversion, pos, settlement]
---

## Overview

This Adyen reporting guide (last-modified metadata 2026-09-15; captured 2026-09-15) shows where to identify point-of-sale Dynamic Currency Conversion (DCC) acceptance and associated **DCC markup** in two reports. It applies when DCC is enabled and DCC reporting is turned on. It is a field-routing guide, not a conversion-rate calculation, general processing-fee breakdown, proof of completed settlement, or bank receipt. See [[adyen-reporting]] and [[adyen]].

## Key takeaways

- The Customer Area DCC Overview dashboard is linked for a high-level POS acceptance/earnings view. Adyen warns that enabling DCC can affect automated reconciliation and directs merchants to their Account Manager or Support for more information before enabling it. This page does not give an enablement procedure or current eligibility rule. [Raw lines 19–28]
- With DCC reporting on, **Settlement details report** position 24 / column W has `DCC Markup (NC)`: DCC markup **in settlement currency**. A negative amount indicates a credit in the merchant's favor. This field is not identified here as a gross shopper-currency amount, FX rate, or all-in processing fee. [Raw lines 30–36]
- With DCC reporting on, **Received payment details report** position 44 / column AR has `DCC`, indicating whether DCC was used. Values described are `DCC accepted` (shopper accepted and completed in shopper currency), `DCC declined` (shopper refused and completed in merchant currency), and `DCC not offered` (shopper and merchant share a currency). The statuses describe DCC selection, not a separate proof of payment settlement or payout. [Raw lines 38–48]
- This short page states no report role, generation interval/time zone, transaction-date column, markup formula, conversion rate, or reconciliation total. Consult each underlying report's own schema and a bank statement when those facts matter.

## Detail locators

- DCC enablement context and reconciliation warning: raw lines 19–28. Settlement details markup column and sign/currency interpretation: raw lines 30–36. Received payment details DCC status column and values: raw lines 38–48.
- The links to the DCC dashboard, currency conversion and both report guides at raw lines 19–21 and 52–57 are navigation. Those pages own their own permissions, timing and full report fields.

## Related

- [[adyen-reporting]]
- [[adyen]]
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report]]
- [[source-adyen-docs-reporting-received-payment-details-report]]

## Raw Sources

- [[raw/adyen/docs/reporting/dcc-transactions-and-fees/2026-09-15|Adyen DCC transactions and fees, 2026-09-15 snapshot]]
