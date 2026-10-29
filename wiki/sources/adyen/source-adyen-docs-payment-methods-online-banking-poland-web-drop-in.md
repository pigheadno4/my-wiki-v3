---
title: "Adyen Online banking Poland Web Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-poland/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-poland/web-drop-in/2026-09-15.md"
tags: [adyen, online-banking-poland, web, drop-in, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Poland** to an existing Web Drop-in integration. It covers Sessions and Advanced request additions, redirect handling, optional `OnlineBankingPL` import, and test/live setup. It is a method-specific add-on, not a complete Web integration or proof of current account enablement. See [[adyen]], [[adyen-online-payments]], and the separate PL/PLN Przelewy24 method overview [[source-adyen-docs-payment-methods-online-banking-poland]].

## Key takeaways

- **Sessions:** start with an existing Web Drop-in Sessions flow, Checkout API v68 or later, redirect handling for `action.type: redirect`, and Online banking Poland added in Customer Area. The `/sessions` table requires `shopperEmail` and says it must be **50 or fewer characters**. The TEST v71 examples use PL/PLN. The curl and some SDK snippets are incomplete as shown; the displayed custom-scheme `adyencheckout://your.package.name` return URL is a mobile-style example in a Web guide, not a validated Web return route. See raw lines 25–69 and 71–268.
- For either flow, importing `OnlineBankingPL` individually alongside Adyen Web and Drop-in is **optional**, offered for tree shaking/performance. Do not turn the optional import into a prerequisite for showing the method. See raw lines 270–280 and 302–312.
- **Advanced:** start with an existing Web Drop-in Advanced flow, redirect handling, and method addition in Customer Area. Its integration-guide link contains an encoded unresolved platform template; use the guide title and the other Web-labeled links for scope rather than copying that URL as a valid target. The v68 minimum is stated only in Sessions requirements on this page. The `/payments` table requires `shopperEmail` with the same 50-character limit; it lists `paymentMethod.issuer` as the shopper-selected bank's issuer ID **without a required mark**. TEST v72 examples show `paymentMethod.type: onlineBanking_PL` and issuer `141`, but an example does not make the issuer universally required. See raw lines 290–349.
- The Advanced example response has `resultCode: RedirectShopper` and a `redirect` action; this is a redirect step, not final payment confirmation. The guide says to check test payment status in Customer Area > Payments > Payment list and to submit a request for Online banking Poland in the **live** Customer Area before accepting live payments. The curl examples omit a continuation after `-X POST`, so they should not be treated as executable verbatim. See raw lines 657–679 and 50–69, 327–349.

## Detail locators

- Sessions prerequisites, email limit and TEST request examples: raw lines 25–268.
- Optional Sessions import and test/live instructions: raw lines 270–288.
- Advanced prerequisites, optional import and request table: raw lines 290–323.
- Advanced TEST payment requests: raw lines 325–655.
- Redirect response and repeated test/live instructions: raw lines 657–679.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-poland]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-poland/web-drop-in/2026-09-15|Fully read Online banking Poland Web Drop-in raw]]
