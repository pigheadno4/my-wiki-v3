---
title: "Adyen PayTo Web integration chooser"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payto/web"
raw_files:
  - "adyen/docs/payment-methods/payto/web/2026-09-15.md"
tags: [adyen, payto, web, integration-chooser]
---

## Overview

This 2026-09-15-captured Adyen page is a **Web integration chooser** for PayTo. It routes to Web Drop-in or Components method guides and to Sessions or Advanced base integrations. It contains no PayTo request fields, agreement/mandate lifecycle, SDK minimum, payment outcome or merchant enablement evidence. See [[adyen]], [[adyen-online-payments]], and the separate PayTo method overview [[source-adyen-docs-payment-methods-payto]].

## Key takeaways

- The page presents **Drop-in** as Adyen's all-in-one website UI route and **Components** as a PayTo website payment route. Its Components label says “Use the PayTo”; it does not name a specific class or define Component behavior here. See raw lines 19–27.
- It says to create the main integration before adding PayTo and lists four base routes: **Web Drop-in with Sessions**, **Web Components with Sessions**, **Web Drop-in with Advanced**, and **Web Components with Advanced**. Follow the chosen child guide for PayTo-specific fields, mandate flow and outcome handling. See raw lines 29–36.
- The separate method overview describes Australian PayTo bank agreements, one-off/recurring payments and webhook finality. Those details are not claims of this 36-line Web chooser; its links alone do not establish current account eligibility or an executed payment. See [[source-adyen-docs-payment-methods-payto]] and raw lines 15–36.

## Detail locators

- Web Drop-in and Components routes: raw lines 19–27.
- Base Sessions and Advanced integration routes: raw lines 29–36.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-payto]]
- [[source-adyen-docs-payment-methods-payto-web-drop-in]]
- [[source-adyen-docs-payment-methods-payto-web-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payto/web/2026-09-15|Fully read PayTo Web chooser raw]]
