---
title: "Adyen Clearpay Android Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/clearpay/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/clearpay/android-drop-in/2026-09-15.md"
tags: [adyen, clearpay, android, drop-in, buy-now-pay-later, online-payments]
---

## Overview

This captured [[adyen]] guide adds Clearpay to an **existing Android Drop-in** integration, with separate Sessions and Advanced server-side flow instructions. It describes shopper and order request fields, a redirect action, capture/partial-capture behavior, cancellation versus refund, discounts, and test/live setup. The GB/GBP payloads illustrate requests and do not prove merchant enablement or a completed payment. [[adyen-online-payments]]

## Key takeaways

- **Flow prerequisites:** Sessions requires an existing Android Drop-in Sessions integration with Checkout API v68 or later and Clearpay added in Customer Area. Advanced requires an existing Android Drop-in Advanced integration, handling `action.type: redirect`, and Clearpay added in Customer Area. Its requirements table does not restate the Sessions API minimum (raw lines 25–34, 213–221).
- **Fields and configuration:** Both flow tables mark `shopperName`, `shopperEmail`, `shopperReference` (minimum three characters), `countryCode`, `billingAddress`, `deliveryAddress` and `lineItems` required; `telephoneNumber` appears if provided. Both sections say no additional Clearpay Drop-in configuration is needed. The Advanced table omits `paymentMethod`, but its `/payments` example includes `paymentMethod.type: clearpay`; preserve this table/example distinction (raw lines 38–51, 114–118, 225–256).
- **Redirect boundary:** The Advanced response example has `resultCode: RedirectShopper` and `action.type: redirect`. That is an intermediate shopper action, not proof of authorization, capture or settlement (raw lines 310–324).
- **Capture and partial capture:** Capture can be automatic or manual depending on account configuration, and partial capture requires manual capture. Clearpay must be captured within 13 days after authorization; the guide says the first installment is charged during authorization, and an uncaptured payment past that window is cancelled with the first installment refunded. Test authorizations expire in one day. An unclaimed remainder after partial capture is normally cancelled unless the account has multiple partial captures enabled through Support; this mode creates a new invoice per capture (raw lines 122–141; repeated at 328–347).
- **Cancellation, refund and discounts:** An uncaptured payment can be cancelled; returning funds after capture uses refund. Full or partial refund requests specify `amount.value` and can include `lineItems`. The discount prose instructs a negative amount added to original price, and its “1 GBP on Item #2” illustration uses a negative line item. The shown payload contains `...` and lacks a comma between item objects, so it is illustrative and not copy-ready JSON (raw lines 143–192; repeated at 349–394).
- **Sandbox/live gates:** Testing requires Clearpay's sandbox and a test shopper account; the page says sandbox environments/details vary by country or region and Adyen appears as sandbox merchant name. It says a request for Clearpay in live Customer Area is needed before live acceptance (raw lines 194–211; repeated at 396–411).

## Detail locators

- Identity, Sessions prerequisites and request field table: pinned raw lines 15–51.
- Sessions example, no-extra-configuration and lifecycle/test sections: pinned raw lines 53–211.
- Advanced prerequisites, field table/example and redirect response: pinned raw lines 213–324.
- Advanced capture, refund/cancel, discount and test/live sections: pinned raw lines 326–411.

## Related

- [[adyen-online-payments]] — online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-clearpay]] — Clearpay regional/method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/clearpay/android-drop-in/2026-09-15|Clearpay Android Drop-in, captured 2026-09-15]]
