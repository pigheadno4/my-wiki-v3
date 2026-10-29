---
title: "Atome iOS Component | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/atome/ios-component"
raw_files:
  - "adyen/docs/payment-methods/atome/ios-component/2026-09-15.md"
tags: [adyen, atome, ios, components, redirect, refunds]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] guide adds Atome to an existing iOS Components integration using Sessions or Advanced server-side flow. It covers request additions, `AtomeComponent` initialization, redirect setup, partial refunds and sandbox/live routes. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-atome|the Atome overview]] for broader context. The examples do not prove eligibility or a completed payment.

## Key takeaways

- Sessions requires an existing iOS Components Sessions integration, Checkout API v68 or later, redirect handling and Atome added in Customer Area (raw lines 25–36). Advanced requires an existing iOS Components Advanced integration, redirect handling and the same setup (lines 793–803). The Advanced Integration type label says Components but links to `integration=Drop-in` (line 801); verify the matching Components base guide.
- Both request tables mark shopper full name, email, telephone, billing address, `lineItems` and `countryCode` required; `deliveryAddress` is optional when it matches billing (Sessions lines 40–52; Advanced lines 837–850). The documented country/currency pairs are MY/MYR and SG/SGD. Advanced additionally requires `paymentMethod.type: atome` (line 843). TEST examples show SG/SGD with v71 `/sessions` and v72 `/payments`; sample versions do not replace the Sessions minimum (lines 54–115, 852–922).
- Neither flow needs additional Atome configuration parameters (lines 732–736, 805–809). The iOS snippets use `AtomePaymentMethod` and `AtomeComponent`; Sessions assigns the session as delegate, Advanced assigns self (lines 738–761, 811–833). The Advanced example response is `RedirectShopper` with a redirect action (lines 1567–1579). Its “successful payment” heading does not establish final authorisation or settlement.
- The Sessions curl repeats `countryCode: SG` (lines 72, 78), and both curl examples omit shell continuation between `-X POST` and `-d` (lines 63–64, 861–862). Advanced's iOS example uses an HTTPS `returnUrl` (line 871), while the Sessions example uses `adyencheckout://your.package.name` (line 70). The guide does not reconcile these return-URL styles; verify the selected iOS base flow.
- Both sections describe partial refund via `/payments/{paymentPspReference}/refunds` with an `amount` (lines 763–771, 1581–1589); this page gives no capture or final-result procedure. Testing requires an Atome sandbox shopper account requested via an Adyen contact, with a different account per country/region tested; it lists MY/SG test apps and Customer Area status checks (lines 773–789, 1591–1607). For live acceptance, contact Support to add Atome in live Customer Area (lines 791, 1609).

## Detail locators

- Scope and Sessions requirements/fields: raw lines 15–52.
- Sessions v71 SG/SGD TEST request: lines 54–731; repeated country code at 72/78 and curl continuation at 63–64.
- Sessions configuration, Component, refund, test/live: lines 732–791.
- Advanced requirements, misrouted link, Component and fields: lines 793–850.
- Advanced v72 SG/SGD TEST request: lines 852–1565; curl continuation at 861–862 and HTTPS return URL at 871.
- Advanced redirect response, partial refund and test/live: lines 1567–1609.

## Related

- [[adyen-online-payments]] — provider online-payment integration concept.
- [[source-adyen-docs-payment-methods-atome]] — Atome method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/atome/ios-component/2026-09-15|2026-09-15 Atome iOS Component guide]]
