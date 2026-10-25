---
title: "Rakuten Pay Android Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/rakutenpay/android-component"
raw_files:
  - "adyen/docs/payment-methods/rakutenpay/android-component/2026-09-15.md"
tags: [adyen, rakuten-pay, android, components, redirect, recurring]
---

## Overview

This 2026-09-15 Adyen page describes Rakuten Pay additions to an existing Android Components integration, separately for Sessions and Advanced flows. Both use `InstantPaymentComponent` to handle a redirect action. The page is a method-specific add-on, not a standalone integration or proof of live merchant eligibility or completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions prerequisites and method data:** Use an existing Android Components Sessions flow, Checkout API v68 or later, redirect handling and Customer Area method setup. No additional `/sessions` parameters are stated. The example obtains `rakutenpay` from the checkout session and uses `InstantPaymentComponent` with or without Jetpack Compose. (raw lines 25–42, 89–142)
- **Advanced prerequisites and method data:** Use an existing Android Components Advanced flow that handles the additional `redirect` action, with Rakuten Pay added in Customer Area. The examples select `rakutenpay` from a `/paymentMethods` response; the page says no additional `/payments` parameters are needed. It does not state an Advanced Checkout API minimum. (raw lines 160–168, 215–276)
- **Android module/configuration scope:** Both flows show `com.adyen.checkout:instant:YOUR_VERSION`; the Compose variant also shows `components-compose:YOUR_VERSION`. `setSubmitButtonVisible` is optional and defaults to true. The shown configuration snippets contain an unexplained nested brace and placeholder `value`; they should not be treated as verified runnable Kotlin or as a fixed SDK version. The Compose examples call for a distinct key per different screen or session/reset. (raw lines 44–87, 95–123, 170–213, 221–250)
- **Recurring restriction:** In the source's subscription and unscheduled card-on-file context, Rakuten Pay allows one-off card-on-file transactions only after review. It says a merchant without a periodic charging cadence must not initiate the card-on-file Recurring Processing Model, describes that model as primarily allowed for Food & Beverage, and requires application for every Recurring Processing Model when requesting Rakuten Pay. Tokenization is linked as a separate integration; the page strongly recommends explicit shopper permission for future recurring charges. These words do not establish automatic approval or unrestricted recurring capability. (raw lines 144–150, 278–284)
- **TEST boundary:** The page names `DGFT_AcquirerAccount_RakutenPay_closedLoop` for TEST payments and says the redirect goes to a DGFT simulator without the Rakuten Pay app. Payment-list status inspection is mentioned. A simulator flow or status-location instruction does not prove LIVE readiness, authorization, capture or settlement. (raw lines 152–158, 286–292)

## Detail locators

- Sessions requirements and request additions: raw lines 25–42.
- Sessions imports, optional configuration and Compose/non-Compose launch: raw lines 44–142.
- Advanced requirements, imports, optional configuration and launch: raw lines 160–270.
- Advanced `/payments`, recurring qualification and TEST simulator: raw lines 272–292.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/rakutenpay/android-component/2026-09-15|Adyen Rakuten Pay Android Component guide, 2026-09-15 snapshot]]
