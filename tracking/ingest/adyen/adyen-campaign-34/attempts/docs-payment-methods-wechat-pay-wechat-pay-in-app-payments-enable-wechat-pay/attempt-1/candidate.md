---
title: "Adyen WeChat Pay in-app enablement guide"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wechat-pay/wechat-pay-in-app-payments/enable-wechat-pay"
raw_files:
  - "adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/enable-wechat-pay/2026-09-15.md"
tags: [adyen, wechat-pay, in-app, setup]
---

## Overview

This [[adyen]] snapshot documents additional **provider-side setup** before accepting **WeChat Pay in-app** payments: a WeChat Open Platform developer account, WeChat mobile-app registration, and transmission of the resulting app credentials to Adyen Support. It separately directs merchants building their **own integration**, rather than using Adyen Drop-in or Component, to integrate WeChat's mobile SDKs. These are setup instructions, not evidence that registration, provider verification, Adyen enablement, a payment, or settlement occurred. The source was last modified in 2020 and captured in 2026. [[adyen-online-payments]]

## Key takeaways

- **WeChat account and registration:** The guide says to create a WeChat Open Platform developer account. WeChat verifies the submitted details; after approval the merchant can register the mobile app. Its registration section is introduced as Android registration but includes an **iOS-only** App Store download link and Bundle ID field; the heading must not erase that iOS condition. See raw lines 19–22 and 28–50.
- **Provider credentials and Adyen Support:** Successful app registration yields a WeChat **AppID** and **AppSecret**. The guide then directs the merchant to provide these to **Adyen Support**, saying this is to ensure payments made with the app are settled to the Adyen account. This describes the historical setup purpose; it does not verify credential submission, enablement, or any actual settlement. Credential ownership is with the registered WeChat app; this page gives no credential-storage or rotation procedure. See raw lines 50–52.
- **Own integration condition:** Only merchants who prefer to build their **own WeChat Pay integration** instead of Adyen's existing Drop-in or Component are additionally directed to register with WeChat for in-app payments and integrate the WeChat Pay mobile SDK. The downloads are described for iOS and Android, with an unspecified iOS kit version placeholder; no exact SDK minimum, app-signature/package-name procedure, API version, environment or runtime payment-result contract is established here. See raw lines 24–26 and 54–67.

## Detail locators

- Developer-account steps and WeChat verification: raw lines 28–35.
- App registration fields, platform qualification, AppID/AppSecret and Adyen Support handoff: raw lines 37–52.
- Conditional own-integration SDK route: raw lines 54–67.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-api-only]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/enable-wechat-pay/2026-09-15|Adyen WeChat Pay in-app enablement snapshot]]
