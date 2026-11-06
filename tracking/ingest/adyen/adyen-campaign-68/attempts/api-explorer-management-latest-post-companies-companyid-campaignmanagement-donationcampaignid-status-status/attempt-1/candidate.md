---
title: "Adyen Management API: Activate or end a donation campaign"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/campaignManagement/(donationCampaignId)/status/(status)"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/campaignManagement/(donationCampaignId)/status/(status)/2026-11-07.md"
tags: [adyen, management-api, giving, donation-campaign]
---

## Overview

This 2026-11-07-captured Management API `latest` reference lists a TEST `/v3` server for `POST /companies/{companyId}/campaignManagement/{donationCampaignId}/status/{status}`. It starts or stops the specified donation campaign. [[adyen]] [[adyen-giving]]

## Key takeaways

- The required path IDs are `companyId` for the company account and `donationCampaignId` for the campaign. Required path `status` accepts `activate` to start an **inactive** campaign or `end` to stop an **active** campaign. The reference says other transitions are not allowed. It lists no request body or query parameters.
- The caller's API credential requires **Management API—Campaign Management read and write**.
- A `200` means this request succeeded and returns a campaign representation. `id`, `name`, `nonprofitCause`, and `status` are required in that response schema; account-holder IDs, activation/end timestamps, and online/in-person settings are optional. The response `status` is described as current status, without an enum in this page. Nested amount/currency fields have their own requirements if their optional parent amounts are present.
- The reference lists `400`, `401`, `403`, `422`, `500`, and `503` errors. For `503`, campaign management is temporarily unavailable for the account, while donations themselves are unaffected. A campaign status response does not prove that any shopper donated, a payment succeeded, or a nonprofit received funds.

## Detail locators

- Transition rule, role and TEST server: raw lines 5–15; required path parameters: lines 17–24.
- `200` campaign fields and channel settings: raw lines 26–68; error schemas: lines 71–182.

## Related

- [[adyen-giving]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/campaignManagement/(donationCampaignId)/status/(status)/2026-11-07|Activate or end donation campaign, captured 2026-11-07]]
