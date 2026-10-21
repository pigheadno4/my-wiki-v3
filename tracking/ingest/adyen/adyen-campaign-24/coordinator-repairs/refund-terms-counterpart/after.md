---
title: "Adyen Classic Platforms release notes, 2018–2023"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/release-notes"
raw_files:
  - "adyen/docs/classic-platforms/release-notes/2026-09-15.md"
tags: [adyen, classic-platforms, release-notes, api-versions, notifications]
---

## Overview

This 2026-09-15 capture is a dated change log for **Classic Adyen for Platforms**, with entries from 2018-12-27 through 2023-06-05. It groups API, notification, hosted-onboarding, Customer Area, KYC, report and general changes. Entries describe changes at their release dates and sometimes distinguish API or notification versions; they are not a current feature or eligibility guarantee. The 2022-08-01 entry directs new integrations to upgraded Adyen for Platforms documentation and existing integrations to the Classic guide. [[adyen]] [[adyen-classic-platforms]]

## Consequential changes by period

- **2018-12-27, API v5 and Classic notifications v5:** Create, update and delete requests became asynchronous, so integrations need notification webhooks for outcomes; business account-holder creation requires `country`; `/verify` became `/checkAccountHolder`. KYC codes became more granular, and v5 added payout-method deletion and optional HMAC signing for notifications. Notification types gained root `error` and `content.invalidFields` fields. These are v5 migration changes, not blanket claims for every API version (raw lines 1629–1672).
- **2019:** The log records Customer Area manual payouts and fund transfers, report changes, verification and payout fixes, and notification corrections. It removed the End of Month Balance Report in favor of the MarketPay Balance Report (2019-01-17), disallowed beneficiary setup from a suspended source account (2019-03-25), and changed KYC re-suspension timing after a deadline-related unsuspension to 42 days (2019-04-23). Same-holder transfers stopped increasing processed volume (2019-09-16); they became possible regardless of payout status (2019-10-29). Those separate entries do not establish that all other transfer gates are absent (raw lines 1146–1628).
- **2020-08-05, API/notification v6:** API verification response names moved from `verification.bankAccounts`/`bankAccountUUID` to `verification.payoutMethods`/`payoutMethodCode`; v6 notification fields changed in parallel, including `content.bankAccountUUID` to `content.payoutMethodCode`. Selected notifications removed `content.pspReference` in favor of root `pspReference`; payout notifications removed `content.amount` in favor of `content.amounts`. The same date introduced payout-return reasons and confirmed-payout detail fields. Preserve version and event-type context when parsing historical payloads (raw lines 1039–1085).
- **2020–2021 money and verification behavior:** The log added liable-account threshold notifications, configurable verification profiles, legal-arrangement data in Account API v6, account-holder top-ups, and more HOP controls (raw lines 898–1139). A 2021-02-15 split validation change rejects local-payment-method splits whose amounts do not sum to the payment amount, after earlier acceptance caused settlement problems (raw lines 910–914). On 2021-09-27 the default handling of existing funds and new payments for suspended or closed account holders remained refunding, with support-enabled automatic transfer to the liable account as an option; refunds and chargebacks became liable-account deductions by default, and only active holders could receive payouts (raw lines 796–817). The 2021-10-25 payout notification improvement distinguished successfully processed card payouts as `Confirmed` and failures as `Failed`; this release note alone does not prove final bank receipt (raw lines 752–756).
- **2022:** The 2022-02-21 API entry deprecated `ownerDateOfBirth` and specified `yyyy-mm-dd` for integrations still sending it. The year also brought HOP and KYC collection fixes, upfront document collection as an enablement option, report booking corrections, Customer Area suspension action, and country-specific bank-data rules (raw lines 91–599). The 2022-03-14 Reports entry says California bank payouts no longer include “Right To Refund” text under the Marketplace Payments accounting report’s `Refund terms` column (release-note raw lines 412–416); the 2023-modified [[source-adyen-docs-classic-platforms-reports-and-fees-marketplace-payments-accounting-report]] still describes that column as containing the text (report raw line 73). Treat this as a dated documentation difference, not evidence that later report rows contain the text. The 2022-08-01 entry explicitly separated upgraded infrastructure documentation for new integrations from the Classic guide for existing integrations (raw lines 171–175). Changes requiring Support or platform configuration are conditional, for example local-timezone payout scheduling for new integrations and opt-in for existing ones (raw lines 310–316).
- **2023 entries:** Croatia HRK bank accounts ceased to be supported after EUR became the sole official currency there; US residents had to enter full nine-digit SSN/TIN on HOP. Later entries concern HOP shareholder roles, signatory data, missing-role warnings and Cyprus company-number length. The latest listed entry is 2023-06-05 even though the file was captured 2026-09-15; do not infer post-2023 product status from this ledger (raw lines 37–89).

## Detail locators

- Category definitions and API Diff Tool: raw lines 19–31. Newest 2023 entries and regional/identity changes: lines 37–89.
- 2022 HOP, API, KYC, payout and report changes, including deprecation and upgraded-infrastructure boundary: lines 91–599.
- 2021 releases: lines 603–961; suspended/closed holder funds-direction change: lines 796–817; split validation: lines 910–914.
- 2020 releases and exact API/notification v6 field migrations/removals: lines 963–1144, especially 1039–1085.
- 2019 releases, including transfers, beneficiary restrictions, verification, reports and v5 fixes: lines 1146–1628. Initial 2018 v5 breaking and notification changes: lines 1629–1672.

## Related

- [[adyen]] — provider.
- [[adyen-classic-platforms]] — Classic model and source index.
- [[adyen-platforms]] — separate upgraded Platforms model named in the 2022 release note.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/release-notes/2026-09-15|Classic Platforms release notes — 2026-09-15 snapshot]]
