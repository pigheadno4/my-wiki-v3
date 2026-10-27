---
title: "Pre-Authorized Debit Canada for Web | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pad/web"
raw_files:
  - "adyen/docs/payment-methods/pad/web/2026-09-15.md"
tags: [adyen, pad, canada, web, drop-in, components, integration-chooser]
---

## Overview

This 2026-09-15 page is a Pre-Authorized Debit Canada (PADs Canada) **Web integration chooser**. It routes merchants to Web Drop-in or Web Components child guides and to the matching main Sessions or Advanced integration guide. It provides navigation, not payment-request fields, mandate instructions or payment-outcome handling (raw lines 15–36).

## Key takeaways

- Choose [[source-adyen-docs-payment-methods-pad-web-drop-in|Web Drop-in]] for Adyen's all-in-one UI or [[source-adyen-docs-payment-methods-pad-web-component|Web Components]] for the `PreAuthorizedDebitCanada` route. These are different UI guides; this page does not say they share configuration or request fields (raw lines 19–27).
- Build the main integration before adding PADs Canada. The page links Web Drop-in and Web Components for both Sessions and Advanced server-side flows, so implementation requirements belong to the selected child plus base guide (raw lines 29–36).
- The related [[source-adyen-docs-payment-methods-pad|PAD overview]] requires a merchant-held shopper PAD agreement before any debit, a Canadian financial-institution account for acceptance, and warns that bank authorization is not real-time and PAD chargebacks cannot be defended. These method-level claims come from the overview, not this chooser; the links do not prove current merchant activation, mandate validity or successful debit (overview raw lines 23–31, 33–60; this raw lines 15–36).

## Detail locators

- Web Drop-in and `PreAuthorizedDebitCanada` Components route choices: raw lines 19–27.
- Four Web Sessions/Advanced base-guide routes and main-integration prerequisite: raw lines 29–36.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-pad|PAD overview (mandate and delayed-outcome context)]]
- [[source-adyen-docs-payment-methods-pad-web-drop-in|Web Drop-in child guide]]
- [[source-adyen-docs-payment-methods-pad-web-component|Web Components child guide]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pad/web/2026-09-15|PADs Canada for Web, fetched 2026-09-15]]
