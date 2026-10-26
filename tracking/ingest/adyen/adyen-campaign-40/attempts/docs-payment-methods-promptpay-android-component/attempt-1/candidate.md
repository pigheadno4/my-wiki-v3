---
title: "Adyen PromptPay Android Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/promptpay/android-component"
raw_files:
  - "adyen/docs/payment-methods/promptpay/android-component/2026-09-15.md"
tags: [adyen, promptpay, android, components, instant-payment, online-payments]
---

## Overview

This 2026-09-15 capture of a page marked last modified in 2019 describes PromptPay-specific additions to an existing Android Components integration. It has separate Sessions and Advanced paths, import and launch guidance for the InstantPayment Component, an Advanced `/payments` example, and TEST/LIVE setup notes. It does not itself explain QR action handling or prove current merchant enablement or a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** Requires an existing Sessions Android Components integration with a stated minimum required version of **5.0.0**, plus Support assistance to add PromptPay in Customer Area. The version wording is attached to the Android Components integration, not stated as a Checkout API minimum. The page says no extra PromptPay-specific payment-session request parameters or Component configuration. The main-guide links include version-qualified `5.3.0` anchors, which are navigation context, not a new minimum. (raw lines 23–40, 65–73)
- **Component setup:** For both flows, import `com.adyen.checkout:instant`; Compose also imports `components-compose`. The Sessions examples select `PaymentMethodTypes.PROMPTPAY` from the checkout session and use `InstantPaymentComponent` in Compose or a View. Advanced points to the base guide for launch rather than giving a full PromptPay-specific Component instance. The Sessions Compose snippet includes a stray `Component` line and appears to omit the enclosing composable's closing brace; the View snippet passes `cardConfiguration` to the instant provider. Treat these as examples requiring Android SDK/version review. (raw lines 42–133, 150–175)
- **Advanced:** Requires an existing Advanced Android Components integration and Support-assisted Customer Area setup; no PromptPay-specific configuration is stated. Its `/payments` curl example uses `paymentMethod.type: promptpay` and THB. It does not establish THB as a complete country/currency eligibility rule or supply the QR action, shopper confirmation, return or final webhook sequence. The Advanced section states no separate 5.0.0 minimum. (raw lines 135–200, 401–413)
- **Testing and live:** The page instructs testing PromptPay with real payment details and small amounts, checking status in the test Customer Area, and contacting Support to add PromptPay in the live Customer Area before live acceptance. This is not presented as a free simulator; no test or live payment was performed for this ingestion. The page gives status navigation, not a completed authorization, capture or settlement record. (raw lines 401–407)
- **Sample limits:** The Advanced Java, PHP, C# and Go snippets call payment services with request objects that are not constructed in those snippets; the TypeScript sample likewise leaves `paymentRequest` undefined. Node samples use unshown `Config`/`EnvironmentEnum` symbols. These examples and the 2019 modified metadata alongside versioned 2026 capture do not establish runnable current SDK behavior. (raw lines 202–399; metadata lines 1–13)

## Detail locators

- Sessions requirements, request/configuration statements and Component setup: raw lines 23–133.
- Advanced requirements, imports, launch routing and `/payments` examples: raw lines 135–399.
- TEST/LIVE instructions and related navigation: raw lines 401–413.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-android-sdk]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/promptpay/android-component/2026-09-15|Adyen PromptPay Android Component guide, 2026-09-15 snapshot]]
