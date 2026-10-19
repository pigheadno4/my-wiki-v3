---
title: "Adyen Issuing: Determine verification requirements"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/verification-requirements"
raw_files:
  - "adyen/docs/issuing/verification-requirements/2026-09-15.md"
tags: [adyen, issuing, verification, kyc, onboarding]
---

## Overview

This Adyen guide (last modified 2021-02-24, captured 2026-09-15) explains how to determine verification information to collect for an Adyen Issuing or Adyen for Platforms user. Requirements vary by country/region of operation, legal-entity type and requested card-issuing capability level. It routes country/entity-specific minimum data to a separate reference and says card issuance also requires the user's VAT number, or tax ID where there is no VAT system. Its tables are dated documentation, not a current eligibility, legal or capability decision.

## Key takeaways

- Establish the **main legal entity** holding the contractual relationship, collect its information, and create/link individual legal entities for associated owners where applicable. The page describes organization, individual and sole-proprietorship categories and a country-by-entity support matrix (raw lines 67-113, 115-196). Consult the linked minimum-required-information reference for country-specific fields rather than treating the page's general lists as complete.
- Minor onboarding is described as possible only with Legal Entity Management API v3 or v4 and Adyen contact. Under 13 cannot be onboarded. The snapshot's residency table says EU (including Norway, Switzerland and UK) ages 16–18 and Australia/Canada/US ages 13–18 may be onboarded with a legal representative who is also onboarded as an authorized signatory; Hong Kong and Singapore under-18s cannot. The representative information, consent statement and possible ID request appear at raw lines 39-65. These are dated provider statements, not current legal advice.
- For organizations, the snapshot identifies ownership UBOs at 25% or more, control UBOs if ownership identifies none (and for US organizations), at least one signatory, and country-specific director requirements. All qualifying ownership UBOs must be identified; certain foreign-resident associated individuals may require extra due diligence or be unacceptable under Adyen's risk tolerance (raw lines 128-149). Confirm individual/entity acceptance with Adyen.
- A multiple-card-user/one-balance-account scenario may verify only the account holder; the page directs the platform to discuss and confirm that use case with Adyen, so it is not a blanket exemption for named card users (raw lines 198-202).
- Card-issuing `withdrawFromAtm`, `withdrawFromAtmInRestrictedCountries`, `useCardInRestrictedCountries` and `useCardInRestrictedIndustries` are mapped to low, medium or high levels. Amount thresholds are **per card, per day**; higher levels may require more checks and monitoring. Exact dated values and `0`/`>0` distinctions remain in the raw table (raw lines 204-213). A level does not prove that a particular card or authorization is active/allowed.

## Material qualification

The page's general Issuing statement says to collect a VAT number, or a tax ID where there is no VAT system (raw line 25), while its sole-proprietorship general list says VAT number **if the business has VAT registration** (raw lines 186-196). The page does not reconcile the two scopes; keep both conditions and confirm the relevant country/entity requirement in the referenced detailed guide and with Adyen. The source also contains an incomplete phrase about the main entity's contractual counterparty (raw line 71), so no missing party is inferred.

## Detail locators

- Country/region examples and linked detailed KYC reference: raw lines 33-37. Legal-entity support matrix: raw lines 75-111. General organization, individual and sole-proprietorship collection lists: raw lines 115-196. UBO ID-number country list: raw lines 151-171.

## Related

- [[adyen]] — provider.
- [[adyen-issuing]] — Issuing concept and source route.

## Raw Sources

- [[raw/adyen/docs/issuing/verification-requirements/2026-09-15|2026-09-15 capture of Adyen Issuing verification requirements]]
