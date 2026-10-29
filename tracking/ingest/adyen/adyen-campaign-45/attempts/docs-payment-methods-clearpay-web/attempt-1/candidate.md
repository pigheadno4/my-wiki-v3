---
title: "Adyen Clearpay for Web"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/clearpay/web"
raw_files:
  - "adyen/docs/payment-methods/clearpay/web/2026-09-15.md"
tags: [adyen, clearpay, web, drop-in, components, online-payments]
---

## Overview

This captured [[adyen]] page is a **Web integration chooser** for Clearpay. It links method-specific Web Drop-in and Components guides and the main Web Sessions and Advanced integration guides. Its Components label says to use Redirect for Clearpay payments on a website; the chooser itself does not specify the request, return or payment-result contract. [[adyen-online-payments]]

## Key takeaways

- **Method-specific routes:** Drop-in is labelled as an all-in-one UI solution for adding Clearpay to a website. The Components route says to use Redirect. These are route descriptions, not full integration steps (raw lines 19–27).
- **Build the base integration first:** The See also section tells readers to create the main integration before adding Clearpay and links Web Drop-in and Components for both Sessions and Advanced flows (raw lines 29–36).
- **Evidence boundary:** This chooser gives no fields, API or Web SDK version, merchant enablement, capture/refund rule or transaction outcome. Use the chosen child and base guides for those questions.

## Detail locators

- Web chooser and child-guide links: pinned raw lines 15–27.
- Main Sessions/Advanced Drop-in/Components route list: pinned raw lines 29–36.

## Related

- [[adyen-online-payments]] — online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-clearpay-web-drop-in]] — Clearpay Web Drop-in guide.
- [[source-adyen-docs-payment-methods-clearpay-web-component]] — Clearpay Web Components guide.

## Raw Sources

- [[raw/adyen/docs/payment-methods/clearpay/web/2026-09-15|Clearpay for Web chooser, captured 2026-09-15]]
