---
title: "Adyen IRIS Web integration chooser"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/iris/web"
raw_files:
  - "adyen/docs/payment-methods/iris/web/2026-09-15.md"
tags: [adyen, iris, web, drop-in, components]
---

## Overview

This 2026-09-15-captured Adyen **IRIS for Web** page is a short chooser for method-specific Web Drop-in and Components guides. It also links the four main Web integration routes, which the page says to follow before adding IRIS. It does not describe request fields, redirect results, account enablement, or completed payment behavior. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-iris|the IRIS overview]] for the separate bank-contract, gateway, and operation qualifications.

## Key takeaways

- The **Drop-in** route points to `/payment-methods/iris/web-drop-in` and is described as an all-in-one website UI solution (pinned raw lines 19–23).
- The **Components** route points to `/payment-methods/iris/web-component`. Its rendered description is incomplete — “Use the to make IRIS payments on your website” — so use the linked child guide for actual Component behavior rather than filling in the missing text (lines 25–27).
- The page says to create the main integration before adding IRIS, then lists **Web Drop-in with Sessions**, **Web Components with Sessions**, **Web Drop-in with Advanced**, and **Web Components with Advanced** base guides (lines 29–36). These are navigation choices, not evidence that a particular merchant supports every flow or is live.

## Detail locators

- IRIS Web chooser and child-guide links: pinned raw lines 15–27.
- Main Sessions/Advanced Web Drop-in and Components guide links: lines 29–36.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-iris]] — IRIS method overview and bank/DIAS context

## Raw Sources

- [[raw/adyen/docs/payment-methods/iris/web/2026-09-15|IRIS Web chooser, captured 2026-09-15]]
