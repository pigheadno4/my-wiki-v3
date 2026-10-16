---
title: "Determine platform verification requirements | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/verification-requirements"
raw_files:
  - "adyen/docs/platforms/verification-requirements/2026-09-15.md"
tags: [adyen, platforms, verification, legal-entities, onboarding, financial-products]
---

## Overview

This 2026-09-15 capture of a 2023-modified [[adyen]] guide helps an Adyen for Platforms or Issuing integration determine **which user information to collect and submit to start verification**. The factors are the user's country/region of operation, legal-entity type, and financial products offered. Its requirements and availability statements are historical documentation, not a current compliance determination, verified account status, enabled capability, completed onboarding, or money-movement proof. [[adyen-platforms]]

## Key takeaways

- The page says an Adyen for Platforms or Issuing integration has no **additional** preparation listed in its Requirements section; that does not waive the verification information described throughout the page. Country rules differ, and a separate minimum-information guide owns exact country/entity fields. Minor users are limited to Legal Entity Management API v3/v4, with age/residency rules: under 13 cannot be onboarded; eligible 13–18 or 16–18 cases need a legal representative also onboarded as authorised signatory, while Hong Kong and Singapore under-18 cases are excluded in this snapshot. The representative's identity, relationship and consent details, and possible ID follow-up, are in the raw. See raw lines 19–63.
- The **main legal entity** is the user with a contractual relationship with the platform. The guide requires information about that entity plus associated entities, such as separately created and linked owners of a private company. Country-by-entity support is a matrix, not general eligibility. Organization checks include relevant UBOs/controllers/signatories and region-qualified directors; individual legal entities are described as payment-facilitator-only. Trusts are listed only for Australia/New Zealand, and unincorporated partnerships have their own country list, document and partner-association rules; incorporated partnerships route to organizations. See raw lines 65–310.
- Processing payments and payouts are described as included by default in this verification guide, while optional financial products can add checks. **Business accounts** are limited here to organizations/sole proprietorships with both entity and associated individuals in the listed BE/DE/ES/FR/GB/NL/US countries, with extra industry, tax, source-of-funds/wealth and identity information. US business-account onboarding adds disclosure, terms/certification timing and excludes governmental organizations including SOEs. These are requirements for the stated product, not proof a user's business account is open. See raw lines 311–350.
- **Card issuing** has a separate EEA/UK/US and organization/sole-proprietorship scope, with VAT/tax-ID and source-of-funds additions. Its low/medium/high capability table gives per-card, per-day thresholds and may entail more checks and monitoring; a listed level is not an actual granted capability. **Capital** is invite-only in supported countries for organizations/sole proprietorships and is said to require no additional verification checks because of risk assessment and limited availability; baseline verification still applies. See raw lines 352–386.
- This source does not establish a legal seller or merchant of record, ownership of a balance account, liable/reserve account allocation, a transfer instrument, a person's verified state, or whether an account can process or receive payouts. Those require the appropriate current account and capability evidence. See raw lines 19–25, 65–69, 311–317.

## Detail locators

- **Three requirement axes, country rules and minors:** raw lines 15–63.
- **Legal-entity support matrix and organization/individual/sole-proprietor rules:** raw lines 65–177.
- **Trust and partnership identities, country lists and associations:** raw lines 179–310.
- **Business-account product and US disclosure/eligibility conditions:** raw lines 311–350.
- **Issuing levels and Capital invite-only exception:** raw lines 352–386.

## Related

- [[adyen]]
- [[adyen-platforms]]
- [[adyen-financial-products]]

## Raw Sources

- [[raw/adyen/docs/platforms/verification-requirements/2026-09-15|Adyen platform verification requirements — collected 2026-09-15]]
