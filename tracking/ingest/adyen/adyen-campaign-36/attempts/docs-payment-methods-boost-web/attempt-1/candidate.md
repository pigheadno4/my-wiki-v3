---
title: "Adyen Boost Wallet Web integration chooser"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boost/web"
raw_files:
  - "adyen/docs/payment-methods/boost/web/2026-09-15.md"
tags: [adyen, boost, web, wallets, navigation]
---

## Overview

This [[adyen]] page is a **Web integration chooser** for Boost Wallet. It links the Web Drop-in and Components method guides and four main Web integration routes. See [[adyen-online-payments]]. This navigation snapshot was captured 2026-09-15; it does not establish current method eligibility, implementation behavior or a payment result.

## Key takeaways

- The page presents **Drop-in** as the all-in-one website UI route and **Components** as a route whose link text refers to **Redirect**. These are links to separate child guides, not an API request, callback, QR, token or outcome specification. See raw lines 19–27.
- It instructs readers to create the **main integration before adding Boost Wallet**, then links Web Drop-in and Web Components main guides for both **Sessions** and **Advanced** flows. It does not select a flow for the merchant or state an SDK/API minimum. See raw lines 29–36.
- No country/currency matrix, Customer Area setup, TEST/live availability, redirect handling, QR expiry or settlement/refund procedure is given on this chooser. Those questions require their own pinned guide evidence; clicking a child link alone is not evidence of payment authorization or current support. See full raw lines 15–36.

## Detail locators

- **Drop-in and Components child links:** raw lines 19–27.
- **Main integration prerequisite and four flow links:** raw lines 29–36.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-boost]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/boost/web-drop-in/2026-09-15|Boost Wallet Web Drop-in guide]] — linked child; behavior separate.
- [[raw/adyen/docs/payment-methods/boost/web-component/2026-09-15|Boost Wallet Web Components guide]] — linked child; behavior separate.

## Raw Sources

- [[raw/adyen/docs/payment-methods/boost/web/2026-09-15|Boost Wallet Web chooser — captured 2026-09-15]]
