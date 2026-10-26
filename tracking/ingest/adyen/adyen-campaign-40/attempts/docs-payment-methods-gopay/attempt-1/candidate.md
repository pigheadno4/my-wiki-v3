---
title: "GoPay payment method overview"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gopay"
raw_files:
  - "adyen/docs/payment-methods/gopay/2026-09-15.md"
tags: [adyen, gopay, indonesia, wallet, redirect, online-payments]
---

## Overview

This 2026-09-15 Adyen overview describes GoPay as an Indonesian e-wallet and outlines shopper handoffs for one-time website/app and recurring payments. It gives a dated capability matrix and routes to channel-specific integration guides. The page does not prove present merchant eligibility or an executed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Wallet and one-time shopper path:** shoppers register using a mobile number and PIN, and the page says they can fund the wallet from a bank account or cash deposit at GoPay offline stores. For a website checkout it describes a redirect to the GoPay website for mobile-number login, an SMS URL to make the payment, shopper confirmation and return to the merchant website. For a mobile-app checkout it instead describes a redirect to the GoJek app, a push-notification URL, confirmation and return to the merchant app. These are shopper steps, not server-side authorization or settlement evidence. (raw lines 23–45)
- **Recurring shopper path:** after selection on a website or app, the page describes GoPay website login, an SMS one-time password, PIN authentication, confirmation and return. The overview does not supply token creation, consent, recurring charge execution or webhook mechanics. (raw lines 47–55)
- **Dated capability row:** the table labels GoPay `Wallets / redirect / ID / IDR`. It marks recurring, refunds, partial refunds and multiple partial refunds with checkmarks; separate, partial and multiple partial captures and chargebacks have x marks. These are method overview indicators, not a promise for a particular account or transaction. (raw lines 57–59)
- **Integration routes:** chooser links Web, iOS, Android, React Native, Flutter, API-only merchant-built UI, and Pay by Link. Child guides determine their own SDK/API prerequisites, redirect/return handling and payment status flow. (raw lines 61–103)

## Detail locators

- Registration/funding and website versus app one-time paths: raw lines 23–45.
- Recurring shopper authentication/confirmation path: raw lines 47–55.
- Country/currency and capability row: raw lines 57–59.
- Channel and Pay by Link routes: raw lines 61–103.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gopay/2026-09-15|Adyen GoPay overview, 2026-09-15 snapshot]]
