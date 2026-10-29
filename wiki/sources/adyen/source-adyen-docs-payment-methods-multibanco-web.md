---
title: "Multibanco Web integration chooser"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/multibanco/web"
raw_files:
  - "adyen/docs/payment-methods/multibanco/web/2026-09-15.md"
tags: [adyen, multibanco, web, drop-in, components]
---

## Overview

This 2026-09-15-captured Multibanco Web page is an **integration chooser**. It routes merchants to Multibanco Drop-in or Components child guides and to the main Web Sessions/Advanced integration guides. It does not itself give voucher action handling, request fields, payment finality, merchant eligibility or proof of a live paid transaction. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-multibanco]] for method-level voucher lifecycle.

## Key takeaways

- **Drop-in** is described as an all-in-one website UI solution and links the Multibanco Web Drop-in child guide (raw lines 19–23).
- **Components** links the Multibanco Web Component child guide. The chooser's phrase “Use the Multibanco” gives no class name, initialization procedure or capability assertion beyond navigation (raw lines 25–27).
- The “See also” section says to create the main integration before adding Multibanco and links Web Drop-in and Web Components for both Sessions and Advanced flows (raw lines 29–36). Follow the corresponding base and child guides for implementation; choosing a route does not mean a voucher has been paid.

## Detail locators

- Drop-in versus Components chooser: raw `### How do you want to integrate?` lines 19–27.
- Main Sessions/Advanced guide routes: raw `## See also` lines 29–36.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-multibanco]]
- [[source-adyen-docs-payment-methods-multibanco-web-drop-in]]
- [[source-adyen-docs-payment-methods-multibanco-web-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/multibanco/web/2026-09-15|Multibanco Web chooser, captured 2026-09-15]]
