---
title: "Adyen cards integration overview"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards"
raw_files:
  - "adyen/docs/payment-methods/cards/2026-09-15.md"
tags: [adyen, cards, payment-methods, online-payments, pci, historical]
---

## Overview

This [[adyen]] Cards overview, last modified **2023-02-10** and captured 2026-09-15, introduces credit/debit card acceptance and routes readers to channel-specific integration guides. It says Adyen supports **most**, not all, global and local card methods through one technical integration (raw lines 17–23). The primary Web/mobile collection and payment path belongs to [[adyen-online-payments]]; Pay by Link and in-person links are additional navigation. This page does not establish current merchant, card-brand, region, pricing, account or channel eligibility, or show an actual payment.

## Key takeaways

- For sensitive card data, the page offers Adyen PCI-compliant **client-side solutions** to collect and encrypt it, or submission of **raw card data if the merchant is fully PCI compliant** (raw line 25). This is a conditional choice, not proof that a custom integration meets PCI requirements or that card data was handled safely.
- **Depending on the integration**, Adyen **may require PCI DSS documents** before card payments can be accepted in **LIVE** (raw line 27). The page does not specify which configuration triggers that requirement or confirm that any merchant passed review.
- The page states that card payments are **captured immediately after authorisation by default**, with configurable capture delay or manual capture alternatives (raw line 29). Authorization and capture remain distinct events; this overview has no payment, capture, settlement or bank-receipt outcome.
- For 3D Secure card authentication, it links to separate integration guides (raw line 31). It says EEA and Australia integrations must comply with co-badged card regulations (raw lines 33–36); that is a dated provider statement, not a current legal determination or implementation proof.
- The navigation lists **Web, iOS, Android, React Native, Flutter and API only**, plus **Pay by Link and in-person** routes (raw lines 38–86). API only is described as building one's own UI for a website or iOS/Android app (raw lines 70–74). Those child pages own their actual prerequisites, versions and behavior; their link labels alone do not establish support or successful execution.

## Detail locators

- Purpose, geographic/pricing link and “most” card-method statement: raw lines 15–23.
- Card-data collection, PCI document gate, capture and 3DS/co-badged routes: raw lines 25–36.
- Channel-specific online, link and in-person navigation: raw lines 38–86.
- Other online-payment, authentication, capture and method references: raw lines 90–95.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-card-encryption]]
- [[co-badged-cards]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/2026-09-15|Full pinned Adyen Cards overview]]
