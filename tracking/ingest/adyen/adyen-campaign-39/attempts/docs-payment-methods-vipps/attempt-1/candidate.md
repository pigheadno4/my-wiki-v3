---
title: "Adyen Vipps payment-method overview"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/vipps"
raw_files:
  - "adyen/docs/payment-methods/vipps/2026-09-15.md"
tags: [adyen, vipps, norway, wallet, redirect]
---

## Overview

This [[adyen]] overview introduces Vipps for online payments. Its 2026-09-15 snapshot describes a Norway-focused mobile wallet, the shopper handoff for app and website payments, a capability matrix, and routes to channel-specific integration guides. It does not establish present merchant eligibility or a successful payment. [[adyen-online-payments]]

## Key takeaways

- The shopper needs the Vipps app on a mobile device and a Visa or Mastercard linked to the Vipps account; the account information is connected to the shopper's phone number. In an app checkout, the shopper switches to the Vipps app to authenticate. On a website, the shopper first visits a Vipps-hosted page to enter a phone number, then authenticates in the Vipps app. Authentication here is a shopper step, not proof of authorization or capture. See raw lines 23–27.
- The overview table labels Vipps **Wallets / redirect / NO / NOK**. It marks refunds, partial and multiple partial refunds, separate, partial and multiple partial captures, and chargebacks with checkmarks. Recurring is marked with an x and “See note,” but this pinned page contains no explanatory note; do not infer its exact scope from this matrix. These are overview capability marks, not setup or transaction outcome evidence. See raw lines 29–31.
- The chooser links Web, iOS, Android, React Native, Flutter and API-only guides; its API-only description offers a merchant-built UI for a website or iOS/Android app. Pay by Link has a separate route. The child links do not specify their own SDK/API versions, prerequisites, return handling or payment outcome here. See raw lines 33–75.

## Detail locators

- Vipps identity and shopper authentication paths: raw lines 15–27.
- Country, currency and capability matrix: raw lines 29–31.
- Channel and Pay by Link navigation: raw lines 33–75.
- General online-payment, 3D Secure and capture links: raw lines 77–82.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/vipps/2026-09-15|Adyen Vipps overview snapshot]]
