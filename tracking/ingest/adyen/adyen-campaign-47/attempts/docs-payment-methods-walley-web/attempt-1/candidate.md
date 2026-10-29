---
title: "Adyen Walley for Web"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/walley/web"
raw_files:
  - "adyen/docs/payment-methods/walley/web/2026-09-15.md"
tags: [adyen, walley, web, drop-in, components]
---

## Overview

This captured Adyen page is a Web integration chooser for Walley. It routes website implementers to separate Walley Web Drop-in and Web Components guides and to the main Web integration guides for those UI choices. It is navigation, not a method-specific request recipe or evidence of current merchant eligibility, account activation, or a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Drop-in route:** The page calls Drop-in an all-in-one UI for adding Walley to a website and links its method-specific Web Drop-in guide. The captured guide has a local source route at [[source-adyen-docs-payment-methods-walley-web-drop-in]]. [Raw: lines 19–23]
- **Components route:** The page links a separate method-specific Web Component guide for rendering Walley on a website. Its contents are not specified by this chooser page. [Raw: lines 25–27]
- **Main integrations:** The final line links the general Web Drop-in and Components Sessions-flow guides. Follow the selected method-specific child guide and base integration guide for implementation details; this chooser itself states no country, currency, payment field, B2B/B2C, result or capture rules. [Raw: line 29]

## Detail locators

- Web identity and integration-choice heading: pinned raw lines 15–19.
- Drop-in and Components child-guide links: pinned raw lines 21–27.
- General Web UI integration routes: pinned raw line 29.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-walley]] — separate Walley method overview.
- [[source-adyen-docs-payment-methods-walley-web-drop-in]] — method-specific Web Drop-in guide.

## Raw Sources

- [[raw/adyen/docs/payment-methods/walley/web/2026-09-15|Walley Web chooser, captured 2026-09-15]]
