---
title: "PaySafeCard React Native Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paysafecard/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paysafecard/react-native-drop-in/2026-09-15.md"
tags: [adyen, paysafecard, react-native, drop-in, redirect, prepaid]
---

## Overview

This 2026-09-15-captured Adyen guide adds PaySafeCard to an **existing React Native Drop-in** integration. It separates Sessions and Advanced server-side flows, covers a method-specific shopperReference addition, redirect handling, no extra Drop-in configuration and test/live setup. It is an add-on, not a complete base integration or evidence of current entitlement, a successful payment or regulatory compliance. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** the guide lists an existing React Native Drop-in Sessions integration, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and PaySafeCard in Customer Area. Its Sessions integration-type link points to an **Advanced-flow URL**, while the create-session/redirect links point to Sessions; use the flow heading and matching base guide rather than treating the mismatched link as flow authority (raw lines 25–42).
- Add `shopperReference`, a merchant reference uniquely identifying the shopper, to `/sessions`; the table marks it required. The v71 sample uses NL/EUR and an app-scheme returnUrl as examples. Some SDK snippets omit the constructed request object, so they are not a standalone recipe (raw lines 40–69, 71–267).
- **Advanced:** an existing Advanced React Native Drop-in with redirect handling and Customer Area method setup is listed. Add required `shopperReference` to `/payments`. The v72 examples use EUR and an HTTPS returnUrl, but **omit `paymentMethod` entirely**; the response example identifies `paysafecard`. Do not copy those abbreviated requests as complete method-selection examples or infer the method type from their omission (raw lines 286–333, 599–613).
- The guide says no PaySafeCard-specific configuration parameters are needed in either flow (raw lines 270–274, 298–302). It gives a 16-digit test code and says Support must add PaySafeCard in **live Customer Area** before live acceptance (raw lines 276–284, 615–623). The code and example response are test material, not live proof.
- The separate [[source-adyen-docs-payment-methods-paysafecard|PaySafeCard method overview]] describes a conditional Customer Data Exchange option for EU countries **where gambling-customer KYC is required**; it says the feature can prevent acquiring funds from an anonymous shopper (overview pinned raw lines 29–31). This is method-level context, not an extra parameter stated by this React Native child guide or a blanket KYC/compliance guarantee.

## Detail locators

- Add-on scope, Sessions requirements and shopperReference: raw lines 15–46; Sessions request examples at lines 48–268.
- Sessions no-extra-configuration and test/live gate: raw lines 270–284.
- Advanced requirements, shopperReference and abbreviated requests: raw lines 286–333 and 336–597; redirect response example lines 599–613.
- Advanced test/live gate: raw lines 615–623.
- Separate method-level conditional CDE scope: [[source-adyen-docs-payment-methods-paysafecard]] and its pinned raw lines 29–31; the child raw_files entry remains child-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paysafecard]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paysafecard/react-native-drop-in/2026-09-15|PaySafeCard React Native Drop-in guide, captured 2026-09-15]]
