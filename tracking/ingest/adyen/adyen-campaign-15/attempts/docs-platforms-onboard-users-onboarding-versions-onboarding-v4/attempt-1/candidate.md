---
title: "Adyen Platforms onboarding v4 changes"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4"
raw_files:
  - "adyen/docs/platforms/onboard-users/onboarding-versions/onboarding-v4/2026-09-15.md"
tags: [adyen, platforms, onboarding, legal-entity-management, verification, v4]
---

## Overview

This Adyen **Platforms onboarding v4** page catalogs changes to legal-entity data and validation for hosted and API-only onboarding, with country/entity exceptions and separate financial-product sections. It is a 2025-modified guide captured 2026-09-15, not a migration procedure, a verification result or proof of current user eligibility, capability activation or money movement. Use the linked onboarding-version and API-diff routes for version comparisons beyond the changes listed here.

## Key takeaways

- v4 limits PO-box use: individuals cannot give one as residential address; an organization may use one as registered address only while also providing a physical, non-PO-box principal place of business. The LEM API section says DELETE `/documents/{id}` now returns **404**; document-upload validation can return a low-quality-ID error. New name/address-field validation applies to hosted and API-only onboarding. Check the exact field and verification-error tables rather than assuming any submitted entity has passed checks.
- Underage users aged **13–18** can be onboarded with a legal representative only in particular countries/regions. Unincorporated partnerships are stated as available **beginning with v3**, in selected regions, and **LEM API only**; they are not a universal v4 hosted-onboarding addition. Organizations generally must provide a registration number before processing payments, while country sections include exceptions such as New Zealand organizations using `registrationNumberAbsent: true`.
- Organizations and legal arrangements must identify whether a Doing Business As name differs from the registered name or indicate absence, using hosted onboarding or the corresponding LEM API `doingBusinessAsAbsent` field. If an organization has a principal-place-of-business address, its country must match its registered-address country. For the **platform model**, users must supply a support phone number and email, with entity-specific placement for sole proprietorships, trusts and unincorporated partnerships. These are information/verification conditions, not proof of consent, role assignment or an enabled payment capability.
- Country sections distinguish Australia registration/tax and optionality rules; cross-border associated-entity ID-document requirements in Brazil, Hong Kong, Singapore and the US; EU and UK business-account financial information; New Zealand nominee/natural-person checks; Singapore possible Singpass or separate document route; UK governing-law/director checks; and Gibraltar/UK Crown dependency tax-ID alternatives. Apply the relevant entity, country, onboarding method and product condition rather than treating the list as universal.
- **Financial-product-only changes:** card issuing requires an issuing business line with industry code. Business accounts and issuing require Adyen to verify source of funds and may require supporting documents; the LEM API business-line service is `banking` for business accounts or `issuing` for issuing. If funds were not Adyen-processed, the page requires source-of-funds type and description. These requirements do not by themselves confirm business-account or card-issuing approval.

## Detail locators

- Opening and `## Limitations on using a PO Box as an address` — v4 scope, version/API-diff navigation, individual versus organization address rule and error codes.
- `## Improvements for Legal Entity Management API`, `## Improved validation for ID document uploads`, `## New validations on fields` — DELETE response change, low-quality document response example, hosted/API-only name and address validation; exact allowed characters and prohibited placeholders are in raw.
- `## Onboarding underage users` through `## Requirements for principal place of business` — age/region/legal representative, v3-origin partnership rule, registration timing, DBA absence and principal-place-country conditions.
- `## Requirements for specific countries/regions` — separate Australia, Brazil, EU, Gibraltar, Hong Kong, New Zealand, Singapore, UK, UK Crown dependencies and US rules; exact field formats and remedial error tables in raw.
- `## Support email and phone numbers` / `## Updates for hosted onboarding` — platform-model support contacts and hosted public-company ticker.
- `## Requirement for business lines and industry codes for issuing` / `## Source of funds for business accounts and issuing` — product-only business lines, SOF flags, possible documents and detailed evidence table.

## Related

- Company: [[adyen]]
- Platforms concept: [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/docs/platforms/onboard-users/onboarding-versions/onboarding-v4/2026-09-15|2026-09-15 Platforms onboarding v4 changes]]
