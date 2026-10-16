---
title: "Adyen Platforms manage transfer instruments"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/manage-transfer-instruments"
raw_files:
  - "adyen/docs/platforms/manage-transfer-instruments/2026-09-15.md"
tags: [adyen, platforms, transfer-instruments, payouts, bank-accounts]
---

## Overview

This Adyen for Platforms guide (last modified 2023-03-28; captured 2026-09-15) defines a transfer instrument as an API resource representing an external bank account. It covers Legal Entity Management API create/view/update/delete for users' bank accounts and platform payout accounts, plus Customer Area management of the platform's own payout accounts. A user's bank account belongs to an account holder's legal entity; the platform payout account is its own company's bank account linked to the liable account. These are distinct from an account holder, legal entity, balance account and actual fund transfer. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Ownership and identifiers:** A create request uses bankAccount type and the legalEntityId of the entity with the contractual relationship to the platform that owns the bank account; for sole proprietorships, the guide names the individual owner's legal entity. Bank details depend on bank location. The response supplies a separate transfer-instrument id that a sweep or manual transfer may target. Do not substitute the legal-entity, account-holder, balance-account or liable-account ID for that target.
- **Access and state:** The stated prerequisite is Adyen for Platforms with a Legal Entity Management web service user holding Manage LegalEntities via API and Balance Platform BCL Legal Entity role. Customer Area lists Manage account holders & legal entities and, to manage payout accounts, Merchant manage bank accounts. The create example has sendToTransferInstrument requested true, allowed false and verificationStatus pending; problems can report bank-verification issues. The Customer Area payout account is usable when its status is valid after verification. Creating or viewing an instrument does not establish enabled payout capability or bank receipt.
- **Updates and deletion:** PATCH modifies supplied fields and, in the guide's bank-account update example, retains the transfer-instrument ID, so schedules and requests aimed at that ID remain associated with it. DELETE cannot be undone; future scheduled or on-demand payouts referencing the deleted ID fail. The guide's payout-account rotation sequence is add a new instrument, update schedules or requests, verify receipt, then delete the old one. This is a documented sequence, not evidence that any payout occurred.
- **Company payout accounts:** The platform's payout accounts connect to its liable account for settlement to company bank accounts. The Customer Area path Balances > Payout accounts manages only these platform accounts, not users' transfer instruments; the page mentions adding accounts in additional currencies. It does not establish country/currency eligibility or a particular platform's settlement result.
- Dated examples show test hosts and mixed Legal Entity Management API versions (create curl v3; later operations v4). Check the relevant API Explorer and current account configuration before implementing; these examples do not prove current availability or authorization.

## Detail locators

- Definition, two account types, scope and role prerequisites: pinned raw lines 15-40.
- Create fields, owner legalEntityId, location-dependent bank details, response id and pending capability, verification problems: pinned raw lines 47-57 and 343-374.
- GET details and PATCH behavior: pinned raw lines 376-548 and 815-836.
- Irreversible deletion and future payout references: pinned raw lines 838-986.
- Liable-account company payout accounts, Customer Area scope, valid status and rotation sequence: pinned raw lines 988-1017.

## Related

- [[adyen-platforms]] — platform-integration concept and reciprocal source route.
- [[source-adyen-docs-platforms-manage-account-holders]] — separate platform user and legal-entity identity.

## Raw Sources

- [[raw/adyen/docs/platforms/manage-transfer-instruments/2026-09-15|Adyen Manage transfer instruments, captured 2026-09-15]]
