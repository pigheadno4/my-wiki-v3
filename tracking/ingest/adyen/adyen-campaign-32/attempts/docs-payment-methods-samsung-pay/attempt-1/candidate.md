---
title: "Adyen Samsung Pay overview"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/samsung-pay"
raw_files:
  - "adyen/docs/payment-methods/samsung-pay/2026-09-15.md"
tags: [adyen, samsung-pay, wallet, online-payments, point-of-sale]
---

## Overview

This Adyen Samsung Pay overview (last-modified metadata 2022-11-22; captured 2026-09-15) identifies **Samsung Pay as a Samsung-provided Android mobile wallet**. It describes shoppers adding cards in the Samsung Pay app, an **NFC** contactless route at physical point of sale, and an ecommerce route where an installed app presents a Samsung Pay payment sheet for card selection. It links to a separate API-only guide for a merchant-built website or Android-app UI and to an in-person guide. The overview itself is not an integration recipe or evidence of current merchant availability or payment success. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The in-person route has the payment terminal communicate with the wallet through the shopper phone or smartwatch NFC chip. The ecommerce description is conditional on the app being installed on the shopper's mobile device; the shopper selects a card in a payment sheet and proceeds with payment. Selection or wallet authentication does not itself establish authorization, capture, or settlement. (raw lines 23–27)
- The dated catalog row labels Samsung Pay as a **wallet** with **additional action**, “International” countries and “Multiple” currencies. It marks recurring, refunds, partial refunds, separate captures, partial captures and chargebacks with checkmarks; it marks **multiple partial refunds** and **multiple partial captures** with X. These are overview feature marks, not per-country, per-issuer, per-merchant or per-transaction guarantees; follow child guides and provider/account setup for executable details. (raw lines 29–31)
- Compatibility is explicitly limited to specific devices, countries/regions and issuers; the page points to Samsung's regional lists rather than enumerating a fixed global support list. The pricing/settlement link points outside this snapshot and supplies no price, settlement timing or completed transfer evidence here. (raw lines 21, 33–38)
- The integration chooser links **API only** for a merchant-built website or Android-app UI and **in-person payments** for the POS route. Those child targets are navigation from this overview; this source alone supplies no API/SDK version, token, certificate, PCI, redirect, return, recurring-consent or payment-result instructions. (raw lines 40–52)

## Detail locators

- Wallet identity and channel descriptions: raw lines 15–27.
- Dated feature matrix: raw lines 29–31.
- Conditional device/country/issuer compatibility: raw lines 33–38.
- API-only and in-person child-guide routes: raw lines 40–52.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-pos-alternative-payment-methods]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/samsung-pay/2026-09-15|Adyen Samsung Pay overview, 2026-09-15 snapshot]]
