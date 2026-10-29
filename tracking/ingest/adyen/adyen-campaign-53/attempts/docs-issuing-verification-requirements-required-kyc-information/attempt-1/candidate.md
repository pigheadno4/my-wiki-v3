---
title: "Adyen Issuing required KYC information by entity and country"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/verification-requirements/required-kyc-information"
raw_files:
  - "adyen/docs/issuing/verification-requirements/required-kyc-information/2026-09-15.md"
tags: [adyen, issuing, kyc, verification]
---

## Overview

This Adyen Issuing verification-requirements page is a country/region and legal-entity field matrix for information to collect from an account holder for verification checks. It is a 2026-09-15 capture of a page marked last modified 2023-03-13; use it as dated provider documentation, not as a current legal checklist. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The page says required information varies with the account holder's legal entity type and country/region of operation. Its four tabs are **individuals, organization, sole proprietorship, and trust**. The trust table in this capture has an Australia column only. See raw lines 17–23, 41–45, 96–99, 154–157, 177–207.
- The legend distinguishes **Required** (minimum information for KYC checks), **Conditionally required** (particular setups and financial products), **Optional** (recommended), and **Not applicable**. These are per-cell statuses, not a universal field list. See raw lines 25–39.
- The individual matrix includes name, personal/ID and document data, residential address, contact, bank-account identification, bank documents, and an entity-association field. The organization matrix includes organization and tax details, registered and principal-business addresses, stock information, bank details/documents, and association type/job title. Sole-proprietorship and Australia-only trust matrices provide their own entity, address, tax, and association fields. See raw lines 43–94, 96–152, 154–175, 177–207.
- The page points to a separate country/region data-format guide and a downloadable all-country requirements file; this capture does not reproduce those materials. See raw lines 19–21.

> [!warning] Scope of the captured matrix
> Several cells say “More info” without their conditional explanation in this Markdown capture. The table names an `individual.identificationData.nationalIdExempt` field (raw line 53), but that does not state a blanket KYC exemption. It has association-type fields for individuals, organizations, and trusts (raw lines 94, 151–152, 205–207), but does not enumerate UBO, controller, or signatory eligibility rules. Consult the linked verification-requirements and document guides for those distinct decisions; do not infer a complete onboarding or legal requirement from this matrix alone.

## Detail locators

- Status legend and legal-entity selector: raw lines 17–43.
- Individual country matrix (35 country/region columns), including country-specific ID/document/bank/association status: raw lines 45–94.
- Organization country matrix (same 35 columns), including registered versus conditional principal-business address, stock, bank, document, and association rows: raw lines 96–152.
- Sole-proprietorship country matrix, including conditional registration/VAT/principal-business rows: raw lines 154–175.
- Australia-only trust matrix, including entity/tax/address/association rows: raw lines 177–207.

## Related

- [[adyen-issuing]] — Issuing product context.
- [[source-adyen-docs-issuing-verification-requirements]] — separate guide to determine verification requirements.
- [[source-adyen-docs-issuing-verification-requirements-data-formats-per-country]] — field formats by country/region.
- [[source-adyen-docs-issuing-verification-requirements-document-requirements]] — document-upload requirements.

## Raw Sources

- [[raw/adyen/docs/issuing/verification-requirements/required-kyc-information/2026-09-15|Full pinned Issuing KYC field matrix]]
