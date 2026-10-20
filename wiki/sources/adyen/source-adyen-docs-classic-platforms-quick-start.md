---
title: "Adyen Classic Platforms: Quick start"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/quick-start"
raw_files:
  - "adyen/docs/classic-platforms/quick-start/2026-09-15.md"
tags: [adyen, classic-platforms, quick-start, onboarding, split-payments, payouts]
---

## Overview

This 2021-modified, 2026-09-15-captured quick start walks through a **Classic Adyen for Platforms** test integration: obtain credentials after a use-case fit check, create sub-merchant account holders, collect verification information, split a customer payment between sub-merchant and platform accounts, request a payout, configure notifications, and inspect reports. It directs new implementations to a separate new-integration guide.

## Key takeaways

- The page starts with Adyen Sales checking use-case eligibility and providing **test** credentials. It distinguishes a platform API credential for onboarding/payouts from a payments credential for processing payments. The examples use Classic Account/Fund/Notification **v6 test** endpoints and a Checkout **v68 test** `/payments` endpoint. These are snapshot examples, not current credentials or successful execution. See raw lines 21–34, 56–57, 121–123, 173–175 and 201–203.
- A sub-merchant becomes a Classic account holder with one or more accounts. This guide lists basic individual/business fields for starting acceptance and verification, and says the default account is created unless `createDefaultAccount: false` is used. Higher processing tiers and payouts require further verification; onboarding may be hosted or platform-built, with optional document upload. See raw lines 36–109.
- In its illustrative EUR 62 payment, the customer pays the platform; `splits` allocate EUR 60 to the account holder's account and EUR 2 to platform commission. The guide says a successful **authorisation still requires capture for settlement**, automatically if configured or with `/capture`. No example proves authorisation or capture succeeded. See raw lines 111–163.
- After the account holder passes required verification, the example `/payoutAccountHolder` request identifies the **source** with `accountCode` and `accountHolderCode`, and the receiving bank account with `bankAccountUUID`; the guide also mentions eligible-card and scheduled payouts. A request is not bank receipt. See raw lines 165–189.
- Classic Platforms API create/update/delete calls are asynchronous. The system must accept notifications to know final request and verification results. The guide illustrates configuration and later test-report inspection; its step order does not make an earlier API response final evidence. See raw lines 191–232.

## Dated verification and example boundary

The quick start's basic creation fields and sample `gender` field (raw lines 42–77) are from a **2021-modified** page. The related Classic [[source-adyen-docs-classic-platforms-verification-process-requirements-update|requirements-update guide]] applies additional information requirements to new sub-merchants from **1 August 2022** ([[raw/adyen/docs/classic-platforms/verification-process/requirements-update/2026-09-15|related raw lines 21–37]]) and says `gender` is no longer required (related raw lines 434–436). Do not use this quick start's old field list as an exhaustive later verification checklist.

## Detail locators

- Credential roles, account-holder creation and verification paths: [[raw/adyen/docs/classic-platforms/quick-start/2026-09-15|raw lines 21–109]].
- Checkout split example, capture gate and payout request: [[raw/adyen/docs/classic-platforms/quick-start/2026-09-15|raw lines 111–189]].
- Asynchronous notifications and report step: [[raw/adyen/docs/classic-platforms/quick-start/2026-09-15|raw lines 191–232]].

## Related

- [[adyen-classic-platforms]] — Classic model and source catalog.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/quick-start/2026-09-15|Platforms quick start (captured 2026-09-15)]]
