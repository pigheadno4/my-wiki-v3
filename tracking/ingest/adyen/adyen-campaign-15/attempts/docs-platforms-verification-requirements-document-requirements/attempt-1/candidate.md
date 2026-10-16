---
title: "Adyen platform verification document-upload requirements"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/verification-requirements/document-requirements"
raw_files:
  - "adyen/docs/platforms/verification-requirements/document-requirements/2026-09-15.md"
tags: [adyen, platforms, verification, documents, legal-entities]
---

## Overview

This Adyen for Platforms verification reference, **last modified 2023-11-29 and captured 2026-09-15**, lists documents Adyen **may request when automatic verification of a user, legal entity or bank account fails**. It covers individuals (including UBOs, signatories and sole proprietors), organizations, sole proprietorships, bank accounts and narrower business-account/card-issuing cases. Documents must be original and unedited; AI or image-editor alteration can cause rejection. The page says Adyen for Platforms or Issuing integrations have no additional *preparation* requirements, while the subsequent document-type, product, country and onboarding-version conditions still apply when a document is requested. Uploading a conforming document is not verification approval, legal compliance, capability activation, payment processing or funds movement.

## Key takeaways

- **Bank-account proof:** after automatic verification failure, API-only onboarding uses `bankStatement` with Legal Entity Management `POST /documents`; hosted onboarding auto-detects the type, with the page's hosted bank-document feature limited to Australia, France, UK and US in this snapshot. The account-holder name must match the legal-entity name on record; account number/IBAN, recent issue date and bank issuer indication are required, subject to listed document exceptions. Bank cards, ATM/terminal output, third-party bookkeeping output and altered or illegible documents are excluded. The bank-statement section allows JPEG/JPG/PNG/PDF, **one file and 4 MB maximum**; do not substitute another document type's size limit.
- **Identity and onboarding version:** a live selfie is described only for **business accounts using onboarding v4**, for organization signatories and individual legal entities owning sole proprietorships. It pairs with photo ID and an Onfido-powered biometric check. The platform must present Adyen/Onfido notices and consent; a separately uploaded selfie must be within 24 hours of capture. ID-image quality validation is also marked onboarding-v4-only. For requested photo ID, legal-entity first/last names must match exactly; card/licence front and back are separate files in the same `POST /documents` request. Physical, non-expired ID and unedited legible images are required, with country-specific validity exceptions in the raw.
- **Entity and country conditions:** sole-proprietorship constitutional documents have freshness conditions and a country example table. Organizational proof of director applies only to **UK organizations**; proof of signatory applies only when creating **business accounts**. Registration, organization tax and VAT proofs require legal-entity identity and relevant numbers; a trading name does not replace the legal name, and VAT/tax IDs may differ by country. Residential-address proof has **3- or 12-month** windows depending on document type. The local document-name and number tables are historical examples, not a current country eligibility list.
- **Ownership and minor relationship:** when UBO ownership verification fails, a requested ownership chart must show all intermediate entities, UBOs, percentages, legal names/structures/countries and a dated signature. The raw distinguishes qualified signers who need no extra support from other signers who must provide recent external official documents. A minor may be asked for an external document establishing their legal representative and relationship.
- **Funds versus wealth:** proof of **source of funds** applies only to business accounts and card issuing; the described Legal Entity Management `POST /businessLines` uses service `banking` or `issuing` and an `adyenProcessedFunds` branch, with source type/description required when funds were not processed through Adyen. Proof of **source of wealth** is likewise scoped to business accounts and card issuing, asks for total/main wealth sources, and uses `proofOfFundingOrWealthSource` in `POST /documents`. Its supporting-document examples are explicitly illustrative. Neither section says money was accepted or moved.
- **Per-type upload limits:** the common JPEG/JPG/PNG/PDF pattern is not a single global limit. Most later proof sections specify one file, PDF **1 KB–2 MB** or image **100 KB–2 MB**; sole-proprietorship constitutional documents allow up to **30 MB**; bank proof allows up to **4 MB**. Consult the named section for its exact files, pages, issue-date and country exceptions.

## Detail locators

- Raw lines 15–62: conditional verification purpose, unedited-document rule, product-preparation statement and document-type navigation by individual/organization/sole proprietorship/bank account.
- Raw lines 64–128, `Bank statement`: onboarding route, hosted-country qualifier, bank proof fields, accepted/rejected items and distinct 4 MB limit.
- Raw lines 130–197, `Constitutional document`: sole-proprietorship examples, multi-country table and 30 MB file limit.
- Raw lines 199–301, `Live selfie photo`: business-account/onboarding-v4 scope, Onfido notices/consent, 24-hour separate-upload condition and quality checks.
- Raw lines 303–370, `Photo IDs`: exact name, accepted type table, same-request front/back, physical/quality restrictions, France/Poland/Ukraine exceptions and v4 quality validation.
- Raw lines 372–479: address/director/tax/industry/national-ID/organization-tax document conditions, including UK-only director proof and legal-name rule.
- Raw lines 480–531, `Proof of ownership`: chart contents, 6-month signature, qualified-signer exception and supporting external documents.
- Raw lines 533–609: residency date windows and business-account-only signatory proof.
- Raw lines 611–723, `Proof of source of funds`: business-account/issuing scope, `/businessLines` route, Adyen-processed branch and source-type table.
- Raw lines 725–821: wealth source scope, illustrative support table, and minor relationship proof.
- Raw lines 823–906: registration and VAT proof, country-specific example table, legal-name and tax/VAT distinctions.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — platform onboarding and verification context, pending coordinator-owned foundation concept.
- [[adyen-mirakl]] — distinct connector-specific seller onboarding path.

## Raw Sources

- [[raw/adyen/docs/platforms/verification-requirements/document-requirements/2026-09-15|Platform document requirements, fetched 2026-09-15]]
