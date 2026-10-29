---
title: "Clearpay Web Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/clearpay/web-component"
raw_files:
  - "adyen/docs/payment-methods/clearpay/web-component/2026-09-15.md"
tags: [adyen, clearpay, web, components, redirect, capture]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] guide adds Clearpay to an existing Web Components integration through Sessions or Advanced flow. It covers request fields, Redirect Component setup, capture/refund behavior and test/live setup. See [[adyen-online-payments]]. Its GB/GBP TEST examples and sandbox instructions do not prove current merchant eligibility or a completed payment.

## Key takeaways

- Sessions requires an existing Web Components Sessions integration, Checkout API v68 or later, redirect handling and Clearpay added in Customer Area. Advanced requires the corresponding Advanced integration, redirect handling and Customer Area setup. The `/sessions` TEST example uses Checkout API v71 with GB/GBP; `/payments` uses v72 and `paymentMethod.type: clearpay`. These are examples, not a full country support matrix.
- Both endpoint tables mark shopper name/email/reference, country code, billing/delivery address and `lineItems` required; telephone number is optional. Import Adyen Web with `Redirect` and initialize that class for Clearpay. The page says no extra Clearpay configuration parameters are needed. Its JS example writes `{ type:clearpay }` without quoting or defining `clearpay`; treat it as illustrative rather than verified runnable code.
- Advanced shows a `RedirectShopper` response with `action.type: redirect`, which calls for the existing redirect handler; it does not establish return processing or final authorization.
- Capture can occur automatically or manually under merchant configuration. To capture after goods are sent, configure a delay or manual capture; partial capture requires manual capture. Capture within 13 days of authorisation or Clearpay cancels and refunds the first installment charged at authorization. TEST authorization expires in one day. An unclaimed remainder after partial capture is cancelled unless multiple partial captures are enabled through Support; each capture then creates a new invoice. Cancel before capture, refund after capture.
- The discount section describes a negative line-item amount, but the shown JSON is abbreviated and not a complete validated request. Testing uses a Clearpay sandbox shopper account and regional test details; live acceptance requires requesting Clearpay in live Customer Area.

## Detail locators

- Sessions prerequisites, fields and GB/GBP v71 example: pinned raw lines 25–114. Import, no-extra-config and Redirect initialization: lines 116–144. Sessions capture, refund, discount and test/live: lines 146–231.
- Advanced prerequisites, import/init, fields, GB/GBP v72 example and redirect response: lines 233–362. Repeated capture/refund/discount and test/live guidance: lines 364–449.

## Related

- [[adyen-online-payments]] — provider integration concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/clearpay/web-component/2026-09-15|Clearpay Web Component guide, captured 2026-09-15]]
