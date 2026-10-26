---
title: "Swish payment method overview"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/swish"
raw_files:
  - "adyen/docs/payment-methods/swish/2026-09-15.md"
tags: [adyen, swish, wallet, sweden, online-payments]
---

## Overview

This 2026-09-15 Adyen overview describes Swish as a wallet for online payments and points to channel-specific integration guides. Its shopper path uses a direct mobile-device switch to the Swish app or a desktop QR scan. The page also mentions in-person payments, Pay by Link and a claimed real-time transfer to the merchant account; it does not document a completed transaction or establish current merchant availability. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Scope and shopper path:** the page identifies Swish as a wallet popular in Sweden. For the described payment, a shopper reaches the Swish app directly on mobile or by scanning a QR code on desktop. The page says the amount is transferred to the merchant account in real time, but gives no authorization, capture, settlement, return or webhook procedure. (raw lines 23–25)
- **Capability matrix:** the page's row labels Swish a QR wallet for **SE/SEK**. It marks recurring, separate captures, partial captures, multiple partial captures and chargebacks with x symbols; refunds, partial refunds and multiple partial refunds have checkmarks. These are overview capability marks, not evidence of a particular merchant's enablement or a successfully executed refund. (raw lines 27–29)
- **Integration routes:** the linked online paths are Web, iOS, Android, React Native, Flutter and API only. The UI routes advertise pre-built solutions; API only says the merchant builds its own UI for web or native apps. Pay by Link and in-person payments are separately linked routes. Endpoint, SDK/version, API flow, TEST/LIVE and activation details belong to the linked guides. (raw lines 31–79)

## Detail locators

- Wallet description and mobile/desktop shopper path: raw lines 23–25.
- Country, currency and feature matrix: raw lines 27–29.
- Online UI, API-only, Pay by Link and in-person routes: raw lines 31–79.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/swish/2026-09-15|Adyen Swish overview, 2026-09-15 snapshot]]
