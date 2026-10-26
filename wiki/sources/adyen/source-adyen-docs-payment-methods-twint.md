---
title: "Adyen TWINT payment method overview"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/twint"
raw_files:
  - "adyen/docs/payment-methods/twint/2026-09-15.md"
tags: [adyen, twint, switzerland, chf, wallet, redirect, capture]
---

## Overview

This 2026-09-15 Adyen overview describes TWINT as a Swiss mobile wallet method for online and in-person payments. It distinguishes the online mobile app or short-code handoff from the desktop webpage QR or short-code handoff, gives a CH/CHF capability table, and routes to platform-specific guides. The overview is a captured provider claim, not evidence of current merchant eligibility, feature enablement, funds transfer, or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Shopper handoff:** the page says a shopper can connect a bank account or card in the TWINT app. For online mobile checkout, the shopper is redirected to the app or a webpage where they can open the app or copy and enter a short code. On desktop/laptop, a TWINT webpage offers app QR scanning or short-code entry. These are shopper routes; the page does not specify a Checkout response, return URL, expiry, or final webhook status. Its separate in-store example has the shopper scan a terminal-displayed QR code. (raw lines 23–30)
- **Capture and capability scope:** the source says the amount is transferred to the merchant account in real time **after capture**, so the statement is capture-dependent and not proof of immediate authorization or settlement for any transaction. Its table labels TWINT a redirect wallet for **CH/CHF** and marks recurring, refunds, partial/multiple partial refunds, separate and partial captures, and chargebacks with checkmarks; it marks **multiple partial captures** with an x. The table supplies no account-specific prerequisites or detailed lifecycle rules for those marks. (raw lines 32–36)
- **Implementation routes:** this overview links Web, iOS, Android, Flutter, API-only, Pay by Link and in-person routes. The API-only link says merchants can build their own UI for website/iOS/Android. The child guides, rather than this overview, own platform request fields, redirect/QR continuation and result handling. (raw lines 38–80)

## Detail locators

- TWINT identity and mobile, desktop, and in-store shopper patterns: pinned raw lines 15–30.
- Capture-dependent transfer statement and CH/CHF capability matrix: pinned raw lines 32–36.
- Web, native, Flutter, API-only, Pay by Link and POS routes: pinned raw lines 38–80.
- General online payments, 3DS, capture and payment-method navigation: pinned raw lines 82–87.

## Related

- [[adyen-online-payments]] — main provider online-payment context
- [[adyen]] — provider
- [[adyen-tokenization]] — provider token lifecycle; recurring details require child evidence

## Raw Sources

- [[raw/adyen/docs/payment-methods/twint/2026-09-15|TWINT overview, 2026-09-15]]
