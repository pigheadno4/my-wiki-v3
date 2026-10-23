---
title: "Adyen Web card-payment integration chooser"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/web"
raw_files:
  - "adyen/docs/payment-methods/cards/web/2026-09-15.md"
tags: [adyen, cards, web, integration-navigation]
---

## Overview

This [[adyen]] page is a short **Web card-payment integration chooser**, linking Drop-in, Card Component, and a custom integration. Its 2019 modification metadata and 2026 capture mark it as a dated navigation snapshot. It describes the options, not their full implementation, current support, merchant eligibility, PCI requirements, or payment outcome. [[adyen-online-payments]]

## Key takeaways

- **Drop-in** is described as an all-in-one card-payment UI for a website, and **Card Component** as a card-payment UI. These are links to separate guides rather than claims about a configured merchant or an implemented checkout. See raw lines 19–27.
- The **Custom integration** route says to build a UI and use the Custom Card Web Component to securely collect and encrypt card details. This one-sentence navigation does not specify card-data handling boundaries, PCI scope, or a full payment request; consult the linked guide before applying it. See raw lines 29–31.
- The closing “more information” links point to Web Drop-in and Components integration pages. This page does not label either link with an API flow or SDK version, and it gives no server, webhook, authentication, authorization, capture, or settlement sequence. See raw line 33.

## Detail locators

- Source modification and capture metadata: raw lines 2, 11.
- All three card UI choices and their child URLs: raw lines 19–31.
- Supplemental Web integration guide links: raw line 33.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/web/2026-09-15|Adyen Web cards chooser snapshot]]
