---
title: "Adyen Rakuten Pay Web integration chooser"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/rakutenpay/web"
raw_files:
  - "adyen/docs/payment-methods/rakutenpay/web/2026-09-15.md"
tags: [adyen, rakutenpay, web, wallets, navigation]
---

## Overview

This [[adyen]] page is a **Web integration chooser** for Rakuten Pay. It links Web Drop-in and Components method guides and four main Web integration routes. See [[adyen-online-payments]]. The captured 2026-09-15 navigation page does not establish current merchant enablement or an executed payment.

## Key takeaways

- **Drop-in** is presented as an all-in-one website UI option; **Components** links to a page whose label says to use **Redirect**. These are child-guide links, not evidence of request fields, action/callback handling, authentication, recurring approval, tokenization or transaction result. See raw lines 19–27.
- The page says to create the **main integration before adding Rakuten Pay**, then links main Web Drop-in and Web Components guides for both **Sessions** and **Advanced** flows. It does not choose the merchant's flow or state an SDK/Checkout API minimum. See raw lines 29–36.
- The chooser provides no JP/JPY matrix, Customer Area setup, DGFT simulator instructions, recurring eligibility or final authorization/capture/settlement procedure. Those claims require the pinned overview or respective child guide; navigation does not confer current availability. See complete raw lines 15–36.

## Detail locators

- **Drop-in/Components child routes:** raw lines 19–27.
- **Main integration prerequisite and Sessions/Advanced links:** raw lines 29–36.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-rakutenpay]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/rakutenpay/web-drop-in/2026-09-15|Rakuten Pay Web Drop-in guide]] — linked child; behavior separate.
- [[raw/adyen/docs/payment-methods/rakutenpay/web-component/2026-09-15|Rakuten Pay Web Components guide]] — linked child; behavior separate.

## Raw Sources

- [[raw/adyen/docs/payment-methods/rakutenpay/web/2026-09-15|Rakuten Pay Web chooser — captured 2026-09-15]]
