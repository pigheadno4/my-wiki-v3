---
title: "Pix React Native Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pix/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/pix/react-native-component/2026-09-15.md"
tags: [adyen, pix, react-native, components, qr-code, asynchronous-payments]
---

## Overview

This 2026-09-15-captured Adyen add-on describes Pix for an existing React Native Components integration. It explicitly says Sessions flow is unavailable for React Native Components; its method instructions cover Advanced /payments, a QR-code action, refunds, and test/live setup. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-pix]] for Pix context. This snapshot does not prove account enablement or a completed payment.

## Key takeaways

- React Native Components do not support Sessions flow on this page. Advanced requires an existing React Native Components Advanced integration, action handling for action.type qrCode, and Pix setup in Customer Area. The page says no extra Pix configuration parameters are needed. See raw lines 25–47.
- The Advanced /payments table marks paymentMethod and amount required. It leaves shopperName, socialSecurityNumber (CPF/CNPJ shown on the Pix form), shopperStatement, sessionValidity and line-item fields unmarked; sending shopperName and socialSecurityNumber together is advice. A supplied shopperStatement must be under 60 characters. sessionValidity is described as payment expiration, with default one hour through Checkout API v71 and 24 hours from v72. The BR/BRL and app-scheme returnUrl in the v72 sample are examples; its 2025-10-01 validity date predates this capture. See raw lines 49–108.
- The example response is Pending with action.type qrCode, qrCodeData and pix.expirationDate. This is a QR presentation/payment-pending state, not final paid status or proof of a separate QR display timer. The page says Pix is asynchronous; test payments can be simulated by promoting a pending offer to sale in the test Customer Area, then checked in Payment list for reconciliation. It says live acceptance requires a Pix request in the live Customer Area. See raw lines 554–593.
- The guide says a paid Pix payment may be refunded within 90 days via Customer Area or API. That is a documented limit, not evidence of a refund performed. See raw lines 576–578.

> [!warning] React Native base-route and callback wording
> The Advanced prerequisite names React Native Components but links to integration=Drop-in (raw line 39). Its qrCode action link targets a handle-the-redirect anchor (line 40). The Pix table describes required paymentMethod as `state.data.paymentMethod` from onSubmit (line 57), while the captured React Native Components Advanced base guide describes onSubmit data passed to the server and the complete paymentMethod object from the client app (base raw `raw/adyen/docs/online-payments/build-your-integration/advanced-flow/2026-09-15.md`, lines 17861–17871 and 17942–17959). Do not treat the child table's web-style property path as a verified React Native Components callback shape.

## Detail locators

- Sessions unavailability and Advanced prerequisites: raw lines 25–41.
- No extra configuration and Advanced fields/expiry: raw lines 43–66.
- BR/BRL request example and stale validity date: raw lines 68–108; other language samples run through line 552.
- Pending QR-code response and pix.expirationDate: raw lines 554–574.
- Refund, asynchronous test promotion, reconciliation and live setup: raw lines 576–593.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-pix]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pix/react-native-component/2026-09-15|Pix React Native Component, captured 2026-09-15]]
