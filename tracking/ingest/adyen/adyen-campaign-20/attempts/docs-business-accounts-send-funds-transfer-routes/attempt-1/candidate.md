---
title: "Adyen Business Accounts transfer routes"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/send-funds/transfer-routes"
raw_files:
  - "adyen/docs/business-accounts/send-funds/transfer-routes/2026-09-15.md"
tags: [adyen, business-accounts, transfer-routes, bank-transfers]
---

## Overview

This Adyen Business Accounts route-calculation guide (last modified 2023-03-13; captured 2026-09-15) describes a pre-transfer check for sending funds to a third-party bank account. Banks or regulators can constrain priorities or amounts, so Adyen recommends calculating routes for a new recipient before requesting a transfer. The result lists routes and conditions for the supplied query; it is not a transfer request, live eligibility guarantee or proof of beneficiary-bank receipt. See [[adyen]] and [[adyen-business-accounts]].

## Key takeaways

- The stated integration prerequisite is Adyen for Platforms with Business Accounts support. The Configuration API credential needs **Balance Platform BCL role**. These are documented requirements, not evidence that a particular credential is enabled.
- Call `POST /transferRoutes/calculate` with `balancePlatform`, `currency` and `category: bank`. In **country/region mode**, supply the counterparty's two-character country code. In **counterparty mode**, supply recipient bank-account details or a transfer instrument; `balanceAccountId` is conditionally required when `counterparty` contains `transferInstrumentId`. The request tables mark `priorities` optional.
- The `transferRoutes` response identifies supported currency and priority plus requirements for each returned route; the counterparty variant also identifies country. Example requirements cover amount minimum/maximum, address fields, bank-account identification type and payment-instrument type/issuing country. These must be evaluated for the actual returned route.
- The TEST examples use USD for an NL country query with `regular`, `crossBorder` and `wire` routes, and EUR for a named NL counterparty query with `instant` and `wire` routes. Those example combinations and numeric limits are not a current country/currency coverage table. The parent send-funds guide separately uses both cross-border and wire wording for cross-border requests; this route example alone does not resolve which priority to submit for a live transfer.

## Detail locators

- Purpose, bank/regulator constraints, recommendation and credential/integration requirements: pinned raw lines 15–30.
- Country/region request field table, including optional priorities: raw lines 36–50; TEST requests and SDK versions: lines 52–299; response and sample conditions: lines 301–357.
- Counterparty request table and conditional `balanceAccountId`: raw lines 359–374; TEST requests and SDK versions: lines 376–714; response and sample conditions: lines 716–780.
- The parent [[source-adyen-docs-business-accounts-send-funds]] contains historical destination and priority tables, with separate cross-border/wire wording and timing conflicts. Use a route response and current provider guidance for a concrete transfer; neither historical example proves availability now.

## Related

- [[adyen-business-accounts]] — Business Accounts product and account context.
- [[source-adyen-docs-business-accounts-send-funds-make-transfer-request]] — separate third-party bank transfer request flow.
- [[source-adyen-docs-platforms-custom-payouts-transfer-routes]] — similar Configuration API route calculation under the distinct Platforms custom-payout scope.

## Raw Sources

- [[raw/adyen/docs/business-accounts/send-funds/transfer-routes/2026-09-15|Adyen Docs: Business Accounts transfer routes (2026-09-15 snapshot)]]
