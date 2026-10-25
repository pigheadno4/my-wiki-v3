---
title: "Online banking Thailand"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-thailand"
raw_files:
  - "adyen/docs/payment-methods/online-banking-thailand/2026-09-15.md"
tags: [adyen, online-banking, thailand, razer-merchant-services, redirect, online-payments]
---

## Overview

This 2026-09-15 overview describes Adyen's Online banking Thailand payment method, offered through partner Razer Merchant Services (RMS), formerly MOLPay. It classifies the route as a TH/THB online-banking redirect and says the final payment result can be asynchronous, requiring webhook evidence. It does not show a completed payment or current merchant entitlement. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Provider and shopper path:** the page places the Thai offering through RMS, formerly MOLPay. For a payment, the shopper is redirected to their bank website to complete the bank-side steps. A redirect or return alone is not the final result; the page says to rely on webhooks when the result arrives asynchronously. It does not specify the webhook event/payload, settlement timing or a successful transaction. (raw lines 23–25)
- **Historical capability row:** the table labels payment type `Online Banking`, flow `redirect`, country `TH` and currency `THB`. It x-marks recurring, refunds, partial/multiple partial refunds, separate/partial/multiple partial captures and chargebacks. These are source-table marks, not evidence of current merchant eligibility or a performed refund/capture. (raw lines 27–29)
- **Integration routes:** the overview links Web, iOS, Android, React Native, Flutter, API-only merchant-built UI and Pay by Link. It does not itself give child-specific versions, API fields, setup, bank list, redirect implementation, expiry, TEST/LIVE procedure or final outcome mapping. (raw lines 31–73)
- **General links:** its See also references 3D Secure and Capture, but those links do not establish method-specific 3DS or capture behavior; the table itself x-marks listed capture variants. (raw lines 75–80)

## Detail locators

- RMS/MOLPay partner and asynchronous bank-redirect/webhook path: raw lines 23–25.
- TH/THB table and capability marks: raw lines 27–29.
- Web, native, API-only and Pay by Link child routes: raw lines 31–73.
- General See also links: raw lines 75–80.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-thailand/2026-09-15|Adyen Online banking Thailand overview, 2026-09-15 snapshot]]
