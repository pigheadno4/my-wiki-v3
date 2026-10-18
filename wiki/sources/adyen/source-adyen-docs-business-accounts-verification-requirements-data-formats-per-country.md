---
title: "Adyen Business Accounts verification data formats by country"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/verification-requirements/data-formats-per-country"
raw_files:
  - "adyen/docs/business-accounts/verification-requirements/data-formats-per-country/2026-09-15.md"
tags: [adyen, business-accounts, platforms, verification, country-formats, legal-entities]
---

## Overview

This Adyen reference (last modified 2024-03-25, captured 2026-09-15) tabulates accepted **data formats and examples** for legal-entity information by operating country/region. It covers address, bank-account and person/entity identification, registration, VAT and tax-number fields. Its countries and example values are format lookup material, not a Business Accounts availability, legal-entity eligibility, universally required-field or KYC-approval list.

## Key takeaways

- The tables cover Belgium, France, Germany, Netherlands, Spain, United Kingdom and United States. Rows are divided by data subject and field: addresses, bank accounts, individuals, organizations, sole proprietorships, and in the UK partnerships. Country-specific examples include IBAN and local account fields, personal ID/tax numbers, organization registration/VAT/tax numbers, and US state/postal/routing/account formats. Select the **country, legal-entity category and field** before using a format; the table's presence does not mean every field is required of every user or that every table country is available to every product integration.
- The guide says Adyen automatically verifies most information. If automatic verification fails because data cannot be verified or is incorrect, Adyen may ask the legal entity for additional documents. An accepted syntactic format or submitted document is not a completed verification result.
- Spaces, dashes, slashes and dots used as separators are generally described as optional in API requests, **but use field-specific instructions**: the Germany organization tax-ID row explicitly says to remove `/` before sending. Do not flatten this exception into a universal separator rule.
- The page's “Requirements” says no **additional requirements, limitations or preparations for using this reference** with an Adyen for Platforms or Adyen Issuing integration. It does not waive KYC, Business Accounts product eligibility, capability requirements or legal-entity checks. Issuing is named as a second scope; a table row alone does not establish Business Accounts support.
- Preserve the table's examples as examples, especially its compound/awkward rows: Spain's DNI/NIE formatting puts alternatives in a single row, with examples for residents, non-residents, minors and foreigners; UK organizations and partnerships have distinct registration/tax rows; US driver's-license length varies by state and SSN accepts full nine or last four digits in the captured table. These are dated input-format descriptions, not a runtime validation schema or current identity-document advice.

## Detail locators

- Opening and `## Requirements`: purpose, automatic verification/additional documents, optional separator statement, Platforms/Issuing reference scope.
- `## Belgium`, `## France`, `## Germany`, `## Netherlands`: address/IBAN and person/organization/sole-proprietor format examples; Germany tax-ID slash instruction.
- `## Spain`: DNI/NIE and organization/sole-proprietor NIF/VAT rows with compound alternatives.
- `## United Kingdom`: postal/IBAN/GBP sort-code/account fields and individual, organization, sole-proprietor and partnership identifiers.
- `## United States`: ZIP/state, routing/account, SSN/driver's-license and EIN formats.

## Related

- [[adyen-business-accounts]] — main Business Accounts concept and separate dated eligibility context.
- [[adyen-platforms]] — Platforms verification/resource context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/business-accounts/verification-requirements/data-formats-per-country/2026-09-15|Adyen data formats per country/region (fetched 2026-09-15)]]
