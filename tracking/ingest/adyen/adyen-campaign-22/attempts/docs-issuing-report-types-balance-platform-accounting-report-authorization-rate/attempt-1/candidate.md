---
title: "Adyen Issuing Accounting Report authorization-rate context"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/report-types/balance-platform-accounting-report/authorization-rate"
raw_files:
  - "adyen/docs/issuing/report-types/balance-platform-accounting-report/authorization-rate/2026-09-15.md"
tags: [adyen, issuing, accounting-report, authorization, troubleshooting]
---

## Overview

This 2026-09-15-captured Issuing-path page names acquirer-sent payment-context fields in the Balance Platform Accounting Report that may help investigate card-payment refusals and authorization rates. It is a field-navigation note, not a rate calculation, diagnostic decision tree or demonstrated authorization improvement. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The page frames payment context as parameters sent by the acquirer. It suggests checking those report fields when investigating refusals; it does not define an authorization-rate numerator, denominator, cohort, period, benchmark or causal remedy (raw lines 17–21).
- The listed fields are payment-instrument type and ID to identify card/cardholder, `Entrymode` as reported by the acquirer (for example chip or manual), `Shopper interaction` (POS or Ecommerce), merchant category code for the counterparty industry, and counterparty name/address/city/country (raw lines 23–27). The page points to Customer Area for additional payment-instrument information, without stating access roles or a complete lookup procedure (raw line 23).

## Detail locators

- Purpose and acquirer-origin qualification: raw lines 15–21. Payment-context field list and examples: raw lines 23–27.

## Related

- [[adyen-issuing]] — issued-card authorization and source route.
- [[source-adyen-docs-issuing-report-types-balance-platform-accounting-report]] — parent report scope and columns.
- [[adyen-reporting]] — broader report context.

## Raw Sources

- [[raw/adyen/docs/issuing/report-types/balance-platform-accounting-report/authorization-rate/2026-09-15|Authorization rates and troubleshooting, captured 2026-09-15]]
