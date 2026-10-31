---
title: "Adyen Fund API v6 overview (Classic Platforms)"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Fund/latest/overview"
raw_files:
  - "adyen/api-explorer/Fund/latest/overview/2026-09-15.md"
tags: [adyen, classic-platforms, fund-api, api-overview]
---

## Overview

This 2026-09-15-captured **Fund API v6** overview is for the Classic Platforms integration. It describes managing funds in platform accounts, including account-to-account transfer, payout to an account holder, and account balance retrieval. It directs new implementations to a separate new-integration guide; its Classic `account holder` and `account` objects must not be conflated with newer balance-platform Transfers API resources. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The overview says an Adyen contact supplies an API credential and API key. It shows `X-API-Key` authentication or username/password basic authentication. For live access, it says to generate **new** web-service-user credentials; the listed server and sample URL are **test** `https://cal-test.adyen.com/cal/services/Fund/v6` (raw lines 13–40).
- The endpoint URL uses a version suffix `vXX`; the example and listed server are `v6`, despite `latest` in the canonical documentation route. This capture does not establish current live availability or credentials (raw lines 29–40).
- The General endpoint catalog lists eight POST operations: `/accountHolderBalance`, `/accountHolderTransactionList`, `/debitAccountHolder`, `/payoutAccountHolder`, `/refundFundsTransfer`, `/refundNotPaidOutTransfers`, `/setupBeneficiary`, and `/transferFunds`. The table supplies brief purposes only. It gives no request or response schema, role, status/error contract, asynchronous outcome, or execution proof for those operations; follow their operation references and relevant Classic guides for details (raw lines 42–54).

## Detail locators

- Classic-only scope, purpose, new-integration pointer: raw lines 5–11. Authentication and distinct live credentials: lines 13–29. Version suffix and test server: lines 31–40. Full endpoint catalog: lines 42–54.

## Related

- [[source-adyen-docs-classic-platforms-fund-transfer]] — Classic transfer/reversal prerequisites and webhook outcome route.
- [[adyen-platforms]] — separate newer balance-platform model.

## Raw Sources

- [[raw/adyen/api-explorer/Fund/latest/overview/2026-09-15|Fund API v6 overview, captured 2026-09-15]]
