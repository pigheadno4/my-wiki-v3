---
title: "Adyen Classic Platforms: reconcile fees"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/reconciliation-use-cases/understand-fees"
raw_files:
  - "adyen/docs/classic-platforms/reconciliation-use-cases/understand-fees/2026-09-15.md"
tags: [adyen, classic-platforms, reconciliation, fees]
---

## Overview

This Classic Adyen for Platforms fee-reconciliation guide (last modified 2021-07-23; captured 2026-09-15) explains how to reconcile fees debited from the **platform's liable account**. Adyen says it deducts fees from settlement and identifies complementary report grains: Settlement details for settled transactions, Payment accounting for transaction-related fees including unsettled items, Marketplace Payments accounting for platform account entries, and the monthly payment-processing invoice for period totals. The page directs new implementations to a different, newer integration guide; its Classic report formulas and account names should not be transplanted to the current balance-platform ledger. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The monthly invoice accounts for fees already deducted in the reports, may include rebates, and carries only remaining fee debits or rebate credits through settlement as `InvoiceDeduction` rows. Avoid adding all invoice fees again to already-deducted report fees.
- The guide offers three cross-checks for a matched report period: (1) Settlement details gross credits minus gross debits minus its `XASTransfer` net amount settled to platform accounts; (2) Settlement details commission, markup, scheme fees and interchange columns plus `Fee` and, if present, `InvoiceDeduction` rows; (3) Marketplace Payments accounting `Fee` plus `InvoiceDeduction` rows. Reports may use different generation periods/time zones, so align both before comparing.
- Its selected-row example computes **EUR 9.72** in fees: EUR 9.40 from transaction fee columns plus EUR 0.32 from a Settlement details `Fee` row. The Marketplace Payments accounting table records the same fee as a **−EUR 9.72** `Fee` debit, so compare the debit magnitude or apply consistent signs; the signed raw row is not literally equal to the positive total. The Payment accounting example traces EUR 0.32 processing fees across four EUR 0.08 rows, including a refused transaction; settled-only views would miss that item.
- Match Payment PSP/merchant references between the Marketplace Payments accounting and Settlement details reports to attribute settled payments and refunds, then use Payment accounting for remaining processing fees. The page shows selected rows and columns, so its example does not prove any particular platform's complete fee ledger or actual settlement.

## Detail locators

- Raw lines 19–33 define Classic scope, liable-account fee flow, report purposes and invoice adjustment.
- Raw lines 35–56 give period/time-zone checks and three total-fee formulas.
- Raw lines 58–98 give selected Marketplace Payments accounting and Settlement details rows, references and the EUR 9.72 calculation.
- Raw lines 100–114 trace EUR 0.32 in Payment accounting, including a refused transaction; lines 116–123 route to report references.

## Related

- [[adyen-classic-platforms]] — Classic platform and liable-account context.
- [[adyen]] — provider context.
- [[adyen-platforms]] — separate current Platforms model.
- [[adyen-index]] — provider navigation.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/reconciliation-use-cases/understand-fees/2026-09-15|Adyen Classic Platforms fee reconciliation, captured 2026-09-15]]
