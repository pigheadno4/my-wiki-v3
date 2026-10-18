---
title: "Adyen Business Accounts verification process"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/verification-overview"
raw_files:
  - "adyen/docs/business-accounts/verification-overview/2026-09-15.md"
tags: [adyen, business-accounts, platforms, verification, kyc, capabilities]
---

## Overview

This Adyen Business Accounts verification overview (last modified 2023-12-29, captured 2026-09-15) describes KYC checks on balance-platform users and the resulting **per-capability** permission state. Adyen says it must verify users before processing payments, paying out funds or offering business accounts, and decides which actions a user can perform from verification results. An account holder, requested capability, pending check, active deadline or example API response does not alone prove successful KYC, account opening or a completed financial operation.

## Key takeaways

- Business-account capabilities configured during design are requested when a new user is onboarded and an account holder is created; a non-default additional capability must be requested separately and can trigger more verification. Checks also run after user-data changes and during Adyen-required or proactively requested periodic reviews. Reviews can include the legal entity/legal arrangement, UBOs and signatories.
- Verification is asynchronous. While several checks are in progress, `verificationErrors` may appear even when overall capability verification remains `pending`; the guide recommends waiting until checks finish and status becomes `invalid` before contacting Adyen. A `rejected` capability verification status means the capability will not be allowed. Inspect the capability's settings and verification state rather than treating a requested flag or an account-holder creation as approval.
- For already allowed capabilities, an active verification deadline can preserve use during re-verification or data review. The deadline is the **final date for required information/documents to be submitted and verified by Adyen**, not merely for user upload. Users must confirm reviewed data and resolve any verification errors for a review to finalize; missed deadlines or failed KYC lead to disallowed capabilities. An updated legal entity by itself does **not** trigger `balancePlatform.accountHolder.updated`; that webhook is for capability-related account-holder changes.
- Deadlines are described as available only with Legal Entity Management API **v3 and v4**. The dated standard table gives 30 days for `issueBankAccount` and `sendToThirdParty`, and 60 days for `receiveFromThirdParty`; Adyen may shorten or remove a standard deadline after monitoring or additional checks. Inspect actual account-holder deadline data in Customer Area or GET `/accountHolders/{id}`, including affected capabilities and `expiresAt`.
- The example response contains `sendToThirdParty.allowed=true`, `verificationStatus=invalid`, a deadline, and a `1_14` error whose message says that capability is not allowed for an individual. Treat this as a mixed illustrative example, not a universal allowed/invalid rule, a real user's outcome, or proof that `1_14` can be remediated. The page does not list supported countries or settle which legal-entity types qualify for a given Business Account; those need separate product/capability evidence.

## Detail locators

- Opening and `## When does Adyen verify users`: KYC purpose, capability settings, capability request, data-change and periodic-review triggers.
- `### Verification deadlines`: LEM v3/v4 scope, final verification deadline, 30-/60-day standard table, shortening/removal, Customer Area/API observation and mixed example.
- `## How the verification process works` / three tabs: asynchronous pending/invalid/rejected behavior, data-change re-verification, review confirmation and deadline loss of permission.

## Related

- [[adyen-business-accounts]] — main Business Accounts concept and dated product eligibility context.
- [[adyen-platforms]] — balance-platform account-holder and legal-entity context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/business-accounts/verification-overview/2026-09-15|Adyen Business Accounts verification process (fetched 2026-09-15)]]
