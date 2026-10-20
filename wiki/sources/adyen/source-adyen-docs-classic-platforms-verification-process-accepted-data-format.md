---
title: "Classic Platforms accepted verification data formats"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/verification-process/accepted-data-format"
raw_files:
  - "adyen/docs/classic-platforms/verification-process/accepted-data-format/2026-09-15.md"
tags: [adyen, classic-platforms, verification, data-formats, bank-accounts]
---

## Overview

This Classic Adyen for Platforms reference (last modified 2023-08-04; captured 2026-09-15) lists identity, organization registration/tax, and payout-bank data formats and examples used in account-holder verification. The page explicitly directs new integrations to a different guide. Use it for the **Classic** model under [[adyen-classic-platforms]], with provider context at [[adyen]]; its examples do not prove current eligibility or verification approval.

## Key takeaways

- For individuals, the page rejects PO boxes as addresses and asks for a name matching photo ID if an ID must later be submitted. For people associated with an organization, it defines owners as individuals directly or indirectly holding **25% or more** of shares, votes or equity and asks for all who meet that threshold (zero to four). If none do, a controller must be provided. Controllers include people with ultimate effective control or, if none can be identified, senior management; at least one is required. At least one signatory must be identified, and all signatories are required (raw lines 23–38).
- National ID numbers are required in **some** countries and strongly recommended in others; the page does not mark which countries fall into each group. Its country-by-country ID types and illustrative strings are at raw lines 40–53. For Australian individuals it lists ID, passport, visa or driver’s licence, with issuer state **recommended** for a driver’s licence (raw lines 55–59). Failed automatic verification may lead Adyen to ask for another document (raw line 42).
- For organizations (businesses, nonprofits, partnerships and public companies), PO boxes are likewise rejected. The registration-number table is at raw lines 61–111. Some nonprofits without a registration number can upload documents; additional documents can also follow failed automatic verification (raw lines 69–71). Do not treat example strings as proof that a specific submitted identifier passes verification.
- A **business legal-entity-type** account holder that has processed payments at a **higher tier** must provide a company TIN. The page says either listed TIN may be provided where two exist and that, for countries outside its list, the TIN and business registration number are the same; the country table is at raw lines 113–132. For a business that is a 100% subsidiary of a company listed on a public exchange or other regulated market, it calls for the exchange and links a separate supported-exchange spreadsheet (raw lines 134–138).
- Adyen says it checks bank-account existence and account-holder ownership for each bank account added as a payout method. The bank owner’s name should match the account holder’s, and bank country should match its operating country (raw lines 140–147). Where IBAN is available, the page accepts either IBAN or bank code plus branch code plus account number; branch code may be required in some countries, with US routing-number and UK sort-code examples (raw lines 149–163). These are submitted-format rules, not bank verification or payout evidence.

## Detail locators

- Organization-linked individual roles and minima: raw lines 30–38. Country ID examples and Australian document route: raw lines 40–59.
- Organization registration identifiers, country table and conditional nonprofit documents: raw lines 61–111. TIN condition and country examples: raw lines 113–132.
- Stock-exchange condition and external spreadsheet navigation: raw lines 134–138. This entry does not assert the contents of that spreadsheet.
- Bank ownership/country match, IBAN alternative, and branch-code examples: raw lines 140–163.

## Related

- [[adyen-classic-platforms]] — Classic model and source route.
- [[adyen]] — provider.
- [[adyen-index]] — provider index.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/verification-process/accepted-data-format/2026-09-15|Classic Platforms accepted data formats, captured 2026-09-15]]
