---
title: "Adyen SFTP AuthorisationReferral request"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/authorisationreferral-request"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/authorisationreferral-request/2026-09-15.md"
tags: [adyen, batch-processing, sftp, modification, referral, authorisation]
---

## Overview

This dated Adyen Docs page (2019-04-30 last-modified metadata; captured 2026-09-15) describes an advanced-SFTP batch `AuthoriseReferral` **Modification request** for a MOTO transaction declined with a `Referral` reason after the shopper contacts the issuing bank and the merchant obtains an authorisation code. The merchant submits the code with the original payment PSP reference. Adyen says that **when it receives and processes** the file, it books a new `Authorised` journal entry and continues the standard workflow. Submission alone is not automatic approval, a captured payment, or final financial outcome. See [[adyen-batch-processing]] and [[adyen]].

## Key takeaways

- The page calls `PaymentDetails` and `AuthoriseReferral` mandatory sub-lines. `PaymentDetails` positions 4–6 hold numeric amount, numeric currency exponent, and three-character ISO currency. Optional field gaps retain commas. Its shopper-reference field is conditional for recurring payments/contracts, not established as required merely because a referral is submitted. [Raw lines 24–46]
- The `AuthoriseReferral` sub-line holds the **original payment PSP reference** at position 4 and the transaction's authorisation code (`authCode`) at position 5. The sample places `PaymentDetails` at `SL,1` and `AuthoriseReferral` at `SL,2`, within a `Modification` file and `AuthoriseReferral` line. [Raw lines 48–66]
- The mandatory-sub-lines sentence calls this a “bank transfer authorisation request” although the title, MOTO referral narrative, `Modification` sample, and `AuthoriseReferral` fields identify a referral modification. Preserve this wording conflict and verify intended applicability with Adyen; do not relabel it as an ordinary bank-transfer authorisation flow. [Raw lines 14–26, 58–66]
- The snapshot does not define ACK/result-file states, capture, settlement, or a retry policy. Check the relevant batch ACK and modification-result sources for validation and result evidence before acting on an individual case.

## Detail locators

- MOTO decline/referral precondition and conditional journal-entry effect: raw lines 16–20. Mandatory `PaymentDetails` positions and delimiters: raw lines 24–46. Original reference/authCode fields and TEST example: raw lines 48–66.
- The example's `100,2,EUR` shows field placement; it does not validate the amount of any live transaction or prove the modification succeeded.

## Related

- [[adyen-batch-processing]]
- [[adyen]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-modification-result-file]]

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/authorisationreferral-request/2026-09-15|Adyen AuthorisationReferral request, 2026-09-15 snapshot]]
