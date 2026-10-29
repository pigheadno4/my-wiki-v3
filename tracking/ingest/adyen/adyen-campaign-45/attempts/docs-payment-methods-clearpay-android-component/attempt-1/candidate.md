---
title: "Clearpay Android Component | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/clearpay/android-component"
raw_files:
  - "adyen/docs/payment-methods/clearpay/android-component/2026-09-15.md"
tags: [adyen, clearpay, android, components, redirect]
---

## Overview

This 2026-09-15 Adyen Docs page adds **Clearpay** to an existing Android Components integration with separate Sessions and Advanced server-side flows. Clearpay is the UK-branded method in the linked overview, whose matrix lists **GB/GBP**; this child uses GB/GBP TEST examples rather than establishing a particular merchant's eligibility. See [[adyen-online-payments]], [[source-adyen-docs-payment-methods-clearpay]] and [[adyen]].

## Key takeaways

- Sessions requires an existing Android Components Sessions flow, **Checkout API v68 or later**, redirect handling and Clearpay added in Customer Area (raw lines 25–36). Its `/sessions` table marks shopper name/email/reference (reference minimum three characters), country code, billing/delivery addresses and line items required; phone is optional (lines 40–53). The GB/GBP v71 TEST curl request is illustrative; its `-X POST` line lacks a continuation before `-d`, so do not assume the literal shell block runs unchanged (lines 55–114).
- Both flows import `com.adyen.checkout:instant`; the Compose variant also imports `components-compose`. The page says no additional Clearpay configuration parameters are needed. Both use `InstantPaymentComponent`: Sessions gets method `clearpay` from the checkout session; Advanced finds `clearpay` in `/paymentMethods`. Compose examples call for a new key when a different screen/payment session needs a new Component or when resetting (Sessions lines 116–198; Advanced lines 297–381).
- Advanced requires an existing Android Components Advanced flow, redirect action handling and Clearpay added in Customer Area (lines 287–295). Its `/payments` table marks the same shopper/country/address/item data required, with optional phone (lines 383–398); the GB/GBP v72 request example sets `paymentMethod.type: clearpay` (lines 400–462). That curl block also puts `-X POST` before `-d` without a line continuation. The example response is `RedirectShopper` with a redirect action (lines 464–478), not final authorisation or capture proof. Follow the linked base flow for returned-shopper handling and outcome.
- Capture can be automatic after authorisation or manual, according to merchant-account configuration. Delayed capture needs delay setup or manual capture; partial capture needs manual capture. Clearpay requires capture within **13 days** after authorisation, or it cancels and refunds the first instalment charged during authorisation; test authorisations expire in **one day** (Sessions lines 200–210; Advanced lines 480–490). Partial manual capture cancels the unclaimed remainder unless the account is enabled for **multiple partial captures**, which requires Support setup and creates a new invoice per capture (lines 212–221 and 492–501).
- Before capture, cancel; after capture, refund to return funds. Full or partial refunds use `amount.value`, with `lineItems` optional in the refund request (lines 223–232 and 503–512). The discounts section says to include a negative amount in the payment request, but its prose says **£1** off Item #2 while the example gives a discount line of quantity **2** at **-100** minor units and reduces the order amount from 1000 to 800; the shown JSON also omits a comma between the second item and discount object (lines 234–268; repeated 514–548). Treat that example as inconsistent, not copy-ready or a universal discount rule.
- Testing requires a Clearpay sandbox and shopper account, with separate sandbox environments/details by country/region. The page links Clearpay test-account/card documentation; in sandbox Adyen is displayed as merchant. It says a request in live Customer Area is needed before accepting live Clearpay payments (lines 270–285 and 550–565). A sandbox result does not establish live enablement, successful capture, refund or settlement.

## Detail locators

- Page scope and Sessions requirements: raw lines 15–36.
- Sessions request fields and GB/GBP v71 TEST example: lines 40–114; curl continuation issue at lines 58–63.
- Sessions Component setup, capture, refunds/cancellations, discounts and sandbox/live: lines 116–285.
- Advanced requirements, Component setup and request table/example: lines 287–462; curl continuation issue at lines 403–408.
- Advanced redirect response, capture, refunds/cancellations, discounts and sandbox/live: lines 464–565.
- Discount prose/example mismatch and malformed JSON: lines 236–268 and 516–548.
- Linked overview's UK/GBP/branding scope: `raw/adyen/docs/payment-methods/clearpay/2026-09-15.md` lines 23–31.

## Related

- [[adyen-online-payments]] — provider online-payment architecture.
- [[source-adyen-docs-payment-methods-clearpay]] — UK product and GB/GBP matrix.

## Raw Sources

- [[raw/adyen/docs/payment-methods/clearpay/android-component/2026-09-15|2026-09-15 Clearpay Android Component Sessions and Advanced guide]]
