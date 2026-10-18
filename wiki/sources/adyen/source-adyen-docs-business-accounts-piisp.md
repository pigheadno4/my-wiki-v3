---
title: "Adyen Business Accounts PIISP funds confirmation"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/piisp"
raw_files:
  - "adyen/docs/business-accounts/piisp/2026-09-15.md"
tags: [adyen, business-accounts, open-banking, piisp, funds-confirmation]
---

## Overview

This 2026-09-15 Adyen Open Banking page addresses a third-party Payment Initiation Service Provider (PIISP) that checks whether an account holder who gave consent has enough available funds for a specified amount. It shows one `POST /funds-confirmations` request and its `fundsAvailable` response. This is an informational funds check, not a reservation, payment instruction, completed transfer, or beneficiary-bank receipt. See [[adyen]], [[adyen-business-accounts]] and [[source-adyen-docs-business-accounts-oauth-flow]] for the separate third-party token/consent route.

## Key takeaways

- The page is for third-party providers. It names prior Adyen onboarding and an access token for the Adyen business account as setup conditions; the introduction qualifies the service by account-holder consent. The sample sends a Bearer token, `X-Request-ID`, and an `IPv4` header, while the text permits an IPv4 or IPv6 address. It does not show a `Consent_Id` header or establish that token issuance alone proves current consent.
- The request body specifies `instructedAmount` (currency and amount) and `account` (the account number to check). Its TEST example asks about EUR 10.50 for a sample IBAN; the sample identity and `fundsAvailable: true` are illustrative, not evidence of any specific live account balance.
- `fundsAvailable` answers whether the **specified amount** is available at that check; `false` means insufficient funds for that amount. The response shown carries only that boolean. The guide does not describe a balance amount, hold, debit, guarantee of later availability, payment initiation or settlement. Follow the separate PISP route for payment initiation; do not infer it from this PIISP response.

## Detail locators

- Third-party PIISP purpose, account-holder consent and setup: raw lines 15–31.
- POST path, body fields, address/header example and TEST amount/account: lines 33–63.
- Boolean response and explicit false meaning: lines 65–73.
- AISP and PISP links are navigation to different services (lines 75–78).

## Related

- [[adyen-business-accounts]] — Business Accounts context.
- [[source-adyen-docs-business-accounts-oauth-flow]] — third-party token and consent setup.
- [[source-adyen-docs-business-accounts-aisp]] — distinct account-information access.
- [[source-adyen-docs-business-accounts-pisp]] — distinct payment-initiation flow.

## Raw Sources

- [[raw/adyen/docs/business-accounts/piisp/2026-09-15|Adyen Docs: Confirm funds availability (2026-09-15 snapshot)]]
