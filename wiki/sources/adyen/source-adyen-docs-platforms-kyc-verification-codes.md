---
title: "Adyen Platforms verification codes"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/kyc-verification-codes"
raw_files:
  - "adyen/docs/platforms/kyc-verification-codes/2026-09-15.md"
tags: [adyen, platforms, issuing, kyc, verification-codes]
---

## Overview

This Adyen verification-code overview (last modified 2021-01-19; captured 2026-09-15) explains how Platforms or Issuing integrations find and interpret verification-error codes in account-holder capability problems. It is a code taxonomy and route to detailed catalogs, not evidence that a particular legal entity is verified or a remediation has succeeded. See [[adyen]] and [[adyen-platforms]] for the Platforms context; Issuing is separately scoped.

## Key takeaways

- **Three code layers:** A general error code broadly describes a failed check, a linked specific suberror gives a more granular cause, and a remediating action code suggests a possible fix. Adyen says it sends a remediating action for every error whenever possible, not invariably. Use suberror detail to design API-only onboarding error handling; the guide recommends handling all possible codes while allowing implementation to fit the use case and resources.
- **Where to inspect:** The Customer Area Account holder details > Capabilities view shows enabled, allowed and verification-status information. The page requires Manage account holder capabilities for that view. API inspection uses a Configuration API web-service credential and GET /accountHolders/{id}; account-holder created/updated webhooks are another route. Account-holder ID or reference and linked legal-entity ID are search choices, not interchangeable object identities.
- **Problems shape:** In an account-holder capability problems array, entity.id identifies the legal entity with the verification error. Each verificationErrors item can carry type (invalidInput or dataMissing), general code/message, a common remediatingActions field when applicable, and subErrors entries with their own type/code/message/remediatingActions array. The prose calls the common field an object (line 80), but the example renders it as an array (lines 98-103); this page does not settle its runtime type, so consult the current API schema or an observed payload when parsing. The example has general 1_30, suberrors 1_3001 and 1_3000, action codes 1_301 and 1_300, and verificationStatus invalid; those are one illustrated case, not all codes or outcomes.
- The detailed remediating-action, general-error and sub-error catalogs are separate pages. Codes can explain reported problems and possible user actions; they do not grant capability, certify compliance, prove current eligibility or ensure the next verification succeeds.

## Detail locators

- Three-level taxonomy, possible-action qualification and integration prerequisites: pinned raw lines 19-35.
- Customer Area and Configuration API/webhook routes: pinned raw lines 37-61.
- API-only recommendation and problems/entity structure, including conflicting common-action shape: pinned raw lines 63-81 and 98-103.
- Illustrative codes, nested actions and invalid verification status: pinned raw lines 83-144.
- Routes to separate testing/action/general/suberror references: pinned raw lines 146-164.

## Related

- [[adyen-platforms]] — platform verification concept and reciprocal source route.
- [[source-adyen-docs-platforms-kyc-verification-codes-remediating-actions]] — detailed action catalog.
- [[source-adyen-docs-platforms-kyc-verification-codes-general-verification-errors]] — detailed general-code catalog.
- [[source-adyen-docs-platforms-kyc-verification-codes-sub-errors]] — detailed suberror catalog.

## Raw Sources

- [[raw/adyen/docs/platforms/kyc-verification-codes/2026-09-15|Adyen Verification codes, captured 2026-09-15]]
