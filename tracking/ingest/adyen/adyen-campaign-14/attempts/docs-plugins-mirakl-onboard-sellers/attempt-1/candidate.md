---
title: "Onboard sellers with the Adyen Mirakl connector"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/mirakl/onboard-sellers"
raw_files:
  - "adyen/docs/plugins/mirakl/onboard-sellers/2026-09-15.md"
tags: [adyen, mirakl, seller-onboarding, kyc]
---

## Overview

Adyen's Mirakl seller-onboarding page (last modified and captured 2026-09-15) describes how the connector submits seller details, produces a Hosted Onboarding Page (HOP) link, and synchronizes KYC status with Mirakl. It covers sellers offering products, services or both. This workflow description does not prove a particular seller's identity was verified, payout eligibility granted, funds received, or who is merchant of record. [[adyen-mirakl]] holds the connector and separate pay-in boundary.

## Key takeaways

- Each seller added to Mirakl undergoes KYC onboarding. If a seller has multiple shops for payments in different currencies, the page says Adyen treats each shop as a separate legal entity and each needs separate onboarding; do not merge their identities or infer shared eligibility (raw lines 19–21).
- Seller email and company legal-business name are supplied to create the Adyen legal entity, following the seller's country/region data format. Address components apply **when an address is provided**; State/Province is conditional on US or Canada. Bank currency, owner, country and IBAN apply **when a bank account is provided**, not as unconditional fields in this page (raw lines 25–45).
- The connector submits the seller information in a `/legalEntities` request. At the next sync it creates an HOP link visible under the Mirakl shop's **Additional Information → Hop Url** field. The seller answers connector-page security questions before redirection to Adyen HOP, where the account holder and any additional shareholders undergo KYC checks (raw lines 47–60). A created link or request is not completed verification.
- After checks, the connector synchronizes KYC status to Mirakl. The page describes passed-check and failed-check email paths, and lists in-process statuses **Awaiting KYC data**, **Awaiting KYC verification**, and **KYC failed**. These status and notification descriptions do not state that a particular seller can receive payouts or that a bank transfer succeeded (raw lines 62–73).
- To sync seller data, phone numbers must include `+` and country code, including on HOP. Mirakl requires Bank name and BIC, while Adyen HOP asks only for IBAN; if the seller supplies bank data via HOP, the connector syncs the IBAN to Adyen and fills Mirakl Bank name/BIC with dummy values. The page recommends entering bank details in Mirakl first. Dummy values and HOP submission are not bank-account verification or bank-receipt proof (raw lines 75–94).
- Payment-flow and payout/commission pages are next-step navigation, not payment or payout behavior established by this onboarding page (raw lines 96–108).

## Detail locators

- Seller/shop and legal-entity separation: raw lines 19–21.
- Country-format, conditional address and bank fields: raw lines 25–45.
- Legal-entity request, HOP creation, security and KYC flow: raw lines 47–60.
- KYC status and notification descriptions: raw lines 62–73.
- Phone and bank-data synchronization, dummy-value warning: raw lines 75–94.
- Payment and payout child routes: raw lines 96–108.

## Related

- [[adyen-mirakl]] — connector concept and separate pay-in boundary.
- [[adyen]] — provider page.

## Raw Sources

- [[raw/adyen/docs/plugins/mirakl/onboard-sellers/2026-09-15|Mirakl seller onboarding, captured 2026-09-15]]
