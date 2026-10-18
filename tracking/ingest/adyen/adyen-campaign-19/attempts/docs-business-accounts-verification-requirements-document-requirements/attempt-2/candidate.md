---
title: "Requirements for document uploads | Adyen Business accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/verification-requirements/document-requirements"
raw_files:
  - "adyen/docs/business-accounts/verification-requirements/document-requirements/2026-09-15.md"
tags: [adyen, business-accounts, verification, documents, kyc]
---

## Overview

This 2023-11-29-modified Adyen Business accounts document-upload reference, captured 2026-09-15, explains evidence Adyen may request when automatic verification fails, organized by individual, organization, sole proprietorship and bank-account resource. It covers Legal Entity Management API `POST /documents` type values, content, age and file constraints, with onboarding-version and country exceptions. It is a dated requirements reference, not evidence that a given user was asked for a document, passed KYC, opened a Business account, or has current eligibility. See [[adyen]], [[adyen-financial-products]], and [[adyen-business-accounts]].

## Key takeaways

- Adyen may request additional documents after automatic verification cannot establish data; the page instructs original, unedited evidence and rejects AI-enhanced/altered documents. Its Requirements section says an Adyen for Platforms or Issuing integration adds no further page-level preparations, not that all document checks are waived (raw lines 19–29).
- Bank-account proof uses `bankStatement` after failed automatic verification. It needs matching legal-entity holder name, account/IBAN, bank issuer and location. Raw lines 92–94 exempt RIBs, cheques, online-banking records and TAMIEYTHPIO from the general issuance-date requirement, while dated RIB/online records still must be under 12 months; raw line 106 separately rejects documents issued more than 12 months ago without those exceptions. This conflict is unresolved in the dated source: do not choose a precedence for older documents without current Adyen confirmation. It excludes bank-card photos and certain edited/third-party documents; US/CA cheque and AU cheque restrictions plus bank stamp/signature rules are document-specific (raw lines 64–135).
- A sole-proprietor constitutional document has a 12-month issuance or signed/current-state alternative and a larger 30 MB file ceiling than the usual 2 MB examples (raw lines 139–170). Live selfie applies only with onboarding v4 to organization signatories and individual owners of sole proprietorships; Business accounts request pairs it with photo ID and the page specifies Onfido/Adyen notice and consent links before collection, direct capture as a recommendation, and a 24-hour limit if separately uploaded (raw lines 172–261).
- Photo ID must match the onboarded name, be physical, non-expired and signed if a signature field exists. Identity cards and driver's licenses require both sides, each in its own file, within one `POST /documents` request; the same section's generic file-format bullet says “maximum 1 file,” an unresolved internal conflict that must be checked before implementation (raw lines 263–315). France, Poland and Ukraine have dated ID-validity exceptions at lines 303–309; the Poland date text is malformed.
- Organization/individual evidence requirements diverge: tax/national ID and industry proof, ownership chart including all intermediate entities/UBOs and a signature no older than six months, three- versus twelve-month residential-address proof by document type, signatory authority with twelve-month dates, source-of-funds versus source-of-wealth evidence, minor/legal-representative relationship, registration and VAT records each have their own conditional checks (raw lines 319–725). Source-of-wealth supporting-document examples are illustrative, not exhaustive (raw line 612). The country registration table at lines 657–693 contains anomalous ISO-2 labels such as Ireland IR, Poland PO and Spain SP; do not use it as a machine-readable country-code authority.

## Detail locators

- Resource/document map and global original-document rule: raw lines 19–62.
- Bank proof, country/age exceptions, cheque signatures and 2 MB sizes: raw lines 64–135; constitutional-document 30 MB exception: lines 139–170.
- Onboarding-v4 selfie actors, consent and 24-hour upload condition: raw lines 172–261. Photo-ID name, sides, validity, country exceptions and count conflict: lines 263–315.
- Tax, industry, national ID, ownership and residential address: raw lines 319–480. Signatory, funds/wealth, minors, registration and VAT: lines 484–725.

## Related

- [[adyen-business-accounts]]
- [[adyen-financial-products]]

## Raw Sources

- [[raw/adyen/docs/business-accounts/verification-requirements/document-requirements/2026-09-15|Pinned Adyen Business accounts document-upload requirements]]
