---
title: "Adyen PayPo iOS Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypo/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paypo/ios-drop-in/2026-09-15.md"
tags: [adyen, paypo, ios, drop-in, poland, redirect, capture]
---

## Overview

This [[adyen|Adyen]] guide, fetched and marked last modified 2026-09-15, adds **PayPo** to an existing **iOS Drop-in** integration with separate Sessions and Advanced-flow instructions. It documents method-specific request fields, redirect action handling, the PayPo offer/authorization/capture timeline and test/live setup. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-paypo|PayPo overview]]. The TEST examples use PL/PLN; this snapshot does not prove current merchant eligibility or payment completion.

## Key takeaways

- **Sessions and Advanced setup:** Sessions requires existing iOS Drop-in Sessions, Checkout API v68 or later, and PayPo added in Customer Area. Its `/sessions` table marks shopper first/last name and email required, with billing and delivery addresses optional. Advanced requires existing iOS Drop-in Advanced, redirect action handling and PayPo setup; its `/payments` table also requires `paymentMethod.type: paypo`, shopper name and email, with addresses optional. Neither flow adds PayPo-specific Drop-in configuration.
- **Redirect and return:** The Sessions TEST v71 example uses PL/PLN and `adyencheckout://your.package.name` as an illustrative iOS app-scheme `returnUrl`. The Advanced TEST v72 `/payments` example uses PL/PLN and an HTTPS website `returnUrl`; that placeholder is not automatically appropriate for an iOS app and the actual return flow must be configured. Advanced `/payments` responds with `resultCode: RedirectShopper` and `action.type: redirect`; it is a next action, not authorization/capture proof. Both curl request snippets omit a shell continuation before `-d` and are not copy-ready.
- **PayPo time and capture:** Before authorization, the offer/payment link is available **up to 72 hours**. Shopper acceptance changes status to **Authorised**, and the shopper's **30-day PayPo payment period begins at authorization**, not capture. The merchant must capture after authorization and can capture **only the full authorized amount**. Automatic capture can be configured for immediate post-authorization execution when adding PayPo in the live Customer Area. For manual capture, the example calls `/payments/{paymentPspReference}/captures` with the original payment PSP reference. The page says merchant funding follows capture without waiting for the shopper's repayment to PayPo; this describes the method, not a proven settlement event for a particular payment.
- **Testing and live:** In TEST, the page gives sample name/email values and verification code 123456 for the PayPo redirect, then directs status checks in Adyen test Customer Area. Accepting live PayPo payments requires a separate request in the **live** Customer Area. The guide does not supply a method-specific refund procedure.

## Detail locators

- Scope, Sessions prerequisites and fields: pinned raw lines 15–47. TEST v71 Sessions examples: lines 49–388. Sessions offer, capture and configuration: lines 390–426; TEST/live steps: lines 428–442.
- Advanced prerequisites/configuration and `/payments` fields: lines 444–474. TEST v72 request examples: lines 476–844; redirect response: lines 846–860. Repeated capture and TEST/live instructions: lines 862–908.

## Related

- [[adyen-online-payments]] — provider integration concept
- [[source-adyen-docs-payment-methods-paypo]] — method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypo/ios-drop-in/2026-09-15|PayPo iOS Drop-in guide, fetched 2026-09-15]]
