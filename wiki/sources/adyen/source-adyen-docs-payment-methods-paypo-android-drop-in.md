---
title: "Adyen PayPo Android Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypo/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paypo/android-drop-in/2026-09-15.md"
tags: [adyen, paypo, android, drop-in, redirect]
---

## Overview

This captured [[adyen]] guide adds PayPo to an existing Android Drop-in integration. It covers method-specific Sessions and Advanced server-flow additions, redirect handling, capture, and test/live setup; the base Android integration supplies the general flow. The PL/PLN requests and test responses are examples, not proof of current merchant eligibility or a completed live payment. [[adyen-online-payments]]

## Key takeaways

- **Sessions flow:** The page requires an existing Android Drop-in Sessions integration, Checkout API v68 or later, and PayPo added in Customer Area. For `/sessions`, its table marks `shopperName` (first and last name) and `shopperEmail` required; `billingAddress` and `deliveryAddress` have no required mark. The example uses `countryCode: PL`, PLN 1000 minor units and an `adyencheckout://` app-scheme `returnUrl` (pinned raw lines 25–74).
- **Advanced flow:** The page requires an existing Android Drop-in Advanced integration configured to handle a `redirect` action and PayPo added in Customer Area. Its requirements row does not state the Sessions row's Checkout API minimum. For `/payments`, the table marks `paymentMethod.type: paypo`, shopper name and shopper email required; the two address fields have no required mark. The sample response is `RedirectShopper` with `action.type: redirect`, an additional shopper step rather than final authorization (lines 444–472, 844–858).
- **Drop-in configuration and return examples:** Neither flow needs additional PayPo-specific Drop-in configuration. The Sessions request example uses an app-scheme `returnUrl`, whereas the Advanced request example uses an HTTPS `returnUrl`; they are examples for their respective sections, not a universal Android return recipe. Follow the linked base integration for platform return handling (lines 65, 424–426, 456–458, 493).
- **Authorization, term and capture:** Before authorization, the offer/payment link is available for up to 72 hours. When the shopper accepts, status changes to `Authorised` and the shopper has 30 days to pay PayPo under its terms, starting at authorization rather than capture. The merchant must capture after authorization, and only the full authorized amount can be captured. Automatic capture immediately after authorization can be configured when adding PayPo in the live Customer Area. The guide says the merchant is funded the full amount after capture without waiting for the shopper's payment to PayPo; manual capture uses the original payment PSP reference at `/payments/{paymentPspReference}/captures` (lines 390–420, 860–890).
- **Test and live:** The test values are `firstName=name`, `lastName=surname`, `shopperEmail=shopper@example.com`, and verification code `123456` at PayPo redirect. The guide sends test-status checks to Customer Area Payment list and requires a request for PayPo in the live Customer Area before accepting live payments (lines 430–442, 892–904).
- **Source sample caveat:** Both payment curl examples put `-X POST` on a line without a shell continuation before `-d`; they are not copy-ready as printed (lines 53–74, 478–501).

## Detail locators

- Identity and Sessions prerequisites/field table: pinned raw lines 15–48; language-specific Sessions request examples: lines 49–388.
- Sessions capture, configuration and test/live: lines 390–442.
- Advanced prerequisites and payment field table: lines 444–472; language-specific payment examples: lines 474–842.
- Advanced redirect response, capture and test/live: lines 844–904.

## Related

- [[adyen-online-payments]] — provider online-payments architecture and method routes.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypo/android-drop-in/2026-09-15|PayPo Android Drop-in guide, captured 2026-09-15]]
