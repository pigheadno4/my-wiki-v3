---
title: "Adyen for Platforms onboarding guidelines"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/verification-requirements/onboarding-guidelines"
raw_files:
  - "adyen/docs/platforms/verification-requirements/onboarding-guidelines/2026-09-15.md"
tags: [adyen, platforms, onboarding, verification, kyc, country-requirements]
---

## Overview

This 2026-09-15 [[adyen]] for Platforms page gives onboarding best practices and selected country/region examples for identity, residency, organization/sole-proprietor and payout-bank verification. It explicitly says the page is **in development** and more countries/regions will be added. It is a dated provider guide for preparing user information, not a complete global requirements matrix, current legal advice, proof of verification, or evidence that account-holder capabilities are granted. [[adyen-platforms]]

## Key takeaways

- Adyen says it must verify a platform's users before processing their payments, paying out funds, or offering financial products. Incorrect or incomplete business information can delay onboarding and trigger requests for supporting documents. Identity and address checks may be automatic, with photo ID or residential-address proof requested if they fail. Organization legal name and registration number should match the official document/registry; a trading name is not a substitute. A bank document may be requested if automatic payout-bank verification fails. These are different user, legal-entity and bank-detail checks, not proof of a payout.
- Name/document conditions are specific: shortened names or initials may be submitted only when they appear on the ID; a marriage certificate for a married name absent from an ID is accepted only if issued after that ID. Organizations with a trading-name bank account must provide both correct trading and legal names. Sole proprietors may use an owner account or a trading-name account, subject to the stated ownership-form/name limits.
- **Australia:** the snapshot's Individuals tab calls for a bank document, while its Organizations and Sole proprietorships tabs specify registered-name and legal/registration-data rules. It says trusts are supported only in Australia and New Zealand in this snapshot, can use API or hosted onboarding, and require a trust deed plus at least settlor, trustee and beneficiary members, among other trust information. This is a dated platform-onboarding statement, not current trust-product availability.
- **Canada, France, Germany and UK:** the page gives entity-specific examples rather than one uniform rule. Canada requires a registration or constitutional document for organizations and describes hosted instant bank verification for individuals and organizations. France requires an ID for hosted-onboarded individuals, gives a limited extension for certain older French IDs (not those issued to under-18 cardholders), and requires full organization legal names rather than trading names. Germany describes hosted instant bank verification and exact organization legal names, while registered sole proprietors need correctly formatted registration numbers. The UK allows a CitizenCard for individual ID in this guide and requires a constitutional document for sole proprietorship verification. Refer to raw country sections for document examples and conditions.
- **United States:** the guide requires the last four SSN digits for individual users and presents full SSN, personal-data correction or SSN proof if verification with four digits fails. Hosted instant bank verification is described for individuals and companies, with bank-document review as an alternative; bank forms and checks have specific acceptance conditions. US organizations must use the full registered legal name; the page says EIN is the only accepted organization registration/tax number. Do not generalize these US rules to other countries or entity types.

## Detail locators

- **In-development scope and general KYC, name and bank-data guidance:** raw lines 15–59.
- **Australia individuals, organizations, sole proprietors and trust/member/deed conditions:** raw lines 61–122.
- **Canada document/instant-bank routes:** raw lines 124–150.
- **France ID, bank, organization and sole-proprietor conditions:** raw lines 152–200.
- **Germany and UK entity-specific conditions:** raw lines 202–260.
- **US individual SSN, bank and organization EIN conditions:** raw lines 262–306.

## Related

- [[adyen-platforms]]
- [[adyen-payouts]] — financial outcome remains a separate question

## Raw Sources

- [[raw/adyen/docs/platforms/verification-requirements/onboarding-guidelines/2026-09-15|Adyen Platforms onboarding guidelines — collected 2026-09-15]]
