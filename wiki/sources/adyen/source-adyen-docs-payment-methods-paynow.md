---
title: "Adyen PayNow QR-code payment overview"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paynow"
raw_files:
  - "adyen/docs/payment-methods/paynow/2026-09-15.md"
tags: [adyen, paynow, singapore, qr-code, real-time-payments, online-payments]
---

## Overview

This 2026-09-15 Adyen page is a **PayNow online-payment overview and channel chooser**. It describes Singapore's real-time transfer network but expressly limits **Adyen's integration offering on this page to QR-code payments**. It does not provide a complete QR creation/scanning procedure, merchant eligibility determination or final transaction evidence. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Network versus Adyen scope:** The page describes PayNow as a Singapore real-time payment network, including transfers of SGD among bank accounts or e-wallets and enrollment identifiers such as mobile number, business registration number or Virtual Payment Address. That broad network description must not be read as Adyen support for every transfer mode: the guide explicitly says Adyen offers PayNow integration **only for QR-code payments**. (raw lines 23–25)
- **Historical capability row:** The table labels the Adyen payment type as real-time payments, flow `qrCode`, country **SG** and currency **SGD**. It marks refunds and partial refunds with checks, while recurring, multiple partial refunds, separate/partial/multiple partial captures and chargebacks carry x marks. These are dated table indicators, not proof of live merchant enablement, a processed refund or a completed/settled payment. (raw lines 27–29)
- **Channel navigation:** The chooser links Web, iOS, Android, React Native and Flutter child guides and describes prebuilt UI solutions. Those links route implementation research; this overview does not state API/SDK versions, QR expiry, shopper scan/return handling, webhook result semantics or channel-specific prerequisites. The nearby 3D Secure and Capture links under “See also” do not change the PayNow capability row. (raw lines 31–68)

## Detail locators

- PayNow network description versus Adyen QR-only integration scope: raw lines 17–25.
- SG/SGD and historical capability matrix: raw lines 27–29.
- Web/native/cross-platform child navigation and generic related links: raw lines 31–68.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paynow/2026-09-15|Adyen PayNow overview, 2026-09-15 snapshot]]
