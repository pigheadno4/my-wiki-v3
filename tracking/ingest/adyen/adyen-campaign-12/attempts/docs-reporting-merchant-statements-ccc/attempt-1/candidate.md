---
title: "Adyen Canada Code of Conduct merchant statements"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/merchant-statements-ccc"
raw_files:
  - "adyen/docs/reporting/merchant-statements-ccc/2026-09-15.md"
tags: [adyen, reporting, canada, merchant-statements, payment-fees]
---

## Overview

This [[adyen]] Canada Code of Conduct guide shows how to construct a merchant statement of aggregate payment fees and effective merchant discount rates from a Payment Accounting Report (PAR) or Interactive Payment Accounting Report (IPAR). Its stated transparency context is fees paid per Payment Card Network Operator (PCNO) in Canada; its worked aggregation groups payment costs first by **Psp Reference** and then calculates totals by **Payment Method**. The source describes a calculation workflow, not a separately generated statement whose row proves bank receipt. See [[adyen-reporting]] for the reporting route.

## Key takeaways

- The guide lists any Adyen integration type, a **Report service user** API credential role, Customer Area roles for column configuration (**Merchant admin**, **Merchant report**, **Merchant financial**, or **Merchant POS Report role**), and **Merchant report** for report generation and download. **Standard Webhook** subscription is conditional on using an automatically generated PAR rather than IPAR. [Raw: Requirements, lines 23–35]
- Configure and download PAR or IPAR for the chosen period at merchant level. The suggested input columns include **Psp Reference**, **Payment Method**, **Booking Date**, **Record Type**, **Settlement Currency**, **Payable (SC)**, **Commission (SC)**, **Markup (SC)**, **Scheme Fees (SC)**, **Interchange (SC)**, **Processing Fee Currency**, and **Processing Fee (FC)**. Here SC is settlement currency and FC is processing-fee currency; the fees should not be silently treated as one currency. Commission is split into markup, scheme fees, and interchange instead when the acquirer provides interchange-level information. [Raw: Configure report columns, lines 58–86; Download IPAR or PAR, lines 87–94]
- Add **Main Amount (SC)** as **Payable (SC) + Commission (SC) + Scheme Fees (SC) + Interchange (SC) + Markup (SC)**. The page describes this derived value as gross transaction amount in settlement currency. Build a pivot by **Psp Reference** with **Payment Method** as the column dimension, then calculate method-level totals, **Total Cost of Payment** as interchange plus scheme fees plus markup plus commission plus processing fees, and **Effective Merchant Discount Rate** as total cost divided by Main Amount total. These are period-level calculated outputs, not native PAR/IPAR row values. [Raw: How it works, lines 37–56; Main Amount, lines 96–101; Create pivot table, lines 137–154; Determine aggregate transaction costs, lines 156–174]
- For multiple currencies, the guide optionally uses an **Exchange rate** report for dates matching each PAR/IPAR **Booking Date**. Convert SC fields and **Processing Fee (FC)** to base-currency fields; use **Exchange Rate** for payments-only integrations and **Exchange Rate (Platform Settlement)** for platform/marketplace integrations. The single-currency formula table retains **Processing Fee (FC)** beside SC totals, so verify its fee currency before combining values. [Raw: Exchange rate report, lines 103–112; Convert to Base Currency, lines 114–135; pivot and formulas, lines 137–174]
- This is a 2026-09-15 webpage snapshot. It supplies a Canada-focused computation method; it does not certify a merchant's legal compliance, report completeness, current role eligibility, accounting finality, or arrival of a payout at a bank. Its formula should be applied to the relevant account, date period, and currency values rather than an unverified sample.

## Detail locators

- Canada Code and PCNO purpose, and effective merchant discount rate definition: opening, lines 15–21.
- API, Customer Area, and conditional webhook requirements: `Requirements`, lines 23–35.
- PAR/IPAR column configuration and exact field meanings: `1. Configure report columns`, lines 58–86.
- Merchant-level date-period download: `2. Download IPAR or PAR`, lines 87–94.
- Derived Main Amount formula: `3. Create new Main Amount column`, lines 96–101.
- Booking-Date exchange-rate matching and integration-specific rate columns: `4. (Optional) Download an Exchange rate report` and `5. (Optional) Convert Settlement Currency to Base Currency`, lines 103–135.
- PSP-reference pivot, method totals, total cost and effective rate formulas: `6. Create pivot table to aggregate costs` and `7. Determine aggregate transaction costs`, lines 137–174.

## Related

- [[adyen]] — provider page.
- [[adyen-reporting]] — provider reporting concept.
- [[source-adyen-docs-reporting-invoice-reconciliation-payment-accounting-report]] — PAR/IPAR source route for underlying report fields and account/date qualifications.

## Raw Sources

- [[raw/adyen/docs/reporting/merchant-statements-ccc/2026-09-15|Adyen Canada Code of Conduct merchant statements (2026-09-15)]]
