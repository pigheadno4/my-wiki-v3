---
title: "Adyen Issuing verification: data formats per country/region"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/verification-requirements/data-formats-per-country"
raw_files:
  - "adyen/docs/issuing/verification-requirements/data-formats-per-country/2026-09-15.md"
tags: [adyen, issuing, verification, data-formats]
---

## Overview

Adyen's data-format reference lists accepted formats and examples for information collected from legal entities by the country or region where they operate. It covers addresses, bank accounts, individual identification or tax information, and organization or sole-proprietorship registration and tax numbers where listed. This is a 2026-09-15 capture of a page marked last modified 2024-03-22; it is format guidance for [[adyen-issuing]] and also addresses Adyen for Platforms integrations, not proof of current eligibility or successful verification.

## Key takeaways

- Under "Requirements," the page says an existing Adyen for Platforms or Adyen Issuing integration needs no additional preparation for this reference. That statement does not establish an integration or live eligibility.
- Adyen says it automatically verifies most information. If automatic verification fails because data cannot be verified or is incorrect, Adyen asks legal entities for additional documents. Canada specifically recommends collecting the Business Incorporation Number when available for automatic verification and requires a registration document without one (raw line 86). Italy says CCIAA/REA registration numbers can only be verified if a CCIAA document is supplied (raw line 240).
- The introductory statement says separator characters in API values are optional, but the country rows contain narrower instructions: Singapore bank account numbers must have no separators or whitespace (raw line 373), while Sweden's individual personnummer and coordination-number rows label the dash mandatory (raw lines 422–423). Follow the applicable country and field row rather than treating the introductory sentence as universal.
- Cyprus accepts the corresponding English prefix for entity registration numbers shown with Greek characters on registry documents; see the entity-type mapping (raw lines 105, 108–114). Australian registration-number rows distinguish onboarding v1/v2/v3/v4 from v4 for specified entity types (raw lines 40–44). These version labels belong to those rows.

## Detail locators

- Introductory purpose, verification and separator statements: raw lines 15–27.
- Australia through Finland: raw country headings and tables, lines 29–155; Canada documentation condition at line 86 and Cyprus prefix conversion at lines 108–114.
- France through Norway: raw country headings and tables, lines 157–333; Italy CCIAA verification condition at line 240.
- Poland through United States: raw country headings and tables, lines 335–452; Singapore separator restriction at line 373 and Sweden's mandatory dash at lines 422–423. Consult each row for entity type, field, format, example, and any currency or onboarding-version qualifier.

## Related

- [[adyen]] — provider context.
- [[adyen-issuing]] — Issuing topic route.

## Raw Sources

- [[raw/adyen/docs/issuing/verification-requirements/data-formats-per-country/2026-09-15|Adyen country and region data formats, captured 2026-09-15]]
