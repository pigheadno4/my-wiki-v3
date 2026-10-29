---
title: "Adyen Online banking Czech Republic Android router"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-czech-republic/android"
raw_files:
  - "adyen/docs/payment-methods/online-banking-czech-republic/android/2026-09-15.md"
tags: [adyen, online-banking-czech-republic, android, integration-router]
---

## Overview

This 2026-09-15-captured Adyen Android page is a short integration router for Online banking Czech Republic. It links method-specific Drop-in and Components child guides and the four main Android Sessions/Advanced guides. It does not itself give a request, SDK version, redirect sequence, method eligibility, or payment outcome. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Android UI choices:** The page calls Drop-in an all-in-one UI route and links a Components route whose label says `OnlineBankingCZComponent` handles the redirect to Online banking Czech Republic. The label is navigation, not a verified action contract or proof that a bank redirect completed. Read the child Component guide for its implementation behavior. [Raw: lines 19–27]
- **Base integration first:** It instructs readers to create the main integration before adding the method and links Android Drop-in and Components for both Sessions and Advanced server-side flows. This chooser does not select one flow or supply flow-specific fields or return handling. [Raw: lines 29–36]
- **Method overview boundary:** The separately approved [[source-adyen-docs-payment-methods-online-banking-czech-republic]] overview supplies CZ/CZK, bank-selection/redirect and method capability context. Those facts belong to the overview; this Android page only routes to implementation guides and cannot establish current merchant availability. [Raw: lines 15–36]

## Detail locators

- Android Drop-in and Components child links: pinned raw lines 19–27.
- Main-integration instruction and four base guide links: pinned raw lines 29–36.

## Related

- [[adyen-online-payments]] — provider integration and method routes.
- [[source-adyen-docs-payment-methods-online-banking-czech-republic]] — approved CZ/CZK bank-redirect method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-czech-republic/android/2026-09-15|Online banking Czech Republic Android router, captured 2026-09-15]]
