---
title: "Onboarding v4 | Adyen Marketplaces"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/onboard-users/onboarding-versions/onboarding-v4"
raw_files:
  - "adyen/docs/marketplaces/onboard-users/onboarding-versions/onboarding-v4/2026-09-15.md"
tags: [adyen, marketplaces, platforms, onboarding, verification, legal-entity-management, v4]
---

## Overview

This 2025-modified, 2026-09-15-captured [[adyen]] Marketplace-path guide catalogs onboarding v4 changes for the modern Adyen for Platforms legal-entity flow, routed through [[adyen-platforms]]. It covers hosted and API-only field validation, entity and country conditions, and verification-error handling. It is a change overview, not a migration procedure or evidence that a particular user passed verification or acquired payment/payout capabilities. For version comparisons beyond this page, the raw points to onboarding-version guidance and the LEM API Diff Tool (raw lines 15–33).

## Key takeaways

- An individual cannot use a PO box as residential address; an organization may use one as its registered address only if it supplies a physical, non-PO-box principal place of business. The page lists corresponding verification suberrors/actions. It says a LEM API v4 DELETE `/documents/{id}` now returns 404, and a low-quality uploaded ID may produce a validation error; do not infer from that wording that a particular deletion succeeded or an ID passed checks (raw **Limitations on using a PO Box**, **Improvements for LEM API**, **Improved validation for ID document uploads**, lines 35–75).
- New name and address validations apply to both hosted and API-only onboarding, with entity-specific allowed characters, minimum lengths, and prohibited placeholder patterns. Use the raw **New validations on fields** section for the exact field list and exceptions (lines 77–191); a syntactically accepted field does not establish completed verification.
- The page limits underage onboarding for ages 13–18 with a legal representative to particular countries/regions. It says unincorporated partnerships became available **beginning with v3**, only in selected countries/regions and via LEM API. Organizations generally must provide a registration number before processing payments, while country sections give exceptions such as New Zealand organizations indicating `registrationNumberAbsent: true`. DBA-name absence may be declared through hosted onboarding or LEM API fields; if an organization has a principal-place-of-business address, its country must match the registered-address country (raw lines 193–236, 301–305).
- Country sections give conditional rules for Australia, Brazil, EU, Gibraltar, Hong Kong, New Zealand, Singapore, UK/Crown dependencies and US. Examples include EU/UK financial-report fields **only when offering business accounts**, Singapore users who **may** need Singpass or an alternative document route, and UK governing-law/director checks. Apply country, entity, product and onboarding-method qualifications in the raw, rather than treating the list as global or current law (raw **Requirements for specific countries/regions**, lines 238–406). Hosted onboarding also adds a ticker-symbol path for publicly listed companies (lines 408–416).

## Detail locators

- PO-box verification codes/remediating actions, LEM DELETE link and sample low-quality-ID `422` validation response: raw lines 35–75.
- Exact name/address fields, rejected patterns, allowed symbols, length exceptions and fictitious-value list: raw lines 77–191.
- Ages, v3 partnership origin, pre-payment registration number, DBA-absence fields and principal-address country condition: raw lines 193–236.
- Country/region tables, optional/absent-number fields, nominee and natural-person checks, Singpass alternative, director proof and hosted ticker: raw lines 238–416.

## Related

- [[adyen-platforms]] — modern Platforms onboarding and verification source route.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/onboard-users/onboarding-versions/onboarding-v4/2026-09-15|Onboarding v4, captured 2026-09-15]]
