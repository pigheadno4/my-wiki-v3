---
title: "Determine the verification requirements | Adyen Business accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/verification-requirements"
raw_files:
  - "adyen/docs/business-accounts/verification-requirements/2026-09-15.md"
tags: [adyen, business-accounts, verification, onboarding, us]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] Business accounts guide identifies additional user data and US-specific onboarding disclosures/acceptances for Business accounts verification. Requirements vary with product, country/region and legal-entity type. See [[adyen-business-accounts]] for the product route. Collecting fields or showing copy starts a verification process; it is not evidence of successful KYC, enabled capabilities, approved eligibility or an opened Adyen bank account.

## Key takeaways

- The page says Business accounts can require additional checks beyond ordinary Platforms onboarding, and users must provide the associated information before relevant Business-account capabilities can be assigned **after successful checks**. Baseline information varies by country/region and legal-entity type; the linked country/type and detailed-document guides own those conditions. [Raw: lines 19–27]
- Beyond the applicable baseline, the captured list includes registered industry, website URL **if** there is an online presence, source of funds, FATCA/CRS classification for organizations (business type and main income), tax-residence country and ID for organization and associated individuals or sole-proprietorship owner, and source-of-wealth data **only if Adyen determines it is needed and informs the platform**. A live selfie and photo ID are specified for **each organization signatory** or **individual legal entity owning a sole proprietorship**. Do not recast conditional items as universally required for every user or individual. [Raw: lines 25–35]
- The linked additional-capabilities reference says FATCA/CRS self-certification is **not required for US-based legal entities applying for US business bank accounts**. This broad page's organization-classification bullet does not mention that exception; the two pages should be read together before making a US data-collection rule. Neither provides a user's actual tax classification or current legal advice. [This raw: line 32; linked reference: `reference-additional-products/2026-09-15.md`, lines 21–30]
- For users in the **US**, Adyen says the platform must include its listed items in onboarding and Adyen will check the flow. Business accounts are stated unavailable to governmental organizations, including SOEs, in the US. The Patriot Act/CIP disclosure and reason for information collection must be shown **before any personal information is collected**; exact prescribed copy is in the raw table. This is historical product guidance and does not establish current US legal or Adyen eligibility. [Raw: lines 37–45]
- The US table says every account holder must accept Adyen Business Account Terms of Service before opening, with a copy supplied alongside acceptance and the authorized representative/privacy statement language shown there. It also calls for Regulation GG internet-gambling certification before opening, **when** the Terms of Service are accepted. Those are distinct steps; an onboarding display or checkbox does not prove a valid acceptance, certification, passed verification or account opening. [Raw: lines 43–47]

## Detail locators

- Product-dependent checks, successful-check-before-capability boundary and baseline country/entity route: raw lines 19–27.
- Additional conditional industry, website, SOF, organization FATCA/CRS, tax, wealth and signatory/sole-owner document data: raw lines 29–35.
- US government-entity exclusion, CIP text/timing, ToS copy/acceptance and Regulation GG timing: raw lines 37–47.
- Onboarding next-step route: raw lines 49–55.
- Related reference's narrow US FATCA/CRS exception: `raw/adyen/docs/business-accounts/verification-requirements/reference-additional-products/2026-09-15.md` lines 21–30 (separately pinned/read).

## Related

- [[adyen-business-accounts]] — product and verification evidence boundary
- [Additional capabilities reference](https://docs.adyen.com/business-accounts/verification-requirements/reference-additional-products) — FATCA/CRS exception, industry and SOF detail
- [Document requirements](https://docs.adyen.com/business-accounts/verification-requirements/document-requirements) — document conditions
- [Business Account Terms of Service](https://docs.adyen.com/business-accounts/onboard-users/terms-of-service) — acceptance flow
- [Onboard users](https://docs.adyen.com/business-accounts/onboard-users) — next-step process

## Raw Sources

- [[raw/adyen/docs/business-accounts/verification-requirements/2026-09-15|Adyen Business accounts verification requirements — collected 2026-09-15]]

## Related raw API references

- [[raw/adyen/docs/business-accounts/verification-requirements/reference-additional-products/2026-09-15|Related detailed FATCA/CRS and SOF reference]]
