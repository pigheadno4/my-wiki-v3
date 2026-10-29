---
title: "Adyen PayPo Android Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypo/android-component"
raw_files:
  - "adyen/docs/payment-methods/paypo/android-component/2026-09-15.md"
tags: [adyen, paypo, android, components, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds PayPo to an existing Android Components integration with either Sessions or Advanced server-side flow. It covers PayPo-specific request fields, the `InstantPaymentComponent`, redirect handling, capture, and test/live setup. Its PLN/PL requests are examples; this page does not establish current merchant eligibility or live acceptance. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions flow:** The page requires an existing Android Sessions Components integration, Checkout API v68 or later, and PayPo added in Customer Area. Its `/sessions` table marks `shopperName.firstName`, `shopperName.lastName`, and `shopperEmail` required; billing and delivery addresses are listed without a required mark (pinned raw lines 25–48).
- **Advanced flow:** The page requires an existing Android Advanced Components integration, handling the additional `action.type=redirect`, and PayPo added in Customer Area. Its `/payments` table marks `paymentMethod.type=paypo`, shopper name, and shopper email required, while billing and delivery addresses are listed without a required mark. The sample response is `RedirectShopper` with a redirect action, which is an additional step rather than evidence of final authorization (lines 521–529, 617–629, 1001–1015). The Advanced requirements table does not state the Sessions table's v68 minimum.
- **Android Component:** Both flows import `com.adyen.checkout:instant`, with `components-compose` added for Jetpack Compose. Both use `InstantPaymentComponent` and specify no PayPo-specific configuration parameters. Sessions retrieves `paypo` from the checkout session; Advanced selects that type from `/paymentMethods`. The Compose examples call for a unique Component key when resetting or using a different screen or payment session (lines 426–504, 531–614).
- **Payment and capture timing:** Before authorization, the guide says the offer/payment link remains available for up to 72 hours. Once the shopper accepts, status changes to `Authorised` and the shopper has 30 days to pay PayPo under its terms, measured from authorization. The merchant must capture after authorization; only a **full-amount capture** is possible. Automatic capture immediately after authorization can be configured when adding PayPo in the live Customer Area. The guide says the merchant is funded the full amount after capture without waiting for the shopper to pay PayPo; manual capture uses the original payment PSP reference at `/payments/{paymentPspReference}/captures` (lines 391–405, repeated at 1017–1031).
- **Test and live:** The test instructions give `firstName=name`, `lastName=surname`, `shopperEmail=shopper@example.com`, and verification code `123456` at the PayPo redirect. They route test status checks to Customer Area Payment list. Accepting live PayPo requires a request in the live Customer Area (lines 507–519, repeated at 1049–1061).

## Detail locators

- Sessions requirements and request field table: pinned raw lines 25–48; server language examples: lines 50–389.
- Sessions capture, imports, Component setup, and test/live: lines 391–519.
- Advanced requirements, imports, and Component setup: lines 521–614; `/payments` fields and server examples: lines 617–999.
- Advanced redirect response, capture, and test/live: lines 1001–1061.

## Related

- [[adyen-online-payments]] — provider online-payments concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypo/android-component/2026-09-15|PayPo Android Component guide, captured 2026-09-15]]
