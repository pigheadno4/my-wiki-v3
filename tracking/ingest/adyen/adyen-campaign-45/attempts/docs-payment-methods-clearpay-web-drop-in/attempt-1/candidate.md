---
title: "Clearpay Web Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/clearpay/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/clearpay/web-drop-in/2026-09-15.md"
tags: [adyen, clearpay, web, drop-in, redirect, capture]
---

## Overview

This 2026-09-15-captured [[adyen]] guide adds **Clearpay** to an existing **Web Drop-in** integration, with separate Sessions and Advanced server flows. It contains method-specific request, capture, refund and test instructions, not a full base integration or evidence of current enablement. The linked [[source-adyen-docs-payment-methods-clearpay]] overview scopes this product to GB/GBP, distinguishes regional Afterpay names and marks recurring unavailable. This guide's GB/GBP TEST examples do not prove merchant or shopper eligibility. See [[adyen-online-payments]].

## Key takeaways

- **Sessions prerequisites and request:** The guide requires existing Web Drop-in Sessions flow, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and Clearpay added in Customer Area (raw lines 25–36). Its `/sessions` table marks `shopperName`, `shopperEmail`, `shopperReference` (minimum three characters), `countryCode`, `billingAddress`, `deliveryAddress` and `lineItems` required; `telephoneNumber` is optional if provided (raw lines 38–53). The example uses TEST `/v71/sessions`, GB/GBP and placeholder credentials. Its curl command puts `-X POST` and `-d` on separate lines without continuation, so it should not be copied as a verified working command (raw lines 55–114).
- **Advanced prerequisites and request:** Advanced requires existing Web Drop-in Advanced flow, redirect handling and Customer Area method setup. Its integration prerequisite URL contains an unresolved encoded `{{getParameter('platform')}}` template rather than `platform=Web`; the surrounding Advanced redirect/payment links name Web (raw lines 221–249). The `/payments` table lists the same required shopper, country, address and item fields with optional telephone; the example adds `paymentMethod.type: clearpay` and uses TEST `/v72/payments` with GB/GBP (raw lines 251–324). This curl example also splits `-X POST` from `-d` without continuation (raw lines 264–270). Its `RedirectShopper`/`action.type: redirect` response is a redirect step, not final authorisation or capture (raw lines 326–340).
- **Optional Web import:** If importing payment methods individually for tree shaking, the page says include `Redirect`; this is optional performance-oriented import guidance, not a payment prerequisite (raw lines 116–126, 233–243).
- **Capture deadline and first installment:** Capture is automatic after authorisation or manual depending on merchant-account configuration. Capture delay or manual capture is needed to capture after shipment; partial capture requires **manual** capture. The page says capture within **13 days** after authorisation; the first installment is charged at authorisation, and if uncaptured by that deadline Clearpay cancels and refunds it. In TEST, authorisations expire in **one day**, requiring manual test capture within that day (raw lines 128–138, 342–352).
- **Partial capture and refunds:** Manual `/payments/{paymentPspReference}/captures` specifies full or partial `amount.value` and optional `lineItems`. An initial partial capture normally cancels unclaimed balance; for an account enabled for **multiple partial captures**, it remains. Setup requires Support and each such capture creates a new invoice (raw lines 140–149, 354–363). An uncaptured payment may be cancelled; a captured payment needs refund to return funds. Full/partial refund uses `/payments/{paymentPspReference}/refunds` with `amount.value` and optional `lineItems` (raw lines 151–162, 365–376).
- **Discount example warning:** The page says discounts use a negative amount and illustrates a GBP 1 discount on Item #2. The displayed JSON lacks a comma between the second item and the discount item, so it is not copyable as valid JSON; use its intent and verified fields rather than treating it as a runnable request (raw lines 164–200, 378–414).
- **Testing and live gate:** Clearpay sandbox and a test shopper account are described; the page points to separate sandbox details by country/region and says Adyen appears as merchant name in sandbox (raw lines 202–217, 416–431). Before live acceptance, it says to submit a Clearpay request in live Customer Area (raw lines 219, 433). The captured page does not demonstrate that such a request was approved or a live payment completed.

## Detail locators

- Sessions requirements, fields and example: pinned raw lines 25–114.
- Optional Redirect import, capture, refund, discount and test/live sections: pinned raw lines 116–219.
- Advanced requirements, unresolved template URL, fields, example and redirect action: pinned raw lines 221–340.
- Advanced capture, refund, discount and test/live sections: pinned raw lines 342–433.

## Related

- [[adyen-online-payments]] — provider checkout architecture.
- [[source-adyen-docs-payment-methods-clearpay]] — GB/GBP product scope, feature matrix and regional naming.

## Raw Sources

- [[raw/adyen/docs/payment-methods/clearpay/web-drop-in/2026-09-15|Clearpay Web Drop-in guide, captured 2026-09-15]]
