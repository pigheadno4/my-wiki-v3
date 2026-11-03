---
title: "Balance Platform API: Get an account holder tax form"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/accountHolders/(id)/taxForms"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/accountHolders/(id)/taxForms/2026-11-02.md"
tags: [adyen, balance-platform, tax-forms, api]
---

## Overview

This captured Balance Platform API v2 `GET /accountHolders/{id}/taxForms` reference describes generating a tax form for account holders operating in the US. The listed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`. It is an account-holder tax-document retrieval route, not a payment, tax calculation, tax-identifier verification, or proof of a financial outcome. [[adyen]] [[adyen-platforms]]

## Key takeaways

- The required path `id` is the account holder's unique identifier. Required query inputs are `year` (tax year in YYYY format) and `formType` (`US1099k` or `US1099nec`). Optional `legalEntityId` identifies the legal entity whose tax form is requested. The reference states no default, year range, pagination, or request body. See **Parameters** in the raw.
- A 200 response has required Base64 `content` and optional `contentType`; the listed possible content type is `application/pdf`. This response establishes that the request succeeded and form content was returned. It does not establish account eligibility, tax correctness, filing, payment authorization, booking, settlement, payout, or bank receipt. See **200 Success** under Responses and Response examples.
- The reference lists 400 request-reading/understanding error, 401 authentication required, 403 insufficient permissions, 404 tax form unavailable, 422 validation error, and 500 server failure. Their shared error schema and generic examples are in **Responses** and **Response examples**. The 422 and 500 examples mention payment instruments; those example details do not define tax-form behavior.
- This is a 2026-11-02 captured reference for the listed test server. The `latest` URL and a successful example do not establish a live base URL, current availability, caller permission, or availability of a particular form. The raw does not describe idempotency, form lifecycle or deletion, asynchronous propagation, reversals, or a version conflict.

## Detail locators

- **Parameters**, lines 12–25: path and query identity, requiredness, accepted form types.
- **Responses**, lines 27–156: success fields and error statuses/schema.
- **Response examples**, lines 158–247: illustrative success and generic errors.

## Related

- [[adyen-platforms]] — platform and account-holder context.
- [US tax forms for platforms](https://docs.adyen.com/platforms/us-tax-forms/) and [marketplaces](https://docs.adyen.com/marketplaces/us-tax-forms/) — further guidance linked by the captured reference; not independently used here.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/accountHolders/(id)/taxForms/2026-11-02|Captured Balance Platform API tax-form endpoint (2026-11-02)]]
