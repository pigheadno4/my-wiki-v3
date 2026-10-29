---
title: "Adyen PayPo Web Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypo/web-component"
raw_files:
  - "adyen/docs/payment-methods/paypo/web-component/2026-09-15.md"
tags: [adyen, paypo, poland, web, components, redirect, capture]
---

## Overview

This [[adyen|Adyen]] guide, fetched and marked last modified 2026-09-15, adds **PayPo** to an existing **Web Components** integration, with separate Sessions and Advanced flow instructions. It covers request fields, Redirect Component setup, the PayPo offer/authorization/capture timeline, and test/live steps. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-paypo|PayPo overview]]. The TEST examples use PL/PLN; this captured guide does not establish current merchant eligibility or a completed transaction.

## Key takeaways

- **Flow prerequisites and fields:** Sessions requires an existing Web Components Sessions integration, Checkout API v68+, and PayPo added in Customer Area. Its `/sessions` table marks shopper first/last name and email required; billing and delivery addresses are optional. Advanced requires an existing Web Components Advanced integration, redirect action handling and Customer Area setup. Its `/payments` table adds required `paymentMethod.type: paypo` and likewise requires shopper name/email, with addresses optional. TEST examples show `/sessions` v71 and `/payments` v72 for PL/PLN.
- **Redirect Component:** Import `Redirect` from Adyen Web; the guide says no PayPo-specific configuration parameters are required. Both flows show a `Redirect` Component mounted in a container. The Advanced response has `resultCode: RedirectShopper` and `action.type: redirect`, which is a next action rather than payment completion.
- **Offer, authorization and capture:** Before authorization, the PayPo offer/payment link remains usable for **up to 72 hours**. Once the shopper accepts, status becomes **Authorised** and the shopper's **30-day PayPo payment period starts at authorization**, not capture. After authorization the merchant captures the payment, and **only the full authorized amount can be captured**. Automatic capture can be configured to execute immediately after authorization when PayPo is added in the live Customer Area; otherwise the guide shows a `/payments/{paymentPspReference}/captures` request using the original PSP reference. It says the merchant need not wait for the shopper's later repayment to PayPo to be funded after capture; this is source-described funding behavior, not proof of actual settlement for a transaction.
- **Sample and live caveats:** The Sessions example uses `adyencheckout://your.package.name`, an app-style `returnUrl` in a Web guide; the Advanced example uses an HTTPS URL. Configure a Web return path appropriate to the deployed flow. The two request curl samples omit a continuation before `-d`. The Component snippets use unquoted `type:paypo`; unless a `paypo` variable exists, that is not a copy-ready JavaScript literal. Testing lists sample shopper values and verification code 123456; the page says to check test payments in test Customer Area. Live acceptance needs a separate PayPo request in live Customer Area. No method-specific refund procedure is provided here.

## Detail locators

- Scope, Sessions prerequisites and `/sessions` field table: pinned raw lines 15–48. Sessions TEST v71 request and SDK variants: lines 50–389.
- Sessions capture lifecycle: lines 391–420. Redirect import, config and initialization: lines 423–450; Sessions TEST/live steps: lines 453–465.
- Advanced prerequisites and Redirect initialization: lines 467–499. Advanced `/payments` fields and TEST v72 examples: lines 501–883; redirect response: lines 885–899. Repeated capture and test/live instructions: lines 901–945.

## Related

- [[adyen-online-payments]] — provider integration concept
- [[source-adyen-docs-payment-methods-paypo]] — method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypo/web-component/2026-09-15|PayPo Web Component guide, fetched 2026-09-15]]
