---
title: "Adyen Management API: Delete an inactive donation campaign"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/delete/companies/(companyId)/campaignManagement/(donationCampaignId)"
raw_files:
  - "adyen/api-explorer/Management/latest/delete/companies/(companyId)/campaignManagement/(donationCampaignId)/2026-11-07.md"
tags: [adyen, management-api, giving, donation-campaigns]
---

## Overview

Captured Management API v3 reference for removing a donation campaign selected by `donationCampaignId` under company account `companyId`. The request is allowed only when the campaign status is **inactive**. See [[adyen]] and [[adyen-giving]].

## Key takeaways

- Both company-account ID and donation-campaign ID are required path identifiers. The reference lists no query parameters or request body.
- The API credential needs **Management API—Campaign Management read and write**. The captured server is `https://management-test.adyen.com/v3`.
- `204` means the request was successfully processed and returns no additional content. The reference does not state rollback behavior or an effect on past donation transactions.
- A documented `503` says campaign management is temporarily unavailable for the account and explicitly says donations themselves are unaffected.

## Detail locators

- Inactive-only deletion condition, credential role, server, required path IDs and success: raw lines 5–27.
- Documented 400, 401, 403, 422 and 500 errors and optional top-level error fields: raw lines 30–122.
- `503` availability condition, donation distinction and error schema: raw lines 125–141.

## Related

- [[adyen-giving]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/delete/companies/(companyId)/campaignManagement/(donationCampaignId)/2026-11-07|Management API v3 donation-campaign deletion reference]]
