---
title: "Adyen Afterpay React Native Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/afterpaytouch/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/afterpaytouch/react-native-component/2026-09-15.md"
tags: [adyen, afterpay, afterpaytouch, react-native, components, online-payments]
---

## Overview

This captured [[adyen]] guide describes adding Afterpay to an **existing React Native Components Advanced-flow** integration. It explicitly says React Native Components do not support Sessions flow. The page supplies method-specific `/payments` fields, redirect handling, capture behavior and test/live setup, while pointing to the main integration guide for the base flow. [[adyen-online-payments]]

## Key takeaways

- **Flow boundary and prerequisite:** `## Sessions flow Component` is marked unavailable. Advanced requires an existing React Native Components integration, redirect handling for `action.type: redirect`, and Afterpay added in Customer Area. The requirements table's link labelled “React Native Components integration” carries `integration=Drop-in`, while its redirect and payment links use `integration=Components`; follow the Components context rather than treating that link target as a separate Drop-in requirement (raw lines 25–41, 51–53).
- **Configuration and fields:** The guide says no extra Afterpay configuration parameters are needed. The `/payments` table marks `paymentMethod: afterpaytouch`, `shopperName`, `shopperEmail`, `shopperReference` (at least three characters), `countryCode`, `billingAddress`, `deliveryAddress` and `lineItems` required. It lists `telephoneNumber` if provided. The AU/AUD examples are examples, not a general availability matrix (raw lines 43–65; examples 67–778).
- **Redirect is an intermediate action:** The sample response has `resultCode: RedirectShopper` and `action.type: redirect`; neither proves successful authorization, capture or settlement. Use the linked base integration's redirect and return handling (raw lines 39–40, 780–794).
- **Capture and cancellation:** Capture is automatic after authorization or manual according to merchant-account configuration. The guide says capture must occur within 13 days; it says the first installment is charged during authorization and Afterpay cancels an uncaptured payment after that window and refunds the first installment. Test authorizations expire in one day, so manual test captures must be within one day (raw lines 796–804).
- **Partial capture:** Partial capture requires manual capture. A capture request specifies `amount.value` and may include `lineItems`. The remaining unclaimed amount is automatically cancelled unless the account is enabled for multiple partial captures; Support setup is described for that mode, with a new invoice per capture (raw lines 806–815).
- **Test/live gate:** Testing uses an Afterpay sandbox shopper account and test card. The sandbox country selector lists Australia, New Zealand, US and Canada, which is not a live acceptance matrix. The page says to submit an Afterpay request in live Customer Area before accepting live payments (raw lines 817–836).

## Detail locators

- Add-on identity and no-Sessions-flow statement: pinned raw lines 15–31.
- Advanced requirements, link-target mismatch, configuration and field table: pinned raw lines 33–65.
- Example requests and redirect response: pinned raw lines 67–794.
- Capture and partial-capture rules: pinned raw lines 796–815.
- Sandbox and live request steps: pinned raw lines 817–836.

## Related

- [[adyen-online-payments]] — online payment architecture and source route.
- [[source-adyen-docs-payment-methods-afterpaytouch]] — Afterpay product/region overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/afterpaytouch/react-native-component/2026-09-15|Afterpay React Native Component, captured 2026-09-15]]
