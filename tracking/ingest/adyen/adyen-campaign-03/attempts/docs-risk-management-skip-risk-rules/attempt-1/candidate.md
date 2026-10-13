---
title: "Adyen skip risk rules"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/skip-risk-rules"
raw_files:
  - "adyen/docs/risk-management/skip-risk-rules/2026-09-15.md"
tags: [adyen, risk-management, risk-rules, checkout]
---

## Overview

This Adyen documentation snapshot explains how a payment request can skip risk-rule triggering for one transaction. It describes the effect on that transaction and the continuing use of its shopper attributes in ShopperDNA.

## Key takeaways

- Set the case-sensitive `riskdata.skipRisk` parameter to `true` inside the payment request's `additionalData` object to prevent risk rules from triggering for that transaction. The page gives this placement for Checkout `/sessions` and `/payments`, and Payment `/authorise`.
- The skipped transaction receives no risk score but is still processed. Skipping risk rules here should not be read as a statement that payment processing is skipped or that every other control is disabled.
- Related shopper attributes, such as `shopperEmail`, still enter ShopperDNA. Future payments with the same shopper attributes can trigger the relevant risk rules. The setting applies to the selected transaction, not a permanent exemption for that shopper.

## Detail locators

- Parameter placement and immediate effect: `raw/adyen/docs/risk-management/skip-risk-rules/2026-09-15.md:16-19`.
- Single-transaction scope, case sensitivity, and `/sessions` example: `raw/adyen/docs/risk-management/skip-risk-rules/2026-09-15.md:21-51`.
- `/payments` placement and example: `raw/adyen/docs/risk-management/skip-risk-rules/2026-09-15.md:53-82`.
- `/authorise` placement and example: `raw/adyen/docs/risk-management/skip-risk-rules/2026-09-15.md:84-113`.

## Related

- [[adyen]]
- [[adyen-risk-management]]

## Raw Sources

- [[raw/adyen/docs/risk-management/skip-risk-rules/2026-09-15|Adyen Docs — Skip risk rules (2026-09-15 snapshot)]]
