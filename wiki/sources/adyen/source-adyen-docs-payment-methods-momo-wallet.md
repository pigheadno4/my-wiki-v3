---
title: "MoMo wallet overview"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/momo-wallet"
raw_files:
  - "adyen/docs/payment-methods/momo-wallet/2026-09-15.md"
tags: [adyen, momo, wallet, vietnam, online-payments]
---

## Overview

This 2026-09-15 Adyen overview describes **MoMo**, a Vietnam e-wallet, for online payments. It outlines different desktop-web, mobile-web and mobile-app shopper journeys, gives a historical method-capability matrix, and routes to channel-specific integration guides. It is not a merchant-onboarding or completed-payment record. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Scope:** the page describes MoMo users registering by mobile number and funding wallets through linked bank accounts/cards or offline deposits. Its matrix classifies the method as a **redirect wallet** for **VN/VND**. The page's user-count and market-share statements are dated snapshot claims, not current measurements or merchant eligibility. (raw lines 17–23, 50–52)
- **Shopper journeys:** on desktop web, shoppers are described as going to MoMo's website, scanning a QR code with the MoMo app and confirming, then returning to the merchant site. On mobile web, they go to MoMo's mobile page and choose the app or a phone-number/password login before returning. In a mobile app, they go to the MoMo app, provide a one-time password to authenticate, then return to the merchant app. Redirect, scan, authentication and return are journey steps; the page does not report a final authorization, capture or settlement result. (raw lines 25–48)
- **Capability marks:** the VN/VND row marks **recurring, refunds, partial refunds and multiple partial refunds** with checkmarks. It marks **separate, partial and multiple partial captures, and chargebacks** with x symbols. These are the page's historical capability labels, not a token/mandate creation procedure, live-account entitlement, executed refund, or transaction-state guarantee. (raw lines 50–52)
- **Navigation:** the page links Web, iOS, Android, React Native, Flutter and API-only guides; the API-only label says merchants build their own UI for website or native apps. Pay by Link and in-person payments are separately linked routes, not details of the online redirect flow. The overview gives no endpoint, SDK/version, TEST/LIVE, credential or merchant-enablement steps; the child guides own those specifics. (raw lines 54–102)

## Detail locators

- Wallet description and claimed reach: raw lines 17–23.
- Desktop, mobile-web and native-app shopper descriptions: raw lines 25–48.
- VN/VND capability matrix, including refund and capture marks: raw lines 50–52.
- Channel, API-only, Pay by Link and POS navigation: raw lines 54–102.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-momo-wallet-web]]
- [[source-adyen-docs-payment-methods-momo-wallet-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/momo-wallet/2026-09-15|Adyen MoMo wallet overview, 2026-09-15 snapshot]]
