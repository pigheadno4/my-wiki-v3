---
title: "Adyen peak-season in-person payment preparation"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/industries/peak-season/in-person-payments"
raw_files:
  - "adyen/docs/industries/peak-season/in-person-payments/2026-09-15.md"
tags: [adyen, point-of-sale, peak-season, terminals, offline-payments]
---

## Overview

This Adyen in-person **peak-season preparation guide** addresses payment-method review, terminal fleets and Mobile devices, software versions, offline resilience, cellular failover, and regional live cloud Terminal API endpoints. It is operational planning advice in a 2026-09-15 snapshot, with terminal-software details expressly scoped to the **2025 Christmas and end-of-year peak season**. It does not show an account's settings, device readiness, payment authorization, capture, or settlement.

## Key takeaways

- Review regional payment-method and accepted-currency settings, refund/chargeback fit, and test methods ahead of the rush. Adyen advises against adding methods immediately before peak season because testing takes time. Mobile solutions do not support every method available on Adyen terminals. Manual key entry is a suggested fallback when chip, NFC, and swipe cannot read a card; its separate configuration guide controls setup.
- Order terminals early enough for delivery, assignment, boarding, and testing. Prepare backup devices; recharge stored terminal batteries and check internet, battery, and basic functionality. Mobile devices must meet their Android or iOS solution's separate requirements.
- Check terminal software and Mobile SDK versions. The listed terminal version recommendations and automatic-rollout pauses are dated **2025-season guidance**, not proof of any terminal's current installed version. The raw's second no-rollout interval reads `December 22, 2026 - January 4, 2026`, an internally reversed range; verify any scheduling decision with Adyen rather than normalizing it. The page says each Mobile SDK version expires six months after release, without proving which version is currently available.
- Internet access is ordinarily needed for transactions. The page recommends enabling offline payments for a temporary outage, distinguishing terminal **Offline EMV** (card/issuer-dependent) from **Store and forward** (terminal approval without verification and higher issuer-decline risk). Mobile offline Store and forward requires prior device-security attestation by Adyen's platform and cannot complete offline transactions with PIN. These paths do not establish eventual issuer approval or funds.
- Cellular failover switches a capable terminal from its primary internet connection to cellular, subject to the separate scenario and configuration guides. For a **live cloud-communication Terminal API** integration, Adyen recommends the geographically closest correct regional endpoint for each store/integration; this is guidance, not evidence of deployed endpoint choice or connectivity.

## Detail locators

- Raw lines 25–41, `Payment methods` and `Configure manual key entry`: method, region/currency, testing, Mobile-method and MKE qualifications.
- Raw lines 43–65, `Hardware`: ordering lead time, assignment/boarding, backup hardware and terminal checks.
- Raw lines 67–102, `Software`: 2025-season terminal freeze/version table, internally inconsistent date, six-month Mobile SDK expiry and device updates.
- Raw lines 104–119, `Offline payments`: terminal Offline EMV versus Store and forward, Mobile prior-attestation and no-offline-PIN conditions.
- Raw lines 121–133, `Cellular failover` and `Regional endpoints for cloud communication`: network fallback and live cloud endpoint scope.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-management]] — fleet ordering, assignment, boarding and software administration.
- [[adyen-terminal-api]] — distinct POS message and cloud-communication integration boundary.
- [[adyen-mobile-pos]] — Mobile solution requirements and SDK routes.

## Raw Sources

- [[raw/adyen/docs/industries/peak-season/in-person-payments/2026-09-15|Peak-season in-person payments, fetched 2026-09-15]]
