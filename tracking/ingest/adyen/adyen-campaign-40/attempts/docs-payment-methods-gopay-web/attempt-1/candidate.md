---
title: "Adyen GoPay Web integration chooser"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gopay/web"
raw_files:
  - "adyen/docs/payment-methods/gopay/web/2026-09-15.md"
tags: [adyen, gopay, web, drop-in, components, redirect]
---

## Overview

This 2026-09-15 captured Adyen page is a GoPay Web integration chooser. It routes readers to separate Drop-in and Components child guides and four base Web guides covering Sessions/Advanced with Drop-in/Components. It gives no method setup, request, redirect completion, tokenization or result procedure of its own. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The Drop-in choice is described as an all-in-one UI solution and links [[source-adyen-docs-payment-methods-gopay-web-drop-in]]. The Components choice links [[source-adyen-docs-payment-methods-gopay-web-component]] and says "Use the Redirect"; this label alone does not specify the Redirect Component API or runtime behavior.
- The See also section says to create the main integration before adding GoPay. It lists Web Drop-in and Web Components main guides for each of Sessions and Advanced flows. This chooser does not itself establish supported SDK/API versions, account eligibility, GoPay redirect and return handling, stored-payment behavior, or a payment outcome.

## Detail locators

- Web scope and Drop-in/Components child choices: pinned raw lines 15–27.
- Main integration prerequisite and four Sessions/Advanced base links: pinned raw lines 29–36.

## Related

- [[adyen-online-payments]] — main provider online-payment concept
- [[source-adyen-docs-payment-methods-gopay-web-drop-in]] — GoPay Web Drop-in child guide
- [[source-adyen-docs-payment-methods-gopay-web-component]] — GoPay Web Components child guide

## Raw Sources

- [[raw/adyen/docs/payment-methods/gopay/web/2026-09-15|GoPay Web chooser, 2026-09-15]]
