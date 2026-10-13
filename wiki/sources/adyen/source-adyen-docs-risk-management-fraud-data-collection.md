---
title: "Adyen Docs: Data collection to detect fraud"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/fraud-data-collection"
raw_files:
  - "adyen/docs/risk-management/fraud-data-collection/2026-09-15.md"
tags: [adyen, protect, fraud-data, web, privacy, sdk]
---

## Overview

This Adyen Web integration guide explains fraud-signal collection for [[adyen-risk-management|Protect]]: which checkout routes collect and send data automatically, how a merchant-built API-only page uses the standalone collection SDK, and how collection can extend beyond checkout. It covers device and behavior information, cookies, privacy considerations, and the server handoff to `riskData.clientData`. The described data collection is a separate configuration setting from Protect itself.

## Key takeaways

- For Web Drop-in and Components in Advanced or Sessions flow, Hosted Checkout, and Web API-only using the Custom Card Component, the guide says checkout-page data is collected and sent automatically. A merchant-built Web API-only checkout requires added SDK configuration. An API-only integration that processes raw card data has additional PCI compliance requirements; this page does not establish that those requirements are met.
- The checkout risk collection setting defaults to **on** for the automatic routes and is **independent of Protect configuration**. The `AdyenCheckout` `risk.enabled` setting can turn collection off; Adyen warns this raises fraud exposure. Protect use separately requires setting up risk and at least one profile. Thus, turning Protect off should not be read as proof that client data collection stopped.
- For a merchant-built API-only Web checkout, the merchant loads the standalone SDK in the iframe where card details are entered, obtains data with `adyenGetData()`, and has its server send that data in `riskData.clientData` on `/payments`. Test and live script URLs differ. The example curl body places a JavaScript call directly where JSON would need a value; it illustrates the handoff rather than a copy-ready request.
- For Web integrations, adding the collection script to non-checkout pages is optional. The guide says Drop-in or Components send data accumulated from those pages when the shopper checks out. Adyen's SDK data table lists cookies with 30-day/session browser lifetimes and device/behavior information with an indefinite lifetime in this snapshot; the precise categories and examples are at raw lines 67–76.
- Adyen tells the merchant to assess applicable privacy rules **before** processing shopper data, consult legal expertise for its operating regions, provide appropriate transparency/consent where required, and track shoppers who consent. The page gives European consent as an example; it is not independent or current legal advice. Its claims about anonymized cross-customer use and no marketing use are Adyen's statements in the captured page, not verification of a particular merchant's data handling.

## Detail locators

- **Requirements, raw lines 21–33** — automatic versus configured Web routes and the API-only raw-card PCI caveat.
- **Data privacy, raw lines 35–42** — merchant obligations, regional-law variation, transparency, consent, and consent tracking examples.
- **How it works / How Protect uses the data, raw lines 44–65** — collection actors, checkout and other-page scope, device/behavior examples, Adyen usage statements, and Protect setup.
- **Data collected by the SDK, raw lines 67–76** — cookie, device, and behavior categories, purposes, domains, and snapshot lifetimes.
- **Configure Drop-in and Components, raw lines 78–115** — independent default `risk.enabled`, opt-out warning, and optional script on other pages.
- **Configure API only, raw lines 117–195** — environment-specific SDK URLs, checkout iframe placement, `adyenGetData()`, server `riskData.clientData` field, and illustrative test `/payments` request.

## Related

- [[adyen]]
- [[adyen-risk-management]]
- [[adyen-online-payments]]
- [[adyen-pci-dss-compliance]]

## Raw Sources

- [[raw/adyen/docs/risk-management/fraud-data-collection/2026-09-15|Adyen Docs — Data collection to detect fraud (2026-09-15)]]
