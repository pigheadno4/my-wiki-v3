---
title: "Adyen Capital API v1 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital/latest/overview"
raw_files:
  - "adyen/api-explorer/capital/latest/overview/2026-09-15.md"
tags: [adyen, capital, platforms, api-explorer]
---

## Overview

This 2026-09-15 API Explorer snapshot is headed **Capital API v1**. It presents endpoints for embedding Adyen Capital into a marketplace or platform: finding available financing offers, requesting a grant on a user's behalf after offer selection, and reading grant-account information. It describes a grant as business financing repaid over a specified term with a fee. An offer, grant request, grant account, disbursement, and repayment are separate records or steps; this endpoint directory does not establish that a particular user was approved or funded. [[adyen]] [[adyen-capital]]

## Key takeaways

- Adyen configures offer amounts or ranges, fees and repayment conditions based on its proactive risk analyses of users. The overview distinguishes dynamic offers, preliminary calculations, converting a selected dynamic amount into a static offer, static-offer listing/details, grant requests/details, grant-account reads, and grant-disbursement reads or repayment-configuration updates. Consult each operation reference for its parameters and result semantics.
- Each Capital API request requires an API key in `X-API-Key`. The API credential must have `Balance_Platform_Capital_Configuration_Role` and `Balance_Platform_Capital_Grant_Initiation_Role`; the page directs readers to an Adyen contact to set up those roles. Going live requires a key generated in the live Customer Area. Listed v1 servers are `https://balanceplatform-api-test.adyen.com/capital/v1` and `https://balanceplatform-api-live.adyen.com/capital/v1`.
- The twelve listed routes are a catalog, not an operation contract or proof of an available offer, an accepted grant, a disbursement, funding receipt, or repayment.

## Detail locators

- Product purpose and offer/grant/grant-account distinction: raw lines 5–15.
- API-key header, roles, live-key rule and v1 server addresses: raw lines 17–48.
- Twelve GET/POST/PATCH routes and summaries: raw `## Endpoints` → `### General`, lines 50–66.

## Related

- [[adyen-capital]] — Capital product and offer/grant lifecycle context.
- [[adyen-platforms]] — marketplace/platform integration context.

## Raw Sources

- [[raw/adyen/api-explorer/capital/latest/overview/2026-09-15|Capital API v1 overview (2026-09-15)]]
