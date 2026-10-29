---
title: "Adyen Alma React Native Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alma/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/alma/react-native-component/2026-09-15.md"
tags: [adyen, alma, react-native, components, online-payments, installments]
---

## Overview

This captured [[adyen]] guide adds Alma to an **existing React Native Components Advanced-flow** integration. It explicitly states React Native Components do not support Sessions flow. The page provides optional request additions, redirect handling and a test/live gate; it does not demonstrate payment authorization, capture or settlement. [[adyen-online-payments]]

## Key takeaways

- **Flow boundary and prerequisites:** Sessions is marked unavailable. Advanced requires an existing React Native Components integration, handling `action.type: redirect`, and Alma added in Customer Area. The requirement link labelled “React Native Components integration” points to `integration=Drop-in`, whereas the redirect and payment links point to `integration=Components`; this link-target mismatch does not change the page's Components scope (raw lines 25–41, 51–53).
- **Configuration and optional fields:** No additional Alma configuration parameters are needed. The `/payments` table lists `telephoneNumber`, `shopperEmail`, `billingAddress`, `deliveryAddress` and `additionalData.alma.installments_count` with blank Required cells. For the installment field, the page says `3` or `4` determines the shopper's installment count; omit it to let the shopper choose. Do not turn the example's included fields into mandatory requirements (raw lines 43–61).
- **Example and redirect caveat:** The FR/EUR TEST curl example places `-X POST` on a line without a shell continuation before `-d`, so the literal command is not copy-ready (raw lines 65–71). The response example has `resultCode: RedirectShopper` and `action.type: redirect`, an intermediate action rather than payment success. The FR/EUR and HTTPS return URL values are examples, not a general eligibility or return-scheme rule (raw lines 72–117).
- **Test/live gate:** The page points to Customer Area for test-payment status and says to submit a request for Alma in live Customer Area before accepting live payments (raw lines 119–123).

## Detail locators

- Guide identity and unsupported Sessions flow: pinned raw lines 15–31.
- Advanced prerequisites and link-target mismatch: pinned raw lines 33–41.
- No-extra-config and optional-field table: pinned raw lines 43–61.
- Request example/curl caveat and redirect response: pinned raw lines 63–117.
- Test status and live request: pinned raw lines 119–123.

## Related

- [[adyen-online-payments]] — online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-alma]] — Alma method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/alma/react-native-component/2026-09-15|Alma React Native Component, captured 2026-09-15]]
