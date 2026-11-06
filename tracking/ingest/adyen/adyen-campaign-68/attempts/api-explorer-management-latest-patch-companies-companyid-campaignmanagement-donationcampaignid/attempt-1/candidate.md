---
title: "Update a company donation campaign (Adyen Management API)"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/campaignManagement/(donationCampaignId)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/companies/(companyId)/campaignManagement/(donationCampaignId)/2026-11-07.md"
tags: [adyen, management-api, giving, donation-campaigns]
---

## Overview

This 2026-11-07 Management API `latest` reference documents `PATCH /companies/{companyId}/campaignManagement/{donationCampaignId}` to update properties of the identified donation campaign under a company account. The listed server is Test `/v3`. The API credential needs `Management API—Campaign Management read and write`.

## Key takeaways

- The required path values are the company-account ID and Adyen donation-campaign ID. The body table marks `accountHolderIds` (array or null), `inPerson`, `name` and `online` optional. It does not define nested request-body fields or a default for them; response fields should not be treated as required PATCH inputs.
- This PATCH cannot update campaign status. The reference directs activation and ending to a separate POST status endpoint. Adding account holders incompatible with the nonprofit causes a validation error. An optional `accountHolderIds` value does not itself establish nonprofit eligibility.
- `200` success returns a donation-campaign schema: required `id`, `name`, `nonprofitCause` and `status`, with optional account-holder IDs, activation/end timestamps and channel settings. Returned status/timestamps are readback, not evidence that this PATCH activated or ended the campaign. No donation transaction, webhook outcome, settlement or bank receipt is established by a campaign-properties update.
- The documented `503` means campaign management is temporarily unavailable for the account, while donations themselves are unaffected. Other listed failures are `400`, `401`, `403`, `422` and `500`.

## Detail locators

- Raw lines 5–35: property-update purpose, status restriction, incompatible-account-holder validation, credential role, Test server, path IDs and four optional body fields.
- Raw lines 37–79: `200` response schema, optional lifecycle timestamps and online/in-person settings. Nested fixed-donation amount limits and units appear only in the response schema at lines 50–52 and 72–74.
- Raw lines 82–193: error status and optional error-body fields, including the consequential `503` statement at lines 177–178.

## Related

- [[adyen]]
- [[adyen-giving]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/campaignManagement/(donationCampaignId)/2026-11-07|PATCH company donation campaign, 2026-11-07 capture]]
