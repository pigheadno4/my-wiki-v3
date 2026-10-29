---
title: "Adyen Online banking Finland Web integration chooser"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/finland-online-banking/web"
raw_files:
  - "adyen/docs/payment-methods/finland-online-banking/web/2026-09-15.md"
tags: [adyen, finland-online-banking, web, integration-chooser]
---

## Overview

This 2026-09-15-captured Adyen page is a **Web integration chooser** for Online banking Finland. It routes readers to Web Drop-in or Components method guides and to Sessions or Advanced base integrations. It contains no Web request schema, Checkout API minimum, payment outcome, or proof of current merchant enablement. See [[adyen]], [[adyen-online-payments]], and the separate FI/EUR method overview [[source-adyen-docs-payment-methods-finland-online-banking]].

## Key takeaways

- The page presents **Drop-in** as Adyen's all-in-one website UI route and **Components** as the route using `Redirect` for Online banking Finland. These are navigation labels, not implementation or execution evidence. See raw lines 19–27.
- It says to create the main integration before adding this method. The base-guide choices are **Web Drop-in with Sessions**, **Web Components with Sessions**, **Web Drop-in with Advanced**, and **Web Components with Advanced**. Follow the selected method guide for request fields and redirect handling; this chooser itself provides none. See raw lines 29–36.
- The separate method overview describes a Paytrail-backed FI/EUR bank-redirect method and has bank-selection/refund-note qualifications. Those facts come from that overview, not from this short Web chooser. See [[source-adyen-docs-payment-methods-finland-online-banking]] and raw lines 15–36.

## Detail locators

- Web Drop-in and Components method-guide routes: raw lines 19–27.
- Base Sessions and Advanced integration navigation: raw lines 29–36.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-finland-online-banking]]
- [[source-adyen-docs-payment-methods-finland-online-banking-web-component]]
- [[source-adyen-docs-payment-methods-finland-online-banking-web-drop-in]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/finland-online-banking/web/2026-09-15|Fully read Online banking Finland Web chooser raw]]
