---
title: "Adyen Online banking Poland Android router"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-poland/android"
raw_files:
  - "adyen/docs/payment-methods/online-banking-poland/android/2026-09-15.md"
tags: [adyen, online-banking-poland, android, integration-router]
---

## Overview

This 2026-09-15-captured Adyen page is a short Android integration router for Online banking Poland. It links method-specific Drop-in and Components child guides and the four main Android Sessions/Advanced guides. It does not itself specify a payment request, version, redirect sequence, method eligibility, or transaction outcome. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Android UI choices:** The page describes Drop-in as an all-in-one UI route and says the Components child uses `OnlineBankingPLComponent` to handle redirect to Online banking Poland. This is link text, not a verified action contract or evidence that bank payment completed; read the child guide for behavior. [Raw: lines 19–27]
- **Main integration first:** It instructs readers to follow the main integration guides before adding the method, then links Android Drop-in and Components for both Sessions and Advanced flows. This chooser does not select a flow or supply method-specific fields or result handling. [Raw: lines 29–36]
- **Method context boundary:** The separately approved [[source-adyen-docs-payment-methods-online-banking-poland]] overview supplies P24 partner, PL/PLN, bank selection and redirect context. Those facts belong to the overview, not this Android navigation page, and do not prove current merchant availability. [Raw: lines 15–36]

## Detail locators

- Method-specific Android Drop-in and Components links: pinned raw lines 19–27.
- Main-integration prerequisite and four base guide links: pinned raw lines 29–36.

## Related

- [[adyen-online-payments]] — provider integration and method routes.
- [[source-adyen-docs-payment-methods-online-banking-poland]] — approved P24/PL/PLN method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-poland/android/2026-09-15|Online banking Poland Android router, captured 2026-09-15]]
