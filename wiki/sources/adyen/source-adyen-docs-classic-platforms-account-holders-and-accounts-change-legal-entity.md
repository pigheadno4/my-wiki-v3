---
title: "Adyen Classic Platforms: Change account-holder legal entity type"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/account-holders-and-accounts/change-legal-entity"
raw_files:
  - "adyen/docs/classic-platforms/account-holders-and-accounts/change-legal-entity/2026-09-15.md"
tags: [adyen, classic-platforms, account-holders, legal-entity, verification]
---

## Overview

This 2020-modified, 2026-09-15-captured **Classic Adyen for Platforms** guide explains changing an existing account holder's legal-entity type with `/updateAccountHolder` so the holder enters the appropriate verification process. The holder retains its `accountHolderCode`, `accountCode` and transaction history. The feature is stated for **Account API v5 and later**; examples use v6 TEST endpoints. New implementations are directed to the separate newer integration model. See [[adyen]] and [[adyen-classic-platforms]].

## Key takeaways

- The guide offers two approaches: **migrate existing details** or **provide new details**. Under migration, Adyen carries over identity-check status and passport verification from the old legal entity, but performs bank-account verification again if required for the new type. After the update completes, `ACCOUNT_HOLDER_VERIFICATION` reports migrated and new check statuses or requirements. This is a verification transition, not automatic approval.
- Individual-to-Business examples send `accountHolderCode`, `legalEntity: Business` and business details. For Business-to-Individual **migration**, Adyen says the business account holder must have **only one shareholder**; a request with multiple shareholders is rejected. Do not apply that migration rule as a stated constraint on the alternative new-details path without its own API contract.
- With new details, the examples send business/shareholder data or individual name/personal/document data along with `accountHolderCode` and the new `legalEntity`. Once the update completes, `ACCOUNT_HOLDER_VERIFICATION` reports **new** check statuses or requirements. Test payloads illustrate the shapes; they do not prove a live holder was reverified, gained payout capability or moved money.

## Detail locators

- Pinned raw lines 15–30: Classic scope, retained identifiers/history, two approaches and v5+ boundary.
- Pinned raw lines 32–36: migrated identity/passport status, conditional bank reverification and notification.
- Pinned raw lines 38–76: Individual-to-Business and Business-to-Individual migration examples, including one-shareholder rejection at line 62.
- Pinned raw lines 78–165: new-details route, completion notification and v6 TEST examples for both direction changes.

## Related

- [[adyen-classic-platforms]] — Classic account-holder and verification context.
- [[source-adyen-docs-classic-platforms-verification-process]] — Classic verification requirements and status flow.
- [[adyen-platforms]] — newer model with separate legal-entity resources.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/account-holders-and-accounts/change-legal-entity/2026-09-15|Classic legal-entity change guide, captured 2026-09-15]]
