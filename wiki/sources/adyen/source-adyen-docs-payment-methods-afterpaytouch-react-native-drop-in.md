---
title: "Adyen Afterpay React Native Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/afterpaytouch/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/afterpaytouch/react-native-drop-in/2026-09-15.md"
tags: [adyen, afterpay, react-native, drop-in, redirect, capture]
---

## Overview

This Adyen Docs guide, captured 2026-09-15, describes **Afterpay-specific additions to an existing React Native Drop-in** integration. It has separate Sessions and Advanced server-flow paths; both require Customer Area setup and redirect handling. It does not itself prove merchant enablement, shopper approval, a completed redirect, capture or live payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The Sessions path requires Checkout API v68 or later, an existing Sessions React Native Drop-in, and handling of `action.type: redirect`. Its `/sessions` table marks shopper name, email, unique reference (minimum three characters), country code, billing and delivery addresses, and `lineItems` required; telephone number is optional. The Advanced `/payments` path marks the same data required plus `paymentMethod: afterpaytouch`, again with optional phone. The guide says no extra Afterpay Drop-in configuration parameters are needed (pinned raw lines 25–53, 739–743, 789–824, 1538–1552).
- The example requests use AU/AUD and test endpoints; they are examples of one region, not a region-wide eligibility matrix or a live result. The Advanced example's redirect action has `resultCode: RedirectShopper`, which requires the existing redirect handling rather than proving authorization (lines 55–113, 827–888, 1538–1552).
- Depending on merchant-account configuration, capture is automatic after authorization or manual. Capture after shipment needs a delay or manual capture; partial capture needs manual capture. The page says capture within 13 days after authorization. The first installment is charged during authorization; if the payment is not captured by the 13-day limit, Afterpay cancels it and refunds that installment. Test authorizations expire after one day, so manual test capture has that shorter limit (lines 747–755, 1554–1562).
- A manual `/payments/{paymentPspReference}/captures` request specifies the full or partial `amount.value`; `lineItems` is optional. An initial partial capture cancels the unclaimed remainder unless the account is enabled for multiple partial captures. Multiple partial captures require Support setup and create a new invoice for each capture (lines 757–766, 1564–1573).
- Testing requires an Afterpay sandbox shopper account; separate accounts are specified for each tested region. The guide lists AU, NZ, US and CA sandbox selection, test-card CVV scenarios, and a live Customer Area request. These sandbox choices and test outcomes do not establish which regional product is available to a particular live merchant (lines 768–787, 1575–1594).

> [!warning] Sessions requirement link mismatch
> The Sessions requirements table says to have a Sessions React Native Drop-in integration, but its integration-type link points to an **Advanced-flow** URL (raw line 33). The neighboring redirect-handling link points to Sessions (line 35). Follow the flow named in the requirement and verify the linked base guide before implementing.

## Detail locators

- Sessions prerequisite, required fields, samples and no-extra-configuration statement: pinned raw lines 25–743.
- Sessions capture and testing sections: lines 745–787. Advanced prerequisite, request fields and examples: lines 789–1552.
- Advanced capture, partial-capture effects and test/live section: lines 1554–1594.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-afterpaytouch]] — Afterpay regional method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/afterpaytouch/react-native-drop-in/2026-09-15|Afterpay React Native Drop-in guide, captured 2026-09-15]]
