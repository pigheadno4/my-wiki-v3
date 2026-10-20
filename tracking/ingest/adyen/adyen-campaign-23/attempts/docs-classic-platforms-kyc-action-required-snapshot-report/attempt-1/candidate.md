---
title: "Adyen Classic Platforms: KYC action required snapshot report"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/kyc-action-required-snapshot-report"
raw_files:
  - "adyen/docs/classic-platforms/kyc-action-required-snapshot-report/2026-09-15.md"
tags: [adyen, classic-platforms, kyc, reports, verification]
---

## Overview

This 2019-modified, 2026-09-15-captured **Classic Adyen for Platforms** page describes a scheduled CSV snapshot of sub-merchants who **processed a payment or received a fund transfer within the last three months and have not completed KYC**. It directs new implementations to a separate new-integration guide. The report can help identify verification issues within that population; it is not a list of all incomplete-KYC sub-merchants or proof of a current account-holder status.

## Key takeaways

- The report is configured in Customer Area for **daily, weekly or monthly** generation, with a default subscription indicated on the page. Adyen recommends **notifications** for identifying these users because notifications are real time and can support quicker resolution. See raw lines 18–24.
- The column catalog includes Marketplace and Account Holder Code; country, UTC creation and next-deadline timestamps; entity type, processing tier and account status; a **Payment instrument code described here as a bank-account identifier**; Shareholder Code; and identity, company, bank-account and document verification statuses. A holder may have multiple bank accounts or shareholders; the page does not define row cardinality. See raw lines 26–43.
- The report describes processing tier values 0–3 and account statuses active, inactive, suspended or closed. The verification columns point to a separate guide for possible check values. These report fields do not themselves establish passed KYC, enabled payouts or live eligibility. See raw lines 35–43.

## Scope discrepancy

This report's **Entity type** column description says **Business or Individual** (raw line 34), while the related Classic [[source-adyen-docs-classic-platforms-account-holders-and-accounts|account-holder creation guide]] lists Individual, Business, Nonprofit, Partnership and Public company ([[raw/adyen/docs/classic-platforms/account-holders-and-accounts/2026-09-15|related raw lines 25–29]]). The captures do not explain whether additional types are omitted, grouped or represented differently in this report.

## Detail locators

- Population filter, schedule and notification preference: [[raw/adyen/docs/classic-platforms/kyc-action-required-snapshot-report/2026-09-15|raw lines 14–24]].
- Report columns, IDs, tier/status/deadline and KYC checks: [[raw/adyen/docs/classic-platforms/kyc-action-required-snapshot-report/2026-09-15|raw lines 26–43]].

## Related

- [[adyen-classic-platforms]] — Classic sub-merchant account and verification context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/kyc-action-required-snapshot-report/2026-09-15|KYC action required snapshot report (captured 2026-09-15)]]
