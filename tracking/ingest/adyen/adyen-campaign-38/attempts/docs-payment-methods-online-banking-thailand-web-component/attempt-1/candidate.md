---
title: "Online banking Thailand Web Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-thailand/web-component"
raw_files:
  - "adyen/docs/payment-methods/online-banking-thailand/web-component/2026-09-15.md"
tags: [adyen, online-banking, thailand, web, components]
---

## Overview

This 2026-09-15 guide adds Online banking Thailand to an existing Adyen Web Components integration. It separates Sessions and Advanced server-side flows, with redirect handling and Customer Area method setup in both. It is a method-specific supplement to the linked main integration guides. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Sessions requires an existing Web Components Sessions integration, Checkout API v68 or later, redirect handling and Customer Area setup; no additional `/sessions` parameters are stated. Advanced separately requires an existing Web Components Advanced integration, redirect handling and Customer Area setup; no additional `/payments` parameters are stated. The v68 requirement appears in the Sessions section only. See raw lines 25–42 and 114–156.
- The guide says to import and initialize `MolPayEBankingTH` in both flows. Its Sessions configuration table offers optional `issuer` bank preselection, `highlightedIssuers` ordering, `showImage` logo display and `placeholder` text. It specifically says `highlightedIssuers` was added in Web v5.1.0; that is not a stated minimum for the entire payment method. See raw lines 44–104 and 124–150.
- The page lists five bank issuer IDs. Its illustrative configuration object gives `highlightedIssuers` as a single string despite prose referring to IDs for banks in plural; the page does not settle the field's full accepted shape. See raw lines 62–88.
- TEST guidance says to use an available issuer ID and inspect Customer Area Payment list for test status. A separate request in live Customer Area is required before accepting live payments. Neither the test instruction nor redirect setup proves a successful final authorization or current merchant eligibility. See raw lines 106–112 and 158–164.
- This component page does not provide a QR flow, shopper-return/result-code procedure or webhook outcome table; follow the linked base guides and separate method flow evidence for those. See raw lines 25–164.

## Detail locators

- Sessions requirements, import/configuration and issuer IDs: raw lines 25–104.
- Advanced prerequisites, import/initialization and no-extra-parameters statement: raw lines 114–156.
- Repeated TEST/live setup conditions: raw lines 106–112 and 158–164.

## Related

- [[adyen-online-payments]] — main online-payments concept.
- [[source-adyen-docs-payment-methods-online-banking-thailand]] — separate method overview.
- [[adyen]] — provider entry.

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-thailand/web-component/2026-09-15|Online banking Thailand Web Component (2026-09-15)]]
