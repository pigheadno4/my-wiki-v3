---
title: "Alipay HK"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipayhk"
raw_files:
  - "adyen/docs/payment-methods/alipayhk/2026-09-15.md"
tags: [adyen, alipayhk, wallets, online-payments, payment-methods]
---

## Overview

This 2026-09-15 Adyen Alipay HK overview identifies a Hong Kong wallet payment method and routes readers to channel-specific integration guides. It describes a shopper scanning a QR code in the app and completing password or biometric authentication. It is a capability and navigation snapshot, not proof that a particular merchant is enabled, that a payment was authorized, or that a live refund or capture succeeded. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The page describes AlipayHK as available in Hong Kong and gives a shopper QR-code/app authentication description. Its capability table classifies the online payment as **Wallets**, with **redirect** flow, **HK** country and **HKD** currency. These are the page's listed scope, not a global acceptance guarantee. (raw lines 23–29)
- In the table, **recurring**, **separate captures**, **partial captures**, **multiple partial captures**, and **chargebacks** have X marks. **Refunds**, **partial refunds**, and **multiple partial refunds** have checkmarks. The page provides capability marks rather than the operational conditions, API steps, timing or actual outcomes for those features. (raw lines 27–29)
- The integration chooser links to Web, iOS, Android, React Native, Flutter and API-only paths. Web and native routes are distinct child guides; the overview gives no Sessions/Advanced, SDK or API-version prerequisites and no redirect/return/webhook implementation details. (raw lines 31–67)
- It also links Pay by Link and in-person payments, which are separate routes. The listed QR authentication is shopper-side wallet behavior; it does not establish Adyen server payment status, authorization, capture or settlement. (raw lines 23–25, 69–79)

## Detail locators

- Wallet description and shopper authentication: raw lines 23–25.
- Country, currency, flow and capability matrix: raw lines 27–29.
- Web/native/API-only navigation: raw lines 31–67.
- Pay by Link and point-of-sale navigation: raw lines 69–79.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipayhk/2026-09-15|Adyen Alipay HK overview, 2026-09-15 snapshot]]
