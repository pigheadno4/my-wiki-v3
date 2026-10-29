---
title: "Afterpay Web Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/afterpaytouch/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/afterpaytouch/web-drop-in/2026-09-15.md"
tags: [adyen, afterpay, web, drop-in, redirect]
---

## Overview

This 2026-09-15 Adyen Docs page describes **Afterpay-specific additions** to an existing Web Drop-in integration. It separates Sessions and Advanced server-side flows and directs both to the base guide for redirect handling. See [[adyen-online-payments]], [[source-adyen-docs-payment-methods-afterpaytouch]] and [[adyen]].

## Key takeaways

- Sessions requires an existing Web Drop-in Sessions flow, Checkout API **v68 or later**, `action.type: redirect` handling and Afterpay added in Customer Area (raw lines 25–36). Its `/sessions` table marks shopper name/email/reference (reference minimum three characters), country code, billing/delivery addresses and line items required; telephone number is optional (lines 40–53). The AU/AUD TEST request examples are fixtures, not country eligibility or successful payment evidence (lines 55–737).
- For either flow, importing individual Adyen Web methods is **optional** for tree shaking; if used, the example imports `Redirect` alongside `AdyenCheckout` and `Dropin` (Sessions lines 739–749; Advanced lines 807–817). The page does not give a Web SDK version or a method-specific Drop-in configuration.
- Advanced requires an existing Web Drop-in Advanced flow, redirect handling and Customer Area addition (lines 795–805). Its `/payments` table also requires `paymentMethod: afterpaytouch` and the same shopper/country/address/item fields, with optional phone (lines 819–835). Its sample initial response has `resultCode: RedirectShopper` and a redirect `action` (lines 1550–1564); this is not final authorisation or capture proof. The page links the base guide for handling the redirect and does not itself document the completed return/webhook result. The Advanced base-integration link at line 803 contains an encoded unresolved `{{getParameter('platform')}}` placeholder; use the explicit Web redirect/request links nearby rather than treating that template as a reliable platform route.
- Afterpay capture can be automatic after authorisation or manual, depending on merchant-account configuration. Delaying capture needs delay setup or manual capture; partial capture needs manual capture. Capture is required within **13 days** after authorisation; otherwise Afterpay cancels and refunds the first instalment charged during authorisation. Test authorisations expire in **one day** (Sessions lines 753–761; Advanced lines 1566–1574). A partial manual capture cancels the unclaimed remainder unless the account is enabled for multiple partial captures. That feature requires contacting Support and creates a new invoice for each capture (lines 763–772 and 1576–1585).
- Sandbox testing calls for a test shopper account and test card, with a different account per test region. The child page offers AU, NZ, US and CA in the **sandbox account selector** (lines 774–793 and 1589–1608), while the linked Afterpay overview's method matrix lists **AU, CA and NZ** and calls the US service Cash App Afterpay/$Afterpay (overview raw lines 23–31). The US sandbox choice is not proof of US live eligibility for this method. Before accepting live Afterpay payments, the page says to submit a request in live Customer Area; it does not prove a specific merchant is enabled.

## Detail locators

- Page scope and Sessions requirements: lines 15–36.
- Sessions request table, TEST examples, optional import, capture and sandbox/live: lines 40–793.
- Advanced requirements, optional import, request table and TEST examples: lines 795–1548; redirect response lines 1550–1564.
- Advanced capture and sandbox/live repetition: lines 1566–1608.
- Related overview country/branding qualification: `raw/adyen/docs/payment-methods/afterpaytouch/2026-09-15.md` lines 23–31.

## Related

- [[adyen-online-payments]] — provider online-payment architecture.
- [[source-adyen-docs-payment-methods-afterpaytouch]] — product/country overview and US branding.

## Raw Sources

- [[raw/adyen/docs/payment-methods/afterpaytouch/web-drop-in/2026-09-15|2026-09-15 Afterpay Web Drop-in Sessions and Advanced guide]]
