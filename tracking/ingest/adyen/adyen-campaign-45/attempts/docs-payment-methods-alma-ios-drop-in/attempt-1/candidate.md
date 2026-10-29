---
title: "Alma iOS Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alma/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alma/ios-drop-in/2026-09-15.md"
tags: [adyen, alma, ios, drop-in, redirect, installments]
---

## Overview

This 2026-09-15-captured [[adyen]] guide adds **Alma** to an existing **iOS Drop-in** integration. It separates Sessions and Advanced server-flow additions, covering optional request fields, Advanced installment choice, a redirect action and test/live routes. The linked [[source-adyen-docs-payment-methods-alma]] overview scopes the captured product to FR/EUR and three or four installments. This guide's TEST examples do not prove current merchant eligibility, a completed redirect, final payment or capture. See [[adyen-online-payments]].

## Key takeaways

- **Sessions prerequisites:** The Sessions section requires an existing iOS Drop-in Sessions integration, Checkout API **v68 or later**, and Alma added in Customer Area (raw lines 25–34). Its `/sessions` table lists `telephoneNumber`, `shopperEmail`, `billingAddress` and `deliveryAddress` with **blank Required cells**; do not infer they are mandatory because the example includes them (raw lines 36–47).
- **Sessions TEST example and return URL:** The sample uses TEST `/v71/sessions`, FR/EUR and an iOS app-scheme `returnUrl` placeholder, `adyencheckout://your.package.name` (raw lines 49–83). Its curl command puts `-X POST` and `-d` on separate lines without a continuation, so it illustrates request content rather than a verified copy-ready shell command (raw lines 51–57). The page says no additional Alma-specific Drop-in configuration parameters are needed (raw lines 85–89).
- **Advanced prerequisites and request:** The Advanced section requires an existing iOS Drop-in Advanced integration, handling the additional `action.type: redirect` action, and Alma added in Customer Area (raw lines 99–109). It also says no additional method configuration is needed (raw lines 111–115). Its `/payments` table leaves the same shopper/contact/address fields optional and lists `additionalData.alma.installments_count` as optional: set `3` or `4` to fix the number of installments, or omit it for shopper choice (raw lines 117–129).
- **Advanced TEST example and action:** The sample uses TEST `/v72/payments`, FR/EUR, `shopperLocale: en-US`, an HTTPS `returnUrl`, and `alma.installments_count: 4` (raw lines 131–169). The example's `-X POST` and `-d` also lack a shell continuation (raw lines 133–139). The Sessions app-scheme URL and Advanced HTTPS URL are both examples; the page does not reconcile their return handling for an actual iOS app. Its `RedirectShopper`/`action.type: redirect` response is an intermediate action, not final authorization (raw lines 171–185).
- **Test/live boundary:** The page points to test payment status in Customer Area and says to submit an Alma request in live Customer Area before accepting live payments (raw lines 91–97, 187–193). It does not define capture, refund or asynchronous final-result behavior. The linked overview's feature matrix is method-level navigation, not this guide's modification procedure; verify the selected base flow for return and outcome handling.

## Detail locators

- Sessions requirements and optional `/sessions` fields: pinned raw lines 25–47.
- Sessions TEST example, app-scheme return URL and malformed curl continuation: pinned raw lines 49–83.
- Sessions no-extra-config and test/live instructions: pinned raw lines 85–97.
- Advanced prerequisites, no-extra-config and optional installment selector: pinned raw lines 99–129.
- Advanced TEST example, HTTPS return URL, malformed curl continuation and redirect action: pinned raw lines 131–185.
- Advanced test/live request: pinned raw lines 187–193.

## Related

- [[adyen-online-payments]] — provider online checkout context.
- [[source-adyen-docs-payment-methods-alma]] — FR/EUR method overview and capability matrix.

## Raw Sources

- [[raw/adyen/docs/payment-methods/alma/ios-drop-in/2026-09-15|Alma iOS Drop-in guide, captured 2026-09-15]]
