---
title: "Atome React Native Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/atome/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/atome/react-native-drop-in/2026-09-15.md"
tags: [adyen, atome, react-native, drop-in, redirect, refunds]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] guide adds Atome to an existing **React Native Drop-in** integration using Sessions or Advanced server-side flow. It covers request additions, redirect prerequisites, partial refunds and sandbox/live routes. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-atome|the Atome overview]] for broader context. Its TEST examples do not prove current account availability or completed payment.

## Key takeaways

- Sessions requires an existing React Native Drop-in Sessions integration, **Checkout API v68 or later**, redirect handling and Atome added in Customer Area (raw lines 25–36). Its Integration type label says Sessions but its URL targets the **Advanced** flow (line 33); follow the label and the correctly scoped Sessions links on the page. Advanced requires an existing React Native Drop-in Advanced integration, redirect handling and the same Customer Area setup (lines 768–778).
- Both tables mark shopper full name, email, telephone, billing address, `lineItems` and `countryCode` required; `deliveryAddress` is optional when it matches billing (Sessions lines 40–52; Advanced lines 788–801). The supported country/currency pairs specified here are **MY/MYR** and **SG/SGD**. Advanced additionally requires `paymentMethod.type: atome` (line 794). The SG/SGD TEST samples use v71 `/sessions` and v72 `/payments`, not a general SDK or payment-success guarantee (lines 54–115, 803–873).
- No additional Atome Drop-in configuration parameters are needed in either section (lines 732–736, 780–784). The Advanced example headed “successful payment” is `RedirectShopper` with `action.type: redirect` (lines 1518–1530), a shopper handoff rather than final authorisation or settlement.
- The Sessions curl repeats `countryCode: SG` (lines 72, 78), and both curl snippets omit shell continuation between `-X POST` and `-d` (lines 63–64, 812–813). The Sessions example uses the app-scheme `adyencheckout://your.package.name` return URL (line 70), while Advanced uses HTTPS (line 822); the page does not reconcile the difference. Use the selected base flow for return handling.
- Both sections route partial refunds to `/payments/{paymentPspReference}/refunds` with an `amount` (lines 738–746, 1532–1540). Testing requires an Atome sandbox shopper account requested through an Adyen contact and a separate account per tested country/region; the page lists MY/SG test apps and test Customer Area status checks (lines 748–764, 1542–1558). For live acceptance, contact Support to add Atome to live Customer Area (lines 766, 1560). This page gives no Atome-specific capture or final-result procedure.

## Detail locators

- Scope and Sessions requirements/fields: raw lines 15–52; misrouted Sessions prerequisite at 33.
- Sessions v71 SG/SGD TEST example: lines 54–731; duplicate country code at 72/78 and curl continuation at 63–64.
- Sessions configuration, partial refunds and test/live: lines 732–766.
- Advanced requirements, configuration and `/payments` fields: lines 768–801.
- Advanced v72 SG/SGD TEST request: lines 803–1516; curl continuation at 812–813 and HTTPS return URL at 822.
- Advanced redirect response, partial refunds and test/live: lines 1518–1560.

## Related

- [[adyen-online-payments]] — provider online-payment integration concept.
- [[source-adyen-docs-payment-methods-atome]] — Atome method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/atome/react-native-drop-in/2026-09-15|2026-09-15 Atome React Native Drop-in guide]]
