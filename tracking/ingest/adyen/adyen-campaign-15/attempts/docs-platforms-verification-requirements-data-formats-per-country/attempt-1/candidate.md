---
title: "Adyen platform legal-entity data formats by country and region"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/verification-requirements/data-formats-per-country"
raw_files:
  - "adyen/docs/platforms/verification-requirements/data-formats-per-country/2026-09-15.md"
tags: [adyen, platforms, issuing, verification, legal-entities, data-formats]
---

## Overview

This 2024-modified, 2026-09-15-captured Adyen reference lists accepted example formats for address, bank-account, identification, registration, VAT and tax data collected from legal entities by operating country/region and entity type. Its stated scope is Adyen for Platforms or Adyen issuing; it says there are no additional requirements, limitations or preparations for those integrations on this page. The format tables support data collection, not a guarantee of successful automatic verification, onboarding, compliance approval, account eligibility or payout. See [[adyen-platforms]] for the pending platform foundation route.

## Key takeaways

- Adyen says it automatically verifies most information, but verification can fail when data cannot be verified or is incorrect; it then asks the legal entity for additional documents. Accepted-looking syntax and illustrative table examples are therefore distinct from a verified identity or bank account.
- The country/region tables distinguish individuals, organizations, sole proprietorships, partnerships or trusts where applicable. Rows may be limited to a bank-account currency, a particular identifier kind, or an onboarding version; for example, Australia’s ACN and association/trust registration rows carry different version labels. Read the relevant row and column together rather than applying a single national pattern to every legal entity.
- In general, separator characters such as spaces, dashes, slashes and dots are optional in API-request values, but row-level instructions qualify that general rule: Sweden’s individual Personnummer and coordination-number rows mark a dash mandatory, Germany’s organizational Steuernummer says to remove the slash before sending, and Singapore’s bank-account row excludes separators and whitespace.
- Country-specific verification and transcription exceptions matter. The Canada footnote recommends collecting a Business Incorporation Number when available for automatic verification and requires a registration document when it is absent. Cyprus requires English equivalents of Greek registry-prefix characters by entity type. Italy accepts Codice Fiscale, CCIAA/REA or Partita IVA as a registration number, but CCIAA/REA can only be verified when a CCIAA document is provided.
- This is a dated format reference, not a current cross-country eligibility matrix. It does not say a formatted value is authentic, that a given country/entity is onboardable now, that submitted documents will pass review, or that funds can move.

## Detail locators

- Purpose, automatic-verification/document boundary, general separators and integration scope: pinned raw lines 5–27.
- Australia through Croatia, including onboarding-version column and Canada BIN footnote: pinned raw lines 29–103.
- Cyprus registry-prefix translation through Guernsey: pinned raw lines 104–217.
- Hong Kong through Italy, including Italy CCIAA document condition: pinned raw lines 218–279.
- Jersey through Singapore, with entity-specific registration, bank and tax rows: pinned raw lines 280–440.
- Slovakia through United States, including Sweden’s mandatory individual-number dash: pinned raw lines 441–529.

## Related

- [[adyen]]
- [[adyen-platforms]]
- [[adyen-index]]

## Raw Sources

- [[raw/adyen/docs/platforms/verification-requirements/data-formats-per-country/2026-09-15|Platform data formats per country/region snapshot (2026-09-15)]]
