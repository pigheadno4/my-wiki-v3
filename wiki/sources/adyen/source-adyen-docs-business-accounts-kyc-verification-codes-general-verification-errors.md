---
title: "Adyen general verification error codes"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/kyc-verification-codes/general-verification-errors"
raw_files:
  - "adyen/docs/business-accounts/kyc-verification-codes/general-verification-errors/2026-09-15.md"
tags: [adyen, business-accounts, platforms, issuing, kyc, verification]
---

## Overview

This general error-code reference (last modified 2023-02-28; captured 2026-09-15) sits under the Business accounts KYC path but says its requirements apply to an Adyen for Platforms or Adyen Issuing integration. Adyen sends broad codes and messages in a legal entity's verificationErrors array, usually with corresponding suberrors. The page maps check families to codes and links separate suberror/remediating-action references. It does not show a particular user's verification result, an opened Business account, a permitted capability or a successful transfer. See [[adyen]], [[adyen-business-accounts]] and [[adyen-platforms]].

## Key takeaways

- **Read the layers separately:** A general code broadly identifies the failing check; a linked suberror can refine the cause; a remediating-action code points to a separate action reference. The example problems array associates a LegalEntity ID with verificationErrors, a general 1_30 code, a remediatingActions entry and subErrors. Do not treat a general code alone as a complete case diagnosis or an action as proof that Adyen has reverified the entity.
- **Check families:** The 1_1x family covers general issues including information/document verification, declined legal entity and capability-not-allowed cases tied to individual/entity type or country. The 1_3x–1_4x, 1_5x, 1_6x, 1_7x, 1_8x and 1_9x families cover individual, organization, legal arrangement, bank account, signatory and business-line checks. A bank-account verification error is an identity/check result, not evidence of a completed bank transfer.
- **Missing information and review:** The 2_8x table maps missing personal, organization, account, document, ownership, tax, business, support and other data to remediating-action codes; the exact row matters, and it includes specialized fields such as Capital-adjacent economic sector/legal form. The 2_9x table includes unsigned PCI forms, unaccepted Terms of Service and incomplete integration. The 3_10 row says review of data is required. A missing-data row or review code is not an automatic eligibility verdict or proof that the issue was resolved.
- **Requirements boundary:** The page says there are no additional requirements, limitations or preparations **if** the reader already has an Adyen for Platforms or Issuing integration. This statement does not establish current product eligibility, onboarding completion or that a Business account is open.

## Detail locators

- Purpose, verificationErrors/suberrors relationship and conditional integration requirement: pinned raw lines 14–20.
- Code-family index, general/individual/organization categories: pinned raw lines 22–88.
- Legal arrangement, bank account, signatory and business-line categories: pinned raw lines 89–135.
- Missing-data-to-remediating-action catalog: pinned raw lines 136–293.
- Missing contracts, review required and example problems array: pinned raw lines 295–338.

## Related

- [[adyen-business-accounts]] — Business accounts concept and reciprocal source route.
- [[adyen-platforms]] — broader integration scope named by the page.

## Related raw API references

- [[raw/adyen/docs/business-accounts/kyc-verification-codes/sub-errors/2026-09-15|Verification suberrors]] — linked detail catalog; navigation only.
- [[raw/adyen/docs/business-accounts/kyc-verification-codes/remediating-actions/2026-09-15|Remediating actions]] — linked action catalog; navigation only.

## Raw Sources

- [[raw/adyen/docs/business-accounts/kyc-verification-codes/general-verification-errors/2026-09-15|Adyen general verification errors, captured 2026-09-15]]
