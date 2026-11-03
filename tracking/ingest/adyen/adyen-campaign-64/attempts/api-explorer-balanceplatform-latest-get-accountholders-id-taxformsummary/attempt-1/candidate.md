---
title: "Balance Platform API v2: Get account-holder tax form summary"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/accountHolders/(id)/taxFormSummary"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/accountHolders/(id)/taxFormSummary/2026-11-02.md"
tags: [adyen, balance-platform, tax-forms, account-holders, api]
---

## Overview

This 2026-11-02-captured Adyen Balance Platform API v2 reference describes `GET /accountHolders/{id}/taxFormSummary`, which returns a summary of tax forms for an account holder. Its displayed server is the TEST base `https://balanceplatform-api-test.adyen.com/bcl/v2`. The path `id` identifies the account holder; the required query parameter `formType` selects `US1099k` or `US1099nec`. [[adyen]] [[adyen-platforms]]

## Key takeaways

- A documented `200` response contains required `data`, an array of summary objects. Each object has a required `legalEntityId` and required `taxYears` array of integers. These identify the legal entity and tax years in which it has a tax form.
- This is a summary read. The returned data identifies legal entities and tax years for the selected form type; it does not itself provide a tax form, establish filing or delivery, or show tax calculation, payment, payout, or bank receipt. The captured page specifies no defaults, limits, caller role, idempotency behavior, lifecycle transition, asynchronous outcome, failure/reversal handling, or LIVE server.

## Detail locators

- Purpose and displayed server: raw lines 5–10.
- Required account-holder path identifier and `formType` query values: raw lines 12–23.
- `200` response schema and illustrative JSON: raw lines 25–60. The example values are illustrative, not a coverage guarantee.

## Related

- [[adyen-platforms]] — Adyen for Platforms concept.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/accountHolders/(id)/taxFormSummary/2026-11-02|Captured Balance Platform API tax form summary reference]]