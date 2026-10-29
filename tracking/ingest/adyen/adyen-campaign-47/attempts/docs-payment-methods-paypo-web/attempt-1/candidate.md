---
title: "Adyen PayPo for Web integration chooser"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypo/web"
raw_files:
  - "adyen/docs/payment-methods/paypo/web/2026-09-15.md"
tags: [adyen, paypo, web, drop-in, components, online-payments]
---

## Overview

This captured [[adyen]] page is a PayPo Web integration chooser. It directs readers to method-specific Drop-in and Components child guides and to the four main Web Sessions/Advanced integration routes. It does not itself supply request fields, authorization or capture rules, or evidence of merchant enablement or payment execution. [[adyen-online-payments]]

## Key takeaways

- **Method-specific choices:** The Drop-in link points to `/payment-methods/paypo/web-drop-in` and describes an all-in-one UI. The Components link points to `/payment-methods/paypo/web-component` and describes using Redirect for PayPo on a website (raw lines 19–27).
- **Base-flow prerequisite routes:** The page says to create the main integration before adding PayPo and links Web Drop-in and Web Components guides for both Sessions and Advanced flows. Follow the selected child and base guide for implementation details; this chooser alone does not specify payment outcome or live setup (raw lines 29–36).

## Detail locators

- Page identity and method-specific Web choices: pinned raw lines 15–27.
- Main Sessions/Advanced Drop-in/Components routes: pinned raw lines 29–36.

## Related

- [[adyen-online-payments]] — provider online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-paypo-web-drop-in]] — captured PayPo Web Drop-in child guide.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypo/web/2026-09-15|PayPo Web chooser, captured 2026-09-15]]
