---
title: "Adyen Payout Service enterprise accounts"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/enterprise-accounts"
raw_files:
  - "adyen/docs/payouts/payout-service/enterprise-accounts/2026-09-15.md"
tags: [adyen, payout-service, enterprise-accounts, balance-accounts, transfers]
---

## Overview

This 2026-09-15 [[adyen]] Payout Service guide describes enterprise accounts as balance-account-connected resources with account identification details for receiving funds from third-party bank accounts and sending funds to third-party bank accounts or cards. It routes under [[adyen-payouts]] and also names Enterprise Issuing as an integration path. The introductory text says enterprise accounts can hold and manage “your funds and your customers' funds,” but the detailed flow on this page traces **the merchant's own sales proceeds** from merchant account to its connected enterprise balance account before third-party transfers; it does not allocate legal ownership of specific customer funds.

## Key takeaways

- Setup is through an Adyen contact. The page says a **Payouts or Enterprise Issuing integration** is required, Transfers API credential roles are needed for transfers, and Transfer plus Transaction webhooks should be subscribed to for status tracking. Some enterprise-account types require an EMI or PI license; the guide does not identify which types or establish any reader's license or eligibility. See raw lines 19–34.
- An enterprise account connects to a balance account and provides account identification such as account number or IBAN. The page describes incoming funds from third-party bank accounts and outgoing transfers to third-party bank accounts or cards. Account details are to be shared with third parties for incoming transfers; US, Netherlands and UK values are **sample formats**, not live destination instructions. See raw lines 36–41 and 58–84.
- For the illustrated merchant-proceeds flow, Adyen processes a customer's payment, credits the merchant account, then moves and settles proceeds in the balance account connected to the enterprise account. Only after that settlement does the guide describe using the funds for transfers and payouts. A payment processed or enterprise account set up is not proof of settled balance, transfer booking or beneficiary receipt. See raw lines 43–56.
- The page lists European Union (with a Dutch IBAN), United Kingdom and United States as supported locations in this 2026-09-15 snapshot. This list is historical documentation, not a current offer, country-level eligibility or approved enterprise-account opening. See raw lines 86–99.

## Evidence boundary

Keep the merchant's payment proceeds, the platform's balance-account resource and third-party sender/beneficiary distinct. The broad “customers' funds” statement does not define a specific fiduciary arrangement, legal owner, merchant of record or permitted account type. Licensing is conditional, and the page gives no application, verification or approval record for a particular entity. Transfer/Transaction webhook subscriptions are tracking setup, not evidence that a transfer occurred.

## Detail locators

- Purpose, setup and conditional licensing: raw lines 19–34.
- Account resource and merchant-proceeds money flow: raw lines 36–56.
- Incoming-transfer account-detail samples and regions: raw lines 58–99.

## Related

- [[adyen-payouts]]
- [[adyen-issuing]]
- [[source-adyen-docs-payouts-payout-service-account-structure-resources]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/enterprise-accounts/2026-09-15|Payout Service enterprise-accounts guide, 2026-09-15]]
