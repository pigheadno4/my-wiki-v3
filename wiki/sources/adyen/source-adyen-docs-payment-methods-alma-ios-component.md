---
title: "Adyen Alma iOS Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alma/ios-component"
raw_files:
  - "adyen/docs/payment-methods/alma/ios-component/2026-09-15.md"
tags: [adyen, alma, ios, components, online-payments, installments]
---

## Overview

This captured [[adyen]] guide describes adding Alma to an **existing iOS Components** integration. It separates Sessions and Advanced server-side flows, gives method-specific request additions and `InstantPaymentComponent` examples, and points to Customer Area setup and test/live steps. The FR/EUR requests and redirect response are examples, not proof of merchant enablement or a completed payment. [[adyen-online-payments]]

## Key takeaways

- **Flow prerequisites:** Sessions requires an existing iOS Components Sessions integration, Checkout API v68 or later, and Alma added in Customer Area. Advanced requires an existing iOS Components Advanced integration, handling an additional `redirect` action, and Alma added in Customer Area. Its link labelled “iOS Components integration” points to an `integration=Drop-in` URL, while its action and payment links point to Components; preserve the label/target mismatch rather than changing the page's Components scope (raw lines 25–35, 120–130).
- **Request additions and requiredness:** The Sessions `/sessions` table lists `telephoneNumber`, `shopperEmail`, `billingAddress` and `deliveryAddress`; its Required column is blank for these fields. The Advanced `/payments` table repeats them with blank Required cells and adds optional `additionalData.alma.installments_count`: set it to `3` or `4` to determine installment count, or omit it to let the shopper choose. Do not promote these blank cells to required fields. The examples use FR/EUR but do not define current eligibility (raw lines 39–83, 161–210).
- **Component setup:** Both flows say no additional Alma configuration parameters are needed and use `InstantPaymentComponent` after looking up `.other("alma")`. The Sessions sample assigns `session` as delegate; the Advanced sample assigns `self`. Both call `initiatePayment()` (raw lines 86–112, 132–157).
- **Redirect and return example:** The Advanced response example has `resultCode: RedirectShopper` and `action.type: redirect`, an intermediate action rather than successful authorization or settlement. The Sessions request example uses a custom-scheme `returnUrl`, while the Advanced example uses an HTTPS return URL; these are example values, not a rule that those flows require different URL schemes (raw lines 64–65, 186–190, 213–227).
- **Curl sample caveat:** Both TEST curl examples put `-X POST` on a line without a shell continuation before the following `-d` line. As written, the literal Sessions and Advanced snippets are not copy-ready requests (raw lines 57–58 and 180–181).
- **Test/live gate:** The guide points to Customer Area to check test-payment status and says to submit an Alma request in live Customer Area before accepting live Alma payments (raw lines 114–118, 229–233).

## Detail locators

- Guide identity and Sessions requirements: pinned raw lines 15–35.
- Sessions field table, FR/EUR sample, no-extra-config and component initialization: pinned raw lines 37–112.
- Advanced requirements, base-link mismatch and initialization: pinned raw lines 120–157.
- Advanced optional fields/installment selector, example and redirect response: pinned raw lines 159–227.
- Test status and live request: pinned raw lines 114–118 and 229–233.

## Related

- [[adyen-online-payments]] — online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-alma]] — Alma product/region overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/alma/ios-component/2026-09-15|Alma iOS Component, captured 2026-09-15]]
