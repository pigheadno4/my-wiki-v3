---
title: "BACS Direct Debit for Web | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bacs/web"
raw_files:
  - "adyen/docs/payment-methods/bacs/web/2026-09-15.md"
tags: [adyen, bacs, direct-debit, web, drop-in, components, integration-chooser]
---

## Overview

This 2026-09-15 page is a BACS Direct Debit **Web integration chooser**. It links Web Drop-in and Web Components child guides and four main Web Sessions/Advanced paths. It supplies no method request schema, Direct Debit Instruction (DDI), notice procedure or payment-outcome sequence itself (raw lines 15–36).

## Key takeaways

- The page routes to [[source-adyen-docs-payment-methods-bacs-web-drop-in|Web Drop-in]] as the all-in-one UI option or [[source-adyen-docs-payment-methods-bacs-web-component|Web Components]] using `BacsDirectDebit`. These child routes, rather than this chooser, own their own field and outcome instructions (raw lines 19–27).
- It says to create the main integration before adding BACS, and lists Drop-in/Components under both Sessions and Advanced flows. The four links identify possible base routes, not a statement that all require the same Checkout API version or request shape (raw lines 29–36).
- The related [[source-adyen-docs-payment-methods-bacs|BACS overview]] describes shopper DDI confirmation/submission, four-to-six-day clearing and settlement, advance-notice risk and undefendable chargebacks. Those are method-level context from the overview, not instructions in this chooser. The links and 2026-09-15 snapshot do not prove a live merchant configuration, valid DDI or cleared payment (overview raw lines 23–27, 35–74; this raw lines 2, 11, 15–36).

## Detail locators

- Web Drop-in versus `BacsDirectDebit` Components child routes: raw lines 19–27.
- Main-integration prerequisite and four Sessions/Advanced Web guide links: raw lines 29–36.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-bacs|BACS overview (DDI, clearing and chargeback context)]]
- [[source-adyen-docs-payment-methods-bacs-web-drop-in|Web Drop-in child guide]]
- [[source-adyen-docs-payment-methods-bacs-web-component|Web Components child guide]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bacs/web/2026-09-15|BACS Direct Debit for Web, fetched 2026-09-15]]
