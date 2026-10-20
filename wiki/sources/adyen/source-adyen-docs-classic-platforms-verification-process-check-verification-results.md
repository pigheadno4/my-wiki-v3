---
title: "Adyen Classic Platforms verification results"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/verification-process/check-verification-results"
raw_files:
  - "adyen/docs/classic-platforms/verification-process/check-verification-results/2026-09-15.md"
tags: [adyen, classic-platforms, verification, account-holders, kyc]
---

## Overview

This 2021-modified page captured 2026-09-15 explains how a **Classic Adyen for Platforms** integration reads account-holder verification checks and decides whether a retry or more evidence is appropriate. It directs new implementations to a separate integration guide; its Classic Account API and notification fields should not be mapped onto the modern balance-platform capability model. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- Results are available through the `ACCOUNT_HOLDER_VERIFICATION` notification, POST `/getAccountHolder` with `accountHolderCode`, or the Customer Area KYC tab. The notification/API check data include verification `type`, `status`, a summary with code and description, and `requiredFields`; the Customer Area path requires the Merchant MarketPlace role. The examples show invalid data and are not a real account-holder result.
- The type catalog distinguishes company, identity, legal arrangement, nonprofit, passport, payout-method and PCI checks. `PAYOUT_METHOD_VERIFICATION` is described as starting with notification webhook version 6 and replacing earlier bank-account/card check types.
- Statuses matter per check: `AWAITING_DATA` calls for missing information, `DATA_PROVIDED` and `PENDING` do not call for an immediate retry, `INVALID_DATA` points to correction, and `RETRY_LIMIT_REACHED` permits retry only for some checks. The table describes `PASSED` as a completed check and `FAILED` as final, with account-holder suspension when a check fails. Do not treat a single sample check as proof of overall live eligibility, enabled payouts or completed payments.
- Retry guidance varies by subject. For identity or payout-method `INVALID_DATA`, ask for review/update; after the retry limit, the table calls for photo ID or bank statement respectively. For company/nonprofit `INVALID_DATA`, inspect the version-specific `kycCheckCode`: API v5+ points to the company-code list, while v4 or earlier singles out `1604`. For those matching codes, review name/registration data, offer a registration document when the holder believes them correct, and require that document after three attempts with those codes. The page says Adyen uses it for manual verification; submission alone is not approval.

## Detail locators

- Classic-only boundary and three result channels: raw lines 19–25. Notification fields and invalid-data example: raw lines 27–69. Customer Area role/navigation: lines 71–77. POST `/getAccountHolder` and verification response: lines 79–132.
- Verification types and v6 payout-method replacement: raw lines 134–144. Per-check statuses/actions, including final `FAILED`: lines 146–158.
- General retry caveat and subject-specific actions: raw lines 160–202. Identity/photo ID: 171–178; payout method/bank statement: 180–187; version-qualified company/nonprofit codes and registration-document escalation: 189–202.

## Related

- [[adyen]] — provider.
- [[adyen-classic-platforms]] — Classic platform/account-holder context.
- [[adyen-platforms]] — separate modern Platforms model.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/verification-process/check-verification-results/2026-09-15|Classic verification results — 2026-09-15 snapshot]]
