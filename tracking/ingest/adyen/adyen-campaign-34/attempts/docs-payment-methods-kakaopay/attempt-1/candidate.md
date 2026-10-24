---
title: "Adyen KakaoPay payment-method overview"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/kakaopay"
raw_files:
  - "adyen/docs/payment-methods/kakaopay/2026-09-15.md"
tags: [adyen, kakaopay, korea, wallet, redirect]
---

## Overview

This [[adyen]] overview presents **KakaoPay** as a Korean e-wallet for online payments. Its capability table identifies **Wallets / redirect / KR / KRW** and lists one-time and recurring shopper journeys. This is a 2026-09-15 snapshot of documentation and capability marks, not proof of current availability, a merchant's enablement, a registered recurring mandate or a successful payment. [[adyen-online-payments]]

## Key takeaways

- **One-time flow:** After selection on a website or mobile app, the page says shoppers are redirected to a website with a QR code scanned in the KakaoPay app. They confirm using biometrics or a six-digit PIN, return to the merchant site/app and receive a KakaoPay purchase notification. The redirect and notification describe shopper steps, not Adyen's final authorization or capture. See raw lines 25–41.
- **Recurring flow:** The described route uses a Kakao credentials login or QR code, sends a KakaoTalk notification, has the shopper select **Login** and log in, then returns to the merchant site/app and sends a KakaoPay recurring/auto-debit notification. This does not by itself define token storage, mandate scope, consent record, subsequent charge rules or final payment status. See raw lines 43–57.
- **Expiry:** The KakaoPay redirect page is valid **30 minutes by default**, then times out. The page directs merchants to Adyen Support to request a different link expiry. It gives no automatic extension or retry outcome. See raw line 59.
- **Capability matrix:** The table marks recurring and refunds (including partial and multiple partial) supported; it marks separate, partial and multiple partial captures plus chargebacks unsupported. These are overview marks for KR/KRW redirect, not a guarantee for a particular merchant or transaction. See raw lines 61–63.
- **Routes:** It links Web, iOS, Android, React Native, Flutter, API-only and Pay by Link guides. The API-only label mentions merchant-built UI for website/iOS/Android. These are navigation; each child guide owns its implementation prerequisites and request behavior. See raw lines 65–107.

## Detail locators

- Provider description and one-time/recurring shopper flows: raw lines 21–57.
- Default redirect expiry and Support route: raw line 59.
- Capability matrix and integration links: raw lines 61–107.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/kakaopay/2026-09-15|Adyen KakaoPay overview snapshot]]
