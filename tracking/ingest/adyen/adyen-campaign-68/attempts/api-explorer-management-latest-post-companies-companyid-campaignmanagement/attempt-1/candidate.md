---
title: "Adyen Management API: create a Giving campaign"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/campaignManagement"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/campaignManagement/2026-11-07.md"
tags: [adyen, management-api, giving, donation-campaigns]
---

## Overview

This captured [[adyen]] Management API `latest` reference documents `POST /companies/{companyId}/campaignManagement` on the v3 test server. It creates a Giving campaign to offer shoppers a donation to a nonprofit during a payment, for online, in-person, or both channels. It is campaign creation, not a donation transaction. See [[adyen-giving]].

## Key takeaways

- Required path `companyId` identifies the company account. The request body requires campaign `name` and `nonprofitCauseId`; `accountHolderIds`, `online`, and `inPerson` are optional. Company, account-holder, merchant-account, store, campaign, and nonprofit-cause identifiers have distinct roles. The API credential needs `Management API—Campaign Management read and write`.
- If in-person settings are supplied, `displayTextField` and `donationFlow` are marked required within that optional object. `presentCardTimeoutMs` is conditionally required for `twoStep`, defaults to 10000 ms, and ranges 5000–15000 ms; `promptTimeoutMs` has the same default and range. Each optional channel's `defaultAmount`, if used, requires a currency code and 1–3 minor-unit amounts.
- A `200` response says the request succeeded and requires an Adyen-generated campaign `id`, `name`, `nonprofitCause`, and `status`. Channel details, account-holder IDs, and activation/end timestamps are optional. The reference does not enumerate `status` values or establish that a newly created campaign is active, shown to a shopper, or has received donations.
- A documented `503` means campaign management is temporarily unavailable for the account; the reference specifically says donations themselves are unaffected. It does not state idempotency or a campaign-activation workflow.

## Detail locators

- `## Parameters` → path and request-body tables: identifier scopes, optional channel objects, conditional in-person fields, donation types, amounts, and timeouts.
- `## Responses` → `200 Success`: campaign ID, status, nonprofit cause, channel associations, amounts, and optional lifecycle timestamps.
- `## Responses` → `400`, `401`, `403`, `422`, `500`, and `503`: failure categories and optional error-envelope fields.

## Related

- [[adyen]]
- [[adyen-giving]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/campaignManagement/2026-11-07|Management API Giving campaign creation, captured 2026-11-07]]
