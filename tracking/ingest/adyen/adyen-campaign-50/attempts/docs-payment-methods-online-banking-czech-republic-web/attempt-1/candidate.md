---
title: "Online banking Czech Republic for Web integration chooser"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-czech-republic/web"
raw_files:
  - "adyen/docs/payment-methods/online-banking-czech-republic/web/2026-09-15.md"
tags: [adyen, online-banking-czech-republic, web, integration-router]
---

## Overview

This 2026-09-15-captured Adyen page is the **Web integration chooser** for Online banking Czech Republic. It routes to Web Drop-in and Components child guides and to the corresponding Sessions or Advanced base integrations. It does not itself specify issuer IDs, request fields, redirect handling, current bank coverage, account enablement or payment outcome. See [[adyen]], [[adyen-online-payments]] and the [[source-adyen-docs-payment-methods-online-banking-czech-republic|method overview]].

## Key takeaways

- **Drop-in** is described as Adyen's all-in-one UI option for adding this Czech online banking method to a website. The linked Web Drop-in child guide supplies method-specific steps; this chooser provides only the navigation route (raw lines 19–23).
- **Components** links to the Web Component child and names `OnlineBankingCZ`. Follow [[source-adyen-docs-payment-methods-online-banking-czech-republic-web-component]] for the Component, issuer-picker and redirect details; the short chooser label alone is not a configuration contract (raw lines 25–27).
- The **See also** section says to build the main integration before adding the method. It lists four Web base routes: Drop-in or Components, each for Sessions or Advanced flow (raw lines 29–36).
- The separate [[source-adyen-docs-payment-methods-online-banking-czech-republic|overview]] describes a **CZ/CZK bank redirect** in which the shopper selects an issuing bank and completes payment on the bank website/app. Its capability marks and contract statement are method-level snapshot claims, not request-field or live-payment proof from this chooser (overview pinned raw lines 23–31).

## Detail locators

- Web chooser and Drop-in route: raw lines 15–23.
- `OnlineBankingCZ` Components route: raw lines 25–27.
- Sessions/Advanced base-guide links and main-integration prerequisite: raw lines 29–36.
- Method-level CZ/CZK bank redirect and capability matrix: [[source-adyen-docs-payment-methods-online-banking-czech-republic]] and its pinned raw lines 23–31; this entry's raw_files remains chooser-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic-web-component]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/online-banking-czech-republic/web-drop-in/2026-09-15|Web Drop-in child guide for method-specific details; not read for this chooser]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-czech-republic/web/2026-09-15|Online banking Czech Republic Web chooser, captured 2026-09-15]]
