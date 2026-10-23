---
title: "Adyen Korean Card Payments via redirect Web Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/korean-cards/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/cards/korean-cards/web-drop-in/2026-09-15.md"
tags: [adyen, cards, korean-cards, web-drop-in, redirect]
---

## Overview

This 2026-09-15 guide describes method-specific additions for **Korean Card Payments via redirect** in an existing **Web Drop-in** integration. It separates Sessions and Advanced server-side flows and points to the main integration guides for general payment/redirect handling. These dated setup instructions do not establish current merchant availability or a successful payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions flow:** The merchant must already have a Sessions Web Drop-in integration using Checkout API **v68 or later**, with `action.type: redirect` handling, and add Korean Card Payments via redirect in Customer Area. The guide says no additional `/sessions` parameters are needed specifically for this method. It does not extend its v68 minimum to the Advanced flow. (raw lines 23–42)
- **Advanced flow:** The merchant must already have an Advanced Web Drop-in integration, redirect handling, and Customer Area method setup. The guide says no additional `/payments` parameters are needed specifically for this method. It gives no separate Advanced Checkout API minimum in this page. (raw lines 64–74, 88–92)
- In either flow, individual Adyen Web imports may optionally include `Redirect` for tree shaking. This is a performance option, not a requirement for all package-import patterns. (raw lines 44–54, 76–86)
- For both flows, the guide directs merchants to contact Support for test-environment setup and says live card acceptance requires assessing PCI DSS compliance and submitting a required Self-Assessment Questionnaire A document. This page alone is not a compliance determination or proof of live enablement. (raw lines 56–62, 94–100)
- The page supplies no payment-result or redirect-return example. Its reference to `action.type: redirect` is an existing-integration prerequisite, not evidence that a shopper completed authentication, authorization, capture, or settlement. (raw lines 29–36, 68–74)

## Detail locators

- Sessions requirements and no-extra-parameter `/sessions` statement: raw lines 23–42.
- Sessions optional import and test/live gates: raw lines 44–62.
- Advanced requirements, optional import and no-extra-parameter `/payments` statement: raw lines 64–92.
- Advanced test/live gates: raw lines 94–100.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/korean-cards/web-drop-in/2026-09-15|Adyen Korean Card Payments Web Drop-in guide, 2026-09-15 snapshot]]
