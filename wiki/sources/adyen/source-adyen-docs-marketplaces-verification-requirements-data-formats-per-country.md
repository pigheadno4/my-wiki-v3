---
title: "Adyen Marketplace data formats per country/region"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/verification-requirements/data-formats-per-country"
raw_files:
  - "adyen/docs/marketplaces/verification-requirements/data-formats-per-country/2026-09-15.md"
tags: [adyen, marketplaces, platforms, verification, data-formats]
---

## Overview

This 2023-modified, 2026-09-15-captured Marketplace-path reference lists accepted example formats for legal-entity data by operating country or region. Its Requirements section says an existing Adyen for Platforms or Adyen issuing integration has no additional requirements, limitations, or preparations for this reference; the page does not establish live eligibility, verification success, or financial-product approval. [[adyen]] [[adyen-platforms]] (raw lines 15–27)

## Key takeaways

- Adyen says it automatically verifies most information, but failed verification or incorrect/unverifiable data can lead to a request for additional documents. The format table is an input reference, not proof that a legal entity has passed verification. (raw lines 19–21)
- The opening rule says separator characters such as spaces, dashes, slashes, and dots are optional in API request values. Apply country/field-specific rows where they say otherwise: Singapore bank-account numbers must have no separators or whitespace, while Sweden's individual personnummer and coordination-number identification/tax-ID rows mark the dash mandatory. These statements should not be flattened into one universal separator rule. (raw lines 23, 426–431, 476–487)
- Australia's registration-number rows carry onboarding-version qualifiers: an ACN for organizations/sole proprietorships is marked v4; incorporated-association numbers v1–v4; trust registration formats v1–v3 and ACN v4. (raw lines 29–44)
- For Canada, the page recommends collecting the Business Incorporation Number when available for automatic verification and says a registration document must be uploaded without one. Cyprus registry numbers shown with Greek prefixes must be submitted with the corresponding English C, O, or P equivalent. Italy accepts C.F., CCIAA/REA, or Partita IVA as a registration number, but says CCIAA/REA can only be verified with a CCIAA document. (raw lines 79–91, 104–120, 262–278)

## Detail locators

- Country tables cover addresses, bank accounts, individual identification and tax IDs, and organization/sole-proprietor registration, VAT, and tax fields. Use the exact country and entity/field row before implementing a format; the tables contain differing character counts, prefixes, allowed separators, and example values. Australia–Denmark: raw lines 29–144; Estonia–Ireland: 146–252; Isle of Man–Malta: 254–339; Netherlands–Romania: 341–424; Singapore–United States: 426–529.
- The US table includes a full nine-digit or last-four-digit SSN format for individual identification, plus routing/account-number and EIN rows; this is a table format, not a statement about acceptable verification evidence or live account capability. (raw lines 518–529)

## Related

- [[adyen-platforms]] — Existing Adyen for Platforms concept; this Marketplace-path page is a country-format reference, not a Classic Platforms resource.

## Raw Sources

- [[raw/adyen/docs/marketplaces/verification-requirements/data-formats-per-country/2026-09-15|Marketplace data formats per country/region, captured 2026-09-15]]
