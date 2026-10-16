---
title: "Adyen Platforms general KYC verification error codes"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/kyc-verification-codes/general-verification-errors"
raw_files:
  - "adyen/docs/platforms/kyc-verification-codes/general-verification-errors/2026-09-15.md"
tags: [adyen, platforms, kyc, verification, error-codes]
---

## Overview

Adyen's general verification-error reference maps broad error codes to messages and possible suberror codes for Adyen for Platforms and Adyen Issuing. Adyen says the general codes and messages appear in `verificationErrors`, which usually also contains corresponding suberrors. The reference says those integrations have no additional preparations for using the codes. See [[adyen]] and [[adyen-platforms]]. This historical lookup does not prove a legal entity's current verification, capability, account eligibility, or successful remediation.

## Key takeaways

- First identify the exact general code and its check category; use the table's **possible suberrors** column to narrow a cause, then the distinct [[source-adyen-docs-platforms-kyc-verification-codes-sub-errors]] reference for granular conditions and its linked action codes. A possible suberror is not guaranteed to appear. See **Types of error codes**, raw lines 22–35, and **General verification errors array example**, raw lines 309–338.
- Two raw table hyperlinks are mislabeled: the link displayed as `1_5054` in the organization `1_50` row targets `#1_5042` (VAT number unverified versus tax-ID/legal-name mismatch), and the link displayed as `1_8015` in the proof-of-signatory `1_85` row targets `#1_8008` (low-quality director-proof image versus signatory-name registry mismatch). Search the exact code in the suberror reference instead of relying on those link targets; do not transfer another code's action. See raw general-error lines 77 and 122; suberror reference lines 184, 196, 329, and 336.
- The example places `verificationErrors` under a `problems` entry whose `entity` is a `LegalEntity` with an ID. Its `1_30` verification error has a message, a common `remediatingActions` example, and `subErrors`. This is an illustrative object shape, not proof of every runtime payload or a completed outcome. See raw lines 309–338.
- The general-issues table includes distinct `1_14` (capability not allowed for type individual), `1_15` (country of legal entity or associated individual), and `1_16` (entity type). These are documented error messages, not a current account-specific eligibility decision. See raw lines 37–47.
- **Missing data** rows name particular absent inputs and map directly to remediating-action codes; their presence in the lookup does not make every listed field a universal API-body requirement. **Missing contracts** and **Data review errors** are separate categories. See raw lines 136–307.

## Detail locators

- **General issues** (raw lines 37–48): broad verification and capability-related errors.
- **Individual identity check** (raw lines 49–72): identity details, ID documents, residency, tax ID, selfie, and biometric checks.
- **Organization check** (raw lines 73–88): organization details, documents, ownership, affiliation, and VAT. General code `1_57` lists possible suberror `1_5052`; the suberror reference states the particular setup consequence.
- **Legal arrangement check** (raw lines 89–99): error message varies with arrangement type.
- **Bank account check** (raw lines 100–112): bank details/documents, authentication, and pending-status rows; no bank receipt inference.
- **Proof of signatory check** (raw lines 113–125) and **Business line check** (raw lines 126–135): exact general-to-suberror mappings.
- **Missing data** (raw lines 136–294): exact field/condition-to-action-code table, including legal-entity, bank-account, organization, business-line, document, and tax fields.
- **Missing contracts** (raw lines 295–302): PCI forms, Terms of Service, and integration completion messages.
- **Data review errors** (raw lines 303–308): review-required code `3_10`.
- **General verification errors array example** (raw lines 309–338): object placement and illustrative common action.

## Related

- [[adyen-platforms]] — platform integration and verification context.
- [[source-adyen-docs-platforms-kyc-verification-codes-sub-errors]] — granular suberror messages and linked remediation codes.
- [Adyen remediating actions](https://docs.adyen.com/platforms/kyc-verification-codes/remediating-actions) — separate action-code definitions referenced by the missing-data/contract tables; navigation only here.

## Raw Sources

- [[raw/adyen/docs/platforms/kyc-verification-codes/general-verification-errors/2026-09-15|Adyen General error codes, fetched 2026-09-15]]
