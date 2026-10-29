---
title: "Adyen MB WAY React Native Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mb-way/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/mb-way/react-native-component/2026-09-15.md"
tags: [adyen, mb-way, react-native, component, advanced-flow]
---

## Overview

This 2026-09-15-captured Adyen guide adds MB WAY to an **existing React Native Components Advanced** integration. Its Sessions section explicitly says React Native Components do not support Sessions flow. The guide covers the Advanced request fields, an await action while payment remains pending, and test/live setup. It is a method add-on, not a complete base integration or proof of live acceptance. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Flow boundary:** React Native Components Sessions flow is marked unavailable. For Advanced, the page requires an existing React Native Components integration, handling `action.type: await`, and MB WAY added in Customer Area. The integration-type link is labeled Components but selects `integration=Drop-in`; the nearby action and payment links select Components. Follow the intended Components base guide rather than treating that mismatched URL as the authority (raw lines 25–41).
- **Advanced request:** No extra MB WAY configuration parameters are specified. The `/payments` table marks `paymentMethod.type: mbway` and `paymentMethod.telephoneNumber` required; `shopperStatement` is listed without a required mark. The TEST v72 EUR example uses an HTTPS `returnUrl`; it is illustrative, and its curl snippet omits a shell continuation after `-X POST`. The example does not establish a minimum Checkout API version or the correct return path for a particular React Native app (raw lines 43–83).
- **Pending response:** The example returns `resultCode: Pending` and `action.type: await`; the action is used to show a waiting screen while the shopper completes payment in the MB WAY app. Pending is not final authorization (raw lines 85–102).
- **Test and live:** The page allows any test telephone number, illustrates `+351234567890`, and directs test payment status checks to test Customer Area. For `/payments` test responses, append `-c1` (Authorised/default), `-c3` (Pending), or `-c5` (Refused) to `shopperStatement`. Live acceptance requires adding MB WAY in live Customer Area; these instructions do not prove a live transaction (raw lines 104–123).

## Detail locators

- Add-on scope, Sessions unavailability and Advanced prerequisites: pinned raw lines 15–41.
- No extra configuration, required request fields, and TEST example: pinned raw lines 43–83.
- Pending/await response: pinned raw lines 85–102.
- Test suffixes and live Customer Area gate: pinned raw lines 104–123.

## Related

- [[source-adyen-docs-payment-methods-mb-way]] — separately captured MB WAY method overview.
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/mb-way/react-native-component/2026-09-15|MB WAY React Native Component guide, captured 2026-09-15]]
