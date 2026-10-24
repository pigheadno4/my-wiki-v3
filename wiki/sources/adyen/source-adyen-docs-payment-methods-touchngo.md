---
title: "Touch'n Go eWallet overview"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/touchngo"
raw_files:
  - "adyen/docs/payment-methods/touchngo/2026-09-15.md"
tags: [adyen, touchngo, wallet, malaysia, online-payments]
---

## Overview

This 2026-09-15 capture of a page last modified in 2022 describes **Touch'n Go eWallet** as a Malaysian digital wallet and routes to channel-specific integration guides. It outlines desktop QR and mobile app/browser shopper journeys and a historical **MY/MYR** capability row. It does not document merchant onboarding or an observed transaction result. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Shopper paths:** on desktop, the page describes a browser redirect that displays a QR code, which the shopper scans and confirms in the Touch'n Go app. On mobile with the app installed, it describes an app redirect, confirmation, and return to the merchant webshop. Without the app, it describes a Touch'n Go mobile-browser route where the shopper enters a phone number and PIN, confirms, and returns. Scan, confirmation and return are described shopper steps, not observed authorization, capture or settlement. (raw lines 19–25)
- **Historical capability matrix:** the row classifies the method as a **redirect wallet for MY/MYR**. It x-marks **recurring, separate/partial/multiple partial captures, and chargebacks**, while check-marking **refunds, partial refunds and multiple partial refunds**. These page marks are not live merchant entitlement or proof that a refund occurred. (raw lines 27–29)
- **Integration routes:** the page links Web, iOS, Android and API-only guides; the API-only label says a merchant builds its own UI for website or native apps. It separately links Pay by Link. These are navigation routes and provide no endpoint/version, redirect or QR expiry, credential, TEST/LIVE or merchant-eligibility procedure on this overview. (raw lines 31–61)

## Detail locators

- Malaysia wallet identity and desktop/mobile shopper journeys: raw lines 19–25.
- MY/MYR capability row: raw lines 27–29.
- Web, native, API-only and Pay by Link navigation: raw lines 31–61.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/touchngo/2026-09-15|Adyen Touch'n Go overview, 2026-09-15 snapshot]]
