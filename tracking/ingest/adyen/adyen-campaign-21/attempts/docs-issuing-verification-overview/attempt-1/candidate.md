---
title: "Adyen Issuing: Verification process"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/verification-overview"
raw_files:
  - "adyen/docs/issuing/verification-overview/2026-09-15.md"
tags: [adyen, issuing, verification, capabilities]
---

## Overview

This Adyen Issuing verification overview (last modified 2023-12-29; captured 2026-09-15) describes when Adyen checks cardholders and how verification status governs requested capabilities. It says cardholders must be verified before paying out their funds and describes asynchronous checks, re-verification after data changes, and conditional deadlines. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Default capabilities set during integration design are requested when a new cardholder's account holder is created; a non-default capability must be requested separately and may require more checks. Adyen's verification decision governs whether the cardholder can use the capability. See raw lines 19–38.
- A change to cardholder data after capabilities are allowed triggers re-verification. If updated data fails, Adyen may set a deadline; the cardholder may continue using the affected capabilities while that deadline is active, but unresolved issues can disallow them. The page says `balancePlatform.accountHolder.updated` is triggered only for capability-related account-holder changes; legal-entity data changes do not themselves trigger that webhook. See raw lines 42–50.
- **Version and timing boundary:** Verification deadlines are stated to be available only in Legal Entity Management API v3/v4. The captured page gives standard 30-day periods for `sendToBalanceAccount`, `sendToTransferInstrument`, and `receiveFromTransferInstrument`; it gives 60-day periods for `receiveFromBalanceAccount`, card issuance/use, restricted-country/industry card use, and ATM withdrawal capabilities. Adyen says monitoring and subsequent checks can shorten or remove a standard deadline. These are dated page descriptions, not a promise of a specific user's deadline or current eligibility. See raw lines 52–80.
- In the illustrated workflow, Adyen checks asynchronously after account-holder creation, additional capability requests, or data changes. Verification errors may appear while overall capability status remains `pending`; the page recommends waiting until checks complete and status becomes `invalid` before contacting Adyen. A `rejected` verification status means the capability is not allowed. If a change-induced issue remains unresolved by the deadline, or new data fails checks, capabilities are disallowed. See raw lines 136–168.
- The sample account-holder response illustrates an `invalid` verification status with `allowed`/`enabled`/`requested` values, deadline entries and errors; it is an example rather than a live verification result. Read the exact example at raw lines 82–132.

## Detail locators

- Verification triggers, default/additional capabilities, data changes and webhook distinction: raw lines 28–50.
- Deadline API-version qualification, standard capability periods, variability and lookup: raw lines 52–80.
- Illustrative account-holder response: raw lines 82–132.
- Initial request and data-change workflow, pending/invalid/rejected handling: raw lines 136–168.

## Related

- [[adyen-issuing]] — main concept.
- [[adyen-index]] — provider index.

## Raw Sources

- [[raw/adyen/docs/issuing/verification-overview/2026-09-15|Verification process, captured 2026-09-15]]
