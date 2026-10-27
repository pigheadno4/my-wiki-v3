---
title: "SEPA Direct Debit for Web integration chooser"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/sepa-direct-debit/web"
raw_files:
  - "adyen/docs/payment-methods/sepa-direct-debit/web/2026-09-15.md"
tags: [adyen, sepa-direct-debit, web, integration-chooser]
---

## Overview

This 2026-09-15 Adyen page is a **SEPA Direct Debit Web integration chooser**. It links Web Drop-in and Web Components SEPA child guides and the four base Web Sessions/Advanced guides. It does not specify SEPA request fields, API/Web version minima, IBAN handling, shopper permission/mandate rules, capture, payment outcome or live availability. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Drop-in** links the all-in-one UI child at `/payment-methods/sepa-direct-debit/web-drop-in`; **Components** links `/payment-methods/sepa-direct-debit/web-component` and names `SepaDirectDebit`. These are alternative Web integration routes, not interchangeable request schemas. See raw lines 19–27.
- The page directs readers to create their **main Web integration first**, with separate Sessions/Advanced guides for Drop-in and Components. Its role is navigation; use the matching child and base guide for implementation. See raw lines 29–36.
- Neither the chooser's phrase 'make SEPA Direct Debit payments' nor a child link establishes a valid shopper authorization, cleared debit or settled funds. The reviewed [[source-adyen-docs-payment-methods-sepa-direct-debit]] overview and matching Web child guide provide the method-specific conditions. See raw lines 15–36.

## Detail locators

- Drop-in and Components SEPA child routes: raw lines 19–27.
- Base Sessions/Advanced Web guide routes: raw lines 29–36.

## Related

- [[adyen-online-payments]] — SEPA online-payment route.
- [[source-adyen-docs-payment-methods-sepa-direct-debit-web-drop-in]] — Web Drop-in child.
- [[source-adyen-docs-payment-methods-sepa-direct-debit-web-component]] — Web Component child.
- [[source-adyen-docs-payment-methods-sepa-direct-debit]] — SEPA method overview and lifecycle.

## Raw Sources

- [[raw/adyen/docs/payment-methods/sepa-direct-debit/web/2026-09-15|SEPA Direct Debit for Web, captured 2026-09-15]]
