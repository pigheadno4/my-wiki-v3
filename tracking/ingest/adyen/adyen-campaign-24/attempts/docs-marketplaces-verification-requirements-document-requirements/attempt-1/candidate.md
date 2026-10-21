---
title: "Adyen Marketplaces verification document-upload requirements"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/verification-requirements/document-requirements"
raw_files:
  - "adyen/docs/marketplaces/verification-requirements/document-requirements/2026-09-15.md"
tags: [adyen, marketplaces, verification, documents, onboarding]
---

## Overview

This Marketplaces-path Adyen guide (last modified 2023-11-29; captured 2026-09-15) catalogs documents Adyen **may request when automatic legal-entity or bank-account verification fails**, with document-specific contents, format, recency and product/version conditions. It says Adyen for Platforms or Issuing integrations have no additional preparation requirement for this page (raw line 25); that does not erase the conditions within particular document sections. See [[adyen-platforms]] and [[adyen]].

## Key takeaways

- Submit **original, unedited** documents. The page says to reject AI-enhanced or image-edited material as potentially altered (raw lines 19–21). Its categories span individuals (including UBOs/signatories/sole proprietors), organizations, sole proprietorships and bank accounts; the list is a navigation catalog, not a requirement to upload every category (raw lines 27–62).
- If bank-account verification fails, the `POST /documents` type is `bankStatement`. The proof must show legal-entity-matching holder name, account number/IBAN, bank country and bank-issued indicator; EU country may be inferred from IBAN. Date is generally within 12 months, with stated exceptions and a rule that a dated RIB or online-banking view also be under 12 months. Bank cards, edited/low-quality or third-party-software documents are rejected; particular cheque, deposit-form and bank-letter rules vary (raw lines 64–135). A trading-name bank account may need a supporting link to the legal entity (raw line 100).
- **Business-account onboarding v4 only:** the live-selfie section applies to each organization signatory and an individual legal entity owning a sole proprietorship. It calls for a live selfie plus photo ID, Onfido/Adyen policy explanation and acceptance before the check, and policy links in the application. Direct capture is recommended; if upload is the only available mechanism, upload must occur within **24 hours** of capture. ID image-quality validation is stated from onboarding v4, and a quality failure is not identity-verification approval (raw lines 208–310).
- If individual ID verification fails, Adyen may request a physical photo ID with **exact first/last-name match** to the legal entity; one-name individuals repeat that name in both fields. Passport, identity card and driver’s licence map to distinct `POST /documents` types. Cards/licences require front and back in the **same POST**, as separate files. Digital IDs, secondary copies, edited images and low-quality photos are excluded (raw lines 312–350). Country-specific exceptions and recency notes are at raw lines 352–364 and are dated snapshot guidance.
- Other conditional sections include UK-only organization proof of each director (raw lines 396–422), tax/industry/national-ID proofs (raw lines 424–487), ownership-control chart with a signature no older than **6 months** and sometimes external supporting records (raw lines 489–540), residential address proofs with **3- or 12-month** limits by document type (raw lines 542–570), and minor-user relationship proof (raw lines 716–736).
- **Additional-product scope:** proof of signatory is labeled business-accounts-only (raw lines 574–618); source-of-funds and source-of-wealth sections are labeled **business accounts and card issuing only**, using `proofOfFundingOrWealthSource` with source-specific information and illustrative documents (raw lines 620–714). The constitutional sole-proprietor section has a **30 MB** cap, unlike the common **2 MB** cap in most later sections (raw lines 139–206, 293–297). Registration/VAT documents require legal-entity name, identifier, qualified issuer and recent date/signature; a DBA/trading name cannot stand in as legal name (raw lines 738–819).

## Material source tensions

- The photo-ID section requires front and back of an identity card or driver’s licence as **separate files in the same POST** (raw lines 322, 337–340), while its file-format line says **maximum 1 file** (raw lines 360–364). The capture does not resolve the packaging rule; do not silently choose one.
- The bank section exempts some document types from needing a visible issue date, with dated RIB/online views subject to the 12-month limit (raw lines 92–94), while a later blanket rejection list says documents older than 12 months are not accepted (raw lines 102–109). Preserve the type-specific distinction; do not generalize the exception to all bank proofs.

## Detail locators

- Bank proof types, content, prohibited material, country-specific cheques and format/size: raw lines 64–137.
- Sole-proprietor constitutional document, location examples, **30 MB** size: raw lines 139–206. Live selfie consent and image quality: raw lines 208–310.
- Photo ID types/name/side/physical-image requirements and country notes: raw lines 312–379. Address, director, tax, industry, national ID and ownership sections: raw lines 381–540.
- Residence, signatory, additional-product funding/wealth and minor relationship: raw lines 542–736. Registration and VAT documents with location examples: raw lines 738–821. Tables and examples are dated reference data, not verification or current legal eligibility evidence.

## Related

- [[adyen-platforms]] — main platform concept and source route.
- [[adyen]] — provider context.
- [[adyen-index]] — provider index.

## Raw Sources

- [[raw/adyen/docs/marketplaces/verification-requirements/document-requirements/2026-09-15|Adyen Marketplaces document requirements, captured 2026-09-15]]
