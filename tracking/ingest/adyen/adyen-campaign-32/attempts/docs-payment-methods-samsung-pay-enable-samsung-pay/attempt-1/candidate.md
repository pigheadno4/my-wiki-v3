---
title: "Enable Samsung Pay"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/samsung-pay/enable-samsung-pay"
raw_files:
  - "adyen/docs/payment-methods/samsung-pay/enable-samsung-pay/2026-09-15.md"
tags: [adyen, samsung-pay, wallet, setup, online-payments]
---

## Overview

This 2026-09-15 snapshot of Adyen's Samsung Pay enablement guide lists additional setup before accepting Samsung Pay: obtain a certificate signing request (CSR) through Adyen, register with Samsung Pay, select Adyen as Samsung Pay's gateway, integrate Samsung Pay's SDK, and ask Adyen Support to configure compatible card schemes on the merchant account. It documents setup instructions, not evidence that a merchant account, SDK integration or live transaction is ready. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The guide's prerequisite list says to request a CSR from Adyen, create a Samsung Pay developer account, set Adyen as payment gateway, integrate the Samsung Pay SDK, and contact Adyen Support to configure Visa, Mastercard, Maestro, Amex and Discover for Samsung Pay on the merchant account. Scheme configuration is a Support request, not an automatic result of the other steps. (raw lines 19–25)
- To generate the encryption CSR for the Samsung Pay platform, first add Samsung Pay as a payment method in Adyen Customer Area. The guide names either **Merchant admin** or **Manage API Credentials** as the needed role. In **Developers > API credentials**, select the web service user that will execute Samsung Pay transactions, then use **Wallet payment methods > Samsung Pay > + Add > Generate CSR > Download CSR**. The page does not claim that downloading the CSR by itself enables payments. (raw lines 27–38)
- Register and complete a developer profile on Samsung Pay's developer site. In that Samsung Pay account, create a service and an app under **My Projects**, choose **Adyen** as **Payment Gateway**, and upload the CSR received from Adyen. The Samsung-side service/app and gateway steps are distinct from Adyen Customer Area's CSR generation. (raw lines 40–52)
- Download and integrate the **Samsung Pay SDK** by following Samsung's linked SDK guide. This page does not itself give SDK integration code, describe the token/server payment request, or establish a successful authorization, capture or settlement. (raw lines 54–57)

## Detail locators

- Prerequisite list and scheme-support request: raw lines 19–25.
- CSR purpose, role gate and Adyen Customer Area sequence: raw lines 27–38.
- Samsung developer registration and gateway/CSR upload: raw lines 40–52.
- SDK delegation: raw lines 54–57.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-samsung-pay-samsung-pay-api]]
- [[source-adyen-docs-payment-methods-samsung-pay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/samsung-pay/enable-samsung-pay/2026-09-15|Adyen Enable Samsung Pay, 2026-09-15 snapshot]]
