---
title: "Adyen Classic API Google Pay"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/classic-google-pay"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/classic-google-pay/2026-09-15.md"
tags: [adyen, online-payments, classic-api, google-pay, wallet]
---

## Overview

This 2026-09-15 snapshot describes Google Pay for an **existing Classic Payment API `/authorise` integration** on Android or the web. The endpoint is inactive and no longer supported for new integrations; Adyen directs new builds to Checkout API and existing users to contact Adyen about migration. The page metadata says last modified in 2019, so its sample Google API parameters and live setup are historical source evidence, not proof of current SDK or merchant eligibility.

## Key takeaways

- The client-side Google Pay request uses `allowedPaymentMethods` with the page's `CARD` and `TOKENIZED_CARD` options and gateway tokenization with `gateway: adyen`. Its sample `gatewayMerchantId` is the **name of the Adyen MerchantAccount or CompanyAccount**. These are parameters sent to Google API, not the server-side payment result. See `Step 1: Integrate the Google Pay SDK`.
- After the merchant server receives the Google Pay token, it sends a Classic `/authorise` payment request to Adyen with the token in `additionalData.googlepay.token`. The example also shows amount, merchant reference, and `merchantAccount`. Token receipt and request submission do not establish an authorized or captured payment; this page provides no authorization-response or webhook outcome procedure. See `Step 2: Send the token to Adyen`.
- Before accepting live Google Pay payments, the guide says to complete integration and testing, request Google Pay in **live Customer Area**, and have the merchant ID configured in Adyen's Google Pay payment-method configuration. The page does not say that the sample gateway account-name value alone completes live enablement. See `Step 3: Go live`.

## Detail locators

- `Step 1`: Google API parameter sample, gateway/account-name value, and `CARD` versus Android device-token descriptions; linked Google API guides are further navigation.
- `Step 2`: Classic `/authorise` endpoint, token field placement, and illustrative request JSON.
- `Step 3`: testing and live Customer Area/configuration prerequisites.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/classic-google-pay/2026-09-15|Adyen Classic Google Pay guide, 2026-09-15 snapshot]]
