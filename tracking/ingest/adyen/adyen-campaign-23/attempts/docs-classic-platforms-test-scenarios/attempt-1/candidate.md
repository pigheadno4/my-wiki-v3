---
title: "Adyen Classic Platforms: Test scenarios"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/test-scenarios"
raw_files:
  - "adyen/docs/classic-platforms/test-scenarios/2026-09-15.md"
tags: [adyen, classic-platforms, testing, verification, payouts]
---

## Overview

This Classic Adyen for Platforms test guide (last modified 2020-10-26; captured 2026-09-15) describes predefined account-holder test states created with Classic Account API requests or Hosted Onboarding Page document uploads. It explicitly directs new implementations to a separate new-integration guide. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The payout-state examples use Classic POST `/createAccountHolder` for Individual or Business account holders, with `PASSED` and `TestData` sentinel fields and at least one bank account. The flow then uploads photo ID/passport and a bank statement through HOP or Classic POST `/uploadDocument`. The page says photo-ID upload sets the account holder to the “limitless” state requiring the highest KYC-check level; after the listed uploads it describes verified identity/document/bank statement (and company for Business). These are predefined test fixtures, not live verification or bank-payout evidence. See raw lines 26–144 and 146–278.
- For a KYC check set to `FAILED`, the guide uses `FRAUD` in city fields for Individual or Business account holders; its examples describe suspended account holders with payouts blocked. The Business example also uses shareholder city. See raw lines 280–421.
- For `INVALID_DATA`, the guide specifies `INVALIDDATA` in `address.city`, a bank-account owner-city field, or passport description/filename; passport testing uses HOP or `/uploadDocument`. The `INVALID_DATA` bullet names `bankAccount.ownerCity`, whereas the earlier payout and `FAILED` examples use `bankAccountDetails.ownerCity`; preserve this field-path difference rather than treating the bullet as validated payload syntax. See raw lines 32–38, 148–156, 286–292, 347–354, 423–443.
- The `INACTIVEDEADLINECITY` and `REFUNDDEADLINECITY` city sentinels are described as inactivating an account holder with a `/refundNotPaidOutTransfers` call scheduled in six weeks or performed immediately, respectively. Those are test-scenario descriptions; this snapshot does not prove a real refund, payout, or bank receipt. See raw lines 445–455.
- The examples use Classic `accountHolderCode`, `processingTier`, `legalEntity`, and Account API endpoints. Do not substitute modern Balance Platform account-holder resources or capability semantics for these Classic test fixtures. See raw lines 32–40, 42–86, 148–158 and 280–358.

## Detail locators

- Individual payout-state fixture and HOP/API document uploads: raw lines 26–144.
- Business payout-state fixture, shareholder passport and bank statement: raw lines 146–278.
- `FAILED` Individual/Business KYC fixtures: raw lines 280–421.
- `INVALID_DATA` and passport fixture: raw lines 423–443.
- Inactivation/refund timing sentinels: raw lines 445–455.

## Related

- [[adyen-classic-platforms]] — main concept.
- [[adyen-index]] — provider index.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/test-scenarios/2026-09-15|Test scenarios, captured 2026-09-15]]
